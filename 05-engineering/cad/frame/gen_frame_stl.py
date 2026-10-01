#!/usr/bin/env python
"""
gen_frame_stl.py - STL generator for the SP1 module frame, float and hand parts
(PROJECT SCRATCH, 05-engineering/cad/frame, CAD agent, 2026-10-01)

Generates into ./stl/ one STL per printed piece P1-P48 of mechanical.md section 11
(the paddles, paddle clamp bars and seam sleeves are the tip lead's, in ../tips/),
plus three small TPU pads and the P15S idler spacer that section 11 implies but does
not number (see CONFLICTS.md).

THE .scad FILES ARE THE SOURCE OF TRUTH.  Every dimension below is copied from
sp1_frame_lib.scad and the pNN_*.scad files and must be kept in sync; constant names
match the SCAD names.  No OpenSCAD binary exists on the build machine, so this script
rebuilds the same solids with manifold3d (CrossSection / Manifold booleans, hulls,
extrusions) and exports through trimesh.

FRAME: the global assembly frame of mechanical.md section 2 (DESIGN-FREEZE-ADDENDUM-1
D9): Z up, X = stroke, Y = across; origin O = centre nail edge, arm at 0 deg, float on
its down-stop, module latched.  Every part that sits on the module is written IN ITS
INSTALLED POSITION, so the STLs load together as the assembly; rotate in the slicer per
README.md.  Desk-side parts (P35, P37-P44, P46, P48) use a local frame (README).

Besides the STLs the script runs the section 2 / 8.7 / 13 checks on the solids:
pairwise interference in the static assembly, the arm swept through +/-32 deg, the
float swept and lifted to its up-stop, the fail-safe lift of the whole module to the
25 deg up-stop, and the paddle-to-knuckle-plate gaps at 0, nominal and 5 mm of leaf
travel (with the roll pre-tilt).  Results go to stdout and stl/checks.txt.

Run (from this folder):  <cadenv>/bin/python gen_frame_stl.py [--no-checks]
Exit code 0 only if every mesh is watertight and inside its expected bounding box.
"""
import math, os, sys
import numpy as np
import trimesh
import manifold3d as m3
from manifold3d import Manifold, CrossSection

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "stl")
os.makedirs(OUT, exist_ok=True)
FN = 48                      # circle segments ($fn in the SCAD)

# =====================================================================
# sp1_frame_lib.scad constants (shared)
# =====================================================================
# --- fasteners / inserts (mechanical.md section 11 header) ---
M2_CLEAR, M3_CLEAR, M4_CLEAR, M5_CLEAR = 2.4, 3.4, 4.5, 5.5
M2_PILOT, M3_PILOT = 1.8, 2.6           # thread-forming pilots in PETG
M2_INS_D, M2_INS_L = 3.2, 3.0           # brass heat-set M2: 3.2 hole, 3 long
M3_INS_D, M3_INS_L = 4.0, 4.0           # brass heat-set M3: 4.0 hole, 4 long
M4_INS_D, M4_INS_L = 5.6, 6.0           # brass heat-set M4 x 6 [VERIFY hole on the insert kit]
M3_HEAD_D, M3_HEAD_H = 6.0, 3.2         # socket head M3 (counterbores)
M5_HEAD_D, M5_HEAD_H = 9.5, 5.0
PIN_BORE = 6.3                          # M6 hinge pin, reamed
EXT, EXT_SOCK = 20.0, 20.2              # 2020 extrusion and its printed socket
# --- global geometry (mechanical.md section 2) ---
AXIS_X, AXIS_Z = 0.0, 84.0              # elbow axis, parallel to Y
PIN_X, PIN_Z = -60.0, 84.0              # fail-safe hinge pin, parallel to Y
SCALP_C, SCALP_R = (0.0, 0.0, -86.0), 90.0
KP_C_Z = -52.5                          # knuckle-plate sphere centre z (underside R 90 at z 37.5)
KP_R, KP_T = 90.0, 1.6
BOOT_T, P31_T = 0.25, 1.2
# --- bought-part reference solids (positions) ---
POST = (-70, -50, -10, 10, 94, 216)     # 2020, 122 mm (see CONFLICTS C-F1)
SPINE = (-50, 30, -10, 10, 196, 216)    # 2020, 80 mm
BEAM = (-35, -15, -135, 135, 164, 184)  # 2020, 270 mm elbow-carrier beam
YAW_X = -25.0
SERVO = (-10, 10, -127, -104, 74, 108)  # XL330 body [VERIFY]
HORN_R, HORN_Y = 10.0, (-104, -101)     # XL330 horn [VERIFY]
RAIL = (33.5, 40, -4.5, 4.5, 68, 168)   # MGN9 rail 100 mm
CARR = (30, 40, -10, 10, 74, 103)       # MGN9C block at the down-stop
MAG = dict(x0=-81.0, x1=-66.0, z=34.0, r=10.0)   # Adafruit 3872 P20/15
FLOAT_TRAVEL = 28.0
MATS = {"PETG": 1.27, "TPU": 1.21}      # g/cm3

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

def cyl_z(r, z0, z1, x=0.0, y=0.0, r2=None, fn=FN):
    return Manifold.cylinder(z1 - z0, r, r if r2 is None else r2, fn).translate([x, y, z0])

def cyl_y(r, y0, y1, x=0.0, z=0.0, fn=FN):
    return cyl_z(r, 0, y1 - y0, fn=fn).transform(MAP_Y).translate([x, y0, z])

def cyl_x(r, x0, x1, y=0.0, z=0.0, fn=FN):
    return cyl_z(r, 0, x1 - x0, fn=fn).transform(MAP_X).translate([x0, y, z])

def sphere(r, c, fn=FN):
    return Manifold.sphere(r, fn).translate(list(c))

# (u, v, w) of an extruded CrossSection -> global axes
MAP_Y = [[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0]]   # profile in (x, z), extruded along +Y (mirror: manifold fixes winding)
MAP_X = [[0, 0, 1, 0], [1, 0, 0, 0], [0, 1, 0, 0]]   # profile in (y, z), extruded along +X

def cs_poly(pts):
    return CrossSection([[(float(a), float(b)) for a, b in pts]])

def cs_rect(u0, u1, v0, v1):
    return cs_poly([(u0, v0), (u1, v0), (u1, v1), (u0, v1)])

def cs_rrect(u0, u1, v0, v1, r):
    """rounded rectangle (offset of a shrunken rectangle)"""
    if r <= 0:
        return cs_rect(u0, u1, v0, v1)
    return cs_rect(u0 + r, u1 - r, v0 + r, v1 - r).offset(r, m3.JoinType.Round, 2.0, FN)

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

def ins_z(d, depth, x, y, ztop, down=True):
    """blind insert/pilot hole: from face z=ztop going down (or up when down=False)"""
    return cyl_z(d / 2, ztop - depth, ztop + 0.01, x, y, fn=24) if down else cyl_z(d / 2, ztop - 0.01, ztop + depth, x, y, fn=24)

def ins_y(d, depth, x, z, yface, toward=+1):
    return cyl_y(d / 2, yface - 0.01, yface + depth, x, z, fn=24) if toward > 0 else cyl_y(d / 2, yface - depth, yface + 0.01, x, z, fn=24)

def ins_x(d, depth, y, z, xface, toward=+1):
    return cyl_x(d / 2, xface - 0.01, xface + depth, y, z, fn=24) if toward > 0 else cyl_x(d / 2, xface - depth, xface + 0.01, y, z, fn=24)

def sph_shell(rc_z, r_in, r_out, fn=160):
    return sphere(r_out, (0, 0, rc_z), fn) - sphere(r_in, (0, 0, rc_z), fn)

def to_trimesh(m):
    mm = m.to_mesh()
    return trimesh.Trimesh(vertices=np.asarray(mm.vert_properties)[:, :3], faces=np.asarray(mm.tri_verts), process=True)

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
          EDGE_RIB_Y=66.0)

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
    return D(m, *cuts)

# =====================================================================
# p02_p07_hinge_parts.scad  (P2 pulley sheave, P5 knuckle, P6 keeper lever, P7 cord bar,
#                            P10 reset tab, P44 reset toggle, P45 reset cord guide)
# =====================================================================
P2 = dict(OD=16.0, W=5.0, GROOVE_DEPTH=1.5, GROOVE_ANGLE=90.0, BORE=10.0, BRG_W=4.0, LIP_D=8.0)

def p02_pulley_sheave(p=P2, placed=True):
    """axis along Y. Profile revolved: V groove for the 1 mm cord, 10 mm bore for a 623ZZ, 1 mm lip"""
    ro, w, gd = p["OD"] / 2, p["W"], p["GROOVE_DEPTH"]
    prof = cs_poly([(p["LIP_D"] / 2, 0), (ro, 0), (ro, w / 2 - gd), (ro - gd, w / 2), (ro, w / 2 + gd), (ro, w),
                    (p["BORE"] / 2, w), (p["BORE"] / 2, w - p["BRG_W"]), (p["LIP_D"] / 2, w - p["BRG_W"])])
    m = prof.revolve(FN)                       # revolved about local Y (CrossSection v axis -> z)
    # CrossSection.revolve revolves the (x, y) profile about the y axis into a solid along z: map to axis Y
    m = m.transform(MAP_Y)                      # axis now along Y, centre at origin plane y in [0, w]
    if placed:
        m = m.translate([P1["PULLEY_X"], P1["PULLEY_Y"] - w / 2, P1["PULLEY_ZC"]])
    return m

P5 = dict(X=24.0, Y=48.0, Z0=76.0, Z1=106.0, SOCK_D=12.0, SCREW_Z=101.0, SCREW_CB_D=9.5, SCREW_CB_DEPTH=6.0)

def p05_hinge_knuckle(p=P5):
    hx, hy = p["X"] / 2, p["Y"] / 2
    m = box(PIN_X - hx, PIN_X + hx, -hy, hy, p["Z0"], p["Z1"])
    s = EXT_SOCK / 2
    cuts = [box(PIN_X - s, PIN_X + s, -s, s, p["Z1"] - p["SOCK_D"], p["Z1"] + 1),
            cyl_y(PIN_BORE / 2, -hy - 1, hy + 1, PIN_X, PIN_Z, fn=32),
            cyl_y(M5_CLEAR / 2, -hy - 1, hy + 1, PIN_X, p["SCREW_Z"], fn=24)]
    for sgn in (-1, 1):
        y0, y1 = sorted((sgn * hy, sgn * (hy - p["SCREW_CB_DEPTH"])))
        cuts.append(cyl_y(p["SCREW_CB_D"] / 2, y0 - (0.01 if sgn < 0 else 0), y1 + (0.01 if sgn > 0 else 0), PIN_X, p["SCREW_Z"], fn=32))
    return D(m, *cuts)

P6 = dict(FOOT_X0=-66.0, FOOT_X1=-54.0, FOOT_Y=30.0, FOOT_Z0=19.0, FOOT_Z1=49.0, KEEPER=25.0, KEEPER_T=3.0,
          BRIDGE_Z1=57.0, UP_X0=-48.0, UP_X1=-40.0, UP_Y=20.0, UP_Z1=134.0, UP_STEP_Z=106.0,
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
    cuts = [cyl_y(M5_CLEAR / 2, -20, 20, PIN_X, (z0 + z1) / 2, fn=24)]
    for s in (-1, 1):
        cuts.append(cyl_z(p["EYE_D"] / 2, z0 - 1, z1 + 1, (p["ARM_X0"] + p["ARM_X1"]) / 2, s * p["CORD_Y"], fn=16))
    return D(m, *cuts)

P10 = dict(X0=20.0, X1=45.0, Y=30.0, Z0=194.0, Z1=219.0, SOCK_DEPTH=10.0, R=5.0)

def p10_reset_tab(p=P10):
    hy = p["Y"] / 2
    body = ext_x(cs_rrect(-hy, hy, p["Z0"], p["Z1"], p["R"]), p["X0"], p["X1"])
    # round the front end in plan too
    body = body ^ ext_z(cs_rrect(p["X0"] - p["R"], p["X1"], -hy, hy, p["R"]), p["Z0"] - 1, p["Z1"] + 1)
    s = EXT_SOCK / 2
    cut = box(p["X0"] - 1, p["X0"] + p["SOCK_DEPTH"], -s, s, 206 - s, 206 + s)
    return D(body, cut)

P44 = dict(D=14.0, L=40.0, BORE=2.5, KNOT_D=6.0, KNOT_H=4.0, CH=1.0)

def p44_reset_toggle(p=P44):
    """LOCAL frame: axis along X, centred at the origin"""
    r, L, c = p["D"] / 2, p["L"], p["CH"]
    m = U(cyl_x(r, -L / 2 + c, L / 2 - c),
          hull(cyl_x(r - c, -L / 2, -L / 2 + 0.01), cyl_x(r, -L / 2 + c, -L / 2 + c + 0.01)),
          hull(cyl_x(r, L / 2 - c - 0.01, L / 2 - c), cyl_x(r - c, L / 2 - 0.01, L / 2)))
    return D(m, cyl_z(p["BORE"] / 2, -r - 1, r + 1, fn=16), cyl_z(p["KNOT_D"] / 2, r - p["KNOT_H"], r + 1, fn=24))

P45 = dict(X0=-95.0, X1=-80.0, Y=20.0, Z0=5.0, Z1=20.0, CH_D=3.0, CH_Z=12.0, BEND_R=3.0, SCREW_X=(-91.0, -84.0))

def p45_reset_cord_guide(p=P45):
    hy = p["Y"] / 2
    m = box(p["X0"], p["X1"], -hy, hy, p["Z0"], p["Z1"])
    r, xb, zc = p["CH_D"] / 2, -88.0 + 0.0, p["CH_Z"]
    # channel: horizontal from the +X face to the bend, R 3 bend (torus quarter), down out of the bottom
    horiz = cyl_x(r, xb, p["X1"] + 1, 0, zc, fn=24)
    bend_c = (xb, 0, zc - p["BEND_R"])
    tor = (CrossSection.circle(r, 24).translate([p["BEND_R"], 0]).revolve(48, 90.0)
           .transform(MAP_Y).rotate([0, 0, 0]))
    # revolve gives a quarter torus in the local x-z plane (about local y -> global Y after MAP_Y)
    tor = rot_about(tor, "y", 180, (0, 0, 0)).translate(list(bend_c))
    down = cyl_z(r, p["Z0"] - 1, zc - p["BEND_R"], xb - p["BEND_R"], 0, fn=24)
    ent = cyl_x(r + p["BEND_R"], p["X1"] - 0.6, p["X1"] + 1, 0, zc, fn=24)   # R 3 entry (flared)
    ent = hull(cyl_x(r, p["X1"] - p["BEND_R"], p["X1"] - p["BEND_R"] + 0.01, 0, zc, fn=24), ent)
    cuts = [horiz, tor, down, ent]
    for xs in p["SCREW_X"]:
        cuts.append(cyl_z(M3_CLEAR / 2, p["Z0"] - 1, p["Z1"] + 1, xs, 6.0, fn=24))
        cuts.append(cyl_z(M3_HEAD_D / 2, p["Z0"] - 1, p["Z0"] + 4.0, xs, 6.0, fn=24))
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

P4 = dict(T=2.0, VENT=(2.0, 20.0), VENT_ZS=(112.0, 134.0), VENT_DY=13.0, LABEL=(20.0, 30.0, 0.6), LABEL_ZC=170.0,
          WAGO_POCKET=(13.6, 20.6, 8.6), WAGO_ZC=118.0)

def p04_tray_lid(p=P4, t=P3):
    x0 = t["X1"]
    yc = (t["Y0"] + t["Y1"]) / 2
    m = box(x0, x0 + p["T"], t["Y0"], t["Y1"], t["Z0"], t["Z1"])
    # Wago 221-413 cradle on the inside face [VERIFY 13.1 x 20.3 x 8.1 body]
    wy, wz, wx = p["WAGO_POCKET"]
    cr = box(x0 - wx - 1.2, x0 + 0.01, yc - wy / 2 - 1.2, yc + wy / 2 + 1.2, p["WAGO_ZC"] - wz / 2 - 1.2, p["WAGO_ZC"] + wz / 2 + 1.2)
    cr = cr - box(x0 - wx - 2, x0 + 0.02, yc - wy / 2, yc + wy / 2, p["WAGO_ZC"] - wz / 2, p["WAGO_ZC"] + wz / 2 + 5)
    m = U(m, cr)
    cuts = []
    for yy, zz in t["LID_INS"]:
        cuts.append(cyl_x(M3_CLEAR / 2, x0 - 1, x0 + p["T"] + 1, yy, zz, fn=24))
    vw, vl = p["VENT"]          # 2 x 20 vent slots, two columns
    for zz in p["VENT_ZS"]:
        for dy in (-p["VENT_DY"], p["VENT_DY"]):
            cuts.append(box(x0 - 1, x0 + p["T"] + 1, yc + dy - vw / 2, yc + dy + vw / 2, zz, zz + vl))
    lw, lh, ld = p["LABEL"]
    cuts.append(box(x0 + p["T"] - ld, x0 + p["T"] + 1, yc - lw / 2, yc + lw / 2, p["LABEL_ZC"] - lh / 2, p["LABEL_ZC"] + lh / 2))
    return D(m, *cuts)
