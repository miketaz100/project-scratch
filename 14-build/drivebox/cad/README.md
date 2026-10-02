# DRIVE BOX CAD: SP1 v3

**Project SCRATCH · 14-build/drivebox/cad · 2026-10-02 · rev 1**

## How the sources and STLs relate

- **The `.scad` files are the source of truth.** They use basic primitives only: cube, cylinder, linear_extrude (including twist for the drum helix), offset, polygon, and booleans.
- No OpenSCAD binary exists on the build machine. **`gen_drivebox_stl.py`** mirrors every constant and module under the same names. It rebuilds the solids with manifold3d, writes `stl/*.stl`, and prints each part's bounding box, volume, mass and watertight check.
- If you edit a `.scad` file, make the same edit in the `.py` and re-run it.

**Run:**

```
/private/tmp/claude-501/-Users-michaeltaszycki/97b6a4f1-1d4a-4d86-ac07-7d01cd99e323/scratchpad/cadenv/bin/python gen_drivebox_stl.py   # [--only DB03,DB06]
```

**Result at rev 1: 21/21 STLs are watertight, valid, single-shell manifolds.**

**Checks run on the geometry:**
- A section through a flexure tongue gives 4 separate islands: the tongues touch the plate only at their roots.
- Drum slices show the helical groove cut.

**Selecting a part in OpenSCAD:** set the `PART` variable, either by editing the line at the top of the file or on the command line:

```
openscad -D 'PART="plate"' -o DB03.stl db02_db05_drum_module.scad
```

## Frames

| Frame | Definition | Placement in the case (frame K = inside floor of the base; X along the length from the left inner wall; Y from front (latches) to rear; Z up) |
|---|---|---|
| **D** (drum module) | Deck top surface is z = 0. +x points at the umbilical wall. y runs across. | D origin = K (105, 40, 44) |
| **b** (bulkhead) | x = u: outward normal of the right end wall, u = 0 on the wall's **outside** surface. y = v along the wall. z = w up. | b origin = K (302 + wall, 115, 68) |
| **L** (local) | Each loose part has its own convenient frame. | See the table below. |

The drum-module STLs **(DB02, DB03, DB03b, DB04)** are written in frame D, in their **installed positions**. Load them together in a slicer or viewer to see the assembled module. The bulkhead STLs **(DB06, DB07, DB08)** are likewise written in frame b in installed position.

## Parts

Masses are at 100 % infill. A PETG print with 4 perimeters and 35 % gyroid infill weighs about 55–60 % of that.

| ID | STL | Source (PART) | Material / process | Size x × y × z (mm) | Vol cm³ | Print orientation | Who prints |
|---|---|---|---|---|---|---|---|
| DB01 | DB01_drum.stl | db01_drum.scad | **SLA**, JLC3DP 9600 or JLC Black resin | 30 × 30 × 25.5 | 5.4 | axis vertical, flange down; supports only under the flange; keep supports out of the grooves | **print service OK** |
| DB02 | DB02_deck.stl | db02_db05_drum_module.scad ("deck") | PETG, 4 perimeters, 40 % gyroid (or MJF PA12) | 150 × 140 × 49 | 101.5 | **top face down** (flip in the slicer), legs up; no supports | print service OK |
| DB03 | DB03_floating_plate.stl | … ("plate") | PETG, **100 % infill in the tongues** (modifier), 4 perimeters (or MJF PA12) | 14 × 142 × 28 | 26.2 | lay it on its −x face (x = 100 on the bed); tongues and seat bosses print vertically | **needs iteration, home printer recommended** |
| DB03b | DB03b_floating_plate_4mm_housing.stl | … ("plate4") | same | same | 26.1 | same | same; only if the S0 rig selects the 4 mm SP41 housing |
| DB04 | DB04_hall_bridge.stl | … ("bridge") | PETG | 5 × 114 × 28 | 15.0 | on its −x face | needs iteration, home printer recommended |
| DB05 | DB05_comb.stl | … ("comb") | PETG | 10 × 110 × 22 | 10.8 | on its x = 0 face | print service OK |
| DB05b | DB05b_comb_4mm_housing.stl | … ("comb4") | PETG | same | 10.3 | same | only with SP41 |
| DB06 | DB06_bulkhead.stl | db06_db08_umbilical_block.scad ("bulkhead") | **SLA** (airtight) | 31 × 124 × 50 | 108.5 | mating face (u = 14) **up**, so the face that seals is support-free | **print service OK** |
| DB07 | DB07_plug.stl | … ("plug") | **SLA** (airtight) | 16 × 124 × 50 | 81.5 | mating face (u = 14) **up**, so the O-ring glands stay support-free | **print service OK** |
| DB08 | DB08_inner_clamp.stl | … ("clamp") | PETG | 4 × 100 × 60 | 12.5 | flat | print service OK. **Set WALL_T first** (CONFLICTS C19) |
| DB09 | DB09_hook_plate.stl | db09_db11_mounts.scad ("plate") | PETG, 4 perimeters, 30 % | 216 × 136 × 6 | 136.5 | flat, z = 0 down; needs a 220 × 220 bed | print service OK |
| DB10 | DB10_hook_30.stl | … ("hook30") | PETG, 5 perimeters, 50 % | 42 × 64 × 25 | 19.1 | flat on the profile (z = 0 down), so the layers run along the J | print service OK |
| DB11 | DB11_hook_55.stl | … ("hook55") | same | 67 × 64 × 25 | 22.9 | same | print service OK |
| DB12 | DB12_pegboard.stl | db12_db18_fitout.scad ("peg") | PETG | 100 × 90 × 20 | 40.4 | plate on the bed, flange up | print service OK |
| DB13 | DB13_saddle_pump_D28.stl | … ("saddle28") ×4 | PETG | 36 × 34 × 13.8 | 5.3 | base down | print service OK |
| DB14 | DB14_saddle_bottle_D51.stl | … ("saddle51") ×2 | PETG | 59 × 34 × 21.9 | 10.4 | base down | print service OK |
| DB15 | DB15_hanger_seat.stl | … ("seat") | PETG | 26 × 26 × 14 | 5.9 | nut-trap face down | needs iteration (3 N setting), home printer recommended |
| DB16a | DB16a_clip_nose.stl | … ("clipnose") | PETG | 30 × 28 × 12 | 5.9 | channel face (z = 9) down | same |
| DB16b | DB16b_clip_plain.stl | … ("clipplain") | PETG | 30 × 28 × 9 | 5.2 | channel face down | same |
| DB17 | DB17_vent_baffle.stl | … ("baffle") ×2 | PETG | 62 × 50 × 18 | 10.9 | open face down | print service OK |
| DB18 | DB18_panel_bracket.stl | … ("bracket") ×2 | PETG | 30 × 20 × 30 | 5.1 | on the foot | print service OK |

**SLA order:** DB01 ×4, DB06, DB07 ≈ 212 cm³.
**PETG total:** ≈ 460 cm³ solid, ≈ 330 g printed.

## Key dimensions and fits

Drill every hole marked "clearance" to size after printing.

| Feature | Nominal | Fit |
|---|---|---|
| Drum D-bore | Ø 5.10, flat at 2.10 | sliding fit on the Ø 5 D-shaft; locked by an M3 × 6 grub through a trapped nut |
| Drum pitch radius / groove | R 6.00 / Ø 0.50, pitch 1.0, 5 turns | cable 0.46 mm sits 2/3 deep |
| Index magnet pocket | Ø 3.4 × 2.2 at R 12 | 3 × 2 or 3.18 × 1.59 N52 magnet, CA glued |
| Motor boss / screws | Ø 22.6 / Ø 3.4 on 31 × 31 | NEMA 17 |
| Rod holes (posts) | Ø 3.9 | press fit for Ø 4 h6 rod |
| LM4UU bores | Ø 8.1 × 12 | slip fit + CA |
| Ferrule seat | Ø 2.5 × 5 (DB03b: Ø 5.2) | 3/32 in brass ferrule OD 2.38 (SP41 end cap OD ≈ 5 [VERIFY]) |
| Release slot | 0.8 wide | the 0.46 mm cable lifts out |
| Heat-set inserts (DB03) | Ø 4.0 × 6 | M3 × 5.7 brass insert |
| M5 ports (DB06/DB07) | Ø 4.2 tap drill × 8 | tap M5 × 0.8; KQ2H23-M5A seals on its gasket face, not on the thread |
| O-ring gland (DB07) | ID 3.0 / OD 5.6 / depth 0.75 | 3 × 1 mm NBR70 at 25 % squeeze |
| Dowels | DB06 Ø 2.95 (press), DB07 Ø 3.10 (slide) | Ø 3 × 12 stainless |
| Thumb screws | Ø 4.5 through; M4 nut slot 7.2 AF × 3.4 from the top of DB06 | M4 × 25 knurled |
| 1/4-20 nut trap (DB15) | 11.3 AF × 6 | 7/16 in hex nut, CA |

## JLC3DP ordering notes (print service)

- **SLA, 9600 resin** (or JLC Black):
  - tolerance ±0.2 mm under 100 mm, ±0.3 % over;
  - upload the STLs as they are (units mm);
  - choose "no surface finish", and **ask for no supports on the faces named above**;
  - holes come out ≈ 0.1 mm small: ream with the drill sizes in the fit table.
- **MJF PA12** (only if there is no home printer):
  - tolerance ±0.3 mm or ±0.4 %;
  - holes under Ø 4 come out small: drill them;
  - heat-set inserts work in PA12 at 230 °C;
  - the DB03 tongues come out ≈ 15 % softer (≈ 14 N/mm);
  - **do not use MJF for DB06/DB07**: it is not reliably airtight at 1–3 mm walls.
- Order DB01 with one spare. Inspect the grooves with a 10× loupe: a continuous helix with no flash.

## Interfaces owned here (SYSTEM-SPEC-v3 §5)

| ID | Interface | Geometry | Notes |
|---|---|---|---|
| **M16** | Box mounting | Hook plate DB09 on the lid's outside: 4 × M5, pattern 200 × 120 (holes at ±100, ±60). J-hooks on 2 × M5 at x ±60, y 30/55. Strap slots 6 × 42 at x ±82. Four sorbothane feet on the base. | CONFLICTS C16 |
| **M17** | Drum module | Drums on 5 mm D-shafts with a grub on the flat. Stop plate on two Ø 4 rods with ≈ 4.5 N total spring force at W (CONFLICTS C2). Hall index magnets in the drum flanges at R 12. Module base = deck top. | — |
| **A / B / P** | Box ports | DB06/DB07 ports at v −16 / 0 / +16, w +8; KQ2H23-M5A both sides; O-ring face seal | — |
| **T1–T4** | Tendons | Seats Ø 2.5 (or 5.2) at D (x 109, y 29/75/121, z 14). Row-2 seats at z 22 are the pad-2 provision. Housing slot 52 × 8 through DB06/DB07. Comb DB05. | — |

## Not modelled here

- The plywood tray, left panel and E-shelf: these are cut from a dimension table (drivebox.md §2.3).
- The case itself.
- Bought parts.
