#!/usr/bin/env python
"""
dish_kinematics.py - S0a dish bench: dish profile, block kinematics, template paths, predictions
(PROJECT SCRATCH, 14-build/S0/cad, S0 kit engineer, 2026-10-02)

What it does
  1. Defines the dome-centre (ball-centre) surface of each dish pocket from SYSTEM-SPEC-v3 sec 4.2,
     read literally (d = ball offset measured at the dish): concentric sphere R_DC = 157 about the
     ball centre C, plus a rise straight up the pad axis that depends only on the ball's lateral
     offset rho from its home ("z-lift"): 0 to rho 7; 34 deg to 13.7 (+4.52); 50 deg to 17.0
     (+8.45); 70 deg stop wall to 18.5.
  2. Builds the printed CEILING as the exact upper envelope of the 6 mm ball swept over that surface
     and writes it as a closed polyhedron (pocket_cavity.scad for OpenSCAD, pocket_mesh.json for
     gen_s0_stl.py).
  3. Solves the rigid block pose (rotation about C + translation, yaw held at 0 by the two template
     styli) for any block offset d, with all three balls on their surfaces.
  4. Converts the wanted d-paths (LINE star + chords, D-path, offset CIRCLE) into the stylus
     paths the templates must carry (template_paths.scad, dish_geometry.json), and predicts what
     the bench should measure: contact length at the dish, ink rake on the ball, turnaround
     clearance, landing angle, block rise and tilt, stylus vertical travel.
  (dish_geometry.json also keeps "ceiling_profile", a superseded tilted-axis revolve profile used
   only for comparison in CONFLICTS #4.)

Frame: C = ball (scalp) centre = origin, +Z = deck axis (up, away from the scalp).
Dome homes at lateral radius A_DOME on 90/210/330 deg.  Nails (group-A triangle of the spec,
P0/P2/P3) at R 18 on 0/144/216 deg, axes parallel to the block axis.

Run:  <cadenv>/bin/python dish_kinematics.py      (numpy only)
"""
import json, math, os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))

# ---------------- frozen numbers (SYSTEM-SPEC-v3 sec 4.1, 4.2) ----------------
R_SCALP = 85.0          # ball / crown radius
R_CEIL = 160.0          # dish sphere (spec: "sphere R 160 about the scalp centre")
RB = 3.0                # Delrin ball radius (6 mm balls; 1/4 in balls = 3.175, 0.18 mm higher, ignore)
R_DC = R_CEIL - RB      # dome-centre sphere, 157
SIG_SPH, SIG_IN, SIG_OUT, SIG_STOP = 7.0, 13.7, 17.0, 18.5
ANG_IN, ANG_OUT, ANG_STOP = 34.0, 50.0, 70.0
A_DOME = 26.0           # bench: R 26 (spec M11 says R 22; see CONFLICTS.md #1)
DOME_ANG = (90.0, 210.0, 330.0)
NAIL_R = 18.0
NAIL_ANG = (0.0, 144.0, 216.0)   # P0, P2, P3 = group A
RESERVE = 2.0           # design reserve at d = 0 on R 85 (spec 1-3.5); nail N30 gives 3.0
D_MAX = 16.5            # path checker: |d| <= 16.5
STYLUS_Z = 187.0        # stylus mid-engagement height above C (deck top 175 + template 19 - 7)
STYLUS2_Y = -30.0       # second stylus, 30 mm toward the C-arm (-Y), same height

# ---------------- VARIANT V2: corrected (nail-plane) dish, Director ruling 2026-10-02 ----------------
# DISH_VARIANT=v2 builds the second bench deck.  The profile is specified AT THE NAIL PLANE and
# scaled to the dish by K = R_DC / R_SCALP (block rotates about C, so the dish moves K x the nails):
#   sphere to 6.0 mm; inner rim 30 deg, +4.5 mm (to 13.79); outer rim 50 deg, +4.5 mm (to 17.57);
#   turnaround at 17.07 mm (nail plane) = 31.5 mm at the dish; 70 deg (dish) stop wall 1.5 mm beyond.
# Chosen as the smallest grid point (v2 search, CONFLICTS #1 note) with rake >= 17, landing <= 35,
# turnaround clearance >= 5 at reserve 2.0.
VARIANT = os.environ.get("DISH_VARIANT", "v1")
SUF = "" if VARIANT == "v1" else "_v2"
K_NAIL = R_DC / R_SCALP
V2 = dict(s0=6.0, ain=30.0, rin=4.5, aout=50.0, rout=4.5)
if VARIANT == "v2":
    _e_in = V2["s0"] + V2["rin"] / math.tan(math.radians(V2["ain"]))
    _e_out = _e_in + V2["rout"] / math.tan(math.radians(V2["aout"]))
    A_DOME = 44.0
    DOME_ANG = (90.0, 210.0, 330.0)
    D_MAX = round((_e_out - 0.5) * K_NAIL, 2)          # 31.53 at the dish
    SIG_STOP = round(_e_out * K_NAIL + 1.5, 2)         # 33.95
    STYLUS_Z = 192.5                                   # V2 stack: deck top 180.5, template top 199.5, stylus mid-engagement
    STYLUS2_Y = 30.0                                   # (V2 uses only stylus 1, the lift rod; S2 paths unused)

# ---------------- 1. dome-centre path in local polar coords (sigma, r) ----------------
def rise_of_sigma(s):
    s = abs(s)
    if s <= SIG_SPH:
        return 0.0
    r = 0.0
    a = min(s, SIG_IN) - SIG_SPH
    r += a * math.tan(math.radians(ANG_IN))
    if s > SIG_IN:
        a = min(s, SIG_OUT) - SIG_IN
        r += a * math.tan(math.radians(ANG_OUT))
    if s > SIG_OUT:
        a = min(s, SIG_STOP) - SIG_OUT
        r += a * math.tan(math.radians(ANG_STOP))
    return r

if VARIANT == "v2":
    def rise_of_sigma(s):
        n = abs(s) / K_NAIL
        r = 0.0
        if n > V2["s0"]:
            r += (min(n, _e_in) - V2["s0"]) * math.tan(math.radians(V2["ain"]))
        if n > _e_in:
            r += (min(n, _e_out) - _e_in) * math.tan(math.radians(V2["aout"]))
        if n > _e_out:
            r += (abs(s) - _e_out * K_NAIL) * math.tan(math.radians(ANG_STOP))
        return r

def r_of_sigma(s):
    return R_DC + rise_of_sigma(s)

def centre_path(n_sph=8):
    """dome-centre path as (rho, s) points in the pocket meridian plane (rho radial from the
    pocket axis, s along it from C), sigma from 0 to SIG_STOP."""
    sig = list(np.linspace(0, SIG_SPH, n_sph)) + [SIG_IN, SIG_OUT, SIG_STOP]
    pts = []
    for sg in sig:
        th = sg / R_DC
        r = r_of_sigma(sg)
        pts.append((r * math.sin(th), r * math.cos(th)))
    return pts

def offset_polyline(pts, d):
    """offset an open polyline (rho increasing) by d to the side AWAY from C (outer side).
    Segments are offset along their normals; consecutive offset lines are intersected
    (the path is convex toward C, so the outer offsets intersect without arcs)."""
    segs = []
    for (x0, y0), (x1, y1) in zip(pts[:-1], pts[1:]):
        tx, ty = x1 - x0, y1 - y0
        L = math.hypot(tx, ty)
        tx, ty = tx / L, ty / L
        nx, ny = -ty, tx            # left normal; for rho increasing and s ~ R, this points to +s (away from C)
        segs.append(((x0 + d * nx, y0 + d * ny), (x1 + d * nx, y1 + d * ny)))
    out = [segs[0][0]]
    for (a0, a1), (b0, b1) in zip(segs[:-1], segs[1:]):
        # intersect line a0-a1 with b0-b1
        ax, ay = a1[0] - a0[0], a1[1] - a0[1]
        bx, by = b1[0] - b0[0], b1[1] - b0[1]
        den = ax * by - ay * bx
        if abs(den) < 1e-12:
            out.append(a1)
            continue
        t = ((b0[0] - a0[0]) * by - (b0[1] - a0[1]) * bx) / den
        out.append((a0[0] + t * ax, a0[1] + t * ay))
    out.append(segs[-1][1])
    return out

# ---------------- geometry helpers ----------------
def rotmat(w):
    th = np.linalg.norm(w)
    if th < 1e-15:
        return np.eye(3)
    k = w / th
    K = np.array([[0, -k[2], k[1]], [k[2], 0, -k[0]], [-k[1], k[0], 0]])
    return np.eye(3) + math.sin(th) * K + (1 - math.cos(th)) * K @ K

def deg(a):
    return math.radians(a)

H = [np.array([A_DOME * math.cos(deg(a)), A_DOME * math.sin(deg(a)), math.sqrt(R_DC**2 - A_DOME**2)]) for a in DOME_ANG]
AX = [h / np.linalg.norm(h) for h in H]
ZQ = H[0][2]                       # reference point on the block axis at dome-centre height
Z_TIPMAX = math.sqrt(R_SCALP**2 - NAIL_R**2) - RESERVE
NAILS = [np.array([NAIL_R * math.cos(deg(a)), NAIL_R * math.sin(deg(a)), Z_TIPMAX]) for a in NAIL_ANG]

def dome_surface_z(xy, i):
    """dome-centre surface of pocket i (z-lift model, see header): concentric sphere R_DC about C
    plus a rise straight up the deck axis that depends only on the ball's lateral offset rho from
    its home.  Rotation about C therefore moves all three balls the same rho, and the rim lifts
    the block without adding tilt."""
    rho = math.hypot(xy[0] - H[i][0], xy[1] - H[i][1])
    return math.sqrt(R_DC**2 - xy[0]**2 - xy[1]**2) + rise_of_sigma(rho)

def residual(x, d):
    w = np.array([x[0], x[1], 0.0])
    t = np.array([x[2], x[3], x[4]])
    R = rotmat(w)
    res = []
    for i, h in enumerate(H):
        W = R @ h + t
        res.append(W[2] - dome_surface_z(W[:2], i))
    Q = R @ np.array([0, 0, ZQ]) + t
    res += [Q[0] - d[0], Q[1] - d[1]]
    return np.array(res)

def solve_pose(d, x0=None):
    d = np.asarray(d, float)
    x = np.array([-d[1] / R_DC, d[0] / R_DC, 0, 0, 0]) if x0 is None else np.array(x0, float)
    for _ in range(60):
        f = residual(x, d)
        if np.max(np.abs(f)) < 1e-9:
            break
        J = np.zeros((5, 5))
        for j in range(5):
            dx = np.zeros(5); dx[j] = 1e-7
            J[:, j] = (residual(x + dx, d) - f) / 1e-7
        x = x - np.linalg.lstsq(J, f, rcond=None)[0]
    return x

def pose_points(x):
    R = rotmat(np.array([x[0], x[1], 0.0]))
    t = np.array([x[2], x[3], x[4]])
    return R, t

def nail_state(R, t, n):
    """returns (gap, along) : gap > 0 = clearance above the ball along the nail axis (lifted),
    gap < 0 = nail pushed back by -gap (in contact).  Uses the max-extended tip."""
    W = R @ n + t
    u = R @ np.array([0, 0, 1.0])
    # |W - lam*u| = R_SCALP  -> lam^2 - 2 lam (W.u) + |W|^2 - R^2 = 0, smallest positive root
    b = W @ u
    c = W @ W - R_SCALP**2
    disc = b * b - c
    if disc < 0:
        return 99.0, W
    lam = b - math.sqrt(disc)
    return lam, W

# ---------------- paths in d (block offset) ----------------
def line(psi, e=0.0, n=67):
    c, s = math.cos(deg(psi)), math.sin(deg(psi))
    half = math.sqrt(max(D_MAX**2 - e**2, 0))
    out = []
    for u in np.linspace(-half, half, n):
        out.append((u * c - e * s, u * s + e * c))
    return out

def dpath(psi=0.0, rr=15.75, n=40):
    c, s = math.cos(deg(psi)), math.sin(deg(psi))
    pts = [(u, 0.0) for u in np.linspace(-rr, rr, n)]
    pts += [(rr * math.cos(a), rr * math.sin(a)) for a in np.linspace(0, math.pi, n)[1:]]
    return [(x * c - y * s, x * s + y * c) for x, y in pts]

def circle(R=11.5, e=3.5, n=96):
    return [(e + R * math.cos(a), R * math.sin(a)) for a in np.linspace(0, 2 * math.pi, n)]

_KT = K_NAIL if VARIANT == "v2" else 1.0
TEMPLATES = {
    "T1_line_star": [line(0), line(45), line(90), line(135), line(0, 5.0 * _KT), line(0, 9.0 * _KT)],
    "T2_dpath": [dpath(0, rr=(15.75 / 16.5) * D_MAX)],
    "T3_circle": [circle(R=11.5 * _KT, e=3.5 * _KT, n=144 if _KT > 1 else 96)],
}

def stylus_xy(R, t, y_off=0.0):
    S = R @ np.array([0.0, y_off, STYLUS_Z]) + t
    return S

def analyse():
    out = {"params": dict(R_SCALP=R_SCALP, R_CEIL=R_CEIL, RB=RB, A_DOME=A_DOME, RESERVE=RESERVE,
                          STYLUS_Z=STYLUS_Z, STYLUS2_Y=STYLUS2_Y, Z_TIPMAX=Z_TIPMAX, ZQ=ZQ)}
    # ceiling profile
    cp = centre_path()
    ceil = offset_polyline(cp, RB)
    out["centre_path"] = cp
    out["ceiling_profile"] = ceil
    # radial sweep along the 3 nail-relevant headings to get rise / tilt / lift / chord
    rows = []
    zmin_s, zmax_s = 1e9, -1e9
    worst_lift_rim = 1e9
    chord = {}
    landing = []
    for psi in range(0, 360, 15):
        c, s = math.cos(deg(psi)), math.sin(deg(psi))
        prev = None
        xg = None
        contact = {j: [] for j in range(3)}
        for u in np.linspace(-D_MAX, D_MAX, 331):
            d = (u * c, u * s)
            xg = solve_pose(d, xg)
            R, t = pose_points(xg)
            for yo in (0.0, STYLUS2_Y):
                S = stylus_xy(R, t, yo)
                zmin_s = min(zmin_s, S[2] - STYLUS_Z - (yo and 0))
                zmax_s = max(zmax_s, S[2] - STYLUS_Z)
            for j, n in enumerate(NAILS):
                lam, W = nail_state(R, t, n)
                if lam < 0:
                    contact[j].append(u)
                if abs(u) >= SIG_IN:
                    worst_lift_rim = min(worst_lift_rim, lam)
        for j in range(3):
            if contact[j]:
                chord.setdefault(j, []).append(max(contact[j]) - min(contact[j]))
    out["stylus_dz_range"] = (zmin_s, zmax_s)
    out["worst_lift_at_rim_13p7"] = worst_lift_rim
    out["chord_range_per_nail"] = {j: (min(v), max(v)) for j, v in chord.items()}
    # rise and tilt along psi = 0
    prof = []
    xg = None
    for u in np.linspace(0, D_MAX, 34):
        xg = solve_pose((u, 0), xg)
        R, t = pose_points(xg)
        Q = R @ np.array([0, 0, ZQ]) + t
        tilt = math.degrees(math.acos(max(-1, min(1, (R @ np.array([0, 0, 1.0]))[2]))))
        rise = np.linalg.norm(Q) - ZQ
        lifts = [nail_state(R, t, n)[0] for n in NAILS]
        prof.append((round(u, 2), round(rise, 2), round(tilt, 2), [round(l, 2) for l in lifts]))
    out["profile_psi0"] = prof
    # landing angle: tip velocity vs local ball tangent at touchdown, line through centre, 1 mm/step
    angs = []
    for psi in range(0, 360, 30):
        c, s = math.cos(deg(psi)), math.sin(deg(psi))
        xg = None
        traj = {j: [] for j in range(3)}
        for u in np.linspace(D_MAX, -D_MAX, 661):       # moving inward from the rim
            xg = solve_pose((u * c, u * s), xg)
            R, t = pose_points(xg)
            for j, n in enumerate(NAILS):
                lam, W = nail_state(R, t, n)
                traj[j].append((lam, W))
        for j in range(3):
            tr = traj[j]
            for k in range(1, len(tr)):
                if tr[k - 1][0] > 0 >= tr[k][0]:
                    W0, W1 = tr[k - 1][1], tr[k][1]
                    v = W1 - W0
                    nrm = W1 / np.linalg.norm(W1)
                    vn = -(v @ nrm)
                    vt = np.linalg.norm(v - (v @ nrm) * nrm)
                    angs.append(math.degrees(math.atan2(vn, vt)))
                    break
    out["landing_angle_deg"] = (min(angs), max(angs)) if angs else None
    # template stylus paths
    tpl = {}
    for name, paths in TEMPLATES.items():
        P1, P2 = [], []
        for path in paths:
            xg = None
            p1, p2 = [], []
            for d in path:
                xg = solve_pose(d, xg)
                R, t = pose_points(xg)
                S1 = stylus_xy(R, t, 0.0)
                S2 = stylus_xy(R, t, STYLUS2_Y)
                p1.append((round(float(S1[0]), 3), round(float(S1[1]), 3)))
                p2.append((round(float(S2[0]), 3), round(float(S2[1]), 3)))
            P1.append(p1)
            P2.append(p2)
        tpl[name] = {"stylus1": P1, "stylus2": P2}
    out["templates"] = tpl
    return out


# ---------------- heightfield ceiling (z-lift model) ----------------
R_POCKET = 21.0 if VARIANT == "v1" else 37.0   # cavity radius around each ball home (ball reach + 3)
def ceiling_heightfield(n_ring=None, n_ang=None, step=0.15):
    """Ceiling of the pocket whose ball home is H[0] (90 deg), in DECK coordinates.
    Exact upper envelope of the 6 mm ball swept over the dome-centre surface.
    Returns (rings, angs, Z) with Z[k][j] at rho = rings[k], angle angs[j] about the
    vertical axis through the ball home."""
    n_ring = n_ring or (43 if VARIANT == "v1" else 62)
    n_ang = n_ang or (120 if VARIANT == "v1" else 160)
    hx, hy = H[0][0], H[0][1]
    g = np.arange(-SIG_STOP, SIG_STOP + 1e-9, step)
    GX, GY = np.meshgrid(g, g, indexing="ij")
    RHO = np.hypot(GX, GY)
    X, Y = GX + hx, GY + hy
    rise = np.vectorize(rise_of_sigma)(RHO)
    ZC = np.sqrt(R_DC**2 - X**2 - Y**2) + rise
    ZC[RHO > SIG_STOP] = -1e9
    rings = np.linspace(0, R_POCKET, n_ring + 1)
    angs = np.linspace(0, 2 * math.pi, n_ang, endpoint=False)
    Z = np.zeros((len(rings), n_ang))
    w = int(math.ceil(RB / step)) + 1
    i0 = len(g) // 2
    for k, r in enumerate(rings):
        for j, a in enumerate(angs):
            px, py = r * math.cos(a), r * math.sin(a)
            ci, cj = i0 + int(round(px / step)), i0 + int(round(py / step))
            a0, a1 = max(ci - w, 0), min(ci + w + 1, len(g))
            b0, b1 = max(cj - w, 0), min(cj + w + 1, len(g))
            dx = GX[a0:a1, b0:b1] - px
            dy = GY[a0:a1, b0:b1] - py
            d2 = dx * dx + dy * dy
            m = d2 <= RB * RB
            zc = ZC[a0:a1, b0:b1]
            cand = zc[m] + np.sqrt(RB * RB - d2[m])
            Z[k, j] = cand.max() if cand.size else np.nan
            if k == 0:
                Z[k, :] = Z[k, j]
                break
    # outermost rings that the ball cannot reach: hold the last valid value (vertical wall)
    for k in range(1, len(rings)):
        bad = ~np.isfinite(Z[k]) | (Z[k] < 0)
        Z[k][bad] = Z[k - 1][bad]
    return rings, angs, Z

def write_scad_pocket(rings, angs, Z, z_bot):
    """closed polyhedron of one pocket cavity in pocket-local XY (origin at the ball home),
    absolute Z.  top = ceiling, flat bottom at z_bot, vertical wall at R_POCKET."""
    pts, faces = [], []
    pts.append((0.0, 0.0, float(Z[0][0])))                      # 0: top centre
    na = len(angs)
    def vid(k, j):
        return 1 + (k - 1) * na + (j % na)
    for k in range(1, len(rings)):
        for j, a in enumerate(angs):
            pts.append((rings[k] * math.cos(a), rings[k] * math.sin(a), float(Z[k][j])))
    nb = len(pts)
    for j, a in enumerate(angs):                                # bottom ring
        pts.append((rings[-1] * math.cos(a), rings[-1] * math.sin(a), z_bot))
    pts.append((0.0, 0.0, z_bot))                               # bottom centre
    bc = len(pts) - 1
    for j in range(na):                                         # top fan (normals out = up)
        faces.append((0, vid(1, j + 1), vid(1, j)))
    for k in range(1, len(rings) - 1):
        for j in range(na):
            a, b, c, d = vid(k, j), vid(k, j + 1), vid(k + 1, j + 1), vid(k + 1, j)
            faces.append((a, b, c)); faces.append((a, c, d))
    K = len(rings) - 1
    for j in range(na):                                         # wall
        a, b = vid(K, j), vid(K, j + 1)
        c, d = nb + ((j + 1) % na), nb + j
        faces.append((a, b, c)); faces.append((a, c, d))
    for j in range(na):                                         # bottom fan
        faces.append((bc, nb + j, nb + ((j + 1) % na)))
    return pts, faces

def scalp_metrics():
    """what the ink on the ball will show: arc length of each nail's contact trace and the
    turnaround clearance, for lines through the centre at 24 headings."""
    res = {"scalp_chord": [], "turn_lift": [], "land": []}
    for psi in range(0, 360, 15):
        c, s = math.cos(deg(psi)), math.sin(deg(psi))
        xg = None
        tips = {j: [] for j in range(3)}
        for u in np.linspace(-D_MAX, D_MAX, 331):
            xg = solve_pose((u * c, u * s), xg)
            R, t = pose_points(xg)
            for j, n in enumerate(NAILS):
                lam, W = nail_state(R, t, n)
                tips[j].append((lam, W))
        for j in range(3):
            pts = [W for lam, W in tips[j] if lam < 0]
            if len(pts) > 1:
                a = pts[0] / np.linalg.norm(pts[0]); b = pts[-1] / np.linalg.norm(pts[-1])
                res["scalp_chord"].append(R_SCALP * math.acos(max(-1, min(1, a @ b))))
            res["turn_lift"].append(min(tips[j][0][0], tips[j][-1][0]))
    return {k: (round(min(v), 2), round(max(v), 2)) for k, v in res.items() if v}

def write_scad_profile(ceil, cp):
    with open(os.path.join(HERE, "pocket_profile.scad"), "w") as f:
        f.write("// pocket_profile.scad - GENERATED by dish_kinematics.py, do not edit by hand.\n")
        f.write("// Dish pocket ceiling in the pocket meridian plane: [rho, s] with rho radial from the\n")
        f.write("// pocket axis (C -> ball home) and s along that axis measured from the ball centre C.\n")
        f.write(f"// Dome-centre path: sphere R {R_DC} to sigma {SIG_SPH}; {ANG_IN} deg to {SIG_IN}; {ANG_OUT} deg to {SIG_OUT}; {ANG_STOP} deg stop to {SIG_STOP}.\n")
        f.write(f"// Ceiling = that path offset {RB} mm outward (6 mm Delrin ball).\n")
        f.write("POCKET_CEIL = [" + ", ".join(f"[{p[0]:.3f}, {p[1]:.3f}]" for p in ceil) + "];\n")
        f.write("POCKET_CENTRE_PATH = [" + ", ".join(f"[{p[0]:.3f}, {p[1]:.3f}]" for p in cp) + "];\n")

def write_scad_templates(tpl):
    with open(os.path.join(HERE, f"template_paths{SUF}.scad"), "w") as f:
        f.write("// template_paths.scad - GENERATED by dish_kinematics.py, do not edit by hand.\n")
        f.write("// Stylus paths [x, y] in the DECK frame (mm), already corrected for the block's rotation\n")
        f.write(f"// about the ball centre (stylus contact height {STYLUS_Z} mm above C).  Two styli: S1 on the\n")
        f.write(f"// block axis, S2 at y = {STYLUS2_Y} mm.\n")
        for name, v in tpl.items():
            for k, key in ((1, "stylus1"), (2, "stylus2")):
                paths = v[key]
                f.write(f"{SUF.upper().lstrip('_') + '_' if SUF else ''}{name}_S{k} = [" + ", ".join("[" + ", ".join(f"[{p[0]:.2f}, {p[1]:.2f}]" for p in path) + "]" for path in paths) + "];\n")

if __name__ == "__main__":
    o = analyse()
    write_scad_templates(o["templates"])
    with open(os.path.join(HERE, f"dish_geometry{SUF}.json"), "w") as f:
        json.dump(o, f, indent=1)
    print("ceiling profile (rho, s):")
    for p in o["ceiling_profile"]:
        print(f"   {p[0]:7.3f} {p[1]:8.3f}")
    print("u  rise  tilt  lift(P0,P2,P3)   (psi = 0)")
    for r in o["profile_psi0"]:
        print("  ", r)
    print("stylus dz range (mm):", o["stylus_dz_range"])
    print("worst nail clearance for |d| >= 13.7 (mm):", round(o["worst_lift_at_rim_13p7"], 2))
    print("contact chord per nail over 24 headings (mm):", {k: (round(a, 1), round(b, 1)) for k, (a, b) in o["chord_range_per_nail"].items()})
    print("landing angle range (deg):", o["landing_angle_deg"])
    for name, v in o["templates"].items():
        xs = [p[0] for path in v["stylus1"] + v["stylus2"] for p in path]
        ys = [p[1] for path in v["stylus1"] + v["stylus2"] for p in path]
        print(f"{name}: stylus span x {min(xs):.1f}..{max(xs):.1f}, y {min(ys):.1f}..{max(ys):.1f}")
        # scale check: S1 extreme vs d extreme

    sm = scalp_metrics()
    print("SCALP-LEVEL (what the ink shows): chord arc", sm["scalp_chord"], "mm; turnaround clearance", sm["turn_lift"], "mm")
    rings, angs, Z = ceiling_heightfield()
    zmin, zmax = float(np.nanmin(Z)), float(np.nanmax(Z))
    z_u = math.floor((zmin - 0.8) * 10) / 10
    pts, faces = write_scad_pocket(rings, angs, Z, (z_u - 1.0) if VARIANT == "v1" else 125.0)   # V2: mouth opens through the R 155.5 underside sphere
    with open(os.path.join(HERE, f"pocket_cavity{SUF}.scad"), "w") as f:
        f.write(f"// pocket_cavity{SUF}.scad - GENERATED by dish_kinematics.py (DISH_VARIANT={VARIANT}), do not edit by hand.\n")
        f.write("// One dish pocket cavity (ceiling = exact envelope of the 6 mm ball over the dome-centre\n")
        if VARIANT == "v1":
            f.write("// surface: sphere R 157 about the ball centre C + rise up the deck axis: 34 deg to 13.7,\n")
            f.write("// 50 deg to 17.0, 70 deg stop to 18.5 mm of ball offset at the dish).  Local XY origin = ball home of\n")
        else:
            f.write("// surface: sphere R 157 about C + rise up the deck axis; profile at the NAIL plane x 157/85:\n")
            f.write("// sphere to 6.0, 30 deg +4.5, 50 deg +4.5, turnaround 17.07 (31.5 at the dish), 70 deg stop).  Local XY origin = ball home of\n")
        f.write(f"// the 90 deg pocket (x 0, y {A_DOME}); Z absolute above C.  Place copies with rotate 120/240.\n")
        f.write(f"POCKET_ZMIN{SUF.upper()} = {zmin:.3f};  POCKET_ZMAX{SUF.upper()} = {zmax:.3f};  DECK_ZU{SUF.upper()} = {z_u:.1f};\n")
        f.write(f"module pocket_cavity{SUF}() polyhedron(points = [" + ",".join(f"[{p[0]:.3f},{p[1]:.3f},{p[2]:.3f}]" for p in pts) + "], faces = [" + ",".join(f"[{a},{b},{c}]" for a, b, c in faces) + "]);\n")
    with open(os.path.join(HERE, f"pocket_mesh{SUF}.json"), "w") as f:
        json.dump({"points": pts, "faces": faces, "zmin": zmin, "zmax": zmax, "z_u": z_u}, f)
    print(f"ceiling z range {zmin:.2f} .. {zmax:.2f}; deck underside DECK_ZU = {z_u:.1f}")
