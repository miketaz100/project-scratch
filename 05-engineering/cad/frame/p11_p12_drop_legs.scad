// =====================================================================
//  p11_p12_drop_legs.scad - P11 drop leg, servo side (-Y) and P12 drop leg, idler side (+Y, mirror)
//  PROJECT SCRATCH · 05-engineering/cad/frame · units: mm · frame: global (section 2)
//  Sources: mechanical.md section 5.2 (legs bolt to the 270 mm beam's end faces: M5 end-tap screw + 2 T-nut screws,
//  come down and forward to the elbow axis; servo cradle on the -Y foot, idler housing on the +Y foot), 2 (legs at
//  Y +/-115..135), 11 P11/P12.  PART = "servo" | "idler" | "both".  Print on the side.
//  Top block: socket over the beam end (20 deep) with the end-screw wall at Y -139..-135; bar 12 x 20 down behind
//  the cradle (X -27..-15); foot flange 5 thick at Y -135..-130, X -35..+15, Z 70..116, carrying 4 M3 inserts for
//  P13 (P12: 2 inserts for P15).  Envelope 51 x 24 x 115 vs section 11's 50 x 20 x 105 (C-F6).
// =====================================================================
include <lib_sp1.scad>
PART = "both";
TOP_X0 = -36;  TOP_X1 = -14;  TOP_Y0 = -139;  TOP_Y1 = -115;  TOP_Z0 = 163;  TOP_Z1 = 185;  SOCK_L = 20;
TNUT_Y = [-125, -119];
BAR_X0 = -29;  BAR_X1 = -17;  BAR_Y0 = -136.5;  BAR_Y1 = -115;  BAR_Z0 = 70;   // behind the 34-wide cradle (X -17)
FL_X0 = -35;  FL_X1 = 19;  FL_Y0 = -136.5;  FL_Y1 = -131.5;  FL_Z0 = 70;  FL_Z1 = 116;   // FRAME-ONLY part (crown mount supersedes it)
FOOT_INS = [[-14, 80], [14, 80], [-14, 104], [14, 104]];   // P13 servo cradle (clear of the XL330 16 x 30 back-face pattern)
FOOT_INS_IDLER = [[0, 70], [0, 98]];                        // P15 idler housing
BEAM_CX = (BEAM[0] + BEAM[1]) / 2;  BEAM_CZ = (BEAM[4] + BEAM[5]) / 2;

module drop_leg(holes) difference() {
    union() {
        box(TOP_X0, TOP_X1, TOP_Y0, TOP_Y1, TOP_Z0, TOP_Z1);
        box(BAR_X0, BAR_X1, BAR_Y0, BAR_Y1, BAR_Z0, TOP_Z0 + 0.01);
        box(FL_X0, FL_X1, FL_Y0, FL_Y1, FL_Z0, FL_Z1);
        box(BAR_X0, BAR_X1, FL_Y0, FL_Y1 + 0.01, FL_Z0, TOP_Z0);
    }
    socket_2020_y(BEAM_CX, BEAM_CZ, TOP_Y1 - SOCK_L, TOP_Y1 + 1);
    cyl_y(M5_CLEAR / 2, TOP_Y0 - 1, TOP_Y1, BEAM_CX, BEAM_CZ, fn = 24);                    // M5 into the extrusion's end tap
    cyl_y(M5_HEAD_D / 2, TOP_Y0 - 1, TOP_Y0 + M5_HEAD_H, BEAM_CX, BEAM_CZ, fn = 32);
    for (yy = TNUT_Y) cyl_z(M5_CLEAR / 2, BEAM_CZ, TOP_Z1 + 1, BEAM_CX, yy, fn = 24);        // 2 T-nut screws into the top slot
    for (h = holes) ins_y(M3_INS_D, M3_INS_L, h[0], h[1], FL_Y1, -1);                        // flange inserts (+Y face)
}
module p11_drop_leg_servo() drop_leg(FOOT_INS);
module p12_drop_leg_idler() mirror_y() drop_leg(FOOT_INS_IDLER);
if (PART == "servo" || PART == "both") p11_drop_leg_servo();
if (PART == "idler" || PART == "both") p12_drop_leg_idler();
