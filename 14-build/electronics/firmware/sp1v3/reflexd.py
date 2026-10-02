"""reflexd — snag reflex daemon, firmware layer F of SPEC §8.5 (runs on the CB1).

Data path:  3 Hall flexures -> Pico (RP2040 ADC, 500 frames/s over USB) -> reflexd
            -> residual = measured external force - modelled force (rim reaction, PTFE, scalp drag)
            -> trip: 'X' to the Pico -> PICO_OK low 50 ms -> hardware REFLEX latch sets -> rail dead.
Heartbeat:  reflexd sends 'H' to the Pico every 50 ms.  If reflexd dies, PICO_OK falls after
            250 ms and the latch sets (fail-safe).  The scorer also faults if reflexd's status
            datagrams stop for 0.5 s.

Criterion (SPEC §8.5 row F):
  * |residual| > 0.8 N for >= 2 consecutive frames (4 ms), or
  * residual component opposing the motion > 0.5 N for >= 60 ms, or
  * tension pattern lost: any cable < 0.2 N or > 3.6 N for >= 2 frames while armed
    (duplicates the LM393 window comparators, layer E; thresholds from ik.audit, CONFLICTS E-C1).
Residual = F_meas - F_model - b, with F_meas = -sum(T_i u_i(d)) (in-plane), F_model from
forcemodel.ForceModel at the PLANNED d(t), v(t) shared by the scorer, and b a slow learned bias
(running median of the residual along the motion, clamped +-0.4 N) that absorbs scalp-friction
error.  Trips only while a plan is active (the block is being driven).
"""
from __future__ import annotations

import argparse
import bisect
import json
import logging
import math
import os
import socket
import statistics
import sys
import termios
import threading
import time
import tty
from collections import deque
from dataclasses import dataclass, field

from .forcemodel import ForceModel
from .ik import Geometry, TendonIK

log = logging.getLogger("sp1v3.reflexd")
SCORER_SOCK = "/tmp/sp1-scorer.sock"
REFLEX_SOCK = "/tmp/sp1-reflexd.sock"


# ------------------------------------------------------------------------- the criterion
@dataclass
class SnagDetector:
    ik: TendonIK
    fm: ForceModel = field(default_factory=ForceModel)
    abs_n: float = 0.8
    abs_frames: int = 2
    opp_n: float = 0.5
    opp_s: float = 0.060
    t_lo: float = 0.2              # slack: cable broken or coupling parted (set from ik.audit)
    t_hi: float = 3.6              # > audit max + margin
    bias_clamp: float = 0.4
    bias_step: float = 0.25          # residual changes larger than this are not learned
    _abs_count: int = 0
    _opp_since: float | None = None
    _pat_count: int = 0
    _bias: deque = field(default_factory=lambda: deque(maxlen=2000))
    peak: float = 0.0

    def measured_force(self, d, T):
        u = self.ik.unit_vectors(d)
        fx = -sum(T[i] * u[i][0] for i in range(3))
        fy = -sum(T[i] * u[i][1] for i in range(3))
        return fx, fy

    def bias(self):
        if len(self._bias) < 50:
            return 0.0
        b = statistics.median(self._bias)
        return max(-self.bias_clamp, min(self.bias_clamp, b))

    def update(self, t, T, d, v, pins_total, pins_on, armed=True):
        """Returns (trip: bool, why: str, residual magnitude)."""
        if armed and (min(T) < self.t_lo or max(T) > self.t_hi):
            self._pat_count += 1
            if self._pat_count >= 2:
                return True, f"tension pattern {['%.2f' % x for x in T]}", 0.0
        else:
            self._pat_count = 0
        if not armed:
            self._abs_count = 0
            self._opp_since = None
            return False, "", 0.0
        mx, my = self.measured_force(d, T)
        ex, ey = self.fm.external(d, v, pins_total, pins_on)
        rx, ry = mx - ex, my - ey
        sp = math.hypot(*v)
        along = 0.0
        if sp > self.fm.v_eps:
            vx, vy = v[0] / sp, v[1] / sp
            along = -(rx * vx + ry * vy)           # positive = opposing the motion
            b = self.bias()
            rx += b * vx                           # remove learned extra drag along -v
            ry += b * vy
            along -= b
        mag = math.hypot(rx, ry)
        self.peak = max(self.peak, mag)
        if mag > self.abs_n:
            self._abs_count += 1
            if self._abs_count >= self.abs_frames:
                return True, f"residual {mag:.2f} N > {self.abs_n}", mag
        else:
            self._abs_count = 0
            # learn slow drag drift only: a step (snag) is never absorbed into the bias
            if sp > self.fm.v_eps and abs(along) < self.bias_step:
                self._bias.append(along + self.bias())
        if along > self.opp_n:
            if self._opp_since is None:
                self._opp_since = t
            elif t - self._opp_since >= self.opp_s:
                return True, f"opposing drag {along:.2f} N for {1000*(t-self._opp_since):.0f} ms", mag
        else:
            self._opp_since = None
        return False, "", mag


# ------------------------------------------------------------------------- planned path buffer
class PlanBuffer:
    def __init__(self):
        self.t0s, self.segs = [], []
        self.lock = threading.Lock()

    def add(self, msg):
        with self.lock:
            self.t0s.append(msg["t0"])
            self.segs.append(msg)
            while self.t0s and self.t0s[0] < time.monotonic() - 5.0:
                self.t0s.pop(0)
                self.segs.pop(0)

    def at(self, t):
        """(d, v, pins_total, pins_on, active) at monotonic time t."""
        with self.lock:
            i = bisect.bisect_right(self.t0s, t) - 1
            if i < 0:
                return (0.0, 0.0), (0.0, 0.0), 0.0, False, False
            m = self.segs[i]
            pts, dur = m["pts"], m["dur"]
            if t > m["t0"] + dur + 0.02 or not pts:
                return tuple(pts[-1]) if pts else (0.0, 0.0), (0.0, 0.0), 0.0, False, False
            n = len(pts)
            u = min(max((t - m["t0"]) / dur * n, 0.0), n - 1.0)
            k = int(u)
            k2 = min(k + 1, n - 1)
            f = u - k
            x = pts[k][0] + (pts[k2][0] - pts[k][0]) * f
            y = pts[k][1] + (pts[k2][1] - pts[k][1]) * f
            dt = dur / n
            vx = (pts[k2][0] - pts[k][0]) / dt if k2 != k else 0.0
            vy = (pts[k2][1] - pts[k][1]) / dt if k2 != k else 0.0
            return (x, y), (vx, vy), m.get("F", 0.0), m.get("pins_on", False), True


# ------------------------------------------------------------------------- the daemon
class Reflexd:
    def __init__(self, port, cal, ik=None, log_T=False):
        self.port_path = port
        self.cal = cal                    # [[zero_counts, N_per_count], x3]
        self.det = SnagDetector(ik or TendonIK(Geometry()))
        self.plan = PlanBuffer()
        self.log_T = log_T
        self.T = [0.0, 0.0, 0.0]
        self.trip = False
        self.why = ""
        self.last_res = 0.0
        self.hb = 0
        self.fd = None

    def open_port(self):
        self.fd = os.open(self.port_path, os.O_RDWR | os.O_NOCTTY)
        tty.setraw(self.fd)
        attrs = termios.tcgetattr(self.fd)
        attrs[3] &= ~termios.ECHO
        termios.tcsetattr(self.fd, termios.TCSANOW, attrs)

    def send(self, b):
        try:
            os.write(self.fd, b)
        except OSError:
            pass

    def plan_rx(self):
        try:
            os.unlink(REFLEX_SOCK)
        except FileNotFoundError:
            pass
        s = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
        s.bind(REFLEX_SOCK)
        while True:
            data = s.recv(262144)
            try:
                self.plan.add(json.loads(data))
            except (ValueError, KeyError):
                pass

    def status_tx(self):
        s = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
        while True:
            self.hb += 1
            self.send(b"H")
            msg = {"hb": self.hb, "T": [round(x, 3) for x in self.T], "trip": self.trip, "why": self.why,
                   "residual": round(self.last_res, 3), "peak": round(self.det.peak, 3), "log_T": self.log_T}
            try:
                s.sendto(json.dumps(msg).encode(), SCORER_SOCK)
            except OSError:
                pass
            self.trip = False
            time.sleep(0.05)

    def tensions(self, counts):
        return [(counts[i] - self.cal[i][0]) * self.cal[i][1] for i in range(3)]

    def run(self):
        self.open_port()
        threading.Thread(target=self.plan_rx, daemon=True).start()
        threading.Thread(target=self.status_tx, daemon=True).start()
        buf = b""
        while True:
            data = os.read(self.fd, 4096)
            if not data:
                time.sleep(0.001)
                continue
            buf += data
            while b"\n" in buf:
                line, buf = buf.split(b"\n", 1)
                line = line.strip()
                if not line.startswith(b"T,"):
                    continue
                try:
                    _, seq, a, b, c = line.split(b",")
                    counts = (int(a), int(b), int(c))
                except ValueError:
                    continue
                t = time.monotonic()
                self.T = self.tensions(counts)
                d, v, F, pins_on, active = self.plan.at(t)
                trip, why, res = self.det.update(t, self.T, d, v, F, pins_on, armed=active)
                self.last_res = res
                if trip:
                    self.send(b"X")                 # Pico drops PICO_OK -> latch sets
                    self.trip, self.why = True, why
                    log.warning("TRIP %s at d=(%.1f, %.1f)", why, *d)


def main(argv=None):
    ap = argparse.ArgumentParser(description="SP1 v3 snag reflex daemon")
    ap.add_argument("--port", default="/dev/serial/by-id/usb-MicroPython_Board_in_FS_mode-if00",
                    help="Pico USB serial (ls /dev/serial/by-id/)")
    ap.add_argument("--config", default=os.path.expanduser("~/sp1v3/config.json"))
    ap.add_argument("--log-tensions", action="store_true")
    a = ap.parse_args(argv)
    logging.basicConfig(level=logging.INFO, format="%(asctime)s reflexd %(levelname)s %(message)s")
    try:
        cfg = json.load(open(a.config))
    except FileNotFoundError:
        cfg = {}
    cal = cfg.get("tension_cal", [[32768, 0.0005]] * 3)      # [VERIFY] set at A3 with a spring scale
    g = cfg.get("geometry", {})
    ik = TendonIK(Geometry(**{k: (tuple(v) if isinstance(v, list) else v) for k, v in g.items()}))
    Reflexd(a.port, cal, ik, a.log_tensions).run()


if __name__ == "__main__":
    sys.exit(main())
