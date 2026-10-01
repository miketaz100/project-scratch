# SP1 tips, TM1 mount and Stage-0 hand wand: CAD folder

Project SCRATCH, 05-engineering/cad/tips, tip lead, 2026-10-01. Units are mm unless stated.
Governing documents: `01-foundations/tip-interface.md` (SP1-TM1 and the tip family),
`05-engineering/DESIGN-FREEZE.md` §1.7, §1.8 and §3 Stage 0, `01-foundations/safety-requirements.md`
(red line 11: tip edge radius 0.4 mm minimum; tape test), `05-engineering/test-protocols.md` (L6, L8, L9 to L12, §Q5).
The engineering write-up for everything in this folder is `05-engineering/tips.md`.

## 1. What each file is

| File | What it is | Prints / makes |
|---|---|---|
| `tm1_tang_lib.scad` | Shared SP1-TM1 library: tang (10 x 4 x 12 mm, 2 x 45° key chamfer on the +X+Y corner), shoulder cone and 14 x 9 mm band, the pocket negative (10.3 x 4.3 x 12.5 mm, N52 6 x 2 mm magnet recess), the B45-family blade module. Renders nothing when included. | nothing (include only) |
| `tip_W.scad` | Tip W, symmetric wedge, 8 mm edge, two 45.7° faces, R 0.4 mm apex, R 9 mm crown. DEFAULT bidirectional tip. | 1 PETG part |
| `tip_B45.scad` | Tip B45, 45° nail-mimic plate 1.0 mm thick, 8 mm edge, R 0.5 mm. `BLADE_MODE = "slot"` turns it into a carrier for a 1.0 mm sheet blade. | 1 PETG part |
| `tip_B45_12.scad` | Tip B45-12, as B45 with a 12 mm edge (width variable). | 1 PETG part |
| `tip_A45.scad` | Tip A45 carrier (default slot mode) for a 0.8 mm nylon sheet blade filed to R 0.3 mm. GATED (below red line 11). | PETG carrier + nylon blade |
| `tip_E_carrier.scad` | Tip E, B45 geometry on a TPU 90A pulp pad. `PART = "carrier" / "pad" / "blade" / "assembly"`. | PETG carrier, TPU pad, nylon blade |
| `tip_H_ball.scad` | Tip H, 3 mm steel ball on a drafted cone: the massager CONTROL tip. | PETG part + 3 mm ball |
| `tip_P_carrier.scad` | Tip P, carrier with a convex R 8.5 mm bed for a trimmed press-on nail. | PETG carrier + ABS nail(s) |
| `paddle_with_pocket.scad` | 25 mm drafted paddle (10° draft on all four faces, `DRAFT_Y = 10` since DESIGN-FREEZE-ADDENDUM-1 D3) ending in a TM1 pocket, clamp for the 0.3 x 12.7 mm feeler leaf, clamp bar, TPU seam sleeve. `PART = "paddle" / "bar" / "sleeve" / "assembly"`. `RISER` (default 0) inserts a straight 22.8 x 17.8 mm section above z = 25 before the root transition; the SP1 centre paddle is `RISER = 9` (its leaf clamps 9 mm higher and crosses over the left paddle, mechanical.md §8.2). Shared by the SP1 hand and the wand. | PETG paddle and bar, TPU sleeve |
| `hand_wand_handle.scad` | Stage-0 hand wand: 150 mm grip + 30 mm clamp block for one end of the feeler leaf. `PART = "handle" / "bar" / "assembly"`. | PETG (or PLA) handle and bar |
| `gen_tips_stl.py` | Python STL generator (no OpenSCAD needed). Mirrors the SCAD files; parameter names match. | `stl/*.stl` |
| `stl/` | Generated meshes, in the MODEL frame (rotate in the slicer per §3). | |

Paddle STLs and quantities for the SP1 hand (mechanical.md §11, T1 to T4) and the wand:

| STL | SCAD setting | Qty SP1 hand | Qty wand | Leaf floor (z) | Leaf floor to W/B45 edge |
|---|---|---|---|---|---|
| `paddle_with_pocket.stl` | `RISER = 0` (default) | 2 (outer nails L, R) | 1 (+1 spare) | 31.5 mm | 44.0 mm |
| `paddle_with_pocket_riser9.stl` | `RISER = 9` | 1 (centre nail C) | 0 | 40.5 mm | 53.0 mm |
| `paddle_clamp_bar.stl` | `PART = "bar"` | 3 | 1 | | |
| `tm1_seam_sleeve.stl` | `PART = "sleeve"` | 3 (+ spares) | 1 (+ spare) | | |

The two paddles are identical below z = 25 (nose, pocket, magnet recess, drafted body, the section at the knuckle plate), so every tip and sleeve fits both.

Frame used in every file: +Z into the pocket (toward the leaf), -Z toward the scalp, X = stroke, Y = across the stroke. Origin = centre of the pocket-mouth plane. The working edge of W, B45, B45-12 and A45 lies 12.5 mm below the mouth.

## 2. Regenerating the STLs

The SCAD files are the source of truth. There is no OpenSCAD binary on the build machine, so the meshes come from the Python mirror:

```
cd 05-engineering/cad/tips
/tmp/claude-0/-home-user-ai-social/a9d4d996-bfe2-5b1b-8c54-ae462b273760/scratchpad/cadenv/bin/python gen_tips_stl.py
```

Any Python 3.10+ with `numpy`, `trimesh` (5.x) and `manifold3d` works (`pip install numpy trimesh manifold3d`); scipy is not needed (hulls use manifold3d). The script writes 15 STLs, checks that each is watertight and that its bounding box matches a hand-derived expectation within 0.06 mm, checks the paddle sections at z = 25 (and, on the riser paddle, at z 29.5 and 33.9) are 22.82 x 17.82 mm and that each leaf floor sits where it should (31.5 / 40.5 mm), prints the table below and exits non-zero on any failure. If you change a SCAD parameter, change the same-named constant in `gen_tips_stl.py` (and its `EXPECTED` row if the envelope moves). With OpenSCAD installed you can export directly instead, e.g. `openscad -o stl/tip_W.stl tip_W.scad` or `openscad -D 'PART="pad"' -o stl/tip_E_pad.stl tip_E_carrier.scad`, and for the centre paddle `openscad -D 'RISER=9' -o stl/paddle_with_pocket_riser9.stl paddle_with_pocket.scad`.

Output of the 2026-10-01 run (regenerated after DESIGN-FREEZE-ADDENDUM-1: `DRAFT_Y` 5 to 10 changed the paddle and the seam sleeve, the riser paddle is new; every other STL has the same bounding box and volume as before):

| File | bbox X x Y x Z (mm) | z range (mm) | volume (mm³) | watertight |
|---|---|---|---|---|
| tip_W.stl | 14.00 x 9.00 x 24.50 | -12.50 to 12.00 | 1428.8 | yes |
| tip_B45.stl | 14.00 x 9.00 x 24.50 | -12.50 to 12.00 | 1299.2 | yes |
| tip_B45_12.stl | 14.00 x 12.00 x 24.50 | -12.50 to 12.00 | 1335.2 | yes |
| tip_A45.stl (carrier) | 14.00 x 9.00 x 21.67 | -9.67 to 12.00 | 1227.4 | yes |
| tip_H_ball.stl (without ball) | 14.00 x 9.00 x 23.00 | -11.00 to 12.00 | 1326.6 | yes |
| tip_E_carrier.stl | 14.00 x 9.00 x 20.51 | -8.51 to 12.00 | 1226.1 | yes |
| tip_E_pad.stl | 10.00 x 10.00 x 7.84 | -14.50 to -6.66 | 493.2 | yes |
| tip_E_blade.stl (blank) | 8.00 x 9.00 x 1.00 | 0 to 1.00 | 68.2 | yes |
| tip_P_carrier.stl | 14.00 x 9.00 x 23.50 | -11.50 to 12.00 | 1440.7 | yes |
| paddle_with_pocket.stl | 28.00 x 17.82 x 35.00 | 0 to 35.00 | 8814.8 | yes |
| paddle_with_pocket_riser9.stl | 28.00 x 17.82 x 44.00 | 0 to 44.00 | 12465.5 | yes |
| paddle_clamp_bar.stl | 24.00 x 8.00 x 3.20 | 0 to 3.20 | 531.2 | yes |
| tm1_seam_sleeve.stl | 15.86 x 10.86 x 8.50 | -5.50 to 3.00 | 352.4 | yes |
| hand_wand_handle.stl | 28.00 x 180.00 x 16.00 | 0 to 16.00 | 63237.3 | yes |
| hand_wand_clamp_bar.stl | 24.00 x 24.00 x 3.20 | 0 to 3.20 | 1650.9 | yes |

## 3. Print settings per part

All tips in ONE bright colour of PETG (orange or yellow): fragments must be visible in dark hair, and a colour difference between tips would break the blinding (§5). PLA never touches the scalp.

| Part | Material | Layer | Orientation on the bed | Walls / infill | Supports | Notes |
|---|---|---|---|---|---|---|
| tip_W, tip_B45, tip_B45_12 | PETG | 0.10 mm | ON ITS SIDE: model Y vertical (rotate 90° about X), band -Y face on the bed. The edge line then runs up the print and its cross-section is traced by the perimeters, so there is no layer staircase across the edge, and the plate bends in-plane rather than across layer bonds | 3 perimeters, 100 % | under the tang (2.5 mm gap) and, for B45-12, under the band (1.5 mm); support Z gap 0.2 mm; nothing on the working faces | slow outer wall (20 mm/s), seam on the tang end, not on the edge; 0.4 mm nozzle |
| tip_A45, tip_P_carrier, tip_E_carrier, tip_H_ball | PETG | 0.10 mm | tang DOWN, working end up | 3 perimeters, 100 % | none (cone 39° and 45° overhangs, bonding faces face up) | carriers: the edge is sheet stock, so orientation does not shape it |
| tip_E_pad | TPU 90A | 0.20 mm | lying on a Y face (the dovetail and 45° chamfer are then in the print plane) | 3 perimeters, 100 % | none | 15 to 20 mm/s, direct drive |
| tip_E_blade | 1.0 mm nylon sheet or pick | | print the STL flat in any filament only as a scribing template | | | do not use a flat-printed blade at the scalp: its edge would be a layer staircase |
| paddle_with_pocket, paddle_with_pocket_riser9 | PETG | 0.20 mm (0.16 for a crisper pocket) | NOSE UP, root block on the bed | SP1 hand: 2 perimeters, 10 % gyroid, with a slicer modifier giving 4 perimeters around the two screw holes (mechanical.md §8.9, float mass budget). Wand: 4 perimeters, 30 % | none (window floor and leaf slots are 8.4 and 12.9 mm bridges; going up the print the 3 mm transition flares out in Y by 1.9 mm per side, 32° from vertical, printable) | PAUSE at print height 23.1 mm (`RISER = 0`) or 32.1 mm (`RISER = 9`), model z 11.9 in both, and drop the N52 6 x 2 magnet into the Ø 6.2 recess with a dot of CA, any polarity; check in the slicer preview that the next layer starts to roof the recess. Mark the riser paddle (it is 9 mm taller) "C" on its root block |
| paddle_clamp_bar, hand_wand_clamp_bar | PETG | 0.20 mm | groove side up, as modelled | 100 % | none | |
| tm1_seam_sleeve | TPU 90A | 0.20 mm | standing, bottom (z -5.5) end on the bed | 2 perimeters (0.8 mm wall) | none | |
| hand_wand_handle | PETG or PLA (never touches hair) | 0.20 to 0.28 mm | flat, window up, as modelled | 3 perimeters, 15 % | none (the leaf slot ceiling is a 12.9 mm bridge) | |

Fasteners: M3 x 8 socket or button head, thread-forming into the 2.6 mm holes (set `SCREW_HOLE_D = 4.0` for heat-set inserts). Two per paddle bar, four per wand bar. On the SP1 hand use aluminium M3 x 8 at 0.3 N·m (mechanical.md §8.6, mass budget); the M2 screws in mechanical.md are for the palm-side root clamp bars (P34), not the paddle.

## 4. Post-processing: edge radius control

The red line is R 0.4 mm minimum for any tip used in a first human session (W 0.4, B45 and B45-12 0.5, E 0.5, P 0.4 to 0.5). A45 (R 0.3) is gated. Work in this order; the full rationale is in tips.md §6.

1. **Clean up.** Remove supports, brim and stringing. Knock the seam zit off with a fresh blade, never on the edge itself. Round the plan-form corners of every edge to R 1.5 mm with a nail file (180 then 240 grit).
2. **Shape the radius.** Wrap 400-grit wet-and-dry around a flat stick. Stroke ALONG the edge (in Y) while rolling the stick over the apex through the full included angle (90° for W; 180° over the 1.0 mm plate end for B45, so the end becomes one full half-round tangent to both faces). A flat with two broken corners is two R 0.15 mm edges, not one R 0.5 mm edge: it fails.
3. **Refine and polish.** Same rolling stroke with 600, then 1000, then 2000 grit, wet. Target surface Ra below 1 µm (no visible scratches at 10x). PETG and the acrylic/ABS press-on may get one optional 1 s pass of a lighter flame for the last micro-burrs; do not dwell. Nylon (A45, E blades): no flame, finish with plastic polish.
4. **Loupe check (radius).** Hold the tip edge-on beside drill-bit shanks on a back-lit white card under the 10x loupe: a 0.8 mm shank is R 0.4, a 1.0 mm shank is R 0.5, a 0.6 mm shank is R 0.3. The edge silhouette must be at least as round as its reference shank (W: 0.8 mm, B45/B45-12/E: 1.0 mm, P: 0.8 mm). Back it up with a phone macro photo next to a ruler and keep the photo with the tip record. Sharper than the reference: sand again. Never sand a tip sharper to "hit" a number.
5. **Burr check.** Drag a cotton ball along the edge both ways: any fibre that snags marks a burr. Then the back of your hand at about 1 N.
6. **UL 1439-style tape test (test-protocols L9).** 10 mm rod wrapped with 3 layers of 50 µm polyester or PTFE tape. Tip in the holder on the hand wand; press at 1.0 N, then 2.4 N (kitchen scale under the rod); slide 50 mm along the rod at about 50 mm/s, three passes each direction, both edge senses for the 45° tips, then across the corners. Inspect under the loupe. Pass: no cut through any layer at 2.4 N. A45 must pass at 2.4 N too or it stays gated. Re-test after 10 sessions or after any drop.
7. **Record** the measured radius, test date and result against the tip's code on the key card (§5).

Assembly notes per tip: steel keeper (6 x 1 mm disc with two flats filed to 3.9 mm, or a 6.0 x 3.9 x 1.0 mm slug from 1 mm mild steel) bonded with epoxy or gel CA into the tang-end notch, flush with the end. H: CA the 3 mm ball into the cup. A45: cut a Dunlop nylon 0.88 mm pick (or 0.8 mm nylon sheet) to 8 x 9 mm with a convex R 9 end, file the edge first, then CA the sheet onto the 45° carrier face with its top butted against the band. E: slide the TPU pad into the dovetail along Y with a drop of CA, bond the 1.0 mm nylon blade on the 45° face with 2 mm overhang. P: see tips.md §5.4 (two nested nails for R 0.4 or more). Seam sleeve: stretch over the paddle nose, bottom flush with the band bottom when a tip is seated; one dot of gel CA at the sleeve's top rim keeps it on the nose when a tip is pulled. The sleeve is now drawn for the 10° nose; a sleeve printed for the old 5° paddle is 0.5 mm narrower in Y at its top and must not be used on a new paddle (it would ride up). SP1 hand: after the paddles are clamped, the knuckle-plate boot (one slack 0.25 mm silicone membrane over the shared slot, mechanical.md §8.7, ADDENDUM-1 D4) is bonded to each paddle at z 26 to 28 with a 2 mm bead of silicone adhesive; keep that band of the paddle free of CA, varnish and slicer seam (put the seam on a +X or -X corner).

## 5. Blinding codes and the tip box (test-protocols §Q5)

- **Code.** Every tip gets a random two-letter code. Draw the letters with a phone random generator from the alphabet without W, B, A, E, H and P (so no code spells a tip name), and never reuse a code.
- **Where.** On the tang's plain -Y face (the 10 x 12 mm face away from the key chamfer), which is inside the pocket and invisible while the tip is installed. Write 3 mm letters with a 0.3 mm permanent marker, then one thin coat of clear nail varnish. No stickers or labels: the pocket has only 0.15 mm clearance per side and a label can jam or peel off inside it. Check the tang still slides home freely after the varnish dries.
- **Duplicates.** Make two copies of every tip that is compared blind (at least W, B45, H, A45, P), each with its own code, so a code cannot be learned as a tip.
- **Key card.** One line per code: tip ID, print batch, measured radius, tape-test result, date. The helper keeps it (or it stays in a sealed envelope); Michael reads it only after the trial forms are filled in. Re-code with fresh letters every two weeks or as soon as a tip has been identified by accident.
- **Tip box.** One slot per tip, each about 11 x 5 x 14 mm deep so the tang stands in it, labelled only with the code (a printed block, or a pill organiser with a cut foam insert). The lid is closed during trials. The helper swaps tips out of Michael's sight; Michael keeps his eyes closed and does not touch the tip before the stroke.
