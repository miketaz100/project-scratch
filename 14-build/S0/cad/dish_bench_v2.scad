// dish_bench_v2.scad - S0a CORRECTED dish bench (V2), parts D21-D27
// PROJECT SCRATCH, 14-build/S0/cad, 2026-10-02 (Director ruling on CONFLICTS #1).  gen_s0_stl.py mirrors it.
// Same nails, plungers, seat discs and nose plate as the frozen bench (dish_bench.scad D03-D07, D16).
// Differences: balls at R 44; three big concentric pockets (generated, pocket_cavity_v2.scad); deck
// underside a sphere R 155.5 about C; legs at R 66 between the pockets; a single stylus that is also the
// LIFT ROD (M3 x 60 resting on the groove floor, a rubber band from its head to the C-arm's top bar
// pulls the block up into the dish - no centre elastic is possible here); C-arm on +Y, bolted under
// the 90 deg ball-post rib.  D27 is the hand-rake handle (bolts to the V1 block ear).
include <s0_lib.scad>
include <pocket_cavity_v2.scad>
include <template_paths_v2.scad>

PART = "deck_v2";   // deck_v2 | block_v2 | c_arm_v2 | template_v2_T1 | template_v2_T2 | template_v2_T3 | rake_handle | assembly

module deck_v2() {
    top = V2_DECK_ZTOP;
    difference() {
        union() {
            intersection() {
                difference() {
                    union() {
                        cyl(2*V2_FLAT_R, 100, top);
                        translate([0, 0, 100]) cylinder(h=top - 100, r1=V2_FLAT_R + (top - 100), r2=V2_FLAT_R, $fn=128);   // 45 deg cone
                    }
                    sphere(r=V2_UNDER_R, $fn=256);
                }
                cyl(2*V2_DECK_R, 99, top + 1);
            }
            for (a = V2_LEG_ANG) let(p = polar(V2_LEG_R, a), zf = sqrt(FOOT_C_R*FOOT_C_R - V2_LEG_R*V2_LEG_R),
                                     zt = sqrt(V2_UNDER_R*V2_UNDER_R - V2_LEG_R*V2_LEG_R) + 6) {
                cyl(LEG_D_BOT, zf, zt, p[0], p[1], d2=LEG_D_TOP);
                sph(FOOT_D, [p[0], p[1], zf]);
            }
            cyl(V2_GRIP[2], top, top + V2_GRIP[3], V2_GRIP[0], V2_GRIP[1], d2=V2_GRIP[2] - 2);
        }
        for (a = DOME_ANG) rotate([0, 0, a - 90]) translate([0, V2_A_DOME, 0]) pocket_cavity_v2();
        for (p = V2_TPL_PIN) cyl(M3_PILOT, top - 8, top + 1, p[0], p[1], fn=24);
    }
}
// NOTE: the legs are unioned after the pocket cut in gen_s0_stl.py; here they are inside the difference
// but lie outside every pocket cavity, so the result is identical.

module block_v2() difference() {
    union() {
        cyl(BODY_D, NOSE_Z1, BODY_Z1);
        cyl(TOP_D, BODY_Z1, TOP_Z1);
        cyl(BODY_D, BODY_Z1 - 6, BODY_Z1, d2=TOP_D);
        for (a = DOME_ANG) {
            rotate([0, 0, a]) box(V2_RIB[0], V2_RIB[1], -V2_RIB[2]/2, V2_RIB[2]/2, V2_RIB[3], V2_RIB[4]);
            let(p = polar(V2_A_DOME, a)) cyl(POST_D0, V2_RIB[4] - 0.5, V2_POST_TOP, p[0], p[1], d2=POST_D1);
        }
    }
    for (a = DOME_ANG) let(p = polar(V2_A_DOME, a)) sph(BALL_SOCKET_D, [p[0], p[1], V2_Z_DOME], fn=48);
    for (a = NAIL_ANG) let(p = polar(NAIL_R, a)) {
        cyl(BORE_D, NOSE_Z1 - 1, BODY_Z1, p[0], p[1], fn=40);
        cyl(M3_PILOT, BODY_Z1 - 0.5, TOP_Z1 + 1, p[0], p[1], fn=24);
    }
    for (a = SCREW_ANG) let(p = polar(SCREW_R, a)) cyl(M3_PILOT, NOSE_Z1 - 1, NOSE_Z1 + 11, p[0], p[1], fn=24);
    for (yy = [32, 42]) cyl(M3_PILOT, NOSE_Z1 - 1, NOSE_Z1 + 9, 0, yy, fn=24);           // C-arm foot screws (from below)
}

module c_arm_v2() {
    w = CARM_W/2;  lo0 = V2_CARM_LOW[0];  lo1 = V2_CARM_LOW[1];
    difference() {
        union() {
            box(-w - 2, w + 2, V2_FOOT_Y[0], V2_FOOT_Y[1], lo0, NOSE_Z1);
            box(-w, w, V2_FOOT_Y[1] - 1, V2_RISER_Y + 5, lo0, lo1);
            box(-w, w, V2_RISER_Y - 5, V2_RISER_Y + 5, lo0, V2_TOP_Z0 + V2_TOP_H);
            box(-w, w, -8, V2_RISER_Y + 5, V2_TOP_Z0, V2_TOP_Z0 + V2_TOP_H);
            box(-15, 15, -5, 5, V2_TOP_Z0, V2_TOP_Z0 + V2_TOP_H);                          // band cross-piece
            hull() { box(-w, w, V2_RISER_Y - 6, V2_RISER_Y - 5, lo1, lo1 + 10); box(-w, w, V2_RISER_Y - 15, V2_RISER_Y - 5, lo1, lo1 + 1); }
            hull() { box(-w, w, V2_RISER_Y - 6, V2_RISER_Y - 5, V2_TOP_Z0 - 14, V2_TOP_Z0); box(-w, w, V2_RISER_Y - 19, V2_RISER_Y - 5, V2_TOP_Z0 - 1, V2_TOP_Z0); }
            cyl_ab(V2_GRIP_C[0], [0, V2_RISER_Y + 4, V2_GRIP_C[1]], [0, V2_RISER_Y + 5 + V2_GRIP_C[2], V2_GRIP_C[1]], fn=40);
            sph(V2_GRIP_C[0], [0, V2_RISER_Y + 5 + V2_GRIP_C[2], V2_GRIP_C[1]], fn=40);
        }
        cyl(M3_CLEAR, V2_TOP_Z0 - 1, V2_TOP_Z0 + V2_TOP_H + 1, 0, 0, fn=24);              // lift rod M3 x 60
        for (x = [-13, 13]) box(x - 1, x + 1, -6, 6, V2_TOP_Z0 + V2_TOP_H - 3, V2_TOP_Z0 + V2_TOP_H + 1);   // band notches
        for (yy = [32, 42]) { cyl(M3_CLEAR, lo0 - 1, NOSE_Z1 + 1, 0, yy, fn=24); cyl(M3_CB_D, lo0 - 1, NOSE_Z1 - 10.5, 0, yy, fn=24); }
    }
}

module template_v2(S1, notches) {
    o = V2_TPL_OUTLINE;
    difference() {
        union() {
            linear_extrude(TPL_BASE) offset(r=o[4]) translate([o[0] + o[4], o[2] + o[4]]) square([o[1] - o[0] - 2*o[4], o[3] - o[2] - 2*o[4]]);
            for (p = S1) swept(p, WALL_D, 0, TPL_H);
        }
        for (p = S1) swept(p, GROOVE_D, TPL_BASE, TPL_H + 1);
        for (p = V2_TPL_PIN) cyl(M3_CLEAR, -1, TPL_BASE + 1, p[0], p[1], fn=24);
        for (k = [0:notches-1]) box(o[1] - 2, o[1] + 1, 10 - 5*k, 12 - 5*k, -1, TPL_BASE + 1);
        box(o[0] - 1, o[0] + 2, -14, 14, -1, TPL_BASE + 1);                                // "V2" slot on the -X edge
    }
}

module rake_handle() difference() {     // bolts to the V1 block ear with 2 x M3 x 12
    union() {
        box(-7, 7, EAR[2] - 6, EAR[2], 124, 139);
        box(-6, 6, EAR[2] - 110, EAR[2] - 5, 128, 136);
        sph(16, [0, EAR[2] - 112, 132], fn=40);
    }
    for (zz = [128, 135]) { cyl_ab(M3_CLEAR, [0, EAR[2] - 7, zz], [0, EAR[2] + 1, zz], fn=24); cyl_ab(M3_CB_D, [0, EAR[2] - 30, zz], [0, EAR[2] - 6 + 2.5, zz], fn=24); }
}

if (PART == "deck_v2") deck_v2();
else if (PART == "block_v2") block_v2();
else if (PART == "c_arm_v2") c_arm_v2();
else if (PART == "template_v2_T1") template_v2(V2_T1_line_star_S1, 1);
else if (PART == "template_v2_T2") template_v2(V2_T2_dpath_S1, 2);
else if (PART == "template_v2_T3") template_v2(V2_T3_circle_S1, 3);
else if (PART == "rake_handle") rake_handle();
else if (PART == "assembly") {
    color("lightgray") sphere(r=R_SCALP, $fn=96);
    color("tan") deck_v2();
    color("steelblue") { block_v2(); c_arm_v2(); }
    color("khaki", 0.6) translate([0, 0, V2_DECK_ZTOP]) template_v2(V2_T1_line_star_S1, 1);
}
