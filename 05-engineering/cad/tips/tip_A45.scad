// =====================================================================
//  tip_A45.scad — SP1 tip A45: nail-mimic 45 deg, R 0.3 mm (EXPERIMENTAL, GATED)
//  PROJECT SCRATCH · 05-engineering/cad/tips · units: mm
//  R 0.3 is below safety red line 11 (tips >= 0.4 mm): HUMAN USE ONLY after the
//  forearm screen AND the UL 1439-style tape test (tips.md §2.4, §2.7).
//  Default route is a CARRIER ("slot" mode): CA-bond a 0.8 mm nylon sheet blade
//  (or a Dunlop nylon .88 pick) cut to 8 x 9 mm with a convex R 9 end, then file
//  the edge to R 0.3 (two 0.3 mm chamfers blended; 0.2 mm flats remain).
//  "printed" mode makes a 0.8 mm PETG plate (2 perimeters) — fragile; carrier preferred.
//  Slot mode (rev 2026-10-01): the carrier now has a true 45 deg bonding face in the
//  plane of the sheet's upper face; butt the sheet's top end against the band.
//  Loaded sense +X.  Print the carrier tang down, 0.10 mm layers.
// =====================================================================
include <tm1_tang_lib.scad>
$fn = TM1_FN;

BLADE_W    = 8.0;
BLADE_R    = 0.4;        // half of the 0.8 mm sheet; the EDGE is hand-filed to R 0.3
ATTACK     = 45;
DROP       = 7.0;
BLADE_MODE = "slot";     // "slot" (carrier for sheet blade) | "printed"
CROSS_HOLE = false;

module tip_A45(w = BLADE_W, r = BLADE_R, attack = ATTACK, drop = DROP,
               mode = BLADE_MODE, cross_hole = CROSS_HOLE) {
    tm1_tip_base(cross_hole);
    tm1_nail_blade(w = w, r = r, attack = attack, drop = drop, mode = mode);
}

tip_A45();
