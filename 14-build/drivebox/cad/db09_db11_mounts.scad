// DB09 chair-back hook plate (bolts to the LID's outside face, M16: 4 x M5 on 200 x 120),
// DB10 J-hook 30 mm throat, DB11 J-hook 55 mm throat - SP1 v3 DRIVE BOX - local frames.
// Hook plate: z = 0 is the lid side, z = 6 faces the chair. Hooks: profile (x = p, y = q),
// extruded 25 mm in z; p = 0 sits on the plate's chair-side face, q = plate y - 20.
// Select with -D 'PART="plate"' | "hook30" | "hook55".
include <lib_drivebox.scad>
PART = "plate";

module db09_hook_plate() {
    difference() {
        linear_extrude(HP_T) crrect(0, 0, HP_X, HP_Y, HP_R);
        for (sx = [-1, 1]) {
            for (sy = [-1, 1]) {
                cyl_z(M5_CLEAR / 2, -0.01, HP_T + 0.01, sx * HP_LID_X, sy * HP_LID_Y, fn = 24);
                cyl_z(HP_CB_D / 2, HP_T - HP_CB_DEPTH, HP_T + 0.01, sx * HP_LID_X, sy * HP_LID_Y, fn = 32);
            }
            translate([0, 0, -0.01]) linear_extrude(HP_T + 0.02) crrect(sx * HP_SLOT_X, 0, HP_SLOT_W, HP_SLOT_L, HP_SLOT_W / 2 - 0.01);
            for (hy = HP_HOOK_Y) {
                cyl_z(M5_CLEAR / 2, -0.01, HP_T + 0.01, sx * HP_HOOK_X, hy, fn = 24);
                hex_z(M5_NUT_AF, -0.01, M5_NUT_T, sx * HP_HOOK_X, hy);
            }
        }
        for (w = HP_WIN) translate([0, 0, -0.01]) linear_extrude(HP_T + 0.02) crrect(w[0], w[1], HP_WIN_X, HP_WIN_Y, 5);
    }
}

module db10_hook(throat) {
    t = HOOK_T;
    difference() {
        linear_extrude(HOOK_WIDTH) union() {
            translate([0, 0]) square([t, HOOK_LEG_Q]);
            translate([0, HOOK_BAR_Q0]) square([2 * t + throat, HOOK_LEG_Q - HOOK_BAR_Q0]);
            translate([t + throat, HOOK_DROP_Q0]) square([t, HOOK_LEG_Q - HOOK_DROP_Q0]);
            polygon([[t - 0.01, HOOK_BAR_Q0 + 0.01], [t - 0.01, HOOK_BAR_Q0 - HOOK_GUSSET], [t + HOOK_GUSSET, HOOK_BAR_Q0 + 0.01]]);
        }
        for (q = HOOK_HOLE_Q) cyl_x(M5_CLEAR / 2, -0.01, t + 0.01, q, HOOK_WIDTH / 2, fn = 24);
    }
}

if (PART == "plate") db09_hook_plate();
else if (PART == "hook30") db10_hook(30);
else if (PART == "hook55") db10_hook(55);
