// =====================================================================
//  p10_reset_tab.scad - P10 reset tab and spine end cap (front end of the 2020 spine at X +30)
//  PROJECT SCRATCH · 05-engineering/cad/frame · units: mm · frame: global (section 2)
//  Sources: mechanical.md section 4.7 (reset tab on the spine), 11 P10 (25 x 30 x 25, socket, finger tab R 5).
//  The spine is 80 long from X -50 (ADDENDUM-1 D8), so its front end is at X +30 (section 2 / 4.7 say X -15: C-F2).
// =====================================================================
include <lib_sp1.scad>
X0 = 20;  X1 = 45;  Y = 30;  Z0 = 194;  Z1 = 219;  SOCK_DEPTH = 10;  R = 5;  SPINE_ZC = 206;
module p10_reset_tab() difference() {
    intersection() {
        ext_x(X0, X1) rrect(0, (Z0 + Z1) / 2, Y, Z1 - Z0, R);
        rbox_z(X0 - R, X1, -Y / 2, Y / 2, Z0 - 1, Z1 + 1, R);
    }
    box(X0 - 1, X0 + SOCK_DEPTH, -EXT_SOCK / 2, EXT_SOCK / 2, SPINE_ZC - EXT_SOCK / 2, SPINE_ZC + EXT_SOCK / 2);
}
p10_reset_tab();
