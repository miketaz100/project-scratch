// DB02 drum deck, DB03 floating housing-stop plate (+ DB03b 4 mm-housing variant),
// DB04 Hall bridge, DB05 housing comb (+ DB05b) - SP1 v3 DRIVE BOX - frame D (comb: local).
// Select with -D 'PART="deck"' | "plate" | "plate4" | "bridge" | "comb" | "comb4".
include <lib_drivebox.scad>
PART = "deck";

module db02_deck() {
    difference() {
        union() {
            box(0, DECK_X1, 0, DECK_Y1, -DECK_T, 0);
            for (L = LEGS) box(L[0], L[1], L[2], L[3], DECK_LEG_Z, -DECK_T + 0.01);
            for (P = [POST_REAR, POST_FRONT]) for (yr = ROD_Y) box(P[0], P[1], yr - 5, yr + 5, -0.01, POST_TOP);
        }
        for (L = LEGS) cyl_z(M4_CLEAR / 2, DECK_LEG_Z - 0.01, 0.01, (L[0] + L[1]) / 2, (L[2] + L[3]) / 2, fn = 24);
        for (my = MOTOR_Y) {
            cyl_z(MOTOR_BOSS_D / 2, -DECK_T - 0.01, 0.01, MOTOR_X, my);
            for (dx = [-MOTOR_HOLE, MOTOR_HOLE]) for (dy = [-MOTOR_HOLE, MOTOR_HOLE])
                cyl_z(M3_CLEAR / 2, -DECK_T - 0.01, 0.01, MOTOR_X + dx, my + dy, fn = 24);
            sx = MOTOR_X - INDEX_R;
            box(sx - 1.7, sx + 1.7, my - 2.2, my + 2.2, -1.7, 0.01);       // index Hall pocket (TO-92 face up)
            box(-0.01, sx - 1.69, my - 1.6, my + 1.6, -1.7, 0.01);         // lead channel to the deck edge
        }
        for (P = [POST_REAR, POST_FRONT]) for (yr = ROD_Y) cyl_x(ROD_HOLE_D / 2, P[0] - 0.01, P[1] + 0.01, yr, ROD_Z, fn = 24);
        for (h = SHELF_HOLES) cyl_z(M3_CLEAR / 2, -DECK_T - 0.01, 0.01, h[0], h[1], fn = 24);
        for (tx = [94, 100, 106]) box(tx - 0.4, tx + 0.4, 118, 126, -0.6, 0.01);   // ticks W-6 / W / W+6
    }
}

module db03_plate(S) {     // S = [boss R, boss x1, bore D, floor, cable D]
    tx0 = FP_X1 - T_T;     // tongue back face, x 105.5
    difference() {
        union() {
            box(FP_X0, FP_X1, 0, DECK_Y1, FP_Z0, FP_Z1);
            for (yr = ROD_Y) cyl_x(FP_BOSS_R, FP_X0, FP_BOSS_X1, yr, ROD_Z);
            for (yc = CABLE_Y) for (zr = ROW_Z) {
                cyl_x(S[0], FP_X1 - 0.01, S[1], yc, zr);                       // housing seat boss on the tongue tip
                cyl_x(MAG_BOSS_R, MAG_BOSS_X0, tx0 + 0.01, yc + MAG_DY, zr);    // magnet boss behind the tongue
            }
        }
        for (yr = ROD_Y) cyl_x(LM4UU_D / 2, FP_X0 - 0.01, FP_BOSS_X1 + 0.01, yr, ROD_Z);
        for (yc = CABLE_Y) {
            y0 = yc - T_ROOT; y1 = yc + T_TIP + T_SLOT;
            box(FP_X0 - 0.01, tx0, y0, y1, T_POCKET_Z0, T_POCKET_Z1);                   // pocket behind both tongues
            for (zz = [[ROW_Z[0] - 4, ROW_Z[0] - 3], [ROW_Z[0] + 3, ROW_Z[1] - 3], [ROW_Z[1] + 3, ROW_Z[1] + 4]])
                box(tx0 - 0.01, FP_X1 + 0.01, y0, y1, zz[0], zz[1]);                    // side slots
            box(tx0 - 0.01, FP_X1 + 0.01, yc + T_TIP, y1, T_POCKET_Z0, T_POCKET_Z1);   // end slot
            for (zr = ROW_Z) {
                cyl_x(S[2] / 2, FP_X1 + S[3], S[1] + 0.01, yc, zr);                     // ferrule bore
                cyl_x(S[4] / 2, FP_X0 - 0.01, S[1] + 0.01, yc, zr, fn = 24);            // cable hole
                cyl_x(MAG_POCKET_D / 2, MAG_BOSS_X0 - 0.01, MAG_BOSS_X0 + MAG_POCKET_DEPTH, yc + MAG_DY, zr, fn = 24);
                box(tx0 - 0.01, S[1] + 0.01, yc - REL_SLOT / 2, yc + REL_SLOT / 2, zr, zr + S[0] + 0.01);   // cable release slot
            }
        }
        for (s = BRIDGE_SCREWS) cyl_x(M3_INS_D / 2, FP_X0 - 0.01, FP_X0 + M3_INS_L, s[0], s[1], fn = 24);
    }
}

module db04_bridge() {
    difference() {
        box(BR_X0, BR_X1, BR_Y0, BR_Y1, BR_Z0, BR_Z1);
        for (s = BRIDGE_SCREWS) cyl_x(M3_CLEAR / 2, BR_X0 - 0.01, BR_X1 + 0.01, s[0], s[1], fn = 24);
        for (yc = CABLE_Y) for (i = [0, 1]) {
            ys = yc + MAG_DY; zr = ROW_Z[i];
            box(BR_X1 - BR_SENS_T, BR_X1 + 0.01, ys - BR_SENS_W / 2, ys + BR_SENS_W / 2, zr - BR_SENS_H / 2, zr + BR_SENS_H / 2);
            if (i == 0) box(BR_X1 - BR_SENS_T, BR_X1 + 0.01, ys - BR_LEAD_W / 2, ys + BR_LEAD_W / 2, BR_Z0 - 0.01, zr - BR_SENS_H / 2 + 0.01);
            else        box(BR_X1 - BR_SENS_T, BR_X1 + 0.01, ys - BR_LEAD_W / 2, ys + BR_LEAD_W / 2, zr + BR_SENS_H / 2 - 0.01, BR_Z1 + 0.01);
            cyl_x(BR_CABLE_D / 2, BR_X0 - 0.01, BR_X1 + 0.01, yc, zr, fn = 24);
        }
        for (yc = CABLE_Y) box(BR_X0 - 0.01, BR_X1 + 0.01, yc - REL_SLOT / 2, yc + REL_SLOT / 2, ROW_Z[0], BR_Z1 + 0.01);   // cable release slots
    }
}

module db05_comb(hod) {
    r = hod / 2 + 0.15;
    difference() {
        union() { box(0, 10, 0, 110, 0, 8); box(0, 10, 70, 90, 7.99, 22); }
        cyl_x(4.0, -0.01, 10.01, 80, 16);
        for (gy = [9, 55, 101]) { cyl_x(r, -0.01, 10.01, gy, 4.0, fn = 24); box(-0.01, 10.01, gy - r, gy + r, 4.0, 8.01); }
    }
}

if (PART == "deck") db02_deck();
else if (PART == "plate") db03_plate(SEAT);
else if (PART == "plate4") db03_plate(SEAT_4MM);
else if (PART == "bridge") db04_bridge();
else if (PART == "comb") db05_comb(HOUS_OD);
else if (PART == "comb4") db05_comb(4.3);
