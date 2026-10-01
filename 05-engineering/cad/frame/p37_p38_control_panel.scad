// =====================================================================
//  p37_p38_control_panel.scad - P37 control panel box and P38 control panel lid (base)
//  PROJECT SCRATCH · 05-engineering/cad/frame · units: mm · frame: local (box face up, z 0 = open base plane)
//  Sources: mechanical.md section 3.3 (SPEED / VARIATION pots, PERIODIC/HUMAN toggle, status LED, 6-core cable),
//  11 P37 (100 x 60 x 40, 2 x diam 7.2 pot holes with anti-rotation slots, diam 6.2 toggle, diam 5.2 LED, 0/50/100 %
//  tick recesses, gland diam 6, 4 corner M3 inserts), P38 (100 x 60 x 2, 4 x diam 3.4, 4 x diam 10 foot recesses).
//  PART = "box" | "lid" | "both".  Print the box face down, the lid flat.
// =====================================================================
include <lib_sp1.scad>
PART = "both";
BX = 100;  BY = 60;  BZ = 40;  WALL = 2;  R = 4;
POT_D = 7.2;  POT_X = [-30, 0];  POT_Y = 8;  POT_KEY = [1.2, 1.5];
TOGGLE_D = 6.2;  TOGGLE_XY = [30, 8];  LED_D = 5.2;  LED_XY = [30, -14];  TICK_R = 9;  TICK = [1.0, 2.0, 0.5];
GLAND_D = 6;  GLAND_Z = 20;  GLAND_Y = 0;
CORNER_INS = [[-45, -25], [45, -25], [-45, 25], [45, 25]];  CORNER_BOSS_D = 7;
module p37_control_panel_box() difference() {
    union() {
        difference() { rbox_z(-BX / 2, BX / 2, -BY / 2, BY / 2, 0, BZ, R); rbox_z(-BX / 2 + WALL, BX / 2 - WALL, -BY / 2 + WALL, BY / 2 - WALL, -1, BZ - WALL, R - WALL); }
        for (h = CORNER_INS) cyl_z(CORNER_BOSS_D / 2, 0, BZ - WALL + 0.01, h[0], h[1], fn = 24);
    }
    for (x = POT_X) {
        cyl_z(POT_D / 2, BZ - WALL - 1, BZ + 1, x, POT_Y, fn = 24);
        cbox(x + POT_D / 2 + POT_KEY[1] / 2 - 0.3, POT_Y, BZ, POT_KEY[1] + 0.6, POT_KEY[0], 2 * WALL + 2);         // anti-rotation slot
        for (i = [0 : 2]) { a = 225 - 135 * i;                                                                      // 0 / 50 / 100 % ticks
            rot_about([0, 0, 1], a, [x + TICK_R * cos(a), POT_Y + TICK_R * sin(a), BZ]) cbox(x + TICK_R * cos(a), POT_Y + TICK_R * sin(a), BZ, TICK[1], TICK[0], 2 * TICK[2]); }
    }
    cyl_z(TOGGLE_D / 2, BZ - WALL - 1, BZ + 1, TOGGLE_XY[0], TOGGLE_XY[1], fn = 24);
    cyl_z(LED_D / 2, BZ - WALL - 1, BZ + 1, LED_XY[0], LED_XY[1], fn = 24);
    cyl_x(GLAND_D / 2, -BX / 2 - 1, -BX / 2 + WALL + 1, GLAND_Y, GLAND_Z, fn = 24);                                  // cable gland (-X wall)
    for (h = CORNER_INS) ins_z(M3_INS_D, M3_INS_L + 2, h[0], h[1], 0, false);
}
LT = 2;  FOOT_D = 10;  FOOT_H = 1;  FOOT_XY = [[-38, -18], [38, -18], [-38, 18], [38, 18]];
module p38_control_panel_lid() difference() {
    rbox_z(-BX / 2, BX / 2, -BY / 2, BY / 2, 0, LT, R);
    for (h = CORNER_INS) cyl_z(M3_CLEAR / 2, -1, LT + 1, h[0], h[1], fn = 24);
    for (h = FOOT_XY) cyl_z(FOOT_D / 2, -1, FOOT_H, h[0], h[1], fn = 32);
}
if (PART == "box" || PART == "both") p37_control_panel_box();
if (PART == "lid" || PART == "both") translate([0, 0, PART == "both" ? -10 : 0]) p38_control_panel_lid();
