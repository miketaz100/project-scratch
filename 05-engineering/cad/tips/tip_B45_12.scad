// =====================================================================
//  tip_B45_12.scad — SP1 tip B45-12: as B45 but 12 mm wide edge (width variable)
//  PROJECT SCRATCH · 05-engineering/cad/tips · units: mm
//  The 12 mm plate is wider than the 9 mm shoulder band; the pulp lump stays
//  9 mm wide, so the outer 1.5 mm of each plate end is a free 1 mm plate.
//  Round those ends to R 1.5 in plan after printing.  Crown R 9 raises the
//  edge ends 2.3 mm (0.94 mm on the 8 mm tips), so the loaded edge grows with
//  force.  The plate ends are clipped at the band plane (tm1_nail_blade) so the
//  TPU seam sleeve seats.  Loaded sense +X. Print as tip_B45 (on its side).
// =====================================================================
include <tm1_tang_lib.scad>
$fn = TM1_FN;

BLADE_W    = 12.0;
BLADE_R    = 0.5;
ATTACK     = 45;
DROP       = 7.0;
BLADE_MODE = "printed";   // "printed" | "slot"
CROSS_HOLE = false;

module tip_B45_12(w = BLADE_W, r = BLADE_R, attack = ATTACK, drop = DROP,
                  mode = BLADE_MODE, cross_hole = CROSS_HOLE) {
    tm1_tip_base(cross_hole);
    tm1_nail_blade(w = w, r = r, attack = attack, drop = drop, mode = mode);
}

tip_B45_12();
