#!/usr/bin/env python
"""
gen_tips_stl.py - convenience STL generator for SP1 tips (PROJECT SCRATCH)

Generates into ./stl/ :
  tips      tip_W, tip_B45, tip_B45_12, tip_A45 (slot carrier), tip_H_ball,
            tip_E_carrier, tip_E_pad (TPU 90A), tip_E_blade (blank / template),
            tip_P_carrier
  holder    paddle_with_pocket (RISER 0: SP1 outer paddles x 2, and the wand),
            paddle_with_pocket_riser9 (RISER 9: SP1 centre paddle x 1),
            paddle_clamp_bar, tm1_seam_sleeve (TPU 90A)
  wand      hand_wand_handle, hand_wand_clamp_bar
using trimesh booleans (manifold3d engine) and manifold3d convex hulls (no scipy needed).

THE .scad FILES ARE THE SOURCE OF TRUTH.  Every dimension below is copied from
tm1_tang_lib.scad / tip_*.scad / paddle_with_pocket.scad / hand_wand_handle.scad and
must be kept in sync; constant and argument names match the SCAD parameters.
Units: mm.  Frame: +Z into the holder pocket, -Z toward the scalp, X = stroke, Y = across.
Meshes are written in the MODEL frame (not the print orientation; see README.md).

Run (from this folder):  <cadenv>/bin/python gen_tips_stl.py
Exit code 0 only if every mesh is watertight and inside its expected bounding box.
"""
import math, os, sys
import numpy as np
import trimesh
import manifold3d
from trimesh import transformations as tf

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "stl")
os.makedirs(OUT, exist_ok=True)
SECT = 48  # cylinder sections (= TM1_FN)

# ---------------- tm1_tang_lib.scad constants ----------------
TM1_TANG_X, TM1_TANG_Y, TM1_TANG_L, TM1_KEY, TM1_END_CH = 10.0, 4.0, 12.0, 2.0, 0.5
TM1_SLUG_X, TM1_SLUG_T, TM1_SLUG_CLEAR = 6.0, 1.0, 0.15
TM1_SH_X, TM1_SH_Y, TM1_SH_R, TM1_SH_TOP, TM1_SH_BOT = 14.0, 9.0, 1.0, -2.5, -5.5
TM1_POCKET_CLEAR, TM1_POCKET_DEPTH, TM1_MOUTH_CH = 0.15, 12.5, 0.6
TM1_MAG_D, TM1_MAG_H, TM1_MAG_CLEAR, TM1_MAG_TOP = 6.0, 2.0, 0.1, 11.9

# ---------------- mesh helpers ----------------
def to_trimesh(M):
    m = M.to_mesh()
    return trimesh.Trimesh(vertices=np.asarray(m.vert_properties)[:, :3], faces=np.asarray(m.tri_verts), process=True)

def hull_pts(pts):
    return to_trimesh(manifold3d.Manifold.hull_points(np.asarray(pts, dtype=float)))

def hull(*meshes):
    return hull_pts(np.vstack([m.vertices for m in meshes]))

def prism_xy(pts, z0, z1):
    """convex 2D polygon (XY) between z0 and z1"""
    pts = np.asarray(pts, dtype=float)
    return hull_pts(np.vstack([np.column_stack([pts, np.full(len(pts), z0)]),
                               np.column_stack([pts, np.full(len(pts), z1)])]))

def prism_xz(pts, length):
    """convex 2D polygon given in (x, z), extruded along Y, centred (= rotate([90,0,0]) linear_extrude(center=true))"""
    pts = np.asarray(pts, dtype=float)
    a = np.column_stack([pts[:, 0], np.full(len(pts), -length / 2), pts[:, 1]])
    b = np.column_stack([pts[:, 0], np.full(len(pts), length / 2), pts[:, 1]])
    return hull_pts(np.vstack([a, b]))

def tang_profile_pts(c=0.0):
    hx, hy = TM1_TANG_X / 2 + c, TM1_TANG_Y / 2 + c
    k = TM1_KEY + c * (2 - math.sqrt(2))
    return [[-hx, -hy], [hx, -hy], [hx, hy - k], [hx - k, hy], [-hx, hy]]

def tang_prism(c, z0, z1):
    return prism_xy(tang_profile_pts(c), z0, z1)

def zcyl(r, z0, z1, x=0.0, y=0.0, sections=SECT):
    m = trimesh.creation.cylinder(radius=r, height=z1 - z0, sections=sections)
    m.apply_translation([x, y, (z0 + z1) / 2])
    return m

def rrect_pts(x, y, r, n=12):
    """outline of tm1_rrect(x, y, r) (rounded rectangle, centred)"""
    pts = []
    for cx, cy, a0 in ((x / 2 - r, y / 2 - r, 0), (-x / 2 + r, y / 2 - r, 90),
                       (-x / 2 + r, -y / 2 + r, 180), (x / 2 - r, -y / 2 + r, 270)):
        for i in range(n + 1):
            a = math.radians(a0 + 90 * i / n)
            pts.append([cx + r * math.cos(a), cy + r * math.sin(a)])
    return pts

def rrect_prism(x, y, r, z0, z1):
    return prism_xy(rrect_pts(x, y, r), z0, z1)

def slab(x, y, r, z, h=0.02):
    return rrect_prism(x, y, r, z - h / 2, z + h / 2)

def band_slab(z=TM1_SH_BOT, h=0.02):
    return slab(TM1_SH_X, TM1_SH_Y, TM1_SH_R, z, h)

def ycyl(r, length, x, z, sections=SECT):
    m = trimesh.creation.cylinder(radius=r, height=length, sections=sections)
    m.apply_transform(tf.rotation_matrix(math.radians(90), [1, 0, 0]))
    m.apply_translation([x, 0, z])
    return m

def xcyl(r, length, z, sections=180):
    m = trimesh.creation.cylinder(radius=r, height=length, sections=sections)
    m.apply_transform(tf.rotation_matrix(math.radians(90), [0, 1, 0]))
    m.apply_translation([0, 0, z])
    return m

def box(x, y, z, cx=0.0, cy=0.0, cz=0.0):
    m = trimesh.creation.box(extents=[x, y, z])
    m.apply_translation([cx, cy, cz])
    return m

def crown(cr=9.0, z_apex=-12.5):
    return xcyl(cr, 80, z_apex + cr)

def below(z, size=100.0):
    """half-space z <= z (as a big box)"""
    return box(size, size, size, cz=z - size / 2)

def ball(r, center, sections=SECT):
    m = trimesh.creation.uv_sphere(radius=r, count=[sections // 2, sections])
    m.apply_translation(center)
    return m

def diff_all(m, cuts):
    for c in cuts:
        m = m.difference(c)
    return m

# ---------------- TM1 tang + shoulder (tm1_tip_base) ----------------
def tm1_tang():
    body = hull(tang_prism(0, 0, TM1_TANG_L - TM1_END_CH),
                tang_prism(-TM1_END_CH, TM1_TANG_L - 0.01, TM1_TANG_L))
    nh = TM1_SLUG_T + TM1_SLUG_CLEAR
    notch = box(TM1_SLUG_X + 2 * TM1_SLUG_CLEAR, TM1_TANG_Y + 2, nh + 1,
                cz=TM1_TANG_L - nh + (nh + 1) / 2)
    return body.difference(notch)

def tm1_shoulder():
    cone = hull(tang_prism(0, -0.01, 0.01), band_slab(TM1_SH_TOP))
    band = rrect_prism(TM1_SH_X, TM1_SH_Y, TM1_SH_R, TM1_SH_BOT, TM1_SH_TOP + 0.01)
    return cone.union(band)

def tm1_tip_base():
    return tm1_tang().union(tm1_shoulder())

def tm1_pocket_negatives(clear=TM1_POCKET_CLEAR, depth=TM1_POCKET_DEPTH, mouth_ch=TM1_MOUTH_CH):
    pocket = tang_prism(clear, -0.01, depth)
    lead = hull(tang_prism(clear + mouth_ch, -0.01, 0.01), tang_prism(clear, mouth_ch, mouth_ch + 0.02))
    mag = zcyl(TM1_MAG_D / 2 + TM1_MAG_CLEAR, TM1_MAG_TOP, TM1_MAG_TOP + TM1_MAG_H + TM1_MAG_CLEAR)
    return [pocket, lead, mag]

# ---------------- tm1_nail_blade (B45 family) ----------------
def tm1_nail_blade(w=8.0, r=0.5, attack=45.0, drop=7.0, x0=-0.35, d_root=9.5, s_lump=3.6,
                   crown_r=9.0, mode="printed"):
    a = math.radians(attack)
    ux, uz = math.cos(a), math.sin(a)
    z0 = TM1_SH_BOT - drop + r
    lump = hull(band_slab(), ycyl(r, min(w, TM1_SH_Y), x0 + s_lump * ux, z0 + s_lump * uz))
    if mode == "slot":
        # remove everything in front of the plate's upper-face plane (normal n_up = (-uz, ux))
        cut = box(100, 100, 100, cz=-50)
        cut.apply_transform(tf.rotation_matrix(-a, [0, 1, 0]))
        cut.apply_translation([x0 - r * uz, 0, z0 + r * ux])
        body = lump.difference(cut)
    else:
        plate = hull(ycyl(r, w, x0, z0), ycyl(r, w, x0 + d_root * ux, z0 + d_root * uz))
        body = plate.union(lump)
    return body.intersection(crown(crown_r, TM1_SH_BOT - drop)).intersection(below(TM1_SH_BOT + 0.01))

# ---------------- tips ----------------
# tip_W.scad
W_EDGE_W, W_EDGE_R, W_HEIGHT, W_CROWN_R = 8.0, 0.4, 7.0, 9.0
def tip_W(w=W_EDGE_W, r=W_EDGE_R, h=W_HEIGHT, crown_r=W_CROWN_R):
    z_apex = TM1_SH_BOT - h
    body = hull(band_slab(), ycyl(r, w, 0.0, z_apex + r)).intersection(crown(crown_r, z_apex))
    return tm1_tip_base().union(body)

# tip_B45.scad / tip_B45_12.scad / tip_A45.scad (BLADE_W, BLADE_R, ATTACK, DROP, BLADE_MODE)
def tip_B45(w=8.0, r=0.5, attack=45.0, drop=7.0, mode="printed"):
    return tm1_tip_base().union(tm1_nail_blade(w=w, r=r, attack=attack, drop=drop, mode=mode))

def tip_B45_12(w=12.0, r=0.5, attack=45.0, drop=7.0, mode="printed"):
    return tm1_tip_base().union(tm1_nail_blade(w=w, r=r, attack=attack, drop=drop, mode=mode))

def tip_A45(w=8.0, r=0.4, attack=45.0, drop=7.0, mode="slot"):
    return tm1_tip_base().union(tm1_nail_blade(w=w, r=r, attack=attack, drop=drop, mode=mode))

# tip_H_ball.scad
BALL_D, STEM_R, STEM_LEN, CUP_OFFSET = 3.0, 2.0, 5.5, 0.3
def tip_H(ball_d=BALL_D, stem_r=STEM_R, stem_len=STEM_LEN, cup_offset=CUP_OFFSET, printed_ball=False):
    z_end = TM1_SH_BOT - stem_len
    z_ball = z_end - cup_offset
    cone = hull(band_slab(), zcyl(stem_r, z_end, z_end + 0.02))
    if printed_ball:
        return tm1_tip_base().union(cone).union(ball(ball_d / 2, [0, 0, z_ball]))
    return tm1_tip_base().union(cone.difference(ball(ball_d / 2 + 0.05, [0, 0, z_ball])))

# tip_E_carrier.scad
E = dict(BLOCK_H=3.0, BLOCK_X=11.0, DT_MOUTH=5.0, DT_TOP=7.0, DT_DEPTH=2.0, DT_CLEAR=0.15,
         PAD_X=10.0, PAD_Y=10.0, PAD_H=6.0, PAD_ATTACK=45.0, PAD_REAR_DRAFT=10.0,
         BLADE_W=8.0, BLADE_LEN=9.0, BLADE_T=1.0, BLADE_OVERHANG=2.0, BLADE_CROWN_R=9.0)
E_ZB = TM1_SH_BOT - E["BLOCK_H"]   # -8.5

def dovetail_xz(w_bot, w_top, z_bot, depth, length):
    return prism_xz([[-w_bot / 2, z_bot], [w_bot / 2, z_bot], [w_top / 2, z_bot + depth], [-w_top / 2, z_bot + depth]], length)

def tip_E_carrier(e=E):
    block = hull(band_slab(), slab(e["BLOCK_X"], TM1_SH_Y, TM1_SH_R, E_ZB))
    block = block.difference(dovetail_xz(e["DT_MOUTH"], e["DT_TOP"], E_ZB - 0.01, e["DT_DEPTH"], TM1_SH_Y + 2))
    return tm1_tip_base().union(block)

def tip_E_pad(e=E):
    rail = dovetail_xz(e["DT_MOUTH"] - 2 * e["DT_CLEAR"], e["DT_TOP"] - 2 * e["DT_CLEAR"], E_ZB - 0.01,
                       e["DT_DEPTH"] - e["DT_CLEAR"], e["PAD_Y"])
    px, ph = e["PAD_X"], e["PAD_H"]
    pad = prism_xz([[-px / 2, E_ZB], [px / 2, E_ZB],
                    [px / 2 - ph / math.tan(math.radians(e["PAD_ATTACK"])), E_ZB - ph],
                    [-px / 2 + ph * math.tan(math.radians(e["PAD_REAR_DRAFT"])), E_ZB - ph]], e["PAD_Y"])
    return rail.union(pad)

def blade_blank_pts(e=E, n=24):
    """eroded (delta -1.5) outline of square(BLADE_W x BLADE_LEN) & circle(R BLADE_CROWN_R at
    (0, BLADE_LEN - BLADE_CROWN_R)); the blank = this outline grown by r 1.5 (convex)"""
    hw, L, cr, rr = e["BLADE_W"] / 2 - 1.5, e["BLADE_LEN"], e["BLADE_CROWN_R"] - 1.5, 1.5
    cy = L - e["BLADE_CROWN_R"]
    ytop = cy + math.sqrt(cr ** 2 - hw ** 2)
    pts = [[-hw, rr], [hw, rr], [hw, ytop]]
    a1 = math.atan2(ytop - cy, hw)
    for i in range(1, n):
        a = a1 + (math.pi - 2 * a1) * i / n
        pts.append([cr * math.cos(a), cy + cr * math.sin(a)])
    pts.append([-hw, ytop])
    return pts

def tip_E_blade(e=E):
    cyls = [zcyl(1.5, 0, e["BLADE_T"], x=p[0], y=p[1], sections=32) for p in blade_blank_pts(e)]
    return hull(*cyls)

def tip_E_blade_placed(e=E):
    """blade on the pad's 45 deg face (preview only; used to report the E edge height)"""
    a = math.radians(e["PAD_ATTACK"])
    cx = e["PAD_X"] / 2 - e["PAD_H"] / math.tan(a)
    cz = E_ZB - e["PAD_H"]
    ux, uz, nx, nz = math.cos(a), math.sin(a), math.sin(a), -math.cos(a)
    s = e["BLADE_LEN"] - e["BLADE_OVERHANG"]
    m = tip_E_blade(e)
    m.apply_transform(tf.rotation_matrix(math.radians(90), [0, 0, 1]))
    m.apply_transform(tf.rotation_matrix(-a, [0, 1, 0]))
    m.apply_translation([cx + s * ux + nx * e["BLADE_T"], 0, cz + s * uz + nz * e["BLADE_T"]])
    return m

# tip_P_carrier.scad
PC = dict(BED_R=8.5, BED_ATTACK=45.0, BED_AXIS_X=-4.52, BED_AXIS_Z=-6.0,
          BOSS_FRONT=(5.0, -9.0), BOSS_BOTTOM=(-0.5, -10.5))
def tip_P_carrier(p=PC):
    body = hull(band_slab(), ycyl(1.0, TM1_SH_Y, *p["BOSS_FRONT"]), ycyl(1.0, TM1_SH_Y, *p["BOSS_BOTTOM"]))
    ring = zcyl(40, -30, 30).difference(zcyl(p["BED_R"], -31, 31, sections=180))
    ring.apply_transform(tf.rotation_matrix(math.radians(90 - p["BED_ATTACK"]), [0, 1, 0]))
    ring.apply_translation([p["BED_AXIS_X"], 0, p["BED_AXIS_Z"]])
    carve = ring.intersection(box(100, 100, 100, cz=TM1_SH_BOT - 50))
    return tm1_tip_base().union(body.difference(carve))

# ---------------- paddle_with_pocket.scad ----------------
# rev 2026-10-01 post DESIGN-FREEZE-ADDENDUM-1 (D2/D3): DRAFT_Y 5 -> 10, new RISER (0 / 9)
P = dict(NOSE_X=14.0, NOSE_Y=9.0, NOSE_R=1.0, DRAFT_X=10.0, DRAFT_Y=10.0, PADDLE_LEN=25.0, RISER=0.0,
         ROOT_X=28.0, ROOT_Y=14.0, ROOT_TRANS=3.0, ROOT_H=7.0, ROOT_R=2.0,
         LEAF_W=12.7, LEAF_T=0.30, WINDOW_X=24.2, WINDOW_Y=8.4, WINDOW_D=3.5,
         WALL_SLOT_H=1.0, SCREW_X=9.5, SCREW_HOLE_D=2.6, SCREW_DEPTH=5.0,
         BAR_X=24.0, BAR_Y=8.0, BAR_H=3.2, BAR_GROOVE_D=0.25, BAR_HOLE_D=3.4,
         SLEEVE_WALL=0.8, SLEEVE_INTERF=0.2, SLEEVE_TOP=3.0, SLEEVE_BOT=TM1_SH_BOT)

def paddle(p=P):
    tx = p["NOSE_X"] + 2 * p["PADDLE_LEN"] * math.tan(math.radians(p["DRAFT_X"]))
    ty = p["NOSE_Y"] + 2 * p["PADDLE_LEN"] * math.tan(math.radians(p["DRAFT_Y"]))
    zd = p["PADDLE_LEN"]                                  # top of the drafted body
    z0 = zd + p["RISER"]                                  # top of the riser
    z1 = z0 + p["ROOT_TRANS"]
    z_top = z1 + p["ROOT_H"]
    z_floor = z_top - p["WINDOW_D"]
    r = p["NOSE_R"]
    body = hull(slab(p["NOSE_X"], p["NOSE_Y"], r, 0.01), slab(tx, ty, r, zd))
    if p["RISER"] > 0:
        body = body.union(rrect_prism(tx, ty, r, zd - 0.01, z0 + 0.01))
    trans = hull(slab(tx, ty, r, z0), slab(p["ROOT_X"], p["ROOT_Y"], p["ROOT_R"], z1))
    root = rrect_prism(p["ROOT_X"], p["ROOT_Y"], p["ROOT_R"], z1 - 0.01, z_top)
    m = body.union(trans).union(root)
    cuts = tm1_pocket_negatives()
    cuts.append(box(p["WINDOW_X"], p["WINDOW_Y"], 100, cz=z_floor + 50))
    cuts.append(box(p["LEAF_W"] + 0.2, p["ROOT_Y"] + 2, p["WALL_SLOT_H"] + 0.02, cz=z_floor - 0.01 + p["WALL_SLOT_H"] / 2))
    for sx in (-p["SCREW_X"], p["SCREW_X"]):
        cuts.append(zcyl(p["SCREW_HOLE_D"] / 2, z_floor - p["SCREW_DEPTH"], z_floor + 0.01, x=sx, sections=24))
    return diff_all(m, cuts)

def paddle_riser9(p=P):
    return paddle(dict(p, RISER=9.0))

def clamp_bar(p=P):
    m = box(p["BAR_X"], p["BAR_Y"], p["BAR_H"], cz=p["BAR_H"] / 2)
    cuts = [box(p["LEAF_W"] + 0.2, p["BAR_Y"] + 2, p["BAR_GROOVE_D"] + 0.02, cz=p["BAR_GROOVE_D"] / 2 - 0.01)]
    cuts += [zcyl(p["BAR_HOLE_D"] / 2, -1, p["BAR_H"] + 1, x=sx, sections=24) for sx in (-p["SCREW_X"], p["SCREW_X"])]
    return diff_all(m, cuts)

def seam_sleeve(p=P):
    nx, ny, nr, wl, it = p["NOSE_X"], p["NOSE_Y"], p["NOSE_R"], p["SLEEVE_WALL"], p["SLEEVE_INTERF"]
    top, bot = p["SLEEVE_TOP"], p["SLEEVE_BOT"]
    ix0, iy0 = nx - 2 * it, ny - 2 * it
    ix1 = nx + 2 * top * math.tan(math.radians(p["DRAFT_X"])) - 2 * it
    iy1 = ny + 2 * top * math.tan(math.radians(p["DRAFT_Y"])) - 2 * it
    outer = hull(slab(ix0 + 2 * wl, iy0 + 2 * wl, nr + wl, bot + 0.01),
                 slab(ix1 + 2 * wl * 0.75, iy1 + 2 * wl * 0.75, nr + wl, top - 0.01))
    c1 = rrect_prism(ix0, iy0, nr, bot - 1, 0.01)
    c2 = hull(slab(ix0, iy0, nr, 0), slab(ix1, iy1, nr, top + 1))
    return diff_all(outer, [c1, c2])

# ---------------- hand_wand_handle.scad ----------------
H = dict(HANDLE_LEN=150.0, HANDLE_X=22.0, HANDLE_H=16.0, HANDLE_R=8.0,
         BLOCK_X=28.0, BLOCK_Y=30.0, BLOCK_H=16.0, BLOCK_R=2.0,
         LEAF_W=12.7, LEAF_T=0.30, WINDOW_X=24.2, WINDOW_Y=24.4, WINDOW_D=3.5,
         WALL_SLOT_H=1.0, SCREWS=((-9.5, -7.0), (9.5, -7.0), (-9.5, 7.0), (9.5, 7.0)),
         SCREW_HOLE_D=2.6, SCREW_DEPTH=6.0, BAR_X=24.0, BAR_Y=24.0, BAR_H=3.2, BAR_GROOVE_D=0.25, BAR_HOLE_D=3.4)

def hand_wand_handle(h=H):
    z_floor = h["BLOCK_H"] - h["WINDOW_D"]
    grip = rrect_prism(h["HANDLE_X"], h["HANDLE_LEN"] + 1, h["HANDLE_R"], 0, h["HANDLE_H"])
    grip.apply_translation([0, -h["BLOCK_Y"] / 2 - h["HANDLE_LEN"] / 2 + 0.5, 0])
    m = grip.union(rrect_prism(h["BLOCK_X"], h["BLOCK_Y"], h["BLOCK_R"], 0, h["BLOCK_H"]))
    cuts = [box(h["WINDOW_X"], h["WINDOW_Y"], 100, cz=z_floor + 50),
            box(h["LEAF_W"] + 0.2, h["BLOCK_Y"] / 2 + 1, h["WALL_SLOT_H"] + 0.02,
                cy=h["BLOCK_Y"] / 4, cz=z_floor - 0.01 + h["WALL_SLOT_H"] / 2)]
    cuts += [zcyl(h["SCREW_HOLE_D"] / 2, z_floor - h["SCREW_DEPTH"], z_floor + 0.01, x=s[0], y=s[1], sections=24)
             for s in h["SCREWS"]]
    return diff_all(m, cuts)

def hand_wand_bar(h=H):
    m = box(h["BAR_X"], h["BAR_Y"], h["BAR_H"], cz=h["BAR_H"] / 2)
    cuts = [box(h["LEAF_W"] + 0.2, h["BAR_Y"] + 2, h["BAR_GROOVE_D"] + 0.02, cz=h["BAR_GROOVE_D"] / 2 - 0.01)]
    cuts += [zcyl(h["BAR_HOLE_D"] / 2, -1, h["BAR_H"] + 1, x=s[0], y=s[1], sections=24) for s in h["SCREWS"]]
    return diff_all(m, cuts)

# ---------------- expected bounding boxes [xmin, xmax, ymin, ymax, zmin, zmax] ----------------
# Worked out by hand from the SCAD parameters (independent of the mesh code). None = not
# checked.  Tolerance 0.06 mm (48-section faceting, the 0.01 mm SCAD overlaps).
EXPECTED = {
    "tip_W":               [-7, 7, -4.5, 4.5, -12.5, 12.0],
    "tip_B45":             [-7, 7, -4.5, 4.5, -12.5, 12.0],
    "tip_B45_12":          [-7, 7, -6.0, 6.0, -12.5, 12.0],
    "tip_A45":             [-7, 7, -4.5, 4.5, None, 12.0],     # carrier only; sheet blade adds the edge
    "tip_H_ball":          [-7, 7, -4.5, 4.5, -11.0, 12.0],    # cup only; the 3 mm ball reaches -12.8
    "tip_E_carrier":       [-7, 7, -4.5, 4.5, -8.5, 12.0],
    "tip_E_pad":           [-5, 5, -5, 5, -14.5, -6.65],
    "tip_E_blade":         [-4, 4, 0, 9, 0, 1.0],
    "tip_P_carrier":       [-7, 7, -4.5, 4.5, None, 12.0],
    # paddle Y: drafted top 9 + 2*25*tan(10) = 17.816 (wider than the 14 mm root) -> +/-8.908
    "paddle_with_pocket":  [-14, 14, -8.908, 8.908, 0, 35],
    "paddle_with_pocket_riser9": [-14, 14, -8.908, 8.908, 0, 44],
    "paddle_clamp_bar":    [-12, 12, -4, 4, 0, 3.2],
    # sleeve top Y: 9 + 2*3*tan(10) - 0.4 + 2*0.8*0.75 = 10.858 -> +/-5.429 (was 5.16 at 5 deg)
    "tm1_seam_sleeve":     [-7.93, 7.93, -5.429, 5.429, -5.5, 3.0],
    "hand_wand_handle":    [-14, 14, -165, 15, 0, 16],
    "hand_wand_clamp_bar": [-12, 12, -12, 12, 0, 3.2],
}

def report(name, m, rows):
    m.merge_vertices()
    ok = bool(m.is_watertight and m.is_volume)
    b = m.bounds
    exp = EXPECTED.get(name)
    bb_ok = True
    if exp:
        got = [b[0][0], b[1][0], b[0][1], b[1][1], b[0][2], b[1][2]]
        bb_ok = all(e is None or abs(g - e) <= 0.06 for g, e in zip(got, exp))
    m.export(os.path.join(OUT, name + ".stl"))
    rows.append((name, b[1] - b[0], b, m.volume, ok, bb_ok))
    return ok and bb_ok

if __name__ == "__main__":
    parts = {
        "tip_W": tip_W, "tip_B45": tip_B45, "tip_B45_12": tip_B45_12, "tip_A45": tip_A45,
        "tip_H_ball": tip_H, "tip_E_carrier": tip_E_carrier, "tip_E_pad": tip_E_pad,
        "tip_E_blade": tip_E_blade, "tip_P_carrier": tip_P_carrier,
        "paddle_with_pocket": paddle, "paddle_with_pocket_riser9": paddle_riser9,
        "paddle_clamp_bar": clamp_bar, "tm1_seam_sleeve": seam_sleeve,
        "hand_wand_handle": hand_wand_handle, "hand_wand_clamp_bar": hand_wand_bar,
    }
    rows = []
    allok = all([report(k, f(), rows) for k, f in parts.items()])
    print(f"{'file':31s} {'bbox X x Y x Z (mm)':25s} {'z range (mm)':17s} {'vol (mm3)':>9s}  watertight  bbox OK")
    for name, size, b, vol, ok, bb_ok in rows:
        print(f"{name + '.stl':31s} {size[0]:6.2f} x {size[1]:6.2f} x {size[2]:6.2f}  "
              f"[{b[0][2]:7.2f},{b[1][2]:6.2f}]  {vol:9.1f}  {str(ok):10s}  {bb_ok}")
    # paddle section checks: the knuckle-plate section (z = 25) and, on the riser paddle, the
    # constant riser section (z 25..34); the leaf floor (31.5 / 40.5) via the window cut
    secs_ok = True
    for name, mk, zs, floor in (("paddle_with_pocket", paddle, (25.0,), 31.5),
                                ("paddle_with_pocket_riser9", paddle_riser9, (25.0, 29.5, 33.9), 40.5)):
        m = mk()
        for z in zs:
            seg = trimesh.intersections.mesh_plane(m, plane_normal=[0, 0, 1], plane_origin=[0, 0, z])
            pts = seg.reshape(-1, 3)
            ext = pts.max(axis=0) - pts.min(axis=0)
            good = abs(ext[0] - 22.816) <= 0.06 and abs(ext[1] - 17.816) <= 0.06
            secs_ok &= good
            print(f"(check) {name}: section at z {z:5.2f} = {ext[0]:.2f} x {ext[1]:.2f} mm  {'OK' if good else 'FAIL'}")
        # leaf floor: a 1 x 1 x 0.4 probe is empty just above the floor (window) and full just below
        def probe(zc):
            with np.errstate(invalid="ignore", divide="ignore"):
                return m.intersection(box(1.0, 1.0, 0.4, cy=3.0, cz=zc)).volume
        above, below_ = probe(floor + 0.25), probe(floor - 0.25)
        good = above < 1e-6 and abs(below_ - 0.4) < 1e-3
        secs_ok &= good
        print(f"(check) {name}: leaf floor at z {floor:.2f} (edge {floor + 12.5:.1f} mm below the leaf)  {'OK' if good else 'FAIL'}")
    print(f"(info) paddle gap at 24 mm pitch, z = 25, free state: {24 - 17.816:.2f} mm")
    allok = allok and secs_ok
    eb = tip_E_blade_placed().bounds
    print(f"(info) E blade edge lowest point z = {eb[0][2]:.2f} mm (W apex -12.50)")
    print("ALL WATERTIGHT, ALL BBOXES AS EXPECTED" if allok else "WARNING: check the rows above")
    sys.exit(0 if allok else 1)
