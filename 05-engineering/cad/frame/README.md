# SP1 module frame, float and hand: CAD folder (P1–P48)

Project SCRATCH, 05-engineering/cad/frame, CAD agent, 2026-10-01 (rev 2, after the Director's XL330 / button vendor data in bom-verified.md §11). Units mm.
Binding design: `05-engineering/mechanical.md` (§2 frame, §3–§10 subsystems, §11 printed parts list) as overridden by `DESIGN-FREEZE-ADDENDUM-1.md`. Tip-side mates (paddles, clamp bars, seam sleeves, tips) are the tip lead's files in `../tips/`. Every conflict, assumption and missing dimension found while modelling is in `CONFLICTS.md`; read it before printing anything in the hand or the electronics tray.

## 0. Scope (Director, 2026-10-01, crown mount)

SP1 will be mounted on a **head-resting crown**, not on the monitor-arm frame. The parts the hand and yoke need are the deliverables: **P13–P16** (servo cradle with the verified XL330 back-face holes, strap, idler housing, horn adapter), **P17–P18** guard caps, **P19–P34** (yoke cheeks, crossbar/mast, rail shroud, stops, scale, riser, cleat, wrist seat, weight cap, knuckle plate, boot clamp, palm tray, lid, root clamp bars), **P35**, **P37–P40**, **P46–P48**. The frame-only parts were modelled before the scope change and are kept but marked **FRAME-ONLY** below: **P1, P2, P5–P12, P41–P45**. P3/P4 (electronics tray) mounted on the VESA adapter and P36 (2020 cable clip) are in neither list: files kept, mounting to be re-decided for the crown. The crown structure must hold the elbow carrier's two bolt faces, which are specified in `CONFLICTS.md` §"Crown interface": the servo cradle's back face (plane Y −131.5, 34 × 46, 4 × M3 at X ±14 / Z 80 and 104) and the idler housing's outer face (plane Y +130, 30 × 40, 2 × M3 at X 0 / Z 70 and 98), coaxial about the elbow axis (X 0, Z 84).

## 1. Files

| File | Parts | Frame |
|---|---|---|
| `lib_sp1.scad` | shared constants and helpers: fastener / insert sizes (M3 insert 4.0 × 4, M2 insert 3.2 × 3, Ø 3.4 clearance, countersink, 2020 socket 20.2), rounded boxes, 15° draft helper, MGN9C 15 × 10 pattern [VERIFY], XL330 pocket 20.4 × 34.4 × 23.5 and its verified 16 × 30 frame-hole pattern, the shared knuckle-plate slot, bought-part reference solids | — |
| `p01_vesa_adapter.scad` | P1 (FRAME-ONLY) | global |
| `p02_p05_p06_p07_hinge_parts.scad` | P2 sheave, P5 knuckle, P6 keeper lever, P7 cord bar, P44 reset toggle, P45 reset cord guide (`PART=`): all FRAME-ONLY | P5/P6/P7/P45 global; P2/P44 local |
| `p03_p04_electronics_tray.scad` | P3, P4 (frame-mounted: relocate for the crown) | global |
| `p08_p09_yaw_plates.scad` | P8, P9 (FRAME-ONLY) | global |
| `p10_reset_tab.scad` | P10 (FRAME-ONLY) | global |
| `p11_p12_drop_legs.scad` | P11, P12 (mirror) (FRAME-ONLY; they show how the two crown bolt faces were carried) | global |
| `p13_p14_servo_cradle.scad` | P13, P14 | global |
| `p15_idler_housing.scad` | P15 | global |
| `p16_horn_adapter_disc.scad` | P16 | global |
| `p17_p18_guard_caps.scad` | P17, P18 (mirror) | global |
| `p19_p20_yoke_cheeks.scad` | P19, P20 | global |
| `p21_yoke_crossbar.scad` | P21 | global |
| `p22_rail_shroud.scad` | P22 | global |
| `p23_p24_rail_stops.scad` | P23, P24 | global |
| `p25_scale_strip.scad` | P25 | local (strip along Z) |
| `p26_carriage_riser.scad` | P26 | global |
| `p27_trim_cleat.scad` | P27 | global |
| `p28_upper_wrist_seat.scad` | P28, P29 cap, P47 filler (`PART=`) | P28 global; P29/P47 local |
| `p30_p31_p35_knuckle_plate_boot.scad` | P30 plate, P31 boot frame, P35 template (`PART=`) | P30/P31 global; P35 local |
| `p32_palm_tray.scad` | P32 | global |
| `p33_palm_lid.scad` | P33 (includes p32 for the outline) | global |
| `p34_root_clamp_bar.scad` | P34 | local |
| `p36_cable_clip.scad` | P36 | local |
| `p37_p38_control_panel.scad` | P37, P38 | local |
| `p39_p40_button_housing.scad` | P39, P40 (split halves) | local |
| `p41_p48_cradle_tools.scad` | P41 foot cup, P42 wedge, P43 gauge (FRAME-ONLY), P46 pull clip, P48 tip box (`PART=`) | local |
| `gen_frame_stl.py` | Python mirror of every SCAD file; writes `stl/*.stl`, prints the parts table, runs the fit and sweep checks (`stl/checks.txt`, `stl/report.txt`) | — |
| `stl/` | 48 meshes, one per part design | as above |

"Global" = the assembly frame of mechanical.md §2 (Z up, X = stroke, Y = across; origin at the centre nail edge, arm at 0°, float on its down-stop, module latched). Global-frame STLs load together as the assembly in any viewer; rotate them in the slicer per §3. "Local" parts are modelled in their natural print pose or in the frame their comment names (P46 in the TM1 frame of the centre paddle nose).

## 2. Rendering the SCAD files and regenerating the STLs

**OpenSCAD GUI.** Open the part file, keep `lib_sp1.scad` in the same folder (it is `include`d), set the `PART = "..."` variable at the top for files that hold several parts, press F5 to preview and **F6** to render, then *File → Export → Export as STL*. The spheres (P30, P31, P32) render in 10–40 s at `$fn = 160`; everything else is seconds. Command line: `openscad -o stl/p30_knuckle_plate.stl -D 'PART="plate"' p30_p31_p35_knuckle_plate_boot.scad`. The SCAD files use only cube, cylinder, sphere, hull, linear_extrude / rotate_extrude of polygons, offset, rotate/translate/mirror and booleans: no text(), import() or surface().

**Python mirror (no OpenSCAD needed).** There is no OpenSCAD binary on the build machine, so the STLs in `stl/` come from the Python mirror:

```
cd 05-engineering/cad/frame
<cadenv>/bin/python gen_frame_stl.py            # all parts + checks; exit 0 only if every mesh is watertight
<cadenv>/bin/python gen_frame_stl.py --no-checks --only=P30,P32
```

Any Python 3.10+ with `numpy`, `trimesh` and `manifold3d` works (`pip install numpy trimesh manifold3d`; no scipy / rtree needed). The SCAD files are the source of truth: constant names in the script match the SCAD names one for one, and every mating feature (hole patterns, pockets, bores, slots, stops, cones, insert holes) is built from the same numbers in both. If you change a SCAD constant, change the same constant in the script.

**Features present in neither** (cosmetic, listed so nobody looks for them): R 3 edge rounds on P1, P17/P18, P30 and the "15° perimeter draft" of P30 (see CONFLICTS C-H2; the slot's 15° lead-in *is* modelled); 1.2 mm stiffening ribs on P32; raised numerals on P25 (ink them; ridges and ticks are modelled); the finger knurl on P29 is 12 notches; rubber-foot recesses on P37 (they are on the lid P38). The STL and SCAD geometry are otherwise identical; nothing was simplified in the STL only.

## 3. Output of the 2026-10-01 run

48/48 meshes watertight (manifold status clean, one solid piece each; P21's box beam contains one sealed cavity, which is correct for a box beam). "§11 bbox" is the X × Y × Z of mechanical.md §11 in the model's frame; "match" = all three within 1 mm. Every "NO" is explained in `CONFLICTS.md` (the id in the last column). Mass = solid volume × 1.27 g/cm³, an upper bound; printed mass depends on walls/infill.

| Part | STL | bbox X × Y × Z | volume mm³ | solid g | §11 bbox | match | conflict |
|---|---|---|---|---|---|---|---|
| P1 | p01_vesa_adapter (FRAME-ONLY) | 91.0 × 140.0 × 150.0 | 212263 | 269.6 | 66 × 140 × 145 | NO | C-F1 |
| P2 | p02_pulley_sheave (FRAME-ONLY) | 16.0 × 16.0 × 5.0 | 533 | 0.7 | 16 × 16 × 5 | yes | |
| P3 | p03_electronics_tray | 32.0 × 36.0 × 92.0 | 24903 | 31.6 | 32 × 36 × 92 | yes | C-F7 |
| P4 | p04_electronics_tray_lid | 11.8 × 36.0 × 92.0 | 6609 | 8.4 | 2 × 36 × 92 | NO | C-E1 |
| P5 | p05_frame_hinge_knuckle (FRAME-ONLY) | 24.0 × 48.0 × 30.0 | 26961 | 34.2 | 24 × 48 × 30 | yes | |
| P6 | p06_keeper_lever (FRAME-ONLY) | 27.0 × 30.0 × 115.0 | 26243 | 33.3 | 12 × 30 × 60 | NO | C-F3 |
| P7 | p07_cord_bar (FRAME-ONLY) | 38.0 × 140.0 × 17.0 | 20968 | 26.6 | 12 × 140 × 12 | NO | C-F4 |
| P8 | p08_frame_yaw_plate (FRAME-ONLY) | 70.0 × 70.0 × 6.0 | 26890 | 34.1 | 70 × 70 × 6 | yes | C-F5 |
| P9 | p09_carrier_yaw_plate (FRAME-ONLY) | 70.0 × 70.0 × 6.0 | 26935 | 34.2 | 70 × 70 × 6 | yes | C-F5 |
| P10 | p10_reset_tab (FRAME-ONLY) | 25.0 × 30.0 × 25.0 | 13905 | 17.7 | 25 × 30 × 25 | yes | C-F2 |
| P11 | p11_drop_leg_servo (FRAME-ONLY) | 55.0 × 24.0 × 115.0 | 36586 | 46.5 | 50 × 20 × 105 | NO | C-F6 |
| P12 | p12_drop_leg_idler (FRAME-ONLY) | 55.0 × 24.0 × 115.0 | 36711 | 46.6 | 50 × 20 × 105 | NO | C-F6 |
| P13 | p13_servo_cradle | 40.0 × 32.5 × 46.0 | 23441 | 29.8 | 30 × 30 × 44 | NO | C-S1, C-S7, crown face |
| P14 | p14_servo_strap | 30.0 × 5.2 × 18.0 | 2099 | 2.7 | 30 × 4 × 10 | NO | C-S3 |
| P15 | p15_idler_housing | 30.0 × 14.0 × 40.0 | 14207 | 18.0 | 30 × 14 × 40 | yes | C-S4 |
| P16 | p16_horn_adapter_disc | 24.0 × 3.0 × 24.0 | 1117 | 1.4 | 24 × 3 × 24 | yes | C-S6 |
| P17 | p17_guard_cap_servo | 60.0 × 32.0 × 30.0 | 10501 | 13.3 | 60 × 40 × 30 | NO | C-S5 |
| P18 | p18_guard_cap_idler | 60.0 × 32.0 × 30.0 | 10501 | 13.3 | 60 × 40 × 30 | NO | C-S5 |
| P19 | p19_yoke_cheek_a | 75.0 × 8.0 × 40.0 | 13724 | 17.4 | 75 × 5 × 40 | NO | 3 mm stop lug |
| P20 | p20_yoke_cheek_b | 75.0 × 5.0 × 40.0 | 13709 | 17.4 | 75 × 5 × 40 | yes | |
| P21 | p21_yoke_crossbar | 20.0 × 186.0 × 106.4 | 33647 | 42.7 | 17 × 196 × 108 | NO | C-Y2, C-Y3 |
| P22 | p22_rail_shroud | 19.5 × 38.0 × 44.0 | 5343 | 6.8 | 16 × 34 × 50 | NO | C-Y4 |
| P23 | p23_rail_down_stop | 12.0 × 20.0 × 8.0 | 1484 | 1.9 | 12 × 20 × 8 | yes | |
| P24 | p24_rail_up_stop | 12.0 × 20.0 × 8.0 | 850 | 1.1 | 12 × 20 × 8 | yes | |
| P25 | p25_scale_strip | 2.5 × 8.0 × 45.4 | 602 | 0.8 | 2 × 8 × 45 | yes | C-T4 |
| P26 | p26_carriage_riser | 38.0 × 34.0 × 39.5 | 3111 | 4.0 | 32 × 20 × 34 | NO | C-Y5 |
| P27 | p27_trim_cleat | 10.0 × 16.0 × 12.0 | 1562 | 2.0 | 10 × 16 × 12 | yes | C-Y6 |
| P28 | p28_upper_wrist_seat | 45.0 × 44.0 × 39.0 | 10066 | 12.8 | 44 × 44 × 39 | yes | C-H6, C-H7 |
| P29 | p29_weight_cap | 15.9 × 15.9 × 4.0 | 741 | 0.9 | 16 × 16 × 4 | yes | |
| P30 | p30_knuckle_plate | 64.0 × 90.0 × 17.4 | 4477 | 5.7 | 64 × 90 × 8 | NO | C-H1, C-H2 |
| P31 | p31_boot_clamp_frame | 60.0 × 86.0 × 15.3 | 3418 | 4.3 | 60 × 86 × 1.2 | NO | C-H1 |
| P32 | p32_palm_tray | 52.0 × 172.0 × 37.1 | 26582 | 33.8 | 52 × 169 × 28 | NO | C-H1, C-H3–C-H5, C-M1 |
| P33 | p33_palm_lid | 54.4 × 174.4 × 11.9 | 18022 | 22.9 | 52 × 169 × 9 | NO | C-H11, C-M1 |
| P34 | p34_root_clamp_bar | 24.0 × 8.0 × 3.0 | 524 | 0.7 | 24 × 8 × 3 | yes | |
| P35 | p35_boot_cutting_template | 76.0 × 104.0 × 1.0 | 7204 | 9.1 | 76 × 104 × 1 | yes | C-T3 |
| P36 | p36_cable_clip | 12.0 × 10.0 × 12.6 | 720 | 0.9 | 12 × 10 × 8 | NO | C-T1 |
| P37 | p37_control_panel_box | 100.0 × 60.0 × 40.0 | 40058 | 50.9 | 100 × 60 × 40 | yes | C-E4 |
| P38 | p38_control_panel_lid | 100.0 × 60.0 × 2.0 | 11588 | 14.7 | 100 × 60 × 2 | yes | |
| P39 | p39_button_housing_half_a | 18.0 × 36.0 × 110.0 | 11640 | 14.8 | 18 × 36 × 110 | yes | C-E3 |
| P40 | p40_button_housing_half_b | 21.0 × 36.0 × 110.0 | 11865 | 15.1 | 18 × 36 × 110 | NO | 3 mm alignment pins |
| P41 | p41_cradle_foot_cup (FRAME-ONLY) | 40.0 × 40.0 × 12.0 | 9042 | 11.5 | 40 × 40 × 12 | yes | |
| P42 | p42_cradle_tilt_wedge (FRAME-ONLY) | 120.0 × 60.0 × 32.2 | 104035 | 132.1 | 120 × 60 × 32 | yes | |
| P43 | p43_apex_height_gauge (FRAME-ONLY) | 12.0 × 12.0 × 120.0 | 16808 | 21.3 | 12 × 12 × 120 | yes | |
| P44 | p44_reset_cord_toggle (FRAME-ONLY) | 40.0 × 14.0 × 14.0 | 5944 | 7.5 | 40 × 14 × 14 | yes | |
| P45 | p45_reset_cord_guide (FRAME-ONLY) | 15.0 × 20.0 × 15.0 | 3873 | 4.9 | 15 × 20 × 15 | yes | |
| P46 | p46_tip_pull_clip | 18.9 × 15.9 × 20.0 | 718 | 0.9 | 18 × 13 × 20 | NO | C-T2 |
| P47 | p47_load_cell_filler | 40.0 × 12.0 × 6.0 | 2763 | 3.5 | 40 × 12 × 6 | yes | C-Y5 |
| P48 | p48_tip_box | 120.0 × 60.0 × 25.0 | 173405 | 220.2 | 120 × 60 × 25 | yes | |

Checks run by the script (full text in `stl/checks.txt`): P13 pocket contains the verified XL330 body with 0.2 mm per side; P21 rail inserts at Z 78/98/118/138/158 = rail holes at 10 + 20 k from the rail end (measure the real rail, bom-verified §11 item 7); P26 holes on the MGN9C 15 × 10 pattern with ≥ 3.3 mm plate margin; P28 recess vs P33 cone 0.20 mm radial, 0.10 axial, no interference; P30 slot to the paddle sections 4.49 / 5.99 / 4.49 mm (§8.7: 4.5 / 6.0 / 4.5), paddle to paddle 6.18 mm (§8.7: 6.2), and with the tip lead's paddle STLs placed at the §8.1 nail positions: no interference with P30–P33, min gaps 4.52 (P30) / 1.90 (P31, see C-H13) / 3.00 (P32) / 7.90 (P33); P32 leaf slots 12.9 × 1.0 vs the 12.7 × 0.3 leaf; P1 ears vs P5 knuckle 1.0 mm per side for the PTFE washers; static assembly of all global-frame parts: no overlaps; arm swept ±31°: no overlaps (the stop lug meets the bumper at ±32° as intended); float at its up-stop at ±28°: no overlaps; fail-safe lift to 25°: **the yaw plates P8/P9 pass through the electronics tray P3/P4 (C-F7)**; highest arm point with the float up Z 177 (§2c asks < 175: the bought rail's top corner, C-Y6).

## 4. Print settings per part (mechanical.md §11; PETG unless stated, 0.4 nozzle, 0.2 layers)

| Part | Orientation on the bed | Walls / infill | Inserts | Post-processing |
|---|---|---|---|---|
| P1 | base plate flat (rear −X face down; rotate −90° about Y) | 5 / 40 % | 4 M3 (tray), 1 M4 (up-stop), 2 M3 (cord guide) | ream the Ø 6.3 pin bores |
| P2 (×2) | flat as modelled | 4 / 100 % | — | press the 623ZZ |
| P3 | open (+X) side up | 3 / 20 % | 2 M3 (lid) | — |
| P4 | flat | 3 / 20 % | — | — |
| P5 | bore axis horizontal, socket up (as modelled) | 6 / 50 % | — | ream Ø 6.3 |
| P6 | lying on its side (Y face down) | 6 / 60 % | — | flatten the keeper recess floor; epoxy + 2 × M3 csk the 25 × 25 × 3 keeper |
| P7 | flat (Z face down) | 5 / 50 % | — | round the eyelet edges |
| P8, P9 | flat | 5 / 50 % | P8: 7 M3 (C-F5) | — |
| P10 | tab flat | 4 / 30 % | — | — |
| P11, P12 | on the side (Y face down) | 5 / 40 % | P11 4 M3, P12 2 M3 | — |
| P13 | horn face (+Y) up | 4 / 40 % | 2 M3 (strap) | glue 2 mm TPU pads on the bumper lugs' trailing faces |
| P14 | flat (Y face down) | 4 / 100 % | — | — |
| P15 | bore axis vertical (rotate 90° about X) | 6 / 60 % | — | test-fit the 625-2RS |
| P16 | flat | 4 / 100 % | — | — |
| P17, P18 | open side up | 3 / 20 % | — | sand edges R 3 |
| P19, P20 | flat (XZ plane on the bed; rotate 90° about X) | 6 / 60 % | P19 6 M3, P20 2 M3 | P20: ream Ø 5.0 |
| P21 | mast face down (rotate so the −X mast face is on the bed), beam along the bed's long axis: **186 mm, bed ≥ 190 mm** | 5 / 40 % | 5 M3 (rail) + 4 (stops) + 2 (cleat) | check the mast face flat to 0.1 with a straightedge |
| P22 | open (−X) side up | 3 / 20 % | — | sand edges |
| P23, P24 | flat | 6 / 100 % | P23 1 M3 brass | P24: glue the 2 mm TPU pad |
| P25 | face up, 0.12 layers | 3 / 100 % | — | ink the ticks and 0/10/20/30 |
| P26 | on its side (Y face down) | 4 / 30 % | — | — |
| P27 | flat | 4 / 50 % | 1 M3 | — |
| P28 | seat face down, post up (as modelled) | 3 / 15 % | 2 M3 (post, filler) | sand the seat face flat on glass; CA the D61, one layer 0.05 tape |
| P29 | flat | 3 / 50 % | — | — |
| P30 | **convex (top) side up: the underside is printed as the top surface**, 0.12 layers, ironing on, supports under the cap | 3 / 30 % | — | 400 grit then buff to Ra ≤ 0.8 µm; IPA wipe |
| P31 | as P30 | 3 / 100 % | — | — |
| P32 | upside down (lid face on the bed), supports under the centre box walls' spherical bottom edge | 2 / 15 %, 4 perimeters locally at the root blocks | 3 M3 (stops), 6 M2 (lid), 6 M2 (plate), 6 M2 (root bars) | — |
| P33 | top face down | 2 / 15 % | — | sand the seat land flat; epoxy the 12 × 1.5 keeper |
| P34 (×3) | groove up (flip Z) | 4 / 100 % | — | — |
| P35 | flat | 2 / 100 % | — | — |
| P36 (×6) | flat (loop up) | 3 / 100 % | — | — |
| P37 | face down | 3 / 20 % | 4 M3 | — |
| P38 | flat | 3 / 20 % | — | — |
| P39, P40 | split face down (as modelled, X = 0 on the bed) | 3 / 25 % | P40 2 M3 | sand the rim R 2; ream the deck hole to Ø 30.0 |
| P41 (×4) | flat | 3 / 30 % | — | — |
| P42 (×2) | flat face down (as modelled) | 3 / 20 % | — | glue the TPU pad |
| P43 | lying flat | 3 / 30 % | — | ink the rings |
| P44 | lying | 3 / 50 % | — | — |
| P45 | flat (Z face down) | 4 / 50 % | — | — |
| P46 | flat | 3 / 100 % | — | — |
| P47 | flat | 5 / 100 % | — | — |
| P48 | flat | 2 / 15 % | — | — |

**Print-test first** (mechanical.md §11 and §13 step 1): P15 (625-2RS press fit: 0.05 mm interference after the test), P2 (623ZZ press fit), P13 (servo fit: the pocket is 20.4 × 34.4 × 23.5 around the verified 20 × 34 × 23 body; check the four back-face M2 × 6 screws line up at X ±8, Z ±15 from the body centre and that the connectors are clear in the side windows), P34 with a leaf scrap (groove grip), and — added by the CAD agent — a 20 mm slice of P21's mast with the real rail (hole pitch and the 1 mm lip, bom-verified §11 item 7), P16 on the real horn (PCD 12), and P39's deck ring on the real button (C-E3).

## 5. Print plate plan (220 × 220 bed; P21 needs ≥ 190 mm on one axis)

| Plate | Parts | Notes |
|---|---|---|
| 1 | P21 alone (186 × ~110 footprint on its mast face) | diagonal not needed on a 220 bed; 5 walls, slow |
| 2 | P1 (150 × 140 footprint) | FRAME-ONLY: skip for the crown build |
| 3 | P32 + P30 + P31 | all hand-side, 0.12 layers for P30/P31 (print P30/P31 on their own plate if the 0.12 layer height is not wanted on P32) |
| 4 | P33 + P28 + P29 + P47 + P34 ×3 + P46 | hand group, 0.2 layers |
| 5 | P19 + P20 + P26 + P22 + P23 + P24 + P25 + P27 | yoke / float, mixed 100 % infill small parts |
| 6 | P5 + P6 + P7 + P8 + P9 + P10 | FRAME-ONLY: skip for the crown build |
| 7 | P13 + P14 + P15 + P16 + P17 + P18 (+ P11 + P12 only for the frame build) | elbow group; P15 standing |
| 8 | P3 + P4 + P37 + P38 + P39 + P40 | electronics / handheld |
| 9 | P36 ×6 (+ P2 ×2, P41 ×4, P43, P44, P45: FRAME-ONLY) | small parts |
| 10 | P48 + P35 (+ P42 ×2: FRAME-ONLY) | tools (optional until the sessions) |

TPU: 2 bumper pads (P13 lugs), 1 up-stop pad (P24), 2 wedge pads (P42): cut from a 2 mm TPU sheet print (any plate).

## 6. Assembly cross-references

Crown build: the crown holds P13 by its back face (4 × M3 at X ±14, Z 80/104, heads of the servo's M2 × 6 are counterbored flush) and P15 by its outer face (2 × M3 at X 0, Z 70/98, Ø 6.4 holes for ±1.5 mm alignment), 261.5 mm apart and coaxial about the elbow axis; P17/P18 hang under them on two M3 at Z 66. Frame build (FRAME-ONLY parts): P5 under the post, P6 and P7 clamp the post, P9 on the beam with P8 under the spine (post passes through both, C-F5), P11/P12 on the beam ends carrying those same two faces. Arm: P16 on the horn (M2 × 6 only), P19 on P16, P20 on the shoulder screw, P21 between the cheeks through its end plates; rail on the mast against the lips; P23, P24, P22 (two M3 × 30 through the mast), P27 on the mast; MGN9C with P26, P47 in the P28 pocket under the riser arm, P29 on the post. Hand: P30 + boot + P31 under P32 (six M2 × 8), leaves in the P32 root blocks under P34, P33 on P32 (six M2 × 6), seated on P28. Adapter: P1 with the magnet, P2 ×2 on M3 × 16 axles, P3/P4 on the front face (but see C-F7), P45 under the magnet arm, P44 on the reset cord.
