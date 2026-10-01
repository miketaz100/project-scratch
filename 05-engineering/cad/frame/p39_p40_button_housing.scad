// =====================================================================
//  p39_p40_button_housing.scad - P39 handheld hold-to-run button housing half A, P40 half B
//  PROJECT SCRATCH · 05-engineering/cad/frame · units: mm · frame: local (axis along Z, cup at the top z 86..110,
//  split plane X = 0; half A is x >= 0, half B is x <= 0).  Print split face down.
//  Sources: mechanical.md section 3.3 (hold-to-run handheld on a 1.5 m cable, gland at the handle, zip-tie anchor),
//  11 P39 (diam 36 x 110 split, 2 mm rim wall, 2.0 button deck with a diam 29.6 hole -> 30.0 verified, uxcell 30 mm button),
//  button face 3.0 below the rim, 2 x diam 3.4 counterbored, gland boss diam 12 x 10 with diam 6 bore, zip-tie anchor
//  bar 8 above the gland), P40 (mirror with 2 M3 inserts, alignment pins diam 3 x 3).  PART = "A" | "B" | "both".
//  CONFLICT C-E3: the verified button body is 33 mm max diameter and 26 tall; the cup bore under the deck is 32 mm.
// =====================================================================
include <lib_sp1.scad>
PART = "both";
L = 110;  CUP_D = 36;  CUP_H = 24;  RIM_WALL = 2;  DECK_T = 2;  DECK_BELOW_RIM = 3;  BTN_HOLE = 30.2;   // 30.0 mounting hole (bom-verified.md 11 item 4): print 30.2, ream to 30.0
GRIP_D = 30;  GRIP_WALL = 2;  GLAND_D = 12;  GLAND_H = 10;  GLAND_BORE = 6;
ANCHOR_Z = 18;  ANCHOR = [4, 3];  SCREW_Z = [30, 80];  SCREW_Y = 0;  BOSS_D = 8;  PIN_D = 3;  PIN_H = 3;  PIN_Z = [45, 65];  PIN_Y = 0;  PIN_BOSS_D = 6;
Z_CUP0 = L - CUP_H;  DECK_TOP = L - DECK_BELOW_RIM;

module housing_full() union() {
    difference() {
        union() {
            cyl_z(CUP_D / 2, Z_CUP0, L);
            hull() { cyl_z(CUP_D / 2, Z_CUP0 - 0.01, Z_CUP0); cyl_z(GRIP_D / 2, Z_CUP0 - 8, Z_CUP0 - 8 + 0.01); }
            cyl_z(GRIP_D / 2, GLAND_H, Z_CUP0 - 8 + 0.01);
            cyl_z(GLAND_D / 2, 0, GLAND_H + 0.01);
            for (zz = SCREW_Z) cyl_x(BOSS_D / 2, -GRIP_D / 2 + 1, GRIP_D / 2 - 1, SCREW_Y, zz);           // split-plane screw bosses
        }
        cyl_z(CUP_D / 2 - RIM_WALL, DECK_TOP, L + 1);                                                       // thumb well
        cyl_z(BTN_HOLE / 2, DECK_TOP - DECK_T - 1, DECK_TOP + 1);                                           // button hole [VERIFY]
        cyl_z(CUP_D / 2 - RIM_WALL, Z_CUP0 + 2, DECK_TOP - DECK_T + 0.01);                                  // cup interior
        cyl_z(GRIP_D / 2 - GRIP_WALL, GLAND_H + 2, Z_CUP0 + 2 + 0.01);                                      // grip interior
        cyl_z(GLAND_BORE / 2, -1, GLAND_H + 3);                                                              // cable bore
        cbox(0, GRIP_D / 2 - 1, ANCHOR_Z, ANCHOR[0], 6, ANCHOR[1]);                                          // zip-tie anchor slot
    }
    for (zz = PIN_Z) cyl_x(PIN_BOSS_D / 2, -GRIP_D / 2 + 1, GRIP_D / 2 - 1, PIN_Y, zz);                      // alignment-pin bosses
}
module p39_button_housing_half_a() difference() {
    intersection() { housing_full(); box(0, 40, -40, 40, -1, L + 1); }
    for (zz = SCREW_Z) { cyl_x(M3_CLEAR / 2, -1, 40, SCREW_Y, zz, fn = 24); cyl_x(M3_HEAD_D / 2, BOSS_D / 2 + 1, 40, SCREW_Y, zz, fn = 24); }
    for (zz = PIN_Z) cyl_x((PIN_D + 0.2) / 2, -1, PIN_H + 0.2, PIN_Y, zz, fn = 16);
}
module p40_button_housing_half_b() union() {
    difference() {
        intersection() { housing_full(); box(-40, 0, -40, 40, -1, L + 1); }
        for (zz = SCREW_Z) ins_x(M3_INS_D, M3_INS_L + 1, SCREW_Y, zz, 0, -1);
    }
    for (zz = PIN_Z) cyl_x(PIN_D / 2, -1, PIN_H, PIN_Y, zz, fn = 16);
}
if (PART == "A" || PART == "both") p39_button_housing_half_a();
if (PART == "B" || PART == "both") p40_button_housing_half_b();
