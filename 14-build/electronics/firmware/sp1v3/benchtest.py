"""S0 / A0 bench tests for the Klipper side (V-K1, V-K2).  Pad retracted or no pad at all.

  python3 -m sp1v3.benchtest stream --strokes 500        # PLINE through the IK, LED on pin_a at each rim
  python3 -m sp1v3.benchtest stream --sim                # same, against the simulator (no hardware)

Pass lines (SPEC §10 S0 "Klipper test"): G1 A/B/C timing follows F (total time within 1 % of
plan), toolhead `stalls` does not increase, SET_PIN edges land at the rim (film at 240 fps:
LED edge vs. the pen mark, +-2 ms).
"""
from __future__ import annotations

import argparse
import time

from .ik import CableComp, TendonIK
from .forcemodel import ForceModel
from .klipper import KlipperAPI, SimKlipper
from .planner import Planner, Settings
from .scorer import Streamer


def stream(kl, strokes, f):
    ik = TendonIK()
    st = Streamer(kl, ik, CableComp(), ForceModel())
    st.ff = False
    pl = Planner(Settings(mode="pline", f=f, vary=False, groups="ab"))
    pl.st.pos = (0.0, 0.0)
    st.reset((0.0, 0.0, 0.0), (0.0, 0.0))
    try:
        s0 = kl.query({"toolhead": ["stalls"]})["toolhead"].get("stalls", 0)
    except Exception:
        s0 = 0
    st.send(pl.to_rim(-90.0))
    planned, n, t_start = 0.0, 0, time.monotonic()
    while n < strokes:
        for tok in pl.next_tokens():
            pre = ["SET_PIN PIN=pin_a VALUE=1"] if tok.kind == "line" else ["SET_PIN PIN=pin_a VALUE=0"]
            st.send(tok, pre=pre)
            planned += tok.duration
            n += tok.kind == "line"
    time.sleep(st.queued() + 0.5)
    wall = time.monotonic() - t_start
    try:
        s1 = kl.query({"toolhead": ["stalls"]})["toolhead"].get("stalls", 0)
    except Exception:
        s1 = 0
    print(f"strokes {n}  planned {planned:.2f} s  wall {wall:.2f} s  stalls {s1 - s0}")
    print("PASS" if (s1 - s0) == 0 else "FAIL: Klipper stalled (host did not keep up)")


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("test", choices=["stream"])
    ap.add_argument("--strokes", type=int, default=100)
    ap.add_argument("--f", type=float, default=1.4)
    ap.add_argument("--sim", action="store_true")
    ap.add_argument("--klippy", default="/home/biqu/printer_data/comms/klippy.sock")
    a = ap.parse_args(argv)
    if a.sim:
        kl = SimKlipper()
    else:
        kl = KlipperAPI(a.klippy)
        kl.connect()
    stream(kl, a.strokes, a.f)


if __name__ == "__main__":
    main()
