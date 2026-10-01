// =====================================================================
//  p34_root_clamp_bar.scad - P34 root clamp bar (x3), presses the leaf onto the tray root-block floor
//  PROJECT SCRATCH · 05-engineering/cad/frame · units: mm · frame: local (bar centred, z 0..3, groove side at z = 0)
//  Sources: mechanical.md section 8.6 (24 x 8 x 3, groove 12.9 x 0.25 shallower than the 0.30 leaf, 2 x diam 2.4
//  at +/-8.6, M2 x 6 at 0.15 N m), 11 P34.  Same scheme as the tip lead's paddle clamp bar.  Print groove UP.
// =====================================================================
include <lib_sp1.scad>
BAR_X = 24;  BAR_Y = 8;  BAR_T = 3;  GROOVE_W = 12.9;  GROOVE_D = 0.25;  HOLE_D = M2_CLEAR;  HOLE_X = 8.6;
module p34_root_clamp_bar() difference() {
    cbox(0, 0, BAR_T / 2, BAR_X, BAR_Y, BAR_T);
    cbox(0, 0, GROOVE_D / 2 - 0.005, GROOVE_W, BAR_Y + 2, GROOVE_D + 0.01);
    for (sx = [-HOLE_X, HOLE_X]) cyl_z(HOLE_D / 2, -1, BAR_T + 1, sx, 0, fn = 16);
}
p34_root_clamp_bar();
