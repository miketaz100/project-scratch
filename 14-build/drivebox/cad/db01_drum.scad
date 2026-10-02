// DB01 cable drum (x3) - SP1 v3 DRIVE BOX - local frame: axis z, z = 0 drum bottom.
// Installed on a 17HS08-1004S 5 mm D-shaft, bottom 1.0 mm above the deck top (frame D z = 1.0).
// Groove 1 (pad 1) z 10.5-15.5, groove 2 (pad-2 provision) z 18.5-23.5: helical, pitch 1.0 mm,
// cable centre on R 6.0 (rotation_distance = pi x 12 = 37.70 mm). M3 grub + M3 nut on the D-flat.
// Index magnet (3 x 2 N52 or K&J D21B-N52) in the flange underside at R 12, angle 180 deg.
// Print: SLA (JLC3DP 9600 or JLC Black resin), axis vertical, flange down, supports on the flange underside only.
include <lib_drivebox.scad>

module db01_drum() {
    difference() {
        union() {
            cyl_z(FL_R, 0, FL_H);
            cyl_z(HUB_R, FL_H, HUB_Z1);
            cyl_z(LAND_R, G1_Z0, G1_Z0 + G_LEN);
            cyl_z(DIV_R, DIV_Z0, DIV_Z1);
            cyl_z(LAND_R, G2_Z0, G2_Z0 + G_LEN);
            cyl_z(HUB_R, TOP_Z0, TOP_Z1);
        }
        // helical grooves: right-hand helix. OpenSCAD's positive twist is clockwise seen from +z,
        // so -TURNS*360 here equals manifold's +TURNS*360 in gen_drivebox_stl.py (handedness is not critical).
        for (z0 = [G1_Z0, G2_Z0])
            translate([0, 0, z0]) linear_extrude(height = G_LEN, twist = -TURNS * 360, slices = TURNS * 72)
                translate([PITCH_R, 0]) circle(r = GROOVE_R, $fn = 16);
        // D bore
        difference() {
            cyl_z(BORE_R, -0.01, TOP_Z1 + 0.01);
            box(FLAT_X, 3.0, -3, 3, -0.02, TOP_Z1 + 0.02);
        }
        box(NUT_X0, NUT_X1, -NUT_HY, NUT_HY, -0.01, NUT_Z1);          // M3 nut slot, opens at the bottom
        cyl_x(1.65, 0, HUB_R + 0.01, 0, GRUB_Z, fn = 24);             // M3 grub hole on the D-flat normal
        cyl_z(DMAG_R, -0.01, DMAG_DEPTH, -INDEX_R, 0, fn = 24);        // index magnet pocket
        for (ztop = [HUB_Z1, DIV_Z1]) {                               // crimp-tube anchor pockets + lead-out notch
            box(-ANCH_HX, ANCH_HX, ANCH_Y0, ANCH_Y1, ztop - ANCH_DEPTH, ztop + 0.01);
            box(-6.0, -ANCH_HX + 0.01, 6.2, 7.2, ztop - 1.0, ztop + 0.01);
        }
    }
}

db01_drum();
