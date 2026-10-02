#!/usr/bin/env python3
"""v31_tendon_audit.py - SP1 v3.1 integration check of the tendon anchor layout (PROJECT SCRATCH, 2026-10-02).

Re-runs the ELECTRONICS firmware's tendon statics (sp1v3.ik.TendonIK.tensions / tension_change) with the
PAD v3b block pose (14-build/pad/CONFLICTS.md P15) instead of the spec-v3 dish model the firmware defaults to:
  * nail-plane origin at (d, sqrt(85^2 - |d|^2) - 85 + h(|d|)); h: 0 to 6.5, 30 deg to +4.5 at 14.29,
    60 deg to +9.0 at 16.89, plateau;
  * half-roll tilt phi = 0.5 * asin(|d| / 85), the block z axis tilting OUTWARD (toward +d), as a roll
    about the scalp centre does;
  * yoke posts at block-frame z 85.5, stops at deck z 85.5 (PAD P2).
The posts then travel ~25.9 mm at |d| = 17.2 (not 17), which is what breaks the R65/R10 and R70/R15 layouts.

Prints, per layout and floating-plate total: unloaded tension range over |d| <= 17.6 and the "any-direction
capacity" = the largest in-plane force, in the worst direction at the worst pose, that keeps every cable
>= 0.3 N (comparator slack window 0.2 N + margin).  Loads to compare against [EST]: scalp + PTFE drag
<= 0.8 N (contact zone only), in-plane gravity of the 57 g moving group <= 0.56 N (bun) / 0.32 N (beta 35),
net dish reaction on the plateau ~0.4-0.9 N, inertia 0.11 N.

  python3 12-sp1v2/scripts/v31_tendon_audit.py
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "14-build", "electronics", "firmware"))
from sp1v3.ik import TendonIK, Geometry, _add, _rotate, _cross, _norm, _scale  # noqa: E402


def h(r):
    if r <= 6.5:
        return 0.0
    if r <= 14.29:
        return (r - 6.5) * math.tan(math.radians(30))
    if r <= 16.89:
        return 4.5 + (r - 14.29) * math.tan(math.radians(60))
    return 9.0


class PadIK(TendonIK):
    def __init__(self, rs, rp, zp=85.5, crossed=False):
        g = Geometry(stop_radius=rs, post_radius=rp)
        self.g = g
        off = 180.0 if crossed else 0.0
        self._stops = [(rs * math.cos(math.radians(a + off)), rs * math.sin(math.radians(a + off)), zp)
                       for a in g.stop_angles_deg]
        self._posts = [(rp * math.cos(math.radians(a)), rp * math.sin(math.radians(a)), zp)
                       for a in g.stop_angles_deg]
        self.l0 = self.lengths((0.0, 0.0))

    def posts(self, d):
        x, y = d
        r = math.hypot(x, y)
        if r < 1e-9:
            return list(self._posts)
        dh = (x / r, y / r, 0.0)
        c = _add(_scale(dh, r), (0.0, 0.0, math.sqrt(85 ** 2 - r * r) - 85 + h(r)))
        axis = _cross((0.0, 0.0, 1.0), dh)
        axis = _scale(axis, 1 / _norm(axis))
        phi = 0.5 * math.asin(min(r, 85.0) / 85.0)
        return [_add(c, _rotate(q, axis, phi)) for q in self._posts]


def sweep(ik, total, rmax, n_r=22, n_a=48, n_th=36, tmin=0.3):
    lo, hi, cap = 1e9, 0.0, 1e9
    for i in range(n_r + 1):
        r = rmax * i / n_r
        for k in range(n_a):
            a = 2 * math.pi * k / n_a
            d = (r * math.cos(a), r * math.sin(a))
            T0 = ik.tensions(d, (0.0, 0.0), total)
            lo, hi = min(lo, min(T0)), max(hi, max(T0))
            for j in range(n_th):
                th = 2 * math.pi * j / n_th
                g = ik.tension_change(d, (math.cos(th), math.sin(th)))
                f = 1e9
                for t0, gi in zip(T0, g):
                    if gi < -1e-12:
                        f = min(f, (t0 - tmin) / (-gi))
                cap = min(cap, f)
    return lo, hi, cap


if __name__ == "__main__":
    ik = PadIK(65, 10)
    p = ik.posts((17.2, 0.0))[0]
    print("post lateral travel at |d| 17.2: %.1f mm" % (p[0] - ik._posts[0][0]))
    print("%-22s %6s  %-17s %-12s %-12s" % ("layout (stop/post)", "total", "unloaded T (N)", "cap |d|<=17.6", "cap |d|<=12.6"))
    for name, kw in [("R65/R10", dict(rs=65, rp=10)), ("R70/R15", dict(rs=70, rp=15)),
                     ("R85/R10", dict(rs=85, rp=10)), ("R90/R10  <- v3.1", dict(rs=90, rp=10)),
                     ("R100/R10", dict(rs=100, rp=10)), ("crossed R65/R10", dict(rs=65, rp=10, crossed=True))]:
        for total in (6.0, 7.5):
            m = PadIK(**kw)
            lo, hi, c1 = sweep(m, total, 17.6)
            _, _, c2 = sweep(m, total, 12.6)
            print("%-22s %6.1f  %5.2f .. %5.2f     %6.2f N     %6.2f N" % (name, total, lo, hi, max(c1, -9.99), c2))
    print("negative capacity = a cable is already below 0.3 N with no load at some pose.")
