// =====================================================================
//  p23_p24_rail_stops.scad - P23 rail down-stop block (thumbscrew) and P24 rail up-stop block (TPU pad)
//  PROJECT SCRATCH · 05-engineering/cad/frame · units: mm · frame: global (section 2)
//  Sources: mechanical.md section 6.3 (down-stop Z 60..68 below the rail end, M3 brass insert vertical, M3 x 16
//  knurled thumbscrew + jam nut, tip at X 29 / Z 69 under the riser's foot tab; up-stop 2 mm TPU pad 28 above the
//  default down-stop: carriage top 103 -> pad face at Z 131), 11 P23/P24.  PART = "down" | "up" | "both".
//  Both blocks are 12 (X 28..40) x 20 x 8 and screw to the mast's -X face (X 40) with 2 x M3 x 8 (counterbored).
//  The up-stop straddles the rail (channel Y +/-6, clear of the 1 mm reference lip).
// =====================================================================
include <lib_sp1.scad>
PART = "both";

// P23
D_X0 = 28;  D_X1 = 40;  D_Y = 10;  D_Z0 = 60;  D_Z1 = 68;  D_SCREW_X = 30.5;  D_MOUNT = [[-7, 64], [7, 64]];
// P24
U_X0 = 28;  U_X1 = 40;  U_Y = 10;  U_Z0 = 132;  U_Z1 = 140;  PAD_T = 2;  PAD_RECESS = 1;  PAD_X = [28, 33];
RAIL_CH_Y = 6;  RAIL_CH_X0 = 33;  U_MOUNT = [[-8, 136], [8, 136]];

module p23_rail_down_stop() difference() {
    box(D_X0, D_X1, -D_Y, D_Y, D_Z0, D_Z1);
    cyl_z(M3_INS_D / 2, D_Z0 - 1, D_Z1 + 1, D_SCREW_X, 0, fn = 24);                 // brass insert, thumbscrew from above
    for (h = D_MOUNT) { cyl_x(M3_CLEAR / 2, D_X0 - 1, D_X1 + 1, h[0], h[1], fn = 24); cyl_x(M3_HEAD_D / 2, D_X0 - 1, D_X0 + M3_HEAD_H, h[0], h[1], fn = 24); }
}
module p24_rail_up_stop() difference() {
    box(U_X0, U_X1, -U_Y, U_Y, U_Z0, U_Z1);
    box(RAIL_CH_X0, U_X1 + 1, -RAIL_CH_Y, RAIL_CH_Y, U_Z0 - 1, U_Z1 + 1);            // rail channel
    box(PAD_X[0] - 1, PAD_X[1], -U_Y + 2, U_Y - 2, U_Z0 - 1, U_Z0 + PAD_RECESS);     // TPU pad recess (pad 2 thick, 1 proud)
    for (h = U_MOUNT) { cyl_x(M3_CLEAR / 2, U_X0 - 1, U_X1 + 1, h[0], h[1], fn = 24); cyl_x(M3_HEAD_D / 2, U_X0 - 1, U_X0 + M3_HEAD_H, h[0], h[1], fn = 24); }
}
if (PART == "down" || PART == "both") p23_rail_down_stop();
if (PART == "up" || PART == "both") p24_rail_up_stop();
