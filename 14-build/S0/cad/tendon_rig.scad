// tendon_rig.scad - S0b tendon ink rig, printed parts T01-T06 (leap4-D (e), SYSTEM-SPEC-v3 sec 4.4, 5.3)
// PROJECT SCRATCH, 14-build/S0/cad, 2026-10-02.  Source of truth; gen_s0_stl.py mirrors it.
// T01 drum carries forward to Stage A (spec: Ø 12 drum, double groove, groove 2 = pad 2; reprint in
// SLA for Stage A).  Everything else is rig-only.  Helix handedness may differ from the STL; it
// does not matter.

include <s0_lib.scad>

PART = "drum";   // drum | motor_table | stop_block | housing_sleeve | rig_deck | pen_plate

// ------------------------------------------------------------------ T01 drum (Ø 12, two helical grooves)
module drum() {
    z_f1 = HUB_H;  z_ga = z_f1 + FL_H;  z_sep = z_ga + GROOVE_W;  z_gb = z_sep + SEP_W;
    z_f2 = z_gb + GROOVE_W;  z_top = z_f2 + FL_H;
    turns = GROOVE_W / GROOVE_PITCH;
    difference() {
        union() {
            cyl(HUB_D, 0, z_f1 + 0.01);
            cyl(DRUM_FL_D, z_f1, z_ga);
            cyl(DRUM_LAND_D, z_ga - 0.01, z_f2 + 0.01);
            cyl(DRUM_FL_D, z_f2, z_top);
        }
        for (z0 = [z_ga, z_gb]) translate([0, 0, z0])
            linear_extrude(height=GROOVE_W, twist=360*turns, slices=turns*48) translate([DRUM_PITCH_D/2, 0]) circle(r=GROOVE_R, $fn=16);
        difference() { cyl(SHAFT_D, -1, z_top + 1, fn=40); box(SHAFT_FLAT, 5, -5, 5, -2, z_top + 2); }   // D-bore
        cyl_ab(3.2, [0, 0, HUB_H/2], [HUB_D/2 + 1, 0, HUB_H/2], fn=20);                             // M3 grub
        box(3.4, 6.0, -2.95, 2.95, -1, HUB_H/2 + 2.95);                                              // M3 nut slot
        // cable anchors: groove end -> channel -> axial Ø1 hole -> crimp-sleeve pocket on the outer face
        box(DRUM_PITCH_D/2 - 0.4, ANCHOR_R + 0.5, -0.5, 0.5, z_ga - 1, z_ga + 0.01);
        cyl(1.0, z_f1 - 0.5, z_ga + 0.5, ANCHOR_R, 0, fn=16);
        box(ANCHOR_R - 1, DRUM_FL_D/2 + 1, -1.1, 1.1, z_f1 - 0.01, z_f1 + 1.2);
        box(DRUM_PITCH_D/2 - 0.4, ANCHOR_R + 0.5, -0.5, 0.5, z_f2 - 0.01, z_f2 + 1);
        cyl(1.0, z_f2 - 0.5, z_top + 0.5, ANCHOR_R, 0, fn=16);
        box(ANCHOR_R - 2.5, DRUM_FL_D/2 + 1, -1.1, 1.1, z_top - 1.2, z_top + 1);
        cyl(3.1, z_top - 2.1, z_top + 1, -ANCHOR_R, 0, fn=24);                                      // Ø3x2 index magnet (Stage A Hall)
    }
}

// ------------------------------------------------------------------ T02 motor table (one per motor; motor hangs below, shaft up)
module motor_table() {
    w = 52;  h = 30;  t = 4;
    difference() {
        union() {
            box(-w/2, w/2, -w/2, w/2, h - t, h);
            box(-w/2, -w/2 + 3, -w/2, w/2, 0, h);  box(w/2 - 3, w/2, -w/2, w/2, 0, h);
            box(-w/2 - 12, -w/2 + 3, -w/2, w/2, 0, 4);  box(w/2 - 3, w/2 + 12, -w/2, w/2, 0, 4);
        }
        cyl(23, h - t - 1, h + 1);                                                // NEMA 17 pilot boss Ø 22
        for (sx = [-15.5, 15.5], sy = [-15.5, 15.5]) cyl(M3_CLEAR, h - t - 1, h + 1, sx, sy, fn=24);
        for (sx = [-w/2 - 6, w/2 + 6], sy = [-16, 16]) cyl(WOOD_SCREW, -1, 5, sx, sy, fn=24);
    }
}

// ------------------------------------------------------------------ T03 box-end housing stop, T04 sleeve for the thin housing
module stop_block() {
    zc = STOP_CABLE_Z;
    difference() {
        union() { box(-8, 8, -7, 7, 0, zc + 8); box(-20, 20, -7, 7, 0, 4); }
        cyl_ab(5.2, [0, -3, zc], [0, 8, zc], fn=32);          // housing ferrule seat, 10 deep from +Y
        cyl_ab(2.0, [0, -8, zc], [0, 0, zc], fn=20);          // cable to the drum
        for (sx = [-14, 14]) cyl(WOOD_SCREW, -1, 5, sx, 0, fn=24);
    }
}
module housing_sleeve() difference() { cyl(5.1, 0, 10); cyl(2.2, -1, 11, fn=24); }

// ------------------------------------------------------------------ T05 rig deck (pad-end housing stops at R 60), T06 pen plate
module rig_deck() {
    difference() {
        union() {
            difference() { cyl(152, 0, 5); cyl(132, -1, 6); }
            for (a = DOME_ANG) rotate([0, 0, a]) box(RIG_STOP_R, RIG_STOP_R + 16, -6, 6, 0, RIG_CABLE_Z + 7);
        }
        for (a = DOME_ANG) let(u = polar(1, a)) {
            cyl_ab(2.0, [u[0]*(RIG_STOP_R - 1), u[1]*(RIG_STOP_R - 1), RIG_CABLE_Z], [u[0]*(RIG_STOP_R + 17), u[1]*(RIG_STOP_R + 17), RIG_CABLE_Z], fn=20);
            cyl_ab(5.2, [u[0]*(RIG_STOP_R + 6), u[1]*(RIG_STOP_R + 6), RIG_CABLE_Z], [u[0]*(RIG_STOP_R + 17), u[1]*(RIG_STOP_R + 17), RIG_CABLE_Z], fn=32);
        }
    }
}
module pen_plate() {
    difference() {
        union() {
            cyl(60, PEN_PLATE_Z0, PEN_PLATE_Z1);
            cyl(18, PEN_PLATE_Z0, PEN_PLATE_Z0 + 28, d2=16);                    // pen collar
            for (a = [30, 150, 270]) let(p = polar(20, a)) cyl(21, 8.5, PEN_PLATE_Z0 + 0.01, p[0], p[1]);
        }
        cyl(12.2, PEN_PLATE_Z0 - 1, PEN_PLATE_Z0 + 30, fn=48);                 // pen bore: wrap tape on the pen to fit
        for (a = [30, 150, 270]) let(p = polar(20, a)) sph(16.4, [p[0], p[1], 8], fn=48);   // marble cups (16 mm marbles)
        for (a = DOME_ANG) let(p = polar(POST_R, a)) cyl(M3_PILOT, PEN_PLATE_Z0 - 1, PEN_PLATE_Z1 + 1, p[0], p[1], fn=24);   // M3 cable posts
    }
}

if (PART == "drum") drum();
else if (PART == "motor_table") motor_table();
else if (PART == "stop_block") stop_block();
else if (PART == "housing_sleeve") housing_sleeve();
else if (PART == "rig_deck") rig_deck();
else if (PART == "pen_plate") rotate([180, 0, 0]) pen_plate();
