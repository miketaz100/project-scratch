// =====================================================================
//  p15_idler_housing.scad - P15 idler housing (625-2RS bearing for the yoke's +Y shoulder screw)
//  PROJECT SCRATCH · 05-engineering/cad/frame · units: mm · frame: global (section 2)
//  Sources: mechanical.md section 5.2 (625-2RS 5 x 16 x 5 pressed in, housing on the +Y drop leg through 2 M3 slots
//  +/-1.5 in X and Z), 11 P15 (30 x 14 x 40, bore diam 16.0 x 5, shoulder relief diam 8).  Print bore axis vertical.
//  Housing Y 116..130 against the P12 flange (section 2's "idler at Y +101..+111" cannot touch the leg: C-S4).
//  The two "slots" are diam 6.4 holes (3.4 + 2 x 1.5) with washer seats, giving +/-1.5 in both X and Z.
// =====================================================================
include <lib_sp1.scad>
X = 30;  Y0 = 116;  Y1 = 130;  Z0 = 64;  Z1 = 104;  END_R = 26;  BRG_D = 16.0;  BRG_W = 5;  RELIEF_D = 8;
SLOT_D = M3_CLEAR + 3;  SLOT_AT = [[0, 70], [0, 98]];
module p15_idler_housing() difference() {
    intersection() { box(-X / 2, X / 2, Y0, Y1, Z0, Z1); cyl_y(END_R, Y0 - 1, Y1 + 1, AXIS_X, AXIS_Z); }
    cyl_y(BRG_D / 2, Y0 - 1, Y0 + BRG_W, AXIS_X, AXIS_Z);                 // bearing bore (press fit, test print first)
    cyl_y(RELIEF_D / 2, Y0 - 1, Y1 + 1, AXIS_X, AXIS_Z);                  // shoulder / screw-head relief
    for (h = SLOT_AT) { cyl_y(SLOT_D / 2, Y0 - 1, Y1 + 1, h[0], h[1], fn = 24); cyl_y(M3_HEAD_D / 2 + 1.5, Y0 - 1, Y0 + 4, h[0], h[1], fn = 24); }
}
p15_idler_housing();
