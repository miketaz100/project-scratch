// =====================================================================
//  p26_carriage_riser.scad - P26 carriage riser (L-bracket) with foot tab, pointer fin and trim hook
//  PROJECT SCRATCH · 05-engineering/cad/frame · units: mm · frame: global (section 2)
//  Sources: mechanical.md section 6.2 (20 x 34 x 3 plate on the MGN9C face at X 30, 4 x M3 x 6 on the 15 x 10
//  pattern [VERIFY]; arm 32 x 12 x 4 back over the palm to the upper seat), 6.3 (foot tab on the down-stop
//  thumbscrew tip at X 29 / Z 69), 6.4 (pointer fin, 0.6 edge 1 mm from the scale), 6.7 (trim hook), 7.4, 11 P26.
//  Plate Z 71.5..103 (ends at the block top so the carriage, not the plate, meets the up-stop pad).  Arm at
//  Z 80..84 lies on the P47 filler in the P28 pocket; holes at X +14 / +4.  Hook on a +Y ear (clear of P24).
//  Print on its side.
// =====================================================================
include <lib_sp1.scad>
PL_X0 = 27;  PL_X1 = 30;  PL_Y = 10;  PL_Z0 = 71.5;  PL_Z1 = 103;  CARR_ZC = 88.5;
TAB_X1 = 33;  TAB_Y = 4;  TAB_Z0 = 69;
ARM_X0 = -5;  ARM_Y = 6;  ARM_Z0 = 80;  ARM_Z1 = 84;  ARM_HOLES = [14, 4];
FIN_Y0 = -19.5;  FIN_Y1 = -10;  FIN_Z = 75;  FIN_T = 1.0;  FIN_EDGE_T = 0.6;  FIN_EDGE_L = 4;
HOOK_D = 2;  HOOK_H = 4;  HOOK_HEAD = 3.5;  HOOK_Y = 12.5;
module p26_carriage_riser() difference() {
    union() {
        box(PL_X0, PL_X1, -PL_Y, PL_Y, PL_Z0, PL_Z1);                                            // plate on the block face
        box(PL_X0, TAB_X1, -TAB_Y, TAB_Y, TAB_Z0, PL_Z0 + 0.01);                                 // foot tab (rests on the thumbscrew)
        box(ARM_X0, PL_X0 + 0.01, -ARM_Y, ARM_Y, ARM_Z0, ARM_Z1);                                // arm to the wrist seat
        box(PL_X0, PL_X1, FIN_Y0 + FIN_EDGE_L, FIN_Y1 + 0.01, FIN_Z - FIN_T / 2, FIN_Z + FIN_T / 2);          // pointer fin
        box(PL_X0, PL_X1, FIN_Y0, FIN_Y0 + FIN_EDGE_L + 0.01, FIN_Z - FIN_EDGE_T / 2, FIN_Z + FIN_EDGE_T / 2); // 0.6 edge
        box(PL_X0, PL_X1, PL_Y - 0.01, HOOK_Y + 2, PL_Z1 - 3, PL_Z1);                            // hook ear
        cyl_z(HOOK_D / 2, PL_Z1 - 0.01, PL_Z1 + HOOK_H, (PL_X0 + PL_X1) / 2, HOOK_Y, fn = 16);  // trim-cord hook
        cyl_z(HOOK_HEAD / 2, PL_Z1 + HOOK_H - 0.01, PL_Z1 + HOOK_H + 1.5, (PL_X0 + PL_X1) / 2, HOOK_Y, fn = 16);
    }
    mgn9c_holes_x(PL_X1, 0, CARR_ZC);                                                            // 4 x diam 3.4, 15 x 10 [VERIFY]
    for (x = ARM_HOLES) cyl_z(M3_CLEAR / 2, ARM_Z0 - 1, ARM_Z1 + 1, x, 0, fn = 24);
}
p26_carriage_riser();
