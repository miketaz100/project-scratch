#!/usr/bin/env python
"""dish_variant_check.py - CONFLICTS #1 evidence: the frozen sec 4.2 dish read at the NAIL plane
(lateral breakpoints x 157/85, balls at R 43).  Prints scalp rake, turnaround clearance, landing
angle and tilt.  Run from this folder after dish_kinematics.py.  (S0 kit engineer, 2026-10-02)"""
import sys, math, numpy as np
sys.path.insert(0, '.')
import dish_kinematics as dk
k = dk.R_DC / dk.R_SCALP
# V2: frozen numbers read at the nail plane -> scale the ball-offset breakpoints, keep the radial rises
rise_in = (13.7-7)*math.tan(math.radians(34)); rise_out = (17-13.7)*math.tan(math.radians(50))
def rise2(s):
    s = abs(s); r = 0.0
    a7, a137, a17 = 7*k, 13.7*k, 17*k
    if s > a7: r += (min(s, a137)-a7) * rise_in/(a137-a7)
    if s > a137: r += (min(s, a17)-a137) * rise_out/(a17-a137)
    if s > a17: r += (s-a17)*math.tan(math.radians(70))
    return r
dk.rise_of_sigma = rise2
dk.A_DOME = 43.0
dk.H = [np.array([43*math.cos(math.radians(a)), 43*math.sin(math.radians(a)), math.sqrt(dk.R_DC**2-43**2)]) for a in dk.DOME_ANG]
dk.ZQ = dk.H[0][2]
dk.D_MAX = 16.5*k
sm = dk.scalp_metrics()
print("V2 dome-level travel +-%.1f, rims at ball level %.1f / %.1f deg" % (dk.D_MAX, math.degrees(math.atan(rise_in/((13.7-7)*k))), math.degrees(math.atan(rise_out/((17-13.7)*k)))))
print("V2 scalp chord", sm["scalp_chord"], "turn clearance", sm["turn_lift"])
# landing angle
angs=[]
for psi in range(0,360,30):
    c,s=math.cos(math.radians(psi)),math.sin(math.radians(psi)); xg=None; tr={j:[] for j in range(3)}
    for u in np.linspace(dk.D_MAX,-dk.D_MAX,801):
        xg=dk.solve_pose((u*c,u*s),xg); R,t=dk.pose_points(xg)
        for j,n in enumerate(dk.NAILS): tr[j].append(dk.nail_state(R,t,n))
    for j in range(3):
        for q in range(1,len(tr[j])):
            if tr[j][q-1][0]>0>=tr[j][q][0]:
                W0,W1=tr[j][q-1][1],tr[j][q][1]; v=W1-W0; nn=W1/np.linalg.norm(W1)
                angs.append(math.degrees(math.atan2(-(v@nn), np.linalg.norm(v-(v@nn)*nn)))); break
print("V2 landing", round(min(angs),1), round(max(angs),1), "max tilt deg", round(math.degrees(16.5/85),1))
