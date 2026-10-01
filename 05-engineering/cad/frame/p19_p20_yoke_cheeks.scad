// =====================================================================
//  p19_p20_yoke_cheeks.scad - P19 yoke cheek A (servo side, -Y) and P20 yoke cheek B (idler side, +Y)
//  PROJECT SCRATCH · 05-engineering/cad/frame · units: mm · frame: global (section 2)
//  Sources: mechanical.md section 6.1 (5 mm plates from the elbow axis to X +57, Z 64..104), 5.3 (horn disc
//  on a diam 18 bolt circle, stop lug, zero-pin bore diam 3.1), 5.2 (shoulder screw, M4 nyloc in cheek B), 11 P19/P20.
//  PART = "A" | "B" | "both".  Print flat (XZ plane on the bed).
//  The crossbar P21 ends between the cheeks (Y +/-93) and bolts to 2 M3 inserts per cheek through its end plates
//  (section 11 says 2 per cheek; section 6.1 says 4: C-Y1).  Zero pin at (X +18, Z 84) through cheek A and the
//  cradle's +X flange (section 5.3 gives no position); pin at X +20 since the cradle is 34 wide (rev 2).
// =====================================================================
include <lib_sp1.scad>
PART = "both";

X0 = -18;  X1 = 57;  Z0 = 64;  Z1 = 104;  END_R = 18;  T = 5;
YA = [-98, -93];  YB = [93, 98];
DISC_PCD = 18;                                   // 4 x M3 inserts for P16 (from the -Y face)
ZERO_PIN = [20, 84];  ZERO_PIN_D = 3.1;
LUG_SX = 3;  LUG_R0 = 12.5;  LUG_R1 = 20;  LUG_Y = 3;   // stop lug under the axis, protruding -Y toward the cradle bumpers
BAR_INS = [[51, 72], [51, 100]];                 // crossbar end-plate screws (from the inner face)
BORE_B = 5.0;                                    // reamed bore for the diam 5 shoulder screw (cheek B)

module cheek_profile() hull() { translate([AXIS_X, AXIS_Z]) circle(END_R, $fn = FN); translate([AXIS_X, Z0]) square([X1 - AXIS_X, Z1 - Z0]); }

module p19_yoke_cheek_a() difference() {
    union() {
        ext_y(YA[0], YA[1]) cheek_profile();
        box(-LUG_SX / 2, LUG_SX / 2, YA[0] - LUG_Y, YA[0] + 0.01, AXIS_Z - LUG_R1, AXIS_Z - LUG_R0);
    }
    for (i = [0 : 3]) ins_y(M3_INS_D, M3_INS_L, AXIS_X + DISC_PCD / 2 * cos(45 + 90 * i), AXIS_Z + DISC_PCD / 2 * sin(45 + 90 * i), YA[0], 1);   // 45 deg: clear of the horn's PCD-12 screws
    cyl_y(ZERO_PIN_D / 2, YA[0] - 5, YA[1] + 1, ZERO_PIN[0], ZERO_PIN[1], fn = 24);
    for (h = BAR_INS) ins_y(M3_INS_D, M3_INS_L, h[0], h[1], YA[1], -1);
}

module p20_yoke_cheek_b() difference() {
    ext_y(YB[0], YB[1]) cheek_profile();
    cyl_y(BORE_B / 2, YB[0] - 1, YB[1] + 1, AXIS_X, AXIS_Z, fn = 32);
    cyl_y(M4_NUT_AF / sqrt(3), YB[0] - 1, YB[0] + M4_NUT_H, AXIS_X, AXIS_Z, fn = 6);   // nut trap on the inner (-Y) face
    for (h = BAR_INS) ins_y(M3_INS_D, M3_INS_L, h[0], h[1], YB[0], 1);
}

if (PART == "A" || PART == "both") p19_yoke_cheek_a();
if (PART == "B" || PART == "both") p20_yoke_cheek_b();
