"""Klipper API-socket client (and a small simulator for the bench and the unit tests).

Protocol (Klipper docs/API_Server.md, checked 2026-10-02): JSON objects terminated by 0x03 on
the Unix socket given to klippy with `-a` (on the BTT CB1 image:
/home/biqu/printer_data/comms/klippy.sock).  `gcode/script` answers when the script has been
processed (for G1: queued), `objects/subscribe` pushes status deltas, `emergency_stop` = M112.
"""
from __future__ import annotations

import json
import logging
import re
import socket
import threading
import time

log = logging.getLogger("sp1v3.klipper")
ETX = b"\x03"


class KlipperError(Exception):
    pass


class KlipperAPI:
    def __init__(self, path="/home/biqu/printer_data/comms/klippy.sock", timeout=5.0):
        self.path = path
        self.timeout = timeout
        self._sock = None
        self._lock = threading.Lock()
        self._pending = {}
        self._next_id = 1
        self._status_cb = []
        self._alive = False

    # ------------------------------------------------------------------ connection
    def connect(self):
        s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        s.connect(self.path)
        self._sock = s
        self._alive = True
        threading.Thread(target=self._reader, name="klippy-rx", daemon=True).start()

    def close(self):
        self._alive = False
        try:
            self._sock.close()
        except Exception:
            pass

    @property
    def alive(self):
        return self._alive

    def _reader(self):
        buf = b""
        while self._alive:
            try:
                data = self._sock.recv(65536)
            except OSError:
                data = b""
            if not data:
                self._alive = False
                for ev in list(self._pending.values()):
                    ev[1]["error"] = {"message": "klippy socket closed"}
                    ev[0].set()
                break
            buf += data
            while ETX in buf:
                raw, buf = buf.split(ETX, 1)
                try:
                    msg = json.loads(raw)
                except ValueError:
                    continue
                self._dispatch(msg)

    def _dispatch(self, msg):
        if "id" in msg and msg["id"] in self._pending:
            ev, box = self._pending.pop(msg["id"])
            box.update(msg)
            ev.set()
            return
        params = msg.get("params", {})
        if "status" in params:
            for cb in self._status_cb:
                try:
                    cb(params["status"], params.get("eventtime"))
                except Exception:
                    log.exception("status callback")

    def request(self, method, params=None, timeout=None):
        with self._lock:
            rid = self._next_id
            self._next_id += 1
            ev, box = threading.Event(), {}
            self._pending[rid] = (ev, box)
            self._sock.sendall(json.dumps({"id": rid, "method": method,
                                           "params": params or {}}).encode() + ETX)
        if not ev.wait(timeout or self.timeout):
            self._pending.pop(rid, None)
            raise KlipperError(f"{method}: timeout")
        if "error" in box:
            raise KlipperError(box["error"].get("message", str(box["error"])))
        return box.get("result", {})

    # ------------------------------------------------------------------ helpers
    def script(self, text, timeout=30.0):
        return self.request("gcode/script", {"script": text}, timeout=timeout)

    def query(self, objects):
        return self.request("objects/query", {"objects": objects})["status"]

    def subscribe(self, objects, callback):
        self._status_cb.append(callback)
        res = self.request("objects/subscribe", {"objects": objects, "response_template": {}})
        callback(res.get("status", {}), res.get("eventtime"))
        return res

    def emergency_stop(self):
        try:
            self.request("emergency_stop", timeout=1.0)
        except Exception:
            log.exception("emergency_stop")


# ======================================================================================
# Simulator: enough of Klipper for bench runs on a Mac and for the unit tests.
# ======================================================================================
_G1 = re.compile(r"^G1\s+(.*)$", re.I)
_ARG = re.compile(r"([A-Z])([-+]?[0-9.]+)", re.I)


class SimKlipper:
    """Accepts the same calls as KlipperAPI.  Tracks queued motion time against wall time,
    axis positions, pins and heater targets, and lets a test drive buttons/sensors."""

    def __init__(self, realtime=True):
        self.realtime = realtime
        self.pos = {"A": 0.0, "B": 0.0, "C": 0.0}
        self.pins = {}
        self.targets = {}
        self.buttons = {}
        self.temps = {}
        self.state = "ready"
        self.lines = []          # every g-code line received
        self.motion_end = time.monotonic()
        self._status_cb = []
        self.max_cable_speed = 0.0
        self.alive = True

    def connect(self):
        pass

    def close(self):
        self.alive = False

    def _now(self):
        return time.monotonic()

    def queued(self):
        return max(0.0, self.motion_end - self._now())

    def script(self, text, timeout=30.0):
        if self.state != "ready":
            raise KlipperError("Klipper not ready: " + self.state)
        now = self._now()
        if self.motion_end < now:
            self.motion_end = now + 0.1
        for line in text.splitlines():
            line = line.strip()
            if not line:
                continue
            self.lines.append(line)
            u = line.upper()
            m = _G1.match(line)
            if m:
                args = {k.upper(): float(v) for k, v in _ARG.findall(m.group(1))}
                dmax = max(abs(args.get(a, self.pos[a]) - self.pos[a]) for a in "ABC")
                F = args.get("F", 600.0)
                if dmax > 0:
                    dt = dmax / (F / 60.0)
                    self.max_cable_speed = max(self.max_cable_speed, F / 60.0)
                    self.motion_end += dt
                for a in "ABC":
                    if a in args:
                        self.pos[a] = args[a]
            elif u.startswith("G4"):
                p = _ARG.findall(line)
                self.motion_end += float(dict((k.upper(), v) for k, v in p).get("P", 0)) / 1000.0
            elif u.startswith("SET_PIN"):
                kv = dict(x.split("=", 1) for x in line.split()[1:])
                self.pins[kv["PIN"].lower()] = float(kv["VALUE"])
            elif u.startswith("SET_HEATER_TEMPERATURE"):
                kv = dict(x.split("=", 1) for x in line.split()[1:])
                self.targets[kv["HEATER"].lower()] = float(kv.get("TARGET", 0))
            elif u.startswith("M112"):
                self.state = "shutdown"
        # emulate Klipper's 1 s buffer limit: the request blocks while > 1 s is queued
        if self.realtime:
            while self.queued() > 1.0:
                time.sleep(0.01)
        return {}

    def query(self, objects):
        st = {}
        for name in objects:
            if name == "toolhead":
                now = self._now()
                st[name] = {"print_time": max(self.motion_end, now), "estimated_print_time": now}
            elif name == "webhooks":
                st[name] = {"state": self.state}
            elif name.startswith("gcode_button"):
                st[name] = {"state": "PRESSED" if self.buttons.get(name) else "RELEASED"}
            elif name.startswith("temperature_sensor") or name.startswith("heater_generic"):
                st[name] = {"temperature": self.temps.get(name, 0.0),
                            "target": self.targets.get(name.split()[-1], 0.0)}
            elif name == "query_endstops":
                st[name] = {"last_query": {}}
        return st

    def subscribe(self, objects, callback):
        self._status_cb.append(callback)
        callback(self.query(objects), self._now())
        return {}

    def push(self, status):
        for cb in self._status_cb:
            cb(status, self._now())

    def emergency_stop(self):
        self.state = "shutdown"
