#!/usr/bin/env python
"""
gen_tips_stl.py — convenience STL generator for SP1 tips (PROJECT SCRATCH)
Generates: tip_W, tip_B45, tip_H_ball, paddle_with_pocket (+ paddle_clamp_bar) into ./stl/
using trimesh + manifold3d booleans.  THE .scad FILES ARE THE SOURCE OF TRUTH; every
dimension below is copied from tm1_tang_lib.scad / tip_*.scad / paddle_with_pocket.scad
and must be kept in sync (names match the SCAD parameters).  Units: mm.
Frame: +Z into the holder pocket, -Z toward the scalp, X = stroke, Y = across.

Run:  <cadenv>/bin/python gen_tips_stl.py
"""
import math, os, sys
import numpy as np
import trimesh
from trimesh import transformations as tf

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "stl")
os.makedirs(OUT, exist_ok=True)
SECT = 48  # cylinder sections (~$fn)

# ---------------- tm1_tang_lib.scad constants ----------------
TM1_TANG_X, TM1_TANG_Y, TM1_TANG_L, TM1_KEY, TM1_END_CH = 10.0, 4.0, 12.0, 2.0, 0.5
TM1_SLUG_X, TM1_SLUG_T, TM1_SLUG_CLEAR = 6.0, 1.0, 0.15
TM1_SH_X, TM1_SH_Y, TM1_SH_R, TM1_SH_TOP, TM1_SH_BOT = 14.0, 9.0, 1.0, -2.5, -5.5
TM1_POCKET_CLEAR, TM1_POCKET_DEPTH, TM1_MOUTH_CH = 0.15, 12.5, 0.6
TM1_MAG_D, TM1_MAG_H, TM1_MAG_CLEAR, TM1_MAG_TOP = 6.0, 2.0, 0.1, 11.9

# ---------------- mesh helpers ----------------
def extrude_convex_polygon(pts, z0, z1):
    """Prism from a CCW convex 2D polygon between z0 and z1 (fan triangulation)."""
    pts = np.asarray(pts, dtype=float)
    n = len(pts)
    v = np.vstack([np.column_stack([pts, np.full(n, z0)]), np.column_stack([pts, np.full(n, z1)])])
    faces = []
    for i in range(1, n - 1):                       # bottom cap (normal -Z): reversed fan
        faces.append([0, i + 1, i])
        faces.append([n, n + i, n + i + 1])          # top cap (normal +Z)
    for i in range(n):                                # sides
        j = (i + 1) % n
        faces += [[i, j, n + j], [i, n + j, n + i]]
    m = trimesh.Trimesh(vertices=v, faces=faces, process=True)
    m.fix_normals()
    return m

def tang_profile_pts(c=0.0):
    hx, hy = TM1_TANG_X / 2 + c, TM1_TANG_Y / 2 + c
    k = TM1_KEY + c * (2 - math.sqrt(2))
    return [[-hx, -hy], [hx, -hy], [hx, hy - k], [hx - k, hy], [-hx, hy]]

def tang_prism(c, z0, z1):
    return extrude_convex_polygon(tang_profile_pts(c), z0, z1)

def hull(*meshes):
    return trimesh.convex.convex_hull(trimesh.util.concatenate(list(meshes)))

def zcyl(r, z0, z1, x=0.0, y=0.0, sections=SECT):
    m = trimesh.creation.cylinder(radius=r, height=z1 - z0, sections=sections)
    m.apply_translation([x, y, (z0 + z1) / 2])
    return m

def rrect_prism(x, y, r, z0, z1):
    """rounded rectangle (vertical corner radius r) between z0 and z1 = hull of 4 cylinders"""
    cs = [zcyl(r, z0, z1, sx * (x / 2 - r), sy * (y / 2 - r)) for sx in (-1, 1) for sy in (-1, 1)]
    return hull(*cs)

def band_slab(z=TM1_SH_BOT, h=0.02):
    return rrect_prism(TM1_SH_X, TM1_SH_Y, TM1_SH_R, z - h / 2, z + h / 2)

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

# ---------------- tips ----------------
def tip_W(w=8.0, r=0.4, h=7.0, crown_r=9.0):
    z_apex = TM1_SH_BOT - h
    body = hull(band_slab(), ycyl(r, w, 0.0, z_apex + r)).intersection(crown(crown_r, z_apex))
    return tm1_tip_base().union(body)

def tip_B45(w=8.0, r=0.5, attack=45.0, drop=7.0, x0=-0.35, d_root=9.5, s_lump=3.6, crown_r=9.0):
    ux, uz = math.cos(math.radians(attack)), math.sin(math.radians(attack))
    z0 = TM1_SH_BOT - drop + r
    plate = hull(ycyl(r, w, x0, z0), ycyl(r, w, x0 + d_root * ux, z0 + d_root * uz))
    lump = hull(band_slab(), ycyl(r, min(w, TM1_SH_Y), x0 + s_lump * ux, z0 + s_lump * uz))
    body = plate.union(lump).intersection(crown(crown_r, TM1_SH_BOT - drop))
    return tm1_tip_base().union(body)

def tip_H(ball_d=3.0, stem_r=2.0, stem_len=5.5, cup_offset=0.3):
    z_end = TM1_SH_BOT - stem_len
    z_ball = z_end - cup_offset
    cone = hull(band_slab(), zcyl(stem_r, z_end, z_end + 0.02))
    cup = trimesh.creation.icosphere(subdivisions=3, radius=ball_d / 2 + 0.05)
    cup.apply_translation([0, 0, z_ball])
    return tm1_tip_base().union(cone.difference(cup))

# ---------------- paddle_with_pocket.scad ----------------
P = dict(NOSE_X=14.0, NOSE_Y=9.0, NOSE_R=1.0, DRAFT_X=10.0, DRAFT_Y=5.0, PADDLE_LEN=25.0,
         ROOT_X=28.0, ROOT_Y=14.0, ROOT_TRANS=3.0, ROOT_H=7.0, ROOT_R=2.0,
         LEAF_W=12.7, LEAF_T=0.30, WINDOW_X=23.2, WINDOW_Y=8.4, WINDOW_D=3.5,
         WALL_SLOT_H=1.0, SCREW_X=10.0, SCREW_HOLE_D=2.6, SCREW_DEPTH=5.0,
         BAR_X=23.0, BAR_Y=8.0, BAR_H=3.2, BAR_GROOVE_D=0.25, BAR_HOLE_D=3.4)

def tm1_pocket_negatives(clear=TM1_POCKET_CLEAR, depth=TM1_POCKET_DEPTH, mouth_ch=TM1_MOUTH_CH):
    pocket = tang_prism(clear, -0.01, depth)
    lead = hull(tang_prism(clear + mouth_ch, -0.01, 0.01), tang_prism(clear, mouth_ch, mouth_ch + 0.02))
    mag = zcyl(TM1_MAG_D / 2 + TM1_MAG_CLEAR, TM1_MAG_TOP, TM1_MAG_TOP + TM1_MAG_H + TM1_MAG_CLEAR)
    return [pocket, lead, mag]

def paddle(p=P):
    tx = p["NOSE_X"] + 2 * p["PADDLE_LEN"] * math.tan(math.radians(p["DRAFT_X"]))
    ty = p["NOSE_Y"] + 2 * p["PADDLE_LEN"] * math.tan(math.radians(p["DRAFT_Y"]))
    z0, z1 = p["PADDLE_LEN"], p["PADDLE_LEN"] + p["ROOT_TRANS"]
    z_top = z1 + p["ROOT_H"]
    z_floor = z_top - p["WINDOW_D"]
    r = p["NOSE_R"]
    body = hull(rrect_prism(p["NOSE_X"], p["NOSE_Y"], r, 0.0, 0.02), rrect_prism(tx, ty, r, z0 - 0.01, z0 + 0.01))
    trans = hull(rrect_prism(tx, ty, r, z0 - 0.01, z0 + 0.01), rrect_prism(p["ROOT_X"], p["ROOT_Y"], p["ROOT_R"], z1 - 0.01, z1 + 0.01))
    root = rrect_prism(p["ROOT_X"], p["ROOT_Y"], p["ROOT_R"], z1 - 0.01, z_top)
    m = body.union(trans).union(root)
    cuts = tm1_pocket_negatives()
    cuts.append(box(p["WINDOW_X"], p["WINDOW_Y"], 100, cz=z_floor + 50))
    cuts.append(box(p["LEAF_W"] + 0.2, p["ROOT_Y"] + 2, p["WALL_SLOT_H"] + 0.02, cz=z_floor - 0.01 + p["WALL_SLOT_H"] / 2))
    for sx in (-p["SCREW_X"], p["SCREW_X"]):
        cuts.append(zcyl(p["SCREW_HOLE_D"] / 2, z_floor - p["SCREW_DEPTH"], z_floor + 0.01, x=sx, sections=24))
    for c in cuts:
        m = m.difference(c)
    return m

def clamp_bar(p=P):
    m = box(p["BAR_X"], p["BAR_Y"], p["BAR_H"], cz=p["BAR_H"] / 2)
    m = m.difference(box(p["LEAF_W"] + 0.2, p["BAR_Y"] + 2, p["BAR_GROOVE_D"] + 0.02, cz=p["BAR_GROOVE_D"] / 2 - 0.01))
    for sx in (-p["SCREW_X"], p["SCREW_X"]):
        m = m.difference(zcyl(p["BAR_HOLE_D"] / 2, -1, p["BAR_H"] + 1, x=sx, sections=24))
    return m

# ---------------- main ----------------
def report(name, m):
    m.merge_vertices()
    ok = m.is_watertight
    b = m.bounds
    size = b[1] - b[0]
    path = os.path.join(OUT, name + ".stl")
    m.export(path)
    print(f"{name:22s} watertight={ok!s:5s} vol={m.volume:8.1f} mm3  "
          f"bbox x[{b[0][0]:6.2f},{b[1][0]:6.2f}] y[{b[0][1]:6.2f},{b[1][1]:6.2f}] "
          f"z[{b[0][2]:6.2f},{b[1][2]:6.2f}]  size {size[0]:.2f} x {size[1]:.2f} x {size[2]:.2f}")
    return ok

if __name__ == "__main__":
    results = {
        "tip_W": tip_W(),
        "tip_B45": tip_B45(),
        "tip_H_ball": tip_H(),
        "paddle_with_pocket": paddle(),
        "paddle_clamp_bar": clamp_bar(),
    }
    allok = all(report(k, v) for k, v in results.items())
    print("ALL WATERTIGHT" if allok else "WARNING: some meshes not watertight")
    sys.exit(0 if allok else 1)
