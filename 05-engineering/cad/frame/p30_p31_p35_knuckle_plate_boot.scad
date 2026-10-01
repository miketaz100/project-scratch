// =====================================================================
//  p30_p31_p35_knuckle_plate_boot.scad - P30 knuckle plate (G1), P31 boot clamp frame, P35 boot cutting template
//  PROJECT SCRATCH · 05-engineering/cad/frame · units: mm · frame: global (P30, P31), local flat (P35)
//  Sources: mechanical.md section 8.7 (plate, slot, boot), 5.5 G1, 11 P30/P31/P35.
//  PART = "plate" | "frame" | "template" | "assembly"
//  Geometry: underside = sphere R 90 about (0, 0, -52.5) (37.5 above the centre nail edge), 1.6 thick; plan
//  outline 64 x 90 with R 3 corners (vertical prism clip); shared slot = union of three R 4 rounded rectangles
//  31.8 x 26.8 at (-8, -24) and (+8, +24), 34.8 x 29.8 at (0, 0), with a 15 deg lead-in on the underside.
//  CONFLICTS: an R 90 cap 64 x 90 sags 18.9 mm at the corners (section 11 says 8 tall); the 15 deg perimeter
//  draft and the R 3 / R 1.5 edge rounds are NOT modelled (C-H1, C-H2); the six M2 holes are at positions the
//  palm tray can carry (section 11 gives none): (0, +/-41), (23.5, -37), (-23.5, 37), (+/-23.5, 0).
// =====================================================================
include <lib_sp1.scad>
PART = "plate";

PL_X = 64;  PL_Y = 90;  CORNER_R = 3;
HOLES = [[0, -41], [0, 41], [23.5, -37], [-23.5, 37], [23.5, 0], [-23.5, 0]];   // 6 x diam 2.4 (M2 x 8 into P32 inserts)
HOLE_D = M2_CLEAR;
Z_BOT_CLIP = 10;  Z_TOP_CLIP = 45;

module p30_knuckle_plate() difference() {
    intersection() {
        sph_shell(KP_C_Z, KP_R, KP_R + KP_T);
        rbox_z(-PL_X / 2, PL_X / 2, -PL_Y / 2, PL_Y / 2, Z_BOT_CLIP, Z_TOP_CLIP, CORNER_R);
    }
    slot_cutter(0, 50, KP_C_Z + KP_R + 1.0);          // lead-in widens the slot over the lowest 1 mm (15 deg)
    for (h = HOLES) cyl_z(HOLE_D / 2, 0, 50, h[0], h[1], fn = 16);
}

// ---- P31 boot clamp frame: same sphere, 1.2 thick, on top of the 0.25 boot, 60 x 86 outline ----
FR_X = 60;  FR_Y = 86;
module p31_boot_frame() difference() {
    r_in = KP_R + KP_T + BOOT_T;
    intersection() {
        sph_shell(KP_C_Z, r_in, r_in + P31_T);
        rbox_z(-FR_X / 2, FR_X / 2, -FR_Y / 2, FR_Y / 2, 10, 45, CORNER_R);
    }
    translate([0, 0, 0]) linear_extrude(50) slot_cs();
    for (h = HOLES) cyl_z(HOLE_D / 2, 0, 50, h[0], h[1], fn = 16);
}

// ---- P35 boot cutting template (local, flat): 76 x 104 x 1 plate; boot outline = slot + 8 flange as a 0.5 groove,
//      three through windows at 70 % of the paddle section, alignment notches on both axes ----
TP_X = 76;  TP_Y = 104;  TP_T = 1;  FLANGE = 8;  GROOVE_D = 0.5;  GROOVE_W = 0.6;  HOLE_SCALE = 0.70;  MARK_L = 6;
module p35_boot_template() difference() {
    cbox(0, 0, TP_T / 2, TP_X, TP_Y, TP_T);
    translate([0, 0, TP_T - GROOVE_D]) linear_extrude(GROOVE_D + 1) difference() { slot_cs(FLANGE); offset(delta = -GROOVE_W) slot_cs(FLANGE); }
    for (n = [NAIL_L, NAIL_C, NAIL_R]) translate([0, 0, -1]) linear_extrude(TP_T + 2) rrect(n[0], n[1], PAD_SEC_X * HOLE_SCALE, PAD_SEC_Y * HOLE_SCALE, 1.0);
    for (s = [-1, 1]) { cbox(s * TP_X / 2, 0, TP_T / 2, MARK_L * 2, 1.0, TP_T + 2); cbox(0, s * TP_Y / 2, TP_T / 2, 1.0, MARK_L * 2, TP_T + 2); }
}

if (PART == "plate") p30_knuckle_plate();
if (PART == "frame") p31_boot_frame();
if (PART == "template") p35_boot_template();
if (PART == "assembly") { color("orange") p30_knuckle_plate(); color("gray") p31_boot_frame(); }
