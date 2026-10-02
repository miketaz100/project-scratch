// DB06 bulkhead (box half, in the right end-wall window), DB07 umbilical plug (latched half),
// DB08 inner clamp plate - SP1 v3 DRIVE BOX - frame b (x = u outward, y = v along the wall, z = w up).
// Wall window: 73 x 39 mm (v +/-36.5, w +/-19.5), centre at case Y 115, Z 64 (inside-floor datum).
// Ports PIN A / PIN B / PALM at v -16 / 0 / +16, w +8: M5 tapped (KQ2H23-M5A) on the inner face of
// DB06 and on the rear face of DB07; 3 x 1 mm NBR O-ring face seals in DB07. Two 3 x 12 dowels,
// two M4 x 30 knurled thumb screws into M4 nuts trapped in DB06. Housing slot 52 x 8 mm through both.
// Select with -D 'PART="bulkhead"' | "plug" | "clamp".  Print DB06/DB07 in SLA (airtight).
include <lib_drivebox.scad>
PART = "bulkhead";

module db06_bulkhead() {
    difference() {
        union() {
            box(HEAD_U0, HEAD_U1, -HEAD_V, HEAD_V, -HEAD_W, HEAD_W);
            box(NECK_U0, HEAD_U0 + 0.01, -NECK_V, NECK_V, -NECK_W, NECK_W);
        }
        for (v = PORT_V) {
            cyl_x(PORT_D / 2, NECK_U0 - 0.01, HEAD_U1 + 0.01, v, PORT_W, fn = 24);
            cyl_x(M5_TAP / 2, NECK_U0 - 0.01, NECK_U0 + 8, v, PORT_W, fn = 24);
        }
        box(NECK_U0 - 0.01, HEAD_U1 + 0.01, -SLOT_V, SLOT_V, SLOT_W0, SLOT_W1);
        for (s = [-1, 1]) {
            cyl_x(DOWEL_D_PRESS / 2, HEAD_U1 - DOWEL_DEPTH, HEAD_U1 + 0.01, s * DOWEL_V, DOWEL_W, fn = 24);
            cyl_x(THUMB_D / 2, HEAD_U0 - 0.01, HEAD_U1 + 0.01, s * THUMB_V, THUMB_W, fn = 24);
            box(THUMB_NUT_U - THUMB_NUT_T / 2, THUMB_NUT_U + THUMB_NUT_T / 2,
                s * THUMB_V - THUMB_NUT_AF / 2, s * THUMB_V + THUMB_NUT_AF / 2,
                THUMB_W - THUMB_NUT_AF / 2 / cos(30), HEAD_W + 0.01);                 // M4 nut slot, opens on top
            for (sw = [-1, 1]) {
                cyl_x(M3_CLEAR / 2, HEAD_U0 - 0.01, HEAD_U1 + 0.01, s * CLAMP_V, sw * CLAMP_W, fn = 24);
                cyl_x(CLAMP_CB_D / 2, HEAD_U1 - CLAMP_CB_DEPTH, HEAD_U1 + 0.01, s * CLAMP_V, sw * CLAMP_W, fn = 24);
            }
        }
        for (p = B1_HEAD_POCKETS) pocket_pair(p, HEAD_U0 - 0.01, HEAD_U0 + 8);
        for (p = B1_NECK_POCKETS) pocket_pair(p, NECK_U0 - 0.01, NECK_U0 + 10);
    }
}

module db07_plug() {
    difference() {
        box(PLUG_U0, PLUG_U1, -HEAD_V, HEAD_V, -HEAD_W, HEAD_W);
        for (v = PORT_V) {
            cyl_x(PORT_D / 2, PLUG_U0 - 0.01, PLUG_U1 + 0.01, v, PORT_W, fn = 24);
            difference() {                                                           // O-ring gland
                cyl_x(OR_OD / 2, PLUG_U0 - 0.01, PLUG_U0 + OR_DEPTH, v, PORT_W, fn = 32);
                cyl_x(OR_ID / 2, PLUG_U0 - 0.02, PLUG_U0 + OR_DEPTH + 0.01, v, PORT_W, fn = 32);
            }
            cyl_x(M5_TAP / 2, PLUG_U1 - 8, PLUG_U1 + 0.01, v, PORT_W, fn = 24);
        }
        box(PLUG_U0 - 0.01, PLUG_U1 + 0.01, -SLOT_V, SLOT_V, SLOT_W0, SLOT_W1);
        for (s = [-1, 1]) {
            cyl_x(DOWEL_D_SLIDE / 2, PLUG_U0 - 0.01, PLUG_U0 + DOWEL_DEPTH, s * DOWEL_V, DOWEL_W, fn = 24);
            cyl_x(THUMB_D / 2, PLUG_U0 - 0.01, PLUG_U1 + 0.01, s * THUMB_V, THUMB_W, fn = 24);
            cyl_x(M3_TAP / 2, PLUG_U1 - PCLIP_DEPTH, PLUG_U1 + 0.01, s * PCLIP_V, PCLIP_W, fn = 24);
        }
        for (p = U1_POCKETS) pocket_pair(p, PLUG_U1 - 10, PLUG_U1 + 0.01);
        box(PLUG_U1 - 10, PLUG_U1 + 0.01, U1_POCKET_C[0], U1_POCKET_C[1], U1_POCKET_C[2], U1_POCKET_C[3]);
    }
}

module db08_clamp() {
    u1 = -WALL_T;
    difference() {
        box(u1 - CLAMP_T, u1, -CLAMP_PLATE_V, CLAMP_PLATE_V, -CLAMP_PLATE_W, CLAMP_PLATE_W);
        box(u1 - CLAMP_T - 0.01, u1 + 0.01, -NECK_V - 0.5, NECK_V + 0.5, -NECK_W - 0.5, NECK_W + 0.5);
        for (s = [-1, 1]) for (sw = [-1, 1]) cyl_x(M3_CLEAR / 2, u1 - CLAMP_T - 0.01, u1 + 0.01, s * CLAMP_V, sw * CLAMP_W, fn = 24);
    }
}

if (PART == "bulkhead") db06_bulkhead();
else if (PART == "plug") db07_plug();
else if (PART == "clamp") db08_clamp();
