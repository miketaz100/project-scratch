# S0 CAD: every printed part for S0a and S0b

**Project SCRATCH · 14-build/S0/cad · S0 kit engineer · 2026-10-02**

Units are mm. Every STL in `stl/` is already in its **print orientation**, sitting on z = 0: open it in the slicer and print. The `.scad` files model the parts in their working frame. Set `PRINT = true` in `dish_bench.scad` to see each part in print orientation.

## Files

| File | What it is |
|---|---|
| `s0_lib.scad` | Shared constants and helpers. Names match `gen_s0_stl.py` one-for-one. |
| `dish_bench.scad` | S0a dish bench, parts D01–D16. Set `PART = "..."`. `PART = "assembly"` shows the bench on the ball. |
| `helmet_test.scad` | H01 hinge pad for the helmet / hinge / coin-bag test |
| `tendon_rig.scad` | S0b tendon ink rig, parts T01–T06 |
| `pocket_cavity.scad`, `template_paths.scad` | **Generated** by `dish_kinematics.py`: the dish pocket ceiling as a polyhedron, and the corrected template stylus paths. Do not edit by hand. |
| `dish_kinematics.py` | Dish profile, block pose solver, template paths, predicted chords, lifts and angles. Also writes `pocket_mesh.json` and `dish_geometry.json`. |
| `gen_s0_stl.py` | Builds every STL with manifold3d (no OpenSCAD binary here), checks watertightness, prints sizes and volumes |
| `check_s0_clearance.py` | Interference sweep: block + nose plate + C-arm + balls + styli against the deck and templates, over 24 headings × full travel and every template path. Also checks the lift elastic through the well. |
| `stl/` | 23 STLs, **all watertight** (checked 2026-10-02) |

**Regenerate.** Run `python dish_kinematics.py`, then `python gen_s0_stl.py`, then `python check_s0_clearance.py`, using a Python environment with numpy, trimesh and manifold3d.

**Last run** (2026-10-02):
- 23/23 STLs watertight.
- Zero interference volume at every pose and on every template.
- The 6 mm balls touch the dish ceiling at rest (raising them 0.3 mm cuts the deck: sanity check passed).
- The elastic clears the well, apart from a 0.3 mm³ kiss of the rim at |d| = 16.5.

## Dish geometry (what is built, and why)

**The frozen numbers (SYSTEM-SPEC-v3 §4.2) are built literally.**
- The balls run on a concentric sphere R 160 (ball centres on R 157) about the ball / scalp centre, for |d| ≤ 7 mm.
- The inner rim is 34° to |d| 13.7 (+4.52 mm).
- The outer rim is 50° to |d| 17 (+8.45 mm).
- A 70° stop wall runs to 18.5.
- d is the offset of each ball from its home, measured **at the dish**.

**The rim lifts along the pad axis as a function of each ball's lateral offset ("z-lift" model).** In the sphere zone, rotation about the ball centre therefore moves all three balls equally, and the rim adds no extra tilt. Lifting along each pocket's own radial axis was modelled first: it added ≈ 3° of tilt and cost the leading nail ≈ 2 mm of lift.

**Each pocket ceiling is the exact envelope of the 6 mm ball swept over that surface.**

**The balls sit at R 26, not R 22.** At R 22 the three pockets overlap and leave no room for the lift elastic. See `../CONFLICTS.md` #3.

**Predicted bench numbers** (`dish_kinematics.py`, on a true R 85 ball, nail N20 = 2.0 mm reserve):

| Quantity | Predicted | S0 pass line | Note |
|---|---|---|---|
| Block rise / tilt at \|d\| 16.5 | 7.8 mm / 6.6° | — | |
| Contact length at the dish (block travel with a nail down) | 19.8–19.9 mm | — | the spec's "chord 17–24" in dish units |
| **Ink trace on the ball (what the scalp feels)** | **10.2–10.4 mm** | ≥ 15 mm | **expected FAIL: CONFLICTS #1** |
| Clearance at the turnaround, \|d\| 16.5 | 5.4–5.8 (N20); 4.4–4.8 (N30); 3.9–4.3 (N35) | ≥ 5 mm | N20 passes |
| Landing angle at the nail, relative to the ball | 48–62° | ≤ 35° | **expected FAIL: CONFLICTS #1** |
| Stylus vertical travel | −1.6 … +10.2 mm | — | groove 17 deep, stylus engaged 14 at home |

## Parts, quantities, materials, settings

**General FDM settings** (PLA or PETG): 0.4 mm nozzle, **0.2 mm layers**, **3 walls**, 4 top / 4 bottom layers, **15–20 % gyroid infill**, no supports unless the table says so.

| STL | Qty | Material | Print orientation (as exported) | Notes | Print service? |
|---|---|---|---|---|---|
| D01_dish_deck | 1 | PLA or PETG | upside down: top plate on the bed, legs up | The dish ceilings face up, so they print clean with no supports. **0.12 mm layers** if your slicer has variable layer height (smoother 34°/50° rims). Sand the pocket ceilings with 400 grit, then wax them or spray dry PTFE lube (guide step D7). The spec's PTFE film does not lie flat in these small curved pockets. | **OK** (FDM PLA). Rims are steps of 0.2 mm either way; the PTFE film covers them. |
| D02_dish_block | 1 | PETG or PLA | upright | The 45° chamfer under the top plate prints without support. Ball sockets face up. | **OK** |
| D03_nose_plate | 1 | PETG, or resin | flat | The nail guide bores are Ø 4.7. If a nail sticks, run a **3/16 in (4.76 mm) drill bit** through by hand. | **OK**. Resin is better: smoother bores. |
| D04_plunger | 4 (1 spare) | resin (SLA), or PETG at 0.12 mm | cup up | Ø 3.1 magnet pocket in the bottom face | **Resin via service recommended** |
| D05_seat_disc | 4 | any | flat | | OK |
| D06_nail_N20_reserve2 | 4 | **resin (SLA)**, tough or standard grey or orange | tip up | **2.0 mm** reserve on a true R 85 ball. One ring near the top. | **Service: JLC3DP SLA** (see below) |
| D07_nail_N30_reserve3 | 4 | resin | tip up | 3.0 mm reserve. Two rings. **Use these on the 7 in (R 89) ball**, where they behave like N20 on R 85. | Service |
| D16_nail_N35_reserve3p5 | 3 | resin | tip up | 3.5 mm reserve, the spec's worst case. Three rings. **Use these on Michael's crown** if his crown is flatter than R 85. | Service |
| D08_c_arm | 1 | PETG (stiffer) or PLA | on its side | | **OK** |
| D09 / D10 / D11 templates | 1 each | PLA | base down | Grooves are 3.4 wide × 17 deep. Use **0.16 mm layers** for cleaner groove walls. Notches on the +X edge: 1 = line star, 2 = D-path, 3 = circle. | **OK** |
| D12_skid_ring_hand_rake | 1 | PETG or PLA | ring on the bed, legs up | Feet are Ø 8 balls | OK |
| D13_ball_cradle | 1 | PLA | flat | | OK. Or use a roll of tape. |
| D14_side_mock_70x150 | 1 | PLA | skirt on the bed, dome up | **Optional.** Only for the side-of-head geometry check. | OK |
| D15_lift_gauge | 1 | PLA | flat | Steps of 2 / 3 / 4 / 5 / 6 / 7 mm. **Check them with calipers.** | OK |
| H01_hinge_pad | 2 | PETG or PLA | flange top on the bed | L-bracket. The base goes on the helmet side; the flange takes the Southco E6 leaf studs (15.1 mm pitch, Ø 5.5 holes), so the hinge pin points ear-to-ear. | OK. Or a 1 × 1 in aluminum angle bracket |
| T01_drum | 3 | resin (SLA) or PETG at 0.12 mm | hub down | Ø 12 drum with two helical grooves at 1 mm pitch. **CF Stage A**: reprint in SLA. D-bore for the 5 mm shaft, flat [VERIFY]. | Resin via service is better |
| T02_motor_table | 3 | PETG or PLA | feet down | The motor hangs under the table, shaft up, held by 4 × M3 × 6 | OK |
| T03_stop_block | 3 | PETG or PLA | flange down | Ø 5.2 housing seat | OK |
| T04_housing_sleeve | 3 | PETG or resin | upright | Adapter for the 2 mm thin housing (optional housing B) | OK |
| T05_rig_deck | 1 | PLA | ring down | Housing stops at R 60 | OK |
| T06_pen_plate | 1 | PLA | plate top on the bed | Three marble cups, Ø 12.2 pen bore, M3 cable posts at R 22 | OK |

## Ordering from a print service (no printer)

**JLC3DP** (jlc3dp.com): upload the STLs and choose the process and material per part.
- **FDM PLA** for everything marked OK. Ask for 0.2 mm layers and 20 % infill.
- **SLA resin** (their standard 9000R, or a tough resin) for:
  - nails: D06 × 4, D07 × 4, D16 × 3;
  - plungers: D04 × 4;
  - drums: T01 × 3 (S0b).
- **Orientation for resin parts.** Nails tip up, supports only on the top end. The R 0.4 tip edge must not carry support marks.
- **Tolerances.** Note "holes as modelled; no shrink compensation" in the order remark. All fits were sized for normal printer tolerances:
  - stem 4.5 in a 4.7 bore;
  - plunger 6.0 in a 6.4 bore;
  - magnet pocket 3.1 for a 3.0 magnet.
- **Expect.** Parts from ≈ $0.30 (SLA) / $1 (FDM) each, 2–3 days to build, DHL 3–7 days, and **≈ 40 % US duty** collected at checkout [cited, JLC3DP FAQ, 2026-03-19]. Rough total for S0a ≈ $55–85 [est].
- **Order S0a and the S0b drums in one go?** No. Order the drums only after S0a is GO (the staging rule).

## Which parts need a home printer (iteration likely)

Only the **deck rims**, and only if the 34°/50° rims chatter or stick after PTFE.
- The fix is a smoother ceiling: 0.12 mm layers, or a resin deck at ≈ $25–40 [est].
- Everything else is "print once".
