"""Host-side inverse kinematics: block offset d (frame S) -> three cable length changes.

SPEC §8.2: l_i = |A_i - (p_i(t) + d(t), z(d), tilt(d))| - l_i0
  A_i  = housing stop on the deck skirt (fixed in frame P), stop angles 90/210/330 deg
  p_i  = yoke post (rides and tilts with the block)
  z(d) = block rise on the printed dish, tilt(d) = block tilt (both from the dish profile)

Conventions
  * Frame P/S: x along the bail tangent, z away from the scalp, mm.
  * Cable coordinate l_i (mm) = change of the free length between stop and post relative
    to the centred block.  l_i > 0  -> cable paid OUT by the drum.  This is the value
    written to G-code axis A/B/C (cable_a/b/c), rotation_distance = pi * 12 mm.
  * Pure Python (no numpy) so it runs unchanged on the CB1 and on a Mac.

The dish model is a block-centre rise table z(r) and tilt table t(r) as functions of
r = |d|.  Defaults follow SPEC §4.2 (R160 sphere to 7 mm, 34 deg to 13.7, 50 deg to 17.0,
tilt <= 5.5 deg).  The CAD WP's C8 sweep (or `cal rim`) replaces both tables via
`DishModel.from_table()` without code changes.
"""
from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Iterable, Sequence

Vec = tuple  # (x, y, z)


# ------------------------------- small vector helpers --------------------------------
def _sub(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def _add(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def _scale(a, s):
    return (a[0] * s, a[1] * s, a[2] * s)


def _dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def _cross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def _norm(a):
    return math.sqrt(_dot(a, a))


def _rotate(v, axis, ang):
    """Rodrigues rotation of v about unit axis by ang (rad)."""
    if ang == 0.0:
        return v
    c, s = math.cos(ang), math.sin(ang)
    kxv = _cross(axis, v)
    kdv = _dot(axis, v)
    return (v[0] * c + kxv[0] * s + axis[0] * kdv * (1 - c),
            v[1] * c + kxv[1] * s + axis[1] * kdv * (1 - c),
            v[2] * c + kxv[2] * s + axis[2] * kdv * (1 - c))


# ------------------------------------- dish -------------------------------------------
@dataclass
class DishModel:
    """Block-centre rise z(r) and tilt(r) on the dish, r = |d| in mm.

    Built by integrating a slope function whose kinks are blended over `blend` mm (the
    Ø6 POM domes round every kink in reality), so z(r) is C1 and the IK has no jumps.
    """
    r_sphere: float = 160.0     # centre sphere radius
    r1: float = 7.0             # sphere -> inner rim
    r2: float = 13.7            # inner rim -> outer rim
    r3: float = 17.0            # rim top
    ang_inner_deg: float = 34.0
    ang_outer_deg: float = 50.0
    tilt_max_deg: float = 5.5   # at r3 [EST: linear ramp from r1; replace with CAD sweep]
    blend: float = 1.0
    step: float = 0.01
    _r: list = field(default_factory=list, repr=False)
    _z: list = field(default_factory=list, repr=False)
    _t: list = field(default_factory=list, repr=False)

    def __post_init__(self):
        if not self._r:
            self._build()

    def _slope_raw(self, r):
        if r < self.r1:
            return r / math.sqrt(self.r_sphere ** 2 - r * r)
        if r < self.r2:
            return math.tan(math.radians(self.ang_inner_deg))
        return math.tan(math.radians(self.ang_outer_deg))

    def _slope(self, r):
        h = self.blend / 2.0
        for rk in (self.r1, self.r2):
            if rk - h < r < rk + h:
                a, b = self._slope_raw(rk - h), self._slope_raw(rk + h)
                u = (r - (rk - h)) / self.blend
                return a + (b - a) * u
        return self._slope_raw(r)

    def _build(self):
        n = int(round((self.r3 + 1.0) / self.step)) + 1
        z = 0.0
        rs, zs, ts = [], [], []
        t_max = math.radians(self.tilt_max_deg)
        for i in range(n):
            r = i * self.step
            if i:
                rm = r - self.step / 2.0
                z += self._slope(rm) * self.step
            rs.append(r)
            zs.append(z)
            u = (r - self.r1) / (self.r3 - self.r1)
            u = min(max(u, 0.0), 1.0)
            ts.append(t_max * (u * u * (3 - 2 * u)))      # smoothstep ramp, C1
        self._r, self._z, self._t = rs, zs, ts

    @classmethod
    def from_table(cls, rows: Sequence[tuple]):
        """rows = [(r_mm, rise_mm, tilt_deg), ...] sorted by r (e.g. from the CAD C8 sweep)."""
        m = cls.__new__(cls)
        m.step = None
        m._r = [float(r) for r, _, _ in rows]
        m._z = [float(z) for _, z, _ in rows]
        m._t = [math.radians(float(t)) for _, _, t in rows]
        m.r3 = m._r[-1]
        return m

    def _interp(self, arr, r):
        rr = self._r
        if r <= rr[0]:
            return arr[0]
        if r >= rr[-1]:
            return arr[-1]
        if self.step:                               # uniform grid: O(1)
            i = int(r / self.step)
        else:                                       # bisection on a user table
            lo, hi = 0, len(rr) - 1
            while hi - lo > 1:
                mid = (lo + hi) // 2
                if rr[mid] <= r:
                    lo = mid
                else:
                    hi = mid
            i = lo
        i = min(i, len(rr) - 2)
        u = (r - rr[i]) / (rr[i + 1] - rr[i])
        return arr[i] + (arr[i + 1] - arr[i]) * u

    def rise(self, r: float) -> float:
        return self._interp(self._z, r)

    def tilt(self, r: float) -> float:
        """Tilt angle (rad); the leading side (toward +d) rises."""
        return self._interp(self._t, r)


# ----------------------------------- geometry -----------------------------------------
@dataclass
class Geometry:
    """Tendon geometry in frame P.  Defaults = SPEC §5.1 M13/M14 (see CONFLICTS.md E-C10)."""
    stop_radius: float = 48.0                 # deck stops on the skirt, M13
    post_radius: float = 30.0                 # yoke posts, M14
    stop_angles_deg: tuple = (90.0, 210.0, 330.0)
    stop_z: float = 0.0                       # stop height above the yoke-post plane at d = 0
    dish: DishModel = field(default_factory=DishModel)

    def stops(self):
        return [(self.stop_radius * math.cos(math.radians(a)),
                 self.stop_radius * math.sin(math.radians(a)), self.stop_z)
                for a in self.stop_angles_deg]

    def posts_local(self):
        return [(self.post_radius * math.cos(math.radians(a)),
                 self.post_radius * math.sin(math.radians(a)), 0.0)
                for a in self.stop_angles_deg]


class TendonIK:
    """d -> cable length changes (and back)."""

    def __init__(self, geom: Geometry | None = None):
        self.g = geom or Geometry()
        self._stops = self.g.stops()
        self._posts = self.g.posts_local()
        self.l0 = self.lengths((0.0, 0.0))

    # ---- pose of the block ----
    def block_pose(self, d):
        """Returns (centre position (x, y, z), tilt axis, tilt angle)."""
        x, y = d
        r = math.hypot(x, y)
        z = self.g.dish.rise(r)
        if r < 1e-9:
            return (x, y, z), (1.0, 0.0, 0.0), 0.0
        dh = (x / r, y / r, 0.0)
        axis = _cross(dh, (0.0, 0.0, 1.0))         # d_hat x z_hat: rotates d_hat upward
        an = _norm(axis)
        axis = _scale(axis, 1.0 / an)
        return (x, y, z), axis, self.g.dish.tilt(r)

    def posts(self, d):
        c, axis, ang = self.block_pose(d)
        return [_add(c, _rotate(q, axis, ang)) for q in self._posts]

    def lengths(self, d):
        """Absolute stop-to-post free lengths (mm)."""
        return [_norm(_sub(a, p)) for a, p in zip(self._stops, self.posts(d))]

    def ik(self, d) -> list:
        """Cable coordinates l_i = L_i(d) - L_i(0) (mm) = G-code A, B, C."""
        L = self.lengths(d)
        return [L[i] - self.l0[i] for i in range(3)]

    def unit_vectors(self, d):
        """Unit vectors from each post toward its stop (direction of the cable pull on the yoke)."""
        out = []
        for a, p in zip(self._stops, self.posts(d)):
            v = _sub(a, p)
            out.append(_scale(v, 1.0 / _norm(v)))
        return out

    def jacobian(self, d, h=1e-4):
        """dl_i/dd (3 x 2), central differences."""
        x, y = d
        lx1, lx0 = self.ik((x + h, y)), self.ik((x - h, y))
        ly1, ly0 = self.ik((x, y + h)), self.ik((x, y - h))
        return [[(lx1[i] - lx0[i]) / (2 * h), (ly1[i] - ly0[i]) / (2 * h)] for i in range(3)]

    def condition(self, d) -> float:
        """Ratio of the singular values of the 3x2 Jacobian (1 = isotropic)."""
        J = self.jacobian(d)
        a = sum(J[i][0] ** 2 for i in range(3))
        b = sum(J[i][0] * J[i][1] for i in range(3))
        c = sum(J[i][1] ** 2 for i in range(3))
        tr, det = a + c, a * c - b * b
        disc = math.sqrt(max(tr * tr / 4 - det, 0.0))
        s1, s2 = tr / 2 + disc, tr / 2 - disc
        if s2 <= 0:
            return float("inf")
        return math.sqrt(s1 / s2)

    def fk(self, l, guess=(0.0, 0.0), tol=1e-9, iters=50):
        """Forward kinematics by Gauss-Newton: cable coordinates -> d (least squares, 3 eq / 2 unknowns)."""
        x, y = guess
        for _ in range(iters):
            f = self.ik((x, y))
            res = [f[i] - l[i] for i in range(3)]
            J = self.jacobian((x, y))
            a = sum(J[i][0] ** 2 for i in range(3))
            b = sum(J[i][0] * J[i][1] for i in range(3))
            c = sum(J[i][1] ** 2 for i in range(3))
            g0 = sum(J[i][0] * res[i] for i in range(3))
            g1 = sum(J[i][1] * res[i] for i in range(3))
            det = a * c - b * b
            if abs(det) < 1e-15:
                break
            dx = (c * g0 - b * g1) / det
            dy = (a * g1 - b * g0) / det
            x -= dx
            y -= dy
            if math.hypot(dx, dy) < tol:
                break
        return (x, y)

    def null_vector(self, d):
        """Positive tension distribution that exerts no net in-plane force (None if none exists:
        the cable directions do not positively span the plane -> a cable must go slack)."""
        u = self.unit_vectors(d)
        ux = [x[0] for x in u]
        uy = [x[1] for x in u]
        n = [ux[1] * uy[2] - ux[2] * uy[1], ux[2] * uy[0] - ux[0] * uy[2], ux[0] * uy[1] - ux[1] * uy[0]]
        if sum(n) < 0:
            n = [-x for x in n]
        return n if min(n) > 0 else None

    def tensions(self, d, f_ext_xy=(0.0, 0.0), total=4.5):
        """Predicted cable tensions (N) at pose d under an external in-plane force, with the
        common mode set by the floating stop plate (sum of tensions = `total`, 3 x 1.5 N).
        Any value < ~0.3 N means that cable goes slack (and the LM393 low window trips)."""
        u = self.unit_vectors(d)
        ux = [x[0] for x in u]
        uy = [x[1] for x in u]
        n = [ux[1] * uy[2] - ux[2] * uy[1], ux[2] * uy[0] - ux[0] * uy[2], ux[0] * uy[1] - ux[1] * uy[0]]
        if sum(n) < 0:
            n = [-x for x in n]
        tp = self.tension_change(d, f_ext_xy)
        c = (total - sum(tp)) / sum(n) if abs(sum(n)) > 1e-12 else 0.0
        return [tp[i] + c * n[i] for i in range(3)]

    def audit(self, fm=None, r_max=16.5, n_r=34, n_a=72, pins_total=2.2, total=4.5):
        """Workspace audit: min/max predicted tension over |d| <= r_max with the rim reaction
        (pins on) and without.  Returns dict(min_T, max_T, worst_d, reach_min)."""
        worst = (1e9, None)
        tmax = 0.0
        for i in range(n_r + 1):
            r = r_max * i / n_r
            for k in range(n_a):
                a = 2 * math.pi * k / n_a
                d = (r * math.cos(a), r * math.sin(a))
                for pins_on in (False, True):
                    F = fm.external(d, (0.0, 0.0), pins_total, pins_on) if fm else (0.0, 0.0)
                    T = self.tensions(d, F, total)
                    if min(T) < worst[0]:
                        worst = (min(T), d)
                    tmax = max(tmax, max(T))
        reach = r_max
        for k in range(n_a):
            a = 2 * math.pi * k / n_a
            r = 0.0
            while r <= r_max:
                if self.null_vector((r * math.cos(a), r * math.sin(a))) is None:
                    reach = min(reach, r)
                    break
                r += 0.1
        return {"min_T": worst[0], "worst_d": worst[1], "max_T": tmax, "reach_min": reach}

    def tension_change(self, d, f_ext_xy):
        """Minimum-norm cable tension changes (N) that balance an in-plane external force on the
        block (N, frame S).  Equilibrium: sum(dT_i * u_i) + F_ext = 0 (horizontal components);
        the common mode is absorbed by the floating stop plate (SPEC C17)."""
        u = self.unit_vectors(d)
        # A (2x3) dT = -F  ->  dT = A^T (A A^T)^-1 (-F)
        a = sum(ui[0] * ui[0] for ui in u)
        b = sum(ui[0] * ui[1] for ui in u)
        c = sum(ui[1] * ui[1] for ui in u)
        det = a * c - b * b
        fx, fy = -f_ext_xy[0], -f_ext_xy[1]
        lx = (c * fx - b * fy) / det
        ly = (a * fy - b * fx) / det
        return [ui[0] * lx + ui[1] * ly for ui in u]


# ------------------------------ compensation ------------------------------------------
@dataclass
class CableComp:
    """Per-cable dead-band compensation and series-spring feed-forward (SPEC §8.2 steps 4-5).

    * dead band: when dl_i/dt changes sign, the offset moves to sign * b_i / 2, spread over
      `spread_mm` of PATH length (not cable length) so no step is commanded.
    * spring feed-forward: l_cmd -= dT_i / k_i  (more tension stretches the spring, so reel in).
    """
    b: tuple = (0.0, 0.0, 0.0)          # mm, calibrated per cable at A3 (`cal deadband`)
    k: tuple = (1.2, 1.2, 1.2)          # N/mm, spring + cable in series per cable (SPEC §4.4)
    spread_mm: float = 3.0
    eps: float = 1e-4
    _dir: list = field(default_factory=lambda: [-1, -1, -1])   # homing approaches from +: last motion '-'
    _off: list = field(default_factory=lambda: [0.0, 0.0, 0.0])
    _from: list = field(default_factory=lambda: [0.0, 0.0, 0.0])
    _ramp_s: list = field(default_factory=lambda: [None, None, None])
    _last_l: list = field(default_factory=lambda: [None, None, None])

    def reset(self, last_direction=-1):
        self._dir = [last_direction] * 3
        self._off = [last_direction * bi / 2.0 for bi in self.b]
        self._from = list(self._off)
        self._ramp_s = [None, None, None]
        self._last_l = [None, None, None]

    def apply(self, l, s_path, dT=(0.0, 0.0, 0.0)):
        """l: geometric cable coordinates, s_path: cumulative path length (mm), dT: modelled
        tension changes (N).  Returns commanded cable coordinates."""
        out = []
        for i in range(3):
            li = l[i]
            if self._last_l[i] is not None:
                dl = li - self._last_l[i]
                if abs(dl) > self.eps:
                    sgn = 1 if dl > 0 else -1
                    if sgn != self._dir[i]:
                        self._dir[i] = sgn
                        self._from[i] = self._off[i]
                        self._ramp_s[i] = s_path
            self._last_l[i] = li
            target = self._dir[i] * self.b[i] / 2.0
            if self._ramp_s[i] is not None:
                u = (s_path - self._ramp_s[i]) / self.spread_mm
                if u >= 1.0:
                    self._off[i] = target
                    self._ramp_s[i] = None
                else:
                    u = max(u, 0.0)
                    self._off[i] = self._from[i] + (target - self._from[i]) * u
            else:
                self._off[i] = target
            out.append(li + self._off[i] - dT[i] / self.k[i])
        return out


def path_ik(ik: TendonIK, pts: Iterable, comp: CableComp | None = None, dT_fn=None):
    """Convert a sequence of (x, y) points to commanded cable coordinates."""
    out = []
    s = 0.0
    prev = None
    for p in pts:
        if prev is not None:
            s += math.hypot(p[0] - prev[0], p[1] - prev[1])
        prev = p
        l = ik.ik(p)
        if comp is not None:
            dT = dT_fn(p) if dT_fn else (0.0, 0.0, 0.0)
            l = comp.apply(l, s, dT)
        out.append(l)
    return out
