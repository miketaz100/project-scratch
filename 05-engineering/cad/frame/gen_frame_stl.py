#!/usr/bin/env python
"""
gen_frame_stl.py - STL generator for the SP1 module frame, float and hand parts
(PROJECT SCRATCH, 05-engineering/cad/frame, CAD agent, 2026-10-01, rev 2)

Generates into ./stl/ one STL per printed part P1-P48 of mechanical.md section 11
(the paddles, paddle clamp bars and seam sleeves are the tip lead's, in ../tips/).

THE .scad FILES ARE THE SOURCE OF TRUTH.  Every dimension below is copied from
lib_sp1.scad and the pNN_*.scad files and must be kept in sync; constant names match
the SCAD names.  No OpenSCAD binary exists on the build machine, so this script
rebuilds the same solids with manifold3d (CrossSection / Manifold booleans, hulls,
extrusions) and exports through trimesh.  README.md lists the few cosmetic features
(edge rounds, knurls, ribs) that the SCAD carries and this mirror leaves out; every
mating feature (holes, pockets, bores, slots, stops) is identical in both.

FRAME: the global assembly frame of mechanical.md section 2 (DESIGN-FREEZE-ADDENDUM-1
D9): Z up, X = stroke, Y = across; origin O = centre nail edge, arm at 0 deg, float on
its down-stop, module latched.  Every part that lives on the module is written IN ITS
INSTALLED POSITION so the STLs load together as the assembly; rotate in the slicer per
README.md.  Desk-side / loose parts (P2, P25, P29, P34-P48) use a LOCAL frame (README).

After the STLs the script runs the cheap checks the brief asks for (section 2 swept
volumes, the section 8.7 paddle-to-slot gaps, the pocket / pattern / cone fits) and
prints a table: name, bounding box, volume, watertight, and whether the bounding box
matches mechanical.md section 11 within 1 mm.  Mismatches are explained in CONFLICTS.md.

Run (from this folder):  <cadenv>/bin/python gen_frame_stl.py [--no-checks] [--only P30,P32]
Exit code 0 only if every mesh is watertight.
"""
import math, os, sys
import numpy as np
import trimesh
import manifold3d as m3
from manifold3d import Manifold, CrossSection

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "stl")
TIPS_STL = os.path.join(HERE, "..", "tips", "stl")
os.makedirs(OUT, exist_ok=True)
FN = 48                      # circle segments ($fn in the SCAD)

# =====================================================================
# lib_sp1.scad constants (shared)
# =====================================================================
# --- fasteners / inserts (mechanical.md section 11 header) ---
M2_CLEAR, M3_CLEAR, M4_CLEAR, M5_CLEAR = 2.4, 3.4, 4.5, 5.5
M2_PILOT, M3_PILOT = 1.8, 2.6           # thread-forming pilots in PETG
M2_INS_D, M2_INS_L = 3.2, 3.0           # brass heat-set M2: 3.2 hole, 3 long
M3_INS_D, M3_INS_L = 4.0, 4.0           # brass heat-set M3: 4.0 hole, 4 long
M4_INS_D, M4_INS_L = 5.6, 6.0           # brass heat-set M4 x 6 [VERIFY hole on the insert kit]
M3_HEAD_D, M3_HEAD_H = 6.0, 3.2         # socket head M3 (counterbores)
M5_HEAD_D, M5_HEAD_H = 9.5, 5.0
M4_NUT_AF, M4_NUT_H = 7.2, 3.4          # M4 nut trap (7.0 AF + 0.2)
PIN_BORE = 6.3                          # M6 hinge pin, reamed
EXT, EXT_SOCK = 20.0, 20.2              # 2020 extrusion and its printed socket
# --- global geometry (mechanical.md section 2) ---
AXIS_X, AXIS_Z = 0.0, 84.0              # elbow axis, parallel to Y
PIN_X, PIN_Z = -60.0, 84.0              # fail-safe hinge pin, parallel to Y
SCALP_C, SCALP_R = (0.0, 0.0, -86.0), 90.0
KP_C_Z = -52.5                          # knuckle-plate sphere centre z (underside R 90 at z 37.5)
KP_R, KP_T = 90.0, 1.6
BOOT_T, P31_T = 0.25, 1.2
TRAY_BOT_R = KP_R + KP_T + BOOT_T + P31_T   # 93.05: tray underside (sits on P31 over the boot)
# --- bought-part reference solids (positions) ---
POST = (-70, -50, -10, 10, 94, 198)     # 2020, 104 mm (ADDENDUM-1 D8)
SPINE = (-50, 30, -10, 10, 196, 216)    # 2020, 80 mm
BEAM = (-35, -15, -135, 135, 164, 184)  # 2020, 270 mm elbow-carrier beam
YAW_X = -25.0
XL330_BODY = (20.0, 23.0, 34.0)         # X x Y(depth) x Z (ROBOTIS X330 drawing, bom-verified.md section 11: confirmed)
XL330_AXIS_FROM_END = 9.5               # output axis 9.5 mm from the lower body end (bom-verified.md section 11 item 2)
SERVO = (-10, 10, -127, -104, 84 - 9.5, 84 - 9.5 + 34)   # XL330 body in place: Z 74.5..108.5
HORN_R, HORN_Y = 8.0, (-104, -101)      # XL330 horn diam 16 x 3 (bom-verified.md section 11 item 3)
XL330_FRAME_HOLES = ((-8.0, -15.0), (8.0, -15.0), (-8.0, 15.0), (8.0, 15.0))   # 4 x diam 1.6 on 16 x 30 (X, dZ from the body centre), back face 4.5 deep, horn face 3.5 deep
XL330_CONN = (13.0, 24.0)               # JST connectors on both 23 x 34 side faces, 13..24 mm behind the horn face, ~1 mm proud
MGN9_RAIL = dict(W=9.0, H=6.5, L=100.0, PITCH=20.0, END=10.0)   # [VERIFY]
MGN9C = dict(W=20.0, L=29.0, H=10.0, HOLE_X=15.0, HOLE_Y=10.0)  # block over the rail base [VERIFY]
RAIL = (33.5, 40, -4.5, 4.5, 68, 168)   # MGN9 rail 100 mm on the mast's -X face
CARR = (30, 40, -10, 10, 74, 103)       # MGN9C block at the down-stop (bounding box; the block straddles the rail)
MAG = dict(x0=-81.0, x1=-66.0, z=34.0, r=10.0)   # Adafruit 3872 P20/15
FLOAT_TRAVEL = 28.0
MATS = {"PETG": 1.27, "TPU": 1.21}      # g/cm3
# --- paddle section at the knuckle plate (tip lead, paddle_with_pocket.scad, z = 25) ---
PAD_SEC_X, PAD_SEC_Y = 22.82, 17.82
NAILS = {"L": (-8.0, -24.0), "C": (0.0, 0.0), "R": (8.0, 24.0)}   # section 8.1 (X, Y)
POCKET_MOUTH_Z = {"L": 8.9, "C": 12.5, "R": 8.9}                  # section 2 row 20

# =====================================================================
# helpers
# =====================================================================
def U(*ms):
    ms = [m for m in ms if m is not None]
    return Manifold.batch_boolean(ms, m3.OpType.Add) if len(ms) > 1 else ms[0]

def D(m, *cuts):
    cuts = [c for c in cuts if c is not None]
    if not cuts:
        return m
    return m - (Manifold.batch_boolean(cuts, m3.OpType.Add) if len(cuts) > 1 else cuts[0])

def box(x0, x1, y0, y1, z0, z1):
    return Manifold.cube([x1 - x0, y1 - y0, z1 - z0]).translate([x0, y0, z0])

def bx(t):
    return box(*t)

def cbox(cx, cy, cz, sx, sy, sz):
    return box(cx - sx / 2, cx + sx / 2, cy - sy / 2, cy + sy / 2, cz - sz / 2, cz + sz / 2)

def cyl_z(r, z0, z1, x=0.0, y=0.0, r2=None, fn=FN):
    return Manifold.cylinder(z1 - z0, r, r if r2 is None else r2, fn).translate([x, y, z0])

def cyl_y(r, y0, y1, x=0.0, z=0.0, fn=FN, r2=None):
    return cyl_z(r, 0, y1 - y0, fn=fn, r2=r2).transform(MAP_Y).translate([x, y0, z])

def cyl_x(r, x0, x1, y=0.0, z=0.0, fn=FN, r2=None):
    return cyl_z(r, 0, x1 - x0, fn=fn, r2=r2).transform(MAP_X).translate([x0, y, z])

def sphere(r, c, fn=FN):
    return Manifold.sphere(r, fn).translate(list(c))

# (u, v, w) of an extruded CrossSection -> global axes
MAP_Y = [[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0]]   # profile in (x, z), extruded along +Y
MAP_X = [[0, 0, 1, 0], [1, 0, 0, 0], [0, 1, 0, 0]]   # profile in (y, z), extruded along +X

def cs_poly(pts):
    """simple polygon; winding is forced CCW (manifold drops CW outlines as empty)"""
    P = [(float(a), float(b)) for a, b in pts]
    area = sum(P[i][0] * P[(i + 1) % len(P)][1] - P[(i + 1) % len(P)][0] * P[i][1] for i in range(len(P)))
    if area < 0:
        P.reverse()
    return CrossSection([P])

def cs_rect(u0, u1, v0, v1):
    return cs_poly([(u0, v0), (u1, v0), (u1, v1), (u0, v1)])

def cs_rrect(u0, u1, v0, v1, r):
    """rounded rectangle (offset of a shrunken rectangle)"""
    if r <= 0:
        return cs_rect(u0, u1, v0, v1)
    return cs_rect(u0 + r, u1 - r, v0 + r, v1 - r).offset(r, m3.JoinType.Round, 2.0, FN)

def cs_crrect(cu, cv, su, sv, r):
    return cs_rrect(cu - su / 2, cu + su / 2, cv - sv / 2, cv + sv / 2, r)

def cs_circle(r, u=0.0, v=0.0, fn=FN):
    return CrossSection.circle(r, fn).translate([u, v])

def ext_z(cs, z0, z1):
    return cs.extrude(z1 - z0).translate([0, 0, z0])

def ext_y(cs_xz, y0, y1):
    return cs_xz.extrude(y1 - y0).transform(MAP_Y).translate([0, y0, 0])

def ext_x(cs_yz, x0, x1):
    return cs_yz.extrude(x1 - x0).transform(MAP_X).translate([x0, 0, 0])

def rbox_z(x0, x1, y0, y1, z0, z1, r):
    """box with vertical edges rounded r"""
    return ext_z(cs_rrect(x0, x1, y0, y1, r), z0, z1)

def slab_z(cx, cy, sx, sy, r, z, h=0.02):
    """thin rounded-rect slab at height z (hull() targets, = lib_sp1 slab())"""
    return ext_z(cs_crrect(cx, cy, sx, sy, r), z - h / 2, z + h / 2)

def hull(*ms):
    return Manifold.batch_hull(list(ms))

def rot_about(m, axis, angle_deg, point):
    """rotate manifold m about an axis ('x'|'y'|'z' or a 3-vector) through point"""
    a = math.radians(angle_deg)
    k = np.array({"x": (1, 0, 0), "y": (0, 1, 0), "z": (0, 0, 1)}[axis] if isinstance(axis, str) else axis, float)
    k /= np.linalg.norm(k)
    K = np.array([[0, -k[2], k[1]], [k[2], 0, -k[0]], [-k[1], k[0], 0]])
    R = np.eye(3) + math.sin(a) * K + (1 - math.cos(a)) * K @ K
    p = np.array(point, float)
    t = p - R @ p
    return m.transform(np.column_stack([R, t]).tolist())

def mirror_y(m):
    return m.mirror([0, 1, 0])

def ins_z(d, depth, x, y, ztop, down=True):
    """blind insert/pilot hole: from face z=ztop going down (or up when down=False)"""
    return cyl_z(d / 2, ztop - depth, ztop + 0.01, x, y, fn=24) if down else cyl_z(d / 2, ztop - 0.01, ztop + depth, x, y, fn=24)

def ins_y(d, depth, x, z, yface, toward=+1):
    return cyl_y(d / 2, yface - 0.01, yface + depth, x, z, fn=24) if toward > 0 else cyl_y(d / 2, yface - depth, yface + 0.01, x, z, fn=24)

def ins_x(d, depth, y, z, xface, toward=+1):
    return cyl_x(d / 2, xface - 0.01, xface + depth, y, z, fn=24) if toward > 0 else cyl_x(d / 2, xface - depth, xface + 0.01, y, z, fn=24)

def sph_shell(rc_z, r_in, r_out, fn=160):
    return sphere(r_out, (0, 0, rc_z), fn) - sphere(r_in, (0, 0, rc_z), fn)

def csk_z(d_hole, d_head, x, y, ztop, down=True, thru=30.0):
    """countersunk through hole from face ztop (90 deg countersink)"""
    h = (d_head - d_hole) / 2
    if down:
        return U(cyl_z(d_hole / 2, ztop - thru, ztop + 1, x, y, fn=24),
                 cyl_z(d_hole / 2, ztop - h, ztop + 0.01, x, y, r2=d_head / 2, fn=24))
    return U(cyl_z(d_hole / 2, ztop - 1, ztop + thru, x, y, fn=24),
             cyl_z(d_head / 2, ztop - 0.01, ztop + h, x, y, r2=d_hole / 2, fn=24))

def to_trimesh(m):
    mm = m.to_mesh()
    # manifold output is already a clean 2-manifold; trimesh's vertex merging (process=True) can break thin features
    return trimesh.Trimesh(vertices=np.asarray(mm.vert_properties)[:, :3], faces=np.asarray(mm.tri_verts), process=False)

def from_stl(path):
    t = trimesh.load(path, force="mesh")
    return Manifold(m3.Mesh(np.asarray(t.vertices, np.float32), np.asarray(t.faces, np.uint32)))

def rrect_frustum(cx, cy, sx0, sy0, sx1, sy1, r, z0, z1):
    """hull of two rounded-rect slabs (drafted box)"""
    return hull(slab_z(cx, cy, sx0, sy0, r, z0 + 0.01), slab_z(cx, cy, sx1, sy1, r, z1 - 0.01))

# =====================================================================
# lib_sp1: shared features
# =====================================================================
def socket_2020_z(cx, cy, z0, z1):
    """pocket for a 2020 extrusion end along Z"""
    s = EXT_SOCK / 2
    return box(cx - s, cx + s, cy - s, cy + s, z0, z1)

def socket_2020_y(cx, cz, y0, y1):
    s = EXT_SOCK / 2
    return box(cx - s, cx + s, y0, y1, cz - s, cz + s)

def mgn9c_holes_x(xface, toward, yc, zc, d=M3_CLEAR, depth=30.0):
    """MGN9C 15 x 10 pattern [VERIFY], holes along X through a plate on the block face"""
    out = []
    for dz in (-MGN9C["HOLE_X"] / 2, MGN9C["HOLE_X"] / 2):
        for dy in (-MGN9C["HOLE_Y"] / 2, MGN9C["HOLE_Y"] / 2):
            out.append(cyl_x(d / 2, xface - depth, xface + depth, yc + dy, zc + dz, fn=24))
    return out

def xl330_pocket(x0, y_floor, z0, open_len=40.0):
    """XL330 body pocket 20.4 x 34.4 x 23.5 [VERIFY]: X across, Z = long body axis, open toward +Y"""
    px, pz, pd = XL330_BODY[0] + 0.4, XL330_BODY[2] + 0.4, XL330_BODY[1] + 0.5
    return box(x0 - px / 2, x0 + px / 2, y_floor, y_floor + pd + open_len, z0, z0 + pz)

# =====================================================================
# p01_vesa_adapter.scad  (P1)
# =====================================================================
P1 = dict(PLATE_X0=-126.0, PLATE_X1=-120.0, PLATE_Y=140.0, PLATE_Z0=25.0, PLATE_Z1=170.0,
          VESA=75.0, VESA_ZC=110.0, VESA_D=4.5, VESA_CB_D=8.0, VESA_CB_H=3.0,
          EAR_Y0=25.0, EAR_Y1=35.0, EAR_H=28.0, EAR_END_R=14.0, RIB_T=4.0,
          MAGARM_X1=-79.0, MAGARM_Y=15.0, MAGARM_Z0=20.0, MAGARM_Z1=48.0, MAGARM_WALL=3.0, MAGARM_FRONT_T=10.0,
          MAG_CB_D=20.4, MAG_CB_H=2.0,
          UPSTOP_X1=-98.0, UPSTOP_Y=10.0, UPSTOP_Z0=92.0, UPSTOP_Z1=108.0, UPSTOP_ZC=100.0,
          PULLEY_Y=60.0, PULLEY_X=-123.0, PULLEY_ZC=141.5, PULLEY_WIN_Y=7.0, PULLEY_WIN_Z=20.0,
          PBOSS_X0=-131.0, PBOSS_X1=-115.0, PBOSS_Y0=54.0, PBOSS_Y1=66.0, PBOSS_Z0=129.0, PBOSS_Z1=154.0,
          AXLE_D=3.2, CHAN_X0=-137.0, CHAN_W0=52.5, CHAN_W1=67.5, CHAN_WALL=2.0, CHAN_Z0=26.0,
          HOOK_Z=30.0, HOOK_D=5.0, HOOK_HEAD_D=8.0, HOOK_L=9.0,
          TRAY_HOLES=((21.0, 105.5), (49.0, 105.5), (21.0, 160.0), (49.0, 160.0)),
          EDGE_RIB_Y=66.0, GUIDE_HOLES=((-91.0, 6.0), (-84.0, 6.0)))

def p01_vesa_adapter(p=P1):
    x0, x1 = p["PLATE_X0"], p["PLATE_X1"]
    hy = p["PLATE_Y"] / 2
    parts = [box(x0, x1, -hy, hy, p["PLATE_Z0"], p["PLATE_Z1"])]
    # edge ribs on the front face (Y +/-66..70), full height
    for s in (-1, 1):
        y0, y1 = sorted((s * p["EDGE_RIB_Y"], s * hy))
        parts.append(box(x1 - 0.01, x1 + 8, y0, y1, p["PLATE_Z0"], p["PLATE_Z1"]))
    # hinge ears: hull of a block from the plate and a round end about the pin, + gusset
    for s in (-1, 1):
        y0, y1 = sorted((s * p["EAR_Y0"], s * p["EAR_Y1"]))
        prof = CrossSection.batch_hull([cs_rect(x1 - 0.01, PIN_X, PIN_Z - p["EAR_H"] / 2, PIN_Z + p["EAR_H"] / 2),
                                        cs_circle(p["EAR_END_R"], PIN_X, PIN_Z)])
        gus = cs_poly([(x1 - 0.01, 40.0), (x1 - 0.01, PIN_Z - 13), (-85.0, PIN_Z - 13)])
        parts.append(ext_y(prof + gus, y0, y1))
    # magnet arm: open-top channel (two side webs, bottom web, front plate)
    ma = p["MAGARM_Y"]
    parts.append(box(x1 - 0.01, p["MAGARM_X1"], -ma, ma, p["MAGARM_Z0"], p["MAGARM_Z0"] + p["MAGARM_WALL"]))
    for s in (-1, 1):
        y0, y1 = sorted((s * (ma - p["MAGARM_WALL"]), s * ma))
        parts.append(box(x1 - 0.01, p["MAGARM_X1"], y0, y1, p["MAGARM_Z0"], p["MAGARM_Z1"]))
    parts.append(box(p["MAGARM_X1"] - p["MAGARM_FRONT_T"], p["MAGARM_X1"], -ma, ma, p["MAGARM_Z0"], p["MAGARM_Z1"]))
    # up-stop boss between the ears
    parts.append(box(x1 - 0.01, p["UPSTOP_X1"], -p["UPSTOP_Y"], p["UPSTOP_Y"], p["UPSTOP_Z0"], p["UPSTOP_Z1"]))
    # pulley cheeks (bosses) and rear spring channels
    for s in (-1, 1):
        y0, y1 = sorted((s * p["PBOSS_Y0"], s * p["PBOSS_Y1"]))
        parts.append(box(p["PBOSS_X0"], p["PBOSS_X1"], y0, y1, p["PBOSS_Z0"], p["PBOSS_Z1"]))
        for w in (p["CHAN_W0"], p["CHAN_W1"] - p["CHAN_WALL"]):
            ya, yb = sorted((s * w, s * (w + p["CHAN_WALL"])))
            parts.append(box(p["CHAN_X0"], x0 + 0.01, ya, yb, p["CHAN_Z0"], p["PBOSS_Z0"] + 0.01))
        # spring-anchor hook: pin + head on the rear face
        parts.append(cyl_x(p["HOOK_D"] / 2, x0 - p["HOOK_L"], x0 + 0.01, s * p["PULLEY_Y"], p["HOOK_Z"]))
        parts.append(cyl_x(p["HOOK_HEAD_D"] / 2, x0 - p["HOOK_L"] - 1.5, x0 - p["HOOK_L"] + 0.01, s * p["PULLEY_Y"], p["HOOK_Z"]))
    m = U(*parts)
    cuts = []
    # VESA 75 holes, counterbored from the front (+X) face
    for yy in (-p["VESA"] / 2, p["VESA"] / 2):
        for zz in (p["VESA_ZC"] - p["VESA"] / 2, p["VESA_ZC"] + p["VESA"] / 2):
            cuts.append(cyl_x(p["VESA_D"] / 2, x0 - 1, x1 + 1, yy, zz, fn=24))
            cuts.append(cyl_x(p["VESA_CB_D"] / 2, x1 - p["VESA_CB_H"], x1 + 1, yy, zz, fn=24))
    # hinge pin bores
    cuts.append(cyl_y(PIN_BORE / 2, -40, 40, PIN_X, PIN_Z, fn=32))
    # magnet seat: 20.4 x 2 locating counterbore + M3 rear-screw hole
    xm = p["MAGARM_X1"]
    cuts.append(cyl_x(p["MAG_CB_D"] / 2, xm - p["MAG_CB_H"], xm + 0.01, 0, MAG["z"]))
    cuts.append(cyl_x(M3_CLEAR / 2, xm - p["MAGARM_FRONT_T"] - 1, xm, 0, MAG["z"], fn=24))
    # up-stop M4 insert (axis X, from the boss front face)
    cuts.append(ins_x(M4_INS_D, M4_INS_L, 0, p["UPSTOP_ZC"], p["UPSTOP_X1"], toward=-1))
    # pulley windows through plate + cheeks, and axle holes along Y
    for s in (-1, 1):
        cuts.append(box(p["PBOSS_X0"] - 1, p["PBOSS_X1"] + 1, s * p["PULLEY_Y"] - p["PULLEY_WIN_Y"] / 2,
                        s * p["PULLEY_Y"] + p["PULLEY_WIN_Y"] / 2, p["PULLEY_ZC"] - p["PULLEY_WIN_Z"] / 2,
                        p["PULLEY_ZC"] + p["PULLEY_WIN_Z"] / 2))
        y0, y1 = sorted((s * (p["PBOSS_Y0"] - 1), s * (p["PBOSS_Y1"] + 1)))
        cuts.append(cyl_y(p["AXLE_D"] / 2, y0, y1, p["PULLEY_X"], p["PULLEY_ZC"], fn=24))
    # tray seat: 4 M3 inserts in the front face
    for yy, zz in p["TRAY_HOLES"]:
        cuts.append(ins_x(M3_INS_D, M3_INS_L, yy, zz, x1, toward=-1))
    # reset-cord guide P45: 2 M3 inserts in the magnet arm's bottom web (from below)
    for xs, yy in p["GUIDE_HOLES"]:
        cuts.append(ins_z(M3_INS_D, M3_INS_L, xs, yy, p["MAGARM_Z0"], down=False))
    return D(m, *cuts)

# =====================================================================
# p02_p05_p06_p07_hinge_parts.scad  (P2 pulley sheave, P5 knuckle, P6 keeper lever, P7 cord bar)
# =====================================================================
P2 = dict(OD=16.0, W=5.0, GROOVE_DEPTH=1.5, BORE=10.0, BRG_W=4.0, LIP_D=8.0)

def p02_pulley_sheave(p=P2):
    """LOCAL frame: axis along Z, z in [0, W]. V groove for the 1 mm cord, 10 mm bore for a 623ZZ, 1 mm lip"""
    ro, w, gd = p["OD"] / 2, p["W"], p["GROOVE_DEPTH"]
    prof = cs_poly([(p["LIP_D"] / 2, 0), (ro, 0), (ro, w / 2 - gd), (ro - gd, w / 2), (ro, w / 2 + gd), (ro, w),
                    (p["BORE"] / 2, w), (p["BORE"] / 2, w - p["BRG_W"]), (p["LIP_D"] / 2, w - p["BRG_W"])])
    return prof.revolve(FN)

P5 = dict(X=24.0, Y=48.0, Z0=76.0, Z1=106.0, SOCK_D=12.0, SCREW_Z=101.0, SCREW_CB_D=9.5, SCREW_CB_DEPTH=6.0)

def p05_hinge_knuckle(p=P5):
    hx, hy = p["X"] / 2, p["Y"] / 2
    m = box(PIN_X - hx, PIN_X + hx, -hy, hy, p["Z0"], p["Z1"])
    cuts = [socket_2020_z(PIN_X, 0, p["Z1"] - p["SOCK_D"], p["Z1"] + 1),
            cyl_y(PIN_BORE / 2, -hy - 1, hy + 1, PIN_X, PIN_Z, fn=32),
            cyl_y(M5_CLEAR / 2, -hy - 1, hy + 1, PIN_X, p["SCREW_Z"], fn=24)]
    for sgn in (-1, 1):
        y0, y1 = sorted((sgn * hy, sgn * (hy - p["SCREW_CB_DEPTH"])))
        cuts.append(cyl_y(p["SCREW_CB_D"] / 2, y0 - (0.01 if sgn < 0 else 0), y1 + (0.01 if sgn > 0 else 0), PIN_X, p["SCREW_Z"], fn=32))
    return D(m, *cuts)

P6 = dict(FOOT_X0=-66.0, FOOT_X1=-54.0, FOOT_Y=30.0, FOOT_Z0=19.0, FOOT_Z1=49.0, KEEPER=25.0, KEEPER_T=3.0,
          BRIDGE_Z1=57.0, UP_X0=-47.0, UP_X1=-39.0, UP_Y=20.0, UP_Z1=134.0, UP_STEP_Z=106.0,
          SCREW_ZS=(115.0, 127.0), EYE_D=2.5, EYE_Z=22.5, KEEPER_SCREW_Y=8.0)

def p06_keeper_lever(p=P6):
    fy, uy = p["FOOT_Y"] / 2, p["UP_Y"] / 2
    m = U(box(p["FOOT_X0"], p["FOOT_X1"], -fy, fy, p["FOOT_Z0"], p["FOOT_Z1"]),
          box(p["FOOT_X0"], p["UP_X1"], -uy, uy, p["FOOT_Z1"] - 0.01, p["BRIDGE_Z1"]),
          box(p["UP_X0"], p["UP_X1"], -uy, uy, p["FOOT_Z1"], p["UP_STEP_Z"] + 0.01),
          box(POST[1], p["UP_X1"], -uy, uy, p["UP_STEP_Z"], p["UP_Z1"]))
    k, zc = p["KEEPER"] / 2, MAG["z"]
    cuts = [box(p["FOOT_X0"] - 1, p["FOOT_X0"] + p["KEEPER_T"], -k, k, zc - k, zc + k),
            cyl_y(p["EYE_D"] / 2, -fy - 1, fy + 1, (p["FOOT_X0"] + p["FOOT_X1"]) / 2, p["EYE_Z"], fn=16)]
    for yy in (-p["KEEPER_SCREW_Y"], p["KEEPER_SCREW_Y"]):
        cuts.append(ins_x(M3_PILOT, 6.0, yy, zc, p["FOOT_X0"] + p["KEEPER_T"], toward=+1))
    for zz in p["SCREW_ZS"]:
        cuts.append(cyl_x(M5_CLEAR / 2, POST[1] - 1, p["UP_X1"] + 1, 0, zz, fn=24))
        cuts.append(cyl_x(M5_HEAD_D / 2, p["UP_X1"] - 3.0, p["UP_X1"] + 1, 0, zz, fn=32))
    return D(m, *cuts)

P7 = dict(Z0=142.0, Z1=154.0, BACK_X0=-76.0, CHEEK_Y0=10.1, CHEEK_Y1=14.0, ARM_X0=-50.0, ARM_X1=-38.0,
          ARM_Y1=70.0, CORD_Y=60.0, EYE_D=2.5, POST_D=4.0, POST_H=5.0, POST_Y=52.0)

def p07_cord_bar(p=P7):
    z0, z1 = p["Z0"], p["Z1"]
    parts = [box(p["BACK_X0"], POST[0] + 0.01, -p["CHEEK_Y1"], p["CHEEK_Y1"], z0, z1)]
    for s in (-1, 1):
        ya, yb = sorted((s * p["CHEEK_Y0"], s * p["CHEEK_Y1"]))
        parts.append(box(p["BACK_X0"], p["ARM_X1"], ya, yb, z0, z1))
        ya, yb = sorted((s * p["CHEEK_Y0"], s * p["ARM_Y1"]))
        parts.append(box(p["ARM_X0"], p["ARM_X1"], ya, yb, z0, z1))
        xc = (p["ARM_X0"] + p["ARM_X1"]) / 2
        parts.append(cyl_z(p["POST_D"] / 2, z1 - 0.01, z1 + p["POST_H"], xc, s * p["POST_Y"], fn=24))
    m = U(*parts)
    cuts = [cyl_y(M5_CLEAR / 2, -20, 20, PIN_X, (z0 + z1) / 2, fn=24)]       # one M5 from each side, T-nuts in the post slots
    for s in (-1, 1):
        cuts.append(cyl_z(p["EYE_D"] / 2, z0 - 1, z1 + 1, (p["ARM_X0"] + p["ARM_X1"]) / 2, s * p["CORD_Y"], fn=16))
    return D(m, *cuts)

# =====================================================================
# p08_p09_yaw_plates.scad  (P8 frame yaw plate, P9 carrier yaw plate)
# =====================================================================
P8 = dict(S=70.0, T=6.0, Z0=190.0, Z1=196.0, BC_D=56.6, N=8, SLOT_X=(-45.0, -5.0), SLOT_L=10.0, POST_NOTCH=True)
P9 = dict(S=70.0, T=6.0, Z0=184.0, Z1=190.0, SQ=40.0, SLOT_Y=(-20.0, 20.0), SLOT_L=10.0)

def post_notch(z0, z1):
    """2020 post passes through both yaw plates (section 2: post Z 94-198, plates Z 184-196 at X -60..10)"""
    s = EXT_SOCK / 2
    return box(POST[0] - 1, POST[1] + 0.1, -s, s, z0 - 1, z1 + 1)

def p08_frame_yaw_plate(p=P8):
    hs = p["S"] / 2
    m = rbox_z(YAW_X - hs, YAW_X + hs, -hs, hs, p["Z0"], p["Z1"], 4.0)
    cuts = [post_notch(p["Z0"], p["Z1"])]
    for i in range(p["N"]):
        a = math.radians(45.0 + 45.0 * i)      # 40 x 40 square corners (45, 135, ..) and the same square rotated 45
        hx, hy = YAW_X + p["BC_D"] / 2 * math.cos(a), p["BC_D"] / 2 * math.sin(a)
        if hx < POST[1] + M3_INS_D / 2 + 1.0 and abs(hy) < EXT_SOCK / 2 + M3_INS_D / 2 + 1.0:
            continue                            # the 180-deg hole at (-53.3, 0) lands in the post notch (CONFLICTS)
        cuts.append(ins_z(M3_INS_D, M3_INS_L, hx, hy, p["Z0"], down=False))
    for xs in p["SLOT_X"]:          # M5 slots along X to the spine's bottom slot
        cuts.append(hull(cyl_z(M5_CLEAR / 2, p["Z0"] - 1, p["Z1"] + 1, xs - p["SLOT_L"] / 2, 0, fn=24),
                         cyl_z(M5_CLEAR / 2, p["Z0"] - 1, p["Z1"] + 1, xs + p["SLOT_L"] / 2, 0, fn=24)))
    return D(m, *cuts)

def p09_carrier_yaw_plate(p=P9):
    hs = p["S"] / 2
    m = rbox_z(YAW_X - hs, YAW_X + hs, -hs, hs, p["Z0"], p["Z1"], 4.0)
    cuts = [post_notch(p["Z0"], p["Z1"])]
    for dx in (-p["SQ"] / 2, p["SQ"] / 2):
        for dy in (-p["SQ"] / 2, p["SQ"] / 2):
            cuts.append(cyl_z(M3_CLEAR / 2, p["Z0"] - 1, p["Z1"] + 1, YAW_X + dx, dy, fn=24))
    for ys in p["SLOT_Y"]:          # M5 slots along Y to the carrier beam's top slot
        cuts.append(hull(cyl_z(M5_CLEAR / 2, p["Z0"] - 1, p["Z1"] + 1, YAW_X, ys - p["SLOT_L"] / 2, fn=24),
                         cyl_z(M5_CLEAR / 2, p["Z0"] - 1, p["Z1"] + 1, YAW_X, ys + p["SLOT_L"] / 2, fn=24)))
    return D(m, *cuts)

# =====================================================================
# p10_reset_tab.scad  (P10, caps the spine's front end at X +30)
# =====================================================================
P10 = dict(X0=20.0, X1=45.0, Y=30.0, Z0=194.0, Z1=219.0, SOCK_DEPTH=10.0, R=5.0)

def p10_reset_tab(p=P10):
    hy = p["Y"] / 2
    body = ext_x(cs_rrect(-hy, hy, p["Z0"], p["Z1"], p["R"]), p["X0"], p["X1"])
    body = body ^ ext_z(cs_rrect(p["X0"] - p["R"], p["X1"], -hy, hy, p["R"]), p["Z0"] - 1, p["Z1"] + 1)
    s = EXT_SOCK / 2
    cut = box(p["X0"] - 1, p["X0"] + p["SOCK_DEPTH"], -s, s, 206 - s, 206 + s)
    return D(body, cut)

# =====================================================================
# p11_p12_drop_legs.scad  (P11 servo side -Y, P12 idler side +Y; P12 = mirror with its own foot holes)
# =====================================================================
P11 = dict(TOP_X0=-36.0, TOP_X1=-14.0, TOP_Y0=-139.0, TOP_Y1=-115.0, TOP_Z0=163.0, TOP_Z1=185.0, SOCK_L=20.0,
           END_SCREW_D=M5_CLEAR, TNUT_Y=(-125.0, -119.0),
           BAR_X0=-29.0, BAR_X1=-17.0, BAR_Y0=-136.5, BAR_Y1=-115.0, BAR_Z0=70.0,   # behind the 34-wide cradle (X -17)
           FL_X0=-35.0, FL_X1=19.0, FL_Y0=-136.5, FL_Y1=-131.5, FL_Z0=70.0, FL_Z1=116.0,
           FOOT_INS=((-14.0, 80.0), (14.0, 80.0), (-14.0, 104.0), (14.0, 104.0)),   # P13 (servo cradle); clear of the servo's 16 x 30 pattern
           FOOT_INS_IDLER=((0.0, 70.0), (0.0, 98.0)))                                 # P15 (idler housing)

def _drop_leg(p, holes):
    parts = [box(p["TOP_X0"], p["TOP_X1"], p["TOP_Y0"], p["TOP_Y1"], p["TOP_Z0"], p["TOP_Z1"]),
             box(p["BAR_X0"], p["BAR_X1"], p["BAR_Y0"], p["BAR_Y1"], p["BAR_Z0"], p["TOP_Z0"] + 0.01),
             box(p["FL_X0"], p["FL_X1"], p["FL_Y0"], p["FL_Y1"], p["FL_Z0"], p["FL_Z1"]),
             # web joining bar and flange (rib)
             box(p["BAR_X0"], p["BAR_X1"], p["FL_Y0"], p["FL_Y1"] + 0.01, p["FL_Z0"], p["TOP_Z0"])]
    m = U(*parts)
    beam_cx, beam_cz = (BEAM[0] + BEAM[1]) / 2, (BEAM[4] + BEAM[5]) / 2
    cuts = [socket_2020_y(beam_cx, beam_cz, p["TOP_Y1"] - p["SOCK_L"], p["TOP_Y1"] + 1),
            cyl_y(p["END_SCREW_D"] / 2, p["TOP_Y0"] - 1, p["TOP_Y1"], beam_cx, beam_cz, fn=24),
            cyl_y(M5_HEAD_D / 2, p["TOP_Y0"] - 1, p["TOP_Y0"] + M5_HEAD_H, beam_cx, beam_cz, fn=32)]
    for yy in p["TNUT_Y"]:          # T-nut screws through the top wall into the beam's top slot
        cuts.append(cyl_z(M5_CLEAR / 2, beam_cz, p["TOP_Z1"] + 1, beam_cx, yy, fn=24))
    for xx, zz in holes:            # inserts in the flange's +Y face (facing the cradle / housing)
        cuts.append(ins_y(M3_INS_D, M3_INS_L, xx, zz, p["FL_Y1"], toward=-1))
    return D(m, *cuts)

def p11_drop_leg_servo(p=P11):
    return _drop_leg(p, p["FOOT_INS"])

def p12_drop_leg_idler(p=P11):
    return mirror_y(_drop_leg(p, p["FOOT_INS_IDLER"]))

# =====================================================================
# p13_p14_servo_cradle.scad  (P13 cradle, P14 strap)
# =====================================================================
# rev 2 (Director, bom-verified.md section 11): no side holes on the XL330; the cradle mounts the servo through the
# four back-face holes (16 x 30, M2 x 6 tapping screws through the 2.5 back wall: 3.5 mm engagement in a 4.5 mm hole;
# M2 x 8 would bottom out), the strap P14 stays as the backup clamp, and both side walls have windows for the
# connectors (13..24 mm behind the horn face).  Cradle widened to X +/-17 so the four M3 leg screws clear the servo pattern.
# rev 3 (Director, crown mount): the cradle's back face (plane Y -131.5, X +/-17, Z 70..116) IS the crown's bolt interface,
# so the back wall is 4.0 thick and the four servo M2 x 6 heads sit in diam 4.4 x 1.8 counterbores, flush with that face
# (3.8 mm engagement in the 4.5 mm holes).  Crown-side holes: 4 x M3 at (X +/-14, Z 80) and (+/-14, 104).
P13 = dict(X0=-17.0, X1=17.0, Y0=-131.5, Y1=-102.0, Z0=70.0, Z1=116.0, BACK=4.0, SERVO_CB_D=4.4, SERVO_CB_H=1.8,
           POCKET_X=XL330_BODY[0] + 0.4, POCKET_Z=XL330_BODY[2] + 0.4, POCKET_D=XL330_BODY[1] + 0.5,
           BODY_Z0=SERVO[4] - 0.2, BODY_ZC=(SERVO[4] + SERVO[5]) / 2, CABLE_WIN=(14.0, 12.0),
           SERVO_SCREW_D=2.2, SERVO_HOLES=XL330_FRAME_HOLES, CONN_WIN_Z=(78.0, 105.0),
           # bumper lugs: the cheek lug (3 wide, r 12.5-20) must meet a 2 mm TPU pad on the lug's trailing face at 32 deg:
           # lug centre angle = 32 + 4.3 (half-angle of the cheek lug corner at r 20) + 7.2 (2 mm pad at r 16) + 7.2 (half lug width at r 16)
           LUG_R=16.0, LUG_ANG=50.7, LUG_SX=4.0, LUG_SZ=6.0, LUG_Y0=-103.0, LUG_Y1=-99.0, BUMPER_T=2.0,
           FLANGE_X1=23.0, FLANGE_Z0=70.0, FLANGE_Z1=98.0, ZERO_PIN=(20.0, 84.0), ZERO_PIN_D=3.1,
           STRAP_INS=((-8.0, 112.0), (8.0, 112.0)), MOUNT=P11["FOOT_INS"])

def p13_servo_cradle(p=P13):
    m = U(box(p["X0"], p["X1"], p["Y0"], p["Y1"], p["Z0"], p["Z1"]),
          box(p["X1"] - 0.01, p["FLANGE_X1"], p["Y0"], p["Y0"] + 6.0, p["FLANGE_Z0"], p["FLANGE_Z1"]))
    # TPU bumper lugs at +/-32 deg below the axis, on the +Y face
    for s in (-1, 1):
        a = math.radians(p["LUG_ANG"])
        cx, cz = AXIS_X + s * p["LUG_R"] * math.sin(a), AXIS_Z - p["LUG_R"] * math.cos(a)
        m = U(m, cbox(cx, (p["LUG_Y0"] + p["LUG_Y1"]) / 2, cz, p["LUG_SX"], p["LUG_Y1"] - p["LUG_Y0"], p["LUG_SZ"]))
    cuts = [xl330_pocket(0.0, p["Y0"] + p["BACK"], p["BODY_Z0"])]
    wx, wy = p["CABLE_WIN"]
    cuts.append(box(-wx / 2, wx / 2, p["Y0"] + p["BACK"] + 2.0, p["Y0"] + p["BACK"] + 2.0 + wy, p["Z0"] - 1, p["BODY_Z0"] + 1))
    for dx, dz in p["SERVO_HOLES"]:    # 4 x M2 x 6 through the back wall into the servo's back-face holes (16 x 30), heads counterbored flush
        cuts.append(cyl_y(p["SERVO_SCREW_D"] / 2, p["Y0"] - 1, p["Y0"] + p["BACK"] + 1, dx, p["BODY_ZC"] + dz, fn=16))
        cuts.append(cyl_y(p["SERVO_CB_D"] / 2, p["Y0"] - 1, p["Y0"] + p["SERVO_CB_H"], dx, p["BODY_ZC"] + dz, fn=24))
    cz0, cz1 = p["CONN_WIN_Z"]         # connector windows in both side walls, 13..24 mm behind the horn face (Y -104)
    cuts.append(box(p["X0"] - 1, p["X1"] + 1, HORN_Y[0] - XL330_CONN[1] - 0.5, HORN_Y[0] - XL330_CONN[0], cz0, cz1))
    cuts.append(cyl_y(p["ZERO_PIN_D"] / 2, p["Y0"] - 1, p["Y1"] + 1, p["ZERO_PIN"][0], p["ZERO_PIN"][1], fn=24))
    for xx, zz in p["STRAP_INS"]:      # strap screws into the top wall's +Y end
        cuts.append(ins_y(M3_INS_D, M3_INS_L, xx, zz, p["Y1"], toward=-1))
    for xx, zz in p["MOUNT"]:          # 4 x M3 clearance through the back wall into the leg flange
        cuts.append(cyl_y(M3_CLEAR / 2, p["Y0"] - 1, p["Y0"] + p["BACK"] + 1, xx, zz, fn=24))
    return D(m, *cuts)

P14 = dict(X=30.0, T=3.5, Z0=98.0, Z1=116.0, Y1=P13["Y1"] + 3.5, INTERF=0.3)   # Y -102..-98.5 (0.5 from cheek A)

def p14_servo_strap(p=P14):
    """strap across the open +Y face above the horn; its inner face presses the servo (0.3 interference)"""
    m = box(-p["X"] / 2, p["X"] / 2, p["Y1"] - p["T"], p["Y1"], p["Z0"], p["Z1"])
    # pad that reaches into the pocket by INTERF (servo front face at Y -104)
    ya, yb = sorted((HORN_Y[0] + p["INTERF"], p["Y1"] - p["T"] + 0.01))   # -103.7 .. -102.49
    m = U(m, box(-8, 8, ya, yb, p["Z0"], 108.0))
    cuts = [cyl_y(M3_CLEAR / 2, p["Y1"] - p["T"] - 1, p["Y1"] + 1, xx, zz, fn=24) for xx, zz in P13["STRAP_INS"]]
    return D(m, *cuts)

# =====================================================================
# p15_idler_housing.scad  (P15; 625-2RS bore, head relief, 2 oversize holes for +/-1.5 alignment)
# =====================================================================
P15 = dict(X=30.0, Y0=116.0, Y1=130.0, Z0=64.0, Z1=104.0, END_R=26.0, BRG_D=16.0, BRG_W=5.0, RELIEF_D=8.0,
           SLOT_D=M3_CLEAR + 3.0, SLOT_AT=P11["FOOT_INS_IDLER"])

def p15_idler_housing(p=P15):
    m = box(-p["X"] / 2, p["X"] / 2, p["Y0"], p["Y1"], p["Z0"], p["Z1"]) ^ cyl_y(p["END_R"], p["Y0"] - 1, p["Y1"] + 1, AXIS_X, AXIS_Z)   # corners rounded about the axis
    cuts = [cyl_y(p["BRG_D"] / 2, p["Y0"] - 1, p["Y0"] + p["BRG_W"], AXIS_X, AXIS_Z),
            cyl_y(p["RELIEF_D"] / 2, p["Y0"] - 1, p["Y1"] + 1, AXIS_X, AXIS_Z)]
    for xx, zz in p["SLOT_AT"]:
        cuts.append(cyl_y(p["SLOT_D"] / 2, p["Y0"] - 1, p["Y1"] + 1, xx, zz, fn=24))
        cuts.append(cyl_y(M3_HEAD_D / 2 + 1.5, p["Y0"] - 1, p["Y0"] + 4.0, xx, zz, fn=24))   # washer seat
    return D(m, *cuts)

# =====================================================================
# p16_horn_adapter_disc.scad  (P16, between the XL330 horn and cheek A)
# =====================================================================
P16 = dict(D=24.0, T=3.0, Y0=-101.0, Y1=-98.0, CENTRE_D=6.0, HORN_PCD=12.0, HORN_HOLE_D=2.2, CHEEK_PCD=18.0, CHEEK_ANG0=45.0)
# horn: diam 16 x 3, 4 x diam 1.6 on PCD 12 at 90 deg with one hole on the body's long axis (Z), M2 x 6 only (3 mm disc):
# bom-verified.md section 11 item 3.  The cheek's 4 x M3 on PCD 18 sit at 45 deg so they clear the horn screws by 3.6 mm.

def p16_horn_adapter_disc(p=P16):
    m = cyl_y(p["D"] / 2, p["Y0"], p["Y1"], AXIS_X, AXIS_Z)
    cuts = [cyl_y(p["CENTRE_D"] / 2, p["Y0"] - 1, p["Y1"] + 1, AXIS_X, AXIS_Z, fn=24)]
    for i in range(4):   # XL330 horn: 4 x M2 on PCD 12 at 0/90/180/270 (one on the body's long axis)
        a = math.radians(90 * i)
        cuts.append(cyl_y(p["HORN_HOLE_D"] / 2, p["Y0"] - 1, p["Y1"] + 1, AXIS_X + p["HORN_PCD"] / 2 * math.cos(a), AXIS_Z + p["HORN_PCD"] / 2 * math.sin(a), fn=16))
    for i in range(4):   # 4 x M3 on PCD 18 into cheek A, at 45 deg
        a = math.radians(p["CHEEK_ANG0"] + 90 * i)
        cuts.append(cyl_y(M3_CLEAR / 2, p["Y0"] - 1, p["Y1"] + 1, AXIS_X + p["CHEEK_PCD"] / 2 * math.cos(a), AXIS_Z + p["CHEEK_PCD"] / 2 * math.sin(a), fn=24))
    return D(m, *cuts)

# =====================================================================
# p17_p18_guard_caps.scad  (G2 servo cap, G3 idler cap: drafted tubs, 2 mm shell)
# =====================================================================
P17 = dict(TOP_X=60.0, TOP_Y=32.0, YC=-119.0, Z0=40.0, Z1=70.0, DRAFT=15.0, WALL=2.0, R=6.0,
           MOUNT_Z=66.0, MOUNT_X=(-25.0, 25.0))

def _guard_cap(p):
    h = p["Z1"] - p["Z0"]
    d = 2 * h * math.tan(math.radians(p["DRAFT"]))
    outer = rrect_frustum(0.0, p["YC"], p["TOP_X"] - d, p["TOP_Y"] - d, p["TOP_X"], p["TOP_Y"], p["R"], p["Z0"], p["Z1"])
    w = p["WALL"]
    inner = rrect_frustum(0.0, p["YC"], p["TOP_X"] - d - 2 * w, p["TOP_Y"] - d - 2 * w, p["TOP_X"] - 2 * w, p["TOP_Y"] - 2 * w, max(p["R"] - w, 1.0), p["Z0"] + w, p["Z1"] + 1)
    m = outer - inner
    cuts = [cyl_y(M3_CLEAR / 2, p["YC"] - p["TOP_Y"], p["YC"] + p["TOP_Y"], xx, p["MOUNT_Z"], fn=24) for xx in p["MOUNT_X"]]
    return D(m, *cuts)

def p17_guard_cap_servo(p=P17):
    return _guard_cap(p)

def p18_guard_cap_idler(p=P17):
    return mirror_y(_guard_cap(p))

# =====================================================================
# p19_p20_yoke_cheeks.scad  (cheek A servo side, cheek B idler side)
# =====================================================================
P19 = dict(X0=-18.0, X1=57.0, Z0=64.0, Z1=104.0, END_R=18.0, T=5.0, YA=(-98.0, -93.0), YB=(93.0, 98.0),
           DISC_PCD=18.0, ZERO_PIN=P13["ZERO_PIN"], ZERO_PIN_D=3.1,
           LUG_SX=3.0, LUG_R0=12.5, LUG_R1=20.0, LUG_Y=3.0,
           BAR_INS=((51.0, 72.0), (51.0, 100.0)), BORE_B=5.0)

def _cheek_profile(p):
    return CrossSection.batch_hull([cs_circle(p["END_R"], AXIS_X, AXIS_Z), cs_rect(AXIS_X, p["X1"], p["Z0"], p["Z1"])]) + \
        cs_rect(p["X0"], AXIS_X + 1, AXIS_Z - 10, AXIS_Z + 10) ^ cs_circle(p["END_R"], AXIS_X, AXIS_Z)

def p19_yoke_cheek_a(p=P19):
    y0, y1 = p["YA"]
    m = ext_y(CrossSection.batch_hull([cs_circle(p["END_R"], AXIS_X, AXIS_Z), cs_rect(AXIS_X, p["X1"], p["Z0"], p["Z1"])]), y0, y1)
    # stop lug below the axis, protruding toward the cradle (-Y)
    m = U(m, box(-p["LUG_SX"] / 2, p["LUG_SX"] / 2, y0 - p["LUG_Y"], y0 + 0.01, AXIS_Z - p["LUG_R1"], AXIS_Z - p["LUG_R0"]))
    cuts = []
    for i in range(4):   # inserts for P16 from the -Y (servo) face, at 45 deg (clear of the horn's PCD-12 screws)
        a = math.radians(45 + 90 * i)
        cuts.append(ins_y(M3_INS_D, M3_INS_L, AXIS_X + p["DISC_PCD"] / 2 * math.cos(a), AXIS_Z + p["DISC_PCD"] / 2 * math.sin(a), y0, toward=+1))
    cuts.append(cyl_y(p["ZERO_PIN_D"] / 2, y0 - 5, y1 + 1, p["ZERO_PIN"][0], p["ZERO_PIN"][1], fn=24))
    for xx, zz in p["BAR_INS"]:   # crossbar end-plate screws from the inner (+Y) face
        cuts.append(ins_y(M3_INS_D, M3_INS_L, xx, zz, y1, toward=-1))
    return D(m, *cuts)

def p20_yoke_cheek_b(p=P19):
    y0, y1 = p["YB"]
    m = ext_y(CrossSection.batch_hull([cs_circle(p["END_R"], AXIS_X, AXIS_Z), cs_rect(AXIS_X, p["X1"], p["Z0"], p["Z1"])]), y0, y1)
    cuts = [cyl_y(p["BORE_B"] / 2, y0 - 1, y1 + 1, AXIS_X, AXIS_Z, fn=32),
            cyl_y(M4_NUT_AF / math.sqrt(3), y0 - 1, y0 + M4_NUT_H, AXIS_X, AXIS_Z, fn=6)]   # nut trap on the inner face
    for xx, zz in p["BAR_INS"]:
        cuts.append(ins_y(M3_INS_D, M3_INS_L, xx, zz, y0, toward=+1))
    return D(m, *cuts)

# =====================================================================
# p21_yoke_crossbar.scad  (P21 crossbar + rail mast)
# =====================================================================
P21 = dict(BAR_X0=45.0, BAR_X1=57.0, BAR_Z0=80.0, BAR_Z1=96.0, BAR_Y=93.0, WALL=2.0, PLUG_L=10.0,
           END_T=3.0, END_Z0=68.0, END_Z1=104.0, END_X0=43.0, END_X1=59.0, END_HOLES=P19["BAR_INS"],
           MAST_X0=40.0, MAST_X1=45.0, MAST_Y=12.0, MAST_Z0=58.0, MAST_ARC_R=90.0,
           LIP_Y0=-5.5, LIP_Y1=-4.5, LIP_X=1.0, LIP_Z=((68.0, 73.0), (134.0, 160.0)),
           RAIL_INS_Z=(78.0, 98.0, 118.0, 138.0, 158.0),
           DOWNSTOP_INS=((-7.0, 64.0), (7.0, 64.0)), UPSTOP_INS=((-8.0, 136.0), (8.0, 136.0)),
           SHROUD_THRU_Z=(70.0, 105.0), SHROUD_THRU_X=42.5, CLEAT_INS=((-4.0, 146.0), (4.0, 146.0)))

def p21_yoke_crossbar(p=P21):
    by = p["BAR_Y"]
    bar = box(p["BAR_X0"], p["BAR_X1"], -by, by, p["BAR_Z0"], p["BAR_Z1"])
    w = p["WALL"]
    hollow = box(p["BAR_X0"] + w, p["BAR_X1"] - w, -by + p["PLUG_L"], by - p["PLUG_L"], p["BAR_Z0"] + w, p["BAR_Z1"] - w)
    parts = [bar - hollow]
    for s in (-1, 1):   # end plates against the cheeks' inner faces
        y0, y1 = sorted((s * by, s * (by - p["END_T"])))
        parts.append(box(p["END_X0"], p["END_X1"], y0, y1, p["END_Z0"], p["END_Z1"]))
    # mast: plate from Z0 up to an R 90 arc about the elbow axis, on the bar's -X face
    arc = cs_circle(p["MAST_ARC_R"], AXIS_X, AXIS_Z)
    prof = cs_rect(p["MAST_X0"], p["MAST_X1"], p["MAST_Z0"], AXIS_Z + p["MAST_ARC_R"] + 1) ^ arc
    parts.append(ext_y(prof, -p["MAST_Y"], p["MAST_Y"]))
    parts.append(box(p["MAST_X1"] - 0.01, p["MAST_X1"] + 1.0, -p["MAST_Y"], p["MAST_Y"], p["BAR_Z0"], p["BAR_Z1"]))   # 1 mm into the bar wall
    # rail reference lip on the -X face along the -Y rail edge, in two segments outside the carriage travel
    # (MGN9C underside clearance H1 ~1 mm [VERIFY]); clipped by the same arc
    for lz0, lz1 in p["LIP_Z"]:
        lip = cs_rect(p["MAST_X0"] - p["LIP_X"], p["MAST_X0"] + 0.01, lz0, lz1) ^ arc
        parts.append(ext_y(lip, p["LIP_Y0"], p["LIP_Y1"]))
    m = U(*parts)
    cuts = []
    for zz in p["RAIL_INS_Z"]:
        cuts.append(ins_x(M3_INS_D, M3_INS_L, 0.0, zz, p["MAST_X0"], toward=+1))
    for yy, zz in p["DOWNSTOP_INS"] + p["UPSTOP_INS"]:
        cuts.append(ins_x(M3_INS_D, M3_INS_L, yy, zz, p["MAST_X0"], toward=+1))
    for zz in p["SHROUD_THRU_Z"]:
        cuts.append(cyl_y(M3_CLEAR / 2, -p["MAST_Y"] - 1, p["MAST_Y"] + 1, p["SHROUD_THRU_X"], zz, fn=24))
    for yy, zz in p["CLEAT_INS"]:
        cuts.append(ins_x(M3_INS_D, M3_INS_L, yy, zz, p["MAST_X1"], toward=-1))
    for s in (-1, 1):
        for xx, zz in p["END_HOLES"]:
            y0, y1 = sorted((s * (by + 1), s * (by - p["END_T"] - 1)))
            cuts.append(cyl_y(M3_CLEAR / 2, y0, y1, xx, zz, fn=24))
    return D(m, *cuts)

# =====================================================================
# p22_rail_shroud.scad  (G4) and p23_p24_rail_stops.scad, p25_scale_strip.scad, p27_trim_cleat.scad
# =====================================================================
# G4: floor + two side walls only.  A front (-X) wall is impossible: the palm lid (X to 27.2, Z to 72) rises 28 mm
# through X 24..27 / Z 58..100 (CONFLICTS).  Scale dovetail on the OUTSIDE of the -Y wall, pointer fin passes a slot in it.
# Floor at Z 64: the knuckle plate's +X edge (X 32) rises to Z 61.2 at the float up-stop.  The down-stop block P23 plugs the floor cut-out.
P22 = dict(X0=27.5, X1=45.0, Y=17.0, Z0=64.0, Z1=108.0, WALL=2.0,
           DOVE_X0=31.0, DOVE_X1=39.0, DOVE_Y0=-21.0, DOVE_Y1=-17.0, DOVE_W_OPEN=5.0, DOVE_W_BOT=6.5, DOVE_D=1.0, DOVE_Z0=66.0, DOVE_Z1=106.0,
           LOCK_Z=80.0, FIN_SLOT=(26.5, 30.5, 68.0, 106.0), MAST_CUT=(39.0, 46.0, 12.5), STOP_CUT=(27.0, 41.0, 10.5),
           BACK_X1=47.0, BACK_NOTCH=(P21["BAR_Z0"] - 0.5, P21["BAR_Z1"] + 0.5),
           THRU=P21["SHROUD_THRU_Z"], THRU_X=P21["SHROUD_THRU_X"])

def p22_rail_shroud(p=P22):
    x0, x1, y, z0, z1, w = p["X0"], p["X1"], p["Y"], p["Z0"], p["Z1"], p["WALL"]
    m = box(x0, x1, -y, y, z0, z1) - box(x0 - 1, x1 + 1, -y + w, y - w, z0 + w, z1 + 1)      # floor + two side walls, open -X and top
    nz0, nz1 = p["BACK_NOTCH"]                                                             # back web behind the mast, notched for the crossbar
    m = U(m, box(x1 - 0.01, p["BACK_X1"], -y, y, z0, nz0), box(x1 - 0.01, p["BACK_X1"], -y, y, nz1, z1))
    m = U(m, box(p["DOVE_X0"], p["DOVE_X1"], p["DOVE_Y0"], p["DOVE_Y1"] + 0.01, z0, z1))   # dovetail boss outside the -Y wall
    mx0, mx1, my = p["MAST_CUT"]
    fx0, fx1, fz0, fz1 = p["FIN_SLOT"]
    sx0, sx1, sy = p["STOP_CUT"]
    cuts = [box(mx0, mx1, -my, my, z0 - 1, z1 + 1),                                        # mast passes through the floor
            box(sx0, sx1, -sy, sy, z0 - 1, z0 + w + 1),                                     # down-stop block P23 passes through the floor
            box(fx0, fx1, -y - 1, -y + w + 1, fz0, fz1)]                                    # pointer-fin slot in the -Y wall
    # (x, y) trapezoid: opening DOVE_W_OPEN at the boss's outer (-Y) face, DOVE_W_BOT at DOVE_D inside; extruded along Z
    dcx = (p["DOVE_X0"] + p["DOVE_X1"]) / 2
    yo, yb = p["DOVE_Y0"], p["DOVE_Y0"] + p["DOVE_D"]
    prof = cs_poly([(dcx - p["DOVE_W_OPEN"] / 2, yo - 1), (dcx + p["DOVE_W_OPEN"] / 2, yo - 1), (dcx + p["DOVE_W_OPEN"] / 2, yo),
                    (dcx + p["DOVE_W_BOT"] / 2, yb), (dcx - p["DOVE_W_BOT"] / 2, yb), (dcx - p["DOVE_W_OPEN"] / 2, yo)])
    cuts.append(ext_z(prof, p["DOVE_Z0"], p["DOVE_Z1"]))
    cuts.append(cyl_y(M3_CLEAR / 2, p["DOVE_Y0"] - 1, -y + w + 1, dcx, p["LOCK_Z"], fn=24))   # scale lock thumbscrew
    for zz in p["THRU"]:   # M3 through both side walls and the mast
        cuts.append(cyl_y(M3_CLEAR / 2, -y - 1, y + 1, p["THRU_X"], zz, fn=24))
    return D(m, *cuts)

P23 = dict(X0=28.0, X1=40.0, Y=10.0, Z0=60.0, Z1=68.0, SCREW_X=30.5, MOUNT=P21["DOWNSTOP_INS"])
P24 = dict(X0=28.0, X1=40.0, Y=10.0, Z0=132.0, Z1=140.0, PAD_T=2.0, PAD_RECESS=1.0, PAD_X=(28.0, 33.0),
           RAIL_CH_Y=6.0, RAIL_CH_X0=33.0, MOUNT=P21["UPSTOP_INS"])

def p23_rail_down_stop(p=P23):
    m = box(p["X0"], p["X1"], -p["Y"], p["Y"], p["Z0"], p["Z1"])
    cuts = [cyl_z(M3_INS_D / 2, p["Z0"] - 1, p["Z1"] + 1, p["SCREW_X"], 0, fn=24)]   # brass insert, vertical, thumbscrew from above
    for yy, zz in p["MOUNT"]:
        cuts.append(cyl_x(M3_CLEAR / 2, p["X0"] - 1, p["X1"] + 1, yy, zz, fn=24))
        cuts.append(cyl_x(M3_HEAD_D / 2, p["X0"] - 1, p["X0"] + M3_HEAD_H, yy, zz, fn=24))
    return D(m, *cuts)

def p24_rail_up_stop(p=P24):
    m = box(p["X0"], p["X1"], -p["Y"], p["Y"], p["Z0"], p["Z1"])
    cuts = [box(p["RAIL_CH_X0"], p["X1"] + 1, -p["RAIL_CH_Y"], p["RAIL_CH_Y"], p["Z0"] - 1, p["Z1"] + 1),   # straddles the rail
            box(p["PAD_X"][0] - 1, p["PAD_X"][1], -p["Y"] + 2, p["Y"] - 2, p["Z0"] - 1, p["Z0"] + p["PAD_RECESS"])]  # TPU pad recess
    for yy, zz in p["MOUNT"]:
        cuts.append(cyl_x(M3_CLEAR / 2, p["X0"] - 1, p["X1"] + 1, yy, zz, fn=24))
        cuts.append(cyl_x(M3_HEAD_D / 2, p["X0"] - 1, p["X0"] + M3_HEAD_H, yy, zz, fn=24))
    return D(m, *cuts)

P25 = dict(L=45.0, W=8.0, FACE_T=1.2, TANG_T=1.0, TANG_W_OPEN=4.8, TANG_W_BOT=6.3, RIDGE_W=0.4, RIDGE_H=0.3,
           TICK_SHORT=2.0, TICK_LONG=5.0, LOCK_SLOT=(3.4, 10.0))

def p25_scale_strip(p=P25):
    """LOCAL frame: strip along Z (0..L), ridged face toward +X (x = 0 plane), dovetail tang on -X matching P22's groove.
    Numerals 0/10/20/30 are inked after printing (no text() in the SCAD either)."""
    L, w = p["L"], p["W"]
    t = p["FACE_T"]
    face = box(-t, 0, -w / 2, w / 2, 0, L)
    xt0, xt1 = -t - p["TANG_T"], -t + 0.01
    tang = ext_z(cs_poly([(xt1, -p["TANG_W_OPEN"] / 2), (xt0, -p["TANG_W_BOT"] / 2), (xt0, p["TANG_W_BOT"] / 2), (xt1, p["TANG_W_OPEN"] / 2)]), 0, L)
    body = U(face, tang)
    ridges = []
    for i in range(0, int(L) + 1):
        tl = p["TICK_LONG"] if i % 5 == 0 else p["TICK_SHORT"]
        ridges.append(box(-0.01, p["RIDGE_H"], w / 2 - tl, w / 2, i - p["RIDGE_W"] / 2, i + p["RIDGE_W"] / 2))
    m = U(body, *ridges)
    sw, sl = p["LOCK_SLOT"]
    slot = hull(cyl_x(sw / 2, -t - p["TANG_T"] - 1, 1, 0, 8.0, fn=24), cyl_x(sw / 2, -t - p["TANG_T"] - 1, 1, 0, 8.0 + sl, fn=24))
    return D(m, slot)

P27 = dict(X0=45.0, X1=55.0, Y=8.0, Z0=140.0, Z1=152.0, CH_D=1.2, CH_X=52.0, CLAMP_Z=146.0, MOUNT=P21["CLEAT_INS"])   # top corner r = 89 < 90

def p27_trim_cleat(p=P27):
    m = box(p["X0"], p["X1"], -p["Y"], p["Y"], p["Z0"], p["Z1"])
    cuts = [cyl_z(p["CH_D"] / 2, p["Z0"] - 1, p["Z1"] + 1, p["CH_X"], 0, fn=16),                 # cord channel
            cyl_y(M3_INS_D / 2, -p["Y"] - 1, 0, p["CH_X"], p["CLAMP_Z"], fn=24)]                  # clamp thumbscrew insert
    for yy, zz in p["MOUNT"]:
        cuts.append(cyl_x(M3_CLEAR / 2, p["X0"] - 1, p["X1"] + 1, yy, zz, fn=24))
        cuts.append(cyl_x(M3_HEAD_D / 2, p["X1"] - M3_HEAD_H, p["X1"] + 1, yy, zz, fn=24))
    return D(m, *cuts)

# =====================================================================
# p26_carriage_riser.scad  (P26 L-bracket with foot tab, pointer fin and trim hook)
# =====================================================================
P26 = dict(PL_X0=27.0, PL_X1=30.0, PL_Y=10.0, PL_Z0=71.5, PL_Z1=103.0, CARR_ZC=88.5,
           TAB_X1=33.0, TAB_Y=4.0, TAB_Z0=69.0,
           ARM_X0=-5.0, ARM_Y=6.0, ARM_Z0=80.0, ARM_Z1=84.0, ARM_HOLES=(14.0, 4.0),
           FIN_Y0=-19.5, FIN_Y1=-10.0, FIN_Z=75.0, FIN_T=1.0, FIN_EDGE_T=0.6, FIN_EDGE_L=4.0,
           HOOK_D=2.0, HOOK_H=4.0, HOOK_HEAD=3.5, HOOK_Y=12.5)

def p26_carriage_riser(p=P26):
    parts = [box(p["PL_X0"], p["PL_X1"], -p["PL_Y"], p["PL_Y"], p["PL_Z0"], p["PL_Z1"]),
             box(p["PL_X0"], p["TAB_X1"], -p["TAB_Y"], p["TAB_Y"], p["TAB_Z0"], p["PL_Z0"] + 0.01),
             box(p["ARM_X0"], p["PL_X0"] + 0.01, -p["ARM_Y"], p["ARM_Y"], p["ARM_Z0"], p["ARM_Z1"]),
             # pointer fin: 1 mm plate from the plate's -Y edge through the shroud wall slot, 0.6 mm edge over the last 4 mm
             box(p["PL_X0"], p["PL_X1"], p["FIN_Y0"] + p["FIN_EDGE_L"], p["FIN_Y1"] + 0.01, p["FIN_Z"] - p["FIN_T"] / 2, p["FIN_Z"] + p["FIN_T"] / 2),
             box(p["PL_X0"], p["PL_X1"], p["FIN_Y0"], p["FIN_Y0"] + p["FIN_EDGE_L"] + 0.01, p["FIN_Z"] - p["FIN_EDGE_T"] / 2, p["FIN_Z"] + p["FIN_EDGE_T"] / 2),
             box(p["PL_X0"], p["PL_X1"], p["PL_Y"] - 0.01, p["HOOK_Y"] + 2.0, p["PL_Z1"] - 3.0, p["PL_Z1"]),                  # hook ear
             cyl_z(p["HOOK_D"] / 2, p["PL_Z1"] - 0.01, p["PL_Z1"] + p["HOOK_H"], (p["PL_X0"] + p["PL_X1"]) / 2, p["HOOK_Y"], fn=16),
             cyl_z(p["HOOK_HEAD"] / 2, p["PL_Z1"] + p["HOOK_H"] - 0.01, p["PL_Z1"] + p["HOOK_H"] + 1.5, (p["PL_X0"] + p["PL_X1"]) / 2, p["HOOK_Y"], fn=16)]
    m = U(*parts)
    cuts = mgn9c_holes_x(p["PL_X1"], -1, 0.0, p["CARR_ZC"])
    for xx in p["ARM_HOLES"]:
        cuts.append(cyl_z(M3_CLEAR / 2, p["ARM_Z0"] - 1, p["ARM_Z1"] + 1, xx, 0, fn=24))
    return D(m, *cuts)

# =====================================================================
# p28_upper_wrist_seat.scad  (P28) + p29_weight_cap.scad (P29) + p47_load_cell_filler.scad (P47)
# =====================================================================
P28 = dict(D=44.0, Z0=69.0, Z1=74.0, CONE_D0=18.4, CONE_D1=12.4, CONE_H=3.1, MAG_D=9.6, MAG_H=1.6,
           KEY_W=3.3, KEY_D=2.2, KEY_R0=14.0, KEY_R1=22.0,
           PK_X=45.0, PK_Y=17.0, PK_Z1=82.0, POCKET=(41.0, 13.0, 8.0), SEAT_SCREW_X=-14.0,
           POST_D=8.0, POST_XY=(0.0, 13.0), POST_Z1=108.0, EYE_D=2.0, EYE_XY=(-12.0, 16.0))

def p28_upper_wrist_seat(p=P28):
    z0, z1 = p["Z0"], p["Z1"]
    parts = [cyl_z(p["D"] / 2, z0, z1),
             cbox(0, 0, (z1 + p["PK_Z1"]) / 2, p["PK_X"], p["PK_Y"], p["PK_Z1"] - z1 + 0.02),
             cyl_z(p["POST_D"] / 2, z1 - 0.01, p["POST_Z1"], *p["POST_XY"])]
    m = U(*parts)
    px, py, pz = p["POCKET"]
    cuts = [cyl_z(p["CONE_D0"] / 2, z0 - 0.01, z0 + p["CONE_H"], r2=p["CONE_D1"] / 2),
            cyl_z(p["MAG_D"] / 2, z0 + p["CONE_H"] - 0.01, z0 + p["CONE_H"] + p["MAG_H"], fn=32),
            box(p["KEY_R0"], p["KEY_R1"] + 1, -p["KEY_W"] / 2, p["KEY_W"] / 2, z0 - 1, z0 + p["KEY_D"]),
            box(-px / 2, px / 2 + 5, -py / 2, py / 2, z1, p["PK_Z1"] + 1),         # load-cell pocket, open at the top and +X
            ins_z(M3_INS_D, M3_INS_L, p["SEAT_SCREW_X"], 0, z1),                     # filler / load-cell screw
            ins_z(M3_INS_D, M3_INS_L, p["POST_XY"][0], p["POST_XY"][1], p["POST_Z1"]),
            cyl_z(p["EYE_D"] / 2, z0 - 1, z1 + 1, *p["EYE_XY"], fn=16)]
    return D(m, *cuts)

P29 = dict(D=16.0, T=4.0, HOLE=M3_CLEAR, KNURL_N=12, KNURL_D=1.2)

def p29_weight_cap(p=P29):
    """LOCAL frame: disc z in [0, T]"""
    m = cyl_z(p["D"] / 2, 0, p["T"])
    cuts = [cyl_z(p["HOLE"] / 2, -1, p["T"] + 1, fn=24)]
    for i in range(p["KNURL_N"]):
        a = math.radians(360.0 * i / p["KNURL_N"])
        cuts.append(cyl_z(p["KNURL_D"] / 2, -1, p["T"] + 1, p["D"] / 2 * math.cos(a), p["D"] / 2 * math.sin(a), fn=12))
    return D(m, *cuts)

P47 = dict(L=40.0, W=12.0, T=6.0, HOLES=((-14.0, M3_CLEAR), (14.0, M3_PILOT), (4.0, M3_PILOT)))

def p47_load_cell_filler(p=P47):
    """LOCAL frame: bar along X centred, z in [0, T]. -14 clears to the seat insert; +14 / +4 are pilots for the P26 arm screws."""
    m = cbox(0, 0, p["T"] / 2, p["L"], p["W"], p["T"])
    return D(m, *[cyl_z(d / 2, -1, p["T"] + 1, xx, 0, fn=24) for xx, d in p["HOLES"]])

# =====================================================================
# p30_knuckle_plate.scad + p31_boot_frame.scad + p35_boot_template.scad  (shared slot outline)
# =====================================================================
SLOT = dict(OUTER=(31.8, 26.8), CENTRE=(34.8, 29.8), R=4.0, LEAD_IN=15.0)
P30 = dict(X=64.0, Y=90.0, CORNER_R=3.0, HOLES=((0.0, -41.0), (0.0, 41.0), (23.5, -37.0), (-23.5, 37.0), (23.5, 0.0), (-23.5, 0.0)),
           HOLE_D=M2_CLEAR, Z_TOP_CLIP=45.0, Z_BOT_CLIP=10.0)

def slot_cs(grow=0.0):
    cs = None
    for k, (cx, cy) in NAILS.items():
        sx, sy = SLOT["CENTRE"] if k == "C" else SLOT["OUTER"]
        c = cs_crrect(cx, cy, sx + 2 * grow, sy + 2 * grow, SLOT["R"] + grow)
        cs = c if cs is None else cs + c
    return cs

def slot_cutter(z0, z1, lead_in_z=None):
    """shared slot through the plate; 15 deg lead-in over the underside (wider below)"""
    body = ext_z(slot_cs(), z0, z1)
    if lead_in_z is not None:
        g = (lead_in_z - z0) * math.tan(math.radians(SLOT["LEAD_IN"]))
        body = U(body, hull(ext_z(slot_cs(g), z0, z0 + 0.01), ext_z(slot_cs(0.0), lead_in_z, lead_in_z + 0.01)))
    return body

def p30_knuckle_plate(p=P30):
    shell = sph_shell(KP_C_Z, KP_R, KP_R + KP_T)
    clip = rbox_z(-p["X"] / 2, p["X"] / 2, -p["Y"] / 2, p["Y"] / 2, p["Z_BOT_CLIP"], p["Z_TOP_CLIP"], p["CORNER_R"])
    m = shell ^ clip
    cuts = [slot_cutter(0.0, 50.0, lead_in_z=KP_C_Z + KP_R + 1.0)]
    for xx, yy in p["HOLES"]:
        cuts.append(cyl_z(p["HOLE_D"] / 2, 0, 50, xx, yy, fn=16))
    return D(m, *cuts)

P31 = dict(X=60.0, Y=86.0, CORNER_R=3.0, T=P31_T, HOLES=P30["HOLES"], HOLE_D=M2_CLEAR)

def p31_boot_frame(p=P31):
    r_in = KP_R + KP_T + BOOT_T
    shell = sph_shell(KP_C_Z, r_in, r_in + p["T"])
    m = shell ^ rbox_z(-p["X"] / 2, p["X"] / 2, -p["Y"] / 2, p["Y"] / 2, 10.0, 45.0, p["CORNER_R"])
    cuts = [ext_z(slot_cs(), 0, 50)] + [cyl_z(p["HOLE_D"] / 2, 0, 50, xx, yy, fn=16) for xx, yy in p["HOLES"]]
    return D(m, *cuts)

P35 = dict(X=76.0, Y=104.0, T=1.0, FLANGE=8.0, GROOVE_D=0.5, GROOVE_W=0.6, HOLE_SCALE=0.70, MARK_L=6.0)

def p35_boot_template(p=P35):
    """LOCAL frame (flat): plate with the boot outline as a 0.5 mm groove (cut line), paddle holes through at 70 % of the section, alignment notches"""
    t = p["T"]
    m = cbox(0, 0, t / 2, p["X"], p["Y"], t)
    cuts = []
    outline = slot_cs(p["FLANGE"])
    cuts.append(ext_z(outline - outline.offset(-p["GROOVE_W"], m3.JoinType.Miter, 2.0, FN), t - p["GROOVE_D"], t + 1))
    for k, (cx, cy) in NAILS.items():
        cuts.append(ext_z(cs_crrect(cx, cy, PAD_SEC_X * p["HOLE_SCALE"], PAD_SEC_Y * p["HOLE_SCALE"], 1.0), -1, t + 1))
    for s in (-1, 1):   # alignment notches on the X axis and Y axis
        cuts.append(cbox(s * p["X"] / 2, 0, t / 2, p["MARK_L"] * 2, 1.0, t + 2))
        cuts.append(cbox(0, s * p["Y"] / 2, t / 2, 1.0, p["MARK_L"] * 2, t + 2))
    return D(m, *cuts)

# =====================================================================
# p32_palm_tray.scad  (P32) + p33_palm_lid.scad (P33) + p34_root_clamp_bar.scad (P34)
# =====================================================================
P32 = dict(BOX_X=26.0, BOX_Y=40.0, Z_TOP=64.4, Z_FLOOR=38.0, WALL=0.8, FLOOR_T=0.8,   # walls end under the 1.6 lid (lid top at 66)
           ARM_N=dict(X0=-24.0, X1=16.0, Y0=-89.5), ARM_P=dict(X0=-8.0, X1=24.0, Y1=82.5),
           ROOT=dict(L=dict(XC=-8.0, Y0=-87.3, Y1=-73.3, FLOOR=44.1, BETA=4.4, DROP_TO=+1),
                     C=dict(XC=0.0, Y0=-59.5, Y1=-45.5, FLOOR=56.7, BETA=4.7, DROP_TO=+1),
                     R=dict(XC=8.0, Y0=66.7, Y1=80.7, FLOOR=44.0, BETA=5.0, DROP_TO=-1)),
           ROOT_X=28.0, WIN_X=24.2, WIN_Y=8.4, WIN_D=3.5, SLOT_W=12.9, SLOT_H=1.0, INS_X=8.6, BLOCK_BELOW=4.1,
           C_PEDESTAL_X=(2.0, 14.0),
           STOP=dict(L=dict(X=-11.0, Y=-34.5, Z0=48.0, Z1=52.0, X0=-25.5, X1=-3.0),
                     C=dict(X=0.0, Y=-10.0, Z0=59.5, Z1=63.5, X0=-25.5, X1=25.5),
                     R=dict(X=8.0, Y=34.5, Z0=48.0, Z1=52.0, X0=1.0, X1=25.5)),
           STOP_W=7.0,
           LID_INS=((-24.0, -20.0), (24.0, -20.0), (-24.0, 20.0), (24.0, 20.0), (10.0, -87.5), (-4.0, 80.5)),
           LID_BOSS_D=4.0, LID_BOSS_Z0=52.0,
           PLATE_INS=P30["HOLES"], PLATE_BOSS_D=5.0)

def root_block_cuts(rb, p=P32):
    """window + wall slots + 2 M2 inserts for one tray root block, tilted by beta about X through the floor line"""
    xc, y0, y1, fl = rb["XC"], rb["Y0"], rb["Y1"], rb["FLOOR"]
    yc = (y0 + y1) / 2
    parts = [cbox(xc, yc, fl + 50, p["WIN_X"], p["WIN_Y"], 100.0),                                  # clamp window from the top
             cbox(xc, yc, fl + p["SLOT_H"] / 2 - 0.005, p["SLOT_W"], (y1 - y0) + 2, p["SLOT_H"] + 0.01)]   # leaf slot through both Y walls
    for sx in (-p["INS_X"], p["INS_X"]):
        parts.append(cyl_z(M2_INS_D / 2, fl - M2_INS_L, fl + 0.01, xc + sx, yc, fn=16))
    c = U(*parts)
    # pre-tilt: floor drops toward the paddle (DROP_TO = +1 toward +Y)
    return rot_about(c, "x", -rb["DROP_TO"] * rb["BETA"], (xc, yc, fl))

def p32_palm_tray(p=P32):
    bxh, byh, zt, w = p["BOX_X"], p["BOX_Y"], p["Z_TOP"], p["WALL"]
    an, ap = p["ARM_N"], p["ARM_P"]
    zf = p["Z_FLOOR"]
    # centre box: walls from the top down to the spherical underside (the knuckle plate / boot / P31 stack)
    sph_out = sphere(TRAY_BOT_R, (0, 0, KP_C_Z), 160)
    box_outer = box(-bxh, bxh, -byh, byh, 10.0, zt)
    box_inner = box(-bxh + w, bxh - w, -byh + w, byh - w, 10.0, zt + 1)
    centre = (box_outer - box_inner) - sph_out
    # arms: open-top trays with flat floors at Z_FLOOR
    arm_n = box(an["X0"], an["X1"], an["Y0"], -byh + w, zf, zt) - box(an["X0"] + w, an["X1"] - w, an["Y0"] + w, -byh + w + 1, zf + p["FLOOR_T"], zt + 1)
    arm_p = box(ap["X0"], ap["X1"], byh - w, ap["Y1"], zf, zt) - box(ap["X0"] + w, ap["X1"] - w, byh - w - 1, ap["Y1"] - w, zf + p["FLOOR_T"], zt + 1)
    # open the box walls where the arms join (inside the arm outline, above the arm floor)
    centre = centre - box(an["X0"] + w, an["X1"] - w, -byh - 1, -byh + w + 0.01, zf + p["FLOOR_T"], zt + 1)
    centre = centre - box(ap["X0"] + w, ap["X1"] - w, byh - w - 0.01, byh + 1, zf + p["FLOOR_T"], zt + 1)
    parts = [centre, arm_n, arm_p]
    # root blocks
    rb = p["ROOT"]
    for k, r in rb.items():
        z_top = r["FLOOR"] + p["WIN_D"]
        z_bot = r["FLOOR"] - p["BLOCK_BELOW"]
        if k == "C":
            parts.append(box(r["XC"] - p["ROOT_X"] / 2, r["XC"] + p["ROOT_X"] / 2, r["Y0"], r["Y1"], z_bot, z_top))
            parts.append(box(p["C_PEDESTAL_X"][0], p["C_PEDESTAL_X"][1], r["Y0"], r["Y1"], zf + 0.5, z_bot + 0.01))
        else:
            parts.append(box(r["XC"] - p["ROOT_X"] / 2, r["XC"] + p["ROOT_X"] / 2, r["Y0"], r["Y1"], zf + 0.5, z_top))
    # stop beams (M3 insert vertical, nylon screw head down)
    for k, s in p["STOP"].items():
        parts.append(box(s["X0"], s["X1"], s["Y"] - p["STOP_W"] / 2, s["Y"] + p["STOP_W"] / 2, s["Z0"], s["Z1"]))
    # lid-screw bosses hanging from the rim, plate-screw bosses standing on the spherical underside
    for xx, yy in p["LID_INS"]:
        parts.append(cyl_z(p["LID_BOSS_D"] / 2, p["LID_BOSS_Z0"], zt, xx, yy, fn=24))
    for xx, yy in p["PLATE_INS"]:
        z_sph = KP_C_Z + math.sqrt(TRAY_BOT_R ** 2 - xx ** 2 - yy ** 2)
        parts.append(cyl_z(p["PLATE_BOSS_D"] / 2, z_sph - 2.0, max(z_sph + 6.0, zf + 1.0), xx, yy, fn=24) - sph_out)
    m = U(*parts)
    cuts = [root_block_cuts(r, p) for r in rb.values()]
    for k, s in p["STOP"].items():
        cuts.append(cyl_z(M3_INS_D / 2, s["Z0"] - 1, s["Z1"] + 1, s["X"], s["Y"], fn=24))
    for xx, yy in p["LID_INS"]:
        cuts.append(ins_z(M2_INS_D, M2_INS_L, xx, yy, zt))
    for xx, yy in p["PLATE_INS"]:
        z_sph = KP_C_Z + math.sqrt(TRAY_BOT_R ** 2 - xx ** 2 - yy ** 2)
        cuts.append(cyl_z(M2_INS_D / 2, z_sph - 3.0, z_sph + M2_INS_L, xx, yy, fn=16))
    return D(m, *cuts)

P33 = dict(T=1.6, SKIRT_H=2.0, SKIRT_T=1.2, SEAT_D=40.0, SEAT_IN_D=30.0, SEAT_Z1=69.0, LAND_RECESS=0.3,
           CONE_D0=18.0, CONE_D1=12.0, CONE_H=3.0, KEEPER_D=12.2, KEEPER_H=1.5,
           PEG_D=3.0, PEG_H=2.0, PEG_R=17.0, CUP_D=12.0, CUP_H=6.0, CUP_Y=25.0, EYE_D=2.0, EYE_XY=(8.0, 25.0),
           HOLES=P32["LID_INS"], HOLE_D=M2_CLEAR)

def p33_palm_lid(p=P33, t=P32):
    zt = t["Z_TOP"] + p["T"]          # lid top at Z 66
    an, ap = t["ARM_N"], t["ARM_P"]
    s = p["SKIRT_T"]
    def outline(g):
        return (cs_rect(-t["BOX_X"] - g, t["BOX_X"] + g, -t["BOX_Y"] - g, t["BOX_Y"] + g)
                + cs_rect(an["X0"] - g, an["X1"] + g, an["Y0"] - g, -t["BOX_Y"] + 1)
                + cs_rect(ap["X0"] - g, ap["X1"] + g, t["BOX_Y"] - 1, ap["Y1"] + g))
    top = ext_z(outline(s), zt - p["T"], zt)
    skirt = ext_z(outline(s) - outline(0.0), zt - p["T"] - p["SKIRT_H"], zt - p["T"] + 0.01)
    seat = cyl_z(p["SEAT_D"] / 2, zt - 0.01, p["SEAT_Z1"])
    cone_z0 = p["SEAT_Z1"] - p["LAND_RECESS"]
    cone = cyl_z(p["CONE_D0"] / 2 + p["LAND_RECESS"], cone_z0 - 0.01, cone_z0 + p["CONE_H"] + p["LAND_RECESS"], r2=p["CONE_D1"] / 2)
    peg = U(cyl_z(p["PEG_D"] / 2, p["SEAT_Z1"] - 0.01, p["SEAT_Z1"] + p["PEG_H"] - p["PEG_D"] / 2, p["PEG_R"], 0, fn=24),
            sphere(p["PEG_D"] / 2, (p["PEG_R"], 0, p["SEAT_Z1"] + p["PEG_H"] - p["PEG_D"] / 2), 24))
    cup = cyl_z(p["CUP_D"] / 2 + 1.0, zt - p["CUP_H"], zt - p["T"] + 0.01, 0, p["CUP_Y"], fn=32)
    m = U(top, skirt, seat, cone, peg, cup)
    cuts = [cyl_z(p["SEAT_IN_D"] / 2, p["SEAT_Z1"] - p["LAND_RECESS"], p["SEAT_Z1"] + 1) - cyl_z(p["CONE_D0"] / 2 + p["LAND_RECESS"] + 0.3, p["SEAT_Z1"] - 1, p["SEAT_Z1"] + 2),
            cyl_z(p["KEEPER_D"] / 2, cone_z0 + p["CONE_H"] + p["LAND_RECESS"] - p["KEEPER_H"], cone_z0 + p["CONE_H"] + 2, fn=32),
            cyl_z(p["CUP_D"] / 2, zt - p["CUP_H"] + 1.0, zt + 1, 0, p["CUP_Y"], fn=32),
            cyl_z(p["EYE_D"] / 2, zt - 10, zt + 1, *p["EYE_XY"], fn=16)]
    for xx, yy in p["HOLES"]:
        cuts.append(cyl_z(p["HOLE_D"] / 2, zt - 10, zt + 1, xx, yy, fn=16))
    return D(m, *cuts)

P34 = dict(X=24.0, Y=8.0, T=3.0, GROOVE_W=12.9, GROOVE_D=0.25, HOLE_D=M2_CLEAR, HOLE_X=8.6)

def p34_root_clamp_bar(p=P34):
    """LOCAL frame, groove side DOWN at z=0 (print groove up = flip); matches the paddle clamp bar scheme"""
    m = cbox(0, 0, p["T"] / 2, p["X"], p["Y"], p["T"])
    cuts = [cbox(0, 0, p["GROOVE_D"] / 2 - 0.005, p["GROOVE_W"], p["Y"] + 2, p["GROOVE_D"] + 0.01)]
    for sx in (-p["HOLE_X"], p["HOLE_X"]):
        cuts.append(cyl_z(p["HOLE_D"] / 2, -1, p["T"] + 1, sx, 0, fn=16))
    return D(m, *cuts)

# =====================================================================
# p03_p04_electronics_tray.scad  (P3 tray, P4 lid)
# =====================================================================
P3 = dict(X0=-120.0, X1=-88.0, Y0=17.0, Y1=53.0, Z0=100.0, Z1=192.0, WALL=2.0, BACK=2.5,
          BRD_L=66.0, BRD_W=25.0, BRD_Z0=109.0, BRD_HOLES=((-4.5, 3.5), (-4.5, 62.5), (16.5, 3.5), (16.5, 62.5)),
          BOSS_D=5.0, BOSS_H=5.0, BOSS_HOLE=2.5,
          USB=(12.0, 7.0), USB_X=-107.5, SLOT=(8.0, 4.0), LID_BOSS_D=8.0, LID_INS=((22.0, 104.0), (48.0, 188.0)),
          CARD_SLOT_X=-97.5, CARD_SLOT_W=1.9, CARD_Z0=152.0, CARD_Z1=180.0, MOUNT_HOLES=P1["TRAY_HOLES"])

def p03_electronics_tray(p=P3):
    x0, x1, y0, y1, z0, z1, w, b = p["X0"], p["X1"], p["Y0"], p["Y1"], p["Z0"], p["Z1"], p["WALL"], p["BACK"]
    yc = (y0 + y1) / 2
    m = box(x0, x1, y0, y1, z0, z1) - box(x0 + b, x1 + 1, y0 + w, y1 - w, z0 + w, z1 - w)
    adds = []
    # OpenRB-150 standoffs (board long axis along Z) [VERIFY hole pattern]
    for du, dv in p["BRD_HOLES"]:
        adds.append(cyl_x(p["BOSS_D"] / 2, x0 + b - 0.01, x0 + b + p["BOSS_H"], yc + du - 6.0, p["BRD_Z0"] + dv, fn=24))
    # lid-screw corner bosses (inserts from the open face)
    for yy, zz in p["LID_INS"]:
        adds.append(cyl_x(p["LID_BOSS_D"] / 2, x0 + b - 0.01, x1, yy, zz, fn=32))
    # perfboard card guides (pairs of ribs on both side walls)
    for s, yw in ((1, y0 + w), (-1, y1 - w)):
        for dx in (-p["CARD_SLOT_W"] / 2 - 1.2, p["CARD_SLOT_W"] / 2):
            ya, yb = sorted((yw - 0.01 * s, yw + 1.0 * s))
            adds.append(box(p["CARD_SLOT_X"] + dx, p["CARD_SLOT_X"] + dx + 1.2, ya, yb, p["CARD_Z0"], p["CARD_Z1"]))
    m = U(m, *adds)
    cuts = []
    for du, dv in p["BRD_HOLES"]:
        cuts.append(cyl_x(p["BOSS_HOLE"] / 2, x0 + 0.5, x0 + b + p["BOSS_H"] + 1, yc + du - 6.0, p["BRD_Z0"] + dv, fn=16))
    for yy, zz in p["LID_INS"]:
        cuts.append(ins_x(M3_INS_D, 6.0, yy, zz, x1, toward=-1))
    for yy, zz in p["MOUNT_HOLES"]:
        cuts.append(cyl_x(M3_CLEAR / 2, x0 - 1, x0 + b + 1, yy, zz, fn=24))
    ux, uw = p["USB"]
    cuts.append(box(p["USB_X"] - uw / 2, p["USB_X"] + uw / 2, yc - ux / 2, yc + ux / 2, z0 - 1, z0 + w + 1))
    sx, sw = p["SLOT"]
    cuts.append(box(x1 - 10 - sw, x1 - 10, yc - sx / 2, yc + sx / 2, z1 - w - 1, z1 + 1))
    cuts.append(box(x1 - 10 - sw, x1 - 10, y0 + 6 - sx / 2, y0 + 6 + sx / 2, z0 - 1, z0 + w + 1))
    return D(m, *cuts)

P4 = dict(T=2.0, VENT_W=2.0, VENT_L=20.0, VENT_Z0=(112.0, 134.0), VENT_DY=(-13.0, 13.0),
          LABEL=(20.0, 30.0, 0.6), LABEL_ZC=170.0, WAGO_POCKET=(13.6, 20.6, 8.6), WAGO_ZC=118.0)

def p04_tray_lid(p=P4, t=P3):
    """lid on the tray's open (+X) face: 2 mm plate, 4 vent slots 2 x 20 (two columns at yc +/-13, two rows),
    2 x diam 3.4 screw holes on the tray's lid inserts, a 0.6 mm label recess, and a Wago 221-413 cradle inside"""
    x0 = t["X1"]
    yc = (t["Y0"] + t["Y1"]) / 2
    m = box(x0, x0 + p["T"], t["Y0"], t["Y1"], t["Z0"], t["Z1"])
    wy, wz, wx = p["WAGO_POCKET"]          # [VERIFY 13.1 x 20.3 x 8.1 body]
    cr = box(x0 - wx - 1.2, x0 + 0.01, yc - wy / 2 - 1.2, yc + wy / 2 + 1.2, p["WAGO_ZC"] - wz / 2 - 1.2, p["WAGO_ZC"] + wz / 2 + 1.2)
    cr = cr - box(x0 - wx - 2, x0 + 0.02, yc - wy / 2, yc + wy / 2, p["WAGO_ZC"] - wz / 2, p["WAGO_ZC"] + wz / 2 + 5)
    m = U(m, cr)
    cuts = [cyl_x(M3_CLEAR / 2, x0 - 1, x0 + p["T"] + 1, yy, zz, fn=24) for yy, zz in t["LID_INS"]]
    for zz in p["VENT_Z0"]:
        for dy in p["VENT_DY"]:
            cuts.append(box(x0 - 1, x0 + p["T"] + 1, yc + dy - p["VENT_W"] / 2, yc + dy + p["VENT_W"] / 2, zz, zz + p["VENT_L"]))
    lw, lh, ld = p["LABEL"]
    cuts.append(box(x0 + p["T"] - ld, x0 + p["T"] + 1, yc - lw / 2, yc + lw / 2, p["LABEL_ZC"] - lh / 2, p["LABEL_ZC"] + lh / 2))
    return D(m, *cuts)

# =====================================================================
# p37_p38_control_panel.scad  (LOCAL frame: box face up, z = 0 is the open base)
# =====================================================================
P37 = dict(X=100.0, Y=60.0, Z=40.0, WALL=2.0, R=4.0, POT_D=7.2, POT_X=(-30.0, 0.0), POT_Y=8.0, POT_KEY=(1.2, 1.5),
           TOGGLE_D=6.2, TOGGLE_XY=(30.0, 8.0), LED_D=5.2, LED_XY=(30.0, -14.0), TICK_R=9.0, TICK=(1.0, 2.0, 0.5),
           GLAND_D=6.0, GLAND_Z=20.0, GLAND_Y=0.0, CORNER_INS=((-45.0, -25.0), (45.0, -25.0), (-45.0, 25.0), (45.0, 25.0)), CORNER_BOSS_D=7.0)

def p37_control_panel_box(p=P37):
    x, y, z, w = p["X"], p["Y"], p["Z"], p["WALL"]
    m = rbox_z(-x / 2, x / 2, -y / 2, y / 2, 0, z, p["R"]) - rbox_z(-x / 2 + w, x / 2 - w, -y / 2 + w, y / 2 - w, -1, z - w, p["R"] - w)
    for xx, yy in p["CORNER_INS"]:
        m = U(m, cyl_z(p["CORNER_BOSS_D"] / 2, 0, z - w + 0.01, xx, yy, fn=24))
    cuts = []
    for xx in p["POT_X"]:
        cuts.append(cyl_z(p["POT_D"] / 2, z - w - 1, z + 1, xx, p["POT_Y"], fn=24))
        kw, kl = p["POT_KEY"]
        cuts.append(cbox(xx + p["POT_D"] / 2 + kl / 2 - 0.3, p["POT_Y"], z, kl + 0.6, kw, 2 * w + 2))      # anti-rotation slot
        for i in range(3):   # 0 / 50 / 100 % tick recesses around each pot (at 225, 90, -45 deg)
            a = math.radians(225 - 135 * i)
            tw, tl, td = p["TICK"]
            cuts.append(rot_about(cbox(xx + p["TICK_R"] * math.cos(a), p["POT_Y"] + p["TICK_R"] * math.sin(a), z, tl, tw, 2 * td), "z", math.degrees(a), (xx + p["TICK_R"] * math.cos(a), p["POT_Y"] + p["TICK_R"] * math.sin(a), z)))
    cuts.append(cyl_z(p["TOGGLE_D"] / 2, z - w - 1, z + 1, *p["TOGGLE_XY"], fn=24))
    cuts.append(cyl_z(p["LED_D"] / 2, z - w - 1, z + 1, *p["LED_XY"], fn=24))
    cuts.append(cyl_x(p["GLAND_D"] / 2, -x / 2 - 1, -x / 2 + w + 1, p["GLAND_Y"], p["GLAND_Z"], fn=24))
    for xx, yy in p["CORNER_INS"]:
        cuts.append(ins_z(M3_INS_D, M3_INS_L + 2, xx, yy, 0, down=False))
    return D(m, *cuts)

P38 = dict(X=100.0, Y=60.0, T=2.0, R=4.0, HOLES=P37["CORNER_INS"], FOOT_D=10.0, FOOT_H=1.0, FOOT_XY=((-38.0, -18.0), (38.0, -18.0), (-38.0, 18.0), (38.0, 18.0)))

def p38_control_panel_lid(p=P38):
    m = rbox_z(-p["X"] / 2, p["X"] / 2, -p["Y"] / 2, p["Y"] / 2, 0, p["T"], p["R"])
    cuts = [cyl_z(M3_CLEAR / 2, -1, p["T"] + 1, xx, yy, fn=24) for xx, yy in p["HOLES"]]
    cuts += [cyl_z(p["FOOT_D"] / 2, -1, p["FOOT_H"], xx, yy, fn=32) for xx, yy in p["FOOT_XY"]]
    return D(m, *cuts)

# =====================================================================
# p39_p40_button_housing.scad  (LOCAL frame: axis along Z, cup at the top, split plane X = 0;
#   half A is x >= 0, half B is x <= 0 mirrored; both printed split face down)
# =====================================================================
P39 = dict(L=110.0, CUP_D=36.0, CUP_H=24.0, RIM_WALL=2.0, DECK_T=2.0, DECK_BELOW_RIM=3.0, BTN_HOLE=30.2,   # 30.0 mounting hole (bom-verified.md section 11 item 4): print 30.2, ream to 30.0
           GRIP_D=30.0, GRIP_WALL=2.0, GLAND_D=12.0, GLAND_H=10.0, GLAND_BORE=6.0,
           ANCHOR_Z=18.0, ANCHOR=(4.0, 3.0), SCREW_Z=(30.0, 80.0), SCREW_Y=0.0, BOSS_D=8.0, PIN_D=3.0, PIN_H=3.0, PIN_Z=(45.0, 65.0), PIN_Y=0.0, PIN_BOSS_D=6.0)

def _button_housing_full(p):
    L, cd, ch = p["L"], p["CUP_D"], p["CUP_H"]
    z_cup0 = L - ch
    outer = U(cyl_z(cd / 2, z_cup0, L), hull(cyl_z(cd / 2, z_cup0 - 0.01, z_cup0), cyl_z(p["GRIP_D"] / 2, z_cup0 - 8, z_cup0 - 8 + 0.01)),
              cyl_z(p["GRIP_D"] / 2, p["GLAND_H"], z_cup0 - 8 + 0.01), cyl_z(p["GLAND_D"] / 2, 0, p["GLAND_H"] + 0.01))
    for zz in p["SCREW_Z"]:   # split-plane screw bosses
        outer = U(outer, cyl_x(p["BOSS_D"] / 2, -p["GRIP_D"] / 2 + 1, p["GRIP_D"] / 2 - 1, p["SCREW_Y"], zz))
    pin_bosses = [cyl_x(p["PIN_BOSS_D"] / 2, -p["GRIP_D"] / 2 + 1, p["GRIP_D"] / 2 - 1, p["PIN_Y"], zz) for zz in p["PIN_Z"]]
    deck_top = L - p["DECK_BELOW_RIM"]
    cuts = [cyl_z(cd / 2 - p["RIM_WALL"], deck_top, L + 1),                                   # thumb well above the deck
            cyl_z(p["BTN_HOLE"] / 2, deck_top - p["DECK_T"] - 1, deck_top + 1),                # button hole [VERIFY]
            cyl_z(cd / 2 - p["RIM_WALL"], z_cup0 + 2, deck_top - p["DECK_T"] + 0.01),          # cup interior
            cyl_z(p["GRIP_D"] / 2 - p["GRIP_WALL"], p["GLAND_H"] + 2, z_cup0 + 2 + 0.01),      # grip interior
            cyl_z(p["GLAND_BORE"] / 2, -1, p["GLAND_H"] + 3)]                                   # cable bore
    aw, ad = p["ANCHOR"]
    cuts.append(cbox(0, p["GRIP_D"] / 2 - 1, p["ANCHOR_Z"], aw, 6.0, ad))                        # zip-tie anchor slot (bar left above the gland)
    return U(D(outer, *cuts), *pin_bosses)

def p39_button_housing_half_a(p=P39):
    full = _button_housing_full(p)
    half = full ^ box(0, 40, -40, 40, -1, p["L"] + 1)
    cuts = []
    for zz in p["SCREW_Z"]:
        cuts.append(cyl_x(M3_CLEAR / 2, -1, 40, p["SCREW_Y"], zz, fn=24))
        cuts.append(cyl_x(M3_HEAD_D / 2, p["BOSS_D"] / 2 + 1.0, 40, p["SCREW_Y"], zz, fn=24))   # counterbore from the outside
    for zz in p["PIN_Z"]:
        cuts.append(cyl_x((p["PIN_D"] + 0.2) / 2, -1, p["PIN_H"] + 0.2, p["PIN_Y"], zz, fn=16))
    return D(half, *cuts)

def p40_button_housing_half_b(p=P39):
    full = _button_housing_full(p)
    half = full ^ box(-40, 0, -40, 40, -1, p["L"] + 1)
    cuts = [ins_x(M3_INS_D, M3_INS_L + 1, p["SCREW_Y"], zz, 0, toward=-1) for zz in p["SCREW_Z"]]
    m = D(half, *cuts)
    for zz in p["PIN_Z"]:
        m = U(m, cyl_x(p["PIN_D"] / 2, -1.0, p["PIN_H"], p["PIN_Y"], zz, fn=16))
    return m

# =====================================================================
# p36_cable_clip.scad, p41-p46, p48  (LOCAL frames)
# =====================================================================
P36 = dict(X=12.0, Y=10.0, BASE_T=2.0, NECK_W=5.8, NECK_H=1.8, FOOT_W=9.5, FOOT_T=1.5, LOOP_ID=5.0, LOOP_WALL=1.5, TIE=(3.0, 1.5))

def p36_cable_clip(p=P36):
    """2020 T-slot snap foot (-Z), cable loop (C ring, axis along Y) and a zip-tie slot"""
    base = cbox(0, 0, p["BASE_T"] / 2, p["X"], p["Y"], p["BASE_T"])
    neck = cbox(0, 0, -p["NECK_H"] / 2, p["NECK_W"], p["Y"], p["NECK_H"])
    foot = cbox(0, 0, -p["NECK_H"] - p["FOOT_T"] / 2, p["FOOT_W"], p["Y"], p["FOOT_T"])
    rid, rw = p["LOOP_ID"] / 2, p["LOOP_WALL"]
    loop = cyl_y(rid + rw, -p["Y"] / 2, p["Y"] / 2, 0, p["BASE_T"] + rid + rw - 0.5) - cyl_y(rid, -p["Y"] - 1, p["Y"] + 1, 0, p["BASE_T"] + rid + rw - 0.5)
    loop = loop - box(-1.2, 1.2, -p["Y"] - 1, p["Y"] + 1, p["BASE_T"] + rid + rw, p["BASE_T"] + 2 * rid + 3 * rw)   # C opening
    m = U(base, neck, foot, loop)
    tw, tt = p["TIE"]
    return D(m, box(-p["X"] / 2 - 1, p["X"] / 2 + 1, -tw / 2, tw / 2, p["BASE_T"] + 0.2, p["BASE_T"] + 0.2 + tt))

P41 = dict(D=40.0, H=12.0, CUP_D=30.4, CUP_H=8.0, SCREW_R=16.0, SCREW_D=M3_CLEAR, CSK_D=7.0)

def p41_cradle_foot_cup(p=P41):
    m = cyl_z(p["D"] / 2, 0, p["H"], fn=64)
    cuts = [cyl_z(p["CUP_D"] / 2, p["H"] - p["CUP_H"], p["H"] + 1, fn=64)]
    for s in (-1, 1):
        cuts.append(csk_z(p["SCREW_D"], p["CSK_D"], s * p["SCREW_R"], 0, p["H"], down=True))
    return D(m, *cuts)

P42 = dict(L=120.0, W=60.0, ANG=15.0, RIB_N=6, RIB=(2.0, 1.0), PAD_T=2.0, PAD_INSET=5.0)

def p42_cradle_tilt_wedge(p=P42):
    L, w, h = p["L"], p["W"], p["L"] * math.tan(math.radians(p["ANG"]))
    prof = cs_poly([(0, 0), (L, 0), (L, h)])            # (x, z); thick end at +X
    m = ext_y(prof, -w / 2, w / 2)
    cuts = []
    rw, rh = p["RIB"]
    for i in range(1, p["RIB_N"] + 1):                   # anti-slip grooves on the underside
        xx = L * i / (p["RIB_N"] + 1)
        cuts.append(cbox(xx, 0, 0, rw, w + 2, 2 * rh))
    # TPU pad recess on the sloping face: a slab parallel to the slope
    pad = cbox(L / 2, 0, 0, L - 2 * p["PAD_INSET"], w - 2 * p["PAD_INSET"], 2 * p["PAD_T"])
    pad = rot_about(pad, "y", -p["ANG"], (0, 0, 0)).translate([0, 0, 0])
    cuts.append(rot_about(cbox(L / 2 * math.cos(math.radians(p["ANG"])) ** 2 * 0 + L / 2, 0, (L / 2) * math.tan(math.radians(p["ANG"])), L - 2 * p["PAD_INSET"], w - 2 * p["PAD_INSET"], 2 * p["PAD_T"]), "y", -p["ANG"], (L / 2, 0, (L / 2) * math.tan(math.radians(p["ANG"])))))
    return D(m, *cuts)

P43 = dict(S=12.0, L=120.0, FOOT_R=6.0, RINGS=(80.0, 82.0, 84.0, 86.0, 88.0), RING=(0.6, 0.4))

def p43_apex_height_gauge(p=P43):
    """LOCAL frame: stick along Z, foot tip at z = 0 (rounded R 6), rings measured from the foot tip"""
    s, L = p["S"], p["L"]
    m = U(cbox(0, 0, (L + p["FOOT_R"]) / 2, s, s, L - p["FOOT_R"]), sphere(p["FOOT_R"], (0, 0, p["FOOT_R"]), 48))
    m = m ^ cbox(0, 0, L / 2, s, s, L)
    cuts = []
    rw, rd = p["RING"]
    for zz in p["RINGS"]:
        cuts.append(cbox(0, 0, zz, s + 2, s + 2, rw) - cbox(0, 0, zz, s - 2 * rd, s - 2 * rd, rw + 1))
    return D(m, *cuts)

P44 = dict(D=14.0, L=40.0, BORE=2.5, KNOT_D=6.0, KNOT_H=4.0, CH=1.0)

def p44_reset_toggle(p=P44):
    """LOCAL frame: axis along X, centred at the origin"""
    r, L, c = p["D"] / 2, p["L"], p["CH"]
    m = U(cyl_x(r, -L / 2 + c, L / 2 - c),
          hull(cyl_x(r - c, -L / 2, -L / 2 + 0.01), cyl_x(r, -L / 2 + c, -L / 2 + c + 0.01)),
          hull(cyl_x(r, L / 2 - c - 0.01, L / 2 - c), cyl_x(r - c, L / 2 - 0.01, L / 2)))
    return D(m, cyl_z(p["BORE"] / 2, -r - 1, r + 1, fn=16), cyl_z(p["KNOT_D"] / 2, r - p["KNOT_H"], r + 1, fn=24))

P45 = dict(X0=-95.0, X1=-80.0, Y=20.0, Z0=5.0, Z1=20.0, CH_D=3.0, CH_Z=12.0, BEND_R=3.0, SCREW=P1["GUIDE_HOLES"])

def p45_reset_cord_guide(p=P45):
    """installed under the magnet arm's bottom web (Z 20): channel comes in horizontally from +X, bends R 3 and leaves downward"""
    hy = p["Y"] / 2
    m = box(p["X0"], p["X1"], -hy, hy, p["Z0"], p["Z1"])
    r, xb, zc = p["CH_D"] / 2, -88.0, p["CH_Z"]
    horiz = cyl_x(r, xb, p["X1"] + 1, 0, zc, fn=24)
    bend_c = (xb, 0, zc - p["BEND_R"])
    # quarter torus: revolve gives the +x/+y quadrant about Z; MAP_Y puts it in the XZ plane (+x/+z); R_y(-90) turns it to -x/+z
    tor = CrossSection.circle(r, 24).translate([p["BEND_R"], 0]).revolve(48, 90.0).transform(MAP_Y)
    tor = rot_about(tor, "y", -90, (0, 0, 0)).translate(list(bend_c))
    down = cyl_z(r, p["Z0"] - 1, zc - p["BEND_R"], xb - p["BEND_R"], 0, fn=24)
    ent = cyl_x(r + p["BEND_R"], p["X1"] - 0.6, p["X1"] + 1, 0, zc, fn=24)
    ent = hull(cyl_x(r, p["X1"] - p["BEND_R"], p["X1"] - p["BEND_R"] + 0.01, 0, zc, fn=24), ent)
    cuts = [horiz, tor, down, ent]
    for xs, yy in p["SCREW"]:
        cuts.append(cyl_z(M3_CLEAR / 2, p["Z0"] - 1, p["Z1"] + 1, xs, yy, fn=24))
        cuts.append(cyl_z(M3_HEAD_D / 2, p["Z0"] - 1, p["Z0"] + 4.0, xs, yy, fn=24))
    return D(m, *cuts)

P46 = dict(RING_IN=(16.5, 11.5), WALL=1.2, RING_H=8.0, TAB_W=6.0, TAB_T=2.0, TAB_L=12.0, EYE_D=3.0)

def p46_tip_pull_clip(p=P46):
    """LOCAL frame = TM1 frame of the centre paddle nose: ring over the seam sleeve (z 3 .. -5), tab down to nail height"""
    ix, iy = p["RING_IN"]
    w = p["WALL"]
    ring = rbox_z(-ix / 2 - w, ix / 2 + w, -iy / 2 - w, iy / 2 + w, -5.0, -5.0 + p["RING_H"], 2.0) - rbox_z(-ix / 2, ix / 2, -iy / 2, iy / 2, -6, 4, 1.0)
    tab = box(-p["TAB_W"] / 2, p["TAB_W"] / 2, -iy / 2 - w - p["TAB_T"], -iy / 2 - w + 0.01, -5.0 - p["TAB_L"], -5.0 + 2.0)
    m = U(ring, tab)
    return D(m, cyl_y(p["EYE_D"] / 2, -iy / 2 - w - p["TAB_T"] - 1, -iy / 2 + 1, 0, -5.0 - p["TAB_L"] + 3.5, fn=16))

P48 = dict(X=120.0, Y=60.0, Z=25.0, SLOT=(11.0, 5.0, 14.0), N=8, SLOT_Y=-8.0, LABEL=(10.0, 6.0, 0.5), LABEL_Y=6.0, R=3.0)

def p48_tip_box(p=P48):
    m = rbox_z(-p["X"] / 2, p["X"] / 2, -p["Y"] / 2, p["Y"] / 2, 0, p["Z"], p["R"])
    sx, sy, sd = p["SLOT"]
    lw, lh, ld = p["LABEL"]
    cuts = []
    pitch = (p["X"] - 2 * 8.0) / (p["N"] - 1)
    for i in range(p["N"]):
        xx = -p["X"] / 2 + 8.0 + i * pitch
        cuts.append(cbox(xx, p["SLOT_Y"], p["Z"] - sd / 2 + 0.5, sx, sy, sd + 1))
        cuts.append(cbox(xx, p["LABEL_Y"], p["Z"], lw, lh, 2 * ld))
    return D(m, *cuts)

# =====================================================================
# registry: (id, file name, builder, material, section-11 bbox (X, Y, Z) in the model's frame, frame note)
# =====================================================================
PARTS = [
    ("P1", "p01_vesa_adapter", p01_vesa_adapter, "PETG", (66, 140, 145), "global"),
    ("P2", "p02_pulley_sheave", p02_pulley_sheave, "PETG", (16, 16, 5), "local (axis Z)"),
    ("P3", "p03_electronics_tray", p03_electronics_tray, "PETG", (32, 36, 92), "global"),
    ("P4", "p04_electronics_tray_lid", p04_tray_lid, "PETG", (2, 36, 92), "global"),
    ("P5", "p05_frame_hinge_knuckle", p05_hinge_knuckle, "PETG", (24, 48, 30), "global"),
    ("P6", "p06_keeper_lever", p06_keeper_lever, "PETG", (12, 30, 60), "global"),
    ("P7", "p07_cord_bar", p07_cord_bar, "PETG", (12, 140, 12), "global"),
    ("P8", "p08_frame_yaw_plate", p08_frame_yaw_plate, "PETG", (70, 70, 6), "global"),
    ("P9", "p09_carrier_yaw_plate", p09_carrier_yaw_plate, "PETG", (70, 70, 6), "global"),
    ("P10", "p10_reset_tab", p10_reset_tab, "PETG", (25, 30, 25), "global"),
    ("P11", "p11_drop_leg_servo", p11_drop_leg_servo, "PETG", (50, 20, 105), "global"),
    ("P12", "p12_drop_leg_idler", p12_drop_leg_idler, "PETG", (50, 20, 105), "global"),
    ("P13", "p13_servo_cradle", p13_servo_cradle, "PETG", (30, 30, 44), "global"),
    ("P14", "p14_servo_strap", p14_servo_strap, "PETG", (30, 4, 10), "global"),
    ("P15", "p15_idler_housing", p15_idler_housing, "PETG", (30, 14, 40), "global"),
    ("P16", "p16_horn_adapter_disc", p16_horn_adapter_disc, "PETG", (24, 3, 24), "global"),
    ("P17", "p17_guard_cap_servo", p17_guard_cap_servo, "PETG", (60, 40, 30), "global"),
    ("P18", "p18_guard_cap_idler", p18_guard_cap_idler, "PETG", (60, 40, 30), "global"),
    ("P19", "p19_yoke_cheek_a", p19_yoke_cheek_a, "PETG", (75, 5, 40), "global"),
    ("P20", "p20_yoke_cheek_b", p20_yoke_cheek_b, "PETG", (75, 5, 40), "global"),
    ("P21", "p21_yoke_crossbar", p21_yoke_crossbar, "PETG", (17, 196, 108), "global"),
    ("P22", "p22_rail_shroud", p22_rail_shroud, "PETG", (16, 34, 50), "global"),
    ("P23", "p23_rail_down_stop", p23_rail_down_stop, "PETG", (12, 20, 8), "global"),
    ("P24", "p24_rail_up_stop", p24_rail_up_stop, "PETG", (12, 20, 8), "global"),
    ("P25", "p25_scale_strip", p25_scale_strip, "PETG", (2, 8, 45), "local (strip along Z)"),
    ("P26", "p26_carriage_riser", p26_carriage_riser, "PETG", (32, 20, 34), "global"),
    ("P27", "p27_trim_cleat", p27_trim_cleat, "PETG", (10, 16, 12), "global"),
    ("P28", "p28_upper_wrist_seat", p28_upper_wrist_seat, "PETG", (44, 44, 39), "global"),
    ("P29", "p29_weight_cap", p29_weight_cap, "PETG", (16, 16, 4), "local"),
    ("P30", "p30_knuckle_plate", p30_knuckle_plate, "PETG", (64, 90, 8), "global"),
    ("P31", "p31_boot_clamp_frame", p31_boot_frame, "PETG", (60, 86, 1.2), "global"),
    ("P32", "p32_palm_tray", p32_palm_tray, "PETG", (52, 169, 28), "global"),
    ("P33", "p33_palm_lid", p33_palm_lid, "PETG", (52, 169, 9), "global"),
    ("P34", "p34_root_clamp_bar", p34_root_clamp_bar, "PETG", (24, 8, 3), "local"),
    ("P35", "p35_boot_cutting_template", p35_boot_template, "PETG", (76, 104, 1), "local"),
    ("P36", "p36_cable_clip", p36_cable_clip, "PETG", (12, 10, 8), "local"),
    ("P37", "p37_control_panel_box", p37_control_panel_box, "PETG", (100, 60, 40), "local"),
    ("P38", "p38_control_panel_lid", p38_control_panel_lid, "PETG", (100, 60, 2), "local"),
    ("P39", "p39_button_housing_half_a", p39_button_housing_half_a, "PETG", (18, 36, 110), "local (half, split plane X=0)"),
    ("P40", "p40_button_housing_half_b", p40_button_housing_half_b, "PETG", (18, 36, 110), "local (half, split plane X=0)"),
    ("P41", "p41_cradle_foot_cup", p41_cradle_foot_cup, "PETG", (40, 40, 12), "local"),
    ("P42", "p42_cradle_tilt_wedge", p42_cradle_tilt_wedge, "PETG", (120, 60, 32), "local"),
    ("P43", "p43_apex_height_gauge", p43_apex_height_gauge, "PETG", (12, 12, 120), "local (stick along Z)"),
    ("P44", "p44_reset_cord_toggle", p44_reset_toggle, "PETG", (40, 14, 14), "local (axis X)"),
    ("P45", "p45_reset_cord_guide", p45_reset_cord_guide, "PETG", (15, 20, 15), "global"),
    ("P46", "p46_tip_pull_clip", p46_tip_pull_clip, "PETG", (18, 13, 20), "local (TM1 frame)"),
    ("P47", "p47_load_cell_filler", p47_load_cell_filler, "PETG", (40, 12, 6), "local"),
    ("P48", "p48_tip_box", p48_tip_box, "PETG", (120, 60, 25), "local"),
]

# =====================================================================
# checks
# =====================================================================
def mesh_min_dist(ma, mb, n=None, search=60.0):
    """exact minimum surface gap between two manifolds (Manifold.min_gap) and their overlap volume (0 if clear)"""
    inter = (ma ^ mb).volume()
    if inter > 1e-6:
        return 0.0, inter
    return float(ma.min_gap(mb, search)), 0.0

def poly_min_dist(cs_a, cs_b, n=400):
    """min distance between the boundaries of two CrossSections (sampled polygon edges)"""
    def pts(cs):
        P = []
        for poly in cs.to_polygons():
            poly = np.asarray(poly)
            for i in range(len(poly)):
                a, b = poly[i], poly[(i + 1) % len(poly)]
                for t in np.linspace(0, 1, 8, endpoint=False):
                    P.append(a + t * (b - a))
        return np.asarray(P)
    A, B = pts(cs_a), pts(cs_b)
    d = np.sqrt(((A[:, None, :] - B[None, :, :]) ** 2).sum(-1))
    return float(d.min())

def run_checks(built):
    lines = []
    def say(s):
        print(s); lines.append(s)
    say("\n=== CHECKS (mechanical.md sections 2, 5.3, 6, 7.1, 8.6, 8.7, 11) ===")
    # 1. P13 pocket vs XL330 body
    body = bx(SERVO)
    pocket = xl330_pocket(0.0, P13["Y0"] + P13["BACK"], P13["BODY_Z0"], open_len=0.0)
    say(f"P13 pocket {XL330_BODY[0]+0.4} x {XL330_BODY[2]+0.4} x {XL330_BODY[1]+0.5} vs XL330 body 20 x 34 x 23 (verified): "
        f"pocket contains body = {(body - pocket).volume() < 1e-6}, clearance per side 0.2 (X,Z), floor gap "
        f"{(SERVO[2] - (P13['Y0'] + P13['BACK'])):.1f} mm; cradle vs body interference volume {(built['P13'] ^ body).volume():.2f} mm3; "
        f"axis 9.5 from the body end: body Z {SERVO[4]}..{SERVO[5]}; back-face M2 holes at X +/-8, Z {P13['BODY_ZC']-15:.1f} / {P13['BODY_ZC']+15:.1f} "
        f"vs the leg screws at {P11['FOOT_INS']}: nearest centres {min(math.hypot(a-c, b-(P13['BODY_ZC']+d)) for a,b in P11['FOOT_INS'] for c,d in XL330_FRAME_HOLES):.1f} mm apart; "
        f"connector windows Y {HORN_Y[0]-XL330_CONN[1]-0.5:.1f}..{HORN_Y[0]-XL330_CONN[0]:.1f} in both side walls")
    # 2. P21 mast inserts vs MGN9 rail holes
    rail_holes = [RAIL[4] + MGN9_RAIL["END"] + i * MGN9_RAIL["PITCH"] for i in range(5)]
    say(f"P21 rail inserts Z {list(P21['RAIL_INS_Z'])} vs MGN9 rail holes (10 + 20k from the rail end at Z {RAIL[4]}) {rail_holes} [VERIFY]: "
        f"match = {all(abs(a-b) < 1e-6 for a, b in zip(P21['RAIL_INS_Z'], rail_holes))}; top insert to mast top at X 40: "
        f"{AXIS_Z + math.sqrt(P21['MAST_ARC_R']**2 - P21['MAST_X0']**2) - (P21['RAIL_INS_Z'][-1] + M3_INS_D/2):.1f} mm of wall")
    # 3. P26 vs MGN9C pattern
    say(f"P26 plate 20 x 34 carries the MGN9C 15 x 10 pattern [VERIFY]: holes at Z {P26['CARR_ZC']}+/-7.5, Y +/-5; plate edge margins "
        f"{(P26['PL_Y'] - 5 - M3_CLEAR/2):.1f} (Y) / {(P26['PL_Z1'] - P26['CARR_ZC'] - 7.5 - M3_CLEAR/2):.1f} (Z) mm; block face at X {CARR[0]}, plate X {P26['PL_X0']}..{P26['PL_X1']}")
    # 4. P28 cone vs P33 cone
    say(f"P28 recess diam {P28['CONE_D0']}/{P28['CONE_D1']} x {P28['CONE_H']} vs P33 cone diam {P33['CONE_D0']}/{P33['CONE_D1']} x {P33['CONE_H']}: "
        f"radial clearance {(P28['CONE_D0']-P33['CONE_D0'])/2:.2f} mm (section 7.1 states these numbers; brief's 0.4 mm is NOT in mechanical.md), axial {P28['CONE_H']-P33['CONE_H']:.2f} mm; "
        f"seat-to-seat interference volume {(built['P28'] ^ built['P33']).volume():.2f} mm3")
    # 5. P30 slot vs paddles (2D at the plate level, free state) and 3D with the tip lead's STLs
    for k, (cx, cy) in NAILS.items():
        sec = cs_crrect(cx, cy, PAD_SEC_X, PAD_SEC_Y, 1.0)
        own = cs_crrect(cx, cy, *(SLOT["CENTRE"] if k == "C" else SLOT["OUTER"]), SLOT["R"])
        d_edge = poly_min_dist(sec, slot_cs() - sec.offset(-0.01, m3.JoinType.Miter, 2.0, FN)) if False else poly_min_dist(sec, slot_cs())
        others = [cs_crrect(ox, oy, PAD_SEC_X, PAD_SEC_Y, 1.0) for kk, (ox, oy) in NAILS.items() if kk != k]
        d_pad = min(poly_min_dist(sec, o) for o in others)
        say(f"P30 slot vs paddle {k} section 22.82 x 17.82 at ({cx:+.0f}, {cy:+.0f}): to slot edge {d_edge:.2f} mm (section 8.7: {'6.0' if k=='C' else '4.5'}), to nearest paddle {d_pad:.2f} mm (section 8.7: 6.2)")
    try:
        pads = []
        for k, (cx, cy) in NAILS.items():
            f = "paddle_with_pocket_riser9.stl" if k == "C" else "paddle_with_pocket.stl"
            pads.append(from_stl(os.path.join(TIPS_STL, f)).translate([cx, cy, POCKET_MOUTH_Z[k]]))
        pad_u = U(*pads)
        for pid in ("P30", "P31", "P32", "P33"):
            v = (built[pid] ^ pad_u).volume()
            dmin, _ = mesh_min_dist(built[pid], pad_u)
            say(f"{pid} vs the three paddles (tip lead STLs placed at the section 8.1 nail positions, free state): interference {v:.2f} mm3, min gap {dmin:.2f} mm")
        for k, pm in zip(NAILS, pads):
            others = [q for q in pads if q is not pm]
            say(f"paddle {k} vs the other paddles: min gap {min(mesh_min_dist(pm, q)[0] for q in others):.2f} mm (section 8.7 table: 6.2 at the plate, free state)")
    except Exception as e:
        say(f"(paddle STLs not available for the 3D check: {e})")
    # 6. P32 root block slots vs leaves
    say(f"P32 root-block leaf slots {P32['SLOT_W']} x {P32['SLOT_H']} vs leaf 12.7 x 0.30: clearance 0.10 per side (W), 0.70 (H, bar sets the height); "
        f"clamp window {P32['WIN_X']} x {P32['WIN_Y']} vs P34 bar 24 x 8: 0.1 / 0.2; P34 groove 12.9 x 0.25 < leaf 0.30 so the bar presses the leaf")
    # 7. P39 hole vs 30 mm arcade button
    say(f"P39 button hole diam {P39['BTN_HOLE']} (ream to 30.0) vs the uxcell 30 mm snap-in button (body 33 max diam, 26 tall, verified): "
        f"cup ID = {P39['CUP_D'] - 2*P39['RIM_WALL']:.1f} mm vs body 33 -> the button body does NOT fit inside the cup below the deck (see CONFLICTS)")
    # 8. P1 ears vs P5 knuckle
    say(f"P1 ears Y +/-{P1['EAR_Y0']}..{P1['EAR_Y1']} vs P5 knuckle Y +/-{P5['Y']/2}: {P1['EAR_Y0'] - P5['Y']/2:.1f} mm per side for a 0.5 mm PTFE washer; "
        f"interference volume {(built['P1'] ^ built['P5']).volume():.2f} mm3; pin bores coaxial at (X {PIN_X}, Z {PIN_Z})")
    # 9. static pairwise interference of the installed (global-frame) parts
    say("\n--- static assembly interference (installed parts, volume of overlap > 0.5 mm3 listed) ---")
    glob = [pid for pid, f, b, mat, exp, fr in PARTS if fr == "global"]
    bad = 0
    for i, a in enumerate(glob):
        for b_ in glob[i + 1:]:
            v = (built[a] ^ built[b_]).volume()
            if v > 0.5:
                say(f"  OVERLAP {a} x {b_}: {v:.1f} mm3")
                bad += 1
    say(f"  {bad} overlapping pairs" if bad else "  none")
    # bought parts vs printed
    bought = {"post": bx(POST), "spine": bx(SPINE), "beam": bx(BEAM), "servo": body, "rail": bx(RAIL), "carriage": bx(CARR),
              "magnet": cyl_x(MAG["r"], MAG["x0"], MAG["x1"], 0, MAG["z"]), "horn": cyl_y(HORN_R, HORN_Y[0], HORN_Y[1], AXIS_X, AXIS_Z)}
    for bn, bm in bought.items():
        for a in glob:
            v = (built[a] ^ bm).volume()
            if v > 0.5 and not (a == "P14" and bn == "servo"):
                say(f"  OVERLAP {a} x bought {bn}: {v:.1f} mm3")
            elif a == "P14" and bn == "servo":
                say(f"  P14 strap pad x servo: {v:.1f} mm3 = the intended 0.3 mm interference pad (section 11)")
    # 10. swept volumes (section 2 a-e): arm +/-32 deg, float at the up-stop, fail-safe lift 25 deg
    say("\n--- swept-volume checks (section 2; >= 8 mm clearance asked) ---")
    arm_ids = ["P19", "P20", "P21", "P22", "P23", "P24", "P26", "P27", "P28", "P30", "P31", "P32", "P33"]
    carr = bx(CARR) - bx(RAIL)
    arm = U(*[built[i] for i in arm_ids], bx(RAIL), carr)
    hand_float = U(built["P26"], built["P28"], built["P30"], built["P31"], built["P32"], built["P33"], carr)
    fixed_ids = ["P9", "P11", "P12", "P13", "P15", "P17", "P18"]
    fixed = U(*[built[i] for i in fixed_ids], bx(BEAM))
    def culprits(moving_ids, mover, fixed_ids_, fixed_parts):
        out = []
        for a_ in moving_ids:
            ma = mover(built[a_])
            for b_ in fixed_ids_:
                v = (ma ^ fixed_parts[b_]).volume()
                if v > 0.5:
                    out.append(f"{a_}x{b_}:{v:.0f}")
        return ", ".join(out) if out else "-"
    fixed_parts = {i: built[i] for i in fixed_ids}
    fixed_parts["beam"] = bx(BEAM)
    for ang in (-32, -31, 0, 31, 32):
        mv = lambda m_, ang=ang: rot_about(m_, "y", -ang, (AXIS_X, 0, AXIS_Z))   # +ang = hand toward +X
        a = mv(arm)
        d, v = mesh_min_dist(a, fixed)
        say(f"  arm at {ang:+d} deg vs carrier/legs/cradle/housing/caps: min gap {d:.1f} mm, overlap {v:.1f} mm3 "
            f"[{culprits(arm_ids, mv, list(fixed_parts), fixed_parts)}]{'  (stop lug on the TPU bumper: intended contact)' if abs(ang) == 32 else ''}")
    for ang in (-28, 28):
        mv = lambda m_, ang=ang: rot_about(m_, "y", -ang, (AXIS_X, 0, AXIS_Z))
        a = mv(U(arm, hand_float.translate([0, 0, FLOAT_TRAVEL])))
        fp2 = dict(fixed_parts, P8=built["P8"], spine=bx(SPINE))
        d, v = mesh_min_dist(a, U(fixed, built["P8"], bx(SPINE)))
        float_ids = ["P26", "P28", "P30", "P31", "P32", "P33"]
        up = lambda m_, mv=mv: mv(m_.translate([0, 0, FLOAT_TRAVEL]))
        say(f"  arm at {ang:+d} deg with the float at its up-stop (+{FLOAT_TRAVEL}) vs carrier + yaw plates + spine: min gap {d:.1f} mm, overlap {v:.1f} mm3 "
            f"[{culprits(arm_ids, mv, list(fp2), fp2)} | float: {culprits(float_ids, up, list(fp2), fp2)}]")
    # self-check of the float travel: lifted float vs the arm-fixed parts (up-stop, shroud, mast)
    v = (hand_float.translate([0, 0, FLOAT_TRAVEL]) ^ U(built["P21"], built["P22"], built["P24"], built["P27"], bx(RAIL))).volume()
    fl_parts = {"P26": built["P26"], "P28": built["P28"], "P30": built["P30"], "P31": built["P31"], "P32": built["P32"], "P33": built["P33"], "carr": carr}
    st_parts = {"P21": built["P21"], "P22": built["P22"], "P24": built["P24"], "P27": built["P27"], "rail": bx(RAIL)}
    pairs = [f"{a_}x{b_}:{(fl_parts[a_].translate([0, 0, FLOAT_TRAVEL]) ^ st_parts[b_]).volume():.0f}" for a_ in fl_parts for b_ in st_parts
             if (fl_parts[a_].translate([0, 0, FLOAT_TRAVEL]) ^ st_parts[b_]).volume() > 0.5]
    say(f"  float at its up-stop vs mast/shroud/up-stop/cleat/rail: overlap {v:.1f} mm3 [{', '.join(pairs) or '-'}] (carriage top meets the TPU pad: {CARR[5] + FLOAT_TRAVEL:.0f} vs pad {P24['Z0'] - P24['PAD_T'] + P24['PAD_RECESS']:.0f})")
    top = max(to_trimesh(rot_about(U(arm, hand_float.translate([0, 0, FLOAT_TRAVEL])), "y", -ang, (AXIS_X, 0, AXIS_Z))).bounds[1][2] for ang in (-32, -24, -16, -8, 0, 8, 16, 24, 32))
    rmax = {}
    for pid_ in arm_ids + ["rail", "carr"]:
        mm_ = {"rail": bx(RAIL), "carr": carr}.get(pid_, built.get(pid_))
        if pid_ in ("P26", "P28", "P30", "P31", "P32", "P33", "carr"):
            mm_ = mm_.translate([0, 0, FLOAT_TRAVEL])
        v_ = np.asarray(mm_.to_mesh().vert_properties)[:, :3]
        rmax[pid_] = float(np.sqrt((v_[:, 0] - AXIS_X) ** 2 + (v_[:, 2] - AXIS_Z) ** 2).max())
    worst = sorted(rmax.items(), key=lambda kv: -kv[1])[:3]
    say(f"  highest arm-mounted point over +/-32 deg with the float up: Z {top:.1f} (section 2c: < 175; yaw plates from 184); "
        f"largest radii about the elbow axis: " + ", ".join(f"{k} {v:.1f}" for k, v in worst) + " (section 2c asks <= 91)")
    # fail-safe lift: everything forward of the hinge rotates 25 deg about the pin
    module = U(arm, fixed, built["P5"], built["P6"], built["P7"], built["P8"], built["P10"], bx(POST), bx(SPINE))
    lifted = rot_about(module, "y", -25, (PIN_X, 0, PIN_Z))   # R_y(-25): hand up 33 and forward 28, post top backward (section 4.1)
    adapter = U(built["P1"], built["P3"], built["P4"], built["P45"], bought["magnet"])
    d, v = mesh_min_dist(lifted, adapter)
    adp = {"P1": built["P1"], "P3": built["P3"], "P4": built["P4"], "P45": built["P45"], "magnet": bought["magnet"]}
    mod_ids = ["P5", "P6", "P7", "P8", "P9", "P10", "P11", "P12", "P19", "P20", "P21"]
    lift = lambda m_: rot_about(m_, "y", -25, (PIN_X, 0, PIN_Z))
    extra = {"post": bx(POST), "spine": bx(SPINE), "beam": bx(BEAM)}
    cul = culprits(mod_ids, lift, list(adp), adp)
    cul2 = ", ".join(f"{k}x{b}:{(lift(mm) ^ adp[b]).volume():.0f}" for k, mm in extra.items() for b in adp if (lift(mm) ^ adp[b]).volume() > 0.5)
    say(f"  module lifted 25 deg about the hinge vs adapter + tray + magnet: min gap {d:.1f} mm, overlap {v:.1f} mm3 [{cul}; {cul2 or '-'}]")
    d, v = mesh_min_dist(module, adapter)
    say(f"  module latched vs adapter + tray + magnet: min gap {d:.1f} mm, overlap {v:.1f} mm3 (keeper on the magnet face is the intended contact)")
    with open(os.path.join(OUT, "checks.txt"), "w") as f:
        f.write("\n".join(lines) + "\n")

# =====================================================================
# main
# =====================================================================
def main(argv):
    only = None
    for a in argv:
        if a.startswith("--only"):
            only = set(a.split("=", 1)[1].split(","))
    do_checks = "--no-checks" not in argv
    built, rows, fails = {}, [], 0
    for pid, fname, builder, mat, exp, frame in PARTS:
        if only and pid not in only:
            continue
        try:
            m = builder()
        except Exception as e:
            print(f"{pid:4s} {fname:32s} BUILD ERROR: {e!r}")
            fails += 1
            continue
        built[pid] = m
        tm = to_trimesh(m)
        tm.export(os.path.join(OUT, fname + ".stl"))
        bb = m.bounding_box()
        size = [bb[i + 3] - bb[i] for i in range(3)]
        vol = m.volume()
        comps = m.decompose()
        ncomp = sum(1 for c in comps if c.volume() > 0)          # sealed cavities (negative volume) are allowed
        wt = bool(tm.is_watertight and tm.is_volume and ncomp == 1 and m.status() == m3.Error.NoError)
        if ncomp != 1:
            print(f"{pid}: {ncomp} disconnected solid pieces")
        if len(comps) != ncomp:
            print(f"{pid}: {len(comps) - ncomp} sealed internal cavity (box beam / closed shell): fine for printing")
        match = all(abs(s - e) <= 1.0 for s, e in zip(size, exp))
        rows.append((pid, fname, size, vol, wt, match, exp, mat, frame, bb))
        if not wt:
            fails += 1
    print("\n=== PARTS ===")
    print(f"{'id':4s} {'file':32s} {'bbox X x Y x Z (mm)':26s} {'volume mm3':>11s} {'mass g':>7s} {'wt':3s} {'s11 bbox':18s} {'match':5s} frame")
    for pid, fname, size, vol, wt, match, exp, mat, frame, bb in rows:
        print(f"{pid:4s} {fname:32s} {size[0]:6.1f} x {size[1]:6.1f} x {size[2]:6.1f}   {vol:11.0f} {vol*MATS[mat]/1000:7.1f} {'yes' if wt else 'NO ':3s} "
              f"{exp[0]:>5g} x {exp[1]:>5g} x {exp[2]:>5g} {'yes' if match else 'NO':5s} {frame}")
    print(f"\n{sum(1 for r in rows if r[4])}/{len(rows)} watertight, {sum(1 for r in rows if r[5])}/{len(rows)} inside the section-11 bounding box (+/-1 mm)")
    if do_checks and not only:
        run_checks(built)
    return 1 if fails else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
