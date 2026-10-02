# PAD CAD — sources, STLs, print and ordering notes

**Project SCRATCH · 14-build/pad/cad · PAD engineer · 2026-10-02**

## 1. What is here

| File | What |
|---|---|
| `lib_pad.scad` | Source of truth: every constant and one module per printed part (basic primitives only). |
| `pdNN_*.scad` | One wrapper per part (`include <lib_pad.scad>` + one call). Open in OpenSCAD and export STL. |
| `pad_assembly.scad` | The whole pad at the home pose. |
| `pockets_data.scad` | GENERATED: the three pocket-ceiling height fields used by the deck polyhedra. Do not edit. |
| `gen_pad_stl.py` | Rebuilds every STL with manifold3d (same constants and modules), prints bbox, volume, mass and watertightness; writes `mass_by_part.csv`, `shadowgraph_nail.svg`, `pockets_data.scad`. |
| `pad_geom.py` | Dish kinematics, gate on a line, head-shape table, skid-adjuster table → `pad_geom_report1.txt`. |
| `pad_geom2.py` | Dome pockets (`pockets.npz`), block-to-deck clearance, C8 sweep, lift springs, yaw → `pad_geom_report2.txt`. |
| `check_assembly.py` | Pairwise STL interference at home, plus the moving block swept through 145 poses against every static part. |
| `stl/` | 17 STLs (PD01–PD19, no PD03/PD04), all watertight (`gen_report.txt`). |
| `shadowgraph_nail.svg` | Nail template at 10:1 (tip) and 1:1; print at 100 %. |
| `mass_by_part.csv` | Masses by part. |

**No OpenSCAD binary was available on the build machine.** The STLs come from `gen_pad_stl.py`. The SCAD files were checked for bracket balance and written to mirror the Python line for line.

Known cosmetic difference: `seg_cyl()` in SCAD is a hull of two spheres (round ends); in Python it is a plain cylinder. It is used only for gallery channels, lift hooks and skirt-frame struts.

## 2. Parts, process and where to get them printed

All parts are modelled **in their installed position** in pad frame P (z = height above the scalp; the block at home). Rotate them in the slicer per the "orientation" column.

| STL | Qty to order | Process | Orientation | Notes | Who prints |
|---|---|---|---|---|---|
| PD01_deck | 1 (+1 spare at Stage B) | SLA, standard resin | top face down (pockets up) | supports on the flat top only, never in the pockets; pockets are the dish surfaces | **JLC3DP SLA** |
| PD02_skirt_frame | 1 | MJF PA12 | as modelled | — | **JLC3DP MJF** |
| PD05_floor_plate | 1 (+1) | SLA tough | underside down | ream the bush bores after pressing | JLC3DP SLA |
| PD06_cartridge | 8 | SLA tough | upright, top up, no internal supports | bore Ø 7.0 is a working surface | JLC3DP SLA |
| PD07_gallery_plate | 1 (+1) | SLA standard | plate face up | ask for "internal channels, please clean"; flush with IPA through each port | JLC3DP SLA |
| PD08_skirt_plate | 2 | MJF PA12 | flat | bead-blast, then seal the underside (thin CA, sand 1500) | JLC3DP MJF |
| PD09_piston | 8 | SLA tough | flat | or turn from Ø 6 POM rod | JLC3DP SLA |
| PD10_yoke | 2 | SLA | flat | — | JLC3DP SLA |
| PD11_stop_block | 3 (+2) | PETG / MJF | on its side | iterate the spring bore fit | **home printer recommended** |
| PD12_skid_stem | 3 (+1) | PETG 100 % or MJF | upright | slides in Ø 6.3 | home or MJF |
| PD13_skid_foot | 3 (+1) | SLA | cap up | polish 1500 grit; scalp contact | JLC3DP SLA |
| PD14_skid_knob | 3 | PETG | flat | — | home or MJF |
| PD15_nail_reference | 18 | **CNC turning, POM-C** | — | send the §6.1 table of pad.md and this STL to the turning service; red POM if offered | JLCCNC / PCBWay CNC |
| PD16_hang_cup | 2 | PETG | flat | label "HOLD 11", "DROP 20" | home or MJF |
| PD17_shadow_card | 1 | PETG, black | flat | — | home or MJF |
| PD18_skid_gauge | 1 | PETG | flat | check the 0.5 mm steps with calipers | home or MJF |
| PD19_s0_pocket | 1 | SLA | flange down | S0 dish bench: one pocket (dome 30°) | JLC3DP SLA |

**Ordering notes (JLC3DP):**
- **Resin:** "8001 / Imagine Black" class for the deck and gallery plate; "9600 / tough" class for the cartridges, floor plate and pistons.
- **Tolerance class:** standard (±0.1–0.2). The working diameters are reamed or checked as described in pad.md §11.
- **MJF PA12:** black dye.
- **Batching:** order all SLA parts in one batch, Stage A, after the S0 gate passes.
- **Nails:** request a turning quote for 18 pieces in POM-C: Ø 3.92 −0.03, Ra 0.4 on the land, red if possible, with the dowel hole.

**Home-printer settings (PETG):**
- 0.4 nozzle, 0.12 mm layers, 5 walls, 40 % gyroid (100 % for stems).
- 240 °C / 80 °C bed. Dry the filament first.
- Heat-set inserts: Ø 4.0 holes, iron at 230 °C.

**SLA post-processing:**
- IPA wash 2 × 3 min, UV cure 10 min.
- Flush every internal channel with IPA from a syringe before curing.

## 3. Tolerances that matter

| Feature | Value | How it is controlled |
|---|---|---|
| PTFE bush bores | Ø 5.95 | press-fit 6.0 tube; ream inside with the nail |
| Piston bore | Ø 7.0 +0.05 | as printed; rolling sleeve tolerates ±0.1 |
| Cartridge sockets | Ø 9.55 on a Ø 9.4 cartridge | ±0.05; pin position ±0.1 |
| Nail land | Ø 3.92 −0.03 | turning service; checked on the PD17 slot pair |
| Pocket ceilings | as printed ±0.1 | sanded 1000/1500; PTFE film; V-D3 test |
| Ball sockets | Ø 6.25 (ball 6.35) | press-fit; lip 0.4 above the equator |
| Magnet pockets | Ø 3.25 / Ø 6.45 | CA |

## 4. Regenerating

```
PY=/private/tmp/claude-501/-Users-michaeltaszycki/97b6a4f1-1d4a-4d86-ac07-7d01cd99e323/scratchpad/cadenv/bin/python
$PY pad_geom.py  > pad_geom_report1.txt   # dish, gate, head shapes (≈ 1 min)
$PY pad_geom2.py > pad_geom_report2.txt   # pockets.npz, clearances, lift, yaw (≈ 1 min)
$PY gen_pad_stl.py > gen_report.txt       # STLs, masses, pockets_data.scad, SVG (≈ 5 s)
$PY check_assembly.py                     # interference at home and swept (≈ 1 min)
```

Change a dish number in `pad_geom.py`, then run all four. Change a part dimension in **both** `lib_pad.scad` and `gen_pad_stl.py` (same name).

## 5. S0 single-pocket bench (PD19)

1. Bolt PD19 flange-up under a sheet of 6 mm plywood with a 66 mm hole (4 × M3).
2. Glue one 1/4 in PTFE ball on a stalk to a sliding plate. Spring the plate up against the pocket with a 0.3 N elastic.
3. Guide the plate by hand through printed templates (line, offset circle).
4. Measure:
   - ball height versus travel (dial indicator or caliper depth rod) against the `pad_geom.py` table, 0.2 mm agreement;
   - smoothness and noise (phone accelerometer at 140 mm/s, V-D3).

This checks the pocket surface and the printer. The full gate (rake, landing, lift) needs the Stage A block on the R 85 ball.

## 6. Cover band (not printed)

- 0.5 mm polypropylene sheet (a document folder), or 0.25 mm PET for the diet. It wraps the skirt frame outside the struts.
- Developed shape: an annular sector with inner radius **468.7 mm**, outer radius **512.5 mm**, angle **41.1°**, plus 10 mm of overlap. Mark it with a string compass on the floor.
- Cut two windows 30 × 22 mm for the PIN tubes, at 108° and 252°. Centre each 26 mm above the band's lower edge (z 62 in the pad frame).
- Fix with the frame struts outside and 6 dots of CA.
