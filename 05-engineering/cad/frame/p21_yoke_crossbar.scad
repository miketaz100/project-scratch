// =====================================================================
//  p21_yoke_crossbar.scad - P21 yoke crossbar with the rail mast
//  PROJECT SCRATCH · 05-engineering/cad/frame · units: mm · frame: global (section 2)
//  Sources: mechanical.md section 6.1 (box beam X 45..57, Z 80..96, 2 mm walls; mast 24 wide x 5 thick, X 40..45,
//  from Z 64 to an R 90 arc about the elbow axis; MGN9 rail on the -X face Z 68..168, 5 M3 inserts at 20 pitch;
//  1 mm reference lip on the -Y edge), 6.3 (down-stop P23 at Z 60..68, up-stop P24 at +28), 6.4/6.7, 11 P21.
//  Beam length 186 between the cheeks' inner faces (section 11's 196 counts the 5 mm cheeks: C-Y2); 3 mm end
//  plates with 2 holes each bolt to the cheek inserts.  Mast starts at Z 58 so the down-stop block can be screwed
//  to it (C-Y3).  Lip in two short segments outside the carriage travel (MGN9C underside clearance H1 ~1 mm [VERIFY]).
//  Print mast face down (the mast's -X face on the bed), beam along the bed's X.  Bed >= 190 mm.
// =====================================================================
include <lib_sp1.scad>

BAR_X0 = 45;  BAR_X1 = 57;  BAR_Z0 = 80;  BAR_Z1 = 96;  BAR_Y = 93;  WALL = 2;  PLUG_L = 10;
END_T = 3;  END_Z0 = 68;  END_Z1 = 104;  END_X0 = 43;  END_X1 = 59;  END_HOLES = [[51, 72], [51, 100]];
MAST_X0 = 40;  MAST_X1 = 45;  MAST_Y = 12;  MAST_Z0 = 58;  MAST_ARC_R = 90;
LIP_Y0 = -5.5;  LIP_Y1 = -4.5;  LIP_X = 1;  LIP_Z = [[68, 73], [134, 160]];
RAIL_INS_Z = [78, 98, 118, 138, 158];                        // = rail holes 10 + 20 k from the rail end at Z 68 [VERIFY]
DOWNSTOP_INS = [[-7, 64], [7, 64]];  UPSTOP_INS = [[-8, 136], [8, 136]];
SHROUD_THRU_Z = [70, 105];  SHROUD_THRU_X = 42.5;
CLEAT_INS = [[-4, 146], [4, 146]];

module mast_profile() intersection() {               // (x, z)
    translate([MAST_X0, MAST_Z0]) square([MAST_X1 - MAST_X0, AXIS_Z + MAST_ARC_R + 1 - MAST_Z0]);
    translate([AXIS_X, AXIS_Z]) circle(MAST_ARC_R, $fn = FN);
}

module p21_yoke_crossbar() difference() {
    union() {
        difference() {                                                                 // box beam, solid plugs at the ends
            box(BAR_X0, BAR_X1, -BAR_Y, BAR_Y, BAR_Z0, BAR_Z1);
            box(BAR_X0 + WALL, BAR_X1 - WALL, -BAR_Y + PLUG_L, BAR_Y - PLUG_L, BAR_Z0 + WALL, BAR_Z1 - WALL);
        }
        for (s = [-1, 1]) box(END_X0, END_X1, min(s * BAR_Y, s * (BAR_Y - END_T)), max(s * BAR_Y, s * (BAR_Y - END_T)), END_Z0, END_Z1);
        ext_y(-MAST_Y, MAST_Y) mast_profile();                                         // mast
        box(MAST_X1 - 0.01, MAST_X1 + 1, -MAST_Y, MAST_Y, BAR_Z0, BAR_Z1);             // 1 mm into the beam wall
        for (lz = LIP_Z) ext_y(LIP_Y0, LIP_Y1) intersection() {                        // rail reference lip (arc-clipped)
            translate([MAST_X0 - LIP_X, lz[0]]) square([LIP_X + 0.01, lz[1] - lz[0]]);
            translate([AXIS_X, AXIS_Z]) circle(MAST_ARC_R, $fn = FN);
        }
    }
    for (z = RAIL_INS_Z) ins_x(M3_INS_D, M3_INS_L, 0, z, MAST_X0, 1);                 // rail inserts, -X face
    for (h = concat(DOWNSTOP_INS, UPSTOP_INS)) ins_x(M3_INS_D, M3_INS_L, h[0], h[1], MAST_X0, 1);
    for (z = SHROUD_THRU_Z) cyl_y(M3_CLEAR / 2, -MAST_Y - 1, MAST_Y + 1, SHROUD_THRU_X, z, fn = 24);   // shroud through-screws
    for (h = CLEAT_INS) ins_x(M3_INS_D, M3_INS_L, h[0], h[1], MAST_X1, -1);           // trim cleat, +X face
    for (s = [-1, 1]) for (h = END_HOLES) cyl_y(M3_CLEAR / 2, min(s * (BAR_Y + 1), s * (BAR_Y - END_T - 1)), max(s * (BAR_Y + 1), s * (BAR_Y - END_T - 1)), h[0], h[1], fn = 24);
}

p21_yoke_crossbar();
