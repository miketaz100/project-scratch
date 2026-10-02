#!/usr/bin/env python
"""
gen_pad_stl.py - STL generator for the SP1 v3 PAD (14-build/pad/cad), PAD engineer, 2026-10-02.

THE .scad FILES ARE THE SOURCE OF TRUTH for every printed part EXCEPT the deck's three pocket
ceilings, whose height fields come from pad_geom2.py (pockets.npz) and are written to
pockets_data.scad for the SCAD side.  Constant names here match lib_pad.scad.

FRAME P (spec 3.1, pad.md 2): origin = nail plane on the pad axis; z away from the scalp;
x = bail tangent; pentagon P0 on +x.  Every part is written IN ITS INSTALLED POSITION so the
STLs load together as the assembly (block at home).  README.md gives print orientation.

Run:  <cadenv>/bin/python gen_pad_stl.py [--only PD05,PD06]
Prints name, bounding box, volume, mass (by material) and watertightness; exit 0 only if every
mesh is watertight.  Also writes mass_by_part.csv and shadowgraph_nail.svg.
"""
import math, os, sys, csv
import numpy as np
import trimesh
import manifold3d as m3
from manifold3d import Manifold, CrossSection

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "stl")
os.makedirs(OUT, exist_ok=True)
FN = 48

# ===================================================================== lib_pad.scad constants
# fasteners
M2_CLEAR, M2_PILOT, M3_CLEAR, M3_INS_D, M3_INS_L = 2.4, 1.7, 3.4, 4.0, 4.0
# frame / stack (z above the nail plane at home, design head R85)
Z_SKIRT_BOT, SKIRT_T = 32.0, 2.0          # wiper skirt plate underside, thickness
Z_FLOOR0, Z_FLOOR1 = 34.0, 38.0            # floor plate
Z_CART0, Z_CART1 = 38.0, 80.0              # cartridge
Z_GAL0, Z_GAL1 = 80.0, 83.5                # gallery plate
Z_YOKE0, Z_YOKE1 = 83.5, 87.0              # yoke
Z_CABLE = 85.5                             # tendon height at the post (home)
R_BLOCK = 27.0                             # floor / gallery / skirt plate radius
PIN_R = 18.0
PINS = [(0.0, 0.0)] + [(PIN_R * math.cos(math.radians(72 * k)), PIN_R * math.sin(math.radians(72 * k))) for k in range(5)]
PIN_NAMES = ["C", "P0", "P1", "P2", "P3", "P4"]
# cartridge
CART_OD, CART_OD_TOP, CART_TOP_L = 9.4, 8.7, 4.0
CART_BORE_LAND, BUSH_BORE, PISTON_BORE = 4.6, 5.95, 7.0
Z_BUSH0, Z_BUSH1 = 50.0, 54.0              # upper PTFE bush in the cartridge
CART_SOCKET = 9.55
# nail
LAND_D, TIP_FLAT_D, TIP_R, NAIL_TOP_R = 3.92, 2.0, 0.4, 0.5
Z_LAND_TOP_E15 = 59.9                      # land top at e = 15 (block home, R85)
INSERT_D, INSERT_L = 2.0, 4.0              # hardened dowel pressed flush in the land top
# piston
PISTON_D, PISTON_H, MAG_C1_D, MAG_C1_H = 5.8, 4.5, 3.25, 1.62
# dome lugs / balls (pad_geom.py RD, DOME_ANG; pad_geom2.py ZD)
RD, DOME_ANG, ZD, BALL_D = 38.0, (30.0, 150.0, 270.0), 91.5, 6.35
LUG_W, Z_LUG1 = 7.0, 87.0
# columns (gallery plate down to the floor plate) and ports
COL_R, COL_ANG, COL_D = 24.0, (108.0, 180.0, 252.0), 5.0
PORT_ANG = {"B": 108.0, "A": 252.0}
Z_PORT = 60.0
# yoke / coupling
R_YOKE, YOKE_MAG_R, YOKE_MAG_ANG, POST_R, POST_ANG = 14.0, 8.0, (30.0, 150.0, 270.0), 10.0, (90.0, 210.0, 330.0)
MAG_CPL_D, MAG_CPL_H = 6.45, 3.4           # pocket for K&J D42-N52 (6.35 x 3.17)
WASHER_D, WASHER_T = 7.1, 0.6              # M3 DIN 125 steel washer 7 x 3.2 x 0.5 (coupling keeper)
CAGE_R_IN, CAGE_H = 20.0, 1.5
# deck
Z_DECK_TOP, DECK_PLATE_T, SHELL_T = 108.0, 1.5, 1.0
POST_RAD, POST_ANGS, POST_D = 58.0, (78.0, 102.0, 198.0, 222.0, 318.0, 342.0), 5.0
SEAT_R, SEAT_ANG, Z_SEAT = 55.0, (30.0, 150.0, 270.0), 109.5    # HALO ball seats (spherical band about P0)
DISC_R, DISC_D, DISC_T = 42.0, 8.1, 1.1                          # HALO M8 steel discs 0 8 x 1
# skirt frame
SK_R_BOT, SK_R_TOP, Z_SK0, Z_SK1 = 51.0, 56.0, 36.0, 79.5
SKID_R, SKID_ANG, SKID_STEM_D = 60.0, (60.0, 180.0, 300.0), 6.0
STOP_R, STOP_ANG = 65.0, (90.0, 210.0, 330.0)
LIFT_ANG = (60.0, 180.0, 300.0)
LIFT_LOW, LIFT_HIGH = (28.5, 36.0), (55.5, 77.0)
# skid foot
SKID_DOME_R, SKID_FOOT_D = 15.0, 8.0
ZF = -85.0 + math.sqrt((85.0 + SKID_DOME_R) ** 2 - SKID_R ** 2)       # foot dome centre (R85 zero setting)

DENS = {"SLA": 1.15, "MJF": 1.01, "PETG": 1.27, "POM": 1.41}

# ===================================================================== helpers
def U(*ms):
    ms = [m for m in ms if m is not None]
    return Manifold.batch_boolean(ms, m3.OpType.Add) if len(ms) > 1 else ms[0]

def Dm(m, *cuts):
    cuts = [c for c in cuts if c is not None]
    if not cuts: return m
    return m - (Manifold.batch_boolean(cuts, m3.OpType.Add) if len(cuts) > 1 else cuts[0])

def box(x0, x1, y0, y1, z0, z1):
    return Manifold.cube([x1 - x0, y1 - y0, z1 - z0]).translate([x0, y0, z0])

def cyl(r, z0, z1, x=0.0, y=0.0, r2=None, fn=FN):
    return Manifold.cylinder(z1 - z0, r, r if r2 is None else r2, fn).translate([x, y, z0])

def sphere(r, c, fn=FN):
    return Manifold.sphere(r, fn).translate(list(c))

def polar(r, ang):
    return (r * math.cos(math.radians(ang)), r * math.sin(math.radians(ang)))

def rotz(m, ang):
    return m.rotate([0, 0, ang])

def cs_poly(pts):
    P = [(float(a), float(b)) for a, b in pts]
    area = sum(P[i][0] * P[(i + 1) % len(P)][1] - P[(i + 1) % len(P)][0] * P[i][1] for i in range(len(P)))
    if area < 0: P.reverse()
    return CrossSection([P])

def revolve(profile_rz, fn=FN):
    """solid of revolution about z from a closed (r, z) polygon with r >= 0"""
    return cs_poly(profile_rz).revolve(fn)

def radial_bar(ang, r0, r1, w, z0, z1):
    """bar along the radial direction ang from r0 to r1, width w"""
    return rotz(box(r0, r1, -w / 2, w / 2, z0, z1), ang)

def radial_cyl(ang, r0, r1, rad, z):
    """cylinder along the radial direction ang"""
    c = Manifold.cylinder(r1 - r0, rad, rad, 24).rotate([0, 90, 0]).translate([r0, 0, z])
    return rotz(c, ang)

def seg_cyl(p0, p1, rad, fn=16):
    """cylinder between two 3D points"""
    p0, p1 = np.array(p0, float), np.array(p1, float)
    v = p1 - p0; L = np.linalg.norm(v); k = v / L
    z = np.array([0, 0, 1.0]); ax = np.cross(z, k); s = np.linalg.norm(ax); c = float(np.dot(z, k))
    if s < 1e-9:
        R = np.eye(3) if c > 0 else np.diag([1, -1, -1])
    else:
        ax /= s; K = np.array([[0, -ax[2], ax[1]], [ax[2], 0, -ax[0]], [-ax[1], ax[0], 0]])
        R = np.eye(3) + s * K + (1 - c) * K @ K
    m = Manifold.cylinder(L, rad, rad, fn)
    return m.transform(np.column_stack([R, p0]).tolist())

def to_trimesh(m):
    mm = m.to_mesh()
    return trimesh.Trimesh(vertices=np.asarray(mm.vert_properties)[:, :3], faces=np.asarray(mm.tri_verts), process=False)

def mesh_manifold(V, F):
    return Manifold(m3.Mesh(np.asarray(V, np.float32), np.asarray(F, np.uint32)))

# ===================================================================== pocket height fields
def load_pockets():
    d = np.load(os.path.join(HERE, "pockets.npz"))
    rs, th, homes = d["rs"], d["th"], d["homes"]
    Zs = []
    for k in range(3):
        Z = np.array(d["Z%d" % k], float)
        # fill un-reached cells outward with the last finite value of each spoke (plateau)
        for j in range(Z.shape[1]):
            last = None
            for i in range(Z.shape[0]):
                if np.isfinite(Z[i, j]): last = Z[i, j]
                elif last is not None: Z[i, j] = last
        Z[~np.isfinite(Z)] = np.nanmax(np.where(np.isfinite(Z), Z, np.nan))
        Zs.append(Z)
    return rs, th, homes, Zs

def hf_prism(rs, th, zbot, ztop, home, r_extra=0.0):
    """closed solid over a polar grid about home: bottom surface zbot[i,j], top z = ztop.
    The outer rim is extended by r_extra with the rim values (vertical wall)."""
    nr, nt = zbot.shape
    R = list(rs) + ([rs[-1] + r_extra] if r_extra > 0 else [])
    Zb = np.vstack([zbot] + ([zbot[-1:]] if r_extra > 0 else []))
    nr = len(R)
    V, F = [], []
    def vid(i, j, top):
        return (0 if top else 1) * (1 + (nr - 1) * nt) + (0 if i == 0 else 1 + (i - 1) * nt + (j % nt))
    for top in (True, False):
        zc = ztop if top else float(np.mean(Zb[0]))
        V.append((home[0], home[1], zc))
        for i in range(1, nr):
            for j in range(nt):
                x = home[0] + R[i] * math.cos(th[j]); y = home[1] + R[i] * math.sin(th[j])
                V.append((x, y, ztop if top else Zb[i, j]))
    for top in (True, False):
        for j in range(nt):
            a, b = vid(0, 0, top), vid(1, j, top); c = vid(1, j + 1, top)
            F.append((a, b, c) if top else (a, c, b))
        for i in range(1, nr - 1):
            for j in range(nt):
                a, b, c, d = vid(i, j, top), vid(i + 1, j, top), vid(i + 1, j + 1, top), vid(i, j + 1, top)
                F += ([(a, b, c), (a, c, d)] if top else [(a, c, b), (a, d, c)])
    for j in range(nt):   # side wall
        a, b = vid(nr - 1, j, True), vid(nr - 1, j + 1, True)
        c, d = vid(nr - 1, j + 1, False), vid(nr - 1, j, False)
        F += [(a, d, c), (a, c, b)]
    return mesh_manifold(V, F)

# ===================================================================== parts
def pd01_deck():
    """DECK (SLA): three OPEN pocket shells (1.0 mm; the dish ceilings) joined by a top lattice
    (hub + six spokes at z 106.5-108), six posts down to the skirt frame, three HALO ball seats
    on a sphere about P0 (a meridional V-groove at 270 deg = yaw key, two spherical facets) and
    three steel-disc bosses at R42.  Pillars inside a pocket stop at its ceiling (the ball's space)."""
    rs, th, homes, Zs = load_pockets()
    ZT = 116.0
    outers, shells, foot = [], [], []
    for k in range(3):
        h = homes[k]
        outer = hf_prism(rs, th, Zs[k], ZT, h, r_extra=SHELL_T)
        cav = hf_prism(rs, th, Zs[k] + SHELL_T, ZT + 1.0, h)
        outers.append(outer)
        shells.append((outer - cav) ^ box(-200, 200, -200, 200, 0, Z_DECK_TOP))
        foot.append(cyl(rs[-1] + SHELL_T, 70.0, ZT + 2.0, h[0], h[1], fn=96))
    allowed = U(U(*outers), box(-200, 200, -200, 200, 60.0, ZT + 3.0) - U(*foot))
    lattice = [cyl(14.0, Z_DECK_TOP - DECK_PLATE_T, Z_DECK_TOP)]
    for a in POST_ANGS:
        lattice.append(radial_bar(a, 0, POST_RAD, 6.0, Z_DECK_TOP - DECK_PLATE_T, Z_DECK_TOP))
        x, y = polar(POST_RAD, a)
        lattice.append(Dm(cyl(POST_D / 2, Z_SK1, Z_DECK_TOP, x, y), cyl(1.4, Z_SK1 + 8.5, Z_DECK_TOP - 2.0, x, y, fn=16)))
    for k in range(3):           # rim ring of each pocket at the top, ties the lattice to the shell rims
        h = homes[k]
        lattice.append(Dm(cyl(rs[-1] + SHELL_T, Z_DECK_TOP - DECK_PLATE_T, Z_DECK_TOP, h[0], h[1], fn=96),
                          cyl(rs[-1] - 2.0, Z_DECK_TOP - DECK_PLATE_T - 1, Z_DECK_TOP + 1, h[0], h[1], fn=96)))
    SR = math.hypot(SEAT_R, Z_SEAT)
    pillars = []
    for a in SEAT_ANG:
        pillars.append(radial_bar(a, SEAT_R - 6.5, SEAT_R + 6.5, 12, 80.0, Z_SEAT + 4))
        pillars.append(cyl(DISC_D / 2 + 1.5, 80.0, Z_DECK_TOP + 0.4, *polar(DISC_R, a)))
    pil = (U(*pillars) ^ allowed)
    hollow = []
    for a in SEAT_ANG:     # lighten: pillars are tubes below their top 2.5 mm
        hollow.append(cyl(DISC_D / 2 - 0.3, 80.0, Z_DECK_TOP + 0.4 - DISC_T - 2.5, *polar(DISC_R, a)))
        hollow.append(radial_bar(a, SEAT_R - 4.5, SEAT_R + 4.5, 8, 80.0, Z_SEAT - 6.0))
    pil = Dm(pil, *hollow)
    pil = pil ^ U(sphere(SR, (0, 0, 0), 256), box(-200, 200, -200, 200, -10, Z_DECK_TOP + 0.41))
    deck = U(*shells, *lattice, pil)
    cuts = []
    a = SEAT_ANG[2]
    vs = []
    for t in np.linspace(-6.5, 6.5, 6):
        r = SEAT_R + t; z = math.sqrt(SR * SR - r * r)
        x, y = polar(r, a)
        vs.append(Manifold.cube([2.6, 2.6, 2.6], True).rotate([45, 0, 0]).rotate([0, 0, a]).translate([x, y, z]))
    cuts.append(Manifold.batch_hull(vs))
    cuts += [cyl(DISC_D / 2, Z_DECK_TOP + 0.4 - DISC_T, Z_DECK_TOP + 1, *polar(DISC_R, a)) for a in SEAT_ANG]
    cuts += [cyl(M2_PILOT / 2, Z_SK1 - 0.1, Z_SK1 + 8, *polar(POST_RAD, a), fn=16) for a in POST_ANGS]
    return Dm(deck, *cuts)

def pd02_skirt_frame():
    """SKIRT FRAME (MJF PA12): bottom ring (cage + skid guides), top ring (post seats, lift hooks,
    skid adjuster bosses, stop arms), six struts. The 0.5 mm PP cover band clips round it."""
    bot = Dm(cyl(SK_R_BOT + 2.5, Z_SK0, Z_SK0 + 3.0, fn=128), cyl(SK_R_BOT, Z_SK0 - 1, Z_SK0 + 4, fn=128))
    top = Dm(cyl(SK_R_TOP + 2.5, Z_SK1 - 3.5, Z_SK1, fn=128), cyl(SK_R_TOP, Z_SK1 - 5, Z_SK1 + 1, fn=128))
    parts = [bot, top]
    for a in POST_ANGS:
        parts.append(seg_cyl((*polar(SK_R_BOT + 1.5, a), Z_SK0 + 1), (*polar(SK_R_TOP + 1.5, a), Z_SK1 - 1), 2.0))
        parts.append(cyl(POST_D / 2 + 1.6, Z_SK1 - 4.0, Z_SK1, *polar(POST_RAD, a)))
    holes = [cyl(M2_CLEAR / 2, Z_SK1 - 5, Z_SK1 + 1, *polar(POST_RAD, a), fn=16) for a in POST_ANGS]
    # skid bosses: top (adjuster, 0 8 bore for the M3 screw collar) and bottom (stem guide 0 6.3)
    for a in SKID_ANG:
        parts.append(radial_bar(a, SK_R_TOP + 2, SKID_R + 4.5, 9.0, Z_SK1 - 6, Z_SK1))
        parts.append(radial_bar(a, SK_R_BOT + 2, SKID_R + 4.5, 9.0, Z_SK0, Z_SK0 + 6))
        x, y = polar(SKID_R, a)
        holes.append(cyl(M3_CLEAR / 2, Z_SK1 - 7, Z_SK1 + 1, x, y, fn=20))
        holes.append(cyl(3.1, Z_SK1 - 7, Z_SK1 - 3.5, x, y, fn=24))             # stem top travel pocket
        holes.append(cyl(SKID_STEM_D / 2 + 0.15, Z_SK0 - 1, Z_SK0 + 7, x, y, fn=32))
    # lift-spring hooks on the top ring inner face
    for a in LIFT_ANG:
        x, y = polar(LIFT_HIGH[0], a)
        parts.append(radial_bar(a, LIFT_HIGH[0] - 1.0, SK_R_TOP + 1, 4.0, LIFT_HIGH[1] - 2.0, Z_SK1))
        holes.append(seg_cyl((*polar(LIFT_HIGH[0] - 0.5, a - 8), LIFT_HIGH[1] - 0.5), (*polar(LIFT_HIGH[0] - 0.5, a + 8), LIFT_HIGH[1] - 0.5), 0.6, 12))
    # stop arms out to the stop blocks (R65, cable height)
    for a in STOP_ANG:
        parts.append(radial_bar(a, SK_R_TOP + 1, STOP_R + 1.0, 8.0, Z_SK1 - 3.5, Z_SK1))
        parts.append(radial_bar(a, STOP_R - 6.0, STOP_R + 1.0, 8.0, Z_SK1 - 0.01, Z_CABLE - 3.5))
        for dy in (-2.5, 2.5):
            c = rotz(cyl(1.0, Z_SK1 - 5, Z_CABLE, STOP_R - 2.0, dy, fn=16), a)
            holes.append(c)
    # jumper-tube clip bosses outside at the port angles
    for a in PORT_ANG.values():
        parts.append(radial_bar(a, SK_R_BOT + 2, SK_R_BOT + 7, 7.0, Z_SK0, Z_SK0 + 6))
        holes.append(rotz(cyl(1.65, Z_SK0 - 1, Z_SK0 + 7, SK_R_BOT + 5.5, 0, fn=20), a))
    return Dm(U(*parts), *holes)

def pd05_floor_plate():
    """FLOOR PLATE (SLA): lower PTFE bushes, cartridge sockets, column screws, lift eyelets,
    wiper clamp face (underside), snap rim for the skirt plate."""
    base = cyl(R_BLOCK, Z_FLOOR0, Z_FLOOR1)
    parts = [base]
    for (x, y) in PINS:
        parts.append(Dm(cyl(CART_SOCKET / 2 + 1.2, Z_FLOOR1, Z_FLOOR1 + 1.5, x, y), cyl(CART_SOCKET / 2, Z_FLOOR1 - 0.1, Z_FLOOR1 + 2, x, y)))
    for a in LIFT_ANG:
        parts.append(Dm(radial_bar(a, R_BLOCK - 2, LIFT_LOW[0] + 1.8, 4.0, Z_FLOOR0, Z_FLOOR1),
                        rotz(cyl(0.7, Z_FLOOR0 - 1, Z_FLOOR1 + 1, LIFT_LOW[0], 0, fn=12), a)))
    for a in COL_ANG:
        parts.append(cyl(COL_D / 2 + 0.5, Z_FLOOR1, Z_FLOOR1 + 1.0, *polar(COL_R, a)))
    m = U(*parts)
    holes = []
    for (x, y) in PINS:
        holes.append(cyl(BUSH_BORE / 2, Z_FLOOR0 - 0.1, Z_FLOOR1 + 0.1, x, y, fn=32))
    for a in COL_ANG:
        holes.append(cyl(M2_CLEAR / 2, Z_FLOOR0 - 0.1, Z_FLOOR1 + 1.5, *polar(COL_R, a), fn=16))
        holes.append(cyl(2.2, Z_FLOOR0 - 0.1, Z_FLOOR0 + 1.6, *polar(COL_R, a), fn=16))   # screw head recess
    # orientation notch at 0 deg (P0 side) and snap groove round the rim for the skirt-plate hooks
    holes.append(Manifold.cube([2.0, 2.0, 10.0], True).rotate([0, 0, 45]).translate([R_BLOCK, 0, Z_FLOOR1]))
    holes.append(Dm(cyl(R_BLOCK + 1, Z_FLOOR0 + 1.0, Z_FLOOR0 + 2.0), cyl(R_BLOCK - 0.6, Z_FLOOR0 + 0.9, Z_FLOOR0 + 2.1)))
    # lightening pockets between pin bosses (top face, 2 mm deep)
    for a in (36.0, 324.0):
        holes.append(cyl(3.0, Z_FLOOR1 - 2.5, Z_FLOOR1 + 0.1, *polar(22.0, a), fn=24))
    for a in (0.0, 72.0, 144.0, 216.0, 288.0):
        holes.append(cyl(2.2, Z_FLOOR1 - 2.5, Z_FLOOR1 + 0.1, *polar(9.0, a + 36.0), fn=24))
    return Dm(m, *holes)

def pd06_cartridge(x=0.0, y=0.0):
    """CARTRIDGE (SLA): land clearance, upper PTFE bush seat, 0 7 piston bore, sleeve flange
    step at the top, rod-side vent hole + OD groove."""
    prof_out = [(0, Z_CART0), (CART_OD / 2, Z_CART0), (CART_OD / 2, Z_CART1 - CART_TOP_L), (CART_OD_TOP / 2, Z_CART1 - CART_TOP_L + 0.4),
                (CART_OD_TOP / 2, Z_CART1), (0, Z_CART1)]
    body = revolve(prof_out, 64)
    bore = revolve([(0, Z_CART0 - 0.1), (CART_BORE_LAND / 2, Z_CART0 - 0.1), (CART_BORE_LAND / 2, Z_BUSH0), (BUSH_BORE / 2, Z_BUSH0),
                    (BUSH_BORE / 2, Z_BUSH1), (PISTON_BORE / 2, Z_BUSH1), (PISTON_BORE / 2, Z_CART1 - 0.6),
                    (PISTON_BORE / 2 + 0.3, Z_CART1 + 0.1), (0, Z_CART1 + 0.1)], 64)
    vent = U(Manifold.cylinder(3.0, 0.5, 0.5, 12).rotate([0, 90, 0]).translate([2.9, 0, 55.5]),
             box(CART_OD / 2 - 0.6, CART_OD / 2 + 0.5, -0.5, 0.5, 55.0, Z_CART1 + 0.1))
    return Dm(body, bore, vent).translate([x, y, 0])

def pd07_gallery_plate():
    """GALLERY PLATE (SLA): galleries A/B (internal 0 1.4), sleeve-clamp beads, three columns
    with the two side barbs, three dome lugs with PTFE-ball sockets, coupling-washer pockets,
    yoke cage ring, vent grooves."""
    parts = [cyl(R_BLOCK, Z_GAL0, Z_GAL1)]
    for a in COL_ANG:
        parts.append(cyl(COL_D / 2, Z_FLOOR1 + 1.0, Z_GAL0 + 0.01, *polar(COL_R, a)))
    for a in PORT_ANG.values():
        x, y = polar(COL_R, a)
        # barb: 0 2.5 shank with a 0 3.0 ridge, radial, out to R31
        parts.append(radial_cyl(a, COL_R, COL_R + 6.0, 1.25, Z_PORT))
        parts.append(rotz(Manifold.cylinder(1.5, 1.5, 1.0, 24).rotate([0, 90, 0]).translate([COL_R + 4.0, 0, Z_PORT]), a))
    for k, a in enumerate(DOME_ANG):
        parts.append(radial_bar(a, R_BLOCK - 6, RD, LUG_W, Z_GAL0, Z_LUG1))
        x, y = polar(RD, a)
        parts.append(cyl(3.75, Z_LUG1 - 0.01, ZD - 1.0, x, y))
        parts.append(cyl(3.75, ZD - 1.0, ZD + 0.4, x, y, r2=3.3))
    parts.append(Dm(cyl(CAGE_R_IN + 1.5, Z_GAL1 - 0.01, Z_GAL1 + CAGE_H), cyl(CAGE_R_IN, Z_GAL1 - 1, Z_GAL1 + CAGE_H + 1)))
    m = U(*parts)
    cuts = []
    # ball sockets: PTFE ball 0 6.35 pressed in, lip 0.4 above the equator
    for a in DOME_ANG:
        cuts.append(sphere(BALL_D / 2 - 0.05, (*polar(RD, a), ZD), 48))
    # cartridge tops: bead ring (raised) is ADDED below; port holes
    zc = 0.5 * (Z_GAL0 + Z_GAL1)
    for (x, y) in PINS:
        cuts.append(cyl(0.7, Z_GAL0 - 0.1, zc + 0.7, x, y, fn=16))
    # gallery channels (internal tubes 0 1.4)
    def ch(p0, p1):
        return seg_cyl((p0[0], p0[1], zc), (p1[0], p1[1], zc), 0.7, 12)
    def arc(a0, a1, r, n=10):
        pts = [polar(r, a0 + (a1 - a0) * i / n) for i in range(n + 1)]
        return [ch(pts[i], pts[i + 1]) for i in range(n)] + [sphere(0.7, (p[0], p[1], zc), 12) for p in pts]
    P = dict(zip(PIN_NAMES, PINS))
    # B: port 108 -> arc R24 -> 72 (P1) ; P1 -> C ; C -> P4
    cuts += arc(108, 72, COL_R) + [ch(polar(COL_R, 72), P["P1"]), ch(P["P1"], P["C"]), ch(P["C"], P["P4"])]
    # A: port 252 -> arc R24 -> 360 (P0) and -> 144 (P2), stubs to P3 (216), P0, P2
    cuts += arc(252, 360, COL_R, 14) + arc(252, 144, COL_R, 14)
    cuts += [ch(polar(COL_R, 216), P["P3"]), ch(polar(COL_R, 0), P["P0"]), ch(polar(COL_R, 144), P["P2"])]
    # vertical feed in the port columns: barb axis -> column -> plate
    for a in PORT_ANG.values():
        x, y = polar(COL_R, a)
        cuts.append(cyl(0.7, Z_PORT, zc + 0.7, x, y, fn=12))
        cuts.append(radial_cyl(a, COL_R, COL_R + 6.2, 0.6, Z_PORT))
    # coupling washers (steel M3 washers, flush)
    for a in YOKE_MAG_ANG:
        cuts.append(cyl(WASHER_D / 2, Z_GAL1 - WASHER_T, Z_GAL1 + 0.1, *polar(YOKE_MAG_R, a), fn=32))
    # column screw pilots (from below)
    for a in COL_ANG:
        cuts.append(cyl(M2_PILOT / 2, Z_FLOOR1 + 0.9, Z_FLOOR1 + 9, *polar(COL_R, a), fn=16))
    # vent grooves on the underside, from each cartridge OD out to the rim
    for (x, y), nm in zip(PINS, PIN_NAMES):
        a = math.degrees(math.atan2(y, x)) if nm != "C" else 36.0
        r0 = math.hypot(x, y)
        cuts.append(rotz(box(r0 + 3.5, R_BLOCK + 1, -0.4, 0.4, Z_GAL0 - 0.1, Z_GAL0 + 0.5), a) if nm != "C"
                    else rotz(box(3.5, R_BLOCK + 1, -0.4, 0.4, Z_GAL0 - 0.1, Z_GAL0 + 0.5), a))
    m = Dm(m, *cuts)
    beads = [Dm(cyl(4.2, Z_GAL0 - 0.4, Z_GAL0 + 0.01, x, y), cyl(3.8, Z_GAL0 - 1, Z_GAL0 + 1, x, y)) for (x, y) in PINS]
    return U(m, *beads)

def pd08_skirt_plate():
    """WIPER SKIRT PLATE (MJF PA12, bead-blast + seal): 2 mm, 15 deg drafted rim, six wiper
    pockets (0 9 x 1.0 silicone discs), drafted 0 6 nose holes, three snap hooks."""
    prof = [(0, Z_SKIRT_BOT), (R_BLOCK - 2.0 * math.tan(math.radians(75)) * 0 - 0.54, Z_SKIRT_BOT), (R_BLOCK, Z_SKIRT_BOT + 2.0), (0, Z_SKIRT_BOT + 2.0)]
    # 15 deg draft from vertical would be tiny; the rim is a 2 mm x 0.54 mm chamfer plus R1 (hand-sanded)
    plate = revolve([(0, Z_SKIRT_BOT), (R_BLOCK - 1.0, Z_SKIRT_BOT), (R_BLOCK, Z_SKIRT_BOT + 1.0), (R_BLOCK, Z_SKIRT_BOT + 2.0), (0, Z_SKIRT_BOT + 2.0)], 96)
    cuts = []
    for (x, y) in PINS:
        cuts.append(cyl(4.55, Z_SKIRT_BOT + 1.0, Z_SKIRT_BOT + 2.1, x, y, fn=40))              # wiper pocket 0 9.1
        cuts.append(cyl(3.0, Z_SKIRT_BOT - 0.1, Z_SKIRT_BOT + 1.01, x, y, r2=2.2, fn=40))     # drafted nose hole 0 6 -> 0 4.4
    hooks = []
    for a in (0.0, 120.0, 240.0):
        h = U(box(R_BLOCK + 0.1, R_BLOCK + 1.3, -3, 3, Z_SKIRT_BOT + 1.0, Z_FLOOR0 + 2.0),
              box(R_BLOCK - 0.5, R_BLOCK + 1.3, -3, 3, Z_FLOOR0 + 1.1, Z_FLOOR0 + 1.9))
        hooks.append(rotz(h, a + 36.0))
    return U(Dm(plate, *cuts), *hooks)

def pd09_piston(x=0.0, y=0.0, e=15.0):
    zb = Z_LAND_TOP_E15 + (15.0 - e)
    p = revolve([(0, zb), (PISTON_D / 2, zb), (PISTON_D / 2, zb + PISTON_H - 0.5), (PISTON_D / 2 - 0.5, zb + PISTON_H), (0, zb + PISTON_H)], 48)
    return Dm(p, cyl(MAG_C1_D / 2, zb - 0.1, zb + MAG_C1_H, 0, 0, fn=32)).translate([x, y, 0])

def pd10_yoke():
    """YOKE (SLA): 0 28 x 3.5; three D42-N52 pockets from below at R8; three tendon notches
    (apex R10, +-22 deg flare, floor sloping 9 deg down outward) with ferrule pockets."""
    y = cyl(R_YOKE, Z_YOKE0, Z_YOKE1, fn=96)
    cuts = []
    for a in YOKE_MAG_ANG:
        cuts.append(cyl(MAG_CPL_D / 2, Z_YOKE0 - 0.1, Z_YOKE0 + MAG_CPL_H, *polar(YOKE_MAG_R, a), fn=40))
    for a in POST_ANG:
        # flared notch: hull of a thin slot at the apex and a wide slot at the rim
        apex = rotz(box(POST_R - 0.1, POST_R + 0.1, -0.45, 0.45, Z_CABLE - 0.45, Z_YOKE1 + 0.1), a)
        w = 2 * (R_YOKE - POST_R + 0.5) * math.tan(math.radians(22)) + 0.9
        rim = rotz(box(R_YOKE + 0.4, R_YOKE + 0.6, -w / 2, w / 2, Z_CABLE - 0.45 - 0.7, Z_YOKE1 + 0.1), a)
        cuts.append(Manifold.batch_hull([apex, rim]))
        cuts.append(rotz(box(POST_R - 4.2, POST_R - 0.4, -1.1, 1.1, Z_CABLE - 1.1, Z_YOKE1 + 0.1), a))   # ferrule pocket
        cuts.append(rotz(box(POST_R - 0.5, POST_R + 0.2, -0.45, 0.45, Z_CABLE - 0.45, Z_YOKE1 + 0.1), a))
    # 0 3 lift-off hole in the centre
    cuts.append(cyl(1.5, Z_YOKE0 - 0.1, Z_YOKE1 + 0.1, fn=20))
    return Dm(y, *cuts)

def pd11_stop_block(a=90.0):
    """TENDON STOP (PETG): sits on the stop arm at R65; housing ferrule cup on a 2 N/mm
    compression spring (series spring) in a 0 5.2 bore; M3 barrel adjuster from the outside."""
    L = 14.0
    b = box(STOP_R - 6.0, STOP_R - 6.0 + L, -4.0, 4.0, Z_CABLE - 3.5, Z_CABLE + 4.0)
    cuts = [Manifold.cylinder(L + 2, 2.6, 2.6, 32).rotate([0, 90, 0]).translate([STOP_R - 6.0 + 2.5, 0, Z_CABLE]),     # spring bore 0 5.2
            Manifold.cylinder(4, 0.5, 0.5, 12).rotate([0, 90, 0]).translate([STOP_R - 7.0, 0, Z_CABLE]),             # cable exit 0 1.0
            Manifold.cylinder(3, M3_INS_D / 2, M3_INS_D / 2, 24).rotate([0, 90, 0]).translate([STOP_R - 6 + L - 3.0, 0, Z_CABLE]),
            cyl(1.0, Z_CABLE - 5, Z_CABLE - 2, STOP_R - 2.0, -2.5, fn=16), cyl(1.0, Z_CABLE - 5, Z_CABLE - 2, STOP_R - 2.0, 2.5, fn=16)]
    return rotz(Dm(b, *cuts), a)

def pd12_skid_stem(a=60.0, H=0.0):
    """SKID STEM (PETG, 0 6): from the top-ring boss (M3 insert at the top) down to the foot;
    the R15 foot cap is PD13. H = skid length setting (+ = longer)."""
    ztop = Z_SK1 - 3.5; zbot = ZF + SKID_DOME_R - 1.0 - H
    s = cyl(SKID_STEM_D / 2, zbot, ztop, fn=32)
    s = Dm(s, cyl(M3_INS_D / 2, ztop - M3_INS_L, ztop + 0.1, fn=24), box(2.5, 4, -4, 4, zbot + 12, ztop + 1),   # flat = anti-rotation
           cyl(1.9, zbot + 3.0, ztop - M3_INS_L - 2.0, fn=24))                                                        # hollow 0 3.8
    x, y = polar(SKID_R, a)
    return s.translate([x, y, 0])

def pd13_skid_foot(a=60.0, H=0.0):
    """SKID FOOT (SLA, polished): R15 spherical cap 0 8, its axis tilted toward the head centre,
    on a 0 6 socket for the stem."""
    x, y = polar(SKID_R, a)
    cen = np.array([x, y, ZF - H])
    tilt = math.degrees(math.asin(SKID_R / (85.0 + SKID_DOME_R)))
    cap = sphere(SKID_DOME_R, (0, 0, 0), 96) ^ cyl(SKID_FOOT_D / 2, -SKID_DOME_R - 0.1, -SKID_DOME_R + 3.0, fn=48)
    cap = cap.rotate([0, -tilt, 0]).rotate([0, 0, a]).translate(list(cen))
    sock = Dm(cyl(4.5, ZF - H + SKID_DOME_R - 6.0, ZF - H + SKID_DOME_R + 1.0, x, y, fn=40),
              cyl(SKID_STEM_D / 2 + 0.1, ZF - H + SKID_DOME_R - 1.0, ZF - H + SKID_DOME_R + 1.5, x, y, fn=40))
    neck = Manifold.batch_hull([cap, cyl(4.5, ZF - H + SKID_DOME_R - 6.0, ZF - H + SKID_DOME_R - 5.0, x, y, fn=40)])
    return U(neck, sock)

def pd14_skid_knob(a=60.0):
    x, y = polar(SKID_R, a)
    k = cyl(6.0, Z_SK1 + 0.2, Z_SK1 + 6.0, x, y, fn=12)        # 12-lobe knob (one click = 1/12 turn = 0.042 mm)
    return Dm(k, cyl(2.85, Z_SK1 + 0.1, Z_SK1 + 3.2, x, y, fn=6), cyl(M3_CLEAR / 2, Z_SK1 - 1, Z_SK1 + 7, x, y, fn=16))

def pd15_nail(x=0.0, y=0.0, e=15.0):
    """NAIL (CNC-turned POM, red if available) - reference solid. Tip at the scalp at e=15."""
    z0 = 15.0 - e
    h = (LAND_D - TIP_FLAT_D) / 2          # 90 deg cone: height = radial step
    prof = [(0, z0), (TIP_FLAT_D / 2 - TIP_R, z0), (TIP_FLAT_D / 2, z0 + TIP_R * 0.6), (LAND_D / 2, z0 + h + TIP_R * 0.4),
            (LAND_D / 2, z0 + Z_LAND_TOP_E15 - NAIL_TOP_R), (LAND_D / 2 - NAIL_TOP_R, z0 + Z_LAND_TOP_E15), (0, z0 + Z_LAND_TOP_E15)]
    return revolve(prof, 64).translate([x, y, 0])

def pd16_hang_cup():
    """HANG CUP (PETG): 0 22 cup with a 0.6 mm monofilament eye; empty mass ~2.5 g; fill with
    rice to 11.0 g (must HOLD) and 20.0 g (must DROP) - the per-session C1 check."""
    c = Dm(cyl(11, 0, 14, fn=64), cyl(10, 1.0, 15, fn=64))
    eye = Dm(box(-1.5, 1.5, -6, 6, 13.5, 18), Manifold.cylinder(4, 1.0, 1.0, 16).rotate([90, 0, 0]).translate([0, 2, 16.2]))
    return U(c, eye).translate([150, 0, 0])

def pd17_shadow_card():
    """SHADOWGRAPH CARD (PETG, black): 80 x 30 x 1.2 with the nail's max-material outline cut
    through at 1:1 (+0.05) and a 0 3.95 / 0 3.88 go/no-go slot pair for the land."""
    card = box(0, 80, 0, 30, 0, 1.2)
    h = (LAND_D - TIP_FLAT_D) / 2
    pts = [(5, 15 - 1.05), (5 + 0.05 + 0.4, 15 - 1.05), (5 + h + 0.05, 15 - LAND_D / 2 - 0.05), (75, 15 - LAND_D / 2 - 0.05),
           (75, 15 + LAND_D / 2 + 0.05), (5 + h + 0.05, 15 + LAND_D / 2 + 0.05), (5 + 0.45, 15 + 1.05), (5, 15 + 1.05)]
    win = cs_poly(pts).extrude(2.0).translate([0, 0, -0.4])
    slots = [box(10, 30, 24.0, 24.0 + 3.95, -0.4, 1.6), box(40, 60, 24.0, 24.0 + 3.88, -0.4, 1.6)]
    return Dm(card, win, *slots).translate([150, 40, 0])

def pd18_skid_gauge():
    """SKID HEIGHT GAUGE (PETG): stepped block 0..9 mm in 0.5 mm steps to set the three skids
    equal against the deck reference face; see pad.md 11."""
    steps = [box(i * 4.0, i * 4.0 + 4.0, 0, 12, 0, 3.0 + 0.5 * i) for i in range(19)]
    return U(*steps).translate([150, 80, 0])


def pd19_s0_pocket():
    """S0 SINGLE-POCKET BENCH (SLA): pocket 0's ceiling (30 deg) as a 3 mm shell with a
    square flange, re-centred on its home; used upside-down on the S0 dish bench with one
    1/4 in PTFE ball on a hand-guided slider to prove the v3b profile, smoothness and noise."""
    rs, th, homes, Zs = load_pockets()
    h = homes[0]
    outer = hf_prism(rs, th, Zs[0], Z_DECK_TOP, h, r_extra=3.0)
    cav = hf_prism(rs, th, Zs[0] + 3.0, Z_DECK_TOP + 1.0, h)
    shell = (outer - cav) ^ box(-200, 200, -200, 200, 0, Z_DECK_TOP)
    flange = Dm(box(h[0] - 40, h[0] + 40, h[1] - 40, h[1] + 40, Z_DECK_TOP - 3, Z_DECK_TOP),
                cyl(rs[-1] + 2.0, Z_DECK_TOP - 4, Z_DECK_TOP + 1, h[0], h[1], fn=96),
                *[cyl(1.7, Z_DECK_TOP - 4, Z_DECK_TOP + 1, h[0] + sx * 34, h[1] + sy * 34, fn=16) for sx in (-1, 1) for sy in (-1, 1)])
    return U(shell, flange).translate([-h[0], -h[1] + 200.0, 0])

# ===================================================================== registry
PARTS = [
    ("PD01_deck", pd01_deck, "SLA", 1, "deck with three pocket ceilings, HALO seats"),
    ("PD02_skirt_frame", pd02_skirt_frame, "MJF", 1, "skirt frame: rings, struts, stop arms, skid bosses, lift hooks"),
    ("PD05_floor_plate", pd05_floor_plate, "SLA", 1, "floor plate: lower bushes, sockets, lift eyelets"),
    ("PD06_cartridge", lambda: pd06_cartridge(*PINS[1]), "SLA", 6, "pin cartridge (x6 + 2 spares)"),
    ("PD07_gallery_plate", pd07_gallery_plate, "SLA", 1, "gallery plate: galleries, columns, barbs, dome lugs"),
    ("PD08_skirt_plate", pd08_skirt_plate, "MJF", 1, "wiper skirt plate (snaps on)"),
    ("PD09_piston", lambda: pd09_piston(*PINS[1]), "SLA", 6, "piston (x6 + 2 spares)"),
    ("PD10_yoke", pd10_yoke, "SLA", 1, "tendon yoke"),
    ("PD11_stop_block", pd11_stop_block, "PETG", 3, "tendon stop block (x3)"),
    ("PD12_skid_stem", pd12_skid_stem, "PETG", 3, "skid stem (x3)"),
    ("PD13_skid_foot", pd13_skid_foot, "SLA", 3, "skid foot R15 (x3)"),
    ("PD14_skid_knob", pd14_skid_knob, "PETG", 3, "skid adjuster knob (x3)"),
    ("PD15_nail_reference", lambda: pd15_nail(*PINS[1]), "POM", 6, "nail - CNC turned, reference only"),
    ("PD16_hang_cup", pd16_hang_cup, "PETG", 1, "C1 hang-test cup"),
    ("PD17_shadow_card", pd17_shadow_card, "PETG", 1, "nail shadowgraph card"),
    ("PD18_skid_gauge", pd18_skid_gauge, "PETG", 1, "skid height gauge"),
    ("PD19_s0_pocket", pd19_s0_pocket, "SLA", 1, "S0 single-pocket dish bench (not head-borne)"),
]

def write_svg():
    """1:1 and 10:1 nail shadowgraph template (pad.md 6.4)."""
    h = (LAND_D - TIP_FLAT_D) / 2
    def outline(sc, ox, oy, tol):
        pts = [(0, -TIP_FLAT_D / 2 + TIP_R), (0, TIP_FLAT_D / 2 - TIP_R), (TIP_R, TIP_FLAT_D / 2), (h, LAND_D / 2), (Z_LAND_TOP_E15, LAND_D / 2),
               (Z_LAND_TOP_E15, -LAND_D / 2), (h, -LAND_D / 2), (TIP_R, -TIP_FLAT_D / 2)]
        return " ".join(f"{ox + p[0] * sc:.3f},{oy - (p[1] + math.copysign(tol, p[1] if p[1] else 1)) * sc:.3f}" for p in pts)
    W, Hh = 260, 150
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}mm" height="{Hh}mm" viewBox="0 0 {W} {Hh}">',
         '<rect width="100%" height="100%" fill="white"/>',
         '<text x="5" y="8" font-size="4" font-family="Helvetica">SP1 v3 nail shadowgraph template - print at 100 % (check the 50 mm bar), PAD pad.md 6.4</text>',
         '<line x1="5" y1="14" x2="55" y2="14" stroke="black" stroke-width="0.3"/><text x="57" y="15" font-size="3">50 mm check bar</text>']
    # 10:1 tip detail: max (red) and min (blue) envelopes
    s.append(f'<polygon points="{outline(10, 20, 80, 0.05)}" fill="none" stroke="red" stroke-width="0.3"/>')
    s.append(f'<polygon points="{outline(10, 20, 80, -0.05)}" fill="none" stroke="blue" stroke-width="0.3"/>')
    s.append('<text x="20" y="112" font-size="3.5">10:1 tip: the shadow edge must lie between RED (max) and BLUE (min) everywhere; flat 0 2.0, rim R0.4, 90 deg cone to 0 3.92; NO narrowing anywhere going up</text>')
    s.append(f'<polygon points="{outline(1, 20, 135, 0.05)}" fill="none" stroke="black" stroke-width="0.2"/>')
    s.append('<text x="20" y="145" font-size="3.5">1:1 whole nail (59.9 mm). Top end R0.5, steel insert flush.</text></svg>')
    open(os.path.join(HERE, "shadowgraph_nail.svg"), "w").write("\n".join(s))

def write_pockets_scad():
    rs, th, homes, Zs = load_pockets()
    lines = ["// pockets_data.scad - GENERATED by gen_pad_stl.py from pockets.npz (pad_geom2.py). Do not edit.",
             f"POCKET_RS = [{', '.join(f'{r:.3f}' for r in rs)}];",
             f"POCKET_TH = [{', '.join(f'{math.degrees(t):.3f}' for t in th)}];",
             f"POCKET_HOMES = [{', '.join('[%.3f, %.3f, %.3f]' % tuple(h) for h in homes)}];"]
    for k in range(3):
        rows = ", ".join("[" + ", ".join(f"{v:.3f}" for v in Zs[k][i]) + "]" for i in range(len(rs)))
        lines.append(f"POCKET_Z{k} = [{rows}];")
    open(os.path.join(HERE, "pockets_data.scad"), "w").write("\n".join(lines) + "\n")

def main():
    only = None
    if "--only" in sys.argv:
        only = set(sys.argv[sys.argv.index("--only") + 1].split(","))
    ok = True; rows = []
    for name, fn, mat, qty, desc in PARTS:
        if only and name.split("_")[0] not in only: continue
        m = fn(); tm = to_trimesh(m)
        path = os.path.join(OUT, name + ".stl"); tm.export(path)
        wt = tm.is_watertight; ok &= wt
        vol = m.volume() / 1000.0
        mass = vol * DENS[mat]
        bb = tm.bounds
        rows.append((name, mat, qty, round(vol, 3), round(mass, 2), round(mass * qty, 2), desc))
        print(f"{name:22s} {mat:4s} x{qty}  bbox {bb[0].round(1)} .. {bb[1].round(1)}  size {(bb[1]-bb[0]).round(1)}  vol {vol:7.3f} cm3  mass {mass:6.2f} g (x{qty} = {mass*qty:6.2f})  watertight {wt}", flush=True)
    if not only:
        with open(os.path.join(HERE, "mass_by_part.csv"), "w", newline="") as f:
            w = csv.writer(f); w.writerow(["part", "material", "qty", "vol_cm3", "mass_g_each", "mass_g_total", "description"]); w.writerows(rows)
        write_svg(); write_pockets_scad()
    print("ALL WATERTIGHT" if ok else "NOT ALL WATERTIGHT")
    sys.exit(0 if ok else 1)

if __name__ == "__main__":
    main()
