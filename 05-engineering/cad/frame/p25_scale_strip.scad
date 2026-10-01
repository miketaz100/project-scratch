// =====================================================================
//  p25_scale_strip.scad - P25 float scale strip (slides in the P22 dovetail)
//  PROJECT SCRATCH · 05-engineering/cad/frame · units: mm · frame: local (strip along Z 0..45, ridged face at x = 0
//  looking +X, dovetail tang on -X).  Print face up, 0.12 mm layers.
//  Sources: mechanical.md section 6.4 (45 x 8 x 2, ridges every 1 mm 0.4 wide, long ticks every 5 mm, numerals
//  0/10/20/30, M3 lock slot), 11 P25.  Numerals are INKED after printing (no text() allowed); ridges are 0.3 proud.
// =====================================================================
include <lib_sp1.scad>
L = 45;  W = 8;  FACE_T = 1.2;  TANG_T = 1.0;  TANG_W_OPEN = 4.8;  TANG_W_BOT = 6.3;   // tang matches P22: opening 5.0, bottom 6.5, 1.0 deep
RIDGE_W = 0.4;  RIDGE_H = 0.3;  TICK_SHORT = 2;  TICK_LONG = 5;  LOCK_SLOT = [3.4, 10];
module p25_scale_strip() difference() {
    union() {
        box(-FACE_T, 0, -W / 2, W / 2, 0, L);
        translate([0, 0, 0]) linear_extrude(L) polygon([[-FACE_T + 0.01, -TANG_W_OPEN / 2], [-FACE_T - TANG_T, -TANG_W_BOT / 2], [-FACE_T - TANG_T, TANG_W_BOT / 2], [-FACE_T + 0.01, TANG_W_OPEN / 2]]);
        for (i = [0 : L]) box(-0.01, RIDGE_H, W / 2 - (i % 5 == 0 ? TICK_LONG : TICK_SHORT), W / 2, i - RIDGE_W / 2, i + RIDGE_W / 2);
    }
    hull() { cyl_x(LOCK_SLOT[0] / 2, -FACE_T - TANG_T - 1, 1, 0, 8, fn = 24); cyl_x(LOCK_SLOT[0] / 2, -FACE_T - TANG_T - 1, 1, 0, 8 + LOCK_SLOT[1], fn = 24); }
}
p25_scale_strip();
