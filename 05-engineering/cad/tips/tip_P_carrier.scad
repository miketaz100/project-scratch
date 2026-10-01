// =====================================================================
//  tip_P_carrier.scad — SP1 tip P: carrier for a trimmed PRESS-ON NAIL
//  PROJECT SCRATCH · 05-engineering/cad/tips · units: mm
//  Zero-fabrication reference tip.  A press-on ABS nail (KISS 100 Full-Cover,
//  size 1-2, ~8-9 mm wide), trimmed to 10 mm long, is CA-bonded
//  with its concave underside on a CONVEX cylindrical bed (R 8.5, axis at 45 deg)
//  so its convex dorsal face faces +X and down = the leading face.
//  Bed length ≈ 7.5 mm; the nail's free edge overhangs ≈ 2.5-3 mm; fill the void
//  under the overhang with gel CA / 5-min epoxy (no hollow under the nail).
//  EDGE RADIUS (red line 11, DESIGN-FREEZE 1.8): a single ~0.6 mm nail can only
//  be filed to R <= 0.3 (half its thickness) = A45 class, GATED.  For first human
//  sessions nest two nails CA-bonded (~1.2 mm) or use one >= 0.8 mm thick, and
//  file the free edge to R 0.4-0.5; tape test (L9) before use.
//  Nail edge lowest point ≈ z = -14.3 to -14.7 (-15.0 with two nested nails).
//  Free overhang beyond the gel-CA fill: <= 3 mm (ABS proof load, redteam-2).
//  Loaded sense +X.  Print: PETG, tang down, 0.10 mm layers.
// =====================================================================
include <tm1_tang_lib.scad>
$fn = TM1_FN;

BED_R       = 8.5;      // convex bed radius (nail underside R ≈ 8.5-9)
BED_ATTACK  = 45;       // bed axis angle: rises toward +X at this angle
BED_AXIS_X  = -4.52;    // axis passes through (BED_AXIS_X, 0, BED_AXIS_Z); the bed surface meets
BED_AXIS_Z  = -6.0;     // the band's bottom front edge at |y| = 3.4 (band corner at y = 0 is 7.8 mm
                        // from the axis); at y = 0 the bed spans z = -6.9 .. -10.6
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
