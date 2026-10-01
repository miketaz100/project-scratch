// =====================================================================
//  p17_p18_guard_caps.scad - P17 guard cap G2 (servo) and P18 guard cap G3 (idler, mirror)
//  PROJECT SCRATCH · 05-engineering/cad/frame · units: mm · frame: global (section 2)
//  Sources: mechanical.md section 5.5 G2/G3 (2 mm shell under the cradle, 15 deg drafted sides, R 3 edges, cheek
//  passes >= 10 mm clear), 11 P17/P18 (60 x 40 x 30).  PART = "servo" | "idler" | "both".  Print open side up.
//  Modelled as a drafted tub Z 40..70 under the cradle / housing, 60 x 32 (not 40: the +Y wall would be inside
//  cheek A's sweep, C-S5), 2 mm walls, two M3 through-holes at Z 66 for its mounting.  R 3 edge rounds not modelled.
// =====================================================================
include <lib_sp1.scad>
PART = "both";
TOP_X = 60;  TOP_Y = 32;  YC = -119;  Z0 = 40;  Z1 = 70;  DRAFT = 15;  WALL = 2;  R = 6;  MOUNT_Z = 66;  MOUNT_X = [-25, 25];
module guard_cap() {
    d = 2 * (Z1 - Z0) * tan(DRAFT);
    difference() {
        rrect_frustum(0, YC, TOP_X - d, TOP_Y - d, TOP_X, TOP_Y, R, Z0, Z1);
        rrect_frustum(0, YC, TOP_X - d - 2 * WALL, TOP_Y - d - 2 * WALL, TOP_X - 2 * WALL, TOP_Y - 2 * WALL, max(R - WALL, 1), Z0 + WALL, Z1 + 1);
        for (x = MOUNT_X) cyl_y(M3_CLEAR / 2, YC - TOP_Y, YC + TOP_Y, x, MOUNT_Z, fn = 24);
    }
}
module p17_guard_cap_servo() guard_cap();
module p18_guard_cap_idler() mirror_y() guard_cap();
if (PART == "servo" || PART == "both") p17_guard_cap_servo();
if (PART == "idler" || PART == "both") p18_guard_cap_idler();
