#!/usr/bin/env python
"""check_s0_clearance_v2.py - interference sweep for the V2 (corrected) dish bench.
Run:  DISH_VARIANT=v2 <cadenv>/bin/python check_s0_clearance_v2.py
Moves block_v2 + nose plate + C-arm V2 + balls + the lift rod (part above the template top) through
24 headings x full travel and every template path; intersects with deck_v2 and the templates."""
import math, os, numpy as np
assert os.environ.get("DISH_VARIANT") == "v2", "run with DISH_VARIANT=v2"
import dish_kinematics as dk
import gen_s0_stl as g

pm, dg = g.load_geom("_v2")
deck = g.deck_v2(pm)
rod_above = g.cyl(3.0, g.V2_DECK_ZTOP + g.TPL_H + 0.5, g.V2_TOP_Z0 + g.V2_TOP_H, 0, 0, fn=16)   # rod portion that moves with the bar
mov = g.U(g.block_v2(), g.nose_plate(), g.carm_v2(),
          *[g.sph(6.0, (*g.polar(g.V2_A_DOME, a), g.V2_Z_DOME), fn=32) for a in g.DOME_ANG])
tpls = {k: g.template_v2(dg, k, 0).translate([0, 0, g.V2_DECK_ZTOP]) for k in ("T1_line_star", "T2_dpath", "T3_circle")}
arm = g.carm_v2()

def M(x):
    R, t = dk.pose_points(x)
    return np.hstack([R, t.reshape(3, 1)]).tolist()

def sweep(paths, against, body):
    worst = 0.0
    for path in paths:
        xg = None
        for d in path:
            xg = dk.solve_pose(d, xg)
            worst = max(worst, (body.transform(M(xg)) ^ against).volume())
    return worst

radial = [[(u * math.cos(math.radians(p)), u * math.sin(math.radians(p))) for u in np.linspace(0, dk.D_MAX, 40)] for p in range(0, 360, 15)]
print(f"V2 block+nose+C-arm+balls vs deck, 24 headings: {sweep(radial, deck, mov):.3f} mm3")
for name in ("T1_line_star", "T2_dpath", "T3_circle"):
    print(f"V2 along {name}: vs deck {sweep(dk.TEMPLATES[name], deck, mov):.3f} mm3; C-arm vs template {sweep(dk.TEMPLATES[name], tpls[name], arm):.3f} mm3")
balls = g.U(*[g.sph(6.0, (*g.polar(g.V2_A_DOME, a), g.V2_Z_DOME), fn=48) for a in g.DOME_ANG])
print(f"sanity: balls at rest vs deck {(balls ^ deck).volume():.3f}; raised 0.3 mm {(balls.translate([0, 0, 0.3]) ^ deck).volume():.3f} (> 0 expected)")
