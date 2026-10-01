// =====================================================================
//  p27_trim_cleat.scad - P27 trim cleat (elastic trim cord clamp on the mast's +X face)
//  PROJECT SCRATCH · 05-engineering/cad/frame · units: mm · frame: global (section 2)
//  Sources: mechanical.md section 6.7 (cleat on the mast near Z 160, 1 mm cord channel, M3 thumbscrew into an
//  insert), 11 P27.  Placed at Z 140..152 so its outer corner stays inside the R 90 envelope of section 2(c).
// =====================================================================
include <lib_sp1.scad>
X0 = 45;  X1 = 55;  Y = 8;  Z0 = 140;  Z1 = 152;  CH_D = 1.2;  CH_X = 52;  CLAMP_Z = 146;  MOUNT = [[-4, 146], [4, 146]];
module p27_trim_cleat() difference() {
    box(X0, X1, -Y, Y, Z0, Z1);
    cyl_z(CH_D / 2, Z0 - 1, Z1 + 1, CH_X, 0, fn = 16);                                   // cord channel (vertical)
    cyl_y(M3_INS_D / 2, -Y - 1, 0, CH_X, CLAMP_Z, fn = 24);                              // clamp thumbscrew insert
    for (h = MOUNT) { cyl_x(M3_CLEAR / 2, X0 - 1, X1 + 1, h[0], h[1], fn = 24); cyl_x(M3_HEAD_D / 2, X1 - M3_HEAD_H, X1 + 1, h[0], h[1], fn = 24); }
}
p27_trim_cleat();
