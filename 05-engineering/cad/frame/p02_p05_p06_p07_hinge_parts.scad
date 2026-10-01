// =====================================================================
//  p02_p05_p06_p07_hinge_parts.scad - P2 pulley sheave, P5 frame hinge knuckle, P6 keeper lever, P7 cord bar,
//                                     P44 reset cord toggle, P45 reset cord guide
//  PROJECT SCRATCH · 05-engineering/cad/frame · units: mm · frame: global for P5/P6/P7/P45, local for P2/P44
//  Sources: mechanical.md section 4.1 (knuckle Y +/-24, bore 6.3, bolted under the post), 4.3 (pulleys, cord bar
//  at Z 148, Y +/-60), 4.4 (keeper 25 x 25 x 3 at r 50 below the pin), 4.7 (reset cord), 11 P2/P5/P6/P7/P44/P45.
//  PART = "sheave" | "knuckle" | "lever" | "cordbar" | "toggle" | "guide" | "all"
//  P6 runs from the keeper (Z 19..49) up in front of the knuckle to clamp the post's front face (Z 106..134):
//  115 tall, not section 11's 60 (C-F3).  P7 wraps the post (38 in X, C-F4).
// =====================================================================
include <lib_sp1.scad>
PART = "all";

// ---- P2 pulley sheave (local: axis Z, z 0..5): V groove for the 1 mm cord, diam 10 bore for a 623ZZ, 1 mm lip ----
SH_OD = 16;  SH_W = 5;  SH_GROOVE = 1.5;  SH_BORE = 10;  SH_BRG_W = 4;  SH_LIP_D = 8;
module p02_pulley_sheave() rotate_extrude($fn = FN)
    polygon([[SH_LIP_D / 2, 0], [SH_OD / 2, 0], [SH_OD / 2, SH_W / 2 - SH_GROOVE], [SH_OD / 2 - SH_GROOVE, SH_W / 2], [SH_OD / 2, SH_W / 2 + SH_GROOVE],
             [SH_OD / 2, SH_W], [SH_BORE / 2, SH_W], [SH_BORE / 2, SH_W - SH_BRG_W], [SH_LIP_D / 2, SH_W - SH_BRG_W]]);

// ---- P5 frame hinge knuckle: 24 x 48 x 30 at the pin, 2020 socket 12 deep on top, 2 x M5 counterbored ----
K_X = 24;  K_Y = 48;  K_Z0 = 76;  K_Z1 = 106;  K_SOCK_D = 12;  K_SCREW_Z = 101;  K_CB_D = 9.5;  K_CB_DEPTH = 6;
module p05_hinge_knuckle() difference() {
    box(PIN_X - K_X / 2, PIN_X + K_X / 2, -K_Y / 2, K_Y / 2, K_Z0, K_Z1);
    socket_2020_z(PIN_X, 0, K_Z1 - K_SOCK_D, K_Z1 + 1);
    cyl_y(PIN_BORE / 2, -K_Y / 2 - 1, K_Y / 2 + 1, PIN_X, PIN_Z, fn = 32);
    cyl_y(M5_CLEAR / 2, -K_Y / 2 - 1, K_Y / 2 + 1, PIN_X, K_SCREW_Z, fn = 24);
    cyl_y(K_CB_D / 2, -K_Y / 2 - 0.01, -K_Y / 2 + K_CB_DEPTH, PIN_X, K_SCREW_Z, fn = 32);
    cyl_y(K_CB_D / 2, K_Y / 2 - K_CB_DEPTH, K_Y / 2 + 0.01, PIN_X, K_SCREW_Z, fn = 32);
}

// ---- P6 keeper lever ----
FOOT_X0 = -66;  FOOT_X1 = -54;  FOOT_Y = 30;  FOOT_Z0 = 19;  FOOT_Z1 = 49;  KEEPER = 25;  KEEPER_T = 3;
BRIDGE_Z1 = 57;  UP_X0 = -47;  UP_X1 = -39;  UP_Y = 20;  UP_Z1 = 134;  UP_STEP_Z = 106;
L_SCREW_ZS = [115, 127];  EYE_D = 2.5;  EYE_Z = 22.5;  KEEPER_SCREW_Y = 8;
module p06_keeper_lever() difference() {
    union() {
        box(FOOT_X0, FOOT_X1, -FOOT_Y / 2, FOOT_Y / 2, FOOT_Z0, FOOT_Z1);                   // foot with the keeper recess
        box(FOOT_X0, UP_X1, -UP_Y / 2, UP_Y / 2, FOOT_Z1 - 0.01, BRIDGE_Z1);                 // bridge under the knuckle
        box(UP_X0, UP_X1, -UP_Y / 2, UP_Y / 2, FOOT_Z1, UP_STEP_Z + 0.01);                   // upright in front of the knuckle
        box(POST[1], UP_X1, -UP_Y / 2, UP_Y / 2, UP_STEP_Z, UP_Z1);                          // clamp pad on the post's front face
    }
    box(FOOT_X0 - 1, FOOT_X0 + KEEPER_T, -KEEPER / 2, KEEPER / 2, MAG_Z - KEEPER / 2, MAG_Z + KEEPER / 2);   // 25 x 25 x 3 keeper recess
    cyl_y(EYE_D / 2, -FOOT_Y / 2 - 1, FOOT_Y / 2 + 1, (FOOT_X0 + FOOT_X1) / 2, EYE_Z, fn = 16);              // reset-cord eyelet
    for (yy = [-KEEPER_SCREW_Y, KEEPER_SCREW_Y]) ins_x(M3_PILOT, 6, yy, MAG_Z, FOOT_X0 + KEEPER_T, 1);         // 2 x M3 x 6 csk (keeper)
    for (zz = L_SCREW_ZS) { cyl_x(M5_CLEAR / 2, POST[1] - 1, UP_X1 + 1, 0, zz, fn = 24); cyl_x(M5_HEAD_D / 2, UP_X1 - 3, UP_X1 + 1, 0, zz, fn = 32); }   // 2 x M5 T-nut
}

// ---- P7 cord bar: clamps the post at Z 148 (M5 T-nuts through the cheeks), arms to Y +/-70, eyelets at Y +/-60 ----
CB_Z0 = 142;  CB_Z1 = 154;  CB_BACK_X0 = -76;  CB_CHEEK_Y0 = 10.1;  CB_CHEEK_Y1 = 14;  CB_ARM_X0 = -50;  CB_ARM_X1 = -38;
CB_ARM_Y1 = 70;  CB_CORD_Y = 60;  CB_EYE_D = 2.5;  CB_POST_D = 4;  CB_POST_H = 5;  CB_POST_Y = 52;
module p07_cord_bar() difference() {
    union() {
        box(CB_BACK_X0, POST[0] + 0.01, -CB_CHEEK_Y1, CB_CHEEK_Y1, CB_Z0, CB_Z1);
        for (s = [-1, 1]) {
            box(CB_BACK_X0, CB_ARM_X1, min(s * CB_CHEEK_Y0, s * CB_CHEEK_Y1), max(s * CB_CHEEK_Y0, s * CB_CHEEK_Y1), CB_Z0, CB_Z1);
            box(CB_ARM_X0, CB_ARM_X1, min(s * CB_CHEEK_Y0, s * CB_ARM_Y1), max(s * CB_CHEEK_Y0, s * CB_ARM_Y1), CB_Z0, CB_Z1);
            cyl_z(CB_POST_D / 2, CB_Z1 - 0.01, CB_Z1 + CB_POST_H, (CB_ARM_X0 + CB_ARM_X1) / 2, s * CB_POST_Y, fn = 24);   // bowline post
        }
    }
    cyl_y(M5_CLEAR / 2, -20, 20, PIN_X, (CB_Z0 + CB_Z1) / 2, fn = 24);
    for (s = [-1, 1]) cyl_z(CB_EYE_D / 2, CB_Z0 - 1, CB_Z1 + 1, (CB_ARM_X0 + CB_ARM_X1) / 2, s * CB_CORD_Y, fn = 16);
}

// ---- P44 reset cord toggle (local: axis X, centred): diam 14 x 40, cord bore 2.5, knot pocket ----
TG_D = 14;  TG_L = 40;  TG_BORE = 2.5;  TG_KNOT_D = 6;  TG_KNOT_H = 4;  TG_CH = 1;
module p44_reset_toggle() difference() {
    union() {
        cyl_x(TG_D / 2, -TG_L / 2 + TG_CH, TG_L / 2 - TG_CH);
        hull() { cyl_x(TG_D / 2 - TG_CH, -TG_L / 2, -TG_L / 2 + 0.01); cyl_x(TG_D / 2, -TG_L / 2 + TG_CH, -TG_L / 2 + TG_CH + 0.01); }
        hull() { cyl_x(TG_D / 2, TG_L / 2 - TG_CH - 0.01, TG_L / 2 - TG_CH); cyl_x(TG_D / 2 - TG_CH, TG_L / 2 - 0.01, TG_L / 2); }
    }
    cyl_z(TG_BORE / 2, -TG_D / 2 - 1, TG_D / 2 + 1, fn = 16);
    cyl_z(TG_KNOT_D / 2, TG_D / 2 - TG_KNOT_H, TG_D / 2 + 1, fn = 24);
}

// ---- P45 reset cord guide: under the magnet arm's bottom web (Z 20), channel in from +X, R 3 bend, out downward ----
G_X0 = -95;  G_X1 = -80;  G_Y = 20;  G_Z0 = 5;  G_Z1 = 20;  G_CH_D = 3;  G_CH_Z = 12;  G_BEND_R = 3;  G_XB = -88;
G_SCREW = [[-91, 6], [-84, 6]];
module p45_reset_cord_guide() difference() {
    box(G_X0, G_X1, -G_Y / 2, G_Y / 2, G_Z0, G_Z1);
    cyl_x(G_CH_D / 2, G_XB, G_X1 + 1, 0, G_CH_Z, fn = 24);                                                   // horizontal channel
    translate([G_XB, 0, G_CH_Z - G_BEND_R]) rotate([0, -90, 0]) rotate([90, 0, 0])                           // quarter torus (-X/+Z quadrant)
        rotate_extrude(angle = 90, $fn = 48) translate([G_BEND_R, 0]) circle(G_CH_D / 2, $fn = 24);
    cyl_z(G_CH_D / 2, G_Z0 - 1, G_CH_Z - G_BEND_R, G_XB - G_BEND_R, 0, fn = 24);                             // down channel
    hull() { cyl_x(G_CH_D / 2, G_X1 - G_BEND_R, G_X1 - G_BEND_R + 0.01, 0, G_CH_Z, fn = 24); cyl_x(G_CH_D / 2 + G_BEND_R, G_X1 - 0.6, G_X1 + 1, 0, G_CH_Z, fn = 24); }   // R 3 entry flare
    for (h = G_SCREW) { cyl_z(M3_CLEAR / 2, G_Z0 - 1, G_Z1 + 1, h[0], h[1], fn = 24); cyl_z(M3_HEAD_D / 2, G_Z0 - 1, G_Z0 + 4, h[0], h[1], fn = 24); }
}

if (PART == "sheave") p02_pulley_sheave();
if (PART == "knuckle" || PART == "all") p05_hinge_knuckle();
if (PART == "lever" || PART == "all") p06_keeper_lever();
if (PART == "cordbar" || PART == "all") p07_cord_bar();
if (PART == "toggle") p44_reset_toggle();
if (PART == "guide" || PART == "all") p45_reset_cord_guide();
