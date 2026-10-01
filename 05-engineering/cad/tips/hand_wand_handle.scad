// =====================================================================
//  hand_wand_handle.scad — Stage-0 HAND WAND handle
//  PROJECT SCRATCH · 05-engineering/cad/tips · units: mm
//  A 180 mm printed handle (150 mm grip + 30 mm clamp block) that clamps one end
//  of a 0.3 x 12.7 mm feeler-stock leaf (no holes in the leaf: window + clamp bar
//  + 4x M3x8, bar 24 x 24).  The leaf runs out along +Y; its free end carries
//  paddle_with_pocket.scad (same clamp design) with a TM1 pocket, 25 mm drafted
//  paddle and any SP1 tip.  Leaf free length LEAF_FREE (handle face to paddle -Y
//  face) sets the normal stiffness AT THE TIP.  The leaf also flexes 3 mm inside each
//  wall slot (bar edge to wall) and the tip sits 4 mm past the paddle bar edge, so
//  k = EI / (a^3/3 + a^2 b + a b^2), a = LEAF_FREE + 6, b = 4, EI = 5715 N mm^2
//  (E = 200 GPa, I = 12.7 x 0.3^3 / 12):
//    30 mm 0.27 N/mm · 35 mm 0.19 · 38 mm 0.155 (default) · 40 mm 0.14 · 45 mm 0.10
//  (rev 2026-10-01: the old table used 3EI/L^3 on LEAF_FREE and overstated k 1.75x;
//  48 mm actually gives 0.09 N/mm, below the DESIGN-FREEZE 0.1-0.25 band).
//  Calibrate on the kitchen scale (tips.md 7.3) and trim the leaf to suit.
//  Print flat as modelled (window up), PETG or PLA (handle never touches hair),
//  0.2 mm layers, 15 % infill, 3 perimeters.  No bridges.
//  PART = "handle" | "bar" | "assembly"
// =====================================================================
include <tm1_tang_lib.scad>
$fn = TM1_FN;

PART = "handle";

HANDLE_LEN = 150;   // grip length along -Y
HANDLE_X   = 22;    // grip width
HANDLE_H   = 16;    // grip height
HANDLE_R   = 8;     // grip corner radius (vertical corners)
BLOCK_X    = 28;    // clamp block
BLOCK_Y    = 30;
BLOCK_H    = 16;
BLOCK_R    = 2;
LEAF_W     = 12.7;
LEAF_T     = 0.30;
WINDOW_X   = 24.2;
WINDOW_Y   = 24.4;
WINDOW_D   = 3.5;   // leaf floor at BLOCK_H - WINDOW_D = 12.5
WALL_SLOT_W = LEAF_W + 0.2;
WALL_SLOT_H = 1.0;
SCREWS     = [[-9.5, -7], [9.5, -7], [-9.5, 7], [9.5, 7]];   // rev: was +/-10 (holes broke out of the bar)
SCREW_HOLE_D = 2.6; // M3 thread-forming in PETG/PLA (4.0 for inserts)
SCREW_DEPTH  = 6;
BAR_X      = 24;
BAR_Y      = 24;
BAR_H      = 3.2;
BAR_GROOVE_D = 0.25;
BAR_HOLE_D = 3.4;
LEAF_FREE  = 38;    // documentation only: leaf free length to the paddle root (-Y face); 0.155 N/mm

z_floor = BLOCK_H - WINDOW_D;

module rr_prism(x, y, h, r) { linear_extrude(height = h) tm1_rrect(x, y, r); }

module handle_body() {
    // grip: from y = -(BLOCK_Y/2 + HANDLE_LEN) to y = -BLOCK_Y/2 (+1 overlap)
    translate([0, -BLOCK_Y / 2 - HANDLE_LEN / 2 + 0.5, 0]) rr_prism(HANDLE_X, HANDLE_LEN + 1, HANDLE_H, HANDLE_R);
    rr_prism(BLOCK_X, BLOCK_Y, BLOCK_H, BLOCK_R);
}

module handle_cuts() {
    translate([0, 0, z_floor + 50]) cube([WINDOW_X, WINDOW_Y, 100], center = true);
    // leaf exit slot through the +Y wall only (leaf ends blind in the -Y wall)
    translate([0, BLOCK_Y / 4, z_floor - 0.01 + WALL_SLOT_H / 2]) cube([WALL_SLOT_W, BLOCK_Y / 2 + 1, WALL_SLOT_H + 0.02], center = true);
    for (s = SCREWS) translate([s[0], s[1], z_floor - SCREW_DEPTH]) cylinder(d = SCREW_HOLE_D, h = SCREW_DEPTH + 0.01, $fn = 24);
}

module handle() { difference() { handle_body(); handle_cuts(); } }

module clamp_bar() {
    difference() {
        translate([0, 0, BAR_H / 2]) cube([BAR_X, BAR_Y, BAR_H], center = true);
        translate([0, 0, BAR_GROOVE_D / 2 - 0.01]) cube([LEAF_W + 0.2, BAR_Y + 2, BAR_GROOVE_D + 0.02], center = true);
        for (s = SCREWS) translate([s[0], s[1], -1]) cylinder(d = BAR_HOLE_D, h = BAR_H + 2, $fn = 24);
    }
}

if (PART == "handle") handle();
if (PART == "bar") clamp_bar();
if (PART == "assembly") {
    color("orange") handle();
    color("gray") translate([0, 0, z_floor + LEAF_T - BAR_GROOVE_D]) clamp_bar();
    // leaf: 27 mm inside the block + LEAF_FREE + 14 mm in the paddle root
    color("silver") translate([0, -BLOCK_Y / 2 + 2.8 + (27 + LEAF_FREE + 14) / 2, z_floor + LEAF_T / 2])
        cube([LEAF_W, 27 + LEAF_FREE + 14, LEAF_T], center = true);
}
