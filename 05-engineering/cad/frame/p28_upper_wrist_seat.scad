// =====================================================================
//  p28_upper_wrist_seat.scad - P28 upper wrist seat with weight post (+ P29 weight cap, P47 load-cell filler)
//  PROJECT SCRATCH · 05-engineering/cad/frame · units: mm · frame: global (section 2); P29 / P47 local
//  Sources: mechanical.md section 7.1 (seat), 6.6 (post), 7.4 (load-cell pocket), 11 P28/P29/P47.
//  PART = "seat" | "cap" | "filler" | "assembly"
//  CONFLICTS: the 41 x 13 x 8 load-cell pocket and the diam 8 post cannot share X 0 / Y 0 (C-H6):
//  the post is offset to Y +13; the pocket floor carries one M3 insert at X -14 (section 11 lists 1 insert).
// =====================================================================
include <lib_sp1.scad>
PART = "seat";

// ---- seat plate (section 7.1) ----
D = 44;  Z0 = 69;  Z1 = 74;                      // diam 44 x 5, bottom = contact face at the seat plane Z 69
CONE_D0 = 18.4;  CONE_D1 = 12.4;  CONE_H = 3.1;   // conical recess
MAG_D = 9.6;  MAG_H = 1.6;                        // K&J D61 pocket at the recess floor
KEY_W = 3.3;  KEY_D = 2.2;  KEY_R0 = 14;  KEY_R1 = 22;   // radial key slot on +X (peg at r 17 on the lid)
// ---- load-cell pocket block (section 7.4): 41 x 13 x 8 pocket open at the top and toward +X (riser arm side) ----
PK_X = 45;  PK_Y = 17;  PK_Z1 = 82;  POCKET = [41, 13, 8];  SEAT_SCREW_X = -14;
// ---- weight post (section 6.6): diam 8 x 34, M3 insert at the top ----
POST_D = 8;  POST_XY = [0, 13];  POST_Z1 = 108;
EYE_D = 2;  EYE_XY = [-12, 16];                   // tether eyelet (ADDENDUM-1: 25 mm tether)

module p28_upper_wrist_seat() difference() {
    union() {
        cyl_z(D / 2, Z0, Z1);
        cbox(0, 0, (Z1 + PK_Z1) / 2, PK_X, PK_Y, PK_Z1 - Z1 + 0.02);
        cyl_z(POST_D / 2, Z1 - 0.01, POST_Z1, POST_XY[0], POST_XY[1]);
    }
    cyl_z(CONE_D0 / 2, Z0 - 0.01, Z0 + CONE_H, r2 = CONE_D1 / 2);                     // 45 deg recess
    cyl_z(MAG_D / 2, Z0 + CONE_H - 0.01, Z0 + CONE_H + MAG_H, fn = 32);               // D61 pocket (0.3 roof: C-H7)
    box(KEY_R0, KEY_R1 + 1, -KEY_W / 2, KEY_W / 2, Z0 - 1, Z0 + KEY_D);               // key slot
    box(-POCKET[0] / 2, POCKET[0] / 2 + 5, -POCKET[1] / 2, POCKET[1] / 2, Z1, PK_Z1 + 1);   // load-cell / filler pocket
    ins_z(M3_INS_D, M3_INS_L, SEAT_SCREW_X, 0, Z1);                                   // filler screw
    ins_z(M3_INS_D, M3_INS_L, POST_XY[0], POST_XY[1], POST_Z1);                       // weight-cap thumbscrew
    cyl_z(EYE_D / 2, Z0 - 1, Z1 + 1, EYE_XY[0], EYE_XY[1], fn = 16);                  // tether eyelet
}

// ---- P29 weight cap (section 6.6, 11): local frame, disc z 0..4 ----
CAP_D = 16;  CAP_T = 4;  CAP_HOLE = M3_CLEAR;  KNURL_N = 12;  KNURL_D = 1.2;
module p29_weight_cap() difference() {
    cyl_z(CAP_D / 2, 0, CAP_T);
    cyl_z(CAP_HOLE / 2, -1, CAP_T + 1, fn = 24);
    for (i = [0 : KNURL_N - 1]) cyl_z(KNURL_D / 2, -1, CAP_T + 1, CAP_D / 2 * cos(360 * i / KNURL_N), CAP_D / 2 * sin(360 * i / KNURL_N), fn = 12);
}

// ---- P47 load-cell filler bar (section 7.4, 11): local frame, bar along X, z 0..6 ----
FIL_L = 40;  FIL_W = 12;  FIL_T = 6;
FIL_HOLES = [[-14, M3_CLEAR], [14, M3_PILOT], [4, M3_PILOT]];   // -14 clears to the seat insert; +14/+4 pilots for the P26 arm screws
module p47_load_cell_filler() difference() {
    cbox(0, 0, FIL_T / 2, FIL_L, FIL_W, FIL_T);
    for (h = FIL_HOLES) cyl_z(h[1] / 2, -1, FIL_T + 1, h[0], 0, fn = 24);
}

if (PART == "seat") p28_upper_wrist_seat();
if (PART == "cap") p29_weight_cap();
if (PART == "filler") p47_load_cell_filler();
if (PART == "assembly") {
    color("orange") p28_upper_wrist_seat();
    color("gray") translate([POST_XY[0], POST_XY[1], POST_Z1]) p29_weight_cap();
    color("silver") translate([0, 0, Z1]) p47_load_cell_filler();
}
