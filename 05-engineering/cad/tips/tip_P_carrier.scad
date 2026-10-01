// =====================================================================
//  tip_P_carrier.scad — SP1 tip P: carrier for a trimmed PRESS-ON NAIL
//  PROJECT SCRATCH · 05-engineering/cad/tips · units: mm
//  Zero-fabrication reference tip.  A press-on ABS nail (KISS 100 Full-Cover,
//  size 1-2, ~8-9 mm wide, ~0.6 mm thick), trimmed to 10 mm long, is CA-bonded
//  with its concave underside on a CONVEX cylindrical bed (R 8.5, axis at 45 deg)
//  so its convex dorsal face faces +X and down = the leading face.
//  Bed length ≈ 7.5 mm; the nail's free edge overhangs ≈ 2.5-3 mm; fill the void
//  under the overhang with gel CA / 5-min epoxy (no hollow under the nail).
//  Nail edge lowest point ≈ z = -14.7.  Scratch direction +X.
//  Print: PETG, tang down, 0.12 mm layers.
// =====================================================================
include <tm1_tang_lib.scad>
$fn = TM1_FN;

BED_R       = 8.5;      // convex bed radius (nail underside R ≈ 8.5-9)
BED_ATTACK  = 45;       // bed axis angle: rises toward +X at this angle
BED_AXIS_X  = -4.52;    // axis passes through (BED_AXIS_X, 0, BED_AXIS_Z); chosen so the bed
BED_AXIS_Z  = -6.0;     // surface passes exactly through the band's (+7, -5.5) bottom corner
BOSS_FRONT  = [5.0, -9.0];   // hull point giving material out to the bed surface
BOSS_BOTTOM = [-0.5, -10.5]; // hull point: pulp lump behind/below the bed (r = 1 cylinders)
CROSS_HOLE  = false;

module tip_P_carrier(cross_hole = CROSS_HOLE) {
    tm1_tip_base(cross_hole);
    difference() {
        hull() {
            tm1_band_slab();
            tm1_ycyl(1.0, TM1_SH_Y, BOSS_FRONT[0], BOSS_FRONT[1]);
            tm1_ycyl(1.0, TM1_SH_Y, BOSS_BOTTOM[0], BOSS_BOTTOM[1]);
        }
        // carve the convex bed: remove everything farther than BED_R from the
        // inclined axis, but only below the shoulder band
        intersection() {
            translate([BED_AXIS_X, 0, BED_AXIS_Z]) rotate([0, 90 - BED_ATTACK, 0])
                difference() {
                    cylinder(r = 40, h = 60, center = true, $fn = TM1_FN);
                    cylinder(r = BED_R, h = 62, center = true, $fn = 180);
                }
            translate([0, 0, TM1_SH_BOT - 50]) cube([100, 100, 100], center = true);
        }
    }
}

tip_P_carrier();
