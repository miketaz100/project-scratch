"""Path primitives in frame S (block offset d, mm).  SPEC §4.5, §8.3.

Every primitive returns a `Token`: uniformly time-sampled points (dt <= SAMPLE_DT) that
START AND END AT REST ON THE RIM (|d| >= R_NO_REVERSAL), so tokens can be chained in any
order without a junction ever lying inside the no-reversal radius.  Group-valve events are
time-stamped inside the token and must fall on the rim (the checker enforces it).

Contact profile (SPEC §8.3): constant path speed while |d| <= R_LAND_OUTER, accelerate /
decelerate only in the rim zone, turnaround at |d| = 14-16.5.
"""
from __future__ import annotations

import math
from dataclasses import dataclass, field

from . import limits as L


@dataclass
class Token:
    kind: str
    samples: list                       # [(t, x, y)], t from 0
    events: list = field(default_factory=list)   # [(t, name, value)]
    params: dict = field(default_factory=dict)
    force: dict | None = None           # {"rail": kPa, "groups": "A"/"B"/"AB"/"", "bratio": r, "palm": kPa}
    contact: bool = True                # pins pressurised during this token

    @property
    def duration(self):
        return self.samples[-1][0] if self.samples else 0.0

    @property
    def start(self):
        return self.samples[0][1:]

    @property
    def end(self):
        return self.samples[-1][1:]


def _uniform_times(T, dt):
    n = max(1, int(math.ceil(T / dt - 1e-9)))
    return [T * k / n for k in range(n + 1)]


def _unit(deg):
    a = math.radians(deg)
    return math.cos(a), math.sin(a)


# --------------------------------------------------------------------------------------
# straight stroke (LINE, PLINE, CHORD)
# --------------------------------------------------------------------------------------
def line_profile(s_end, s_c, T_h):
    """Trapezoid in path speed along s in [-s_end, +s_end]: rest at both ends, constant v_c for
    |s| <= s_c.  Returns (v_c, a_rim, s(t) function)."""
    D_r = s_end - s_c
    if D_r <= 0:
        raise ValueError("turnaround must lie outside the contact zone")
    v_c = (2 * s_c + 4 * D_r) / T_h
    a = v_c * v_c / (2 * D_r)
    t_r = v_c / a                                # time for each rim zone

    def s_of_t(t):
        if t <= t_r:
            return -s_end + 0.5 * a * t * t
        if t <= T_h - t_r:
            return -s_c + v_c * (t - t_r)
        tt = T_h - t
        return s_end - 0.5 * a * tt * tt
    return v_c, a, s_of_t


def line(psi_deg, amp=16.0, e=0.0, f=1.4, reverse=False, dt=L.SAMPLE_DT, period_scale=1.0):
    """One half-stroke (rim -> through contact -> rim) along heading psi, offset e (chord).

    amp is the turnaround RADIUS |d| (14-16.5).  f is the out-and-back frequency, so the
    half-stroke lasts 1/(2f) (times period_scale, the variation)."""
    if not (L.R_NO_REVERSAL < amp <= L.D_MAX):
        raise ValueError(f"amp {amp} outside ({L.R_NO_REVERSAL}, {L.D_MAX}]")
    if abs(e) >= L.R_LAND_OUTER - 1.0:
        raise ValueError("chord offset too large: no contact")
    s_end = math.sqrt(amp * amp - e * e)
    s_c = math.sqrt(L.R_LAND_OUTER ** 2 - e * e)
    T_h = period_scale / (2.0 * f)
    v_c, a, s_of_t = line_profile(s_end, s_c, T_h)
    ux, uy = _unit(psi_deg)
    nx, ny = -uy, ux
    sgn = -1.0 if reverse else 1.0
    samples = []
    for t in _uniform_times(T_h, dt):
        s = sgn * s_of_t(t)
        samples.append((t, s * ux + e * nx, s * uy + e * ny))
    return Token("line", samples, params={"psi": psi_deg, "amp": amp, "e": e, "f": f,
                                          "v_c": v_c, "a_rim": a, "reverse": reverse})


# --------------------------------------------------------------------------------------
# rim connector / turn (heading change only on the rim)
# --------------------------------------------------------------------------------------
def rim_arc(p_from, p_to, v_avg=80.0, dt=L.SAMPLE_DT, min_T=0.06, way=0):
    """Move from p_from to p_to along the rim (polar interpolation: radius linear, angle along the
    shorter arc unless way=+1/-1 forces the direction).  Cosine speed profile, rest at both ends.
    Both endpoints must be at |d| >= R_NO_REVERSAL, so every point is too."""
    r0, r1 = math.hypot(*p_from), math.hypot(*p_to)
    a0, a1 = math.atan2(p_from[1], p_from[0]), math.atan2(p_to[1], p_to[0])
    da = (a1 - a0 + math.pi) % (2 * math.pi) - math.pi
    if way > 0 and da < 0:
        da += 2 * math.pi
    elif way < 0 and da > 0:
        da -= 2 * math.pi
    length = abs(da) * (r0 + r1) / 2 + abs(r1 - r0)
    T = max(min_T, length / v_avg)
    samples = []
    for t in _uniform_times(T, dt):
        u = 0.5 - 0.5 * math.cos(math.pi * t / T)
        r = r0 + (r1 - r0) * u
        a = a0 + da * u
        samples.append((t, r * math.cos(a), r * math.sin(a)))
    samples[-1] = (samples[-1][0], p_to[0], p_to[1])
    samples[0] = (0.0, p_from[0], p_from[1])
    return Token("rim", samples, params={"len": length}, contact=False)


def park(p, duration, dt=L.SAMPLE_DT):
    """Hold at p (must be on the rim).  The streamer turns this into a G4 dwell."""
    T = max(duration, dt)
    return Token("park", [(t, p[0], p[1]) for t in _uniform_times(T, max(dt, T / 4))],
                 params={"duration": T}, contact=False)


# --------------------------------------------------------------------------------------
# offset circle with a precessing offset (lifts once per revolution)
# --------------------------------------------------------------------------------------
def circle(R=11.5, e=3.5, phi0_deg=0.0, prec_deg=25.0, f=1.2, revs=3, direction=1,
           dt=L.SAMPLE_DT, ramp_deg=None, start_off_deg=None):
    """d(th) = c(th) + R (cos th, sin th), c(th) = e * u(phi0 + k (th - th0)), k = prec/360.

    Starts at rest at th0 = phi0 - start_off (on the rim, |d| ~ 14.4 for the defaults),
    ramps the angular speed up over ramp_deg on the rim, runs at w = 2 pi f, ramps down and
    ends at rest at +start_off from the (precessed) far point, again on the rim.
    start_off defaults to 85 % of the half-width of the arc that lies outside 13.9 mm."""
    if start_off_deg is None:
        cw = (13.9 ** 2 - R * R - e * e) / (2 * R * e)
        if cw >= 1.0:
            raise ValueError("circle never reaches the rim (R + e too small)")
        half = math.degrees(math.acos(max(-1.0, cw)))
        start_off_deg = min(40.0, 0.85 * half)
    if ramp_deg is None:
        ramp_deg = start_off_deg
    k = prec_deg / 360.0 * direction
    th0 = math.radians(phi0_deg - direction * start_off_deg)
    # total angle so the end lands start_off past the far point (see module notes)
    Theta = (2 * math.pi * revs + math.radians(2 * start_off_deg)) / (1.0 - abs(k))
    w = 2 * math.pi * f
    ra = math.radians(ramp_deg)
    alpha = w * w / (2 * ra)
    t_a = w / alpha
    T = 2 * t_a + (Theta - 2 * ra) / w

    def th_of_t(t):
        if t <= t_a:
            return 0.5 * alpha * t * t
        if t <= T - t_a:
            return ra + w * (t - t_a)
        tt = T - t
        return Theta - 0.5 * alpha * tt * tt

    samples = []
    for t in _uniform_times(T, dt):
        u = th_of_t(t)
        th = th0 + direction * u
        phi = math.radians(phi0_deg) + k * u
        x = e * math.cos(phi) + R * math.cos(th)
        y = e * math.sin(phi) + R * math.sin(th)
        samples.append((t, x, y))
    return Token("circle", samples, params={"R": R, "e": e, "prec": prec_deg, "f": f,
                                            "revs": revs, "phi0": phi0_deg})


# --------------------------------------------------------------------------------------
# one-way D-path: contact chord with the grain, return round the rim (nails up)
# --------------------------------------------------------------------------------------
def dpath(psi_deg, amp=16.0, f=1.4, side=1, dt=L.SAMPLE_DT, v_arc=110.0):
    """Returns [stroke, rim return]; the block ends where it started (-amp along psi)."""
    st = line(psi_deg, amp=amp, e=0.0, f=f, dt=dt)
    ret = rim_arc(st.end, st.start, v_avg=v_arc, dt=dt, way=side)
    ret.kind = "dpath_return"
    return [st, ret]


def concat_ok(a: Token, b: Token, tol=1e-6) -> bool:
    return math.hypot(a.end[0] - b.start[0], a.end[1] - b.start[1]) < tol


def connect(p_from, p_to, dt=L.SAMPLE_DT):
    """Connector between two tokens (both on the rim).  None if already there."""
    if math.hypot(p_from[0] - p_to[0], p_from[1] - p_to[1]) < 1e-6:
        return None
    return rim_arc(p_from, p_to, dt=dt)
