// =====================================================================
//  p32_palm_tray.scad - P32 palm tray (enclosed clamshell, lower half)
//  PROJECT SCRATCH · 05-engineering/cad/frame · units: mm · frame: global (section 2)
//  Sources: mechanical.md section 8.6 (tray, root blocks, clamping), 8.4 (stop screws), 8.1/8.2 (leaf levels,
//  pre-tilt beta), 8.7 (knuckle plate under the tray), 11 P32.
//  Layout: centre box X +/-26, Y +/-40 (section 11: 72 -> 80 so the walls clear the 74.8 slot, C-H3); -Y arm
//  X -24..16 to Y -89.5, +Y arm X -8..24 to Y 82.5 (arms widened / lengthened for the root blocks, C-H4/C-H5);
//  walls 0.8; the centre box's walls run down to the spherical P31/boot/P30 stack (R 93.05 about (0,0,-52.5));
//  the arms have flat floors at Z 38.  Walls end at Z 64.4 under the 1.6 lid (lid top Z 66).
//  Root blocks (section 8.3/8.6): leaf floors L 44.1 / C 56.7 / R 44.0, pre-tilt beta 4.4 / 4.7 / 5.0 deg about X
//  (floor drops toward the paddle), 12.9 x 1.0 leaf slots through both Y walls, 24.2 x 8.4 x 3.5 clamp window,
//  2 M2 inserts at X +/-8.6.  Stop beams: M3 insert vertical, nylon M3 x 10 head down (section 8.4 positions).
//  Ribs (1.2 every 20 mm) are not modelled (mass, C-H8).
// =====================================================================
include <lib_sp1.scad>
RENDER_P32 = true;   // p33_palm_lid.scad includes this file for the outline and sets RENDER_P32 = false

BOX_X = 26;  BOX_Y = 40;  Z_TOP = 64.4;  Z_FLOOR = 38;  WALL = 0.8;  FLOOR_T = 0.8;
ARM_N = [-24, 16, -89.5];        // X0, X1, Y0 of the -Y arm
ARM_P = [-8, 24, 82.5];          // X0, X1, Y1 of the +Y arm
// root blocks: [XC, Y0, Y1, FLOOR, BETA, DROP_TO]  (DROP_TO = +1: floor drops toward +Y)
ROOT_L = [-8, -87.3, -73.3, 44.1, 4.4, 1];
ROOT_C = [0, -59.5, -45.5, 56.7, 4.7, 1];
ROOT_R = [8, 66.7, 80.7, 44.0, 5.0, -1];
ROOT_X = 28;  WIN_X = 24.2;  WIN_Y = 8.4;  WIN_D = 3.5;  SLOT_W = 12.9;  SLOT_H = 1.0;  INS_X = 8.6;  BLOCK_BELOW = 4.1;
C_PEDESTAL_X = [2, 14];          // pedestal under C's block, clear of L's leaf lane (X -14.35..-1.65)
// stop beams: [X, Y, Z0, Z1, X0, X1]  (section 8.4: L at Y -34 / X -11, C at Y -10 / X 0, R at Y +34 / X +8)
STOP_L = [-11, -34.5, 48, 52, -25.5, -3];
STOP_C = [0, -10, 59.5, 63.5, -25.5, 25.5];
STOP_R = [8, 34.5, 48, 52, 1, 25.5];
STOP_W = 7;
LID_INS = [[-24, -20], [24, -20], [-24, 20], [24, 20], [10, -87.5], [-4, 80.5]];   // 6 x M2 for P33
LID_BOSS_D = 4;  LID_BOSS_Z0 = 52;
PLATE_INS = [[0, -41], [0, 41], [23.5, -37], [-23.5, 37], [23.5, 0], [-23.5, 0]];  // 6 x M2 for P30 (= P30 HOLES)
PLATE_BOSS_D = 5;

function z_sph(x, y) = KP_C_Z + sqrt(TRAY_BOT_R * TRAY_BOT_R - x * x - y * y);

module root_block_cuts(rb) {
    xc = rb[0]; y0 = rb[1]; y1 = rb[2]; fl = rb[3]; yc = (y0 + y1) / 2;
    rot_about([1, 0, 0], -rb[5] * rb[4], [xc, yc, fl]) {
        cbox(xc, yc, fl + 50, WIN_X, WIN_Y, 100);                                   // clamp window from the top
        cbox(xc, yc, fl + SLOT_H / 2 - 0.005, SLOT_W, (y1 - y0) + 2, SLOT_H + 0.01);  // leaf slot through both Y walls
        for (sx = [-INS_X, INS_X]) cyl_z(M2_INS_D / 2, fl - M2_INS_L, fl + 0.01, xc + sx, yc, fn = 16);
    }
}

module root_block(rb, pedestal = false) {
    z_top = rb[3] + WIN_D; z_bot = rb[3] - BLOCK_BELOW;
    if (pedestal) {
        box(rb[0] - ROOT_X / 2, rb[0] + ROOT_X / 2, rb[1], rb[2], z_bot, z_top);
        box(C_PEDESTAL_X[0], C_PEDESTAL_X[1], rb[1], rb[2], Z_FLOOR + 0.5, z_bot + 0.01);
    } else box(rb[0] - ROOT_X / 2, rb[0] + ROOT_X / 2, rb[1], rb[2], Z_FLOOR + 0.5, z_top);
}

module p32_palm_tray() difference() {
    union() {
        // centre box: walls from the top down to the spherical underside
        difference() {
            box(-BOX_X, BOX_X, -BOX_Y, BOX_Y, 10, Z_TOP);
            box(-BOX_X + WALL, BOX_X - WALL, -BOX_Y + WALL, BOX_Y - WALL, 10, Z_TOP + 1);
            sph(TRAY_BOT_R, [0, 0, KP_C_Z], 160);
            box(ARM_N[0] + WALL, ARM_N[1] - WALL, -BOX_Y - 1, -BOX_Y + WALL + 0.01, Z_FLOOR + FLOOR_T, Z_TOP + 1);   // openings to the arms
            box(ARM_P[0] + WALL, ARM_P[1] - WALL, BOX_Y - WALL - 0.01, BOX_Y + 1, Z_FLOOR + FLOOR_T, Z_TOP + 1);
        }
        // arms: open-top trays with flat floors
        difference() { box(ARM_N[0], ARM_N[1], ARM_N[2], -BOX_Y + WALL, Z_FLOOR, Z_TOP);
                       box(ARM_N[0] + WALL, ARM_N[1] - WALL, ARM_N[2] + WALL, -BOX_Y + WALL + 1, Z_FLOOR + FLOOR_T, Z_TOP + 1); }
        difference() { box(ARM_P[0], ARM_P[1], BOX_Y - WALL, ARM_P[2], Z_FLOOR, Z_TOP);
                       box(ARM_P[0] + WALL, ARM_P[1] - WALL, BOX_Y - WALL - 1, ARM_P[2] - WALL, Z_FLOOR + FLOOR_T, Z_TOP + 1); }
        root_block(ROOT_L); root_block(ROOT_C, true); root_block(ROOT_R);
        for (s = [STOP_L, STOP_C, STOP_R]) box(s[4], s[5], s[1] - STOP_W / 2, s[1] + STOP_W / 2, s[2], s[3]);
        for (h = LID_INS) cyl_z(LID_BOSS_D / 2, LID_BOSS_Z0, Z_TOP, h[0], h[1], fn = 24);
        for (h = PLATE_INS) difference() {
            cyl_z(PLATE_BOSS_D / 2, z_sph(h[0], h[1]) - 2, max(z_sph(h[0], h[1]) + 6, Z_FLOOR + 1), h[0], h[1], fn = 24);
            sph(TRAY_BOT_R, [0, 0, KP_C_Z], 160);
        }
    }
    root_block_cuts(ROOT_L); root_block_cuts(ROOT_C); root_block_cuts(ROOT_R);
    for (s = [STOP_L, STOP_C, STOP_R]) cyl_z(M3_INS_D / 2, s[2] - 1, s[3] + 1, s[0], s[1], fn = 24);
    for (h = LID_INS) ins_z(M2_INS_D, M2_INS_L, h[0], h[1], Z_TOP);
    for (h = PLATE_INS) cyl_z(M2_INS_D / 2, z_sph(h[0], h[1]) - 3, z_sph(h[0], h[1]) + M2_INS_L, h[0], h[1], fn = 16);
}

if (RENDER_P32) p32_palm_tray();
