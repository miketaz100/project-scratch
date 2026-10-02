// dish_bench.scad - S0a dish bench, every printed part (D01-D15)
// PROJECT SCRATCH, 14-build/S0/cad, 2026-10-02.  Source of truth; gen_s0_stl.py mirrors it.
// Set PART to one name below and render.  Parts are modelled in the dish frame (C = ball
// centre at the origin, +Z up the pad axis); PRINT = true turns the part into its print
// orientation (README.md).  The STLs in stl/ are already in print orientation.
//
// Dish geometry = SYSTEM-SPEC-v3 sec 4.2 read literally (ball offset d measured at the dish):
// concentric sphere R 160, inner rim 34 deg to d 13.7 (+4.52), outer rim 50 deg to d 17 (+8.45).
// The pocket ceiling is generated (pocket_cavity.scad, exact envelope of the 6 mm ball) and the
// templates' stylus paths are generated (template_paths.scad, corrected for block rotation).

include <s0_lib.scad>
include <pocket_cavity.scad>
include <template_paths.scad>

PART = "deck";   // deck | block | nose_plate | plunger | seat_disc | nail_N20 | nail_N30 | nail_N35 | c_arm |
                 // template_T1 | template_T2 | template_T3 | skid_ring | ball_cradle | side_mock | lift_gauge | assembly
PRINT = false;

// ------------------------------------------------------------------ D01 deck
module leg(a) {
    p = polar(LEG_R, a);
    zf = sqrt(FOOT_C_R*FOOT_C_R - LEG_R*LEG_R);          // 69.97
    cyl(LEG_D_BOT, zf, DECK_ZTOP - 3, p[0], p[1], d2=LEG_D_TOP);
    cyl(LEG_D_TOP + 6, DECK_ZTOP - 10, DECK_ZTOP - 3, p[0], p[1]);
    sph(FOOT_D, [p[0], p[1], zf]);
}
module deck() {
    difference() {
        union() {
            cyl(2*DECK_R, DECK_ZTOP - 3, DECK_ZTOP);                       // top plate (template seat)
            for (a = DOME_ANG) let(p = polar(A_DOME, a)) cyl(2*(POCKET_R + 2.5), DECK_ZU, DECK_ZTOP, p[0], p[1]);
            cyl(12, DECK_ZU, DECK_ZTOP);                                    // centre island
            for (a = DOME_ANG) leg(a);                                      // skid legs, feet on R 89
            cyl(GRIP[2], DECK_ZTOP, DECK_ZTOP + GRIP[3], GRIP[0], GRIP[1], d2=GRIP[2] - 2);   // helper's hold
        }
        for (a = DOME_ANG) rotate([0, 0, a - 90]) translate([0, A_DOME, 0]) pocket_cavity();
        cyl(3.2, DECK_ZU - 2, DECK_ZTOP + 1);                              // lift-elastic hole
        box(-7, 7, -2, 2, DECK_ZTOP - 2.5, DECK_ZTOP + 1);                 // toggle recess
        for (p = TPL_PIN) cyl(M3_PILOT, DECK_ZTOP - 8, DECK_ZTOP + 1, p[0], p[1], fn=24);
    }
}

// ------------------------------------------------------------------ D02 block
module block() {
    slope = (WELL_D_TOP - WELL_D_BOT) / (TOP_Z1 - WELL_Z_BOT);
    difference() {
        union() {
            cyl(BODY_D, NOSE_Z1, BODY_Z1);
            cyl(TOP_D, BODY_Z1, TOP_Z1);
            cyl(BODY_D, BODY_Z1 - 6, BODY_Z1, d2=TOP_D);                   // 45 deg chamfer under the rim
            box(EAR[0], EAR[1], EAR[2], EAR[3], NOSE_Z1, TOP_Z1);           // C-arm ear
            for (a = DOME_ANG) let(p = polar(A_DOME, a)) cyl(POST_D0, TOP_Z1 - 0.5, POST_TOP, p[0], p[1], d2=POST_D1);
        }
        for (a = DOME_ANG) let(p = polar(A_DOME, a)) sph(BALL_SOCKET_D, [p[0], p[1], Z_DOME], fn=48);
        for (a = NAIL_ANG) let(p = polar(NAIL_R, a)) {
            cyl(BORE_D, NOSE_Z1 - 1, BODY_Z1, p[0], p[1], fn=40);          // plunger + spring bore, open below
            cyl(M3_PILOT, BODY_Z1 - 0.5, TOP_Z1 + 1, p[0], p[1], fn=24);   // M3 x 6 preload set screw
        }
        for (a = SCREW_ANG) let(p = polar(SCREW_R, a)) cyl(M3_PILOT, NOSE_Z1 - 1, NOSE_Z1 + 11, p[0], p[1], fn=24);
        cyl(WELL_D_BOT, WELL_Z_BOT, TOP_Z1 + 1, d2=WELL_D_TOP + slope);    // conical well for the lift elastic
        cyl_ab(2.2, [-14, 0, HOOK_Z], [14, 0, HOOK_Z], fn=20);             // hook pin (paper clip) cross-hole
        for (zz = [128, 135]) cyl_ab(M3_PILOT, [0, EAR[2] - 1, zz], [0, EAR[2] + 12, zz], fn=20);
    }
}

// ------------------------------------------------------------------ D03 nose plate (stem guides)
module nose_plate() {
    difference() {
        union() { cyl(NOSE_D - 2, NOSE_Z0, NOSE_Z0 + 1, d2=NOSE_D); cyl(NOSE_D, NOSE_Z0 + 1, NOSE_Z1); }
        for (a = NAIL_ANG) let(p = polar(NAIL_R, a)) {
            cyl(STEM_BORE_D, NOSE_Z0 - 1, NOSE_Z1 + 1, p[0], p[1], fn=40);
            cyl(STEM_BORE_D + 1.2, NOSE_Z0 - 1, NOSE_Z0 + 0.6, p[0], p[1], d2=STEM_BORE_D, fn=40);
        }
        for (a = SCREW_ANG) let(p = polar(SCREW_R, a)) {
            cyl(M3_CLEAR, NOSE_Z0 - 1, NOSE_Z1 + 1, p[0], p[1], fn=24);
            cyl(M3_CB_D, NOSE_Z0 - 1, NOSE_Z0 + M3_CB_H, p[0], p[1], fn=24);
        }
    }
}

// ------------------------------------------------------------------ D04 plunger, D05 seat disc
module plunger() difference() {
    cyl(PLUNGER_D, 0, PLUNGER_H);
    cyl(MAG_D, -1, MAG_H, fn=32);                                          // 3 x 2 magnet, flush in the face
    cyl(CUP_D, PLUNGER_FLOOR, PLUNGER_H + 1, fn=40);                        // spring cup
}
module seat_disc() cyl(SEAT_D, 0, SEAT_H);

// ------------------------------------------------------------------ D06 / D07 nails
// 90 deg tip cone from a 2.0 mm flat (rim R 0.4) to 4.5 mm at 1.25 mm, then a constant 4.5 stem
// (safety ruling C2, "constant stem" option); steel pin hole in the top; ID rings (1 = reserve 2, 2 = reserve 3, 3 = reserve 3.5).
function nail_prof(L) = let(r0 = NAIL_TIP_D/2, r1 = STEM_D/2, rf = NAIL_TIP_R, t = rf*tan(22.5), cx = r0 - t, cz = rf)
    concat([[0, 0], [r0 - t, 0]],
           [for (k = [1:7]) let(a = -90 + 45*k/7) [cx + rf*cos(a), cz + rf*sin(a)]],
           [[r1, NAIL_CONE_H], [r1, L - 0.3], [r1 - 0.3, L], [0, L]]);
module nail(reserve, rings) {
    L = nail_len(reserve);
    difference() {
        rotate_extrude($fn=64) polygon(nail_prof(L));
        cyl(PIN_HOLE_D, L - PIN_HOLE_DEPTH, L + 1, fn=20);
        for (k = [0:rings-1]) let(zc = L - 1.5*(k + 1))
            difference() { cyl(STEM_D + 2, zc - 0.3, zc + 0.3); cyl(STEM_D - 0.6, zc - 0.4, zc + 0.4); }
    }
}

// ------------------------------------------------------------------ D08 C-arm (drive arm + styli bar)
module c_arm() {
    w = CARM_W/2;  lo0 = CARM_LOW_Z;  lo1 = CARM_LOW_Z + CARM_LOW_H;
    difference() {
        union() {
            box(-w - 2, w + 2, EAR[2] - 6, EAR[2], 124, lo1);                       // foot on the block ear
            box(-w, w, CARM_RISER_Y - 5, EAR[2] - 6, lo0, lo1);                     // lower bar
            box(-w, w, CARM_RISER_Y - 5, CARM_RISER_Y + 5, lo0, CARM_TOP_Z0 + CARM_TOP_H);   // riser
            box(-w, w, CARM_RISER_Y - 5, 8, CARM_TOP_Z0, CARM_TOP_Z0 + CARM_TOP_H);  // top bar (carries the styli)
            hull() { box(-w, w, CARM_RISER_Y + 5, CARM_RISER_Y + 6, lo1, lo1 + 14); box(-w, w, CARM_RISER_Y + 5, CARM_RISER_Y + 19, lo1, lo1 + 1); }
            hull() { box(-w, w, CARM_RISER_Y + 5, CARM_RISER_Y + 6, CARM_TOP_Z0 - 14, CARM_TOP_Z0); box(-w, w, CARM_RISER_Y + 5, CARM_RISER_Y + 19, CARM_TOP_Z0 - 1, CARM_TOP_Z0); }
            cyl_ab(DRIVE_GRIP[0], [0, CARM_RISER_Y - 4, DRIVE_GRIP[1]], [0, CARM_RISER_Y - 5 - DRIVE_GRIP[2], DRIVE_GRIP[1]], fn=40);
            sph(DRIVE_GRIP[0], [0, CARM_RISER_Y - 5 - DRIVE_GRIP[2], DRIVE_GRIP[1]], fn=40);
        }
        for (y = STYLUS_Y) cyl(M3_CLEAR, CARM_TOP_Z0 - 1, CARM_TOP_Z0 + CARM_TOP_H + 1, 0, y, fn=24);   // drop-in M3 x 25 styli: head rests on the bar, tip 3 mm above the groove floor
        for (zz = [128, 135]) {
            cyl_ab(M3_CLEAR, [0, EAR[2] - 7, zz], [0, EAR[2] + 1, zz], fn=24);
            cyl_ab(M3_CB_D, [0, EAR[2] - 7, zz], [0, EAR[2] - 6 + 2.5, zz], fn=24);
        }
    }
}

// ------------------------------------------------------------------ D09-D11 templates (sit on the deck top)
module template(S1, S2, notches) {
    o = TPL_OUTLINE;
    difference() {
        union() {
            linear_extrude(TPL_BASE) offset(r=o[4]) translate([o[0] + o[4], o[2] + o[4]]) square([o[1] - o[0] - 2*o[4], o[3] - o[2] - 2*o[4]]);
            for (p = S1) swept(p, WALL_D, 0, TPL_H);
            for (p = S2) swept(p, WALL_D, 0, TPL_H);
        }
        for (p = S1) swept(p, GROOVE_D, TPL_BASE, TPL_H + 1);
        for (p = S2) swept(p, GROOVE_D, TPL_BASE, TPL_H + 1);
        for (p = TPL_PIN) cyl(M3_CLEAR, -1, TPL_BASE + 1, p[0], p[1], fn=24);
        for (k = [0:notches-1]) box(o[1] - 2, o[1] + 1, 10 - 5*k, 12 - 5*k, -1, TPL_BASE + 1);
    }
}

// ------------------------------------------------------------------ D12 skid ring (hand-rake mode)
module skid_ring() {
    z0 = SKID_Z0;  z1 = SKID_Z0 + SKID_T;
    difference() {
        union() {
            difference() { cyl(62, z0, z1); cyl(47, z0 - 1, z1 + 1); }
            for (a = SCREW_ANG) let(p = polar(SCREW_R, a), q = polar(27, a)) {
                cyl(10, z0, z1, p[0], p[1]);
                hull() { cyl(10, z0, z1, p[0], p[1]); cyl(8, z0, z1, q[0], q[1]); }
            }
            for (a = SCREW_ANG) let(p = polar(SKID_FOOT_R, a), zf = sqrt(FOOT_C_R*FOOT_C_R - SKID_FOOT_R*SKID_FOOT_R)) {
                cyl(6, zf, z1, p[0], p[1], d2=8);
                sph(FOOT_D, [p[0], p[1], zf]);
            }
        }
        for (a = SCREW_ANG) let(p = polar(SCREW_R, a)) { cyl(M3_CLEAR, z0 - 1, z1 + 1, p[0], p[1], fn=24); cyl(M3_CB_D, z0 - 1, z0 + 1.6, p[0], p[1], fn=24); }
        for (a = NAIL_ANG) let(p = polar(NAIL_R, a)) cyl(9, z0 - 1, z1 + 1, p[0], p[1]);
    }
}

// ------------------------------------------------------------------ D13-D15 accessories
module ball_cradle() difference() { cyl(110, 0, 12); cyl(98, -1, 13); cyl(98, 7, 12.01, d2=106); }
module side_mock() {           // tube radius 70 (crosswise) x outer radius 150 (lengthwise); 2.4 mm shell + skirt
    module torus(rt) rotate([0, 90, 0]) rotate_extrude($fn=220) translate([80, 0]) circle(r=rt, $fn=160);
    difference() {
        intersection() { torus(70); box(-62, 62, -62, 62, 108, 160); }
        intersection() { torus(67.6); box(-59.6, 59.6, -59.6, 59.6, 100, 160); }
    }
}
module lift_gauge() difference() {
    union() { box(0, 12, 0, 10, 0, 2); for (i = [0:4]) box(12 + 12*i, 24 + 12*i, 0, 10, 0, 3 + i); }
    for (i = [0:4]) box(14 + 12*i, 14.8 + 12*i, 7, 10.5, 3 + i - 0.4, 3 + i + 1);
}

// ------------------------------------------------------------------ selector
module part(name) {
    if (name == "deck") deck();
    else if (name == "block") block();
    else if (name == "nose_plate") nose_plate();
    else if (name == "plunger") plunger();
    else if (name == "seat_disc") seat_disc();
    else if (name == "nail_N20") nail(2.0, 1);
    else if (name == "nail_N30") nail(3.0, 2);
    else if (name == "nail_N35") nail(3.5, 3);
    else if (name == "c_arm") c_arm();
    else if (name == "template_T1") template(T1_line_star_S1, T1_line_star_S2, 1);
    else if (name == "template_T2") template(T2_dpath_S1, T2_dpath_S2, 2);
    else if (name == "template_T3") template(T3_circle_S1, T3_circle_S2, 3);
    else if (name == "skid_ring") skid_ring();
    else if (name == "ball_cradle") ball_cradle();
    else if (name == "side_mock") side_mock();
    else if (name == "lift_gauge") lift_gauge();
}
// print orientation (the exporter then drops each part onto z = 0)
PRINT_ROT = [["deck", [180, 0, 0]], ["nail_N20", [180, 0, 0]], ["nail_N30", [180, 0, 0]], ["nail_N35", [180, 0, 0]], ["c_arm", [0, 90, 0]], ["skid_ring", [180, 0, 0]]];
function prot(n) = let(m = [for (r = PRINT_ROT) if (r[0] == n) r[1]]) len(m) ? m[0] : [0, 0, 0];

if (PART == "assembly") {
    color("lightgray") sphere(r=R_SCALP, $fn=96);
    color("tan") deck();
    color("steelblue") { block(); nose_plate(); c_arm(); }
    color("orange") for (a = NAIL_ANG) let(p = polar(NAIL_R, a)) translate([p[0], p[1], sqrt(R_SCALP*R_SCALP - NAIL_R*NAIL_R) - 2.0]) nail(2.0, 1);
    color("white") for (a = DOME_ANG) let(p = polar(A_DOME, a)) sph(6, [p[0], p[1], Z_DOME]);
    color("khaki", 0.6) translate([0, 0, DECK_ZTOP]) template(T1_line_star_S1, T1_line_star_S2, 1);
} else if (PRINT) rotate(prot(PART)) part(PART);
else part(PART);
