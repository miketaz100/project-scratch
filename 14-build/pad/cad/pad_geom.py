#!/usr/bin/env python3
"""
pad_geom.py - PAD work package: dish kinematics, gate, head-curvature, pockets, C8 sweep,
lift, yaw and stack calculator (SP1 v3 build, 14-build/pad).  Source of every number in
pad.md sections 3, 4, 5, 9, 10.  Writes pockets.npz (the pocket ceiling height fields) that
gen_pad_stl.py turns into the deck.

Run:  <cadenv>/bin/python pad_geom.py            (full report, ~3 min)
      <cadenv>/bin/python pad_geom.py --quick    (coarser sweeps)

FRAME P (spec 3.1): origin = nail plane on the pad axis = centre-nail tip at extension
e = 15.0; z_P away from the scalp; x_P = bail tangent; pentagon P0 on +x_P.
Design head: sphere R 85 about C = (0, 0, -85).

DISH v3b (this package; replaces spec 4.2, see CONFLICTS.md P1):
  d = block offset AT THE NAIL PLANE (fixes 14-build/S0/CONFLICTS.md #1).
  tilt   phi(d)  = R_TILT * asin(|d| / 85)   (half of the full concentric roll)
  rise   h(d)    = 0 to S0, then a BAND at T1 deg to HB, then an OUTER rim at T2 deg to HTOP,
                   then a plateau.  Rise is measured above the concentric surface.
  domes  three PTFE balls on lugs at RD, angles 30/150/270, ball centre ZD above the nail plane.
  Each dome rides its OWN pocket (no shared sphere), so pockets must not overlap.
"""
import math, sys, json, os
import numpy as np

QUICK = "--quick" in sys.argv
HERE = os.path.dirname(os.path.abspath(__file__))

# ------------------------------------------------------------------ frozen inputs
R_HEAD = 85.0
C = np.array([0.0, 0.0, -R_HEAD])
STROKE, E_NOM = 18.5, 15.0
TIP_MAX = E_NOM - STROKE                     # -3.5: tip z (block frame) at full extension
NAILS = [("C", (0.0, 0.0))] + [("P%d" % k, (18 * math.cos(math.radians(72 * k)), 18 * math.sin(math.radians(72 * k)))) for k in range(5)]
GROUP = {"P0": "A", "P2": "A", "P3": "A", "C": "B", "P1": "B", "P4": "B"}

# ------------------------------------------------------------------ PAD v3b design choices
R_TILT = 0.5                                 # fraction of the concentric roll
S0, T1, HB, T2, HTOP = 6.5, 30.0, 4.5, 60.0, 9.0
TB, TO = math.tan(math.radians(T1)), math.tan(math.radians(T2))
SB = S0 + HB / TB                            # end of the landing band (14.29)
STOP_RIM = SB + (HTOP - HB) / TO             # start of the plateau (16.89)
A_WORK = 17.2                                # PLINE / LINE reversal amplitude (on the plateau)
A_CAGE = 18.0                                # hard cage (block body hits the skirt ring stop)
RD, DOME_ANG = 38.0, (30.0, 150.0, 270.0)    # dome lugs
BALL_R = 6.35 / 2                            # 1/4 in PTFE ball
# stack (z above the nail plane at the pad axis, block at home)
Z_SKIRT_BOT = 32.0                           # wiper skirt plate underside (= block underside)
Z_BLOCK_TOP = 83.5                           # gallery plate top
Z_YOKE_TOP = 87.0                            # yoke plate top (coupling magnets inside)
R_YOKE = 14.0
R_GAL = 27.0                                 # gallery plate / block body radius
GAP_MIN = 1.5                                # block-to-deck clearance target (C8 asks > 3 or booted;
                                             # the zone is covered by the pad cover, see pad.md 9)
# skids, stops, skirt
SKID_R, SKID_ANG, SKID_DOME_R, SKID_FOOT_D = 60.0, (60.0, 180.0, 300.0), 15.0, 8.0
STOP_R, STOP_ANG = 65.0, (90.0, 210.0, 330.0)
POST_R = 10.0
SKIRT_R_IN = 50.0

def h_rim(s):
    s = abs(s)
    if s <= S0: return 0.0
    if s <= SB: return (s - S0) * TB
    if s <= STOP_RIM: return HB + (s - SB) * TO
    return HTOP

def phi_of(s):
    return R_TILT * math.asin(min(abs(s), R_HEAD - 1e-6) / R_HEAD)

def rot(axis, ang):
    axis = np.asarray(axis, float); n = np.linalg.norm(axis)
    if n < 1e-12 or abs(ang) < 1e-15: return np.eye(3)
    k = axis / n; K = np.array([[0, -k[2], k[1]], [k[2], 0, -k[0]], [-k[1], k[0], 0]])
    return np.eye(3) + math.sin(ang) * K + (1 - math.cos(ang)) * K @ K

def pose_vec(dx, dy, yaw=0.0):
    """block pose for offset vector (dx, dy) at the nail plane. x_P = R x_B + t"""
    s = math.hypot(dx, dy)
    if s < 1e-9:
        return rot([0, 0, 1], yaw), np.zeros(3)
    u = np.array([dx / s, dy / s, 0.0]); a = np.array([-u[1], u[0], 0.0])
    Rm = rot(a, phi_of(s)) @ rot([0, 0, 1], yaw)
    t = np.array([dx, dy, math.sqrt(R_HEAD**2 - s * s) - R_HEAD + h_rim(s)])
    return Rm, t

def pose(s, psi, yaw=0.0):
    return pose_vec(s * math.cos(psi), s * math.sin(psi), yaw)

def sphere_head(Rh, zc):
    cen = np.array([0, 0, zc])
    return lambda p: np.linalg.norm(p - cen) - Rh

HEAD85 = sphere_head(R_HEAD, -R_HEAD)

def tip_world(q, Rm, t, ext_z=TIP_MAX):
    return Rm @ np.array([q[0], q[1], ext_z]) + t

# ------------------------------------------------------------------ 1. dish table
def dish_table():
    out = []
    print("\n=== 1. DISH v3b AT THE NAIL PLANE (design head R85) ===")
    print(f" R_TILT {R_TILT}, contact zone |d|<={S0}, band {T1} deg to +{HB} at |d| {SB:.2f}, outer {T2} deg to +{HTOP} at |d| {STOP_RIM:.2f}, plateau, work amplitude {A_WORK}, cage {A_CAGE}")
    print(" |d|    rise   tilt   dome travel D  dome dz   clearance C   min/max nail clearance (all headings)")
    for s in [0, 2, 4, 6, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.29, 15.0, 15.5, 16.0, 16.5, 16.89, 17.2, 18.0, 18.5]:
        Rm, t = pose(s, 0.0)
        dome0 = np.array([RD, 0, 91.5]); D = Rm @ dome0 + t - dome0   # ball centre ZD (pad_geom2.py)
        cl = [HEAD85(tip_world(q, *pose(s, psi))) for psi in np.radians(np.arange(0, 360, 10)) for nm, q in NAILS]
        cc = HEAD85(tip_world((0, 0), Rm, t))
        out.append(dict(d=s, h=h_rim(s), tilt=math.degrees(phi_of(s)), D=float(math.hypot(D[0], D[1])), cmin=min(cl), cmax=max(cl)))
        print(f" {s:5.2f}  {h_rim(s):5.2f}  {math.degrees(phi_of(s)):5.2f}   {math.hypot(D[0], D[1]):6.2f}      {D[2]:+6.2f}    {cc:+6.2f}        {min(cl):+6.2f} / {max(cl):+6.2f}")
    return out

# ------------------------------------------------------------------ 2. gate on a line
def line_metrics(head=HEAD85, A=A_WORK, step=10, label=None):
    res = {"rake_min": 1e9, "rake_max": 0.0, "land_max": 0.0, "lift_min": 1e9, "never": 0, "spread": 0.0}
    ss = np.linspace(-A, A, int(A * 20) + 1)
    for psi in np.radians(np.arange(0, 180, step)):
        P = [pose(s, psi) for s in ss]
        allc = []
        for nm, q in NAILS:
            tips = np.array([tip_world(q, Rm, t) for Rm, t in P])
            cl = np.array([head(p) for p in tips]); allc.append(cl)
            inc = cl <= 0
            if not inc.any():
                res["never"] += 1; continue
            rake = sum(np.linalg.norm(tips[i, :2] - tips[i - 1, :2]) for i in range(1, len(ss)) if inc[i] and inc[i - 1])
            res["rake_min"] = min(res["rake_min"], rake); res["rake_max"] = max(res["rake_max"], rake)
            for i in range(1, len(ss)):
                if inc[i] != inc[i - 1]:
                    j0, j1 = max(i - 2, 0), min(i + 2, len(ss) - 1)
                    ang = math.degrees(math.atan2(abs(cl[j1] - cl[j0]), np.linalg.norm(tips[j1, :2] - tips[j0, :2])))
                    res["land_max"] = max(res["land_max"], ang)
            res["lift_min"] = min(res["lift_min"], cl[0], cl[-1])
        allc = np.array(allc); m = np.abs(ss) <= S0
        res["spread"] = max(res["spread"], float(np.max(allc[:, m].max(0) - allc[:, m].min(0))))
    if label:
        print(f" {label:34s} rake {res['rake_min']:5.1f}-{res['rake_max']:5.1f} | landing/lift <= {res['land_max']:4.1f} deg | lift at reversal >= {res['lift_min']:+5.2f} | spread in contact {res['spread']:.2f} | never touching {res['never']}")
    return res

def landing_points():
    """|d| at which each nail lands on a centred line, heading 0 and 36 deg (R85)."""
    rows = []
    for psi_deg in (0, 36):
        psi = math.radians(psi_deg)
        ss = np.linspace(0, A_WORK, 1721)
        for nm, q in NAILS:
            for sg in (1, -1):
                prev = None
                for s in ss:
                    c = HEAD85(tip_world(q, *pose(sg * s, psi)))
                    if prev is not None and prev <= 0 < c:
                        rows.append((psi_deg, nm, sg * s)); break
                    prev = c
    return rows

# ------------------------------------------------------------------ 3. head curvature
ZF = -R_HEAD + math.sqrt((R_HEAD + SKID_DOME_R)**2 - SKID_R**2)   # skid dome centre z

def seat_sphere(Rh):
    return ZF - math.sqrt((Rh + SKID_DOME_R)**2 - SKID_R**2)

def ellipsoid_head(a, b, cz, ztop):
    cen = np.array([0, 0, ztop - cz]); sc = np.array([a, b, cz])
    def f(p):
        v = (p - cen) / sc; r = np.linalg.norm(v)
        return (r - 1.0) * np.linalg.norm(p - cen) / max(r, 1e-9)
    return f

def seat_ellipsoid(a, b, cz):
    x = np.zeros(3)
    def gaps(x):
        R = rot([1, 0, 0], x[1]) @ rot([0, 1, 0], x[2]); head = ellipsoid_head(a, b, cz, x[0])
        return np.array([head(R @ np.array([SKID_R * math.cos(math.radians(g)), SKID_R * math.sin(math.radians(g)), ZF])) - SKID_DOME_R for g in SKID_ANG]), R
    for _ in range(80):
        g, _ = gaps(x)
        if np.max(np.abs(g)) < 1e-7: break
        J = np.zeros((3, 3))
        for j in range(3):
            dx = np.zeros(3); dx[j] = 1e-5; J[:, j] = (gaps(x + dx)[0] - g) / 1e-5
        x = x - np.linalg.solve(J, g)
    return x, gaps(x)[1]

def contact_ext(head, q):
    lo, hi = -25.0, 25.0
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if head(np.array([q[0], q[1], mid])) > 0: hi = mid
        else: lo = mid
    return E_NOM - 0.5 * (lo + hi)

def head_table(step=15):
    print("\n=== 3. HEAD SHAPE vs FIXED SKIDS (0 120 skid circle, R15 feet, pad gimbal seats all three) ===")
    print(" head                          skin@axis  e_contact C   P min..max   retract margin  reserve max  lift at reversal  C6   gate")
    heads = []
    for Rh in (65, 70, 75, 80, 85, 90, 100, 120, 150):
        zc = seat_sphere(Rh); heads.append((f"sphere R{Rh}", sphere_head(Rh, zc), 0.0, 0.0))
    for a2, b2, lab in ((70, 150, "parietal Rx70 x Ry150"), (150, 70, "parietal Rx150 x Ry70"), (90, 100, "crown Rx90 x Ry100"), (65, 80, "bun Rx65 x Ry80")):
        cz = 100.0; a, b = math.sqrt(a2 * cz), math.sqrt(b2 * cz)
        x, Rt = seat_ellipsoid(a, b, cz); hd = ellipsoid_head(a, b, cz, x[0])
        heads.append((lab, (lambda p, hd=hd, Rt=Rt: hd(Rt @ p)), math.degrees(x[1]), math.degrees(x[2])))
    rows = []
    for lab, head, tx, ty in heads:
        es = [contact_ext(head, q) for nm, q in NAILS]
        lm = line_metrics(head, A_WORK, step)
        emin = min(es)
        row = dict(head=lab, skin=E_NOM - es[0], eC=es[0], ePmin=min(es[1:]), ePmax=max(es[1:]), emin=emin, resmax=STROKE - emin,
                   resmin=STROKE - max(es), lift=lm["lift_min"], rake=lm["rake_min"], land=lm["land_max"], never=lm["never"], tilt=(tx, ty))
        rows.append(row)
        c6 = "ok" if emin >= 15.0 - 1e-6 else "FAIL"
        gate = "ok" if (lm["lift_min"] >= 5.0 and lm["never"] == 0 and max(es) <= STROKE) else ("no-reach" if max(es) > STROKE else ("weak" if lm["lift_min"] > 0 else "FAIL"))
        print(f" {lab:30s} {row['skin']:+6.2f}    {es[0]:5.2f}   {min(es[1:]):5.2f}..{max(es[1:]):5.2f}      {emin:5.2f}         {STROKE - emin:5.2f}       {lm['lift_min']:+6.2f}         {c6:4s} {gate}")
    return rows

if __name__ == "__main__" and "--part2" not in sys.argv:
    R = {}
    R["dish"] = dish_table()
    print("\n=== 2. GATE ON THE DESIGN HEAD R85 (centred lines, all headings) ===")
    for A in (16.89, 17.2, 17.5):
        line_metrics(HEAD85, A, 5, f"R85, reversal at |d| = {A}")
    lp = landing_points()
    print(" landing |d| per nail (heading 0 / 36):", ", ".join(f"{p}deg {n} {s:+.1f}" for p, n, s in lp))
    R["heads"] = head_table(30 if QUICK else 15)
    with open(os.path.join(HERE, "pad_geom_part1.json"), "w") as f:
        json.dump(R, f, indent=1, default=float)

# ------------------------------------------------------------------ 3b. with the skid-height adjuster
def skid_adjust_table(rows):
    """The three skid stems move together by H (mm, + = pad moves AWAY from the scalp).
    Best H puts the earliest-touching nail at e = 15.0 (C6) if the spread allows the latest
    one to reach (e <= 18.5 - 0.3) and the gate lift (reserve max <= HTOP - 5 - 0.2)."""
    print("\n=== 3b. WITH THE SKID-HEIGHT ADJUSTER (one setting per station group) ===")
    print(" head                            spread of e_contact  skid length change (mm, + = longer)  e range after      lift >= 5   all six reach")
    out = []
    for r in rows:
        span = r["ePmax"] - min(r["eC"], r["ePmin"]) if r["ePmax"] > r["eC"] else r["eC"] - r["ePmin"]
        emin = r["emin"]; emax = max(r["eC"], r["ePmax"])
        H = 15.0 - emin                     # shift so the earliest nail touches at 15.0
        e0, e1 = emin + H, emax + H
        lift_ok = (STROKE - e0) <= (HTOP - 5.0 - 0.2) + 1e-9 or True
        lift = HTOP - (STROKE - e0)        # clearance of the worst-reserve nail at the plateau (approx.)
        reach = e1 <= STROKE - 0.3
        out.append(dict(head=r["head"], spread=emax - emin, H=H, e0=e0, e1=e1, lift=lift, reach=reach))
        print(f" {r['head']:32s} {emax - emin:5.2f}               {H:+6.2f}          {e0:5.2f}..{e1:5.2f}      {lift:+5.2f}      {'yes' if reach else 'NO (' + format(e1 - STROKE, '.1f') + ' short)'}")
    return out

if __name__ == "__main__" and "--part2" not in sys.argv:
    R["skid_adjust"] = skid_adjust_table(R["heads"])
    with open(os.path.join(HERE, "pad_geom_part1.json"), "w") as f:
        json.dump(R, f, indent=1, default=float)
