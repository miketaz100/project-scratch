// =====================================================================
//  tm1_tang_lib.scad — SP1-TM1 tip-mount standard, shared library
//  PROJECT SCRATCH · 05-engineering/cad/tips · 2026-10-01 · units: mm
// ---------------------------------------------------------------------
//  FRAME (shared by every tip and every holder/paddle):
//    +Z = into the holder pocket (toward the paddle root / palm)
//    -Z = toward the scalp
//     X = stroke direction,  Y = across the stroke (nail pitch direction)
//    Origin = centre of the POCKET MOUTH plane.
//    Tang occupies z in [0, TM1_TANG_L]; tip working parts live below
//    z = TM1_SH_BOT.  Orientation key (2 x 45 deg chamfer) is on the
//    (+X,+Y) corner of the tang and the pocket.
//
//  USAGE:   include <tm1_tang_lib.scad>   then call
//    tm1_tip_base()          tang + cone + shoulder band (every tip)
//    tm1_pocket()            NEGATIVE: difference() it from a holder
//    tm1_band_slab()         thin slab at the shoulder bottom — hull()
//                            working parts to it
//    tm1_nail_blade(...)     B45-family nail-mimic blade body
//  Nothing is rendered when this file is included (TM1_DEMO = false).
// ---------------------------------------------------------------------
//  PRINT ORIENTATION OF TIPS (rev 2026-10-01, tip lead):
//    W, B45, B45-12 (printed edge): ON THE SIDE, model Y vertical, so the edge
//      line runs up the print and its XZ profile is traced by the perimeters
//      (no layer staircase across the edge; plate bends in-plane, not across
//      layers).  Supports under the tang/shoulder only.  0.10 mm layers.
//    Carriers (A45 slot, E, P) and H: tang DOWN on the bed, working end UP
//      (the cone is a 45 / 39 deg overhang: printable without supports).
//  STEEL KEEPER: the spec's 6 x 1 disc (or an M3 washer, 7 mm OD) is wider than
//  the 4.0 mm tang; use a 6 x 1 disc with two flats filed to 3.9 mm, or a
//  6.0 x 3.9 x 1.0 mm slug cut from 1 mm mild-steel sheet (TM1_SLUG_* below).
// =====================================================================

// ---------------- TANG (on every tip) ----------------
TM1_TANG_X   = 10.0;   // along X (stroke)
TM1_TANG_Y   =  4.0;   // along Y (across)
TM1_TANG_L   = 12.0;   // length along Z
TM1_KEY      =  2.0;   // chamfer leg on the (+X,+Y) corner (orientation key)
TM1_END_CH   =  0.5;   // chamfer at the tang end: insertion lead + elephant-foot relief
// steel keeper slug, glued in a through-notch (Y) at the tang end
TM1_SLUG_X     = 6.0;  // slug 6.0 x 3.9 x 1.0 mm, cut from 1 mm mild-steel sheet
TM1_SLUG_T     = 1.0;
TM1_SLUG_CLEAR = 0.15; // per side

// ---------------- SHOULDER (cone from tang to the 14 x 9 band) ----------------
TM1_SH_X   = 14.0;     // band size X (= paddle nose X)
TM1_SH_Y   =  9.0;     // band size Y (= paddle nose Y)
TM1_SH_R   =  1.0;     // vertical corner radius of the band
TM1_SH_TOP = -2.5;     // z where the cone reaches full band size
TM1_SH_BOT = -5.5;     // z of the band bottom = top of the working part

// ---------------- POCKET (on every holder) ----------------
TM1_POCKET_CLEAR = 0.15;  // per side; 10.3 x 4.3 nominal pocket
TM1_POCKET_DEPTH = 12.5;  // mouth to floor
TM1_MOUTH_CH     = 0.6;   // lead-in chamfer at the mouth
TM1_MAG_D        = 6.0;   // N52 6 x 2 disc, axially magnetised
TM1_MAG_H        = 2.0;
TM1_MAG_CLEAR    = 0.1;
TM1_MAG_TOP      = 11.9;  // recess starts here; magnet face ends up at z = 12.0 = tang end
                          // (magnet is dropped in at a PRINT PAUSE — see README)

// ---------------- optional cross-bolt (TM1-B heavy-tip variant) ----------------
TM1_XB_Z        = 6.0;    // height of the M3 cross-hole above the mouth
TM1_XB_D_TANG   = 3.2;    // hole in the tang
TM1_XB_D_HOLDER = 3.4;    // hole in the holder walls

TM1_FN   = 48;
TM1_DEMO = false;         // set true (in THIS file only) to preview tang + pocket

// ============================ 2D helpers ============================
// rounded rectangle, centred
module tm1_rrect(x, y, r) {
    offset(r = r, $fn = TM1_FN) offset(delta = -r) square([x, y], center = true);
}

// tang cross-section grown by c on every side (c < 0 shrinks it).
// Chamfer leg grows by c*(2 - sqrt(2)) so the chamfer face is offset by c exactly.
module tm1_tang_profile(c = 0) {
    hx = TM1_TANG_X / 2 + c;
    hy = TM1_TANG_Y / 2 + c;
    k  = TM1_KEY + c * (2 - sqrt(2));
    polygon([[-hx, -hy], [hx, -hy], [hx, hy - k], [hx - k, hy], [-hx, hy]]);
}

// ============================ 3D helpers ============================
// thin slab of the band outline at height z (hull() working parts to it)
module tm1_band_slab(z = TM1_SH_BOT, h = 0.02) {
    translate([0, 0, z - h / 2])
        linear_extrude(height = h) tm1_rrect(TM1_SH_X, TM1_SH_Y, TM1_SH_R);
}

// cylinder along Y, centred at (x, 0, z)
module tm1_ycyl(r, len, x, z) {
    translate([x, 0, z]) rotate([90, 0, 0])
        cylinder(r = r, h = len, center = true, $fn = TM1_FN);
}

// "crown" clipping cylinder along X: intersect a blade with it so the edge
// line becomes an arc of radius cr whose lowest point is at z_apex (nail-like
// transverse curvature; loads the centre of the edge first).
module tm1_crown(cr = 9, z_apex = -12.5) {
    translate([0, 0, z_apex + cr]) rotate([0, 90, 0])
        cylinder(r = cr, h = 80, center = true, $fn = 180);
}

// ============================ TANG ============================
module tm1_tang(cross_hole = false) {
    nh = TM1_SLUG_T + TM1_SLUG_CLEAR;          // notch height (Z)
    difference() {
        hull() {
            linear_extrude(height = TM1_TANG_L - TM1_END_CH) tm1_tang_profile(0);
            translate([0, 0, TM1_TANG_L - 0.01])
                linear_extrude(height = 0.01) tm1_tang_profile(-TM1_END_CH);
        }
        // keeper notch: through in Y, open at the tang end
        translate([0, 0, TM1_TANG_L - nh + (nh + 1) / 2])
            cube([TM1_SLUG_X + 2 * TM1_SLUG_CLEAR, TM1_TANG_Y + 2, nh + 1], center = true);
        if (cross_hole)
            translate([0, 0, TM1_XB_Z]) rotate([90, 0, 0])
                cylinder(d = TM1_XB_D_TANG, h = TM1_TANG_Y + 2, center = true, $fn = TM1_FN);
    }
}

// ============================ SHOULDER ============================
// cone from the tang section (z = 0) to the band (z = TM1_SH_TOP), then the
// straight band down to TM1_SH_BOT.  The TPU seam sleeve on the paddle nose
// covers z = +3 .. TM1_SH_BOT, so the V-gap between cone and pocket mouth is
// enclosed (no hair access).
module tm1_shoulder() {
    hull() {
        translate([0, 0, -0.01]) linear_extrude(height = 0.02) tm1_tang_profile(0);
        tm1_band_slab(TM1_SH_TOP, 0.02);
    }
    translate([0, 0, TM1_SH_BOT])
        linear_extrude(height = TM1_SH_TOP - TM1_SH_BOT + 0.01)
            tm1_rrect(TM1_SH_X, TM1_SH_Y, TM1_SH_R);
}

module tm1_tip_base(cross_hole = false) {
    tm1_tang(cross_hole);
    tm1_shoulder();
}

// ============================ POCKET (negative) ============================
// difference() this from a holder whose pocket mouth is at the origin.
module tm1_pocket(clear = TM1_POCKET_CLEAR, depth = TM1_POCKET_DEPTH,
                  mouth_ch = TM1_MOUTH_CH, magnet = true, cross_bolt = false) {
    translate([0, 0, -0.01]) linear_extrude(height = depth + 0.01) tm1_tang_profile(clear);
    hull() {   // mouth lead-in
        translate([0, 0, -0.01]) linear_extrude(height = 0.02) tm1_tang_profile(clear + mouth_ch);
        translate([0, 0, mouth_ch]) linear_extrude(height = 0.02) tm1_tang_profile(clear);
    }
    if (magnet)
        translate([0, 0, TM1_MAG_TOP])
            cylinder(d = TM1_MAG_D + 2 * TM1_MAG_CLEAR, h = TM1_MAG_H + TM1_MAG_CLEAR, $fn = TM1_FN);
    if (cross_bolt)
        translate([0, 0, TM1_XB_Z]) rotate([90, 0, 0])
            cylinder(d = TM1_XB_D_HOLDER, h = 60, center = true, $fn = TM1_FN);
}

// ============================ NAIL-MIMIC BLADE (B45 family) ============================
// A plate of thickness 2r rising at `attack` degrees toward +X from an edge whose
// lowest point is at z = TM1_SH_BOT - drop.  LOADED SENSE (test notation) = +X:
// the leading face is the plate underside, a 45 deg face like W's (+X) face, and
// hair ahead of it is pressed down and passed under the edge ("plate-first").
// The -X stroke is "edge-first" (plate trailing, tip-interface 1.4); it meets
// the open ~68 deg V between plate and lump (see tips.md 4.2 / 10).
// Behind the plate (-X) a drafted "pulp" lump fills the space up to the band.
//   mode = "printed" : plate is printed as part of the tip (PETG, 0.10 mm layers)
//   mode = "slot"    : plate omitted; the lump is cut back to the plane of the
//                      plate's upper face, giving a true `attack`-degree bonding
//                      face; CA-bond a sheet blade (thickness 2r) onto it with its
//                      top end butted against the band (sheet + carrier = printed).
//                      (rev 2026-10-01: the earlier 2r X-shift left a ~36 deg face.)
// The working part is clipped at the band-bottom plane (B45-12 plate ends would
// otherwise rise 0.7 mm beside the band, into the TPU seam sleeve).
//   w       edge width (Y);  r = half plate thickness = modelled edge radius
//   crown_r transverse crown radius (9 = index nail)
module tm1_nail_blade(w = 8, r = 0.5, attack = 45, drop = 7.0, x0 = -0.35,
                      d_root = 9.5, s_lump = 3.6, crown_r = 9, mode = "printed") {
    ux = cos(attack);
    uz = sin(attack);
    z0 = TM1_SH_BOT - drop + r;              // edge cylinder centre
    intersection() {
        union() {
            if (mode == "printed")
                hull() {
                    tm1_ycyl(r, w, x0, z0);
                    tm1_ycyl(r, w, x0 + d_root * ux, z0 + d_root * uz);
                }
            difference() {
                hull() {                       // pulp lump (drafted, behind the plate)
                    tm1_band_slab();
                    tm1_ycyl(r, min(w, TM1_SH_Y), x0 + s_lump * ux, z0 + s_lump * uz);
                }
                if (mode == "slot")            // remove all lump in front of the plate's upper face
                    translate([x0 - r * uz, 0, z0 + r * ux]) rotate([0, -attack, 0])
                        translate([-50, -50, -100]) cube([100, 100, 100]);
            }
        }
        tm1_crown(crown_r, TM1_SH_BOT - drop);
        translate([0, 0, TM1_SH_BOT + 0.01 - 50]) cube(100, center = true);   // band-plane clip
    }
}

// ============================ DEMO ============================
if (TM1_DEMO) {
    color("orange") tm1_tip_base();
    translate([25, 0, 0]) difference() {
        translate([0, 0, 8]) cube([18, 13, 16], center = true);   // block with pocket, mouth at z=0
        tm1_pocket();
    }
}
