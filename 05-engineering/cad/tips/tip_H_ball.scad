// =====================================================================
//  tip_H_ball.scad — SP1 tip H: 3 mm BALL — massager CONTROL tip
//  PROJECT SCRATCH · 05-engineering/cad/tips · units: mm
//  Drafted cone stem from the shoulder band to a 4 mm dia end 5.5 mm below it,
//  with a spherical cup for a 3.0 mm steel bearing ball (CA/epoxy bonded).
//  Ball lowest point z = -12.8 (comparable to the W apex at -12.5).
//  PRINTED_BALL = true prints the ball solid (sand smooth) if you have no balls.
//  Print: PETG, tang down, 0.12 mm layers.
// =====================================================================
include <tm1_tang_lib.scad>
$fn = TM1_FN;

BALL_D       = 3.0;
STEM_R       = 2.0;    // radius of the cone end
STEM_LEN     = 5.5;    // band bottom to cone end
CUP_OFFSET   = 0.3;    // ball centre below the cone end (mouth 3.04 mm > ball: drop-in, glue holds)
PRINTED_BALL = false;
CROSS_HOLE   = false;

module tip_H(ball_d = BALL_D, stem_r = STEM_R, stem_len = STEM_LEN,
             printed_ball = PRINTED_BALL, cross_hole = CROSS_HOLE) {
    z_end  = TM1_SH_BOT - stem_len;     // -11.0
    z_ball = z_end - CUP_OFFSET;        // -11.3
    tm1_tip_base(cross_hole);
    difference() {
        hull() {
            tm1_band_slab();
            translate([0, 0, z_end]) cylinder(r = stem_r, h = 0.02, $fn = TM1_FN);
        }
        if (!printed_ball)
            translate([0, 0, z_ball]) sphere(r = ball_d / 2 + 0.05, $fn = TM1_FN);
    }
    if (printed_ball)
        translate([0, 0, z_ball]) sphere(r = ball_d / 2, $fn = TM1_FN);
}

tip_H();
