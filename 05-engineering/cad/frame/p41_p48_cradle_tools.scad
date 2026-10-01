// =====================================================================
//  p41_p48_cradle_tools.scad - P41 cradle foot cup, P42 cradle tilt wedge, P43 apex height gauge,
//                              P46 tip-height pull clip, P48 tip box
//  PROJECT SCRATCH · 05-engineering/cad/frame · units: mm · frame: local for every part (see each module)
//  Sources: mechanical.md section 10.2 (foot cups diam 40 x 12 for diam 30 x 15 feet), 10.3 (15 deg wedges 120 x 60,
//  apex gauge 12 x 12 x 120 with rings at 80/82/84/86/88), 7.2 (pull clip P46 over the centre seam sleeve), TP Q5 /
//  11 P48 (tip box 120 x 60 x 25, 8 slots 11 x 5 x 14 deep, label recesses).
//  PART = "foot" | "wedge" | "gauge" | "clip" | "box" | "all"
// =====================================================================
include <lib_sp1.scad>
PART = "all";

// ---- P41 foot cup: diam 40 x 12, diam 30.4 x 8 cup, 2 countersunk diam 3.4 at r 16 for wood screws ----
FC_D = 40;  FC_H = 12;  FC_CUP_D = 30.4;  FC_CUP_H = 8;  FC_SCREW_R = 16;  FC_CSK_D = 7;
module p41_cradle_foot_cup() difference() {
    cyl_z(FC_D / 2, 0, FC_H, fn = 64);
    cyl_z(FC_CUP_D / 2, FC_H - FC_CUP_H, FC_H + 1, fn = 64);
    for (s = [-1, 1]) csk_z(M3_CLEAR, FC_CSK_D, s * FC_SCREW_R, 0, FC_H, true);
}

// ---- P42 tilt wedge: 15 deg, 120 x 60, thick end at +X; anti-slip grooves underneath, 2 mm TPU pad recess on the slope ----
W_L = 120;  W_W = 60;  W_ANG = 15;  W_RIB_N = 6;  W_RIB = [2, 1];  W_PAD_T = 2;  W_PAD_INSET = 5;
module p42_cradle_tilt_wedge() difference() {
    ext_y(-W_W / 2, W_W / 2) polygon([[0, 0], [W_L, 0], [W_L, W_L * tan(W_ANG)]]);
    for (i = [1 : W_RIB_N]) cbox(W_L * i / (W_RIB_N + 1), 0, 0, W_RIB[0], W_W + 2, 2 * W_RIB[1]);
    rot_about([0, 1, 0], -W_ANG, [W_L / 2, 0, (W_L / 2) * tan(W_ANG)]) cbox(W_L / 2, 0, (W_L / 2) * tan(W_ANG), W_L - 2 * W_PAD_INSET, W_W - 2 * W_PAD_INSET, 2 * W_PAD_T);
}

// ---- P43 apex height gauge: 12 square x 120 along Z, foot tip at z 0 rounded R 6, rings 0.6 wide x 0.4 deep ----
G_S = 12;  G_L = 120;  G_FOOT_R = 6;  G_RINGS = [80, 82, 84, 86, 88];  G_RING = [0.6, 0.4];
module p43_apex_height_gauge() difference() {
    intersection() {
        union() { cbox(0, 0, (G_L + G_FOOT_R) / 2, G_S, G_S, G_L - G_FOOT_R); sph(G_FOOT_R, [0, 0, G_FOOT_R], 48); }
        cbox(0, 0, G_L / 2, G_S, G_S, G_L);
    }
    for (z = G_RINGS) difference() { cbox(0, 0, z, G_S + 2, G_S + 2, G_RING[0]); cbox(0, 0, z, G_S - 2 * G_RING[1], G_S - 2 * G_RING[1], G_RING[0] + 1); }
}

// ---- P46 pull clip (TM1 frame of the centre paddle nose): ring over the seam sleeve (z +3..-5), tab to nail height ----
C_RING_IN = [16.5, 11.5];  C_WALL = 1.2;  C_RING_H = 8;  C_TAB_W = 6;  C_TAB_T = 2;  C_TAB_L = 12;  C_EYE_D = 3;
module p46_tip_pull_clip() difference() {
    union() {
        difference() {
            rbox_z(-C_RING_IN[0] / 2 - C_WALL, C_RING_IN[0] / 2 + C_WALL, -C_RING_IN[1] / 2 - C_WALL, C_RING_IN[1] / 2 + C_WALL, -5, -5 + C_RING_H, 2);
            rbox_z(-C_RING_IN[0] / 2, C_RING_IN[0] / 2, -C_RING_IN[1] / 2, C_RING_IN[1] / 2, -6, 4, 1);
        }
        box(-C_TAB_W / 2, C_TAB_W / 2, -C_RING_IN[1] / 2 - C_WALL - C_TAB_T, -C_RING_IN[1] / 2 - C_WALL + 0.01, -5 - C_TAB_L, -5 + 2);
    }
    cyl_y(C_EYE_D / 2, -C_RING_IN[1] / 2 - C_WALL - C_TAB_T - 1, -C_RING_IN[1] / 2 + 1, 0, -5 - C_TAB_L + 3.5, fn = 16);
}

// ---- P48 tip box: 120 x 60 x 25, 8 slots 11 x 5 x 14 deep at Y -8, label recesses 10 x 6 x 0.5 at Y +6 ----
B_X = 120;  B_Y = 60;  B_Z = 25;  B_SLOT = [11, 5, 14];  B_N = 8;  B_SLOT_Y = -8;  B_LABEL = [10, 6, 0.5];  B_LABEL_Y = 6;  B_R = 3;
module p48_tip_box() difference() {
    rbox_z(-B_X / 2, B_X / 2, -B_Y / 2, B_Y / 2, 0, B_Z, B_R);
    for (i = [0 : B_N - 1]) { x = -B_X / 2 + 8 + i * (B_X - 16) / (B_N - 1);
        cbox(x, B_SLOT_Y, B_Z - B_SLOT[2] / 2 + 0.5, B_SLOT[0], B_SLOT[1], B_SLOT[2] + 1);
        cbox(x, B_LABEL_Y, B_Z, B_LABEL[0], B_LABEL[1], 2 * B_LABEL[2]); }
}

if (PART == "foot") p41_cradle_foot_cup();
if (PART == "wedge") p42_cradle_tilt_wedge();
if (PART == "gauge") p43_apex_height_gauge();
if (PART == "clip") p46_tip_pull_clip();
if (PART == "box") p48_tip_box();
if (PART == "all") {
    p41_cradle_foot_cup();
    translate([60, 0, 0]) p42_cradle_tilt_wedge();
    translate([-40, 0, 0]) p43_apex_height_gauge();
    translate([-40, 60, 10]) p46_tip_pull_clip();
    translate([60, 100, 0]) p48_tip_box();
}
