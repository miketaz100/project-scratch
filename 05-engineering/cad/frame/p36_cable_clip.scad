// =====================================================================
//  p36_cable_clip.scad - P36 cable clip (x6): 2020 T-slot snap, 5 mm cable loop, zip-tie slot
//  PROJECT SCRATCH · 05-engineering/cad/frame · units: mm · frame: local (base plate z 0..2, snap foot below, loop above)
//  Sources: mechanical.md section 3.3 (DXL cable with a 60 mm service loop in clip P36), 11 P36 (12 x 10 x 8).
//  Envelope 12 x 10 x 12.6: a diam 5 loop plus the 3.3 snap foot cannot fit in 8 (C-T1).  Print flat (loop up).
// =====================================================================
include <lib_sp1.scad>
CX = 12;  CY = 10;  BASE_T = 2;  NECK_W = 5.8;  NECK_H = 1.8;  FOOT_W = 9.5;  FOOT_T = 1.5;  LOOP_ID = 5;  LOOP_WALL = 1.5;  TIE = [3, 1.5];
module p36_cable_clip() difference() {
    union() {
        cbox(0, 0, BASE_T / 2, CX, CY, BASE_T);
        cbox(0, 0, -NECK_H / 2, NECK_W, CY, NECK_H);                                   // neck through the 6 mm slot opening
        cbox(0, 0, -NECK_H - FOOT_T / 2, FOOT_W, CY, FOOT_T);                          // snap foot inside the slot
        rid = LOOP_ID / 2; zc = BASE_T + rid + LOOP_WALL - 0.5;
        difference() {
            cyl_y(rid + LOOP_WALL, -CY / 2, CY / 2, 0, zc);
            cyl_y(rid, -CY - 1, CY + 1, 0, zc);
            box(-1.2, 1.2, -CY - 1, CY + 1, BASE_T + rid + LOOP_WALL, BASE_T + 2 * rid + 3 * LOOP_WALL);   // C opening
        }
    }
    box(-CX / 2 - 1, CX / 2 + 1, -TIE[0] / 2, TIE[0] / 2, BASE_T + 0.2, BASE_T + 0.2 + TIE[1]);        // zip-tie slot
}
p36_cable_clip();
