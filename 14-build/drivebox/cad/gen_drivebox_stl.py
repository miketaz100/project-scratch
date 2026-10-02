#!/usr/bin/env python
"""
gen_drivebox_stl.py - STL generator for the SP1 v3 DRIVE BOX printed parts
(PROJECT SCRATCH, 14-build/drivebox/cad, DRIVE BOX WP, 2026-10-02, rev 1)

THE .scad FILES ARE THE SOURCE OF TRUTH.  Every constant below has the same name as in
lib_drivebox.scad / dbNN_*.scad.  No OpenSCAD binary exists on the build machine, so this
script rebuilds the same solids with manifold3d and exports through trimesh, then prints
name, bounding box, volume, mass (PETG 1.27 / SLA resin 1.15 / PA12 1.01 g/cm3) and a
watertight flag.  Exit code 0 only if every mesh is watertight, single-shell and valid.

Frames (README.md):
  D  drum-module frame: deck top surface z = 0; +x points at the umbilical wall; y across.
  b  bulkhead frame: u (= STL x) outward normal of the right end wall, u = 0 on the wall's
     OUTSIDE surface; v (= STL y) horizontal along the wall (= case Y); w (= STL z) up.
  L  local frame for loose parts (hook plate, hooks, saddles, clip, seat, bracket, baffle).

Run:  <cadenv>/bin/python gen_drivebox_stl.py [--only DB01,DB03]
"""
import math, os, sys
import numpy as np
import trimesh
import manifold3d as m3
from manifold3d import Manifold, CrossSection

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "stl")
os.makedirs(OUT, exist_ok=True)
FN = 48

# ============================ lib_drivebox constants ============================
M3_CLEAR, M4_CLEAR, M5_CLEAR = 3.4, 4.5, 5.5
M3_INS_D, M3_INS_L = 4.0, 6.0           # brass heat-set M3 x 5.7 (hole 4.0, 6 deep)
M3_TAP, M5_TAP = 2.5, 4.2               # tap drills (SLA parts are tapped, not heat-set)
M3_NUT_AF, M3_NUT_T = 5.6, 2.6
M5_NUT_AF, M5_NUT_T = 8.2, 4.2
NUT_1420_AF, NUT_1420_T = 11.3, 6.0     # 1/4-20 hex nut 7/16 in AF

# --- drum module (frame D) ---
MOTOR_X = 34.0
MOTOR_Y = (23.0, 69.0, 115.0)           # motor pitch 46
CABLE_Y = tuple(y + 6.0 for y in MOTOR_Y)   # 29, 75, 121 : tangent line of each drum (pitch R 6)
DRUM_Z0 = 1.0                           # drum bottom above the deck top
ROW_Z = (14.0, 22.0)                    # cable heights: groove 1 (pad 1), groove 2 (pad 2 provision)
MOTOR_BOSS_D = 22.6
MOTOR_HOLE = 15.5                       # 31 mm square pattern
INDEX_R = 12.0                          # index magnet radius on the drum flange
DECK = dict(X0=0.0, X1=150.0, Y0=0.0, Y1=140.0, T=4.0, LEG_Z=-28.0)
LEGS = ((0, 10, 0, 12), (0, 10, 128, 140), (80, 92, 0, 12), (80, 92, 128, 140),
        (138, 150, 0, 12), (138, 150, 128, 140))
ROD_Y = (5.0, 135.0)
ROD_Z = 16.0
ROD_HOLE_D = 3.9                        # press fit for the 4 mm rod
POST_REAR = (57.5, 65.5)
POST_FRONT = (139.5, 147.5)
POST_TOP = 21.0
FP = dict(X0=100.0, X1=108.0, Z0=2.0, Z1=30.0, BOSS_R=6.0, BOSS_X1=112.0, LM4UU_D=8.1)
TONGUE = dict(ROOT=14.0, TIP=3.0, SLOT=1.0, T=2.5, POCKET_Z0=10.0, POCKET_Z1=26.0)
SEAT = dict(R=3.0, X1=114.0, BORE_D=2.5, FLOOR=1.0, CABLE_D=1.0)            # brass-ferrule housing (default)
SEAT_4MM = dict(R=3.6, X1=114.0, BORE_D=5.2, FLOOR=1.0, CABLE_D=1.5)        # 4 mm bicycle housing variant
MAG = dict(DY=-5.0, BOSS_R=2.5, BOSS_X0=101.5, POCKET_D=3.4, POCKET_DEPTH=2.2)
BRIDGE = dict(X0=94.0, X1=99.0, Y0=13.0, Y1=127.0, Z0=2.0, Z1=30.0, SENS_W=4.4, SENS_H=3.4, SENS_T=1.7, LEAD_W=3.2, CABLE_D=3.0)
BRIDGE_SCREWS = ((47.0, 9.0), (47.0, 23.0), (93.0, 9.0), (93.0, 23.0))
SHELF_HOLES = ((60.0, 52.0), (60.0, 98.0), (145.0, 52.0), (145.0, 98.0))   # M3 standoffs for the electronics shelf
REL_SLOT = 0.8                          # cable release slot width (tongue, seat boss, bridge): lets a tendon lift out for unpacking
HOUS_OD = 1.6                           # housing OD used by the comb (brass ferrule variant); 4.3 for the 4 mm variant

# --- drum (local, axis z, z = 0 drum bottom) ---
DRUM = dict(FL_R=15.0, FL_H=3.0, HUB_R=8.0, HUB_Z1=10.5, G1_Z0=10.5, G_LEN=5.0, LAND_R=6.15,
            DIV_R=10.0, DIV_Z0=15.5, DIV_Z1=18.5, G2_Z0=18.5, TOP_Z0=23.5, TOP_Z1=25.5,
            PITCH_R=6.0, GROOVE_R=0.25, TURNS=5.0, BORE_R=2.55, FLAT_X=2.1, GRUB_Z=6.5,
            NUT_X0=3.7, NUT_X1=6.3, NUT_HY=3.3, NUT_Z1=9.6, MAG_R=1.7, MAG_DEPTH=2.2,
            ANCH_HX=1.8, ANCH_Y0=5.7, ANCH_Y1=7.9, ANCH_DEPTH=2.4)

# --- bulkhead / plug (frame b) ---
WALL_T = 3.0                            # Apache 2800 end-wall shell [VERIFY on the case]
HEAD = dict(U0=0.0, U1=14.0, V=62.0, W=25.0)
NECK = dict(U0=-17.0, V=36.0, W=19.0)
PLUG = dict(U0=14.0, U1=30.0)
PORT_V = (-16.0, 0.0, 16.0)
PORT_W = 8.0
PORT_D = 2.0
ORING = dict(ID=3.0, OD=5.6, DEPTH=0.75)  # metric 3 x 1 NBR70 face seal
SLOT = dict(V=26.0, W0=-14.0, W1=-6.0)
DOWEL = dict(V=28.0, W=16.0, D_PRESS=2.95, D_SLIDE=3.1, DEPTH=10.0)
THUMB = dict(V=52.0, W=0.0, D=4.5, NUT_AF=7.2, NUT_T=3.4, NUT_U=7.0)
CLAMP = dict(V=42.0, W=19.0, CB_D=6.5, CB_DEPTH=3.5, PLATE_V=50.0, PLATE_W=30.0, T=4.0)
PCLIP = dict(V=20.0, W=-20.0, DEPTH=8.0)
# lightening pockets (blind): (v0, v1, w0, w1) mirrored about v = 0, depth from the stated face
B1_HEAD_POCKETS = ((38.0, 47.0, -15.0, 12.0),)          # from the head's wall face u = 0, depth 8
B1_NECK_POCKETS = ((21.0, 33.0, -4.0, 16.0),)           # from the neck's inner face, depth 10
U1_POCKETS = ((33.0, 46.0, -22.0, 10.0),)               # from the plug's rear face, depth 10
U1_POCKET_C = (-10.0, 10.0, 14.0, 22.0)                 # centre pocket above the middle port, depth 10

# --- hook plate and hooks (local) ---
HP = dict(X=216.0, Y=136.0, T=6.0, R=8.0, LID_X=100.0, LID_Y=60.0, CB_D=10.0, CB_DEPTH=3.6,
          SLOT_X=82.0, SLOT_W=6.0, SLOT_L=42.0, HOOK_X=60.0, HOOK_Y=(30.0, 55.0),
          WIN=((-25, -28), (25, -28), (-25, 28), (25, 28)), WIN_X=40.0, WIN_Y=36.0)
HOOK = dict(T=6.0, WIDTH=25.0, LEG_Q=64.0, BAR_Q0=58.0, DROP_Q0=34.0, GUSSET=8.0, HOLE_Q=(10.0, 35.0))

# --- pegboard, saddles, clip, seat, baffle, bracket (local) ---
PEG = dict(X=100.0, Y=90.0, T=4.0, PITCH=10.0, HOLE_D=3.4, FL_Z=20.0, FL_T=4.0, FL_HOLES=(-45.0, 0.0, 45.0))
SADDLE_L = 16.0
SEAT15 = dict(R=13.0, H=14.0, BOLT_R=3.4, BOLT_Z=7.0, MAG_R=3.1, MAG_Z0=8.0, CONE_R0=7.0, CONE_R1=10.0, CONE_Z0=11.0)
CLIP = dict(X=15.0, Y=14.0, H=9.0, CH_R=6.2, HOLE_X=9.0, HOLE_Y=10.5, NOSE_R0=9.75, NOSE_R1=6.75, NOSE_H=3.0,
            WASHER_R=6.2, WASHER_DEPTH=1.7)

DENS = {"PETG": 1.27, "SLA": 1.15, "PA12": 1.01, "TPU": 1.21}

# ============================ helpers ============================
def U(*ms):
    ms = [m for m in ms if m is not None]
    return Manifold.batch_boolean(ms, m3.OpType.Add) if len(ms) > 1 else ms[0]

def D(m, *cuts):
    cuts = [c for c in cuts if c is not None]
    return m - (Manifold.batch_boolean(cuts, m3.OpType.Add) if len(cuts) > 1 else cuts[0]) if cuts else m

def box(x0, x1, y0, y1, z0, z1):
    return Manifold.cube([x1 - x0, y1 - y0, z1 - z0]).translate([x0, y0, z0])

MAP_Y = [[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0]]
MAP_X = [[0, 0, 1, 0], [1, 0, 0, 0], [0, 1, 0, 0]]

def cyl_z(r, z0, z1, x=0.0, y=0.0, r2=None, fn=FN):
    return Manifold.cylinder(z1 - z0, r, r if r2 is None else r2, fn).translate([x, y, z0])

def cyl_x(r, x0, x1, y=0.0, z=0.0, fn=FN):
    return Manifold.cylinder(x1 - x0, r, r, fn).transform(MAP_X).translate([x0, y, z])

def cyl_y(r, y0, y1, x=0.0, z=0.0, fn=FN):
    return Manifold.cylinder(y1 - y0, r, r, fn).transform(MAP_Y).translate([x, y0, z])

def hex_z(af, z0, z1, x=0.0, y=0.0):
    """hexagonal prism, across-flats af (vertices on +/-x, flats parallel to x)"""
    return Manifold.cylinder(z1 - z0, af / 2 / math.cos(math.pi / 6), af / 2 / math.cos(math.pi / 6), 6).translate([x, y, z0])

def cs_poly(pts):
    P = [(float(a), float(b)) for a, b in pts]
    area = sum(P[i][0] * P[(i + 1) % len(P)][1] - P[(i + 1) % len(P)][0] * P[i][1] for i in range(len(P)))
    if area < 0:
        P.reverse()
    return CrossSection([P])

def cs_rect(u0, u1, v0, v1):
    return cs_poly([(u0, v0), (u1, v0), (u1, v1), (u0, v1)])

def cs_crrect(cu, cv, su, sv, r):
    return cs_rect(cu - su / 2 + r, cu + su / 2 - r, cv - sv / 2 + r, cv + sv / 2 - r).offset(r, m3.JoinType.Round, 2.0, FN)

def ext_z(cs, z0, z1):
    return cs.extrude(z1 - z0).translate([0, 0, z0])

def ext_y(cs_xz, y0, y1):
    return cs_xz.extrude(y1 - y0).transform(MAP_Y).translate([0, y0, 0])

def ext_x(cs_yz, x0, x1):
    return cs_yz.extrude(x1 - x0).transform(MAP_X).translate([x0, 0, 0])

def to_trimesh(m):
    mm = m.to_mesh()
    return trimesh.Trimesh(vertices=np.asarray(mm.vert_properties)[:, :3], faces=np.asarray(mm.tri_verts), process=False)

# ============================ DB01 drum (db01_drum.scad) ============================
def db01_drum(d=DRUM):
    body = U(cyl_z(d["FL_R"], 0, d["FL_H"]),
             cyl_z(d["HUB_R"], d["FL_H"], d["HUB_Z1"]),
             cyl_z(d["LAND_R"], d["G1_Z0"], d["G1_Z0"] + d["G_LEN"]),
             cyl_z(d["DIV_R"], d["DIV_Z0"], d["DIV_Z1"]),
             cyl_z(d["LAND_R"], d["G2_Z0"], d["G2_Z0"] + d["G_LEN"]),
             cyl_z(d["HUB_R"], d["TOP_Z0"], d["TOP_Z1"]))
    helix = CrossSection.circle(d["GROOVE_R"], 16).translate([d["PITCH_R"], 0]).extrude(
        d["G_LEN"], int(d["TURNS"] * 72), d["TURNS"] * 360.0)          # right-hand helix, pitch 1.0
    g1 = helix.translate([0, 0, d["G1_Z0"]])
    g2 = helix.translate([0, 0, d["G2_Z0"]])
    bore = D(cyl_z(d["BORE_R"], -0.01, d["TOP_Z1"] + 0.01), box(d["FLAT_X"], 3.0, -3, 3, -0.02, d["TOP_Z1"] + 0.02))
    nut = box(d["NUT_X0"], d["NUT_X1"], -d["NUT_HY"], d["NUT_HY"], -0.01, d["NUT_Z1"])
    grub = cyl_x(1.65, 0.0, d["HUB_R"] + 0.01, 0.0, d["GRUB_Z"], fn=24)
    mag = cyl_z(d["MAG_R"], -0.01, d["MAG_DEPTH"], -INDEX_R, 0.0, fn=24)
    anchors = []
    for ztop in (d["HUB_Z1"], d["DIV_Z1"]):
        anchors.append(box(-d["ANCH_HX"], d["ANCH_HX"], d["ANCH_Y0"], d["ANCH_Y1"], ztop - d["ANCH_DEPTH"], ztop + 0.01))
        anchors.append(box(-6.0, -d["ANCH_HX"] + 0.01, 6.2, 7.2, ztop - 1.0, ztop + 0.01))   # cable lead-out notch
    return D(body, g1, g2, bore, nut, grub, mag, *anchors)

# ============================ DB02 drum deck (db02_deck.scad) ============================
def db02_deck(p=DECK):
    plate = box(p["X0"], p["X1"], p["Y0"], p["Y1"], -p["T"], 0)
    legs = [box(x0, x1, y0, y1, p["LEG_Z"], -p["T"] + 0.01) for (x0, x1, y0, y1) in LEGS]
    posts = []
    for (x0, x1) in (POST_REAR, POST_FRONT):
        for yr in ROD_Y:
            posts.append(box(x0, x1, yr - 5, yr + 5, -0.01, POST_TOP))
    body = U(plate, *legs, *posts)
    cuts = []
    for (x0, x1, y0, y1) in LEGS:
        cuts.append(cyl_z(M4_CLEAR / 2, p["LEG_Z"] - 0.01, 0.01, (x0 + x1) / 2, (y0 + y1) / 2, fn=24))
    for my in MOTOR_Y:
        cuts.append(cyl_z(MOTOR_BOSS_D / 2, -p["T"] - 0.01, 0.01, MOTOR_X, my))
        for dx in (-MOTOR_HOLE, MOTOR_HOLE):
            for dy in (-MOTOR_HOLE, MOTOR_HOLE):
                cuts.append(cyl_z(M3_CLEAR / 2, -p["T"] - 0.01, 0.01, MOTOR_X + dx, my + dy, fn=24))
        sx = MOTOR_X - INDEX_R
        cuts.append(box(sx - 1.7, sx + 1.7, my - 2.2, my + 2.2, -1.7, 0.01))      # index Hall pocket (TO-92 flat, face up)
        cuts.append(box(-0.01, sx - 1.69, my - 1.6, my + 1.6, -1.7, 0.01))        # lead channel to the deck edge
    for (x0, x1) in (POST_REAR, POST_FRONT):
        for yr in ROD_Y:
            cuts.append(cyl_x(ROD_HOLE_D / 2, x0 - 0.01, x1 + 0.01, yr, ROD_Z, fn=24))
    for (hx, hy) in SHELF_HOLES:
        cuts.append(cyl_z(M3_CLEAR / 2, -p["T"] - 0.01, 0.01, hx, hy, fn=24))
    for tx in (94.0, 100.0, 106.0):
        cuts.append(box(tx - 0.4, tx + 0.4, 118.0, 126.0, -0.6, 0.01))            # working-point ticks W-6 / W / W+6
    return D(body, *cuts)

# ============================ DB03 floating stop plate (db03_floating_plate.scad) ============================
def db03_floating_plate(seat=SEAT):
    f, t = FP, TONGUE
    body = U(box(f["X0"], f["X1"], 0.0, DECK["Y1"], f["Z0"], f["Z1"]),
             *[cyl_x(f["BOSS_R"], f["X0"], f["BOSS_X1"], yr, ROD_Z) for yr in ROD_Y])
    tx0 = f["X1"] - t["T"]                                   # tongue back face x 105.5
    cuts = [cyl_x(f["LM4UU_D"] / 2, f["X0"] - 0.01, f["BOSS_X1"] + 0.01, yr, ROD_Z) for yr in ROD_Y]
    adds = []
    for yc in CABLE_Y:
        y0, y1 = yc - t["ROOT"], yc + t["TIP"] + t["SLOT"]
        cuts.append(box(f["X0"] - 0.01, tx0, y0, y1, t["POCKET_Z0"], t["POCKET_Z1"]))
        for (za, zb) in ((ROW_Z[0] - 4, ROW_Z[0] - 3), (ROW_Z[0] + 3, ROW_Z[1] - 3), (ROW_Z[1] + 3, ROW_Z[1] + 4)):
            cuts.append(box(tx0 - 0.01, f["X1"] + 0.01, y0, y1, za, zb))
        cuts.append(box(tx0 - 0.01, f["X1"] + 0.01, yc + t["TIP"], y1, t["POCKET_Z0"], t["POCKET_Z1"]))
        for zr in ROW_Z:
            adds.append(cyl_x(seat["R"], f["X1"] - 0.01, seat["X1"], yc, zr))
            adds.append(cyl_x(MAG["BOSS_R"], MAG["BOSS_X0"], tx0 + 0.01, yc + MAG["DY"], zr))
    body = U(body, *adds)
    for yc in CABLE_Y:
        for zr in ROW_Z:
            cuts.append(cyl_x(seat["BORE_D"] / 2, f["X1"] + seat["FLOOR"], seat["X1"] + 0.01, yc, zr))
            cuts.append(cyl_x(seat["CABLE_D"] / 2, f["X0"] - 0.01, seat["X1"] + 0.01, yc, zr, fn=24))
            cuts.append(cyl_x(MAG["POCKET_D"] / 2, MAG["BOSS_X0"] - 0.01, MAG["BOSS_X0"] + MAG["POCKET_DEPTH"], yc + MAG["DY"], zr, fn=24))
            cuts.append(box(tx0 - 0.01, seat["X1"] + 0.01, yc - REL_SLOT / 2, yc + REL_SLOT / 2, zr, zr + seat["R"] + 0.01))   # cable release slot
    for (yy, zz) in BRIDGE_SCREWS:
        cuts.append(cyl_x(M3_INS_D / 2, f["X0"] - 0.01, f["X0"] + M3_INS_L, yy, zz, fn=24))
    return D(body, *cuts)

# ============================ DB04 Hall bridge (db04_hall_bridge.scad) ============================
def db04_hall_bridge(b=BRIDGE):
    body = box(b["X0"], b["X1"], b["Y0"], b["Y1"], b["Z0"], b["Z1"])
    cuts = [cyl_x(M3_CLEAR / 2, b["X0"] - 0.01, b["X1"] + 0.01, yy, zz, fn=24) for (yy, zz) in BRIDGE_SCREWS]
    for yc in CABLE_Y:
        ys = yc + MAG["DY"]
        for i, zr in enumerate(ROW_Z):
            cuts.append(box(b["X1"] - b["SENS_T"], b["X1"] + 0.01, ys - b["SENS_W"] / 2, ys + b["SENS_W"] / 2, zr - b["SENS_H"] / 2, zr + b["SENS_H"] / 2))
            if i == 0:
                cuts.append(box(b["X1"] - b["SENS_T"], b["X1"] + 0.01, ys - b["LEAD_W"] / 2, ys + b["LEAD_W"] / 2, b["Z0"] - 0.01, zr - b["SENS_H"] / 2 + 0.01))
            else:
                cuts.append(box(b["X1"] - b["SENS_T"], b["X1"] + 0.01, ys - b["LEAD_W"] / 2, ys + b["LEAD_W"] / 2, zr + b["SENS_H"] / 2 - 0.01, b["Z1"] + 0.01))
            cuts.append(cyl_x(b["CABLE_D"] / 2, b["X0"] - 0.01, b["X1"] + 0.01, yc, zr, fn=24))
        cuts.append(box(b["X0"] - 0.01, b["X1"] + 0.01, yc - REL_SLOT / 2, yc + REL_SLOT / 2, ROW_Z[0], b["Z1"] + 0.01))   # cable release slot
    return D(body, *cuts)

# ============================ DB05 housing comb (db05_comb.scad) ============================
def db05_comb(hous_od=HOUS_OD):
    r = hous_od / 2 + 0.15
    body = U(box(0, 10, 0, 110, 0, 8), box(0, 10, 70, 90, 7.99, 22))
    cuts = [cyl_x(4.0, -0.01, 10.01, 80.0, 16.0)]
    for gy in (9.0, 55.0, 101.0):
        cuts.append(cyl_x(r, -0.01, 10.01, gy, 4.0, fn=24))
        cuts.append(box(-0.01, 10.01, gy - r, gy + r, 4.0, 8.01))
    return D(body, *cuts)

# ============================ DB06 bulkhead (db06_bulkhead.scad) ============================
def db06_bulkhead():
    body = U(box(HEAD["U0"], HEAD["U1"], -HEAD["V"], HEAD["V"], -HEAD["W"], HEAD["W"]),
             box(NECK["U0"], HEAD["U0"] + 0.01, -NECK["V"], NECK["V"], -NECK["W"], NECK["W"]))
    cuts = []
    for v in PORT_V:
        cuts.append(cyl_x(PORT_D / 2, NECK["U0"] - 0.01, HEAD["U1"] + 0.01, v, PORT_W, fn=24))
        cuts.append(cyl_x(M5_TAP / 2, NECK["U0"] - 0.01, NECK["U0"] + 8.0, v, PORT_W, fn=24))
    cuts.append(box(NECK["U0"] - 0.01, HEAD["U1"] + 0.01, -SLOT["V"], SLOT["V"], SLOT["W0"], SLOT["W1"]))
    for s in (-1, 1):
        cuts.append(cyl_x(DOWEL["D_PRESS"] / 2, HEAD["U1"] - DOWEL["DEPTH"], HEAD["U1"] + 0.01, s * DOWEL["V"], DOWEL["W"], fn=24))
        cuts.append(cyl_x(THUMB["D"] / 2, HEAD["U0"] - 0.01, HEAD["U1"] + 0.01, s * THUMB["V"], THUMB["W"], fn=24))
        cuts.append(box(THUMB["NUT_U"] - THUMB["NUT_T"] / 2, THUMB["NUT_U"] + THUMB["NUT_T"] / 2,
                        s * THUMB["V"] - THUMB["NUT_AF"] / 2, s * THUMB["V"] + THUMB["NUT_AF"] / 2,
                        THUMB["W"] - THUMB["NUT_AF"] / 2 / math.cos(math.pi / 6), HEAD["W"] + 0.01))
        for sw in (-1, 1):
            cuts.append(cyl_x(M3_CLEAR / 2, HEAD["U0"] - 0.01, HEAD["U1"] + 0.01, s * CLAMP["V"], sw * CLAMP["W"], fn=24))
            cuts.append(cyl_x(CLAMP["CB_D"] / 2, HEAD["U1"] - CLAMP["CB_DEPTH"], HEAD["U1"] + 0.01, s * CLAMP["V"], sw * CLAMP["W"], fn=24))
        for (v0, v1, w0, w1) in B1_HEAD_POCKETS:
            cuts.append(box(HEAD["U0"] - 0.01, HEAD["U0"] + 8.0, min(s * v0, s * v1), max(s * v0, s * v1), w0, w1))
        for (v0, v1, w0, w1) in B1_NECK_POCKETS:
            cuts.append(box(NECK["U0"] - 0.01, NECK["U0"] + 10.0, min(s * v0, s * v1), max(s * v0, s * v1), w0, w1))
    return D(body, *cuts)

# ============================ DB07 umbilical plug (db07_plug.scad) ============================
def db07_plug():
    body = box(PLUG["U0"], PLUG["U1"], -HEAD["V"], HEAD["V"], -HEAD["W"], HEAD["W"])
    cuts = []
    for v in PORT_V:
        cuts.append(cyl_x(PORT_D / 2, PLUG["U0"] - 0.01, PLUG["U1"] + 0.01, v, PORT_W, fn=24))
        cuts.append(D(cyl_x(ORING["OD"] / 2, PLUG["U0"] - 0.01, PLUG["U0"] + ORING["DEPTH"], v, PORT_W, fn=32),
                      cyl_x(ORING["ID"] / 2, PLUG["U0"] - 0.02, PLUG["U0"] + ORING["DEPTH"] + 0.01, v, PORT_W, fn=32)))
        cuts.append(cyl_x(M5_TAP / 2, PLUG["U1"] - 8.0, PLUG["U1"] + 0.01, v, PORT_W, fn=24))
    cuts.append(box(PLUG["U0"] - 0.01, PLUG["U1"] + 0.01, -SLOT["V"], SLOT["V"], SLOT["W0"], SLOT["W1"]))
    for s in (-1, 1):
        cuts.append(cyl_x(DOWEL["D_SLIDE"] / 2, PLUG["U0"] - 0.01, PLUG["U0"] + DOWEL["DEPTH"], s * DOWEL["V"], DOWEL["W"], fn=24))
        cuts.append(cyl_x(THUMB["D"] / 2, PLUG["U0"] - 0.01, PLUG["U1"] + 0.01, s * THUMB["V"], THUMB["W"], fn=24))
        cuts.append(cyl_x(M3_TAP / 2, PLUG["U1"] - PCLIP["DEPTH"], PLUG["U1"] + 0.01, s * PCLIP["V"], PCLIP["W"], fn=24))
        for (v0, v1, w0, w1) in U1_POCKETS:
            cuts.append(box(PLUG["U1"] - 10.0, PLUG["U1"] + 0.01, min(s * v0, s * v1), max(s * v0, s * v1), w0, w1))
    v0, v1, w0, w1 = U1_POCKET_C
    cuts.append(box(PLUG["U1"] - 10.0, PLUG["U1"] + 0.01, v0, v1, w0, w1))
    return D(body, *cuts)

# ============================ DB08 inner clamp plate (db08_clamp.scad) ============================
def db08_clamp():
    u1 = -WALL_T
    body = box(u1 - CLAMP["T"], u1, -CLAMP["PLATE_V"], CLAMP["PLATE_V"], -CLAMP["PLATE_W"], CLAMP["PLATE_W"])
    cuts = [box(u1 - CLAMP["T"] - 0.01, u1 + 0.01, -NECK["V"] - 0.5, NECK["V"] + 0.5, -NECK["W"] - 0.5, NECK["W"] + 0.5)]
    for s in (-1, 1):
        for sw in (-1, 1):
            cuts.append(cyl_x(M3_CLEAR / 2, u1 - CLAMP["T"] - 0.01, u1 + 0.01, s * CLAMP["V"], sw * CLAMP["W"], fn=24))
    return D(body, *cuts)

# ============================ DB09 hook plate (db09_hook_plate.scad) ============================
def db09_hook_plate(p=HP):
    body = ext_z(cs_crrect(0, 0, p["X"], p["Y"], p["R"]), 0, p["T"])
    cuts = []
    for sx in (-1, 1):
        for sy in (-1, 1):
            cuts.append(cyl_z(M5_CLEAR / 2, -0.01, p["T"] + 0.01, sx * p["LID_X"], sy * p["LID_Y"], fn=24))
            cuts.append(cyl_z(p["CB_D"] / 2, p["T"] - p["CB_DEPTH"], p["T"] + 0.01, sx * p["LID_X"], sy * p["LID_Y"], fn=32))
        cuts.append(ext_z(cs_crrect(sx * p["SLOT_X"], 0, p["SLOT_W"], p["SLOT_L"], p["SLOT_W"] / 2 - 0.01), -0.01, p["T"] + 0.01))
        for hy in p["HOOK_Y"]:
            cuts.append(cyl_z(M5_CLEAR / 2, -0.01, p["T"] + 0.01, sx * p["HOOK_X"], hy, fn=24))
            cuts.append(hex_z(M5_NUT_AF, -0.01, M5_NUT_T, sx * p["HOOK_X"], hy))
    for (wx, wy) in p["WIN"]:
        cuts.append(ext_z(cs_crrect(wx, wy, p["WIN_X"], p["WIN_Y"], 5.0), -0.01, p["T"] + 0.01))
    return D(body, *cuts)

# ============================ DB10/DB11 J-hooks (db10_hook.scad) ============================
def db10_hook(throat, h=HOOK):
    t = h["T"]
    prof = cs_rect(0, t, 0, h["LEG_Q"]) + cs_rect(0, 2 * t + throat, h["BAR_Q0"], h["LEG_Q"]) \
        + cs_rect(t + throat, 2 * t + throat, h["DROP_Q0"], h["LEG_Q"]) \
        + cs_poly([(t - 0.01, h["BAR_Q0"] + 0.01), (t - 0.01, h["BAR_Q0"] - h["GUSSET"]), (t + h["GUSSET"], h["BAR_Q0"] + 0.01)])
    body = ext_z(prof, 0, h["WIDTH"])
    cuts = [cyl_x(M5_CLEAR / 2, -0.01, t + 0.01, q, h["WIDTH"] / 2, fn=24) for q in h["HOLE_Q"]]
    return D(body, *cuts)

# ============================ DB12 pegboard valve rack (db12_pegboard.scad) ============================
def db12_pegboard(p=PEG):
    hx = p["X"] / 2
    body = U(box(-hx, hx, 0, p["Y"], 0, p["T"]),
             box(-hx, hx, 0, p["FL_T"], 0, p["FL_Z"]),
             *[ext_x(cs_poly([(p["FL_T"] - 0.01, p["T"] - 0.01), (20.0, p["T"] - 0.01), (p["FL_T"] - 0.01, 20.0)]), gx - 1.5, gx + 1.5)
               for gx in (-hx + 1.5, hx - 1.5)])
    cuts = []
    nx = int(round((p["X"] - 20) / p["PITCH"]))
    for i in range(nx + 1):
        for j in range(8):
            cuts.append(cyl_z(p["HOLE_D"] / 2, -0.01, p["T"] + 0.01, -hx + 10 + i * p["PITCH"], 15 + j * p["PITCH"], fn=16))
    for fx in p["FL_HOLES"]:
        cuts.append(cyl_y(M4_CLEAR / 2, -0.01, p["FL_T"] + 0.01, fx, 12.0, fn=24))
    return D(body, *cuts)

# ============================ DB13/DB14 saddles (db13_saddle.scad) ============================
def db13_saddle(dia):
    w = dia + 8.0
    h = 4.0 + 0.35 * dia
    L = SADDLE_L
    body = U(box(-w / 2, w / 2, 0, L, 0, h), box(-8, 8, -9, L + 9, 0, 4))
    cuts = [cyl_y(dia / 2 + 0.5, -0.01, L + 0.01, 0.0, 4.0 + dia / 2, fn=96),
            box(-w / 2 - 0.01, w / 2 + 0.01, L / 2 - 2.5, L / 2 + 2.5, 1.0, 3.0),
            cyl_z(M4_CLEAR / 2, -0.01, 4.01, 0.0, -4.5, fn=24),
            cyl_z(M4_CLEAR / 2, -0.01, 4.01, 0.0, L + 4.5, fn=24)]
    return D(body, *cuts)

# ============================ DB15 hanger clip seat (db15_seat.scad) ============================
def db15_seat(s=SEAT15):
    body = cyl_z(s["R"], 0, s["H"], fn=64)
    cuts = [hex_z(NUT_1420_AF, -0.01, NUT_1420_T),
            cyl_z(s["BOLT_R"], -0.01, s["BOLT_Z"], fn=32),
            cyl_z(s["MAG_R"], s["MAG_Z0"], s["CONE_Z0"] + 0.01, fn=32),
            cyl_z(s["CONE_R0"], s["CONE_Z0"], s["H"] + 0.01, r2=s["CONE_R1"] + 0.01 * (s["CONE_R1"] - s["CONE_R0"]) / 3.0, fn=64)]
    return D(body, *cuts)

# ============================ DB16 clip halves (db16_clip.scad) ============================
def db16_clip(nose=True, c=CLIP):
    body = box(-c["X"], c["X"], -c["Y"], c["Y"], 0, c["H"])
    if nose:
        body = U(body, cyl_z(c["NOSE_R1"], -c["NOSE_H"], 0.01, r2=c["NOSE_R0"], fn=64))
    cuts = [cyl_x(c["CH_R"], -c["X"] - 0.01, c["X"] + 0.01, 0.0, c["H"], fn=64)]
    for sx in (-1, 1):
        for sy in (-1, 1):
            cuts.append(cyl_z(M3_CLEAR / 2, -0.01, c["H"] + 0.01, sx * c["HOLE_X"], sy * c["HOLE_Y"], fn=24))
            if not nose:
                cuts.append(hex_z(M3_NUT_AF, -0.01, M3_NUT_T, sx * c["HOLE_X"], sy * c["HOLE_Y"]))
    if nose:
        cuts.append(cyl_z(c["WASHER_R"], -c["NOSE_H"] - 0.01, -c["NOSE_H"] + c["WASHER_DEPTH"], fn=64))
    return D(body, *cuts)

# ============================ DB17 vent baffle (db17_vent_baffle.scad) ============================
def db17_vent_baffle():
    body = U(box(-25, 25, -25, 25, 0, 18), box(-31, 31, -4, 4, 0, 3))
    cuts = [box(-23, 23, -23, 23, -0.01, 16), box(-15, 15, 22.99, 25.01, 4, 12),
            cyl_z(M3_CLEAR / 2, -0.01, 3.01, -28, 0, fn=24), cyl_z(M3_CLEAR / 2, -0.01, 3.01, 28, 0, fn=24)]
    return D(body, *cuts)

# ============================ DB18 panel bracket (db18_bracket.scad) ============================
def db18_bracket():
    g = cs_poly([(3.99, 3.99), (20.0, 3.99), (3.99, 20.0)])
    body = U(box(0, 30, 0, 20, 0, 4), box(0, 4, 0, 20, 0, 30), ext_y(g, 0, 3), ext_y(g, 17, 20))
    cuts = [cyl_z(M4_CLEAR / 2, -0.01, 4.01, 18, 10, fn=24), cyl_x(M4_CLEAR / 2, -0.01, 4.01, 10, 18, fn=24)]
    return D(body, *cuts)

# ============================ parts table ============================
PARTS = [
    ("DB01_drum", db01_drum, "SLA"),
    ("DB02_deck", db02_deck, "PETG"),
    ("DB03_floating_plate", lambda: db03_floating_plate(SEAT), "PETG"),
    ("DB03b_floating_plate_4mm_housing", lambda: db03_floating_plate(SEAT_4MM), "PETG"),
    ("DB04_hall_bridge", db04_hall_bridge, "PETG"),
    ("DB05_comb", lambda: db05_comb(HOUS_OD), "PETG"),
    ("DB05b_comb_4mm_housing", lambda: db05_comb(4.3), "PETG"),
    ("DB06_bulkhead", db06_bulkhead, "SLA"),
    ("DB07_plug", db07_plug, "SLA"),
    ("DB08_inner_clamp", db08_clamp, "PETG"),
    ("DB09_hook_plate", db09_hook_plate, "PETG"),
    ("DB10_hook_30", lambda: db10_hook(30.0), "PETG"),
    ("DB11_hook_55", lambda: db10_hook(55.0), "PETG"),
    ("DB12_pegboard", db12_pegboard, "PETG"),
    ("DB13_saddle_pump_D28", lambda: db13_saddle(28.0), "PETG"),
    ("DB14_saddle_bottle_D51", lambda: db13_saddle(51.0), "PETG"),
    ("DB15_hanger_seat", db15_seat, "PETG"),
    ("DB16a_clip_nose", lambda: db16_clip(True), "PETG"),
    ("DB16b_clip_plain", lambda: db16_clip(False), "PETG"),
    ("DB17_vent_baffle", db17_vent_baffle, "PETG"),
    ("DB18_panel_bracket", db18_bracket, "PETG"),
]

def main():
    only = None
    if "--only" in sys.argv:
        only = set(sys.argv[sys.argv.index("--only") + 1].split(","))
    rows, ok_all = [], True
    for name, fn, mat in PARTS:
        if only and name.split("_")[0] not in only and name not in only:
            continue
        m = fn()
        tm = to_trimesh(m)
        ncomp = len(m.decompose())
        wt = bool(tm.is_watertight and tm.is_volume and ncomp == 1 and m.status() == m3.Error.NoError)
        ok_all &= wt
        tm.export(os.path.join(OUT, name + ".stl"))
        lo, hi = tm.bounds
        vol = m.volume() / 1000.0
        rows.append((name, mat, hi - lo, lo, vol, vol * DENS[mat], wt))
    print(f"{'part':36s} {'mat':5s} {'size x*y*z mm':>24s} {'min corner':>24s} {'cm3':>7s} {'g@100%':>7s} wt")
    for name, mat, size, lo, vol, g, wt in rows:
        print(f"{name:36s} {mat:5s} {size[0]:7.1f}x{size[1]:7.1f}x{size[2]:7.1f} {lo[0]:7.1f},{lo[1]:7.1f},{lo[2]:7.1f} {vol:7.2f} {g:7.1f} {'OK' if wt else 'FAIL'}")
    print(f"\n{sum(1 for r in rows if r[6])}/{len(rows)} watertight single-shell")
    sys.exit(0 if ok_all else 1)

if __name__ == "__main__":
    main()
