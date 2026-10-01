// =====================================================================
//  p03_p04_electronics_tray.scad - P3 electronics tray and P4 tray lid (on the VESA adapter's front face)
//  PROJECT SCRATCH · 05-engineering/cad/frame · units: mm · frame: global (section 2)
//  Sources: mechanical.md section 3.3 (tray seat Y +15..50, Z 120..165, 4 x M3), 11 P3 (32 x 36 x 92; OpenRB-150
//  pocket ~66 x 25 [VERIFY] on 4 diam 2.5 bosses, Wago 221-413 and 30 x 20 perfboard, USB-C 12 x 7, cable slots 8 x 4),
//  11 P4 (2 x 36 x 92, vent slots 2 x 20, 2 x diam 3.4, label recess).  PART = "tray" | "lid" | "both".
//  Tray X -120..-88 (open toward +X), Y 17..53, Z 100..192; the lid carries a Wago cradle inside (C-E1).
//  CONFLICT C-E2: the frame yaw plates sweep through this tray during the 25 deg fail-safe lift.
// =====================================================================
include <lib_sp1.scad>
PART = "both";
X0 = -120;  X1 = -88;  Y0 = 17;  Y1 = 53;  Z0 = 100;  Z1 = 192;  WALL = 2;  BACK = 2.5;  YC = (Y0 + Y1) / 2;
BRD_Z0 = 109;  BRD_HOLES = [[-4.5, 3.5], [-4.5, 62.5], [16.5, 3.5], [16.5, 62.5]];   // OpenRB-150 [VERIFY], (dY, dZ) from (YC - 6, BRD_Z0)
BOSS_D = 5;  BOSS_H = 5;  BOSS_HOLE = 2.5;
USB = [12, 7];  USB_X = -107.5;  SLOT = [8, 4];  LID_BOSS_D = 8;  LID_INS = [[22, 104], [48, 188]];
CARD_SLOT_X = -97.5;  CARD_SLOT_W = 1.9;  CARD_Z0 = 152;  CARD_Z1 = 180;
MOUNT_HOLES = [[21, 105.5], [49, 105.5], [21, 160], [49, 160]];                        // = P1 TRAY_HOLES

module p03_electronics_tray() difference() {
    union() {
        difference() { box(X0, X1, Y0, Y1, Z0, Z1); box(X0 + BACK, X1 + 1, Y0 + WALL, Y1 - WALL, Z0 + WALL, Z1 - WALL); }
        for (h = BRD_HOLES) cyl_x(BOSS_D / 2, X0 + BACK - 0.01, X0 + BACK + BOSS_H, YC + h[0] - 6, BRD_Z0 + h[1], fn = 24);   // board standoffs
        for (h = LID_INS) cyl_x(LID_BOSS_D / 2, X0 + BACK - 0.01, X1, h[0], h[1], fn = 32);                               // lid-screw bosses
        for (yw = [Y0 + WALL, Y1 - WALL]) for (dx = [-CARD_SLOT_W / 2 - 1.2, CARD_SLOT_W / 2])                          // perfboard card guides
            box(CARD_SLOT_X + dx, CARD_SLOT_X + dx + 1.2, min(yw - 0.01, yw + (yw < YC ? 1 : -1)), max(yw + 0.01, yw + (yw < YC ? 1 : -1)), CARD_Z0, CARD_Z1);
    }
    for (h = BRD_HOLES) cyl_x(BOSS_HOLE / 2, X0 + 0.5, X0 + BACK + BOSS_H + 1, YC + h[0] - 6, BRD_Z0 + h[1], fn = 16);
    for (h = LID_INS) ins_x(M3_INS_D, 6, h[0], h[1], X1, -1);
    for (h = MOUNT_HOLES) cyl_x(M3_CLEAR / 2, X0 - 1, X0 + BACK + 1, h[0], h[1], fn = 24);
    box(USB_X - USB[1] / 2, USB_X + USB[1] / 2, YC - USB[0] / 2, YC + USB[0] / 2, Z0 - 1, Z0 + WALL + 1);      // USB-C opening (bottom)
    box(X1 - 10 - SLOT[1], X1 - 10, YC - SLOT[0] / 2, YC + SLOT[0] / 2, Z1 - WALL - 1, Z1 + 1);                // cable slot top
    box(X1 - 10 - SLOT[1], X1 - 10, Y0 + 6 - SLOT[0] / 2, Y0 + 6 + SLOT[0] / 2, Z0 - 1, Z0 + WALL + 1);        // cable slot bottom
}

T = 2;  VENT_W = 2;  VENT_L = 20;  VENT_Z0 = [112, 134];  VENT_DY = [-13, 13];
LABEL = [20, 30, 0.6];  LABEL_ZC = 170;  WAGO_POCKET = [13.6, 20.6, 8.6];  WAGO_ZC = 118;   // Wago 221-413 [VERIFY 13.1 x 20.3 x 8.1]
module p04_tray_lid() difference() {
    union() {
        box(X1, X1 + T, Y0, Y1, Z0, Z1);
        difference() {                                                                                     // Wago cradle inside
            box(X1 - WAGO_POCKET[2] - 1.2, X1 + 0.01, YC - WAGO_POCKET[0] / 2 - 1.2, YC + WAGO_POCKET[0] / 2 + 1.2, WAGO_ZC - WAGO_POCKET[1] / 2 - 1.2, WAGO_ZC + WAGO_POCKET[1] / 2 + 1.2);
            box(X1 - WAGO_POCKET[2] - 2, X1 + 0.02, YC - WAGO_POCKET[0] / 2, YC + WAGO_POCKET[0] / 2, WAGO_ZC - WAGO_POCKET[1] / 2, WAGO_ZC + WAGO_POCKET[1] / 2 + 5);
        }
    }
    for (h = LID_INS) cyl_x(M3_CLEAR / 2, X1 - 1, X1 + T + 1, h[0], h[1], fn = 24);
    for (zz = VENT_Z0) for (dy = VENT_DY) box(X1 - 1, X1 + T + 1, YC + dy - VENT_W / 2, YC + dy + VENT_W / 2, zz, zz + VENT_L);   // 4 vent slots 2 x 20
    box(X1 + T - LABEL[2], X1 + T + 1, YC - LABEL[0] / 2, YC + LABEL[0] / 2, LABEL_ZC - LABEL[1] / 2, LABEL_ZC + LABEL[1] / 2);   // label recess
}
if (PART == "tray" || PART == "both") p03_electronics_tray();
if (PART == "lid" || PART == "both") p04_tray_lid();
