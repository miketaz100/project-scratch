// =====================================================================
//  p16_horn_adapter_disc.scad - P16 horn adapter disc (XL330 horn -> yoke cheek A)
//  PROJECT SCRATCH · 05-engineering/cad/frame · units: mm · frame: global (disc at Y -101..-98 on the elbow axis)
//  Sources: mechanical.md section 5.3 (diam 24 x 3, screws to the horn's M2 holes [VERIFY], cheek A bolts to it with
//  4 x M3 on a diam 18 circle, centre relief diam 6 for the horn screw), 11 P16.  Print flat.
//  Horn (bom-verified.md 11 item 3): diam 16 x 3, 4 x diam 1.6 on PCD 12 at 90 deg with one hole on the body's long
//  axis (Z), M2 x 6 tapping screws ONLY (3 mm disc + 3 mm engagement; M2 x 8 bottoms into the gearbox).  The 4 x M3
//  cheek screws on PCD 18 sit at 45 deg so they clear the horn screws (centres 3.6 mm apart).
// =====================================================================
include <lib_sp1.scad>
D = 24;  Y0 = -101;  Y1 = -98;  CENTRE_D = 6;  HORN_PCD = 12;  HORN_HOLE_D = 2.2;  CHEEK_PCD = 18;  CHEEK_ANG0 = 45;
module p16_horn_adapter_disc() difference() {
    cyl_y(D / 2, Y0, Y1, AXIS_X, AXIS_Z);
    cyl_y(CENTRE_D / 2, Y0 - 1, Y1 + 1, AXIS_X, AXIS_Z, fn = 24);
    for (i = [0 : 3]) cyl_y(HORN_HOLE_D / 2, Y0 - 1, Y1 + 1, AXIS_X + HORN_PCD / 2 * cos(90 * i), AXIS_Z + HORN_PCD / 2 * sin(90 * i), fn = 16);
    for (i = [0 : 3]) cyl_y(M3_CLEAR / 2, Y0 - 1, Y1 + 1, AXIS_X + CHEEK_PCD / 2 * cos(CHEEK_ANG0 + 90 * i), AXIS_Z + CHEEK_PCD / 2 * sin(CHEEK_ANG0 + 90 * i), fn = 24);
}
p16_horn_adapter_disc();
