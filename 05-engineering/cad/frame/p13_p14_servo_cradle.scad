// =====================================================================
//  p13_p14_servo_cradle.scad - P13 servo cradle (XL330-M288-T) and P14 servo strap
//  PROJECT SCRATCH · 05-engineering/cad/frame · units: mm · frame: global (section 2)
//  Sources: mechanical.md section 5.3 (pocket 20.4 x 34.4 x 23.5, 2.5 walls, open at the horn face +Y and the cable
//  end, strap, TPU bumpers at +/-32 deg, zero-pin bore 3.1), 11 P13/P14, and bom-verified.md section 11 (Director,
//  rev 2): the XL330 has NO side holes; it mounts through its four back-face holes (16 x 30, diam 1.6, 4.5 deep) with
//  M2 x 6 tapping screws through the 2.5 mm back wall (3.5 mm engagement; M2 x 8 bottoms out); the JST connectors
//  sit on both 23 x 34 side faces 13..24 mm behind the horn face, so both side walls have windows there; the output
//  axis is 9.5 mm from the body end (body Z 74.5..108.5).  PART = "cradle" | "strap" | "both".  Print horn face up.
//  Cradle X +/-17 (the four M3 leg screws at (+/-14, 80 / 104) clear the servo pattern), Y -130..-102 (ends 1 mm
//  short of the P16 disc), Z 70..116 (46 tall: the top wall carries the strap inserts, C-S1).  Cable end = a 14 x 12
//  window in the bottom wall.  Zero-pin flange on +X (X 17..23).
//  Bumper lugs at 50.7 deg so a 2 mm TPU pad on their trailing face meets the cheek lug at 32 deg (C-S2).
//  Strap P14 lies across the open +Y face above the horn (Y -102..-98.5, Z 98..116) with a pad reaching 0.3 mm
//  into the servo's front face; 30 x 3.5 x 18 vs section 11's 30 x 4 x 10 (C-S3).
// =====================================================================
include <lib_sp1.scad>
PART = "both";
// rev 3 (crown mount): the back face (plane Y -131.5, X +/-17, Z 70..116) is the crown's bolt interface: back wall 4.0 thick,
// the four servo M2 x 6 heads counterbored diam 4.4 x 1.8 flush with it (3.8 mm engagement); crown holes 4 x M3 at (+/-14, 80 / 104).
X0 = -17;  X1 = 17;  Y0 = -131.5;  Y1 = -102;  Z0 = 70;  Z1 = 116;  BACK = 4.0;  SERVO_CB_D = 4.4;  SERVO_CB_H = 1.8;
BODY_Z0 = SERVO[4] - 0.2;  BODY_ZC = (SERVO[4] + SERVO[5]) / 2;
CABLE_WIN = [14, 12];  SERVO_SCREW_D = 2.2;  CONN_WIN_Z = [78, 105];
LUG_R = 16;  LUG_ANG = 50.7;  LUG_SX = 4;  LUG_SZ = 6;  LUG_Y0 = -103;  LUG_Y1 = -99;  BUMPER_T = 2;
FLANGE_X1 = 23;  FLANGE_Z0 = 70;  FLANGE_Z1 = 98;  ZERO_PIN = [20, 84];  ZERO_PIN_D = 3.1;
STRAP_INS = [[-8, 112], [8, 112]];
MOUNT = [[-14, 80], [14, 80], [-14, 104], [14, 104]];      // = P11 FOOT_INS

module p13_servo_cradle() difference() {
    union() {
        box(X0, X1, Y0, Y1, Z0, Z1);
        box(X1 - 0.01, FLANGE_X1, Y0, Y0 + 6, FLANGE_Z0, FLANGE_Z1);                                  // zero-pin flange
        for (s = [-1, 1]) cbox(AXIS_X + s * LUG_R * sin(LUG_ANG), (LUG_Y0 + LUG_Y1) / 2, AXIS_Z - LUG_R * cos(LUG_ANG), LUG_SX, LUG_Y1 - LUG_Y0, LUG_SZ);   // bumper lugs
    }
    xl330_pocket(0, Y0 + BACK, BODY_Z0);
    box(-CABLE_WIN[0] / 2, CABLE_WIN[0] / 2, Y0 + BACK + 2, Y0 + BACK + 2 + CABLE_WIN[1], Z0 - 1, BODY_Z0 + 1);   // cable window (bottom)
    for (h = XL330_FRAME_HOLES) {                                                                                  // 4 x M2 x 6 into the servo's back-face holes
        cyl_y(SERVO_SCREW_D / 2, Y0 - 1, Y0 + BACK + 1, h[0], BODY_ZC + h[1], fn = 16);
        cyl_y(SERVO_CB_D / 2, Y0 - 1, Y0 + SERVO_CB_H, h[0], BODY_ZC + h[1], fn = 24);                                // head counterbore, flush with the crown face
    }
    box(X0 - 1, X1 + 1, HORN_Y[0] - XL330_CONN[1] - 0.5, HORN_Y[0] - XL330_CONN[0], CONN_WIN_Z[0], CONN_WIN_Z[1]);   // connector windows, both side walls
    cyl_y(ZERO_PIN_D / 2, Y0 - 1, Y1 + 1, ZERO_PIN[0], ZERO_PIN[1], fn = 24);
    for (h = STRAP_INS) ins_y(M3_INS_D, M3_INS_L, h[0], h[1], Y1, -1);                                 // strap inserts in the top wall's +Y end
    for (h = MOUNT) cyl_y(M3_CLEAR / 2, Y0 - 1, Y0 + BACK + 1, h[0], h[1], fn = 24);                   // 4 x M3 through the back into P11
}

S_X = 30;  S_T = 3.5;  S_Z0 = 98;  S_Z1 = 116;  S_Y1 = Y1 + 3.5;  INTERF = 0.3;
module p14_servo_strap() difference() {
    union() {
        box(-S_X / 2, S_X / 2, S_Y1 - S_T, S_Y1, S_Z0, S_Z1);
        box(-8, 8, HORN_Y[0] + INTERF, S_Y1 - S_T + 0.01, S_Z0, 108);                                  // pad into the pocket (0.3 interference)
    }
    for (h = STRAP_INS) cyl_y(M3_CLEAR / 2, S_Y1 - S_T - 1, S_Y1 + 1, h[0], h[1], fn = 24);
}
if (PART == "cradle" || PART == "both") p13_servo_cradle();
if (PART == "strap" || PART == "both") p14_servo_strap();
