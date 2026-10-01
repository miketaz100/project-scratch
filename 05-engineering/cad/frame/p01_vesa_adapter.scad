// =====================================================================
//  p01_vesa_adapter.scad - P1 VESA adapter plate (fixed side of the fail-safe hinge)
//  PROJECT SCRATCH · 05-engineering/cad/frame · units: mm · frame: global (section 2)
//  Sources: mechanical.md section 3.3 (6 mm plate 140 x 145, VESA 75 counterbored, hinge ears at Y +/-30 to the
//  pin at X -60 / Z 84, magnet arm to X -81..-66 / Z 34, up-stop boss M4, tray seat, pulley bosses Y +/-60 on the
//  top edge, rear spring channels, anchor hooks Z 30), 4.1 (ears Y +/-25..35, bore 6.3), 4.4, 4.6, 11 P1.
//  Print base plate flat on the bed (rear face down).  Ribs: 8 mm edge ribs on the front face (section 11: 4 mm ribs).
//  Section 11's 66 x 140 x 145 envelope cannot hold the ear round ends (to X -46), the pulley bosses (X -131) or
//  the rear spring channels (X -137): modelled envelope 91 x 140 x 150 (C-F1).
// =====================================================================
include <lib_sp1.scad>
PLATE_X0 = -126;  PLATE_X1 = -120;  PLATE_Y = 140;  PLATE_Z0 = 25;  PLATE_Z1 = 170;
VESA = 75;  VESA_ZC = 110;  VESA_D = 4.5;  VESA_CB_D = 8;  VESA_CB_H = 3;
EAR_Y0 = 25;  EAR_Y1 = 35;  EAR_H = 28;  EAR_END_R = 14;
MAGARM_X1 = -79;  MAGARM_Y = 15;  MAGARM_Z0 = 20;  MAGARM_Z1 = 48;  MAGARM_WALL = 3;  MAGARM_FRONT_T = 10;
MAG_CB_D = 20.4;  MAG_CB_H = 2;
UPSTOP_X1 = -98;  UPSTOP_Y = 10;  UPSTOP_Z0 = 92;  UPSTOP_Z1 = 108;  UPSTOP_ZC = 100;
PULLEY_Y = 60;  PULLEY_X = -123;  PULLEY_ZC = 141.5;  PULLEY_WIN_Y = 7;  PULLEY_WIN_Z = 20;
PBOSS_X0 = -131;  PBOSS_X1 = -115;  PBOSS_Y0 = 54;  PBOSS_Y1 = 66;  PBOSS_Z0 = 129;  PBOSS_Z1 = 154;
AXLE_D = 3.2;  CHAN_X0 = -137;  CHAN_W0 = 52.5;  CHAN_W1 = 67.5;  CHAN_WALL = 2;  CHAN_Z0 = 26;
HOOK_Z = 30;  HOOK_D = 5;  HOOK_HEAD_D = 8;  HOOK_L = 9;
TRAY_HOLES = [[21, 105.5], [49, 105.5], [21, 160], [49, 160]];       // 4 x M3 inserts, front face (P3)
EDGE_RIB_Y = 66;  GUIDE_HOLES = [[-91, 6], [-84, 6]];               // 2 x M3 inserts under the magnet arm (P45)

module p01_vesa_adapter() {
    x0 = PLATE_X0; x1 = PLATE_X1; hy = PLATE_Y / 2; xm = MAGARM_X1; ma = MAGARM_Y;
    difference() {
        union() {
            box(x0, x1, -hy, hy, PLATE_Z0, PLATE_Z1);
            for (s = [-1, 1]) box(x1 - 0.01, x1 + 8, min(s * EDGE_RIB_Y, s * hy), max(s * EDGE_RIB_Y, s * hy), PLATE_Z0, PLATE_Z1);   // edge ribs
            for (s = [-1, 1]) ext_y(min(s * EAR_Y0, s * EAR_Y1), max(s * EAR_Y0, s * EAR_Y1)) {                                  // hinge ears + gusset
                hull() { translate([x1 - 0.01, PIN_Z - EAR_H / 2]) square([PIN_X - (x1 - 0.01), EAR_H]); translate([PIN_X, PIN_Z]) circle(EAR_END_R, $fn = FN); }
                polygon([[x1 - 0.01, 40], [x1 - 0.01, PIN_Z - 13], [-85, PIN_Z - 13]]);
            }
            box(x1 - 0.01, xm, -ma, ma, MAGARM_Z0, MAGARM_Z0 + MAGARM_WALL);                                                          // magnet arm: bottom web
            for (s = [-1, 1]) box(x1 - 0.01, xm, min(s * (ma - MAGARM_WALL), s * ma), max(s * (ma - MAGARM_WALL), s * ma), MAGARM_Z0, MAGARM_Z1);   // side webs
            box(xm - MAGARM_FRONT_T, xm, -ma, ma, MAGARM_Z0, MAGARM_Z1);                                                             // magnet seat plate
            box(x1 - 0.01, UPSTOP_X1, -UPSTOP_Y, UPSTOP_Y, UPSTOP_Z0, UPSTOP_Z1);                                                    // up-stop boss
            for (s = [-1, 1]) {
                box(PBOSS_X0, PBOSS_X1, min(s * PBOSS_Y0, s * PBOSS_Y1), max(s * PBOSS_Y0, s * PBOSS_Y1), PBOSS_Z0, PBOSS_Z1);        // pulley cheeks
                for (w = [CHAN_W0, CHAN_W1 - CHAN_WALL]) box(CHAN_X0, x0 + 0.01, min(s * w, s * (w + CHAN_WALL)), max(s * w, s * (w + CHAN_WALL)), CHAN_Z0, PBOSS_Z0 + 0.01);   // spring channels (rear)
                cyl_x(HOOK_D / 2, x0 - HOOK_L, x0 + 0.01, s * PULLEY_Y, HOOK_Z);                                                      // anchor hook pin
                cyl_x(HOOK_HEAD_D / 2, x0 - HOOK_L - 1.5, x0 - HOOK_L + 0.01, s * PULLEY_Y, HOOK_Z);                                  // hook head
            }
        }
        for (yy = [-VESA / 2, VESA / 2]) for (zz = [VESA_ZC - VESA / 2, VESA_ZC + VESA / 2]) {
            cyl_x(VESA_D / 2, x0 - 1, x1 + 1, yy, zz, fn = 24); cyl_x(VESA_CB_D / 2, x1 - VESA_CB_H, x1 + 1, yy, zz, fn = 24); }
        cyl_y(PIN_BORE / 2, -40, 40, PIN_X, PIN_Z, fn = 32);                                        // hinge pin bores (ream 6.3)
        cyl_x(MAG_CB_D / 2, xm - MAG_CB_H, xm + 0.01, 0, MAG_Z);                                    // magnet locating counterbore
        cyl_x(M3_CLEAR / 2, xm - MAGARM_FRONT_T - 1, xm, 0, MAG_Z, fn = 24);                        // magnet rear M3
        ins_x(M4_INS_D, M4_INS_L, 0, UPSTOP_ZC, UPSTOP_X1, -1);                                     // up-stop M4 insert
        for (s = [-1, 1]) {
            box(PBOSS_X0 - 1, PBOSS_X1 + 1, s * PULLEY_Y - PULLEY_WIN_Y / 2, s * PULLEY_Y + PULLEY_WIN_Y / 2, PULLEY_ZC - PULLEY_WIN_Z / 2, PULLEY_ZC + PULLEY_WIN_Z / 2);   // pulley window
            cyl_y(AXLE_D / 2, min(s * (PBOSS_Y0 - 1), s * (PBOSS_Y1 + 1)), max(s * (PBOSS_Y0 - 1), s * (PBOSS_Y1 + 1)), PULLEY_X, PULLEY_ZC, fn = 24);   // M3 axle
        }
        for (h = TRAY_HOLES) ins_x(M3_INS_D, M3_INS_L, h[0], h[1], x1, -1);
        for (h = GUIDE_HOLES) ins_z(M3_INS_D, M3_INS_L, h[0], h[1], MAGARM_Z0, false);
    }
}
p01_vesa_adapter();
