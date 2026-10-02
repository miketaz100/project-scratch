#!/usr/bin/env python3
"""
pad_geom.py - PAD work package geometry, gate and clearance calculator (SP1 v3, 14-build/pad)

Every number in pad.md section 3 (dish), 4 (head-curvature reserve), 9 (C8 sweep) and
10 (yaw, lift) comes from this file.  Run:  <cadenv>/bin/python pad_geom.py [--short]

FRAME P (spec section 3.1): origin = nail plane at the pad axis = the centre nail tip at
extension e = 15.0 mm; z_P away from the scalp; x_P = bail tangent; pentagon P0 on +x_P.
Design head for the dish: sphere R 85 centred at C = (0, 0, -85).

BLOCK OFFSET d is measured AT THE NAIL PLANE (14-build/S0/CONFLICTS.md #1 fix):
  |d| <= S0 (7 mm): concentric zone, the block ROLLS about C, tilt phi = asin(|d|/85),
                     so every nail keeps its skin gap (pure concentric scrub).
  |d| >  S0:        rim zone. The tilt UNWINDS linearly to 0 at S1 (17 mm) while the block
                     rises h(|d|) above the concentric surface. Unwinding keeps the dome travel
                     <= 17 mm, so the three dome pockets still fit on R 22 (deck ~ 0 116),
                     instead of the 0 165 / 11 deg deck that a full roll would need.
"""
import math, sys
import numpy as np

SHORT = "--short" in sys.argv
R_HEAD = 85.0
C = np.array([0.0, 0.0, -R_HEAD])
S0, S1 = 7.0, 17.0            # concentric zone edge; rim top (tilt fully unwound)
RIM1_DEG, RIM2_DEG = 34.0, 50.0
S_RIM1 = 13.7                  # end of the 34 deg landing band
STROKE, E_NOM = 18.5, 15.0     # pin stroke; nominal contact extension (centre nail, R85)
TIP_MAX = E_NOM - STROKE       # tip z at full extension in block frame (-3.5)
PHI0 = math.asin(S0 / R_HEAD)

def h_rim(s):
    """block rise above the concentric surface at nail-plane offset s (mm)"""
    s = abs(s)
    if s <= S0: return 0.0
    if s <= S_RIM1: return (s - S0) * math.tan(math.radians(RIM1_DEG))
    h1 = (S_RIM1 - S0) * math.tan(math.radians(RIM1_DEG))
    if s <= S1: return h1 + (s - S_RIM1) * math.tan(math.radians(RIM2_DEG))
    return h1 + (S1 - S_RIM1) * math.tan(math.radians(RIM2_DEG))

def phi_of(s):
    s = abs(s)
    if s <= S0: return math.asin(s / R_HEAD)
    return max(0.0, PHI0 * (S1 - s) / (S1 - S0))

def rot(axis, ang):
    axis = np.asarray(axis, float); n = np.linalg.norm(axis)
    if n < 1e-12 or abs(ang) < 1e-15: return np.eye(3)
    k = axis / n; K = np.array([[0, -k[2], k[1]], [k[2], 0, -k[0]], [-k[1], k[0], 0]])
    return np.eye(3) + math.sin(ang) * K + (1 - math.cos(ang)) * K @ K

def pose(s, psi, yaw=0.0):
    """block pose for signed offset s along heading psi (rad). Returns (R, t): x_P = R x_B + t"""
    u = np.array([math.cos(psi), math.sin(psi), 0.0])
    a = np.array([-math.sin(psi), math.cos(psi), 0.0])
    sg = 1.0 if s >= 0 else -1.0
    ph = phi_of(s) * sg
    Rm = rot(a, ph) @ rot([0, 0, 1], yaw)
    sa = abs(s)
    if sa <= S0:
        t = C + rot(a, ph) @ np.array([0, 0, R_HEAD])
    else:
        z = math.sqrt(R_HEAD**2 - sa**2) - R_HEAD + h_rim(sa)
        t = np.array([s * u[0], s * u[1], z])
    return Rm, t

NAILS = [("C", (0.0, 0.0))] + [("P%d" % k, (18 * math.cos(math.radians(72 * k)), 18 * math.sin(math.radians(72 * k)))) for k in range(5)]
GROUP = {"P0": "A", "P2": "A", "P3": "A", "C": "B", "P1": "B", "P4": "B"}

def sphere_head(Rh, zc):
    """scalp sphere radius Rh centred on the axis at z = zc; returns signed-distance fn"""
    cen = np.array([0, 0, zc])
    return lambda p: np.linalg.norm(p - cen) - Rh

def clearance(nail_xy, s, psi, head=None, yaw=0.0):
    """gap between the nail tip at FULL extension and the scalp (>0 = lifted, <=0 = in contact)"""
    head = head or sphere_head(R_HEAD, -R_HEAD)
    Rm, t = pose(s, psi, yaw)
    tip = Rm @ np.array([nail_xy[0], nail_xy[1], TIP_MAX]) + t
    return head(tip), tip

# ---------------------------------------------------------------- 1. dish profile table
def dish_table():
    print("\n=== 1. DISH PROFILE AT THE NAIL PLANE (frame S, design head R85) ===")
    print(" |d| mm  rise h  tilt deg  dome travel D (R22, z+75)  centre-nail clr  min/max nail clr (psi 0..355)")
    for s in [0, 2, 4, 6, 7, 8, 8.5, 9, 10, 11, 12, 12.2, 13, 13.7, 14.5, 15, 15.5, 16, 16.5, 17]:
        Rm, t = pose(s, 0.0)
        dome0 = np.array([22.0, 0, 75.0])
        D = (Rm @ dome0 + t) - dome0
        cl = []
        for psi in np.radians(np.arange(0, 360, 5)):
            for nm, q in NAILS:
                cl.append(clearance(q, s, psi)[0])
        cc = clearance((0, 0), s, 0)[0]
        print(f" {s:5.1f}  {h_rim(s):5.2f}   {math.degrees(phi_of(s)):5.2f}     {math.hypot(D[0], D[1]):5.2f} (dz {D[2]:+5.2f})          {cc:+6.2f}        {min(cl):+6.2f} / {max(cl):+6.2f}")

# ---------------------------------------------------------------- 2. gate metrics on a line
def line_metrics(head=None, label="R85", A=17.0, verbose=True):
    """For each nail and heading: rake length (skin travel in contact over one pass),
    landing / lift angle (deg) and the clearance at the reversal point |d| = A."""
    res = {"rake_min": 1e9, "rake_max": 0, "land_max": 0, "lift_min_at_A": 1e9, "never": 0}
    ss = np.linspace(-A, A, 681)
    worst = None
    for psi in np.radians(np.arange(0, 180, 5)):
        for nm, q in NAILS:
            cls, tips = [], []
            for s in ss:
                c, tip = clearance(q, s, psi, head)
                cls.append(c); tips.append(tip)
            cls = np.array(cls); tips = np.array(tips)
            inc = cls <= 0
            if not inc.any():
                res["never"] += 1; continue
            rake = 0.0
            for i in range(1, len(ss)):
                if inc[i] and inc[i - 1]:
                    rake += np.linalg.norm(tips[i, :2] - tips[i - 1, :2])
            # landing angles at contact transitions
            for i in range(1, len(ss)):
                if inc[i] != inc[i - 1]:
                    j0, j1 = max(i - 3, 0), min(i + 3, len(ss) - 1)
                    dz = cls[j1] - cls[j0]; dx = np.linalg.norm(tips[j1, :2] - tips[j0, :2])
                    ang = math.degrees(math.atan2(abs(dz), dx))
                    res["land_max"] = max(res["land_max"], ang)
            res["rake_min"] = min(res["rake_min"], rake); res["rake_max"] = max(res["rake_max"], rake)
            lift = min(cls[0], cls[-1])
            if lift < res["lift_min_at_A"]:
                res["lift_min_at_A"] = lift; worst = (nm, round(math.degrees(psi)))
    if verbose:
        print(f" {label:22s} rake {res['rake_min']:5.1f}-{res['rake_max']:5.1f} mm | max landing/lift angle {res['land_max']:4.1f} deg | min lift at |d|={A}: {res['lift_min_at_A']:+5.2f} mm (nail {worst}) | nail-headings never touching: {res['never']}")
    return res

# ---------------------------------------------------------------- 3. skid seating on other heads
SKID_R, SKID_ANG, DOME_R15 = 58.0, (30.0, 150.0, 270.0), 15.0
ZF = -R_HEAD + math.sqrt((R_HEAD + DOME_R15)**2 - SKID_R**2)   # skid dome centre z (touch R85)

def seat_sphere(Rh):
    """pad on 3 skids (R15 domes on R58) seated on an isotropic head of radius Rh:
    returns z of the head centre in P (head axis = pad axis by symmetry)."""
    return ZF - math.sqrt((Rh + DOME_R15)**2 - SKID_R**2)

def ellipsoid_head(a, b, cz, ztop):
    """scalp = ellipsoid semi-axes a (x), b (y), cz (z), top at z = ztop; signed distance
    approximated by the scaled-radius method (adequate within a few mm of the surface)."""
    cen = np.array([0, 0, ztop - cz])
    def f(p):
        v = (p - cen) / np.array([a, b, cz])
        r = np.linalg.norm(v)
        # distance along the ray to the surface, in mm
        return (r - 1.0) * np.linalg.norm(p - cen) / max(r, 1e-9)
    return f

def seat_ellipsoid(a, b, cz):
    """find ztop and pad tilt so all three skid domes touch (gimbal = 2 tilts + height).
    Small-angle: solve for (ztop, tx, ty) with Newton on the three dome-surface gaps."""
    x = np.array([0.0, 0.0, 0.0])  # ztop, tilt about x, tilt about y (rad)
    def gaps(x):
        ztop, tx, ty = x
        R = rot([1, 0, 0], tx) @ rot([0, 1, 0], ty)
        head = ellipsoid_head(a, b, cz, ztop)
        g = []
        for ang in SKID_ANG:
            p = R @ np.array([SKID_R * math.cos(math.radians(ang)), SKID_R * math.sin(math.radians(ang)), ZF])
            g.append(head(p) - DOME_R15)
        return np.array(g), R
    for _ in range(60):
        g, _ = gaps(x)
        J = np.zeros((3, 3)); eps = 1e-4
        for j in range(3):
            dx = np.zeros(3); dx[j] = eps
            J[:, j] = (gaps(x + dx)[0] - g) / eps
        x = x - np.linalg.solve(J, g)
        if np.max(np.abs(g)) < 1e-6: break
    return x, gaps(x)[1]

def head_reserve_table():
    print("\n=== 3. HEAD CURVATURE vs FIXED SKIDS (0 116, R15 domes): centre-skin offset and gate ===")
    print(" head                      skin@axis  e_contact C / P(min..max)  retract margin  reserve max  lift@|d|17 (min)  C6 ok  gate ok")
    rows = []
    for Rh in [65, 70, 75, 80, 85, 90, 100, 120, 150]:
        zc = seat_sphere(Rh)
        head = sphere_head(Rh, zc)
        top = zc + Rh
        ec = E_NOM + top    # centre nail contacts where its tip reaches the skin
        eps_ = []
        for nm, q in NAILS[1:]:
            # extension at contact for pentagon nail at home = 15 - (skin z at q)
            zs = zc + math.sqrt(Rh**2 - q[0]**2 - q[1]**2)
            eps_.append(E_NOM - zs)
        e_all = [E_NOM - top] + eps_
        rm = min(e_all); res_max = STROKE - rm if False else STROKE - min(e_all)
        lm = line_metrics(head, "", 17.0, verbose=False)
        rows.append((f"sphere R{Rh}", top, E_NOM - top, min(eps_), max(eps_), min(e_all), STROKE - min(e_all), lm["lift_min_at_A"]))
    for (a, b, cz, lab) in [(math.sqrt(70 * 100), math.sqrt(150 * 100), 100.0, "side Rx70 x Ry150"),
                            (math.sqrt(150 * 100), math.sqrt(70 * 100), 100.0, "side Rx150 x Ry70"),
                            (math.sqrt(90 * 100), math.sqrt(100 * 100), 100.0, "crown Rx90 x Ry100")]:
        x, Rt = seat_ellipsoid(a, b, cz)
        ztop = x[0]
        head = ellipsoid_head(a, b, cz, ztop)
        # head in pad frame: undo pad tilt by rotating points into head frame
        headP = lambda p, head=head, Rt=Rt: head(Rt @ p)
        es = []
        for nm, q in NAILS:
            # contact extension: bisect tip z
            lo, hi = -15.0, 15.0
            for _ in range(50):
                mid = 0.5 * (lo + hi)
                if headP(np.array([q[0], q[1], mid])) > 0: hi = mid
                else: lo = mid
            es.append(E_NOM - 0.5 * (lo + hi))
        lm = line_metrics(headP, "", 17.0, verbose=False)
        rows.append((lab + f" (tilt {math.degrees(x[1]):+.1f}/{math.degrees(x[2]):+.1f})", E_NOM - es[0], es[0], min(es[1:]), max(es[1:]), min(es), STROKE - min(es), lm["lift_min_at_A"]))
    for r in rows:
        lab, top, ec, pmin, pmax, emin, resmax, lift = r
        c6 = "yes" if emin >= 15.0 - 1e-6 else "NO"
        gate = "yes" if lift >= 5.0 else ("weak" if lift > 0 else "NO")
        print(f" {lab:34s} {top:+6.2f}    {ec:5.2f} / {pmin:5.2f}..{pmax:5.2f}       {emin:5.2f}        {resmax:5.2f}       {lift:+6.2f}        {c6:4s}  {gate}")
    return rows

if __name__ == "__main__":
    dish_table()
    print("\n=== 2. GATE ON THE DESIGN HEAD (PLINE through the centre, all headings) ===")
    for A in (16.0, 16.5, 17.0):
        line_metrics(None, f"R85, amplitude {A}", A)
    head_reserve_table()
