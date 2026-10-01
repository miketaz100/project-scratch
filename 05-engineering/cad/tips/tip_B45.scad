// =====================================================================
//  tip_B45.scad — SP1 tip B45: nail-mimic 45 deg blade, 8 mm edge, R 0.5
//  PROJECT SCRATCH · 05-engineering/cad/tips · units: mm
//  UNIDIRECTIONAL: scratch direction is +X (the 45 deg face faces +X and down).
//  Plate 1.0 mm thick (= 2 x R 0.5), crown R 9, edge lowest point z = -12.5.
//  BLADE_MODE = "printed": one-piece PETG print (tang down, 0.12 mm layers);
//               the apex is sanded to R 0.5 and the plan corners to R 1.5.
//  BLADE_MODE = "slot":    carrier only; CA-bond a 1.0 mm nylon/PETG sheet
//               blade (plan-form: 8 x 9 mm, convex R 9 end) onto the 45 deg face.
// =====================================================================
include <tm1_tang_lib.scad>
$fn = TM1_FN;

BLADE_W    = 8.0;        // edge width along Y
BLADE_R    = 0.5;        // edge radius = half plate thickness
ATTACK     = 45;         // plate angle to the scalp plane, deg
DROP       = 7.0;        // band bottom to edge lowest point
BLADE_MODE = "printed";  // "printed" | "slot"
CROSS_HOLE = false;

module tip_B45(w = BLADE_W, r = BLADE_R, attack = ATTACK, drop = DROP,
               mode = BLADE_MODE, cross_hole = CROSS_HOLE) {
    tm1_tip_base(cross_hole);
    tm1_nail_blade(w = w, r = r, attack = attack, drop = drop, mode = mode);
}

tip_B45();
