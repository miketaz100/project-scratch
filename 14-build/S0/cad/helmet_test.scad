// helmet_test.scad - S0a helmet / hinge / coin-bag fit test (leap4-E E4 (e)), printed part H01 (x2)
// PROJECT SCRATCH, 14-build/S0/cad, 2026-10-02.  gen_s0_stl.py mirrors it.
// L-bracket hinge pad.  The base (X-Z plane) goes on the side of the bike helmet (foam tape + two
// zip ties through vents); the flange sticks straight out sideways (+Y).  The Southco E6-10-101-20
// fixed leaf lies on top of the flange with its two studs down through the holes (nuts underneath),
// so the hinge PIN points ear-to-ear (along Y), which is the spec's alpha axis (C23): the bail then
// swings forward and back over the head.  E6 leaf: studs 15.1 mm apart along the pin, 10.2 mm from
// the pin (Southco e6-at.en.pdf, panel holes 5.4 +0.1/-0).  No printer: a 1 x 1 in aluminium angle
// bracket drilled 7/32 in at the same spacing does the same job.
include <s0_lib.scad>
HB = [46, 5, 30];           // base: X (front-back) x Y (thickness) x Z (height)
HF = [46, 30, 5];           // flange: X x Y (outward) x Z (thickness), on top of the base
E6_PITCH = 15.1;  E6_HOLE = 5.5;  E6_PIN_OFF = 10.2;
module hinge_pad() difference() {
    union() {
        box(-HB[0]/2, HB[0]/2, -HB[1], 0, 0, HB[2]);                         // base against the helmet
        box(-HF[0]/2, HF[0]/2, -HB[1], HF[1], HB[2] - HF[2], HB[2]);          // flange
        for (x = [12, 19]) hull() { box(x, x + 3, -0.1, 0.1, 4, HB[2] - HF[2]); box(x, x + 3, -0.1, 18, HB[2] - HF[2] - 0.1, HB[2] - HF[2]); }   // gussets
    }
    for (y = [9, 9 + E6_PITCH]) {
        cyl(E6_HOLE, HB[2] - HF[2] - 1, HB[2] + 1, -E6_PIN_OFF, y, fn=32);
        cyl(10, HB[2] - HF[2] - 1, HB[2] - HF[2] + 2.5, -E6_PIN_OFF, y, fn=6);   // nut pocket under the flange
    }
    for (x = [-HB[0]/2 + 3.5, HB[0]/2 - 3.5], z = [6, 17.5]) box(x - 1.25, x + 1.25, -HB[1] - 1, 1, z - 2.5, z + 2.5);   // zip-tie slots
}
hinge_pad();     // print with the flange top face on the bed (rotate [180, 0, 0])
