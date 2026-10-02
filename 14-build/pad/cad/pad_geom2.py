#!/usr/bin/env python3
"""
pad_geom2.py - PAD part 2: dome pockets (ceiling height fields for the deck), block-to-deck
clearance, C8 sweep (nail-skid, block underside, fences), lift springs, yaw stiffness,
rim reaction and the stack.  Imports the kinematics from pad_geom.py.

Writes pockets.npz: for each dome k a height field of the pocket CEILING (the surface the
PTFE ball touches) on a polar grid about the dome's home position.

Run: <cadenv>/bin/python pad_geom2.py [--quick]
"""
import math, sys, os, json
import numpy as np
import pad_geom as G

QUICK = "--quick" in sys.argv
HERE = os.path.dirname(os.path.abspath(__file__))

# ------------------------------------------------------------------ dome geometry
ZD = float(os.environ.get("PAD_ZD", "91.5"))   # ball centre above the nail plane at home (set by the clearance loop below)
BR = G.BALL_R

def dome_home(k):
    a = math.radians(G.DOME_ANG[k])
    return np.array([G.RD * math.cos(a), G.RD * math.sin(a), ZD])

def pose_grid(n_s=None, n_psi=None, smax=None):
    smax = smax or G.A_CAGE
    n_s = n_s or (24 if QUICK else 48)
    n_psi = n_psi or (36 if QUICK else 72)
    out = [(0.0, 0.0)]
    for i in range(1, n_s + 1):
        s = smax * i / n_s
        for j in range(n_psi):
            psi = 2 * math.pi * j / n_psi
            out.append((s * math.cos(psi), s * math.sin(psi)))
    return out

def dome_centres(poses):
    """array [pose, dome, xyz]"""
    res = np.zeros((len(poses), 3, 3))
    homes = [dome_home(k) for k in range(3)]
    for i, (dx, dy) in enumerate(poses):
        Rm, t = G.pose_vec(dx, dy)
        for k in range(3):
            # dome lug is part of the block: block-frame position = world home (block home = identity)
            res[i, k] = Rm @ homes[k] + t
    return res

# ------------------------------------------------------------------ pocket ceilings
def pocket_fields(dc, rmax=34.0, nr=69, nth=144):
    """ceiling z(r, theta) about each dome home = upper envelope of the ball spheres."""
    rs = np.linspace(0, rmax, nr); th = np.linspace(0, 2 * math.pi, nth, endpoint=False)
    fields = []
    for k in range(3):
        h0 = dome_home(k)
        X = h0[0] + rs[:, None] * np.cos(th)[None, :]
        Y = h0[1] + rs[:, None] * np.sin(th)[None, :]
        Z = np.full(X.shape, -np.inf)
        for c in dc[:, k, :]:
            d2 = (X - c[0])**2 + (Y - c[1])**2
            m = d2 < BR * BR
            if m.any():
                Z[m] = np.maximum(Z[m], c[2] + np.sqrt(BR * BR - d2[m]))
        fields.append((X, Y, Z))
    return rs, th, fields

def dome_travel(dc):
    D = np.linalg.norm(dc[:, :, :2] - np.array([dome_home(k)[:2] for k in range(3)])[None], axis=2)
    return float(D.max())

def dome_slopes(n_psi=24):
    """max ceiling slope along each dome path (deg) and the horizontal rim reaction per N of
    vertical dome load, for straight lines through the centre."""
    worst = 0.0
    for j in range(n_psi):
        psi = math.pi * j / n_psi
        ss = np.linspace(-G.A_CAGE, G.A_CAGE, 371)
        for k in range(3):
            pts = []
            for s in ss:
                Rm, t = G.pose(s, psi); pts.append(Rm @ dome_home(k) + t)
            pts = np.array(pts)
            dh = np.linalg.norm(np.diff(pts[:, :2], axis=0), axis=1); dz = np.abs(np.diff(pts[:, 2]))
            ok = dh > 1e-6
            worst = max(worst, float(np.degrees(np.arctan2(dz[ok], dh[ok])).max()))
    return worst

# ------------------------------------------------------------------ block features under the deck
def block_top_points():
    """sample points on the block's top features (block frame, home)."""
    pts = []
    # gallery plate top disc R27 at Z_BLOCK_TOP
    for r in np.linspace(0, G.R_GAL, 10):
        for a in np.linspace(0, 2 * math.pi, max(6, int(r * 1.2)), endpoint=False):
            pts.append((r * math.cos(a), r * math.sin(a), G.Z_BLOCK_TOP))
    # yoke disc R14 at Z_YOKE_TOP
    for r in np.linspace(0, G.R_YOKE, 6):
        for a in np.linspace(0, 2 * math.pi, max(6, int(r * 1.5)), endpoint=False):
            pts.append((r * math.cos(a), r * math.sin(a), G.Z_YOKE_TOP))
    # lug arms: from R27 to RD along each dome angle, top at Z_BLOCK_TOP + 3.5, width 7
    for k in range(3):
        a = math.radians(G.DOME_ANG[k]); u = np.array([math.cos(a), math.sin(a)]); n = np.array([-u[1], u[0]])
        for r in np.linspace(G.R_GAL, G.RD + 3.5, 6):
            for w in (-3.5, 0, 3.5):
                p = r * u + w * n; pts.append((p[0], p[1], G.Z_BLOCK_TOP + 3.5))
    return np.array(pts)

def stalk_points(k):
    """points on dome k's stalk (block frame): from lug top up to 1 mm under the ball."""
    h = dome_home(k); pts = []
    for z in np.linspace(G.Z_BLOCK_TOP + 3.5, ZD - BR * 0.6, 6):
        for a in np.linspace(0, 2 * math.pi, 8, endpoint=False):
            pts.append((h[0] + 2.0 * math.cos(a), h[1] + 2.0 * math.sin(a), z))
    return np.array(pts)

def ceiling_at(fields_k, h0, x, y):
    """bilinear lookup of the pocket ceiling of dome k at world (x, y); None if outside."""
    rs, th, (X, Y, Z) = fields_k
    r = math.hypot(x - h0[0], y - h0[1])
    if r > rs[-1]: return None
    a = math.atan2(y - h0[1], x - h0[0]) % (2 * math.pi)
    i = min(int(r / (rs[1] - rs[0])), len(rs) - 2); fr = r / (rs[1] - rs[0]) - i
    nth = len(th); j = int(a / (2 * math.pi) * nth) % nth; fa = a / (2 * math.pi) * nth - int(a / (2 * math.pi) * nth); j2 = (j + 1) % nth
    v = [Z[i, j], Z[i, j2], Z[i + 1, j], Z[i + 1, j2]]
    if any(not np.isfinite(t) for t in v): return None
    return (1 - fr) * ((1 - fa) * v[0] + fa * v[1]) + fr * ((1 - fa) * v[2] + fa * v[3])

def clearance_sweep(rs, th, fields, poses):
    """min vertical gap between every block-top feature and every pocket ceiling over all poses
    (features of the block vs the ceilings of all three pockets; a dome's own ball is excluded)."""
    feats = block_top_points()
    homes = [dome_home(k) for k in range(3)]
    worst = (1e9, None)
    for (dx, dy) in poses:
        Rm, t = G.pose_vec(dx, dy)
        P = (Rm @ feats.T).T + t
        for k in range(3):
            fk = (rs, th, fields[k])
            for p in P:
                c = ceiling_at(fk, homes[k], p[0], p[1])
                if c is None: continue
                g = c - p[2]
                if g < worst[0]: worst = (g, (round(dx, 1), round(dy, 1), k))
        # stalks of dome j against pockets of the OTHER domes, and its own pocket away from the ball
        for j in range(3):
            S = (Rm @ stalk_points(j).T).T + t
            for k in range(3):
                fk = (rs, th, fields[k])
                for p in S:
                    if k == j and math.hypot(p[0] - (Rm @ homes[j] + t)[0], p[1] - (Rm @ homes[j] + t)[1]) < 2.5:
                        continue
                    c = ceiling_at(fk, homes[k], p[0], p[1])
                    if c is None: continue
                    g = c - p[2]
                    if g < worst[0]: worst = (g, (round(dx, 1), round(dy, 1), "stalk%d/pocket%d" % (j, k)))
    return worst

def skirt_r(z):
    """inner radius of the skirt frame / cover band (conical: R51 at z 36 to R56 at z 79.5)"""
    return 51.0 + (min(max(z, 36.0), 79.5) - 36.0) * (5.0 / 43.5)

# ------------------------------------------------------------------ C8 nail-skid and envelope sweep
def c8_sweep(poses):
    """nail cone (tip 0 2 -> 0 3.92 at 0.96, land 0 3.92 up to the skirt plate) vs skid feet
    (0 8 caps on R15 domes at SKID_R) and skid stems (0 6) in 3D; block underside height over
    R85 and R65; nail tip reach (fence) radius."""
    res = dict(nail_skid=1e9, under85=1e9, under65=1e9, reach=0.0, block_skirt=1e9)
    skid_c = [np.array([G.SKID_R * math.cos(math.radians(a)), G.SKID_R * math.sin(math.radians(a)), G.ZF]) for a in G.SKID_ANG]
    head65 = G.sphere_head(65, G.seat_sphere(65))
    for (dx, dy) in poses:
        for yaw in (-math.radians(5), 0.0, math.radians(5)):
            Rm, t = G.pose_vec(dx, dy, yaw)
            for nm, q in G.NAILS:
                for z in (G.TIP_MAX, 0.0, 10.0, 20.0, G.Z_SKIRT_BOT):
                    p = Rm @ np.array([q[0], q[1], z]) + t
                    res["reach"] = max(res["reach"], math.hypot(p[0], p[1]) + 1.96)
                    for sc in skid_c:
                        # skid foot (0 8 cap at the dome bottom) and stem (vertical 0 6 above the dome)
                        foot = sc + np.array([0, 0, -G.SKID_DOME_R])
                        dfoot = math.hypot(p[0] - sc[0], p[1] - sc[1]) - 4.0 - 1.96
                        res["nail_skid"] = min(res["nail_skid"], dfoot)
            # block underside corners (skirt plate R27 at Z_SKIRT_BOT) and block rim at 3 heights vs the skirt frame
            for a in np.linspace(0, 2 * math.pi, 24, endpoint=False):
                p = Rm @ np.array([G.R_GAL * math.cos(a), G.R_GAL * math.sin(a), G.Z_SKIRT_BOT]) + t
                res["under85"] = min(res["under85"], G.HEAD85(p))
                res["under65"] = min(res["under65"], head65(p))
                for z in (G.Z_SKIRT_BOT, 36.0, 60.0, 80.0, G.Z_BLOCK_TOP):
                    p = Rm @ np.array([(G.R_GAL + (1.5 if z < 40 else 0.0)) * math.cos(a), (G.R_GAL + (1.5 if z < 40 else 0.0)) * math.sin(a), z]) + t
                    res["block_skirt"] = min(res["block_skirt"], skirt_r(p[2]) - math.hypot(p[0], p[1]))
    return res

# ------------------------------------------------------------------ lift springs
LIFT_ANG = (0.0, 120.0, 240.0)
LIFT_LOW = (28.5, 36.0)        # (r, z) eyelet on the floor-plate lug (block frame)
LIFT_HIGH = (55.5, 77.0)       # (r, z) hook on the skirt-frame top ring (deck frame)
LIFT_K, LIFT_L0, LIFT_T0 = 0.012, 30.0, 0.09   # N/mm, free length (between hook centres), initial tension

def lift_forces(poses):
    out = []
    for (dx, dy) in poses:
        Rm, t = G.pose_vec(dx, dy)
        F = np.zeros(3)
        for a in LIFT_ANG:
            ca, sa = math.cos(math.radians(a)), math.sin(math.radians(a))
            lo = Rm @ np.array([LIFT_LOW[0] * ca, LIFT_LOW[0] * sa, LIFT_LOW[1]]) + t
            hi = np.array([LIFT_HIGH[0] * ca, LIFT_HIGH[0] * sa, LIFT_HIGH[1]])
            L = np.linalg.norm(hi - lo); T = LIFT_T0 + LIFT_K * max(L - LIFT_L0, 0.0)
            F += T * (hi - lo) / L
        out.append((dx, dy, F[0], F[1], F[2]))
    return np.array(out)

# ------------------------------------------------------------------ yaw stiffness from the tendons
def yaw_stiffness(T=2.0):
    """tension-only pendulum stiffness of three radial tendons, posts R10, stops R65 (N.mm/rad)."""
    k = 0.0
    for a in G.STOP_ANG:
        e = np.array([math.cos(math.radians(a)), math.sin(math.radians(a))])
        th = 1e-4; post = G.POST_R * np.array([math.cos(math.radians(a) + th), math.sin(math.radians(a) + th)])
        stop = G.STOP_R * e; f = T * (stop - post) / np.linalg.norm(stop - post)
        k += -(post[0] * f[1] - post[1] * f[0]) / th
    return k

if __name__ == "__main__":
    poses = pose_grid()
    print(f"\n=== 4. DOME POCKETS (ZD = {ZD} mm ball centre, RD {G.RD}, ball 0 {2*BR:.2f}) ===")
    dc = dome_centres(poses)
    Dmax = dome_travel(dc)
    half = G.RD * math.sin(math.radians(60))
    print(f" max dome travel {Dmax:.2f} mm (cage |d| {G.A_CAGE}); pocket radius incl. ball {Dmax + BR:.2f}; half spacing {half:.2f}; spare {half - Dmax - BR:.2f} mm")
    sl = dome_slopes(12 if QUICK else 24)
    print(f" steepest ceiling slope on any dome path {sl:.1f} deg -> rim reaction <= {math.tan(math.radians(sl)):.2f} x vertical dome load")
    rs, th, fields = pocket_fields(dc, rmax=min(half, Dmax + BR + 1.0))
    zmin = min(np.nanmin(np.where(np.isfinite(f[2]), f[2], np.nan)) for f in fields)
    zmax = max(np.nanmax(np.where(np.isfinite(f[2]), f[2], np.nan)) for f in fields)
    print(f" ceiling z range {zmin:.2f} .. {zmax:.2f} (home ball top {ZD + BR:.2f})")
    np.savez(os.path.join(HERE, "pockets.npz"), rs=rs, th=th, Z0=fields[0][2], Z1=fields[1][2], Z2=fields[2][2],
             homes=np.array([dome_home(k) for k in range(3)]), ZD=ZD, BR=BR)
    cl = clearance_sweep(rs, th, fields, pose_grid(12 if QUICK else 18, 24 if QUICK else 36))
    print(f" min block-feature-to-ceiling gap {cl[0]:+.2f} mm at pose {cl[1]} (target >= {G.GAP_MIN})")
    print("\n=== 5. C8 SWEEP (yaw -5/0/+5 deg, |d| to the cage) ===")
    c8 = c8_sweep(pose_grid(12 if QUICK else 18, 24 if QUICK else 36))
    print(f" nail-to-skid-foot clearance >= {c8['nail_skid']:.1f} mm (C8 >= 8) | block underside >= {c8['under85']:.1f} mm on R85, {c8['under65']:.1f} on R65 (C8 >= 30)"
          f" | nail reach radius {c8['reach']:.1f} mm (fence) | block-to-skirt ring gap >= {c8['block_skirt']:.1f} mm")
    print("\n=== 6. LIFT SPRINGS (3 x, block side to skirt ring) ===")
    lf = lift_forces(pose_grid(12, 24))
    print(f" lift (z) {lf[:,4].min():.3f} .. {lf[:,4].max():.3f} N ; horizontal pull {np.hypot(lf[:,2],lf[:,3]).max():.3f} N max ; at home {lf[0,4]:.3f} N")
    print("\n=== 7. YAW ===")
    ky = yaw_stiffness(2.0)
    print(f" tendon pendulum yaw stiffness at 2.0 N pretension: {ky:.1f} N.mm/rad = {ky*math.pi/180:.2f} N.mm/deg")
    json.dump(dict(ZD=ZD, Dmax=Dmax, slope=sl, gap=cl[0], c8=c8, lift_min=float(lf[:,4].min()), lift_max=float(lf[:,4].max()),
                   hpull=float(np.hypot(lf[:,2],lf[:,3]).max()), yaw=ky), open(os.path.join(HERE, "pad_geom_part2.json"), "w"), indent=1, default=str)
