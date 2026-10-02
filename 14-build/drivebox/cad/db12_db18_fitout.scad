// Case fit-out: DB12 pegboard valve rack, DB13 pump saddle (D 28), DB14 bottle saddle (D 51),
// DB15 hanger clip seat, DB16a/b 3 N clip halves, DB17 vent baffle, DB18 panel bracket.
// SP1 v3 DRIVE BOX - local frames. Select with -D 'PART="peg"' | "saddle28" | "saddle51" |
// "seat" | "clipnose" | "clipplain" | "baffle" | "bracket".
include <lib_drivebox.scad>
PART = "peg";

module db12_pegboard() {
    hx = PEG_X / 2;
    nx = round((PEG_X - 20) / PEG_PITCH);
    difference() {
        union() {
            box(-hx, hx, 0, PEG_Y, 0, PEG_T);
            box(-hx, hx, 0, PEG_FL_T, 0, PEG_FL_Z);
            for (gx = [-hx + 1.5, hx - 1.5])
                ext_x(gx - 1.5, gx + 1.5) polygon([[PEG_FL_T - 0.01, PEG_T - 0.01], [20, PEG_T - 0.01], [PEG_FL_T - 0.01, 20]]);
        }
        for (i = [0 : nx]) for (j = [0 : 7]) cyl_z(PEG_HOLE_D / 2, -0.01, PEG_T + 0.01, -hx + 10 + i * PEG_PITCH, 15 + j * PEG_PITCH, fn = 16);
        for (fx = PEG_FL_HOLES) cyl_y(M4_CLEAR / 2, -0.01, PEG_FL_T + 0.01, fx, 12, fn = 24);
    }
}

module db13_saddle(dia) {
    w = dia + 8; h = 4 + 0.35 * dia; L = SADDLE_L;
    difference() {
        union() { box(-w / 2, w / 2, 0, L, 0, h); box(-8, 8, -9, L + 9, 0, 4); }
        cyl_y(dia / 2 + 0.5, -0.01, L + 0.01, 0, 4 + dia / 2, fn = 96);
        box(-w / 2 - 0.01, w / 2 + 0.01, L / 2 - 2.5, L / 2 + 2.5, 1, 3);       // zip-tie tunnel
        cyl_z(M4_CLEAR / 2, -0.01, 4.01, 0, -4.5, fn = 24);
        cyl_z(M4_CLEAR / 2, -0.01, 4.01, 0, L + 4.5, fn = 24);
    }
}

module db15_seat() {
    difference() {
        cyl_z(S15_R, 0, S15_H, fn = 64);
        hex_z(NUT_1420_AF, -0.01, NUT_1420_T);
        cyl_z(S15_BOLT_R, -0.01, S15_BOLT_Z, fn = 32);
        cyl_z(S15_MAG_R, S15_MAG_Z0, S15_CONE_Z0 + 0.01, fn = 32);
        cyl_z(S15_CONE_R0, S15_CONE_Z0, S15_H + 0.01, r2 = S15_CONE_R1 + 0.01 * (S15_CONE_R1 - S15_CONE_R0) / 3, fn = 64);
    }
}

module db16_clip(nose) {
    difference() {
        union() {
            box(-CL_X, CL_X, -CL_Y, CL_Y, 0, CL_H);
            if (nose) cyl_z(CL_NOSE_R1, -CL_NOSE_H, 0.01, r2 = CL_NOSE_R0, fn = 64);
        }
        cyl_x(CL_CH_R, -CL_X - 0.01, CL_X + 0.01, 0, CL_H, fn = 64);
        for (sx = [-1, 1]) for (sy = [-1, 1]) {
            cyl_z(M3_CLEAR / 2, -0.01, CL_H + 0.01, sx * CL_HOLE_X, sy * CL_HOLE_Y, fn = 24);
            if (!nose) hex_z(M3_NUT_AF, -0.01, M3_NUT_T, sx * CL_HOLE_X, sy * CL_HOLE_Y);
        }
        if (nose) cyl_z(CL_WASHER_R, -CL_NOSE_H - 0.01, -CL_NOSE_H + CL_WASHER_DEPTH, fn = 64);
    }
}

module db17_vent_baffle() {
    difference() {
        union() { box(-25, 25, -25, 25, 0, 18); box(-31, 31, -4, 4, 0, 3); }
        box(-23, 23, -23, 23, -0.01, 16);
        box(-15, 15, 22.99, 25.01, 4, 12);
        cyl_z(M3_CLEAR / 2, -0.01, 3.01, -28, 0, fn = 24);
        cyl_z(M3_CLEAR / 2, -0.01, 3.01, 28, 0, fn = 24);
    }
}

module db18_bracket() {
    difference() {
        union() {
            box(0, 30, 0, 20, 0, 4);
            box(0, 4, 0, 20, 0, 30);
            for (yy = [[0, 3], [17, 20]]) ext_y(yy[0], yy[1]) polygon([[3.99, 3.99], [20, 3.99], [3.99, 20]]);
        }
        cyl_z(M4_CLEAR / 2, -0.01, 4.01, 18, 10, fn = 24);
        cyl_x(M4_CLEAR / 2, -0.01, 4.01, 10, 18, fn = 24);
    }
}

if (PART == "peg") db12_pegboard();
else if (PART == "saddle28") db13_saddle(28);
else if (PART == "saddle51") db13_saddle(51);
else if (PART == "seat") db15_seat();
else if (PART == "clipnose") db16_clip(true);
else if (PART == "clipplain") db16_clip(false);
else if (PART == "baffle") db17_vent_baffle();
else if (PART == "bracket") db18_bracket();
