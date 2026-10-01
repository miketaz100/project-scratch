// =====================================================================
//  tip_E_carrier.scad — SP1 tip E: B45 blade on a TPU 90A "pulp" pad
//  PROJECT SCRATCH · 05-engineering/cad/tips · units: mm
//  THREE BODIES, selected with PART:
//    "carrier"  rigid PETG: TM1 tang + shoulder + 3 mm block with a dovetail
//               slot (5 mm mouth / 7 mm top, 2 mm deep) running through in Y
//    "pad"      TPU 90A 10 x 10 x 6 mm pad with the dovetail rail on top; its
//               +X face is chamfered 45 deg — the blade bonds onto that face
//    "blade"    1.0 mm nylon/PETG sheet blade blank, 8 x 9 mm, convex R 9 end
//               (print as a cutting template, or print in PETG 0.12 mm layers)
//    "assembly" preview of all three
//  Scratch direction +X.  Pad slides in along Y; fix with a drop of CA.
//  Edge lowest point about z = -15.9 (3.4 mm lower than W: lower the rig's
//  down-stop by that amount when running E).
// =====================================================================
include <tm1_tang_lib.scad>
$fn = TM1_FN;

PART        = "carrier";   // "carrier" | "pad" | "blade" | "assembly"
BLOCK_H     = 3.0;         // carrier block below the band
BLOCK_X     = 11.0;        // carrier block bottom width (drafted from 14)
DT_MOUTH    = 5.0;         // dovetail width at the block bottom (mouth)
DT_TOP      = 7.0;         // dovetail width at the top of the slot
DT_DEPTH    = 2.0;
DT_CLEAR    = 0.15;        // per side, on the TPU rail
PAD_X       = 10.0;
PAD_Y       = 10.0;
PAD_H       = 6.0;
PAD_ATTACK  = 45;          // blade face angle
PAD_REAR_DRAFT = 10;
BLADE_W     = 8.0;
BLADE_LEN   = 9.0;
BLADE_T     = 1.0;
BLADE_OVERHANG = 2.0;      // blade edge beyond the pad's bottom-front corner (along the face)
BLADE_CROWN_R  = 9.0;
CROSS_HOLE  = false;

ZB = TM1_SH_BOT - BLOCK_H;   // -8.5 : carrier block bottom = pad top

// trapezoid (in XZ) extruded along Y, centred: used for the dovetail slot and rail
module dovetail_xz(w_bot, w_top, z_bot, depth, len) {
    rotate([90, 0, 0]) linear_extrude(height = len, center = true)
        polygon([[-w_bot / 2, z_bot], [w_bot / 2, z_bot], [w_top / 2, z_bot + depth], [-w_top / 2, z_bot + depth]]);
}

module tip_E_carrier(cross_hole = CROSS_HOLE) {
    tm1_tip_base(cross_hole);
    difference() {
        hull() {
            tm1_band_slab();
            translate([0, 0, ZB]) linear_extrude(height = 0.02) tm1_rrect(BLOCK_X, TM1_SH_Y, TM1_SH_R);
        }
        dovetail_xz(DT_MOUTH, DT_TOP, ZB - 0.01, DT_DEPTH, TM1_SH_Y + 2);
    }
}

module tip_E_pad() {
    // rail (slides into the carrier dovetail along Y)
    dovetail_xz(DT_MOUTH - 2 * DT_CLEAR, DT_TOP - 2 * DT_CLEAR, ZB - 0.01, DT_DEPTH - DT_CLEAR, PAD_Y);
    // pad block: XZ profile, 45 deg front chamfer (+X), 10 deg rear draft (-X)
    rotate([90, 0, 0]) linear_extrude(height = PAD_Y, center = true)
        polygon([[-PAD_X / 2, ZB], [PAD_X / 2, ZB],
                 [PAD_X / 2 - PAD_H / tan(PAD_ATTACK), ZB - PAD_H],
                 [-PAD_X / 2 + PAD_H * tan(PAD_REAR_DRAFT), ZB - PAD_H]]);
}

// flat blade blank lying in XY (print flat or use as a cutting template)
module tip_E_blade() {
    linear_extrude(height = BLADE_T)
        offset(r = 1.5) offset(delta = -1.5)
            intersection() {
                translate([-BLADE_W / 2, 0]) square([BLADE_W, BLADE_LEN]);
                translate([0, BLADE_LEN - BLADE_CROWN_R]) circle(r = BLADE_CROWN_R, $fn = 180);
            }
}

// blade placed on the pad's 45 deg face (preview only): length axis runs down the
// face (-u), thickness points outward (+n), edge overhangs the bottom-front corner.
module tip_E_blade_placed() {
    cx = PAD_X / 2 - PAD_H / tan(PAD_ATTACK);     // pad bottom-front corner
    cz = ZB - PAD_H;
    ux = cos(PAD_ATTACK);  uz = sin(PAD_ATTACK);  // up the face
    nx = sin(PAD_ATTACK);  nz = -cos(PAD_ATTACK); // outward normal of the face
    s  = BLADE_LEN - BLADE_OVERHANG;
    translate([cx + s * ux + nx * BLADE_T, 0, cz + s * uz + nz * BLADE_T])
        rotate([0, -PAD_ATTACK, 0]) rotate([0, 0, 90]) tip_E_blade();
}

if (PART == "carrier") tip_E_carrier();
if (PART == "pad") tip_E_pad();
if (PART == "blade") tip_E_blade();
if (PART == "assembly") {
    color("orange") tip_E_carrier();
    color("gray") tip_E_pad();
    color("white") tip_E_blade_placed();
}
