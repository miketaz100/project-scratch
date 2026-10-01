// =====================================================================
//  p08_p09_yaw_plates.scad - P8 frame yaw plate (under the spine) and P9 carrier yaw plate (on the carrier beam)
//  PROJECT SCRATCH · 05-engineering/cad/frame · units: mm · frame: global (section 2)
//  Sources: mechanical.md section 5.4 (70 x 70 x 6, yaw axis X -25; P9: 4 x diam 3.4 on a 40 x 40 square; P8: 8 M3
//  inserts on diam 56.6 at 45 deg; 2 x M5 slots each), 2 (P9 Z 184..190, P8 Z 190..196), 11 P8/P9.
//  PART = "frame" | "carrier" | "both".
//  Both plates are notched for the 2020 post (X -70..-50, Y +/-10), which passes through them (section 2: post to
//  Z 198, plates from Z 184).  The 180 deg insert at (-53.3, 0) falls in the notch: P8 carries 7 inserts (C-F5).
// =====================================================================
include <lib_sp1.scad>
PART = "both";
S = 70;  T = 6;  R = 4;
F_Z0 = 190;  F_Z1 = 196;  BC_D = 56.6;  N = 8;  F_SLOT_X = [-45, -5];  SLOT_L = 10;
C_Z0 = 184;  C_Z1 = 190;  SQ = 40;  C_SLOT_Y = [-20, 20];

module p08_frame_yaw_plate() difference() {
    rbox_z(YAW_X - S / 2, YAW_X + S / 2, -S / 2, S / 2, F_Z0, F_Z1, R);
    post_notch(F_Z0, F_Z1);
    for (i = [0 : N - 1]) {
        hx = YAW_X + BC_D / 2 * cos(45 + 45 * i); hy = BC_D / 2 * sin(45 + 45 * i);
        if (!(hx < POST[1] + M3_INS_D / 2 + 1 && abs(hy) < EXT_SOCK / 2 + M3_INS_D / 2 + 1)) ins_z(M3_INS_D, M3_INS_L, hx, hy, F_Z0, false);
    }
    for (xs = F_SLOT_X) hull() { cyl_z(M5_CLEAR / 2, F_Z0 - 1, F_Z1 + 1, xs - SLOT_L / 2, 0, fn = 24); cyl_z(M5_CLEAR / 2, F_Z0 - 1, F_Z1 + 1, xs + SLOT_L / 2, 0, fn = 24); }
}
module p09_carrier_yaw_plate() difference() {
    rbox_z(YAW_X - S / 2, YAW_X + S / 2, -S / 2, S / 2, C_Z0, C_Z1, R);
    post_notch(C_Z0, C_Z1);
    for (dx = [-SQ / 2, SQ / 2]) for (dy = [-SQ / 2, SQ / 2]) cyl_z(M3_CLEAR / 2, C_Z0 - 1, C_Z1 + 1, YAW_X + dx, dy, fn = 24);
    for (ys = C_SLOT_Y) hull() { cyl_z(M5_CLEAR / 2, C_Z0 - 1, C_Z1 + 1, YAW_X, ys - SLOT_L / 2, fn = 24); cyl_z(M5_CLEAR / 2, C_Z0 - 1, C_Z1 + 1, YAW_X, ys + SLOT_L / 2, fn = 24); }
}
if (PART == "frame" || PART == "both") p08_frame_yaw_plate();
if (PART == "carrier" || PART == "both") p09_carrier_yaw_plate();
