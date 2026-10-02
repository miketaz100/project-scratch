// s0_lib.scad - shared constants and helpers for every S0 printed part
// PROJECT SCRATCH, 14-build/S0/cad, S0 kit engineer, 2026-10-02.  Units mm.
// gen_s0_stl.py mirrors these names one-for-one; change both together.
// Dish frame: C = ball (scalp) centre at the origin, +Z up the pad axis.  SYSTEM-SPEC-v3 sec 3.1, 4.1, 4.2.
// Two generated includes come from dish_kinematics.py: pocket_cavity.scad, template_paths.scad.

$fn = 64;

// ---------- fasteners ----------
M3_CLEAR = 3.4;  M3_PILOT = 2.6;  M3_CB_D = 6.2;  M3_CB_H = 3.2;
WOOD_SCREW = 4.5;

// ---------- dish bench (spec 4.1, 4.2; bench deviations in ../CONFLICTS.md) ----------
R_SCALP = 85;            // ball / crown radius
RB = 3;                  // 6 mm Delrin ball radius
R_DC = 157;              // ball-centre sphere (ceiling R 160)
A_DOME = 26;             // bench: balls at R 26 (spec M11 says R 22: CONFLICTS #3)
DOME_ANG = [90, 210, 330];
NAIL_R = 18;             // pentagon radius, spec 4.1
NAIL_ANG = [0, 144, 216];// P0, P2, P3 = group A
Z_DOME = sqrt(R_DC*R_DC - A_DOME*A_DOME);   // 154.83, ball centre height at home
POCKET_R = 21;
DECK_R = 58;
DECK_ZTOP = 175;
LEG_R = 55;  LEG_D_TOP = 10;  LEG_D_BOT = 7;  FOOT_D = 8;
FOOT_C_R = R_SCALP + FOOT_D/2;              // feet centres on R 89 about C
GRIP = [0, 45, 14, 30];                     // x, y, dia, height on the deck top
TPL_PIN = [[22, 22], [-22, -52]];
NOSE_Z0 = 115.5;  NOSE_Z1 = 123.5;          // nose plate: 32.4 mm above the R 85 contact plane
BODY_Z1 = 138;  TOP_Z1 = 142;
BODY_D = 50;  TOP_D = 62;
BORE_D = 6.4;  STEM_BORE_D = 4.7;  STEM_D = 4.5;
SCREW_R = 20;  SCREW_ANG = [60, 180, 300];
POST_D0 = 8;  POST_D1 = 7;  POST_TOP = Z_DOME - 0.6;
BALL_SOCKET_D = 6.1;
WELL_D_TOP = 24;  WELL_D_BOT = 9;  WELL_Z_BOT = 125.5;  HOOK_Z = 128;
EAR = [-7, 7, -40, -24];                    // x0, x1, y0, y1 of the C-arm ear (full body height)
NOSE_D = 50;
PLUNGER_D = 6;  PLUNGER_H = 7;  PLUNGER_FLOOR = 2.5;  CUP_D = 5.3;
MAG_D = 3.1;  MAG_H = 2;
SEAT_D = 6;  SEAT_H = 1.5;
NAIL_TIP_D = 2;  NAIL_TIP_R = 0.4;  NAIL_CONE_H = 1.25;
PIN_HOLE_D = 1.1;  PIN_HOLE_DEPTH = 5;
function nail_len(reserve) = NOSE_Z1 - (sqrt(R_SCALP*R_SCALP - NAIL_R*NAIL_R) - reserve);   // 42.43 / 43.43
// C-arm
CARM_W = 10;  CARM_LOW_Z = 132;  CARM_LOW_H = 6;  CARM_RISER_Y = -88;
CARM_TOP_Z0 = 197;  CARM_TOP_H = 8;
STYLUS_Y = [0, -30];
DRIVE_GRIP = [14, 141, 28];                 // dia, z, length: push here (low), never on the top bar
// templates
TPL_H = 19;  TPL_BASE = 2;  GROOVE_D = 3.4;  WALL_D = 7;
TPL_OUTLINE = [-26, 26, -57, 27, 6];        // x0, x1, y0, y1, corner radius
// skid ring (hand-rake mode)
SKID_T = 3;  SKID_Z0 = NOSE_Z0 - SKID_T;  SKID_FOOT_R = 28;

// ---------- tendon ink rig (S0b) ----------
DRUM_PITCH_D = 12;  DRUM_LAND_D = 12.4;  GROOVE_R = 0.32;  GROOVE_PITCH = 1;
DRUM_FL_D = 24;  HUB_D = 16;  HUB_H = 8;  FL_H = 2;
GROOVE_W = 5.5;  SEP_W = 1;
SHAFT_D = 5.15;  SHAFT_FLAT = 2.1;          // 5 mm D-shaft, flat 0.5 deep  [VERIFY on the motor]
ANCHOR_R = 9.5;
STOP_CABLE_Z = 30 + HUB_H + FL_H + GROOVE_W/2;   // groove A centre above the plywood (motor table top 30)
RIG_STOP_R = 60;  POST_R = 22;
PEN_PLATE_Z0 = 12;  PEN_PLATE_Z1 = 16;  RIG_CABLE_Z = PEN_PLATE_Z1 + 3;

// ---------- helpers ----------
function polar(r, a) = [r*cos(a), r*sin(a)];
module box(x0, x1, y0, y1, z0, z1) translate([x0, y0, z0]) cube([x1-x0, y1-y0, z1-z0]);
module cyl(d, z0, z1, x=0, y=0, d2=-1, fn=$fn)
    translate([x, y, z0]) cylinder(d1=d, d2=(d2 < 0 ? d : d2), h=z1-z0, $fn=fn);
module sph(d, c, fn=$fn) translate(c) sphere(d=d, $fn=fn);
module cyl_ab(d, a, b, fn=32) {             // cylinder of diameter d from point a to point b
    v = b - a;  L = norm(v);
    translate(a) rotate([0, acos(v[2]/L), atan2(v[1], v[0])]) cylinder(d=d, h=L, $fn=fn);
}
module swept(path, d, z0, z1, fn=24)        // hull-chain of vertical cylinders along an XY polyline
    for (i = [0:len(path)-2]) hull() { cyl(d, z0, z1, path[i][0], path[i][1], fn=fn); cyl(d, z0, z1, path[i+1][0], path[i+1][1], fn=fn); }

// ---------- V2: corrected (nail-plane) dish bench, Director ruling 2026-10-02 (dish_bench_v2.scad) ----------
// Profile at the NAIL plane, scaled x K = 157/85 to the dish: sphere to 6.0; 30 deg +4.5 to 13.79;
// 50 deg +4.5 to 17.57; turnaround 17.07 nail = 31.5 dish; 70 deg stop.  Generated pocket: pocket_cavity_v2.scad.
V2_A_DOME = 44;
V2_Z_DOME = sqrt(R_DC*R_DC - V2_A_DOME*V2_A_DOME);   // 150.73
V2_POCKET_R = 37;
V2_DECK_R = 84;  V2_FLAT_R = 66;            // deck radius; flat template seat (45 deg cone outside it)
V2_UNDER_R = 155.5;                         // deck underside = sphere about C
V2_DECK_ZTOP = 180.5;
V2_LEG_R = 66;  V2_LEG_ANG = [30, 150, 270];
V2_GRIP = [-70, -20, 14, 30];
V2_TPL_PIN = [[38, -38], [-30, 38]];        // asymmetric: fits one way only
V2_TPL_OUTLINE = [-45, 45, -45, 45, 8];
V2_RIB = [22, 48, 8, NOSE_Z1, 134];          // r0, r1, width, z0, z1 of the ball-post ribs
V2_POST_TOP = V2_Z_DOME - 0.6;
V2_FOOT_Y = [28, 46];
V2_CARM_LOW = [88, 94];
V2_RISER_Y = 138;
V2_TOP_Z0 = 204;  V2_TOP_H = 9;
V2_GRIP_C = [14, 93, 16];
