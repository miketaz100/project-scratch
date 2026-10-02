"""scorer.py — the SP1 v3 host: state machine, path streaming, controls, logging, console.

Runs on the CB1 as a systemd service next to Klipper (see electronics.md §9).  It talks to
Klipper over the API socket, plans the block path (planner + checker), converts it to three
cable lengths (ik) and streams `G1 A B C F` lines, keeping <= 0.5 s queued.

SAFETY POSITION (red line 13): nothing here is credited as a barrier.  The hardware loop
(e-stop, hold-to-run K1, latch, helmet loop, watchdog) removes ACT-24 whatever this program
does.  This program (a) never sends motion unless rail-sense says the rail is up, (b) opens
the latch (M8P_OK low) on any trip, (c) feeds the Klipper heartbeat that keeps the watchdog
PWM alive, and (d) refuses to arm after a weld, a stuck valve, a lost reflexd, or a failed
index check.

Usage on the CB1:   python3 -m sp1v3.scorer --klippy /home/biqu/printer_data/comms/klippy.sock
Bench simulation:   python3 -m sp1v3.scorer --sim          (then: python3 -m sp1v3.scratchctl)
"""
from __future__ import annotations

import argparse
import json
import logging
import math
import os
import socket
import socketserver
import threading
import time
from dataclasses import dataclass, field

from . import checker
from . import limits as L
from .forcemodel import ForceModel
from .ik import CableComp, DishModel, Geometry, TendonIK
from .klipper import KlipperAPI, KlipperError, SimKlipper
from .planner import Planner, Settings

log = logging.getLogger("sp1v3.scorer")

CONFIG_PATH = os.path.expanduser("~/sp1v3/config.json")
LOG_DIR = os.path.expanduser("~/sp1v3/logs")
SCORER_SOCK = "/tmp/sp1-scorer.sock"      # reflexd -> scorer (status datagrams)
REFLEX_SOCK = "/tmp/sp1-reflexd.sock"     # scorer -> reflexd (planned path datagrams)

STATES = ("BOOT", "SELFTEST", "SAFE", "ARMING", "READY", "APPROACH", "PLAY", "REST",
          "STATION_WAIT", "RETRACT", "PAUSED", "FAULT")

BUTTONS = ("rail_sense", "k1_nc", "latch_q", "lever", "estop_ok", "loop_ok", "moved",
           "mode_pline", "mode_line", "mode_circle", "mode_mix")
LED = {"SAFE": (0, 0, 0.2), "ARMING": (0.3, 0.2, 0), "READY": (0, 0.3, 0), "APPROACH": (0, 0.6, 0.2),
       "PLAY": (0, 0.6, 0), "REST": (0, 0.4, 0), "STATION_WAIT": (0.5, 0.3, 0), "RETRACT": (0.3, 0.3, 0),
       "PAUSED": (0.2, 0.2, 0.2), "FAULT": (1, 0, 0)}


# ======================================================================================
# configuration (calibration values live here, not in code)
# ======================================================================================
DEFAULT_CONFIG = {
    "geometry": {"stop_radius": 48.0, "post_radius": 30.0, "stop_z": 0.0,
                 "stop_angles_deg": [90.0, 210.0, 330.0]},
    "dish_table": None,                   # [[r, rise, tilt_deg], ...] from the CAD C8 sweep
    "deadband_mm": [0.0, 0.0, 0.0],       # `cal deadband` (A3)
    "k_n_per_mm": [1.2, 1.2, 1.2],
    "index_pos": [0.0, 0.0, 0.0],         # cable coordinate where each drum Hall triggers (approach from +)
    "home_search_mm": 12.0,
    "home_speed": 5.0,
    "pretension_n": 1.5,
    "trim_tol_n": 0.3,
    "float_spring_n": L.FLOAT_SPRING_N,
    "rim_model": {},                      # ForceModel overrides from `cal rim`
    "bratio_duty_gain": 1.0,
    "stage_b": True,
    "wig_mode": False,                    # fault injection allowed only when true
    "geometry_audit": "fault",            # "fault" | "warn": tendon statics audit at boot (CONFLICTS E-C1)
    "tension_cal": [[32768, 0.0005], [32768, 0.0005], [32768, 0.0005]],   # reflexd, set at A3
}


def load_config(path=CONFIG_PATH):
    cfg = json.loads(json.dumps(DEFAULT_CONFIG))
    try:
        with open(path) as f:
            cfg.update(json.load(f))
    except FileNotFoundError:
        pass
    return cfg


def save_config(cfg, path=CONFIG_PATH):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(cfg, f, indent=2)


# ======================================================================================
# CSV logger (first field = letter; t in ms; settings code on every line)
# ======================================================================================
class CsvLog:
    def __init__(self, directory=LOG_DIR, echo=False):
        os.makedirs(directory, exist_ok=True)
        self.path = os.path.join(directory, time.strftime("sp1-%Y%m%d-%H%M%S.csv"))
        self.f = open(self.path, "a", buffering=1)
        self.t0 = time.monotonic()
        self.code = "------"
        self.echo = echo
        self.lock = threading.Lock()

    def __call__(self, letter, *fields):
        t = int((time.monotonic() - self.t0) * 1000)
        line = ",".join([letter, str(t), self.code] + [str(x) for x in fields])
        with self.lock:
            self.f.write(line + "\n")
        if self.echo or letter in "FE":
            log.info(line)


# ======================================================================================
# streamer: tokens -> G-code, throttled to <= 0.5 s queued
# ======================================================================================
class Streamer:
    def __init__(self, kl, ik: TendonIK, comp: CableComp, fm: ForceModel,
                 max_queue=0.5, chunk_s=0.1, plan_sink=None):
        self.kl, self.ik, self.comp, self.fm = kl, ik, comp, fm
        self.max_queue, self.chunk_s = max_queue, chunk_s
        self.plan_sink = plan_sink
        self.abort = threading.Event()
        self.l_last = [0.0, 0.0, 0.0]
        self.s_path = 0.0
        self.p_last = (0.0, 0.0)
        self.sent_end = time.monotonic()      # wall-clock estimate of when the queue drains
        self.ff = True

    def reset(self, l=(0.0, 0.0, 0.0), p=(0.0, 0.0), last_dir=-1):
        self.l_last = list(l)
        self.p_last = p
        self.s_path = 0.0
        self.comp.reset(last_dir)

    def queued(self):
        return max(0.0, self.sent_end - time.monotonic())

    def gcode_for(self, tok, pins_total=0.0, pins_on=False):
        """Returns [(duration_s, [lines], samples)] chunks of ~chunk_s."""
        chunks, cur, cur_t, cur_s = [], [], 0.0, []
        dwell = 0.0
        s = tok.samples
        # tokens must start where the block is: a jump here would be an unplanned move
        gap = math.hypot(s[0][1] - self.p_last[0], s[0][2] - self.p_last[1])
        if gap > 0.05:
            raise checker.PathRejected([checker.Violation("S1", 0, f"stream discontinuity {gap:.3f} mm")])
        for i in range(1, len(s)):
            t0, x0, y0 = s[i - 1]
            t1, x1, y1 = s[i]
            dt = t1 - t0
            self.s_path += math.hypot(x1 - x0, y1 - y0)
            dT = (0.0, 0.0, 0.0)
            if self.ff:
                v = ((x1 - x0) / dt, (y1 - y0) / dt) if dt > 0 else (0.0, 0.0)
                dT = self.ik.tension_change((x1, y1), self.fm.external((x1, y1), v, pins_total, pins_on))
            l = self.comp.apply(self.ik.ik((x1, y1)), self.s_path, dT)
            dmax = max(abs(l[k] - self.l_last[k]) for k in range(3))
            if dmax < 1e-4:
                dwell += dt
            else:
                if dwell >= 0.001:
                    cur.append(f"G4 P{dwell * 1000:.1f}")
                    cur_t += dwell
                    dwell = 0.0
                F = 60.0 * dmax / (dt + dwell)
                dwell = 0.0
                cur.append(f"G1 A{l[0]:.4f} B{l[1]:.4f} C{l[2]:.4f} F{F:.3f}")
                cur_t += dt
                self.l_last = l
            cur_s.append((x1, y1))
            if cur_t >= self.chunk_s:
                chunks.append((cur_t, cur, cur_s))
                cur, cur_t, cur_s = [], 0.0, []
        if dwell >= 0.001:
            cur.append(f"G4 P{dwell * 1000:.1f}")
            cur_t += dwell
        if cur:
            chunks.append((cur_t, cur, cur_s))
        self.p_last = s[-1][1:]
        return chunks

    def send(self, tok, pre=(), pins_total=0.0, pins_on=False):
        """Submit a token (blocking, throttled).  Returns False if aborted."""
        chunks = self.gcode_for(tok, pins_total, pins_on)
        first = True
        for dur, lines, pts in chunks:
            while self.queued() > self.max_queue:
                if self.abort.wait(0.01):
                    return False
            if self.abort.is_set():
                return False
            if first and pre:
                lines = list(pre) + lines
                first = False
            now = time.monotonic()
            start = max(self.sent_end, now + 0.25)        # Klipper starts ~0.25 s after an idle queue
            self.kl.script("\n".join(lines))
            self.sent_end = start + dur
            if self.plan_sink:
                self.plan_sink(start, dur, pts, pins_on, pins_total)
        return True


# ======================================================================================
# the scorer
# ======================================================================================
@dataclass
class Inputs:
    buttons: dict = field(default_factory=dict)
    knobs: dict = field(default_factory=lambda: {"speed": 50.0, "intensity": 30.0})
    kpa: dict = field(default_factory=lambda: {"rail": 0.0, "palm": 0.0, "line_a": 0.0, "line_b": 0.0})
    klippy: str = "startup"
    reflex_hb: float = 0.0
    reflex: dict = field(default_factory=dict)
    k1_nc_seen_closed: bool = False


class Scorer:
    def __init__(self, kl, cfg=None, logdir=LOG_DIR, sim=False):
        self.kl = kl
        self.sim = sim
        self.cfg = cfg or load_config()
        g = self.cfg["geometry"]
        dish = DishModel.from_table(self.cfg["dish_table"]) if self.cfg.get("dish_table") else DishModel()
        self.ik = TendonIK(Geometry(stop_radius=g["stop_radius"], post_radius=g["post_radius"],
                                    stop_z=g["stop_z"], stop_angles_deg=tuple(g["stop_angles_deg"]),
                                    dish=dish))
        self.comp = CableComp(b=tuple(self.cfg["deadband_mm"]), k=tuple(self.cfg["k_n_per_mm"]))
        self.fm = ForceModel(**self.cfg.get("rim_model", {}))
        self.settings = Settings(stage_b=self.cfg.get("stage_b", True),
                                 float_spring=self.cfg.get("float_spring_n", L.FLOAT_SPRING_N))
        self.planner = Planner(self.settings)
        self.inp = Inputs()
        self.state = "BOOT"
        self.fault_reason = ""
        self.log = CsvLog(logdir)
        self.streamer = Streamer(kl, self.ik, self.comp, self.fm, plan_sink=self._plan_to_reflexd)
        self.lock = threading.RLock()
        self.motion_thread = None
        self.session_t0 = None
        self.dwell_used = 0.0
        self.stay_used = False
        self.lever_t = None
        self.moved_t = None
        self.blind = {}
        self.blind_slot = None
        self._hb_n = 0
        self._stop = threading.Event()
        self._sock_rx = None
        self._sock_tx = None
        self._last_mode_btn = None
        self.homed = False

    # ------------------------------------------------------------------ plumbing
    def g(self, text, timeout=30.0):
        """Send g-code; any Klipper error in a safety-relevant command -> FAULT."""
        return self.kl.script(text, timeout=timeout)

    def set_state(self, new, why=""):
        with self.lock:
            if new == self.state:
                return
            old, self.state = self.state, new
            self.log("E", "state", old, new, why)
            log.info("state %s -> %s %s", old, new, why)
        try:
            r, gg, b = LED.get(new, (0, 0, 0))
            self.g(f"SET_LED LED=status RED={r} GREEN={gg} BLUE={b} SYNC=0")
        except Exception:
            pass

    def fault(self, reason):
        """Any trip: open the latch (M8P_OK low), stop streaming, stay until `reset` + lever re-press."""
        with self.lock:
            self.fault_reason = reason
            self.streamer.abort.set()
            self.log("F", reason)
            try:
                self.g("SET_PIN PIN=m8p_ok VALUE=0\nSET_PIN PIN=pin_a VALUE=0\nSET_PIN PIN=pin_b VALUE=0\n"
                       "SET_PIN PIN=palm VALUE=0\nSET_PIN PIN=rail_dump VALUE=0\nSET_PIN PIN=palm_dump VALUE=0\n"
                       "SET_HEATER_TEMPERATURE HEATER=rail TARGET=0\n"
                       "SET_HEATER_TEMPERATURE HEATER=palm TARGET=0\nM84", timeout=2.0)
            except Exception:
                pass
            self.set_state("FAULT", reason)

    def _settings_code(self):
        self.log.code = L.settings_code(self.settings.as_dict())
        self.log("C", json.dumps(self.settings.as_dict(), sort_keys=True))

    # ------------------------------------------------------------------ reflexd link
    def _open_sockets(self):
        try:
            os.unlink(SCORER_SOCK)
        except FileNotFoundError:
            pass
        self._sock_rx = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
        self._sock_rx.bind(SCORER_SOCK)
        self._sock_rx.settimeout(0.2)
        self._sock_tx = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
        threading.Thread(target=self._reflex_rx, daemon=True, name="reflex-rx").start()

    def _reflex_rx(self):
        while not self._stop.is_set():
            try:
                data = self._sock_rx.recv(65536)
            except socket.timeout:
                continue
            except OSError:
                break
            try:
                msg = json.loads(data)
            except ValueError:
                continue
            self.inp.reflex = msg
            self.inp.reflex_hb = time.monotonic()
            if msg.get("trip"):
                self.log("F", "reflex", msg.get("why", ""), msg.get("residual", ""))
            if msg.get("T") and msg.get("log_T"):
                self.log("T", *[f"{x:.3f}" for x in msg["T"]])

    def _plan_to_reflexd(self, start, dur, pts, pins_on, pins_total):
        if self._sock_tx is None:
            return
        msg = {"t0": start, "dur": dur, "pts": [(round(x, 3), round(y, 3)) for x, y in pts],
               "pins_on": pins_on, "F": pins_total}
        try:
            self._sock_tx.sendto(json.dumps(msg).encode(), REFLEX_SOCK)
        except OSError:
            pass

    def reflexd_alive(self):
        return self.sim or (time.monotonic() - self.inp.reflex_hb) < 0.5

    # ------------------------------------------------------------------ Klipper inputs
    def subscribe(self):
        objs = {"webhooks": ["state"], "toolhead": ["print_time", "estimated_print_time", "stalls"]}
        for b in BUTTONS:
            objs[f"gcode_button {b}"] = ["state"]
        for t in ("speed_knob", "intensity_knob", "line_a", "line_b"):
            objs[f"temperature_sensor {t}"] = ["temperature"]
        for h in ("rail", "palm"):
            objs[f"heater_generic {h}"] = ["temperature", "target"]
        self.kl.subscribe(objs, self._on_status)

    def _on_status(self, status, eventtime):
        for name, val in status.items():
            if name == "webhooks" and "state" in val:
                self.inp.klippy = val["state"]
                if val["state"] in ("shutdown", "error") and self.state not in ("BOOT", "FAULT"):
                    threading.Thread(target=self.fault, args=(f"klipper {val['state']}",), daemon=True).start()
            elif name.startswith("gcode_button") and "state" in val:
                b = name.split()[1]
                self.inp.buttons[b] = (val["state"] == "PRESSED")
                self.log("E", "button", b, val["state"])
            elif name.startswith("temperature_sensor") and "temperature" in val:
                n = name.split()[1]
                if n.endswith("_knob"):
                    self.inp.knobs[n[:-5]] = val["temperature"]
                else:
                    self.inp.kpa[n] = val["temperature"]
            elif name.startswith("heater_generic") and "temperature" in val:
                self.inp.kpa[name.split()[1]] = val["temperature"]

    def btn(self, name):
        return bool(self.inp.buttons.get(name, False))

    # ------------------------------------------------------------------ controls -> settings
    def apply_controls(self):
        s = self.settings
        sp = self.inp.knobs.get("speed", 50.0) / 100.0
        f = 0.6 + (1.4 - 0.6) * (sp / 0.5) if sp <= 0.5 else 1.4 + (2.0 - 1.4) * ((sp - 0.5) / 0.5)
        s.f = L.clamp("f", f)
        s.f_circle = L.clamp("f_circle", f)
        it = self.inp.knobs.get("intensity", 30.0) / 100.0
        lo, hi = (0.20, 0.45) if s.stage_b else (0.10, 0.50)
        s.force = L.clamp("force", lo + (hi - lo) * min(max(it, 0.0), 1.0))
        for m in ("pline", "line", "circle", "mix"):
            if self.btn(f"mode_{m}") and self._last_mode_btn != m:
                self._last_mode_btn = m
                s.mode = m
                self.log("E", "mode", m)
                self._settings_code()

    # ------------------------------------------------------------------ boot / selftest
    def selftest(self):
        self.set_state("SELFTEST")
        print(L.table())
        self.log("C", "limits", L.table().replace("\n", " | "))
        t0 = time.monotonic()
        while self.inp.klippy != "ready":
            if self.inp.klippy in ("shutdown", "error"):
                return self.fault(f"klipper {self.inp.klippy} at boot ('reset' restarts the firmware)")
            if time.monotonic() - t0 > 30:
                return self.fault("klipper not ready after 30 s")
            time.sleep(0.2)
        if self.btn("rail_sense"):
            return self.fault("rail present at boot (K1 welded or loop bypassed)")
        if not self.btn("k1_nc"):
            return self.fault("K1 NC contact open with coil off (weld / wiring)")
        self.inp.k1_nc_seen_closed = True
        # tendon statics: can the cables hold the block with tension inside the comparator window?
        a = self.ik.audit(self.fm, total=3 * self.cfg["pretension_n"])
        self.log("C", "tendon_audit", f"reach {a['reach_min']:.1f}", f"minT {a['min_T']:.2f}", f"maxT {a['max_T']:.2f}")
        if a["reach_min"] < L.D_MAX or a["min_T"] < 0.3 or a["max_T"] > 3.3:
            msg = (f"tendon geometry audit failed: positive-tension reach {a['reach_min']:.1f} mm, "
                   f"tension {a['min_T']:.2f}..{a['max_T']:.2f} N (need 16.5 mm, 0.3..3.3 N) - CONFLICTS E-C1")
            if self.cfg.get("geometry_audit", "fault") == "fault" and not self.sim:
                return self.fault(msg)
            log.warning(msg)
        # outputs to safe values (they have no supply anyway until K1 closes)
        self.g("SET_PIN PIN=pin_a VALUE=0\nSET_PIN PIN=pin_b VALUE=0\nSET_PIN PIN=palm VALUE=0\n"
               "SET_PIN PIN=rail_dump VALUE=0\nSET_PIN PIN=palm_dump VALUE=0\n"
               "SET_HEATER_TEMPERATURE HEATER=rail TARGET=0\nSET_HEATER_TEMPERATURE HEATER=palm TARGET=0")
        # start the watchdog PWM and the host heartbeat, then allow the latch to clear
        self.g("SET_PIN PIN=watchdog VALUE=0.5\nSP1_HEARTBEAT\nSET_PIN PIN=m8p_ok VALUE=1")
        self._settings_code()
        self.set_state("SAFE")

    # ------------------------------------------------------------------ heartbeat + supervision
    def _heartbeat(self):
        while not self._stop.is_set():
            try:
                if self.state != "FAULT":
                    self.kl.script("SP1_HEARTBEAT", timeout=1.0)
            except Exception:
                pass
            self._hb_n += 1
            if self._hb_n % 4 == 0:
                self.log("H", self.state, f"{self.inp.kpa['rail']:.1f}", f"{self.inp.kpa['palm']:.1f}",
                         f"{self.inp.kpa['line_a']:.1f}", f"{self.inp.kpa['line_b']:.1f}",
                         int(self.btn("rail_sense")), int(self.btn("latch_q")), int(self.reflexd_alive()),
                         f"{self.streamer.queued():.2f}")
            self._stop.wait(0.25)

    def supervise(self):
        """Fault detection that does not depend on the motion thread."""
        if not getattr(self.kl, "alive", True):
            # klippy restarted or died: the MCU is in shutdown or restarting, outputs are off.
            log.error("klippy API socket lost - exiting so systemd restarts the scorer")
            self.log("F", "klippy socket lost")
            os._exit(3)
        st = self.state
        if st in ("ARMING", "READY", "APPROACH", "PLAY", "REST", "STATION_WAIT", "RETRACT"):
            if not self.reflexd_alive():
                return self.fault("reflexd heartbeat lost")
            if self.btn("latch_q"):
                return self.fault("reflex latch tripped")
            if not self.btn("rail_sense"):
                return self.on_rail_lost()
            if self.btn("k1_nc"):
                return self.fault("K1 NC closed while rail present (relay fault)")
            # weld signature: rail still up although the lever (or the e-stop) is open
            if not self.btn("lever") or not self.btn("estop_ok"):
                self._weld_t = getattr(self, "_weld_t", None) or time.monotonic()
                if time.monotonic() - self._weld_t > 0.15:
                    return self.fault("RAIL UP WITH LEVER/E-STOP OPEN: K1 welded or loop bypassed - "
                                      "press the E-STOP (pole 2 cuts the rail)")
            else:
                self._weld_t = None
            # valve command/sensor mismatch: a line at rail pressure while commanded off
            if self.state in ("READY", "STATION_WAIT") and self.inp.kpa["line_a"] > 2.0:
                self._mismatch_t = getattr(self, "_mismatch_t", None) or time.monotonic()
                if time.monotonic() - self._mismatch_t > 0.5:
                    return self.fault("PIN A pressurised while commanded off (stuck valve)")
            else:
                self._mismatch_t = None
        if st in ("PLAY", "REST") and self.session_t0 and \
                time.monotonic() - self.session_t0 > L.clamp("session", 1200):
            self.log("E", "session cap 20 min")
            self.retract("session cap")
        if st in ("SAFE", "PAUSED") and not self.btn("rail_sense"):
            if not self.btn("k1_nc"):
                return self.fault("K1 NC open with the rail off (weld check)")
            self.inp.k1_nc_seen_closed = True
        if st in ("SAFE", "PAUSED") and self.btn("rail_sense"):
            if not self.inp.k1_nc_seen_closed:
                return self.fault("rail came up without a closed-NC proof (weld check)")
            self.inp.k1_nc_seen_closed = False
            self.arm()

    def on_rail_lost(self):
        """Hardware already vented everything.  Stop streaming; resume only through ARMING."""
        self.streamer.abort.set()
        self.homed = False
        self.log("E", "rail lost", "estop" if not self.btn("estop_ok") else
                 "lever" if not self.btn("lever") else "loop" if not self.btn("loop_ok") else "latch/watchdog")
        try:
            self.g("SET_PIN PIN=pin_a VALUE=0\nSET_PIN PIN=pin_b VALUE=0\nSET_PIN PIN=palm VALUE=0\n"
                   "SET_HEATER_TEMPERATURE HEATER=rail TARGET=0\nSET_HEATER_TEMPERATURE HEATER=palm TARGET=0",
                   timeout=2.0)
        except Exception:
            pass
        self.set_state("PAUSED", "rail lost")

    # ------------------------------------------------------------------ arming
    def home_drums(self):
        idx = self.cfg["index_pos"]
        srch = self.cfg["home_search_mm"]
        spd = self.cfg["home_speed"]
        lines = []
        for k, (name, ax) in enumerate((("cable_a", "A"), ("cable_b", "B"), ("cable_c", "C"))):
            lines += [f"MANUAL_STEPPER STEPPER={name} GCODE_AXIS=",
                      f"MANUAL_STEPPER STEPPER={name} ENABLE=1",
                      f"MANUAL_STEPPER STEPPER={name} SET_POSITION={idx[k] + srch:.3f}",
                      f"MANUAL_STEPPER STEPPER={name} SPEED={spd} MOVE={idx[k]:.3f} STOP_ON_ENDSTOP=home",
                      f"MANUAL_STEPPER STEPPER={name} SPEED={spd} MOVE=0"]
        for name, ax in (("cable_a", "A"), ("cable_b", "B"), ("cable_c", "C")):
            lines.append(f"MANUAL_STEPPER STEPPER={name} GCODE_AXIS={ax} LIMIT_VELOCITY=250 LIMIT_ACCEL=100000000")
        lines.append("G90")
        self.g("\n".join(lines), timeout=60.0)
        self.streamer.reset((0.0, 0.0, 0.0), (0.0, 0.0), last_dir=-1)
        self.planner.st.pos = (0.0, 0.0)
        self.homed = True

    def index_check(self):
        """Two-point window check: index_pos - 0.3 must read TRIGGERED, index_pos + 0.3 must not."""
        if self.sim:
            return True
        idx = self.cfg["index_pos"]
        ok = True
        for k, (name, ax) in enumerate((("cable_a", "A"), ("cable_b", "B"), ("cable_c", "C"))):
            for off, want in ((-0.3, True), (+0.3, False)):
                self.g(f"G1 {ax}{idx[k] + off:.3f} F300\nM400\nQUERY_ENDSTOPS")
                q = self.kl.query({"query_endstops": ["last_query"]})["query_endstops"]["last_query"]
                got = bool(q.get(f"manual_stepper {name}", False))
                if got != want:
                    self.log("F", "index", name, off, got)
                    ok = False
            self.g(f"G1 {ax}0 F300\nM400")
        return ok

    def arm(self):
        self.set_state("ARMING")
        try:
            if not self.reflexd_alive():
                return self.fault("reflexd not running")
            # dumps closed, lines vented, pumps charge rail and palm (palm valve off = float retracted)
            f = self.planner.force_setting(self.settings.force, "AB", 1.0)
            self.g("SET_PIN PIN=pin_a VALUE=0\nSET_PIN PIN=pin_b VALUE=0\nSET_PIN PIN=palm VALUE=0\n"
                   "SET_PIN PIN=rail_dump VALUE=1\nSET_PIN PIN=palm_dump VALUE=1\n"
                   f"SET_HEATER_TEMPERATURE HEATER=rail TARGET={L.rail_for_force(0.10):.2f}\n"
                   f"SET_HEATER_TEMPERATURE HEATER=palm TARGET={f['palm']:.2f}")
            self.home_drums()
            # tension trim check with the block centred (reflexd reports tensions)
            T = self.inp.reflex.get("T")
            if T and not self.sim:
                pt, tol = self.cfg["pretension_n"], self.cfg["trim_tol_n"]
                if any(abs(t - pt) > tol for t in T):
                    return self.fault(f"tension trim out of band {T}")
            tok = self.planner.to_rim(-90.0)
            self.streamer.abort.clear()
            self.streamer.send(tok)
            self.set_state("READY")
        except KlipperError as ex:
            self.fault(f"arming: {ex}")

    # ------------------------------------------------------------------ approach / play
    def approach(self):
        self.set_state("APPROACH")
        self.streamer.abort.clear()
        try:
            f = self.planner.force_setting(L.clamp("approach_F", 0.10), "AB", 1.0)
            self.g("SET_PIN PIN=palm VALUE=1")              # float extends to skid contact
            time.sleep(0.6)
            self.g(f"SET_HEATER_TEMPERATURE HEATER=rail TARGET={f['rail']:.2f}")
            self.planner.st.ramp_left = 3
            if self.session_t0 is None:
                self.session_t0 = time.monotonic()
            self.set_state("PLAY")
            self.motion_thread = threading.Thread(target=self._play_loop, daemon=True, name="play")
            self.motion_thread.start()
        except KlipperError as ex:
            self.fault(f"approach: {ex}")

    def _valve_lines(self, tok, cur):
        out = []
        for _, name, val in tok.events:
            if name == "groups":
                a = 1 if "A" in val else 0
                out.append(f"SET_PIN PIN=pin_a VALUE={a}")
                cur["groups"] = val
            if name == "bratio":
                b = 0.0
                if "B" in cur.get("groups", ""):
                    b = 1.0 if val >= 0.98 else min(1.0, max(0.3, val * self.cfg["bratio_duty_gain"]))
                out.append(f"SET_PIN PIN=pin_b VALUE={b:.3f}")
        fz = tok.force or {}
        if fz and abs(fz.get("rail", 0) - cur.get("rail", -99)) > 0.2:
            out.append(f"SET_HEATER_TEMPERATURE HEATER=rail TARGET={fz['rail']:.2f}")
            cur["rail"] = fz["rail"]
        if fz and abs(fz.get("palm", 0) - cur.get("palm", -99)) > 0.2:
            out.append(f"SET_HEATER_TEMPERATURE HEATER=palm TARGET={fz['palm']:.2f}")
            cur["palm"] = fz["palm"]
        return out

    def _play_loop(self):
        cur = {}
        try:
            while self.state in ("PLAY", "REST") and not self.streamer.abort.is_set():
                if self.state == "REST":                     # parked on the rim, nails up by geometry
                    if not self.streamer.send(self.planner.park_token(L.clamp("rest_s", 0.5))):
                        return
                    continue
                self.apply_controls()
                toks = self.planner.next_tokens(approach_force=L.clamp("approach_F", 0.10))
                if self.planner.st.rejections >= 3:
                    return self.fault("path checker rejected 3 plans in a row")
                for tok in toks:
                    if tok.kind not in ("park", "retracted"):
                        checker.assert_ok(tok)               # belt and braces: never stream unchecked
                    pre = self._valve_lines(tok, cur)
                    pins_on = bool(cur.get("groups"))
                    ptot = L.pins_total(cur.get("rail", 0.0), cur.get("groups", ""), 1.0)
                    if not self.streamer.send(tok, pre=pre, pins_total=ptot, pins_on=pins_on):
                        return
                    self.log("B", self.planner.st.phrase_mode if self.settings.mode == "mix" else self.settings.mode,
                             tok.kind, f"{tok.params.get('psi', '')}", f"{tok.params.get('e', '')}",
                             f"{tok.params.get('f', '')}", cur.get("groups", ""), f"{cur.get('rail', 0):.1f}",
                             f"{self.inp.reflex.get('peak', '')}")
                # station dwell timer (contact-seconds)
                if self.planner.st.contact_s - self.dwell_used >= self.settings.dwell * (1.5 if self.stay_used else 1.0):
                    return self.station_wait()
        except checker.PathRejected as ex:
            self.fault(f"checker: {ex}")
        except KlipperError as ex:
            if self.state not in ("PAUSED", "FAULT"):
                self.fault(f"stream: {ex}")

    def station_wait(self):
        self.g("SET_PIN PIN=pin_a VALUE=0\nSET_PIN PIN=pin_b VALUE=0\nSET_PIN PIN=chime VALUE=1\n"
               "G4 P300\nSET_PIN PIN=chime VALUE=0")
        self.planner.st.groups = ""
        self.set_state("STATION_WAIT", "dwell timer")

    def moved(self, held_s=0.0):
        self.log("E", "MOVED", f"{held_s:.1f}")
        if held_s >= 2.0 and not self.stay_used:
            self.stay_used = True                       # STAY: one 50 % extension
        else:
            self.dwell_used = self.planner.st.contact_s
            self.stay_used = False
        if self.state == "STATION_WAIT":
            self.approach()

    def retract(self, why="stop"):
        self.streamer.abort.set()
        if self.motion_thread and self.motion_thread is not threading.current_thread():
            self.motion_thread.join(timeout=2.0)
        self.set_state("RETRACT", why)
        try:
            self.g("SET_PIN PIN=pin_a VALUE=0\nSET_PIN PIN=pin_b VALUE=0\nSET_PIN PIN=palm VALUE=0")
            self.planner.st.groups = ""
            time.sleep(0.3)                                  # float retracts (QEV <= 150 ms)
            self.streamer.abort.clear()
            self.streamer.send(self.planner.to_point((0.0, 0.0)))
            time.sleep(self.streamer.queued() + 0.3)
            if not self.index_check():
                return self.fault("drum index error > 0.3 mm")
            self.streamer.reset((0.0, 0.0, 0.0), (0.0, 0.0), last_dir=-1)
            self.planner.st.pos = (0.0, 0.0)
            self.streamer.send(self.planner.to_rim(-90.0))
            self.set_state("READY", why)
        except KlipperError as ex:
            self.fault(f"retract: {ex}")

    # ------------------------------------------------------------------ main loop
    def run(self):
        self._open_sockets()
        self.subscribe()
        threading.Thread(target=self._heartbeat, daemon=True, name="hb").start()
        self.selftest()
        lever_prev = False
        moved_prev = False
        while not self._stop.is_set():
            try:
                self.supervise()
                lever = self.btn("lever")
                if lever and not lever_prev:
                    self.lever_t = time.monotonic()
                if self.state == "READY" and lever and self.lever_t and time.monotonic() - self.lever_t >= 1.0:
                    self.lever_t = None
                    self.approach()
                lever_prev = lever
                mv = self.btn("moved")
                if mv and not moved_prev:
                    self.moved_t = time.monotonic()
                if not mv and moved_prev and self.moved_t:
                    self.moved(time.monotonic() - self.moved_t)
                moved_prev = mv
                if self.state in ("READY", "PLAY", "REST", "STATION_WAIT"):
                    self.apply_controls()
            except Exception as ex:          # never die silently: fault and keep supervising
                log.exception("main loop")
                if self.state != "FAULT":
                    self.fault(f"exception {ex!r}")
            self._stop.wait(0.05)

    # ------------------------------------------------------------------ console commands
    def command(self, line: str) -> str:
        parts = line.strip().split()
        if not parts:
            return ""
        c, a = parts[0].lower(), parts[1:]
        s = self.settings
        self.log("E", "cmd", line.strip())
        try:
            if c == "status":
                return (f"state {self.state} {self.fault_reason}\nmode {s.mode} f {s.f:.2f} force {s.force:.2f} N "
                        f"groups {s.groups} vary {s.vary}\nrail {self.inp.kpa['rail']:.1f} palm {self.inp.kpa['palm']:.1f} "
                        f"A {self.inp.kpa['line_a']:.1f} B {self.inp.kpa['line_b']:.1f} kPa\n"
                        f"buttons {self.inp.buttons}\nreflexd {'ok' if self.reflexd_alive() else 'LOST'} "
                        f"{self.inp.reflex.get('T', '')}\ncontact {self.planner.st.contact_s:.0f} s, "
                        f"dwell used {self.dwell_used:.0f} s, queue {self.streamer.queued():.2f} s, "
                        f"code {self.log.code}")
            if c == "limits":
                return L.table()
            if c == "stop":
                self.retract("stop")
                return "ok"
            if c == "retract":
                self.retract("retract")
                return "ok"
            if c == "rest":
                self.set_state("REST")
                return "ok (REST until 'play')"
            if c == "play":
                if self.state == "REST":
                    self.set_state("PLAY")
                return "ok"
            if c == "arm":
                return "arming is by holding the lever (hardware); nothing to do"
            if c == "reset":
                if self.state != "FAULT":
                    return "not in FAULT"
                if self.btn("rail_sense"):
                    return "release the lever first (resets the latch), then 'reset'"
                if self.inp.klippy != "ready":          # e.g. after the host watchdog's M112
                    # FIRMWARE_RESTART also restarts klippy's API socket: restart ourselves too
                    # (systemd Restart=on-failure brings the scorer back and it re-runs SELFTEST)
                    self.log("E", "reset", "firmware_restart + scorer restart")
                    try:
                        self.kl.request("gcode/firmware_restart", timeout=2.0)
                    except Exception:
                        pass
                    threading.Timer(0.5, lambda: os._exit(3)).start()
                    return "Klipper firmware restart requested; scorer restarts in a few s (reconnect)."
                self.fault_reason = ""
                self.streamer.abort.clear()
                self.selftest()
                if self.state == "SAFE":
                    return "ok: SAFE. Count the nails (6?) before pressing the lever."
                return f"still {self.state}: {self.fault_reason}"
            if c == "mode":
                s.mode = {"pline": "pline", "line": "line", "circle": "circle", "mix": "mix"}[a[0]]
            elif c in ("f", "amp", "dpsi", "psi", "r", "e"):
                key = {"r": "R"}.get(c, c)
                setattr(s, key, L.clamp(key, float(a[0])))
                if c == "f":
                    s.f_circle = L.clamp("f_circle", float(a[0]))
            elif c == "chord":
                s.chord = a[0] == "on"
            elif c == "dpath":
                s.mode = "dpath"
            elif c == "park":
                self.set_state("REST")
            elif c == "force":
                s.force = L.clamp("force", float(a[0]))
            elif c == "sf":
                s.sF = L.clamp("sF", float(a[0]))
            elif c == "groups":
                s.groups = a[0] if a[0] in ("a", "b", "ab", "auto") else s.groups
            elif c == "bratio":
                s.bratio = L.clamp("bratio", float(a[0]))
            elif c == "palm":
                s.palm = "auto" if a[0] == "auto" else L.clamp("palm", float(a[0]))
            elif c == "vary":
                s.vary = a[0] == "on"
                self.planner.var.enabled = s.vary
            elif c == "seed":
                s.seed = int(a[0])
                self.planner.var.seed(s.seed)
            elif c == "dwell":
                s.dwell = L.clamp("dwell", float(a[0]))
            elif c == "bset":
                self.blind[a[0]] = json.loads(" ".join(a[1:]))
                return f"slot {a[0]} stored"
            elif c == "blind":
                self.blind_slot = a[0]
                for k, v in self.blind[a[0]].items():
                    setattr(s, k, v)
                self._settings_code()
                return "ok (settings hidden; code logged)"
            elif c == "reveal":
                return json.dumps({"slot": self.blind_slot, "settings": self.blind.get(self.blind_slot)})
            elif c == "rate":
                self.log("S", "rating", self.blind_slot or "-", float(a[0]))
                return "rating logged"
            elif c == "cal":
                return self.calibrate(a)
            elif c in ("valve", "pump", "sensors", "tensions"):
                return self.diag(c, a)
            elif c == "inject":
                if not self.cfg.get("wig_mode"):
                    return "refused: fault injection only with wig_mode=true in config.json (wig head)"
                return self.inject(a[0])
            elif c == "sim" and self.sim:
                return self.sim_input(a)
            elif c == "help":
                return ("status limits arm play rest stop retract reset | mode f amp dpsi psi R e chord dpath park | "
                        "force sF groups bratio palm | vary seed dwell | cal drums|deadband|rim|lines | "
                        "bset blind next reveal rate | valve pump sensors tensions | inject")
            else:
                return f"unknown command '{c}' (help)"
            self._settings_code()
            return "ok"
        except (IndexError, ValueError, KeyError) as ex:
            return f"error: {ex!r}"

    def calibrate(self, a):
        if self.state not in ("SAFE", "READY"):
            return "calibration only in SAFE/READY with the pad retracted"
        what = a[0] if a else ""
        if what == "drums":
            if self.state != "READY":
                return "hold the lever (READY) so the drums have power"
            self.home_drums()
            return "homed; index check " + ("PASS" if self.index_check() else "FAIL")
        if what == "deadband":
            return ("procedure (A3): with the ink pen on the block, run `cal deadband` sweeps per cable; "
                    "enter b_i (mm) in ~/sp1v3/config.json deadband_mm, then restart scorer")
        if what == "rim":
            return ("procedure: pad retracted, PLINE 60 s no contact; reflexd logs residual vs |d|; "
                    "fit rim_inner_n/rim_outer_n into config.json rim_model")
        if what == "lines":
            return "procedure (A2): valve a 200 / valve b 200 with the scope on the gallery tee; vent <= 100 ms"
        return "cal drums|deadband|rim|lines"

    def diag(self, c, a):
        if self.state not in ("SAFE", "READY"):
            return "diagnostics only with the pad retracted (SAFE/READY)"
        if c == "sensors":
            return json.dumps(self.inp.kpa)
        if c == "tensions":
            return json.dumps(self.inp.reflex.get("T"))
        if c == "valve":
            pin = {"a": "pin_a", "b": "pin_b", "palm": "palm"}[a[0]]
            ms = min(2000.0, float(a[1]))
            self.g(f"SET_PIN PIN={pin} VALUE=1\nG4 P{ms:.0f}\nSET_PIN PIN={pin} VALUE=0")
            return "ok"
        if c == "pump":
            h = {"1": "rail", "3": "palm"}[a[0]]
            tgt = min(float(a[1]), L.RAIL_MAX_KPA if h == "rail" else L.PALM_MAX_KPA)
            self.g(f"SET_HEATER_TEMPERATURE HEATER={h} TARGET={tgt:.1f}")
            return f"{h} target {tgt:.1f} kPa"
        return "?"

    def sim_input(self, a):
        """Bench simulation only: `sim lever 1`, `sim estop 0`, `sim moved 1`, `sim mode circle`,
        `sim knob speed 70`.  The simulated safety chain sets rail_sense / k1_nc like the hardware."""
        kl = self.kl
        if a[0] == "knob":
            kl.push({f"temperature_sensor {a[1]}_knob": {"temperature": float(a[2])}})
            return "ok"
        if a[0] == "mode":
            st = {f"gcode_button mode_{m}": {"state": "PRESSED" if m == a[1] else "RELEASED"}
                  for m in ("pline", "line", "circle", "mix")}
            kl.push(st)
            return "ok"
        name = {"lever": "lever", "estop": "estop_ok", "loop": "loop_ok", "moved": "moved",
                "latch": "latch_q"}[a[0]]
        kl.buttons[f"gcode_button {name}"] = a[1] == "1"
        chain = (kl.buttons.get("gcode_button lever") and kl.buttons.get("gcode_button estop_ok")
                 and kl.buttons.get("gcode_button loop_ok") and not kl.buttons.get("gcode_button latch_q"))
        kl.buttons["gcode_button rail_sense"] = bool(chain)
        kl.buttons["gcode_button k1_nc"] = not chain
        kl.push({f"gcode_button {n}": {"state": "PRESSED" if kl.buttons.get(f"gcode_button {n}") else "RELEASED"}
                 for n in ("lever", "estop_ok", "loop_ok", "moved", "latch_q", "rail_sense", "k1_nc")})
        return f"ok rail={'up' if chain else 'down'}"

    def inject(self, what):
        self.log("E", "inject", what)
        if what == "snag":
            return "pull the wig tether now; expect latch trip <= 50 ms"
        if what == "hang":
            self._stop.set()             # stop heartbeat: Klipper's SP1 host watchdog must M112 in ~1 s
            return "scorer heartbeat stopped; expect watchdog -> rail open within ~1.1 s"
        if what == "stuckvalve":
            self.g("SET_PIN PIN=pin_a VALUE=1")
            return "PIN A forced on while READY: expect FAULT in 0.5 s"
        if what == "cable":
            return "unhook one cable at the drum: expect tension-pattern trip"
        return "inject snag|hang|cable|stuckvalve"


# ======================================================================================
# console server (TCP, line based) for scratchctl
# ======================================================================================
class _Handler(socketserver.StreamRequestHandler):
    def handle(self):
        for raw in self.rfile:
            line = raw.decode(errors="replace").strip()
            if not line:
                continue
            reply = self.server.scorer.command(line)
            self.wfile.write((reply + "\n.\n").encode())


def serve_console(scorer, host="127.0.0.1", port=7700):
    srv = socketserver.ThreadingTCPServer((host, port), _Handler)
    srv.daemon_threads = True
    srv.scorer = scorer
    threading.Thread(target=srv.serve_forever, daemon=True, name="console").start()
    return srv


def main(argv=None):
    ap = argparse.ArgumentParser(description="SP1 v3 scorer")
    ap.add_argument("--klippy", default="/home/biqu/printer_data/comms/klippy.sock")
    ap.add_argument("--sim", action="store_true", help="run against the built-in Klipper simulator")
    ap.add_argument("--listen", default="127.0.0.1", help="console bind address (0.0.0.0 for the PC)")
    ap.add_argument("--port", type=int, default=7700)
    ap.add_argument("--logdir", default=LOG_DIR)
    ap.add_argument("-v", action="store_true")
    args = ap.parse_args(argv)
    logging.basicConfig(level=logging.DEBUG if args.v else logging.INFO,
                        format="%(asctime)s %(name)s %(levelname)s %(message)s")
    if args.sim:
        kl = SimKlipper()
        kl.buttons.update({"gcode_button k1_nc": True, "gcode_button estop_ok": True,
                           "gcode_button loop_ok": True})
    else:
        kl = KlipperAPI(args.klippy)
        for _ in range(60):                 # klippy may still be (re)starting
            try:
                kl.connect()
                break
            except OSError:
                time.sleep(1.0)
        else:
            raise SystemExit("cannot connect to klippy API socket " + args.klippy)
    sc = Scorer(kl, load_config(), args.logdir, sim=args.sim)
    serve_console(sc, args.listen, args.port)
    sc.run()


if __name__ == "__main__":
    main()
