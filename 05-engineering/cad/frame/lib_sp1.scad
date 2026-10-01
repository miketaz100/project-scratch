// =====================================================================
//  lib_sp1.scad - shared library for the SP1 module frame, float and hand parts
//  PROJECT SCRATCH · 05-engineering/cad/frame · CAD agent · 2026-10-01 · units: mm
// ---------------------------------------------------------------------
//  FRAME (mechanical.md section 2, DESIGN-FREEZE-ADDENDUM-1 D9): Z up, X = stroke,
//  Y = across the stroke; origin O = centre nail edge at mid-stroke, arm at 0 deg,
//  float on its down-stop, module latched.  Parts on the module are modelled IN
//  THEIR INSTALLED POSITION (see README.md for print orientation).
//  Only basic primitives are used (cube, cylinder, sphere, hull, linear_extrude of
//  polygons, rotate_extrude, offset, rotate/translate/mirror, booleans): no text(),
//  no import(), no surface().  Numbers marked [VERIFY] are vendor dimensions that
//  mechanical.md also marks [VERIFY].
//  gen_frame_stl.py mirrors every constant and module below under the same name.
// =====================================================================
FN = 48;                               // circle segments

// ---- fasteners and inserts (mechanical.md section 11 header) ----
M2_CLEAR = 2.4;  M3_CLEAR = 3.4;  M4_CLEAR = 4.5;  M5_CLEAR = 5.5;
M2_PILOT = 1.8;  M3_PILOT = 2.6;                      // thread-forming pilots in PETG
M2_INS_D = 3.2;  M2_INS_L = 3.0;                      // brass heat-set M2: 3.2 hole, 3 long
M3_INS_D = 4.0;  M3_INS_L = 4.0;                      // brass heat-set M3: 4.0 hole, 4 long
M4_INS_D = 5.6;  M4_INS_L = 6.0;                      // brass heat-set M4 x 6 [VERIFY hole on the insert kit]
M3_HEAD_D = 6.0; M3_HEAD_H = 3.2;                     // socket head M3 (counterbores)
M5_HEAD_D = 9.5; M5_HEAD_H = 5.0;
M4_NUT_AF = 7.2; M4_NUT_H = 3.4;                      // M4 nut trap (7.0 AF + 0.2)
PIN_BORE = 6.3;                                       // M6 hinge pin, reamed (section 4.1)
EXT = 20.0;  EXT_SOCK = 20.2;                         // 2020 extrusion and its printed socket

// ---- global geometry (mechanical.md section 2) ----
AXIS_X = 0;    AXIS_Z = 84;                           // elbow axis, parallel to Y
PIN_X = -60;   PIN_Z = 84;                            // fail-safe hinge pin, parallel to Y
SCALP_C = [0, 0, -86];  SCALP_R = 90;
KP_C_Z = -52.5;                                       // knuckle-plate sphere centre (underside R 90 at Z 37.5, section 8.7)
KP_R = 90;  KP_T = 1.6;  BOOT_T = 0.25;  P31_T = 1.2;
TRAY_BOT_R = KP_R + KP_T + BOOT_T + P31_T;            // 93.05: palm-tray underside (sits on P31 over the boot)

// ---- bought-part reference solids [x0, x1, y0, y1, z0, z1] ----
POST  = [-70, -50, -10, 10, 94, 198];                 // 2020 post, 104 mm (ADDENDUM-1 D8)
SPINE = [-50, 30, -10, 10, 196, 216];                 // 2020 spine, 80 mm
BEAM  = [-35, -15, -135, 135, 164, 184];              // 2020 elbow-carrier beam, 270 mm
YAW_X = -25;                                          // yaw axis (section 5.4)
XL330_BODY = [20, 23, 34];                            // X x Y(depth) x Z (long axis vertical); ROBOTIS X330 drawing, confirmed (bom-verified.md 11)
XL330_AXIS_FROM_END = 9.5;                            // output axis 9.5 mm from the lower body end (bom-verified.md 11 item 2)
SERVO = [-10, 10, -127, -104, 74.5, 108.5];           // XL330 body in place (section 5.3)
HORN_R = 8;  HORN_Y = [-104, -101];                   // XL330 horn diam 16 x 3 (bom-verified.md 11 item 3)
XL330_FRAME_HOLES = [[-8, -15], [8, -15], [-8, 15], [8, 15]];   // 4 x diam 1.6 on 16 x 30 (X, dZ from the body centre): back face 4.5 deep, horn face 3.5 deep
XL330_CONN = [13, 24];                                // JST connectors on both 23 x 34 side faces, 13..24 mm behind the horn face
MGN9_RAIL = [9, 6.5, 100, 20, 10];                    // W, H, L, hole pitch, end distance [VERIFY]
MGN9C_HOLE_X = 15;  MGN9C_HOLE_Y = 10;                // block pattern (15 along the rail, 10 across) [VERIFY]
RAIL = [33.5, 40, -4.5, 4.5, 68, 168];                // MGN9 rail on the mast's -X face
CARR = [30, 40, -10, 10, 74, 103];                    // MGN9C block at the down-stop
MAG_X0 = -81;  MAG_X1 = -66;  MAG_Z = 34;  MAG_R = 10; // Adafruit 3872 P20/15 (section 4.4)
FLOAT_TRAVEL = 28;

// ---- paddle section at the knuckle plate (tip lead paddle_with_pocket.scad, z = 25) ----
PAD_SEC_X = 22.82;  PAD_SEC_Y = 17.82;
NAIL_L = [-8, -24];  NAIL_C = [0, 0];  NAIL_R = [8, 24];        // section 8.1 nail edges (X, Y)
POCKET_MOUTH_Z_L = 8.9;  POCKET_MOUTH_Z_C = 12.5;  POCKET_MOUTH_Z_R = 8.9;   // section 2 row 20
// shared knuckle-plate slot (section 8.7): union of three R 4 rounded rectangles
SLOT_OUTER = [31.8, 26.8];  SLOT_CENTRE = [34.8, 29.8];  SLOT_R = 4;  SLOT_LEAD_IN = 15;

// ============================ primitives ============================
module box(x0, x1, y0, y1, z0, z1) translate([x0, y0, z0]) cube([x1 - x0, y1 - y0, z1 - z0]);
module cbox(cx, cy, cz, sx, sy, sz) translate([cx, cy, cz]) cube([sx, sy, sz], center = true);
module cyl_z(r, z0, z1, x = 0, y = 0, r2 = -1, fn = FN)
    translate([x, y, z0]) cylinder(r1 = r, r2 = (r2 < 0 ? r : r2), h = z1 - z0, $fn = fn);
// cylinder along +Y from y0 to y1 at (x, z); r2 is the radius at y1
module cyl_y(r, y0, y1, x = 0, z = 0, fn = FN, r2 = -1)
    translate([x, y0, z]) rotate([-90, 0, 0]) cylinder(r1 = r, r2 = (r2 < 0 ? r : r2), h = y1 - y0, $fn = fn);
// cylinder along +X from x0 to x1 at (y, z); r2 is the radius at x1
module cyl_x(r, x0, x1, y = 0, z = 0, fn = FN, r2 = -1)
    translate([x0, y, z]) rotate([0, 90, 0]) cylinder(r1 = r, r2 = (r2 < 0 ? r : r2), h = x1 - x0, $fn = fn);
module sph(r, c, fn = FN) translate(c) sphere(r, $fn = fn);

// 2D rounded rectangle centred at (cx, cy)
module rrect(cx, cy, sx, sy, r) translate([cx, cy]) offset(r = r, $fn = FN) offset(delta = -r) square([sx, sy], center = true);
// box with vertical edges rounded r
module rbox_z(x0, x1, y0, y1, z0, z1, r) translate([0, 0, z0]) linear_extrude(z1 - z0) rrect((x0 + x1) / 2, (y0 + y1) / 2, x1 - x0, y1 - y0, r);
// thin slab (hull target)
module slab_z(cx, cy, sx, sy, r, z, h = 0.02) translate([0, 0, z - h / 2]) linear_extrude(h) rrect(cx, cy, sx, sy, r);
// drafted box: hull of two rounded-rect slabs
module rrect_frustum(cx, cy, sx0, sy0, sx1, sy1, r, z0, z1) hull() { slab_z(cx, cy, sx0, sy0, r, z0 + 0.01); slab_z(cx, cy, sx1, sy1, r, z1 - 0.01); }
// 15-degree draft helper: box whose bottom is smaller by 2 h tan(draft) (bigger at the top, as a guard shell wants)
module drafted_box(cx, cy, sx, sy, r, z0, z1, draft = 15) {
    d = 2 * (z1 - z0) * tan(draft);
    rrect_frustum(cx, cy, sx - d, sy - d, sx, sy, r, z0, z1);
}
// extrude a 2D profile given in (x, z) along +Y from y0 to y1
module ext_y(y0, y1) translate([0, y1, 0]) rotate([90, 0, 0]) linear_extrude(y1 - y0) children();
// extrude a 2D profile given in (y, z) along +X from x0 to x1
module ext_x(x0, x1) translate([x0, 0, 0]) rotate([90, 0, 90]) linear_extrude(x1 - x0) children();
// rotate children by `ang` (deg) about `axis` through `pt`
module rot_about(axis, ang, pt) translate(pt) rotate(a = ang, v = axis) translate(-pt) children();
module mirror_y() mirror([0, 1, 0]) children();

// ============================ holes ============================
// blind insert / pilot hole from face z = ztop going down (or up)
module ins_z(d, depth, x, y, ztop, down = true) {
    if (down) cyl_z(d / 2, ztop - depth, ztop + 0.01, x, y, fn = 24);
    else      cyl_z(d / 2, ztop - 0.01, ztop + depth, x, y, fn = 24);
}
module ins_y(d, depth, x, z, yface, toward = 1) {
    if (toward > 0) cyl_y(d / 2, yface - 0.01, yface + depth, x, z, fn = 24);
    else            cyl_y(d / 2, yface - depth, yface + 0.01, x, z, fn = 24);
}
module ins_x(d, depth, y, z, xface, toward = 1) {
    if (toward > 0) cyl_x(d / 2, xface - 0.01, xface + depth, y, z, fn = 24);
    else            cyl_x(d / 2, xface - depth, xface + 0.01, y, z, fn = 24);
}
// countersunk through hole (90 deg) from the face z = ztop
module csk_z(d_hole, d_head, x, y, ztop, down = true, thru = 30) {
    h = (d_head - d_hole) / 2;
    if (down) { cyl_z(d_hole / 2, ztop - thru, ztop + 1, x, y, fn = 24); cyl_z(d_hole / 2, ztop - h, ztop + 0.01, x, y, r2 = d_head / 2, fn = 24); }
    else      { cyl_z(d_hole / 2, ztop - 1, ztop + thru, x, y, fn = 24); cyl_z(d_head / 2, ztop - 0.01, ztop + h, x, y, r2 = d_hole / 2, fn = 24); }
}
// spherical shell about (0, 0, rc_z)
module sph_shell(rc_z, r_in, r_out, fn = 160) difference() { sph(r_out, [0, 0, rc_z], fn); sph(r_in, [0, 0, rc_z], fn); }

// ============================ shared features ============================
// 2020 socket (pocket) along Z / along Y
module socket_2020_z(cx, cy, z0, z1) { s = EXT_SOCK / 2; box(cx - s, cx + s, cy - s, cy + s, z0, z1); }
module socket_2020_y(cx, cz, y0, y1) { s = EXT_SOCK / 2; box(cx - s, cx + s, y0, y1, cz - s, cz + s); }
// MGN9C 15 x 10 pattern [VERIFY]: holes along X through a plate on the block face at X = xface, centred (yc, zc)
module mgn9c_holes_x(xface, yc, zc, d = M3_CLEAR, depth = 30)
    for (dz = [-MGN9C_HOLE_X / 2, MGN9C_HOLE_X / 2]) for (dy = [-MGN9C_HOLE_Y / 2, MGN9C_HOLE_Y / 2])
        cyl_x(d / 2, xface - depth, xface + depth, yc + dy, zc + dz, fn = 24);
// XL330 body pocket 20.4 x 34.4 x 23.5 [VERIFY]: X across, Z = long body axis, open toward +Y by open_len
module xl330_pocket(x0, y_floor, z0, open_len = 40) {
    px = XL330_BODY[0] + 0.4; pz = XL330_BODY[2] + 0.4; pd = XL330_BODY[1] + 0.5;
    box(x0 - px / 2, x0 + px / 2, y_floor, y_floor + pd + open_len, z0, z0 + pz);
}
// shared knuckle-plate slot outline (2D), grown by `grow` on every side
module slot_cs(grow = 0) {
    rrect(NAIL_L[0], NAIL_L[1], SLOT_OUTER[0] + 2 * grow, SLOT_OUTER[1] + 2 * grow, SLOT_R + grow);
    rrect(NAIL_C[0], NAIL_C[1], SLOT_CENTRE[0] + 2 * grow, SLOT_CENTRE[1] + 2 * grow, SLOT_R + grow);
    rrect(NAIL_R[0], NAIL_R[1], SLOT_OUTER[0] + 2 * grow, SLOT_OUTER[1] + 2 * grow, SLOT_R + grow);
}
// slot cutter z0..z1; with lead_in_z > z0 the underside is widened by tan(15 deg) x (lead_in_z - z0) (section 8.7 lead-in)
module slot_cutter(z0, z1, lead_in_z = -1000) {
    translate([0, 0, z0]) linear_extrude(z1 - z0) slot_cs();
    if (lead_in_z > z0) {
        g = (lead_in_z - z0) * tan(SLOT_LEAD_IN);
        hull() {
            translate([0, 0, z0]) linear_extrude(0.01) slot_cs(g);
            translate([0, 0, lead_in_z]) linear_extrude(0.01) slot_cs(0);
        }
    }
}
// the 2020 post passes through both yaw plates (section 2): notch for it
module post_notch(z0, z1) { s = EXT_SOCK / 2; box(POST[0] - 1, POST[1] + 0.1, -s, s, z0 - 1, z1 + 1); }
// bought-part reference solids (for assembly previews only; not printed)
module ref_post() box(POST[0], POST[1], POST[2], POST[3], POST[4], POST[5]);
module ref_spine() box(SPINE[0], SPINE[1], SPINE[2], SPINE[3], SPINE[4], SPINE[5]);
module ref_beam() box(BEAM[0], BEAM[1], BEAM[2], BEAM[3], BEAM[4], BEAM[5]);
module ref_servo() { box(SERVO[0], SERVO[1], SERVO[2], SERVO[3], SERVO[4], SERVO[5]); cyl_y(HORN_R, HORN_Y[0], HORN_Y[1], AXIS_X, AXIS_Z); }
module ref_rail() box(RAIL[0], RAIL[1], RAIL[2], RAIL[3], RAIL[4], RAIL[5]);
module ref_carriage() difference() { box(CARR[0], CARR[1], CARR[2], CARR[3], CARR[4], CARR[5]); ref_rail(); }
module ref_magnet() cyl_x(MAG_R, MAG_X0, MAG_X1, 0, MAG_Z);
