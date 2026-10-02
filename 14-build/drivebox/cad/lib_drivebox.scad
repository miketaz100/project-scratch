// =====================================================================
//  lib_drivebox.scad - shared constants and helpers, SP1 v3 DRIVE BOX printed parts
//  PROJECT SCRATCH · 14-build/drivebox/cad · DRIVE BOX WP · 2026-10-02 · units: mm
// ---------------------------------------------------------------------
//  Basic primitives only (cube, cylinder, linear_extrude, offset, polygon, booleans).
//  gen_drivebox_stl.py mirrors every constant and module below under the same name;
//  the .scad files are the source of truth.
//  Frames (README.md):
//    D  drum-module frame: deck top surface z = 0; +x toward the umbilical wall; y across.
//    b  bulkhead frame: x = u = outward normal of the right end wall (u = 0 on the wall's
//       OUTSIDE surface); y = v along the wall (= case Y); z = w up.
//    L  local frame for loose parts.
//  [VERIFY] numbers are vendor dimensions not yet measured on the part in hand.
// =====================================================================
FN = 48;

// ---- fasteners ----
M3_CLEAR = 3.4;  M4_CLEAR = 4.5;  M5_CLEAR = 5.5;
M3_INS_D = 4.0;  M3_INS_L = 6.0;            // brass heat-set M3 x 5.7
M3_TAP = 2.5;    M5_TAP = 4.2;              // tap drills (SLA parts are tapped, not heat-set)
M3_NUT_AF = 5.6; M3_NUT_T = 2.6;
M5_NUT_AF = 8.2; M5_NUT_T = 4.2;
NUT_1420_AF = 11.3; NUT_1420_T = 6.0;       // 1/4-20 hex nut, 7/16 in AF

// ---- drum module (frame D) ----
MOTOR_X = 34;
MOTOR_Y = [23, 69, 115];                    // motor pitch 46
CABLE_Y = [29, 75, 121];                    // MOTOR_Y + 6: tangent line of each drum (pitch radius 6)
DRUM_Z0 = 1.0;                              // drum bottom above deck top
ROW_Z = [14, 22];                           // cable heights: groove 1 (pad 1), groove 2 (pad-2 provision)
MOTOR_BOSS_D = 22.6;
MOTOR_HOLE = 15.5;                          // 31 mm square
INDEX_R = 12;
DECK_X1 = 150; DECK_Y1 = 140; DECK_T = 4; DECK_LEG_Z = -28;
LEGS = [[0,10,0,12],[0,10,128,140],[80,92,0,12],[80,92,128,140],[138,150,0,12],[138,150,128,140]];
ROD_Y = [5, 135];
ROD_Z = 16;
ROD_HOLE_D = 3.9;                           // press fit, 4 mm rod
POST_REAR = [57.5, 65.5];
POST_FRONT = [139.5, 147.5];
POST_TOP = 21;
FP_X0 = 100; FP_X1 = 108; FP_Z0 = 2; FP_Z1 = 30; FP_BOSS_R = 6; FP_BOSS_X1 = 112; LM4UU_D = 8.1;
T_ROOT = 14; T_TIP = 3; T_SLOT = 1; T_T = 2.5; T_POCKET_Z0 = 10; T_POCKET_Z1 = 26;
// housing seat: [boss R, boss x1, bore D, floor, cable hole D]
SEAT     = [3.0, 114, 2.5, 1.0, 1.0];       // brass-ferrule (micro coil) housing, default
SEAT_4MM = [3.6, 114, 5.2, 1.0, 1.5];       // 4 mm bicycle shift housing variant
MAG_DY = -5; MAG_BOSS_R = 2.5; MAG_BOSS_X0 = 101.5; MAG_POCKET_D = 3.4; MAG_POCKET_DEPTH = 2.2;
BR_X0 = 94; BR_X1 = 99; BR_Y0 = 13; BR_Y1 = 127; BR_Z0 = 2; BR_Z1 = 30;
BR_SENS_W = 4.4; BR_SENS_H = 3.4; BR_SENS_T = 1.7; BR_LEAD_W = 3.2; BR_CABLE_D = 3.0;
BRIDGE_SCREWS = [[47,9],[47,23],[93,9],[93,23]];
SHELF_HOLES = [[60,52],[60,98],[145,52],[145,98]];   // M3 standoffs for the electronics shelf
REL_SLOT = 0.8;                             // cable release slot width (tongue, seat boss, bridge)
HOUS_OD = 1.6;                              // comb groove; 4.3 for the 4 mm housing variant

// ---- drum (local: axis z, z = 0 drum bottom) ----
FL_R = 15; FL_H = 3; HUB_R = 8; HUB_Z1 = 10.5; G1_Z0 = 10.5; G_LEN = 5; LAND_R = 6.15;
DIV_R = 10; DIV_Z0 = 15.5; DIV_Z1 = 18.5; G2_Z0 = 18.5; TOP_Z0 = 23.5; TOP_Z1 = 25.5;
PITCH_R = 6.0; GROOVE_R = 0.25; TURNS = 5; BORE_R = 2.55; FLAT_X = 2.1; GRUB_Z = 6.5;
NUT_X0 = 3.7; NUT_X1 = 6.3; NUT_HY = 3.3; NUT_Z1 = 9.6; DMAG_R = 1.7; DMAG_DEPTH = 2.2;
ANCH_HX = 1.8; ANCH_Y0 = 5.7; ANCH_Y1 = 7.9; ANCH_DEPTH = 2.4;

// ---- bulkhead / plug (frame b) ----
WALL_T = 3.0;                               // Apache 2800 end-wall shell [VERIFY]
HEAD_U0 = 0; HEAD_U1 = 14; HEAD_V = 62; HEAD_W = 25;
NECK_U0 = -17; NECK_V = 36; NECK_W = 19;
PLUG_U0 = 14; PLUG_U1 = 30;
PORT_V = [-16, 0, 16]; PORT_W = 8; PORT_D = 2.0;
OR_ID = 3.0; OR_OD = 5.6; OR_DEPTH = 0.75;  // metric 3 x 1 NBR70 face seal
SLOT_V = 26; SLOT_W0 = -14; SLOT_W1 = -6;
DOWEL_V = 28; DOWEL_W = 16; DOWEL_D_PRESS = 2.95; DOWEL_D_SLIDE = 3.1; DOWEL_DEPTH = 10;
THUMB_V = 52; THUMB_W = 0; THUMB_D = 4.5; THUMB_NUT_AF = 7.2; THUMB_NUT_T = 3.4; THUMB_NUT_U = 7.0;
CLAMP_V = 42; CLAMP_W = 19; CLAMP_CB_D = 6.5; CLAMP_CB_DEPTH = 3.5; CLAMP_PLATE_V = 50; CLAMP_PLATE_W = 30; CLAMP_T = 4;
PCLIP_V = 20; PCLIP_W = -20; PCLIP_DEPTH = 8;
B1_HEAD_POCKETS = [[38, 47, -15, 12]];      // from the head's wall face u = 0, depth 8, mirrored in v
B1_NECK_POCKETS = [[21, 33, -4, 16]];       // from the neck's inner face, depth 10, mirrored
U1_POCKETS = [[33, 46, -22, 10]];           // from the plug's rear face, depth 10, mirrored
U1_POCKET_C = [-10, 10, 14, 22];            // centre pocket, depth 10

// ---- hook plate and hooks ----
HP_X = 216; HP_Y = 136; HP_T = 6; HP_R = 8; HP_LID_X = 100; HP_LID_Y = 60; HP_CB_D = 10; HP_CB_DEPTH = 3.6;
HP_SLOT_X = 82; HP_SLOT_W = 6; HP_SLOT_L = 42; HP_HOOK_X = 60; HP_HOOK_Y = [30, 55];
HP_WIN = [[-25,-28],[25,-28],[-25,28],[25,28]]; HP_WIN_X = 40; HP_WIN_Y = 36;
HOOK_T = 6; HOOK_WIDTH = 25; HOOK_LEG_Q = 64; HOOK_BAR_Q0 = 58; HOOK_DROP_Q0 = 34; HOOK_GUSSET = 8; HOOK_HOLE_Q = [10, 35];

// ---- pegboard, saddles, seat, clip ----
PEG_X = 100; PEG_Y = 90; PEG_T = 4; PEG_PITCH = 10; PEG_HOLE_D = 3.4; PEG_FL_Z = 20; PEG_FL_T = 4; PEG_FL_HOLES = [-45, 0, 45];
SADDLE_L = 16;
S15_R = 13; S15_H = 14; S15_BOLT_R = 3.4; S15_BOLT_Z = 7; S15_MAG_R = 3.1; S15_MAG_Z0 = 8; S15_CONE_R0 = 7; S15_CONE_R1 = 10; S15_CONE_Z0 = 11;
CL_X = 15; CL_Y = 14; CL_H = 9; CL_CH_R = 6.2; CL_HOLE_X = 9; CL_HOLE_Y = 10.5;
CL_NOSE_R0 = 9.75; CL_NOSE_R1 = 6.75; CL_NOSE_H = 3; CL_WASHER_R = 6.2; CL_WASHER_DEPTH = 1.7;

// ============================ helpers ============================
module box(x0, x1, y0, y1, z0, z1) translate([x0, y0, z0]) cube([x1 - x0, y1 - y0, z1 - z0]);
module cyl_z(r, z0, z1, x = 0, y = 0, r2 = -1, fn = FN)
    translate([x, y, z0]) cylinder(r1 = r, r2 = (r2 < 0 ? r : r2), h = z1 - z0, $fn = fn);
module cyl_x(r, x0, x1, y = 0, z = 0, fn = FN)
    translate([x0, y, z]) rotate([0, 90, 0]) cylinder(r = r, h = x1 - x0, $fn = fn);
module cyl_y(r, y0, y1, x = 0, z = 0, fn = FN)
    translate([x, y0, z]) rotate([-90, 0, 0]) cylinder(r = r, h = y1 - y0, $fn = fn);
// hexagonal prism, across-flats af (vertices on +/-x, flats parallel to x)
module hex_z(af, z0, z1, x = 0, y = 0) translate([x, y, z0]) cylinder(r = af / 2 / cos(30), h = z1 - z0, $fn = 6);
// 2D rounded rectangle centred at (cx, cy)
module crrect(cx, cy, sx, sy, r) translate([cx, cy]) offset(r = r, $fn = FN) square([sx - 2 * r, sy - 2 * r], center = true);
// extrude a 2D profile drawn in (y, z) along +x from x0 to x1
module ext_x(x0, x1) translate([x0, 0, 0]) rotate([90, 0, 90]) linear_extrude(x1 - x0) children();
// extrude a 2D profile drawn in (x, z) along +y from y0 to y1
module ext_y(y0, y1) translate([0, y1, 0]) rotate([90, 0, 0]) linear_extrude(y1 - y0) children();
// mirrored pocket pair about v = 0 (frame b): list entry [v0, v1, w0, w1]
module pocket_pair(p, u0, u1) for (s = [-1, 1]) box(u0, u1, min(s * p[0], s * p[1]), max(s * p[0], s * p[1]), p[2], p[3]);
