// =====================================================================
//  p22_rail_shroud.scad - P22 rail shroud G4 (lower rail, down-stop block and carriage at the down-stop)
//  PROJECT SCRATCH · 05-engineering/cad/frame · units: mm · frame: global (section 2)
//  Sources: mechanical.md section 5.5 G4 (U-channel on the mast, closed bottom, 2 mm walls, 25 mm riser slot),
//  6.4 (scale strip in a dovetail on the side face), 11 P22.
//  AS MODELLED: floor + two side walls + a back web behind the mast (notched for the crossbar).  A front (-X)
//  wall is impossible: the palm lid (X to 27.2, Z to 72) rises 28 mm through that space (C-Y4).  Floor at Z 64
//  because the knuckle plate's +X edge reaches Z 61.2 at the float up-stop; the down-stop block P23 plugs the
//  floor cut-out.  Scale dovetail on the OUTSIDE of the -Y wall; the riser's pointer fin passes a slot in that wall.
// =====================================================================
include <lib_sp1.scad>

X0 = 27.5;  X1 = 45;  Y = 17;  Z0 = 64;  Z1 = 108;  WALL = 2;
DOVE_X0 = 31;  DOVE_X1 = 39;  DOVE_Y0 = -21;  DOVE_Y1 = -17;          // boss outside the -Y wall
DOVE_W_OPEN = 5.0;  DOVE_W_BOT = 6.5;  DOVE_D = 1.0;  DOVE_Z0 = 66;  DOVE_Z1 = 106;   // groove (wider inside), along Z
LOCK_Z = 80;                                                          // M3 lock thumbscrew through the boss into the strip slot
FIN_SLOT = [26.5, 30.5, 68, 106];                                     // X0, X1, Z0, Z1 slot in the -Y wall for the pointer fin
MAST_CUT = [39, 46, 12.5];  STOP_CUT = [27, 41, 10.5];                // floor cut-outs: mast (X, X, +/-Y), down-stop block
BACK_X1 = 47;  BACK_NOTCH = [79.5, 96.5];                             // back web behind the mast, notched for the crossbar
THRU_Z = [70, 105];  THRU_X = 42.5;                                   // M3 through both walls and the mast (P21)

module p22_rail_shroud() difference() {
    union() {
        difference() { box(X0, X1, -Y, Y, Z0, Z1); box(X0 - 1, X1 + 1, -Y + WALL, Y - WALL, Z0 + WALL, Z1 + 1); }
        box(X1 - 0.01, BACK_X1, -Y, Y, Z0, BACK_NOTCH[0]);
        box(X1 - 0.01, BACK_X1, -Y, Y, BACK_NOTCH[1], Z1);
        box(DOVE_X0, DOVE_X1, DOVE_Y0, DOVE_Y1 + 0.01, Z0, Z1);
    }
    box(MAST_CUT[0], MAST_CUT[1], -MAST_CUT[2], MAST_CUT[2], Z0 - 1, Z1 + 1);
    box(STOP_CUT[0], STOP_CUT[1], -STOP_CUT[2], STOP_CUT[2], Z0 - 1, Z0 + WALL + 1);
    box(FIN_SLOT[0], FIN_SLOT[1], -Y - 1, -Y + WALL + 1, FIN_SLOT[2], FIN_SLOT[3]);
    dcx = (DOVE_X0 + DOVE_X1) / 2;  yo = DOVE_Y0;  yb = DOVE_Y0 + DOVE_D;
    translate([0, 0, DOVE_Z0]) linear_extrude(DOVE_Z1 - DOVE_Z0)
        polygon([[dcx - DOVE_W_OPEN / 2, yo - 1], [dcx + DOVE_W_OPEN / 2, yo - 1], [dcx + DOVE_W_OPEN / 2, yo],
                 [dcx + DOVE_W_BOT / 2, yb], [dcx - DOVE_W_BOT / 2, yb], [dcx - DOVE_W_OPEN / 2, yo]]);
    cyl_y(M3_CLEAR / 2, DOVE_Y0 - 1, -Y + WALL + 1, dcx, LOCK_Z, fn = 24);
    for (z = THRU_Z) cyl_y(M3_CLEAR / 2, -Y - 1, Y + 1, THRU_X, z, fn = 24);
}

p22_rail_shroud();
