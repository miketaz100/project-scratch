// =====================================================================
//  p33_palm_lid.scad - P33 palm lid with the lower wrist seat
//  PROJECT SCRATCH · 05-engineering/cad/frame · units: mm · frame: global (section 2)
//  Sources: mechanical.md section 7.1 (lower seat: ring diam 40/30 at Z 69, 45 deg cone diam 18/12 x 3, keeper
//  recess diam 12.2 x 1.5, key peg diam 3 x 2 at r 17 on +X), 7.3 (tether cup diam 12 x 6 at Y +25, eyelet),
//  8.6 (1.6 top, 2 mm lap skirt, 6 x M2 x 6), 11 P33.  Outline = the P32 tray outline + 1.2 skirt.
//  The "2 mm relief above C's paddle" is covered by the 3 mm seat disc (clamp-bar screw heads end at Z 62.5,
//  lid underside at 64.4): not modelled separately.
// =====================================================================
include <lib_sp1.scad>
include <p32_palm_tray.scad>   // tray outline constants: BOX_X, BOX_Y, ARM_N, ARM_P, Z_TOP, LID_INS
RENDER_P32 = false;            // AFTER the include (OpenSCAD: last assignment wins): the tray itself is not rendered here

T = 1.6;  SKIRT_H = 2;  SKIRT_T = 1.2;
SEAT_D = 40;  SEAT_IN_D = 30;  SEAT_Z1 = 69;  LAND_RECESS = 0.3;
CONE_D0 = 18;  CONE_D1 = 12;  CONE_H = 3;  KEEPER_D = 12.2;  KEEPER_H = 1.5;
PEG_D = 3;  PEG_H = 2;  PEG_R = 17;
CUP_D = 12;  CUP_H = 6;  CUP_Y = 25;  EYE_D = 2;  EYE_XY = [8, 25];
HOLE_D = M2_CLEAR;
ZT = Z_TOP + T;                  // lid top at Z 66

module lid_outline(g) {
    translate([-BOX_X - g, -BOX_Y - g]) square([2 * (BOX_X + g), 2 * (BOX_Y + g)]);
    translate([ARM_N[0] - g, ARM_N[2] - g]) square([ARM_N[1] - ARM_N[0] + 2 * g, -BOX_Y + 1 - (ARM_N[2] - g)]);
    translate([ARM_P[0] - g, BOX_Y - 1]) square([ARM_P[1] - ARM_P[0] + 2 * g, ARM_P[2] + g - (BOX_Y - 1)]);
}

module p33_palm_lid() difference() {
    union() {
        translate([0, 0, ZT - T]) linear_extrude(T) lid_outline(SKIRT_T);                                   // top plate
        translate([0, 0, ZT - T - SKIRT_H]) linear_extrude(SKIRT_H + 0.01) difference() { lid_outline(SKIRT_T); lid_outline(0); }   // lap skirt
        cyl_z(SEAT_D / 2, ZT - 0.01, SEAT_Z1);                                                             // seat disc
        cz0 = SEAT_Z1 - LAND_RECESS;
        cyl_z(CONE_D0 / 2 + LAND_RECESS, cz0 - 0.01, cz0 + CONE_H + LAND_RECESS, r2 = CONE_D1 / 2);        // 45 deg cone boss
        cyl_z(PEG_D / 2, SEAT_Z1 - 0.01, SEAT_Z1 + PEG_H - PEG_D / 2, PEG_R, 0, fn = 24);                  // key peg
        sph(PEG_D / 2, [PEG_R, 0, SEAT_Z1 + PEG_H - PEG_D / 2], 24);                                        // hemispherical end
        cyl_z(CUP_D / 2 + 1, ZT - CUP_H, ZT - T + 0.01, 0, CUP_Y, fn = 32);                                 // tether cup wall
    }
    difference() {                                                                                          // land recess inside diam 30
        cyl_z(SEAT_IN_D / 2, SEAT_Z1 - LAND_RECESS, SEAT_Z1 + 1);
        cyl_z(CONE_D0 / 2 + LAND_RECESS + 0.3, SEAT_Z1 - 1, SEAT_Z1 + 2);
    }
    cyl_z(KEEPER_D / 2, SEAT_Z1 - LAND_RECESS + CONE_H + LAND_RECESS - KEEPER_H, SEAT_Z1 - LAND_RECESS + CONE_H + 2, fn = 32);   // keeper recess
    cyl_z(CUP_D / 2, ZT - CUP_H + 1, ZT + 1, 0, CUP_Y, fn = 32);                                            // tether cup
    cyl_z(EYE_D / 2, ZT - 10, ZT + 1, EYE_XY[0], EYE_XY[1], fn = 16);                                       // tether eyelet
    for (h = LID_INS) cyl_z(HOLE_D / 2, ZT - 10, ZT + 1, h[0], h[1], fn = 16);                              // 6 x diam 2.4
}

p33_palm_lid();
