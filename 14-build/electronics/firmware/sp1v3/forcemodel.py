"""Modelled external force on the pin block (frame S, N).  Shared by the scorer (series-spring
feed-forward) and reflexd (snag residual), so both use the same numbers.

SPEC §4.2: rim reaction ~1.2 N on the inner rim with pins in contact, ~0.7 N on the outer
rim (pins up), + ~0.25 N PTFE drag.  Scalp drag ~ mu * sum(F_pins) while nails are down.
All values are [EST] until `cal rim` (no-contact sweep) and the A3 rig replace them.
"""
from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass
class ForceModel:
    r_inner: float = 7.0
    r_outer: float = 13.7
    r_land: float = 10.4          # mid landing radius (nails down inside)
    rim_inner_n: float = 1.2
    rim_outer_n: float = 0.7
    ptfe_n: float = 0.25
    mu_scalp: float = 0.25
    v_eps: float = 2.0            # mm/s below which no drag direction is defined

    def rim(self, r: float, pins_on: bool) -> float:
        if r <= self.r_inner:
            return 0.0
        if r <= self.r_outer:
            u = (r - self.r_inner) / (self.r_outer - self.r_inner)
            return u * (self.rim_inner_n if pins_on else self.rim_outer_n)
        return self.rim_outer_n

    def external(self, p, v, pins_total_n: float, pins_on: bool):
        """In-plane external force on the block (N) at position p (mm) and velocity v (mm/s)."""
        x, y = p
        r = math.hypot(x, y)
        fx = fy = 0.0
        if r > 1e-6:
            R = self.rim(r, pins_on)
            fx -= R * x / r
            fy -= R * y / r
        sp = math.hypot(*v)
        if sp > self.v_eps:
            drag = self.ptfe_n
            if pins_on and r < self.r_land:
                drag += self.mu_scalp * pins_total_n
            fx -= drag * v[0] / sp
            fy -= drag * v[1] / sp
        return fx, fy
