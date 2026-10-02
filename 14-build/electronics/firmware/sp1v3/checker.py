"""Path checker (dish-gate condition C5 and SPEC §8.3).  Runs on EVERY token before it is sent.

Rules (rule id -> SPEC wording):
  P1 bounds      : reject any sample with |d| > 16.5 mm
  P2 speed       : reject any segment with v > 200 mm/s
  P3 contact acc : reject in-contact acceleration > 2 m/s^2 (|d| < 12.2 over 3 samples)
  P4 heading     : reject velocity reversal, or heading change > 30 deg per 50 ms, inside |d| < 13.7
  P5 cusp        : reject path speed < V_CUSP inside |d| < 13.7 (a stop or cusp on the scalp)
  P6 landing     : reject landing/lift (8.5 <= |d| <= 12.2) at path speed < 0.3 v_peak
  P7 circle      : CIRCLE needs R + e >= 14.5, R - e <= 8.5, offset rotation 15-40 deg/rev
  P8 valves      : reject any group-valve change while |d| < 13.7 (switch only on the rim)
  P9 support     : reject sum(F_pins) + 0.45 N > F_float; rail <= 15.6 kPa; palm <= 20 kPa
  P10 endpoints  : token starts and ends at rest with |d| >= 13.7 (so tokens chain safely)
  P11 sampling   : times strictly increasing, step <= SAMPLE_DT (+1 %)

The checker is firmware (third barrier).  The mechanical guarantee is the dish itself:
outside 13.7 mm every nail is lifted >= 5 mm by geometry.
"""
from __future__ import annotations

import math
from dataclasses import dataclass

from . import limits as L
from .paths import Token


@dataclass
class Violation:
    rule: str
    index: int
    detail: str

    def __str__(self):
        return f"{self.rule}@{self.index}: {self.detail}"


class PathRejected(Exception):
    def __init__(self, violations):
        self.violations = violations
        super().__init__("; ".join(str(v) for v in violations[:5]))


def _r(x, y):
    return math.hypot(x, y)


def check_token(tok: Token, first_only=False, tol=1e-6) -> list:
    """Return a list of Violations (empty = OK)."""
    v_out = []

    def bad(rule, i, msg):
        v_out.append(Violation(rule, i, msg))
        return first_only

    s = tok.samples
    if len(s) < 2:
        bad("P11", 0, "token has < 2 samples")
        return v_out

    # P11 sampling
    for i in range(1, len(s)):
        dt = s[i][0] - s[i - 1][0]
        if dt <= 0 or dt > L.SAMPLE_DT * 1.01 + 1e-12:
            if tok.kind != "park" and bad("P11", i, f"dt {dt*1000:.2f} ms"):
                return v_out

    # P1 bounds
    for i, (t, x, y) in enumerate(s):
        if _r(x, y) > L.D_MAX + tol:
            if bad("P1", i, f"|d| {_r(x, y):.2f} > {L.D_MAX}"):
                return v_out

    # interval velocities
    vel = []          # (vx, vy, speed, t_mid, r_mid)
    for i in range(len(s) - 1):
        t0, x0, y0 = s[i]
        t1, x1, y1 = s[i + 1]
        dt = t1 - t0
        if dt <= 0:
            vel.append((0.0, 0.0, 0.0, t0, _r(x0, y0)))
            continue
        vx, vy = (x1 - x0) / dt, (y1 - y0) / dt
        vel.append((vx, vy, math.hypot(vx, vy), (t0 + t1) / 2, _r((x0 + x1) / 2, (y0 + y1) / 2)))
    v_peak = max(v[2] for v in vel) if vel else 0.0

    # P2 speed
    for i, v in enumerate(vel):
        if v[2] > L.V_MAX + 1e-6:
            if bad("P2", i, f"v {v[2]:.1f} mm/s > {L.V_MAX}"):
                return v_out

    # P3 in-contact acceleration: only where three consecutive samples are inside 12.2
    for i in range(1, len(vel)):
        r_a, r_b, r_c = _r(*s[i - 1][1:]), _r(*s[i][1:]), _r(*s[i + 1][1:])
        if max(r_a, r_b, r_c) < L.R_LAND_OUTER:
            dt = vel[i][3] - vel[i - 1][3]
            if dt <= 0:
                continue
            ax = (vel[i][0] - vel[i - 1][0]) / dt
            ay = (vel[i][1] - vel[i - 1][1]) / dt
            a = math.hypot(ax, ay)
            if a > L.A_CONTACT_MAX * 1.02:
                if bad("P3", i, f"a {a/1000:.2f} m/s2 in contact at |d| {r_b:.1f}"):
                    return v_out

    # P5 cusp and P4 heading/reversal inside the no-reversal radius
    for i, v in enumerate(vel):
        if v[4] < L.R_NO_REVERSAL:
            if v[2] < L.V_CUSP:
                if bad("P5", i, f"speed {v[2]:.1f} mm/s at |d| {v[4]:.2f} (< {L.R_NO_REVERSAL})"):
                    return v_out
                continue
            j = i + 1
            while j < len(vel) and vel[j][3] - v[3] <= L.HEADING_WINDOW_S + 1e-9:
                w = vel[j]
                if w[4] < L.R_NO_REVERSAL and w[2] >= L.V_CUSP:
                    c = (v[0] * w[0] + v[1] * w[1]) / (v[2] * w[2])
                    ang = math.degrees(math.acos(max(-1.0, min(1.0, c))))
                    if ang > L.HEADING_MAX_DEG + 1e-6:
                        rule = "P4rev" if ang > 150 else "P4"
                        if bad(rule, i, f"heading change {ang:.1f} deg in "
                                        f"{(w[3]-v[3])*1000:.0f} ms at |d| {v[4]:.2f}"):
                            return v_out
                        break
                j += 1

    # P6 landing / lift speed
    for i, v in enumerate(vel):
        if L.R_LAND_INNER <= v[4] <= L.R_LAND_OUTER and v[2] < L.LAND_SPEED_FRAC * v_peak - 1e-6:
            if bad("P6", i, f"landing at {v[2]:.1f} mm/s < 0.3 v_peak ({v_peak:.0f}) |d| {v[4]:.1f}"):
                return v_out

    # P7 circle parameters
    if tok.kind == "circle":
        R, e, prec = tok.params.get("R"), tok.params.get("e"), tok.params.get("prec", 0.0)
        if R is None or e is None:
            bad("P7", 0, "circle token without R/e")
        else:
            if R + e < L.CIRCLE_RPE_MIN - 1e-9:
                bad("P7", 0, f"R+e {R+e:.1f} < {L.CIRCLE_RPE_MIN} (never lifts)")
            if R - e > L.CIRCLE_RME_MAX + 1e-9:
                bad("P7", 0, f"R-e {R-e:.1f} > {L.CIRCLE_RME_MAX} (never lands / centred)")
            if not (L.CIRCLE_PREC_MIN_DEG - 1e-9 <= abs(prec) <= L.CIRCLE_PREC_MAX_DEG + 1e-9):
                bad("P7", 0, f"offset rotation {prec} deg/rev outside 15-40")
        # geometric confirmation: the path must actually leave the rim at least once per rev
        rmax = max(_r(x, y) for _, x, y in s)
        if rmax < L.R_NO_REVERSAL:
            bad("P7", 0, f"circle never reaches the rim (max |d| {rmax:.1f})")

    # P8 valve events only on the rim
    for (te, name, val) in tok.events:
        # position at time te (nearest sample)
        k = min(range(len(s)), key=lambda q: abs(s[q][0] - te))
        rr = _r(*s[k][1:])
        if rr < L.R_NO_REVERSAL - tol:
            if bad("P8", k, f"valve event {name}={val} at |d| {rr:.2f}"):
                return v_out

    # P9 force / constant support
    if tok.force and tok.contact:
        rail = tok.force.get("rail", 0.0)
        groups = tok.force.get("groups", "")
        br = tok.force.get("bratio", 1.0)
        palm = tok.force.get("palm", 0.0)
        if rail > L.RAIL_MAX_KPA + 1e-9:
            bad("P9", 0, f"rail {rail:.1f} kPa > {L.RAIL_MAX_KPA}")
        if L.nail_force(rail) > L.F_NAIL_MAX + 1e-9:
            bad("P9", 0, f"nail force {L.nail_force(rail):.2f} N > {L.F_NAIL_MAX}")
        if palm > L.PALM_MAX_KPA + 1e-9:
            bad("P9", 0, f"palm {palm:.1f} kPa > {L.PALM_MAX_KPA}")
        spring = tok.force.get("float_spring", L.FLOAT_SPRING_N)
        need = L.pins_total(rail, groups, br) + L.SKID_FLOOR_N
        have = L.float_net(palm, spring)
        if groups and need > have + 1e-9:
            bad("P9", 0, f"support: pins {need - L.SKID_FLOOR_N:.2f} N + 0.45 > float {have:.2f} N")

    # P10 endpoints at rest on the rim
    for idx, vi in ((0, 0), (len(s) - 1, len(vel) - 1)):
        rr = _r(*s[idx][1:])
        if rr < L.R_NO_REVERSAL - tol:
            bad("P10", idx, f"token endpoint at |d| {rr:.2f} (must be >= {L.R_NO_REVERSAL})")
        if tok.kind != "park" and vel and vel[vi][2] > L.V_REST_JOIN:
            bad("P10", idx, f"token endpoint not at rest (v {vel[vi][2]:.1f} mm/s > {L.V_REST_JOIN})")

    return v_out


def assert_ok(tok: Token):
    v = check_token(tok)
    if v:
        raise PathRejected(v)
    return tok


def check_sequence(tokens, tol=1e-6) -> list:
    """Check each token and that consecutive tokens join (positions equal)."""
    out = []
    prev = None
    for n, t in enumerate(tokens):
        for v in check_token(t):
            out.append(Violation(v.rule, v.index, f"token {n} ({t.kind}): {v.detail}"))
        if prev is not None:
            gap = math.hypot(prev.end[0] - t.start[0], prev.end[1] - t.start[1])
            if gap > tol:
                out.append(Violation("P12", n, f"gap {gap:.4f} mm between token {n-1} and {n}"))
        prev = t
    return out
