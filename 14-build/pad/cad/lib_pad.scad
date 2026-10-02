// =====================================================================
//  lib_pad.scad - SP1 v3 PAD: constants and one module per printed part
//  PROJECT SCRATCH · 14-build/pad/cad · PAD engineer · 2026-10-02 · units mm, degrees
// ---------------------------------------------------------------------
//  FRAME P (SYSTEM-SPEC-v3 3.1): origin = nail plane on the pad axis (centre-nail tip at
//  extension 15.0 on the R85 design head); +z away from the scalp; +x = bail tangent;
//  pentagon pin P0 on +x.  Every part is modelled IN ITS INSTALLED POSITION (block at home).
//  Basic primitives only (cube, cylinder, sphere, polygon, rotate_extrude, linear_extrude,
//  hull, booleans).  The deck's three pocket ceilings are a polyhedron built from the
//  height fields in pockets_data.scad, which gen_pad_stl.py writes from pad_geom2.py.
//  gen_pad_stl.py mirrors every constant and module here under the same name; the only
//  intentional difference: seg_cyl() here is a hull of two spheres (round ends), in Python a
//  plain cylinder.  Mating features are identical.
// =====================================================================
$fn = 48;
include <pockets_data.scad>

// ---- fasteners
M2_CLEAR = 2.4; M2_PILOT = 1.7; M3_CLEAR = 3.4; M3_INS_D = 4.0; M3_INS_L = 4.0;
// ---- stack (z above the nail plane at home)
Z_SKIRT_BOT = 32.0; SKIRT_T = 2.0;
Z_FLOOR0 = 34.0; Z_FLOOR1 = 38.0;
Z_CART0 = 38.0;  Z_CART1 = 80.0;
Z_GAL0 = 80.0;   Z_GAL1 = 83.5;
Z_YOKE0 = 83.5;  Z_YOKE1 = 87.0;
Z_CABLE = 85.5;
R_BLOCK = 27.0;
PIN_R = 18.0;
PINS = concat([[0, 0]], [for (k = [0:4]) [PIN_R * cos(72 * k), PIN_R * sin(72 * k)]]);   // C, P0..P4
// ---- cartridge
CART_OD = 9.4; CART_OD_TOP = 8.7; CART_TOP_L = 4.0;
CART_BORE_LAND = 4.6; BUSH_BORE = 5.95; PISTON_BORE = 7.0;
Z_BUSH0 = 50.0; Z_BUSH1 = 54.0;
CART_SOCKET = 9.55;
// ---- nail
LAND_D = 3.92; TIP_FLAT_D = 2.0; TIP_R = 0.4; NAIL_TOP_R = 0.5;
Z_LAND_TOP_E15 = 59.9;
INSERT_D = 2.0; INSERT_L = 4.0;
// ---- piston
PISTON_D = 5.8; PISTON_H = 4.5; MAG_C1_D = 3.25; MAG_C1_H = 1.62;
// ---- dome lugs / PTFE balls
RD = 38.0; DOME_ANG = [30, 150, 270]; ZD = 91.5; BALL_D = 6.35;
LUG_W = 7.0; Z_LUG1 = 87.0;
// ---- columns and ports
COL_R = 24.0; COL_ANG = [108, 180, 252]; COL_D = 5.0;
PORT_B = 108; PORT_A = 252; Z_PORT = 60.0;
// ---- yoke / coupling
R_YOKE = 14.0; YOKE_MAG_R = 8.0; YOKE_MAG_ANG = [30, 150, 270]; POST_R = 10.0; POST_ANG = [90, 210, 330];
MAG_CPL_D = 6.45; MAG_CPL_H = 3.4;
WASHER_D = 7.1; WASHER_T = 0.6;
CAGE_R_IN = 20.0; CAGE_H = 1.5;
// ---- deck
Z_DECK_TOP = 108.0; DECK_PLATE_T = 1.5; SHELL_T = 1.0;
POST_RAD = 58.0; POST_ANGS = [78, 102, 198, 222, 318, 342]; POST_D = 5.0;
SEAT_R = 55.0; SEAT_ANG = [30, 150, 270]; Z_SEAT = 109.5;
DISC_R = 42.0; DISC_D = 8.1; DISC_T = 1.1;
// ---- skirt frame
SK_R_BOT = 51.0; SK_R_TOP = 56.0; Z_SK0 = 36.0; Z_SK1 = 79.5;
SKID_R = 60.0; SKID_ANG = [60, 180, 300]; SKID_STEM_D = 6.0;
STOP_R = 65.0; STOP_ANG = [90, 210, 330];
LIFT_ANG = [60, 180, 300]; LIFT_LOW = [28.5, 36.0]; LIFT_HIGH = [55.5, 77.0];
SKID_DOME_R = 15.0; SKID_FOOT_D = 8.0;
ZF = -85.0 + sqrt(pow(85.0 + SKID_DOME_R, 2) - pow(SKID_R, 2));

// ===================================================================== helpers
function polar(r, a) = [r * cos(a), r * sin(a)];
module cyl(r, z0, z1, x = 0, y = 0, r2 = -1, fn = 48) {
    translate([x, y, z0]) cylinder(h = z1 - z0, r1 = r, r2 = (r2 < 0 ? r : r2), $fn = fn);
}
module box(x0, x1, y0, y1, z0, z1) { translate([x0, y0, z0]) cube([x1 - x0, y1 - y0, z1 - z0]); }
module radial_bar(a, r0, r1, w, z0, z1) { rotate([0, 0, a]) box(r0, r1, -w / 2, w / 2, z0, z1); }
module radial_cyl(a, r0, r1, rad, z) { rotate([0, 0, a]) translate([r0, 0, z]) rotate([0, 90, 0]) cylinder(h = r1 - r0, r = rad, $fn = 24); }
module seg_cyl(p0, p1, rad) { hull() { translate(p0) sphere(rad, $fn = 12); translate(p1) sphere(rad, $fn = 12); } }

// height-field prism over a polar grid about home: bottom = Z[i][j] + zoff, top = ztop.
module hf_prism(Z, home, zoff, ztop, rextra) {
    nt = len(POCKET_TH);
    R  = rextra > 0 ? concat(POCKET_RS, [POCKET_RS[len(POCKET_RS) - 1] + rextra]) : POCKET_RS;
    ZB = rextra > 0 ? concat(Z, [Z[len(Z) - 1]]) : Z;
    n  = len(R);
    NT = 1 + (n - 1) * nt;
    top = concat([[home[0], home[1], ztop]],
                 [for (i = [1:n - 1]) for (j = [0:nt - 1]) [home[0] + R[i] * cos(POCKET_TH[j]), home[1] + R[i] * sin(POCKET_TH[j]), ztop]]);
    bot = concat([[home[0], home[1], ZB[0][0] + zoff]],
                 [for (i = [1:n - 1]) for (j = [0:nt - 1]) [home[0] + R[i] * cos(POCKET_TH[j]), home[1] + R[i] * sin(POCKET_TH[j]), ZB[i][j] + zoff]]);
    function v(i, j, t) = (t ? 0 : NT) + (i == 0 ? 0 : 1 + (i - 1) * nt + (j % nt));
    // OpenSCAD wants faces clockwise seen from outside
    fan_t  = [for (j = [0:nt - 1]) [v(0, 0, true), v(1, j + 1, true), v(1, j, true)]];
    fan_b  = [for (j = [0:nt - 1]) [v(0, 0, false), v(1, j, false), v(1, j + 1, false)]];
    quad_t = [for (i = [1:n - 2]) for (j = [0:nt - 1]) each [[v(i, j, true), v(i + 1, j + 1, true), v(i + 1, j, true)], [v(i, j, true), v(i, j + 1, true), v(i + 1, j + 1, true)]]];
    quad_b = [for (i = [1:n - 2]) for (j = [0:nt - 1]) each [[v(i, j, false), v(i + 1, j, false), v(i + 1, j + 1, false)], [v(i, j, false), v(i + 1, j + 1, false), v(i, j + 1, false)]]];
    side   = [for (j = [0:nt - 1]) each [[v(n - 1, j, true), v(n - 1, j + 1, false), v(n - 1, j, false)], [v(n - 1, j, true), v(n - 1, j + 1, true), v(n - 1, j + 1, false)]]];
    polyhedron(points = concat(top, bot), faces = concat(fan_t, fan_b, quad_t, quad_b, side), convexity = 6);
}
POCKET_Z = [POCKET_Z0, POCKET_Z1, POCKET_Z2];

// ===================================================================== PD01 deck (SLA)
module pd01_deck() {
    ZT = 116.0;
    SR = sqrt(SEAT_R * SEAT_R + Z_SEAT * Z_SEAT);
    rmax = POCKET_RS[len(POCKET_RS) - 1];
    difference() {
        union() {
            for (k = [0:2]) intersection() {               // open pocket shells
                difference() {
                    hf_prism(POCKET_Z[k], POCKET_HOMES[k], 0, ZT, SHELL_T);
                    hf_prism(POCKET_Z[k], POCKET_HOMES[k], SHELL_T, ZT + 1, 0);
                }
                box(-200, 200, -200, 200, 0, Z_DECK_TOP);
            }
            cyl(14, Z_DECK_TOP - DECK_PLATE_T, Z_DECK_TOP);   // lattice hub, spokes, posts
            for (a = POST_ANGS) {
                radial_bar(a, 0, POST_RAD, 6, Z_DECK_TOP - DECK_PLATE_T, Z_DECK_TOP);
                p = polar(POST_RAD, a);
                difference() { cyl(POST_D / 2, Z_SK1, Z_DECK_TOP, p[0], p[1]); cyl(1.4, Z_SK1 + 8.5, Z_DECK_TOP - 2, p[0], p[1], fn = 16); }
            }
            for (k = [0:2]) difference() {
                cyl(rmax + SHELL_T, Z_DECK_TOP - DECK_PLATE_T, Z_DECK_TOP, POCKET_HOMES[k][0], POCKET_HOMES[k][1], fn = 96);
                cyl(rmax - 2, Z_DECK_TOP - DECK_PLATE_T - 1, Z_DECK_TOP + 1, POCKET_HOMES[k][0], POCKET_HOMES[k][1], fn = 96);
            }
            // seat pillars and disc bosses, clipped to "above the ceiling or outside the pockets",
            // cut to the seat sphere about P0, hollowed
            difference() {
                intersection() {
                    union() for (a = SEAT_ANG) {
                        radial_bar(a, SEAT_R - 6.5, SEAT_R + 6.5, 12, 80, Z_SEAT + 4);
                        p = polar(DISC_R, a); cyl(DISC_D / 2 + 1.5, 80, Z_DECK_TOP + 0.4, p[0], p[1]);
                    }
                    union() {
                        for (k = [0:2]) hf_prism(POCKET_Z[k], POCKET_HOMES[k], 0, ZT, SHELL_T);
                        difference() {
                            box(-200, 200, -200, 200, 60, ZT + 3);
                            for (k = [0:2]) cyl(rmax + SHELL_T, 70, ZT + 2, POCKET_HOMES[k][0], POCKET_HOMES[k][1], fn = 96);
                        }
                    }
                    union() { sphere(SR, $fn = 256); box(-200, 200, -200, 200, -10, Z_DECK_TOP + 0.41); }
                }
                for (a = SEAT_ANG) {
                    p = polar(DISC_R, a); cyl(DISC_D / 2 - 0.3, 80, Z_DECK_TOP + 0.4 - DISC_T - 2.5, p[0], p[1]);
                    radial_bar(a, SEAT_R - 4.5, SEAT_R + 4.5, 8, 80, Z_SEAT - 6);
                }
            }
        }
        // meridional V-groove on the 270 deg seat (yaw key for the HALO ball)
        hull() for (t = [-6.5:2.6:6.5]) {
            r = SEAT_R + t; z = sqrt(SR * SR - r * r); p = polar(r, SEAT_ANG[2]);
            translate([p[0], p[1], z]) rotate([0, 0, SEAT_ANG[2]]) rotate([45, 0, 0]) cube(2.6, center = true);
        }
        for (a = SEAT_ANG) { p = polar(DISC_R, a); cyl(DISC_D / 2, Z_DECK_TOP + 0.4 - DISC_T, Z_DECK_TOP + 1, p[0], p[1]); }
        for (a = POST_ANGS) { p = polar(POST_RAD, a); cyl(M2_PILOT / 2, Z_SK1 - 0.1, Z_SK1 + 8, p[0], p[1], fn = 16); }
    }
}

// ===================================================================== PD02 skirt frame (MJF)
module pd02_skirt_frame() {
    difference() {
        union() {
            difference() { cyl(SK_R_BOT + 2.5, Z_SK0, Z_SK0 + 3, fn = 128); cyl(SK_R_BOT, Z_SK0 - 1, Z_SK0 + 4, fn = 128); }
            difference() { cyl(SK_R_TOP + 2.5, Z_SK1 - 3.5, Z_SK1, fn = 128); cyl(SK_R_TOP, Z_SK1 - 5, Z_SK1 + 1, fn = 128); }
            for (a = POST_ANGS) {
                b = polar(SK_R_BOT + 1.5, a); t = polar(SK_R_TOP + 1.5, a);
                seg_cyl([b[0], b[1], Z_SK0 + 1], [t[0], t[1], Z_SK1 - 1], 2.0);
                p = polar(POST_RAD, a); cyl(POST_D / 2 + 1.6, Z_SK1 - 4, Z_SK1, p[0], p[1]);
            }
            for (a = SKID_ANG) {
                radial_bar(a, SK_R_TOP + 2, SKID_R + 4.5, 9, Z_SK1 - 6, Z_SK1);
                radial_bar(a, SK_R_BOT + 2, SKID_R + 4.5, 9, Z_SK0, Z_SK0 + 6);
            }
            for (a = LIFT_ANG) radial_bar(a, LIFT_HIGH[0] - 1, SK_R_TOP + 1, 4, LIFT_HIGH[1] - 2, Z_SK1);
            for (a = STOP_ANG) {
                radial_bar(a, SK_R_TOP + 1, STOP_R + 1, 8, Z_SK1 - 3.5, Z_SK1);
                radial_bar(a, STOP_R - 6, STOP_R + 1, 8, Z_SK1 - 0.01, Z_CABLE - 3.5);
            }
            for (a = [PORT_B, PORT_A]) radial_bar(a, SK_R_BOT + 2, SK_R_BOT + 7, 7, Z_SK0, Z_SK0 + 6);
        }
        for (a = POST_ANGS) { p = polar(POST_RAD, a); cyl(M2_CLEAR / 2, Z_SK1 - 5, Z_SK1 + 1, p[0], p[1], fn = 16); }
        for (a = SKID_ANG) {
            p = polar(SKID_R, a);
            cyl(M3_CLEAR / 2, Z_SK1 - 7, Z_SK1 + 1, p[0], p[1], fn = 20);
            cyl(3.1, Z_SK1 - 7, Z_SK1 - 3.5, p[0], p[1], fn = 24);
            cyl(SKID_STEM_D / 2 + 0.15, Z_SK0 - 1, Z_SK0 + 7, p[0], p[1], fn = 32);
        }
        for (a = LIFT_ANG) {
            p0 = polar(LIFT_HIGH[0] - 0.5, a - 8); p1 = polar(LIFT_HIGH[0] - 0.5, a + 8);
            seg_cyl([p0[0], p0[1], LIFT_HIGH[1] - 0.5], [p1[0], p1[1], LIFT_HIGH[1] - 0.5], 0.6);
        }
        for (a = STOP_ANG) for (dy = [-2.5, 2.5]) rotate([0, 0, a]) cyl(1.0, Z_SK1 - 5, Z_CABLE, STOP_R - 2, dy, fn = 16);
        for (a = [PORT_B, PORT_A]) rotate([0, 0, a]) cyl(1.65, Z_SK0 - 1, Z_SK0 + 7, SK_R_BOT + 5.5, 0, fn = 20);
    }
}

// ===================================================================== PD05 floor plate (SLA)
module pd05_floor_plate() {
    difference() {
        union() {
            cyl(R_BLOCK, Z_FLOOR0, Z_FLOOR1, fn = 96);
            for (p = PINS) difference() { cyl(CART_SOCKET / 2 + 1.2, Z_FLOOR1, Z_FLOOR1 + 1.5, p[0], p[1]); cyl(CART_SOCKET / 2, Z_FLOOR1 - 0.1, Z_FLOOR1 + 2, p[0], p[1]); }
            for (a = LIFT_ANG) difference() { radial_bar(a, R_BLOCK - 2, LIFT_LOW[0] + 1.8, 4, Z_FLOOR0, Z_FLOOR1); rotate([0, 0, a]) cyl(0.7, Z_FLOOR0 - 1, Z_FLOOR1 + 1, LIFT_LOW[0], 0, fn = 12); }
            for (a = COL_ANG) { p = polar(COL_R, a); cyl(COL_D / 2 + 0.5, Z_FLOOR1, Z_FLOOR1 + 1, p[0], p[1]); }
        }
        for (p = PINS) cyl(BUSH_BORE / 2, Z_FLOOR0 - 0.1, Z_FLOOR1 + 0.1, p[0], p[1], fn = 32);
        for (a = COL_ANG) { p = polar(COL_R, a); cyl(M2_CLEAR / 2, Z_FLOOR0 - 0.1, Z_FLOOR1 + 1.5, p[0], p[1], fn = 16); cyl(2.2, Z_FLOOR0 - 0.1, Z_FLOOR0 + 1.6, p[0], p[1], fn = 16); }
        translate([R_BLOCK, 0, Z_FLOOR1]) rotate([0, 0, 45]) cube([2, 2, 10], center = true);                              // orientation notch at P0
        difference() { cyl(R_BLOCK + 1, Z_FLOOR0 + 1, Z_FLOOR0 + 2); cyl(R_BLOCK - 0.6, Z_FLOOR0 + 0.9, Z_FLOOR0 + 2.1); }   // snap groove
        for (a = [36, 324]) { p = polar(22, a); cyl(3.0, Z_FLOOR1 - 2.5, Z_FLOOR1 + 0.1, p[0], p[1], fn = 24); }
        for (a = [0, 72, 144, 216, 288]) { p = polar(9, a + 36); cyl(2.2, Z_FLOOR1 - 2.5, Z_FLOOR1 + 0.1, p[0], p[1], fn = 24); }
    }
}

// ===================================================================== PD06 cartridge (SLA)
module pd06_cartridge(x = 0, y = 0) {
    translate([x, y, 0]) difference() {
        rotate_extrude($fn = 64) polygon([[0, Z_CART0], [CART_OD / 2, Z_CART0], [CART_OD / 2, Z_CART1 - CART_TOP_L], [CART_OD_TOP / 2, Z_CART1 - CART_TOP_L + 0.4], [CART_OD_TOP / 2, Z_CART1], [0, Z_CART1]]);
        rotate_extrude($fn = 64) polygon([[0, Z_CART0 - 0.1], [CART_BORE_LAND / 2, Z_CART0 - 0.1], [CART_BORE_LAND / 2, Z_BUSH0], [BUSH_BORE / 2, Z_BUSH0], [BUSH_BORE / 2, Z_BUSH1],
                                          [PISTON_BORE / 2, Z_BUSH1], [PISTON_BORE / 2, Z_CART1 - 0.6], [PISTON_BORE / 2 + 0.3, Z_CART1 + 0.1], [0, Z_CART1 + 0.1]]);
        translate([2.9, 0, 55.5]) rotate([0, 90, 0]) cylinder(h = 3, r = 0.5, $fn = 12);      // rod-side vent
        box(CART_OD / 2 - 0.6, CART_OD / 2 + 0.5, -0.5, 0.5, 55, Z_CART1 + 0.1);                // vent groove
    }
}

// ===================================================================== PD07 gallery plate (SLA)
module gallery_channels() {
    zc = (Z_GAL0 + Z_GAL1) / 2;
    module ch(p0, p1) seg_cyl([p0[0], p0[1], zc], [p1[0], p1[1], zc], 0.7);
    module arc(a0, a1, r, n) for (i = [0:n - 1]) ch(polar(r, a0 + (a1 - a0) * i / n), polar(r, a0 + (a1 - a0) * (i + 1) / n));
    arc(PORT_B, 72, COL_R, 10); ch(polar(COL_R, 72), PINS[2]); ch(PINS[2], PINS[0]); ch(PINS[0], PINS[5]);      // gallery B: C, P1, P4
    arc(PORT_A, 360, COL_R, 14); arc(PORT_A, 144, COL_R, 14);                                                   // gallery A: P0, P2, P3
    ch(polar(COL_R, 216), PINS[4]); ch(polar(COL_R, 0), PINS[1]); ch(polar(COL_R, 144), PINS[3]);
    for (a = [PORT_B, PORT_A]) { p = polar(COL_R, a); cyl(0.7, Z_PORT, zc + 0.7, p[0], p[1], fn = 12); radial_cyl(a, COL_R, COL_R + 6.2, 0.6, Z_PORT); }
}
module pd07_gallery_plate() {
    zc = (Z_GAL0 + Z_GAL1) / 2;
    union() {
        difference() {
            union() {
                cyl(R_BLOCK, Z_GAL0, Z_GAL1, fn = 96);
                for (a = COL_ANG) { p = polar(COL_R, a); cyl(COL_D / 2, Z_FLOOR1 + 1, Z_GAL0 + 0.01, p[0], p[1]); }
                for (a = [PORT_B, PORT_A]) {
                    radial_cyl(a, COL_R, COL_R + 6, 1.25, Z_PORT);
                    rotate([0, 0, a]) translate([COL_R + 4, 0, Z_PORT]) rotate([0, 90, 0]) cylinder(h = 1.5, r1 = 1.5, r2 = 1.0, $fn = 24);   // barb ridge
                }
                for (a = DOME_ANG) {
                    radial_bar(a, R_BLOCK - 6, RD, LUG_W, Z_GAL0, Z_LUG1);
                    p = polar(RD, a); cyl(3.75, Z_LUG1 - 0.01, ZD - 1, p[0], p[1]); cyl(3.75, ZD - 1, ZD + 0.4, p[0], p[1], r2 = 3.3);
                }
                difference() { cyl(CAGE_R_IN + 1.5, Z_GAL1 - 0.01, Z_GAL1 + CAGE_H); cyl(CAGE_R_IN, Z_GAL1 - 1, Z_GAL1 + CAGE_H + 1); }
            }
            for (a = DOME_ANG) { p = polar(RD, a); translate([p[0], p[1], ZD]) sphere(BALL_D / 2 - 0.05, $fn = 48); }   // PTFE ball press socket
            for (p = PINS) cyl(0.7, Z_GAL0 - 0.1, zc + 0.7, p[0], p[1], fn = 16);
            gallery_channels();
            for (a = YOKE_MAG_ANG) { p = polar(YOKE_MAG_R, a); cyl(WASHER_D / 2, Z_GAL1 - WASHER_T, Z_GAL1 + 0.1, p[0], p[1], fn = 32); }
            for (a = COL_ANG) { p = polar(COL_R, a); cyl(M2_PILOT / 2, Z_FLOOR1 + 0.9, Z_FLOOR1 + 9, p[0], p[1], fn = 16); }
            for (i = [0:5]) {
                p = PINS[i]; a = (i == 0) ? 36 : atan2(p[1], p[0]); r0 = norm(p);
                rotate([0, 0, a]) box((i == 0 ? 3.5 : r0 + 3.5), R_BLOCK + 1, -0.4, 0.4, Z_GAL0 - 0.1, Z_GAL0 + 0.5);   // vent grooves
            }
        }
        for (p = PINS) difference() { cyl(4.2, Z_GAL0 - 0.4, Z_GAL0 + 0.01, p[0], p[1]); cyl(3.8, Z_GAL0 - 1, Z_GAL0 + 1, p[0], p[1]); }   // sleeve-clamp beads
    }
}

// ===================================================================== PD08 wiper skirt plate (MJF)
module pd08_skirt_plate() {
    union() {
        difference() {
            rotate_extrude($fn = 96) polygon([[0, Z_SKIRT_BOT], [R_BLOCK - 1, Z_SKIRT_BOT], [R_BLOCK, Z_SKIRT_BOT + 1], [R_BLOCK, Z_SKIRT_BOT + 2], [0, Z_SKIRT_BOT + 2]]);
            for (p = PINS) { cyl(4.55, Z_SKIRT_BOT + 1, Z_SKIRT_BOT + 2.1, p[0], p[1], fn = 40); cyl(3.0, Z_SKIRT_BOT - 0.1, Z_SKIRT_BOT + 1.01, p[0], p[1], r2 = 2.2, fn = 40); }
        }
        for (a = [0, 120, 240]) rotate([0, 0, a + 36]) {
            box(R_BLOCK + 0.1, R_BLOCK + 1.3, -3, 3, Z_SKIRT_BOT + 1, Z_FLOOR0 + 2);
            box(R_BLOCK - 0.5, R_BLOCK + 1.3, -3, 3, Z_FLOOR0 + 1.1, Z_FLOOR0 + 1.9);
        }
    }
}

// ===================================================================== PD09 piston (SLA or POM)
module pd09_piston(x = 0, y = 0, e = 15) {
    zb = Z_LAND_TOP_E15 + (15 - e);
    translate([x, y, 0]) difference() {
        rotate_extrude($fn = 48) polygon([[0, zb], [PISTON_D / 2, zb], [PISTON_D / 2, zb + PISTON_H - 0.5], [PISTON_D / 2 - 0.5, zb + PISTON_H], [0, zb + PISTON_H]]);
        cyl(MAG_C1_D / 2, zb - 0.1, zb + MAG_C1_H, 0, 0, fn = 32);
    }
}

// ===================================================================== PD10 yoke (SLA)
module pd10_yoke() {
    w = 2 * (R_YOKE - POST_R + 0.5) * tan(22) + 0.9;
    difference() {
        cyl(R_YOKE, Z_YOKE0, Z_YOKE1, fn = 96);
        for (a = YOKE_MAG_ANG) { p = polar(YOKE_MAG_R, a); cyl(MAG_CPL_D / 2, Z_YOKE0 - 0.1, Z_YOKE0 + MAG_CPL_H, p[0], p[1], fn = 40); }
        for (a = POST_ANG) rotate([0, 0, a]) {
            hull() { box(POST_R - 0.1, POST_R + 0.1, -0.45, 0.45, Z_CABLE - 0.45, Z_YOKE1 + 0.1); box(R_YOKE + 0.4, R_YOKE + 0.6, -w / 2, w / 2, Z_CABLE - 1.15, Z_YOKE1 + 0.1); }
            box(POST_R - 4.2, POST_R - 0.4, -1.1, 1.1, Z_CABLE - 1.1, Z_YOKE1 + 0.1);     // ferrule pocket
            box(POST_R - 0.5, POST_R + 0.2, -0.45, 0.45, Z_CABLE - 0.45, Z_YOKE1 + 0.1);
        }
        cyl(1.5, Z_YOKE0 - 0.1, Z_YOKE1 + 0.1, fn = 20);
    }
}

// ===================================================================== PD11 tendon stop block (PETG)
module pd11_stop_block(a = 90) {
    L = 14;
    rotate([0, 0, a]) difference() {
        box(STOP_R - 6, STOP_R - 6 + L, -4, 4, Z_CABLE - 3.5, Z_CABLE + 4);
        translate([STOP_R - 6 + 2.5, 0, Z_CABLE]) rotate([0, 90, 0]) cylinder(h = L + 2, r = 2.6, $fn = 32);   // series-spring bore 0 5.2
        translate([STOP_R - 7, 0, Z_CABLE]) rotate([0, 90, 0]) cylinder(h = 4, r = 0.5, $fn = 12);           // cable exit
        translate([STOP_R - 6 + L - 3, 0, Z_CABLE]) rotate([0, 90, 0]) cylinder(h = 3, r = M3_INS_D / 2, $fn = 24);  // M3 insert (barrel adjuster)
        for (dy = [-2.5, 2.5]) cyl(1.0, Z_CABLE - 5, Z_CABLE - 2, STOP_R - 2, dy, fn = 16);
    }
}

// ===================================================================== PD12-14 skid stem, foot, knob
module pd12_skid_stem(a = 60, H = 0) {
    ztop = Z_SK1 - 3.5; zbot = ZF + SKID_DOME_R - 1 - H; p = polar(SKID_R, a);
    translate([p[0], p[1], 0]) difference() {
        cyl(SKID_STEM_D / 2, zbot, ztop, fn = 32);
        cyl(M3_INS_D / 2, ztop - M3_INS_L, ztop + 0.1, fn = 24);
        box(2.5, 4, -4, 4, zbot + 12, ztop + 1);                       // anti-rotation flat
        cyl(1.9, zbot + 3, ztop - M3_INS_L - 2, fn = 24);               // hollow
    }
}
module pd13_skid_foot(a = 60, H = 0) {
    p = polar(SKID_R, a);
    tilt = asin(SKID_R / (85 + SKID_DOME_R));
    union() {
        hull() {
            translate([p[0], p[1], ZF - H]) rotate([0, 0, a]) rotate([0, -tilt, 0])
                intersection() { sphere(SKID_DOME_R, $fn = 96); cyl(SKID_FOOT_D / 2, -SKID_DOME_R - 0.1, -SKID_DOME_R + 3, fn = 48); }
            cyl(4.5, ZF - H + SKID_DOME_R - 6, ZF - H + SKID_DOME_R - 5, p[0], p[1], fn = 40);
        }
        difference() { cyl(4.5, ZF - H + SKID_DOME_R - 6, ZF - H + SKID_DOME_R + 1, p[0], p[1], fn = 40); cyl(SKID_STEM_D / 2 + 0.1, ZF - H + SKID_DOME_R - 1, ZF - H + SKID_DOME_R + 1.5, p[0], p[1], fn = 40); }
    }
}
module pd14_skid_knob(a = 60) {
    p = polar(SKID_R, a);
    difference() { cyl(6, Z_SK1 + 0.2, Z_SK1 + 6, p[0], p[1], fn = 12); cyl(2.85, Z_SK1 + 0.1, Z_SK1 + 3.2, p[0], p[1], fn = 6); cyl(M3_CLEAR / 2, Z_SK1 - 1, Z_SK1 + 7, p[0], p[1], fn = 16); }
}

// ===================================================================== PD15 nail (CNC-turned POM; reference)
module pd15_nail(x = 0, y = 0, e = 15) {
    z0 = 15 - e; h = (LAND_D - TIP_FLAT_D) / 2;
    translate([x, y, 0]) rotate_extrude($fn = 64) polygon([[0, z0], [TIP_FLAT_D / 2 - TIP_R, z0], [TIP_FLAT_D / 2, z0 + TIP_R * 0.6], [LAND_D / 2, z0 + h + TIP_R * 0.4],
        [LAND_D / 2, z0 + Z_LAND_TOP_E15 - NAIL_TOP_R], [LAND_D / 2 - NAIL_TOP_R, z0 + Z_LAND_TOP_E15], [0, z0 + Z_LAND_TOP_E15]]);
}

// ===================================================================== PD16-18 bench jigs (PETG)
module pd16_hang_cup() translate([150, 0, 0]) union() {
    difference() { cyl(11, 0, 14, fn = 64); cyl(10, 1, 15, fn = 64); }
    difference() { box(-1.5, 1.5, -6, 6, 13.5, 18); translate([0, 2, 16.2]) rotate([90, 0, 0]) cylinder(h = 4, r = 1.0, $fn = 16); }
}
module pd17_shadow_card() {
    h = (LAND_D - TIP_FLAT_D) / 2;
    translate([150, 40, 0]) difference() {
        box(0, 80, 0, 30, 0, 1.2);
        translate([0, 0, -0.4]) linear_extrude(2) polygon([[5, 15 - 1.05], [5.45, 15 - 1.05], [5 + h + 0.05, 15 - LAND_D / 2 - 0.05], [75, 15 - LAND_D / 2 - 0.05],
                                                          [75, 15 + LAND_D / 2 + 0.05], [5 + h + 0.05, 15 + LAND_D / 2 + 0.05], [5.45, 15 + 1.05], [5, 15 + 1.05]]);
        box(10, 30, 24, 24 + 3.95, -0.4, 1.6); box(40, 60, 24, 24 + 3.88, -0.4, 1.6);
    }
}
module pd18_skid_gauge() translate([150, 80, 0]) union() for (i = [0:18]) box(i * 4, i * 4 + 4, 0, 12, 0, 3 + 0.5 * i);

// ===================================================================== PD19 S0 single-pocket bench (SLA)
module pd19_s0_pocket() {
    h = POCKET_HOMES[0]; rmax = POCKET_RS[len(POCKET_RS) - 1];
    translate([-h[0], -h[1] + 200, 0]) union() {
        intersection() {
            difference() { hf_prism(POCKET_Z[0], h, 0, Z_DECK_TOP, 3.0); hf_prism(POCKET_Z[0], h, 3.0, Z_DECK_TOP + 1, 0); }
            box(-200, 200, -200, 200, 0, Z_DECK_TOP);
        }
        difference() {
            box(h[0] - 40, h[0] + 40, h[1] - 40, h[1] + 40, Z_DECK_TOP - 3, Z_DECK_TOP);
            cyl(rmax + 2, Z_DECK_TOP - 4, Z_DECK_TOP + 1, h[0], h[1], fn = 96);
            for (sx = [-1, 1]) for (sy = [-1, 1]) cyl(1.7, Z_DECK_TOP - 4, Z_DECK_TOP + 1, h[0] + sx * 34, h[1] + sy * 34, fn = 16);
        }
    }
}
