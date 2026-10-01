// =====================================================================
//  tip_W.scad — SP1 tip W: symmetric WEDGE (DEFAULT, bidirectional raking)
//  PROJECT SCRATCH · 05-engineering/cad/tips · units: mm
//  8 mm edge along Y, two 45 deg faces (90 deg included), edge R 0.4 mm,
//  transverse crown R 9 (edge ends rise 0.9 mm so the centre loads first).
//  Lowest point of the edge: z = -12.5 (7.0 mm below the shoulder band).
//  Print: PETG, tang down / edge up, 0.12 mm layers, 3 perimeters, 100 % infill.
//  Finish: sand the apex 400 -> 1000 -> 2000 wet to R 0.4; hand-round the two
//  edge-end corners to R 1.5; optional 1 s flame pass (PETG only).
// =====================================================================
include <tm1_tang_lib.scad>
$fn = TM1_FN;

W_EDGE_W   = 8.0;    // edge length along Y
W_EDGE_R   = 0.4;    // modelled apex radius (sand to this after printing)
W_HEIGHT   = 7.0;    // shoulder band bottom to apex. 7.0 = TM1_SH_X/2 gives exactly 45 deg faces
W_CROWN_R  = 9.0;    // transverse crown radius (index-nail value)
CROSS_HOLE = false;  // true adds the 3.2 mm TM1-B cross-bolt hole in the tang

module tip_W(w = W_EDGE_W, r = W_EDGE_R, h = W_HEIGHT, crown_r = W_CROWN_R, cross_hole = CROSS_HOLE) {
    z_apex = TM1_SH_BOT - h;
    tm1_tip_base(cross_hole);
    intersection() {
        hull() {
            tm1_band_slab();
            tm1_ycyl(r, w, 0, z_apex + r);      // apex edge cylinder along Y
        }
        tm1_crown(crown_r, z_apex);
    }
}

tip_W();
