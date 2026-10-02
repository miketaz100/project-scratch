#!/usr/bin/env python
"""check_s0_clearance.py - dish bench interference sweep (PROJECT SCRATCH, 14-build/S0/cad)
Poses from dish_kinematics.solve_pose along 24 headings x |d| 0..16.5 and the three template
paths; for each pose the block + nose plate + C-arm (+ two M3x25 styli and the 6 mm balls) are
moved rigidly and intersected with the deck (+ the template in use).  Also checks that the lift
elastic (hook on the block axis -> deck hole) stays inside the well.  Prints worst cases."""
import math, numpy as np, trimesh
import dish_kinematics as dk
import gen_s0_stl as g
from manifold3d import Manifold

pm, dg = g.load_geom()
deck = g.deck(pm)
mov = g.U(g.block(), g.nose_plate(), g.carm(),
          *[g.cyl(3.0, g.CARM_TOP_Z0 + g.CARM_TOP_H - 25.0 + 0.0, g.CARM_TOP_Z0 + g.CARM_TOP_H, 0, y, fn=16) for y in g.STYLUS_Y],
          *[g.sph(6.0, (*g.polar(g.A_DOME, a), g.Z_DOME), fn=32) for a in g.DOME_ANG])
tpls = {k: g.template(dg, k, 0).translate([0, 0, g.DECK_ZTOP]) for k in ("T1_line_star", "T2_dpath", "T3_circle")}
# the styli must not touch the template; walls are the guide: check only the arm/bar body vs template
arm_only = g.carm()

def pose_M(x):
    R, t = dk.pose_points(x)
    return np.hstack([R, t.reshape(3, 1)]).tolist()

def sweep(paths, against, label, body):
    worst = 0.0
    for path in paths:
        xg = None
        for d in path:
            xg = dk.solve_pose(d, xg)
            v = (body.transform(pose_M(xg)) ^ against).volume()
            worst = max(worst, v)
    print(f"{label:46s} max interference volume {worst:8.3f} mm3")
    return worst

radial = [[(u * math.cos(math.radians(p)), u * math.sin(math.radians(p))) for u in np.linspace(0, dk.D_MAX, 34)] for p in range(0, 360, 15)]
w = sweep(radial, deck, "block+nose+C-arm+balls+styli vs deck (24 headings)", mov)
for name, (paths) in (("T1_line_star", dk.TEMPLATES["T1_line_star"]), ("T2_dpath", dk.TEMPLATES["T2_dpath"]), ("T3_circle", dk.TEMPLATES["T3_circle"])):
    sweep(paths, deck, f"  ... along {name} vs deck", mov)
    sweep(paths, tpls[name], f"  C-arm bar vs {name} template", arm_only)
# sanity: the balls must touch the ceiling: lift the block 0.3 mm at home -> the balls must cut the deck
x0 = dk.solve_pose((0.0, 0.0))
M = pose_M(x0)
balls = g.U(*[g.sph(6.0, (*g.polar(g.A_DOME, a), g.Z_DOME), fn=48) for a in g.DOME_ANG])
print(f"sanity: balls raised 0.3 mm cut the deck by {(balls.translate([0, 0, 0.3]) ^ deck).volume():.3f} mm3 (> 0 expected); at rest {(balls ^ deck).volume():.3f}")
# elastic: 1.5 mm cord from the hook (block axis, HOOK_Z) to the deck hole (0, 0, z_u)
blk = g.block()
worst = 0.0
for path in radial:
    xg = None
    for d in path:
        xg = dk.solve_pose(d, xg)
        R, t = dk.pose_points(xg)
        hook = R @ np.array([0, 0, g.HOOK_Z]) + t
        top = np.array([0, 0, pm["z_u"]])
        p0 = hook + (top - hook) * 0.12
        cord = g.cyl_axis(1.5, p0, top, fn=12)
        worst = max(worst, (cord ^ blk.transform(pose_M(xg))).volume())
print(f"elastic cord (1.5 mm) vs block material, worst pose: {worst:.3f} mm3 (0 = clear of the well walls)")
xg = dk.solve_pose((dk.D_MAX, 0))
R, t = dk.pose_points(xg)
hook = R @ np.array([0, 0, g.HOOK_Z]) + t
v = np.array([0, 0, pm["z_u"]]) - hook
print(f"elastic at |d| = 16.5: {math.degrees(math.atan2(math.hypot(v[0], v[1]), v[2])):.1f} deg from vertical, length {np.linalg.norm(v):.1f} mm (home {pm['z_u'] - g.HOOK_Z:.1f})")
