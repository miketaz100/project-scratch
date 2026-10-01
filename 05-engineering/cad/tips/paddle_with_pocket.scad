// =====================================================================
//  paddle_with_pocket.scad — drafted 25 mm PADDLE ending in a TM1 pocket,
//  with a clamp for a 0.3 x 12.7 mm feeler-stock leaf (no holes in the leaf)
//  PROJECT SCRATCH · 05-engineering/cad/tips · units: mm
//  Used by: the SP1 hand (one per nail, MECH LEAD — all parameters below are
//  yours to override) and the Stage-0 HAND WAND (hand_wand_handle.scad).
// ---------------------------------------------------------------------
//  FRAME = TM1 frame: pocket mouth centre at the origin, +Z toward the root,
//  -Z toward the scalp.  The LEAF runs along Y through the root block.
//  Geometry, bottom to top:
//    z = 0 .. PADDLE_LEN      drafted body: nose 14 x 9 (R1) growing at DRAFT_X / DRAFT_Y
//                             per side (10 deg / 10 deg) to 22.8 x 17.8 at z = 25
//    z = 25 .. 25+RISER       RISER: straight (constant 22.8 x 17.8) extension; 0 for the
//                             outer paddles and the wand, 9 for the SP1 centre paddle
//    (z0 = 25 + RISER below)
//    z = z0 .. z0+3           transition to the root block (above the knuckle plate); with
//                             DRAFT_Y = 10 it NARROWS in Y from 17.8 to the 14 mm root
//    z = z0+3 .. z0+10        root block 28 x 14: clamp WINDOW 24.2 x 8.4 x 3.5 deep from
//                             the top; the leaf lies on the window floor (z = 31.5 + RISER),
//                             passes out through 12.9 x 1.0 slots in the Y walls, and is
//                             pressed down by the CLAMP BAR (24 x 8 x 3.2, with a
//                             12.9 x 0.25 locating groove) via 2x M3x8 screws at x = +/-9.5
//                             (rev 2026-10-01: bar 23 / screws +/-10 broke the 3.4 holes out
//                             of the bar ends by 0.2 mm)
//                             (2.6 mm holes, thread-forming in PETG; or 4.0 mm for inserts)
//  Pocket: tm1_pocket() — 10.3 x 4.3 x 12.5, mouth chamfer 0.6, N52 6x2 magnet recess
//  (magnet dropped in at a PRINT PAUSE at model z = 11.9, i.e. print height 23.1 mm
//  for RISER = 0 and 32.1 mm for RISER = 9; see README).
//  rev 2026-10-01 (post DESIGN-FREEZE-ADDENDUM-1, D2/D3): DRAFT_Y 5 -> 10 (24 mm pitch),
//  new RISER parameter.  SP1 hand: 2x RISER = 0 (L, R), 1x RISER = 9 (C, its leaf crosses
//  one level above L's).  Leaf floor to W/B45 edge: 44.0 mm (RISER 0), 53.0 mm (RISER 9).
//  Print: PETG, NOSE UP (root on the bed), 0.2 mm layers, 4 perimeters (wand); SP1 hand
//  paddles 2 perimeters / 10 % gyroid with 4 perimeters around the screw holes
//  (mechanical.md 8.9, float mass budget).  The window
//  floor is an 8.4 mm bridge — fine for PETG; or paint supports in the window only.
//  TPU seam SLEEVE (PART = "sleeve"): TPU 90A, 0.6-1.0 mm wall, stretched over the nose
//  (0.4 mm interference) covering z = +3 .. -5.5 so the tip/pocket seam is enclosed.
// =====================================================================
include <tm1_tang_lib.scad>
$fn = TM1_FN;

PART = "paddle";        // "paddle" | "bar" | "sleeve" | "assembly"

// ---- nose and draft (nose = TM1 shoulder band size) ----
NOSE_X     = TM1_SH_X;  // 14
NOSE_Y     = TM1_SH_Y;  // 9
NOSE_R     = TM1_SH_R;  // 1
DRAFT_X    = 10;        // deg per side, stroke-facing faces (H-4.3: >= 10)
DRAFT_Y    = 10;        // deg per side, across-stroke faces (H-4.3: >= 10).  Was 5 at the
                        // freeze's 20 mm pitch; 10 since ADDENDUM-1 D2/D3 (24 mm pitch:
                        // 24 - 17.8 = 6.2 mm between paddles at z = 25, free state)
PADDLE_LEN = 25;        // protrusion below the knuckle plate (H-4.5 design basis)
RISER      = 0;         // straight extension of the z = 25 section before the transition
                        // (ADDENDUM-1 D3): 0 = outer paddles / wand, 9 = SP1 centre paddle
POCKET_TILT = 0;        // deg about Y: attack-angle holder variants (0 for SP1 — angle lives in the tip)
BOLT_VARIANT = false;   // TM1-B: M3 cross-bolt through nose + tang (heavy tips); widens nose Y to 12

// ---- root block / leaf clamp ----
ROOT_X     = 28;
ROOT_Y     = 14;
ROOT_TRANS = 3;         // drafted transition height
ROOT_H     = 7;         // straight block height
ROOT_R     = 2;
LEAF_W     = 12.7;      // feeler stock width (1/2")
LEAF_T     = 0.30;      // feeler stock thickness (0.012")
WINDOW_X   = 24.2;
WINDOW_Y   = 8.4;
WINDOW_D   = 3.5;       // depth from the root top
WALL_SLOT_W = LEAF_W + 0.2;
WALL_SLOT_H = 1.0;      // tall slot in the Y walls: the bar sets the leaf height, not the slot
LEAF_THROUGH = true;    // slots in both Y walls (false: only -Y, leaf ends blind in the +Y wall)
SCREW_X    = 9.5;       // screws at (+/-SCREW_X, 0): 0.8 mm bar wall outboard, 1.85 mm clear of the leaf
SCREW_HOLE_D = 2.6;     // 2.6 = M3 thread-forming in PETG; 4.0 = M3 heat-set insert
SCREW_DEPTH  = 5;
BAR_X      = 24;
BAR_Y      = 8;
BAR_H      = 3.2;
BAR_GROOVE_D = 0.25;    // < LEAF_T so the bar presses the leaf, not the floor
BAR_HOLE_D = 3.4;

// ---- TPU seam sleeve ----
SLEEVE_WALL  = 0.8;
SLEEVE_INTERF = 0.2;    // per side
SLEEVE_TOP   = 3.0;     // z of the sleeve top on the nose
SLEEVE_BOT   = TM1_SH_BOT;  // -5.5: covers the whole shoulder band of the tip

// derived
nose_y   = BOLT_VARIANT ? 12 : NOSE_Y;
top_x    = NOSE_X + 2 * PADDLE_LEN * tan(DRAFT_X);
top_y    = nose_y + 2 * PADDLE_LEN * tan(DRAFT_Y);
z_drafted = PADDLE_LEN;               // top of the drafted body
z_root0  = PADDLE_LEN + RISER;        // top of the riser = start of the transition
z_root1  = z_root0 + ROOT_TRANS;
z_top    = z_root1 + ROOT_H;
z_floor  = z_top - WINDOW_D;          // leaf rests here

module slab(x, y, r, z, h = 0.02) {
    translate([0, 0, z - h / 2]) linear_extrude(height = h) tm1_rrect(x, y, r);
}

module paddle_body() {
    hull() { slab(NOSE_X, nose_y, NOSE_R, 0.01); slab(top_x, top_y, NOSE_R, z_drafted); }
    if (RISER > 0)
        translate([0, 0, z_drafted - 0.01]) linear_extrude(height = RISER + 0.02) tm1_rrect(top_x, top_y, NOSE_R);
    hull() { slab(top_x, top_y, NOSE_R, z_root0); slab(ROOT_X, ROOT_Y, ROOT_R, z_root1); }
    translate([0, 0, z_root1 - 0.01]) linear_extrude(height = ROOT_H + 0.01) tm1_rrect(ROOT_X, ROOT_Y, ROOT_R);
}

module paddle_cuts() {
    rotate([0, POCKET_TILT, 0]) tm1_pocket(cross_bolt = BOLT_VARIANT);
    if (BOLT_VARIANT) {   // countersunk head on +Y, hex nut recess on -Y, both under the sleeve
        yf = nose_y / 2 + TM1_XB_Z * tan(DRAFT_Y);
        translate([0, yf + 0.01, TM1_XB_Z]) rotate([90, 0, 0])
            cylinder(d1 = 6.4, d2 = 3.4, h = 1.6, $fn = TM1_FN);
        translate([0, -yf - 0.01, TM1_XB_Z]) rotate([-90, 0, 0])
            cylinder(d = 5.6 / cos(30), h = 2.5, $fn = 6);
    }
    // clamp window from the top
    translate([0, 0, z_floor + 50]) cube([WINDOW_X, WINDOW_Y, 100], center = true);
    // leaf slots through the Y walls
    sy = LEAF_THROUGH ? 0 : -ROOT_Y / 4;
    sl = LEAF_THROUGH ? ROOT_Y + 2 : ROOT_Y / 2 + 1;
    translate([0, sy, z_floor - 0.01 + WALL_SLOT_H / 2]) cube([WALL_SLOT_W, sl, WALL_SLOT_H + 0.02], center = true);
    // screw holes beside the leaf
    for (sx = [-SCREW_X, SCREW_X])
        translate([sx, 0, z_floor - SCREW_DEPTH]) cylinder(d = SCREW_HOLE_D, h = SCREW_DEPTH + 0.01, $fn = 24);
}

module paddle() { difference() { paddle_body(); paddle_cuts(); } }

// clamp bar, printed groove-side up (as modelled)
module clamp_bar() {
    difference() {
        translate([0, 0, BAR_H / 2]) cube([BAR_X, BAR_Y, BAR_H], center = true);
        translate([0, 0, BAR_GROOVE_D / 2 - 0.01]) cube([LEAF_W + 0.2, BAR_Y + 2, BAR_GROOVE_D + 0.02], center = true);
        for (sx = [-SCREW_X, SCREW_X]) translate([sx, 0, -1]) cylinder(d = BAR_HOLE_D, h = BAR_H + 2, $fn = 24);
    }
}

// TPU seam sleeve: inner = band (straight) then nose (drafted), minus interference;
// outer = inner + wall at the bottom, feathering toward the paddle surface at the top.
module seam_sleeve() {
    ix0 = NOSE_X - 2 * SLEEVE_INTERF;  iy0 = nose_y - 2 * SLEEVE_INTERF;
    ix1 = NOSE_X + 2 * SLEEVE_TOP * tan(DRAFT_X) - 2 * SLEEVE_INTERF;
    iy1 = nose_y + 2 * SLEEVE_TOP * tan(DRAFT_Y) - 2 * SLEEVE_INTERF;
    difference() {
        hull() {
            slab(ix0 + 2 * SLEEVE_WALL, iy0 + 2 * SLEEVE_WALL, NOSE_R + SLEEVE_WALL, SLEEVE_BOT + 0.01);
            slab(ix1 + 2 * SLEEVE_WALL * 0.75, iy1 + 2 * SLEEVE_WALL * 0.75, NOSE_R + SLEEVE_WALL, SLEEVE_TOP - 0.01);
        }
        translate([0, 0, SLEEVE_BOT - 1]) linear_extrude(height = 1 - SLEEVE_BOT + 0.01) tm1_rrect(ix0, iy0, NOSE_R);
        hull() { slab(ix0, iy0, NOSE_R, 0); slab(ix1, iy1, NOSE_R, SLEEVE_TOP + 1); }
    }
}

if (PART == "paddle") paddle();
if (PART == "bar") clamp_bar();
if (PART == "sleeve") seam_sleeve();
if (PART == "assembly") {
    color("orange") paddle();
    color("gray") translate([0, 0, z_floor + LEAF_T - BAR_GROOVE_D]) clamp_bar();
    color("silver") translate([0, 0, z_floor + LEAF_T / 2]) cube([LEAF_W, 70, LEAF_T], center = true);
    color("black", 0.4) seam_sleeve();
}
