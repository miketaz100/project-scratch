// pad_assembly.scad - whole PAD at the home pose (block centred, nails at e = 15 on the R85 design head)
include <lib_pad.scad>
color("lightgrey", 0.5) pd01_deck();
color("steelblue") pd02_skirt_frame();
pd05_floor_plate(); pd07_gallery_plate(); pd08_skirt_plate(); pd10_yoke();
for (p = PINS) { pd06_cartridge(p[0], p[1]); pd09_piston(p[0], p[1]); color("red") pd15_nail(p[0], p[1]); }
for (a = STOP_ANG) pd11_stop_block(a);
for (a = SKID_ANG) { pd12_skid_stem(a); pd13_skid_foot(a); pd14_skid_knob(a); }
for (a = DOME_ANG) { p = polar(RD, a); color("white") translate([p[0], p[1], ZD]) sphere(BALL_D / 2); }
