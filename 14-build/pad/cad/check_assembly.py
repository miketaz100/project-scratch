#!/usr/bin/env python
"""check_assembly.py - pairwise interference of the PAD STLs at the home pose (all parts are
modelled in place).  Also places all six cartridges/pistons/nails.  Run after gen_pad_stl.py."""
import itertools, sys
from gen_pad_stl import *
def L(n):
    return [m for m in [None]]
def place():
    P = {}
    P["deck"] = pd01_deck(); P["skirt_frame"] = pd02_skirt_frame(); P["floor"] = pd05_floor_plate()
    P["gallery"] = pd07_gallery_plate(); P["skirt_plate"] = pd08_skirt_plate(); P["yoke"] = pd10_yoke()
    P["carts"] = U(*[pd06_cartridge(x, y) for (x, y) in PINS])
    P["pistons_e15"] = U(*[pd09_piston(x, y, 15.0) for (x, y) in PINS])
    P["nails_e15"] = U(*[pd15_nail(x, y, 15.0) for (x, y) in PINS])
    P["stops"] = U(*[pd11_stop_block(a) for a in STOP_ANG])
    P["stems"] = U(*[pd12_skid_stem(a) for a in SKID_ANG]); P["feet"] = U(*[pd13_skid_foot(a) for a in SKID_ANG])
    P["knobs"] = U(*[pd14_skid_knob(a) for a in SKID_ANG])
    balls = U(*[sphere(BALL_D / 2, (*polar(RD, a), ZD), 48) for a in DOME_ANG])
    P["balls"] = balls
    return P
P = place()
bad = 0
for a, b in itertools.combinations(P.keys(), 2):
    v = (P[a] ^ P[b]).volume()
    if v > 0.05:
        print(f"OVERLAP {a:12s} x {b:12s}: {v:.2f} mm3"); bad += 1
print("pairs checked:", len(list(itertools.combinations(P.keys(), 2))), "overlaps > 0.05 mm3:", bad)

# ---------------- moving block vs static parts over the pose sweep (pad_geom kinematics)
import pad_geom as G
moving = U(P["floor"], P["gallery"], P["skirt_plate"], P["yoke"], P["carts"], P["pistons_e15"], P["nails_e15"])
balls_small = U(*[sphere(BALL_D / 2 - 0.15, (*polar(RD, a), ZD), 32) for a in DOME_ANG])
static = {"deck": P["deck"], "skirt_frame": P["skirt_frame"], "stops": P["stops"], "stems": P["stems"], "feet": P["feet"]}
worst = {}
poses = [(0.0, 0.0)] + [(s * math.cos(math.radians(p)), s * math.sin(math.radians(p))) for s in (6.5, 12.0, 14.3, 16.0, 17.2, 18.0) for p in range(0, 360, 15)]
for (dx, dy) in poses:
    Rm, t = G.pose_vec(dx, dy)
    T = np.column_stack([Rm, t]).tolist()
    mv = moving.transform(T); bl = balls_small.transform(T)
    for n, st in static.items():
        v = (mv ^ st).volume()
        if v > 0.05: worst[n] = max(worst.get(n, (0, None)), (v, (round(dx, 1), round(dy, 1))))
    v = (bl ^ P["deck"]).volume()
    if v > 0.05: worst["balls(-0.15)"] = max(worst.get("balls(-0.15)", (0, None)), (v, (round(dx, 1), round(dy, 1))))
print("moving-block sweep over", len(poses), "poses; overlaps:", worst if worst else "none")
