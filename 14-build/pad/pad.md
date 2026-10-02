# SP1 v3 PAD — detailed design

**Project SCRATCH · 14-build/pad · PAD engineer · 2026-10-02**

**Binding:** SYSTEM-SPEC-v3 §11 PAD work package (§4.1–4.2, §5.1 M8–M14, §7.3–7.4), safety-ruling-dish-gate C1–C8, the 13 red lines and the H-rules.
**Builds on:** leap4-A §4 and the redteam-2 nail and hair findings.
**Builder:** Michael, a careful first-timer who may not own a printer.

**Files:**
- this document;
- `parts.md` (bought parts and prices);
- `CONFLICTS.md` (every departure from the spec: read it first);
- `cad/` (OpenSCAD sources, STLs, the calculators and `cad/README.md` with print and service notes).

**Tags.** [CAD] measured on the model · [EST] computed in `cad/pad_geom*.py` · [JUDG] judgement · [VERIFY] closed by the named bench test · [cited]/[est]/[verify] on prices.

---

## 0. The pad in one page

The pad is a passive, wireless head-borne unit. It has three layers:

- **Block** (moves): six air nails in two galleries. It slides under three dish pockets on three PTFE balls.
- **Yoke**: a small plate on top of the block. Three tendons pull it. Three magnets couple it to the block with a 2 N shear limit.
- **Body** (still): the deck with the three pocket ceilings, the skirt frame with skids, tendon stops and lift-spring hooks, and three spherical ball seats for HALO's float spider.

Everything that touches hair is drafted POM, PTFE or sealed PA12. Nothing on the pad rotates, switches or carries a wire.

| Quantity | Value | Tag |
|---|---|---|
| Nails | 6: centre + pentagon R 18; A = P0, P2, P3; B = C, P1, P4 | spec |
| Nail | one-piece CNC-turned POM: Ø 2.0 flat (R 0.4 rim), 90° cone to Ø 3.92, constant Ø 3.92 land, 59.9 mm long, Ø 2 × 4 steel dowel flush in the top, R 0.5 top rim; 1.0 g | [CAD] |
| Breakaway (C1) | K&J D21B-N52 (Ø 3.18 × 1.59) in each piston face, on the dowel through 0–3 Kapton layers; **target 0.15 ± 0.03 N**; per-session check: 12.5 g holds, 20 g drops | [EST], [VERIFY A2] |
| Pin | Ø 7.0 bore, Ø 5.8 POM/SLA piston, 1/4 in latex Penrose top-hat sleeve; ≈ **0.0322 N/kPa**; stroke 18.5; contact at e = 15.0 (R 85); return spring 0.08 N at contact | [EST], [VERIFY A2] |
| Guides | two PTFE (4 × 6 tube) bushes on the land, 16 mm span; silicone 40A wiper on a snap-off skirt plate | [CAD] |
| Dish (v3b) | half-roll tilt 0.5·asin(d/85); contact zone ≤ 6.5; band 30° to +4.5 at 14.29; outer rim 60° to +9.0 at 16.89; plateau; work amplitude 17.2; cage 18.0 | [EST] |
| Gate on R 85 | rake 17.9–24.7 mm; landing/lift ≤ 34.0°; lift at reversal ≥ 5.34 mm on all nails and headings | [EST] |
| Domes | 3 × 1/4 in PTFE balls on lugs at R 38 (30/150/270°), ball centre 91.5; one pocket each; travel ≤ 28.0 mm; steepest slope 48° | [EST] |
| Lift | 3 inclined extension springs, 0.63–0.81 N over the poses | [EST] |
| Coupling | 3 × K&J D42-N52 over M3 washers, shimmed to **2.0 ± 0.3 N** shear | [VERIFY A3] |
| Tendons | posts R 10 on the yoke, stops R 65 on the skirt frame, 90/210/330°, z 85.5; series spring 2 N/mm in each stop | [CAD] |
| Skids | 3 × R 15 POM-like (SLA) feet, Ø 8, at R 60 (60/180/300°), **height-adjustable ±9 mm** (M3, 0.5 mm per turn) | [CAD] |
| Mount (M8) | HALO's three Ø 5 balls on a **sphere SR 122.5 about the nail-plane point**: a 270° V-groove plus two spherical facets; pad tilts ±3° about the nail plane | [CAD] |
| Envelope | plan Ø ≈ 132 (deck) / ≈ 140 incl. stop blocks; **ball seats 109.5 mm above the skin** | [CAD] |
| Mass | printed 108 g + bought ≈ 24 g = **≈ 132 g** (spec 81.5); moving group ≈ 57 g | [CAD]/[EST] |
| C8 | nail–skid ≥ 15.0 mm; block underside ≥ 34.4 mm (R 85); block–deck ≥ 1.87 mm; fence reach 41.3 mm | [EST] |
| Hair self-score | **30/36, no gating zero** (§9.3) | [JUDG] |

**What changed from the spec, in one line each** (details in CONFLICTS.md):
1. The dish is defined at the nail plane (S0's finding), with a half roll and R 38 domes.
2. The tendon yoke sits above the block (R 10 posts).
3. The stack is ≈ 30 mm taller.
4. The pad is ≈ 50 g heavier.
5. Fixed skids only gate on R 85–90 heads, hence the skid-height adjuster.
6. The nail is a constant Ø 3.92 land with no Ø 1 neck.
7. Pin force is 0.0322 N/kPa.
8. Three lift springs replace the single centred spring.
9. No PP parallelogram: yaw is held by the tendons.
10. M8 is a spherical seat about the nail plane: a true RCC.

---

## 1. How to read and use this package

- **Building from the files:**
  - Start with `cad/README.md` (what to print, where, in what material, orientation and tolerances).
  - Then `parts.md` (what to buy, by stage).
  - Then §12 here (assembly) and §13 (bench checks).
- **Changing a number:**
  1. Change it in `cad/pad_geom.py` / `pad_geom2.py` (kinematics) or `cad/lib_pad.scad` + `cad/gen_pad_stl.py` (parts; same names in both).
  2. Re-run, in this order:
     - `pad_geom.py` (dish, gate, head table);
     - `pad_geom2.py` (pockets, clearances, lift; writes `pockets.npz`);
     - `gen_pad_stl.py` (STLs, masses, `pockets_data.scad`, the shadowgraph SVG);
     - `check_assembly.py` (static and swept interference).
  3. Commands: `cad/README.md` §4.
- **Stage mapping (spec §10):**

| Stage | PAD work |
|---|---|
| S0 dish bench | One pocket (PD19, `cad/README.md` §5) plus three nails on syringes. Proves the v3b profile and the pocket finish before anything else is ordered. |
| Stage A (A2/A3) | The block (floor plate, cartridges, gallery plate, skirt plate, pistons, nails) and the deck + skirt frame, on the R 85 ball. |
| Stage B | Skids, M8 seats on HALO, the C8 feeler checks, B1–B5. |

---

## 2. Frame, stack and layout

**Frame P** is spec §3.1:
- origin = the nail plane on the pad axis, defined as the centre-nail tip at extension e = 15.0 on the R 85 design head;
- +z away from the scalp; +x = bail tangent; P0 on +x.

Every STL is written in its installed position with the block at home.

```
 SECTION through the pad axis (heights in mm above the scalp at the axis, block at home)
 109.5  ── HALO ball seats (sphere SR 122.5 about the nail-plane point; 270° = V-groove)
 108.0  ═══ deck top: lattice hub + six spokes + rim rings over three OPEN pocket shells (1.0 mm SLA)
 93–105 ╲╱  pocket ceilings (one per ball; lowest 93.0 at the ball's home, rising to 105.3)
  94.7  ●   ball top (1/4 in PTFE ball, centre 91.5) on its lug at R 38
  87.0  ▭   yoke top (Ø 28; three D42-N52; tendon notches at R 10, cable z 85.5)
  83.5  ═══ gallery plate top (galleries A/B; cage ring; dome lugs)
  80.0  ─── cartridge tops (sleeve flange clamped by the gallery-plate bead)
        │││  six cartridges Ø 9.4 × 42 (piston chamber 54–80; upper PTFE bush 50–54)
  38.0  ═══ floor plate (lower PTFE bushes 34–38; cartridge sockets; lift-spring lugs)
  34.0  ─── wiper skirt plate (snap-off), wipers at 33–34
  32.0  ─── block underside = hair guard (drafted rim, R ≥ 1)
   0.0  ▼   nail tips at e = 15 (scalp)
  skirt frame: conical R 51 (z 36) → R 56 (z 79.5), PP cover band; skids at R 60 down to the scalp
```

**Plan, angles in frame P:**

| Feature | Where |
|---|---|
| Pins | C at 0; P0–P4 at R 18, 0/72/144/216/288° |
| Dome lugs and pockets | R 38 at 30/150/270° |
| Tendon posts | R 10 at 90/210/330° |
| Tendon stops | R 65 at 90/210/330° |
| Skids | R 60 at 60/180/300° |
| Lift springs | 60/180/300° (block lug R 28.5 → frame hook R 55.5) |
| Columns | R 24 at 108/180/252°; ports B 108°, A 252° at z 60 |
| Deck posts | R 58 at 78/102/198/222/318/342° (clear of lug sweeps and cables) |
| HALO seats | R 55 at 30/150/270°; steel discs at R 42 |

---

## 3. The dish (v3b)

### 3.1 Why the spec's dish had to change

The spec's R 160 dish (leap4-A) rolls the block about the head centre. Measured at the nails, the block then moves only ≈ 0.54× its own offset: S0's solver found a 10 mm rake and 48–62° landings. That is CONFLICTS P1.

Defining the dish at the nail plane fixes the nails. But a full concentric roll swings the domes (92 mm up) 1.85–2.1× as far, so the three pockets overlap unless the domes sit at R ≥ 43–47 (deck Ø ≈ 165).

Unwinding the tilt on the rim keeps the pockets small, but the dome then climbs nearly vertically (60–89° slopes), so the rim reaction becomes unbounded.

**v3b, the chosen compromise:** half the concentric roll everywhere, domes at R 38. The cost is +0.7 mm of gap spread across the nails in contact. Force is air, so that only spreads the landings (natural asynchrony).

### 3.2 Profile (block pose as a function of the nail-plane offset d) [EST, `pad_geom.py` §1]

| \|d\| mm | rise h | tilt ° | dome travel | centre-nail clearance at full extension | min / max nail clearance |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | −3.50 | −3.50 / −1.54 |
| 4.0 | 0 | 1.35 | 6.1 | −3.50 | −3.50 / −1.10 |
| **6.5** (contact-zone edge) | 0 | 2.19 | 10.0 | −3.50 | −3.50 / −0.83 |
| 8.5 | 1.15 | 2.87 | 13.0 | −2.35 | −2.35 / +0.48 |
| 10.5 | 2.31 | 3.55 | 16.1 | −1.20 | −1.20 / +1.78 |
| 12.5 | 3.46 | 4.23 | 19.1 | −0.06 | −0.06 / +3.06 |
| **14.29** (band end, 30°) | 4.50 | 4.84 | 21.9 | +0.95 | +0.95 / +4.19 |
| 15.5 | 6.59 | 5.25 | 23.7 | +3.00 | +3.00 / +6.25 |
| **16.89** (rim top, 60°) | 9.00 | 5.73 | 25.8 | +5.35 | +5.35 / +8.59 |
| **17.2** (work reversal) | 9.00 | 5.84 | 26.3 | +5.34 | +5.34 / +8.62 |
| **18.0** (cage) | 9.00 | 6.11 | 27.5 | +5.33 | +5.33 / +8.67 |

- Negative clearance = the nail is in contact, and the number is its reserve.
- "Rise" is measured above the concentric surface √(85² − d²) − 85.

**Landings on a centred line (R 85):** C at ±12.6 mm; pentagon nails at 7.8–11.3 mm depending on the heading. So the contact chord is 15.6–25 mm and the rake (skin length actually scraped) is **17.9–24.7 mm**.

**Gate metrics on R 85, all headings** [EST, §2]: landing/lift ≤ 34.0° (C5 ≤ 35 ✓); lift at reversal ≥ 5.34 mm (C5 ≥ 5 ✓); no nail-heading pair that never touches.

### 3.3 Pockets (the deck's ceilings)

- Each 1/4 in PTFE ball rides its own pocket.
- The ceiling is the upper envelope of the ball over every pose to the cage. It is computed in `pad_geom2.py` and stored in `cad/pockets.npz` / `pockets_data.scad` as a polar height field: 69 radii × 144 angles, radius 32.1 mm about each ball's home.
- Ceiling z = 92.96 (just under the home ball top, 94.67) to 105.30.
- Max ball travel 27.96 mm; pocket radius incl. the ball 31.13; spacing allows 32.91, so the pockets clear each other by **1.77 mm**.
- **Surface:** SLA, as printed, then 1500-grit wet and a PTFE dry-film spray (WD-40 Specialist Dry PTFE or equivalent).
  - Do **not** tape the pockets: 0.13 mm PTFE tape wrinkles on a doubly curved surface, and each wrinkle is a stick-slip bump. This departs from spec C7 (tape).
  - V-D3 (stick-slip silent at 140 mm/s) is tested on the S0 single-pocket bench.

### 3.4 Rim reaction and the coupling budget [EST]

The horizontal force the ceiling puts on the block is (vertical ball load) × tan(slope along the ball's path):

| \|d\| | ≤ 6.5 | 8–14 | 14.3–16.9 | ≥ 16.9 |
|---|---|---|---|---|
| Max path slope | 15° | 24° | **48°** | 18° |
| Ball load (vertex) | pins + lift − W ≈ 2.0–2.6 N | 1.0–2.6 N | lift − W ≈ 0.1–0.3 N (vertex) … 0.8 N (bun) | as outer |
| Reaction | ≤ 0.7 N | ≤ 1.1 N | ≤ 0.9 N | ≤ 0.3 N |

- Add drag (≤ 6 × 0.3 = 1.8 N worst; typically 0.5–1 N) and the lift springs' centring pull (≤ 0.47 N).
- In the landing band this can pass the 2.0 N coupling: risk R3. Stage A3 measures it (V-D1). The spec allows 2.5 N.
- **FIRMWARE** needs this table for the dish-aware snag criterion (C4) and the IK pose (CONFLICTS P15).

### 3.5 Path-checker numbers (C5)

| Item | Value |
|---|---|
| No-reversal radius | **16.9 mm** (lift ≥ 5.3 for every nail beyond it) |
| Working amplitude | 17.2 (reversal on the plateau) |
| Cage | 18.0 (lift-spring lugs touch the skirt frame's bottom ring) |
| CIRCLE | R + e ≥ 17.0 and R − e ≤ 7.8 (e.g. R 12.5, e 4.5) |
| Chords | offsets 0–9 mm still land (pentagon landings ≥ 7.8) |

---

## 4. Head shape, skids and the skid-height adjuster

### 4.1 The finding

The skids register the pad to the scalp at R 60. The scalp under the pad axis then sits at different depths on differently curved heads [EST, `pad_geom.py` §3]:

| Head (local) | Scalp at the axis vs nominal | Earliest / latest nail contact e | C6 (≥ 15) | Gate |
|---|---|---|---|---|
| sphere R 65 (bun) | **+7.1** | 7.9 / 10.5 | FAIL | FAIL |
| R 70 | +4.8 | 10.2 / 12.6 | FAIL | weak |
| R 80 | +1.4 | 13.7 / 15.7 | FAIL | weak (lift 4.1) |
| **R 85** | 0 | 15.0 / 16.9 | ok | **ok** |
| R 90 | −1.2 | 16.2 / 18.0 | ok | ok |
| R 100 | −3.1 | 18.1 / 19.7 | ok | **pentagon nails never reach** |
| R 150 | −8.7 | 23.7 / 24.8 | ok | none reach |
| crown 90 × 100 | −2.2 | 17.2 / 19.3 | ok | some never reach |
| parietal 70 × 150 | −2.4 | 17.4 / 21.6 | ok | some never reach |
| bun 65 × 80 | +3.3 | 11.7 / 14.9 | FAIL | weak |

The gate works only when the scalp at the axis is within −1.6…0 mm of nominal. The spec's "reserve 1–3.5 everywhere" assumed this away (CONFLICTS P5).

### 4.2 The fix: one skid-length setting per station group

- Each skid stem is moved by a captive M3 screw: 0.5 mm per turn, 12 clicks per turn on the knob. Range ±9 mm.
- All three skids are set equal with the stepped gauge PD18, then locked by the knob's friction.
- **Settings** (skid length change from the R 85 zero, + = longer) [EST, §3b]:

| Station group | Setting | Result |
|---|---|---|
| Bun R 65–70 | +5 … +7 | all six nails reach, C6 ok |
| Bun 65 × 80 | +3.3 | all reach |
| Upper occiput / crown R 80–90 | −1 … +1.4 | all reach |
| Crown 90 × 100 | −2.2 | all reach |
| Flat crown R 100 | −3.1 | all reach |
| Parietal 70 × 150 | −2.4 / −1.6 | **one nail 0.2–0.7 mm short at some headings** (skims, never lands) |

- After the setting, the earliest nail touches at e = 15.0 and the latest by e ≤ 17.5 (≤ 19.2 on the parietal). Lift at reversal ≈ 5.5 mm everywhere.
- **Procedure:** Stage C1 measures each group's setting with the feeler method in §13.6; the station table carries it. Moving between stations of the same group needs no change. Changing group costs ≈ 30 s (three knobs, gauge check).
- **Risk:** this adds a manual step to "moving it". Score it in Stage B ("having to move it" ≤ 3/10). If it fails: a region-keyed second dish (spec R1 fallback) or skids that ride a cam ring (one twist sets all three; +6 g; not drawn).

### 4.3 Skid geometry

| Item | Value |
|---|---|
| Foot | R 15 spherical cap, Ø 8 footprint, axis tilted 36.9° toward the head centre so it meets curved scalp square-on. Contact normals R 65–150 stay inside its ±15° cap. |
| Material | SLA, polished; H-4.7 class |
| Load | skids carry the palm force: float force − pins ≈ 1.5–3 N total, ≤ 1 N each, ≥ 50 mm² at the scalp → ≤ 20 kPa (H13 ≤ 5 kPa holds for the helmet pads, not the skids; skids are a moving contact) [JUDG] |
| Stem | PETG Ø 6, hollow, flat for anti-rotation, M3 insert at the top. Runs in the frame's bottom-ring guide (Ø 6.3) and is driven from the top-ring boss by an M3 × 40 nylon screw with knob PD14. |
| Nail–skid clearance | ≥ 15.0 mm at every pose incl. ±5° yaw (C8 ≥ 8 ✓) |

---

## 5. The pin (cartridge, piston, sleeve, spring, guides, wiper)

### 5.1 Section through one pin (block at home, nail at e = 15)

```
 z (mm)
 83.5 ┌──────── gallery plate (SLA) ─────── channel Ø1.4 at z 81.75 → port Ø1.4 into the hat
 80.0 ├─ bead ring crushes the Penrose flange folded over the cartridge top (the flange IS the seal)
      │  ┌───── hat crown (latex, tied end) ─┐   piston top at e = 0: 79.4 (0.6 mm to the cap)
      │  │ piston Ø5.8 × 4.5 (SLA or POM)    │   ← air pushes down
 ~64  │  │ D21B-N52 in the face (flush)      │   magnet face = land top: 59.9 at e = 15, 56.4 at e = 18.5, 74.9 at e = 0
      │  └─convolution in the 0.6 mm gap────┘   bore Ø7.0 (54–80)
      │   return spring 0.15 wire, OD 5.0, L0 22 (around the land)
 54.0 ├─ upper PTFE bush (4×6 tube, 4 long) 50–54 ── cartridge Ø9.4 OD, SLA
      │   land clearance Ø4.6 (38–50); rod-side vent Ø1.0 at z 55 → OD groove → gallery-plate groove → rim
 38.0 ├─ floor plate: lower PTFE bush 34–38
 34.0 ├─ wiper: 40A silicone Ø9 × 1.0, Ø1.5 hole + 4 slits, in the skirt-plate pocket
 32.0 └─ skirt plate underside (drafted Ø6 → Ø4.4 nose hole)
      ▼  land Ø3.92 (POM) down to the 90° cone and Ø2 flat at z 0
```

### 5.2 Numbers

| Item | Value | Tag |
|---|---|---|
| Stroke | 18.5 (retract stop = piston against the cap) | spec C5/C6 |
| Contact | e = 15.0 centre nail, 16.93 pentagon (R 85) → retract margin ≥ 15.0 (C6 ✓) | [EST] |
| Effective area | rolling sleeve, bore 7.0, piston 5.8 → Ø_eff ≈ 6.4 → **32.2 mm² = 0.0322 N/kPa** (spec 0.0385) | [EST] [VERIFY A2: force at 10 kPa] |
| Return spring | music wire 0.15 mm, OD 5.0, ≈ 9 active coils, L0 22, k ≈ 0.005 N/mm. Force 0.005 (e = 0) / 0.04 (e = 7) / **0.08 (e = 15)** / 0.10 N (e = 18.5); solid 1.6 mm | [EST] |
| Friction | wiper lip ≈ 0.01–0.02 N; PTFE bushes ≈ 0 unloaded; 0.17–0.22 N extra with 0.5 N tangential at the tip | [EST] |
| C7 | spring ≥ 2× friction from e = 18.5 down to e = 7 (≥ 0.04 vs ≤ 0.02 N) → vented nail retracts ≥ 8 mm | [EST] [VERIFY A2] |
| Net force | P·0.0322 − 0.08 N: 0.20 N at 8.7 kPa; 0.37 N at 14.0; 0.50 N at 18.0; max at R1a 0.59 N | [EST] |
| Per-nail caps | R1a 20.7 kPa → **0.67 N**; R1b 24 → 0.77 N; deadhead 50 → 1.61 N (red line 2 ✓) | [EST] |
| Pin installed mass | cartridge 1.78 + piston 0.12 + nail 1.01 + magnet 0.09 + bushes 0.24 + sleeve 0.25 + spring 0.03 + wiper 0.08 ≈ **3.6 g** (spec 2.5) | [CAD] |
| Rod-side breathing | 32 mm² × 18.5 = 0.6 ml per full stroke, vented above the block, never through the wiper (RT2 1.5) | [CAD] |

### 5.3 Penrose sleeve: preparing one (2 minutes, consumable)

1. Cut a 22 mm length of 1/4 in Penrose drain with sharp scissors, square.
2. Tie one end off tight with two turns of 0.12 mm (6 lb) braided fishing line, a surgeon's knot, as close to the end as you can. Trim the tag to 1 mm. Add a drop of CA on the knot only.
3. Turn it inside out, so the knot is inside, and slide it over the piston crown. The knot sits in the shallow dimple you file in the crown with a round needle file.
4. Push the piston, sleeve first, into the cartridge bore from the top until the piston face is 15 mm below the rim.
5. Fold the open end out over the cartridge top rim and 3 mm down the Ø 8.7 step. It must be smooth, with no pleats over the rim face.
- **Good:** pushing the nail up by hand rolls the sleeve with no rubbing feel. Releasing it, the spring returns it fully.
- **If not:** a sleeve that "catches" has a pleat or a twist. Pull the piston out and refit.

### 5.4 Guides and wiper
- **Lower bush:** PTFE tube 4 × 6 mm cut to 4.0 mm, pressed into the Ø 5.95 floor-plate bore.
- **Upper bush:** the same, in the cartridge's Ø 5.95 seat at z 50–54. Ream both with the land itself: spin a spare nail in the bush with a drill at slow speed for 5 s.
- The two bushes are 16 mm apart, centre to centre.
- **Wiper:** 1.0 mm 40A silicone sheet, punched Ø 9 (hollow punch). Centre hole Ø 1.5 (hollow punch or a sharpened 14 G needle). Then four 1.0 mm radial slits with a fresh scalpel blade.
  - The disc sits in the skirt plate's Ø 9.1 × 1.0 pocket and is clamped by the floor plate.
  - The land opens the slits. When a nail drops out, the hole recloses to Ø 1.5, which is 33 mm above the skin (outside H-4.9's 25 mm zone).

### 5.5 Gallery plate, galleries and bleeds
- **Galleries:** Ø 1.4 internal channels at z 81.75.
  - **B** = port at 108° → arc R 24 → P1 → C → P4.
  - **A** = port at 252° → arc R 24 both ways → P0, P2, P3.
  - Each cartridge has a Ø 1.4 port down into its hat.
- **Ports:** printed Ø 2.5 barbs with a Ø 3.0 ridge on the 108° and 252° columns, at z 60, pointing outward. They take 1/8 in × 2 mm PU tube. Back each one up with two turns of waxed thread.
- **Bleed (C3):** a 30 G needle stub, 4 mm, epoxied into a Ø 0.32 hole drilled radially through each port column at z 70 into its vertical channel (§12, step 6). It lets a kinked, pressurised line fall below 2 kPa in < 1 s [VERIFY A2].
- Vent time ≤ 100 ms through the S070 is DRIVE BOX's (V-P1). The pad adds ≈ 0.3 ml of gallery volume per line [CAD].

### 5.6 Fallback: ball-bushing nail (if A2 fails C1(ii) or C7)
- Replace the two PTFE bushes with one **LM4UU** (Ø 4 × Ø 8 × 12) in the floor plate. The cartridge bottom is re-printed with a Ø 8.0 seat.
- The land becomes a **Ø 4 h6 hardened dowel, 4 × 60** with the POM tip pressed on a turned-down end (CNC service).
- Friction drops to ≈ 0.005 N. Each nail weighs ≈ 6 g (+30 g per pad).
- Order only if the A2 side-load test reads > 0.35 N with B set at 0.15.

---

## 6. The nail and the magnetic breakaway (C1, C2)

### 6.1 Nail drawing (PD15, CNC-turned)

| Feature | Dimension | Tolerance |
|---|---|---|
| Tip flat | Ø 2.00 | ±0.05 |
| Tip rim | R 0.40 | 0.35–0.50 (hand-polish, 1500 grit) |
| Cone | 90° included, Ø 2.0 → Ø 3.92 over 0.96 mm | ±2° |
| Land | Ø **3.92** constant, 0 → 59.9 | −0.00 / −0.03 (h8-ish); straight within 0.03 over the length |
| Top | flat, rim R 0.5 | — |
| Insert hole | Ø 1.95 × 4.2 deep, centred ±0.05 | for a Ø 2 × 4 hardened dowel, pressed flush ±0.02 |
| Surface | Ra ≤ 0.4 on the land (it is the wiper and bush surface), ≤ 0.8 on the cone | — |
| Material | POM-C (acetal copolymer), **red or orange if the service stocks it**, else natural white (CONFLICTS P6) | — |
| Mass | 1.01 g + dowel 0.10 g | [CAD] |

- The profile **never narrows going up** (C2): cone to Ø 3.92, then constant.
- No shoulder within 3 mm of the nose at full retract: the cone ends at z 0.96, which is 15.96 at e = 0, 16 mm below the nose.
- Proof (red line 9) for a press-fit dowel in POM: pull-out ≥ 10 N typical [EST]. Proof each nail at 3.1 N axial (insert pull, §13.3) and 3.1 N compression (on the magnet face).

### 6.2 Breakaway magnet selection [cited / EST]

**Chosen: K&J Magnetics D21B-N52**, Ø 3.18 × 1.59 mm, N52, axially magnetised. Pull to a thick steel plate 0.56 lb = **2.49 N** (case 1), surface field 5233 G. $1.68 per 10-pack [cited: kjmagnetics.com/d21b-n52-neodymium-disc-magnet, 2026-10-02].

**Why this size:**
- It is the spec's Ø 3 × 2 class in a stocked, documented part.
- On a Ø 2 dowel face the pull falls to roughly the area ratio (3.14/7.94 mm²) × saturation, i.e. ≈ **0.4–1.0 N at contact** [EST]. That is 2.5–6× the 0.15 N target, so the setting is made with a gap, which is far more repeatable than a near-zero-gap joint.
- Estimated pull versus gap for this pole size: F(g) ≈ F0/(1 + g/0.6)² [EST]. Gap 0.3 → 0.44 F0; gap 0.6 → 0.25 F0; gap 0.9 → 0.16 F0. So the target sits at a **0.5–0.9 mm** gap.

**Gap material:**
- Kapton (polyimide) tape, 0.065 mm per layer (1 mil film + adhesive), stuck on the magnet face, for fine trim.
- 0.25 mm PET discs (Ø 3, punched from a clear report cover) for coarse steps.
- Coarse to 0.5 mm with 2 PET discs, then trim ±1 Kapton layer.

**If at zero gap the pull is < 0.25 N:** use the K&J D22-N52 (1/8 × 1/8 in) [verify price]. **If the pull is unstable** (a dowel end not flat): face the dowel ends on 600-grit paper on glass.

### 6.3 Calibration procedure (Stage A2, every pin; 15 minutes per pin the first time)

Tools: 0.01 g jewellery scale, a 30 cm length of 0.2 mm monofilament, the hang cups PD16 (two of them), fine rice or water, tweezers, Kapton tape, PET discs.

1. **Set up the block** upright on two blocks of wood, so the nails hang free below it. Feed the pin's gallery from the A1 rail at 3 kPa so the piston sits at full extension (e = 18.5). The air only holds the piston down; the magnet joint is what you are measuring.
2. **Fit the nail:** push it up through the wiper and bushes until it clicks onto the magnet.
3. **Tie** the monofilament to the cone with a slip loop just above the tip.
4. **Hang a cup** on the line. Add rice slowly (a pinch at a time) until the nail drops. Weigh cup + rice + line on the scale.
   - **Target 15.3 g ± 3 g** (0.15 ± 0.03 N).
5. **Repeat ×10** (the ruling's (a)). Record mean and range. Range must be ≤ ±1.5 g.
6. **Adjust:** too strong → add one Kapton layer (≈ −1 to −2 g); too weak → remove one.
7. **Side-load check (C1 (ii)):** hang a 50 g weight sideways (thread over a pulley or pencil) from the cone, then repeat step 4. Release must stay **≤ 35.7 g** (0.35 N).
   - **If it fails:** clean the land and bushes with IPA, re-ream (§5.4), retest.
   - **If it still fails:** the §5.6 fallback.
8. Write each pin's final shim stack on the piston with a fine marker.

### 6.4 Shadowgraph template (C2)

- `cad/shadowgraph_nail.svg`: print at 100 % and check the 50 mm bar with calipers. Also the printed card PD17 (black PETG).
- **Method:**
  1. Lay the nail on the 10:1 tip drawing under a phone at 10× macro, or lay it in the PD17 window on a phone torch.
  2. The silhouette must lie between the **red (max)** and **blue (min)** outlines everywhere.
  3. The land must pass the Ø 3.95 slot and not enter the Ø 3.88 slot.
  4. Then sight along the nail against a window: no visible neck, step or bulge above the cone.
- Pass = in-band everywhere and the slot test. Reject otherwise.

### 6.5 Per-session C1 check (ruling (e)), 1 minute

Two labelled cups:
- **"HOLD 11"**: cup + rice = 11.0 g (0.108 N). Hung from each nail's tip loop, it **must not** drop the nail.
- **"DROP 20"**: 20.0 g (0.196 N). It **must** drop the nail.

Count the six nails before and after the session; any missing nail is found before the next session. A nail that fails either cup is re-shimmed (§6.3) before use.

---

## 7. Yoke, coupling, tendons and stops

### 7.1 Yoke (PD10, SLA, 1.9 g)
- Ø 28 × 3.5 plate, sitting on the gallery plate's centre on a 0.25 mm PTFE slider sheet.
- Three D42-N52 magnets in Ø 6.45 × 3.4 pockets from below, at R 8 (30/150/270°).
- Three tendon notches at 90/210/330°:
  - apex at **R 10**, z 85.5; flared ±22° horizontally; floor dropping 0.7 mm to the rim, so a cable leaving 9° downward on the rim plateau does not rub.
  - Each has a 2.2 × 3.8 ferrule pocket inboard.
- A 6 mm cage gap to the gallery plate's cage ring (R 20 inner, 1.5 high).

### 7.2 Coupling magnets [cited]
- **K&J D42-N52**, Ø 6.35 × 3.18 mm, N52: pull 2.85 lb = 12.7 N to a thick plate (case 1), $0.52 each [cited: kjmagnetics.com/d42-n52-neodymium-disc-magnet, 2026-10-02]. This is the spec's Ø 6 × 3.
- **Keeper:** M3 DIN 125 steel washer (7 × 3.2 × 0.5), flush in a Ø 7.1 × 0.6 pocket in the gallery plate top. A thin keeper saturates, which makes the shear release softer and more repeatable.

### 7.3 Coupling calibration (Stage A3)
1. Yoke on the block, the block on its domes under the deck, tendons slack.
2. Tie a thread to one tendon notch. Pull it horizontally with the luggage/kitchen scale, slowly.
3. **Target release 2.0 ± 0.3 N (204 ± 31 g)** in each of the three directions; release = the yoke slides off its washers.
4. Adjust with 0.1 mm PET shims under the yoke's PTFE slider: more shim → lower release.
5. Record. Repeat after the 20-minute nuisance runs (A3).

### 7.4 Tendon stops and series springs (PD11 on the skirt frame)
- Each stop block (PETG) bolts to its stop arm with 2 × M2 × 8.
- Inside: a Ø 5.2 bore holding
  - the housing ferrule (Ø 1.6 brass on the PTFE-lined coil);
  - a **2 N/mm compression spring** (≈ 4 OD × 0.5 wire × 10 free, ≈ 7 active coils, from an assortment; measure the rate, §13.5);
  - an **M3 barrel adjuster** in an M3 heat-set insert at the outboard end.
- The cable runs through the spring, exits inboard through a Ø 1.0 hole at z 85.5, and reaches the yoke notch at R 10.
- **Pretension:** set 2.0 N per cable with the barrel adjusters (ELECTRONICS' value). The spring then sits ≈ 1 mm compressed, with ≥ 4 mm of linear travel left (spec ≥ 4).
- The housing load (equal to the cable tension, ≤ 5 N at VREF) passes into the PA12 frame through the arm (proof 10 N, §13.3).

---

## 8. Lift, yaw, cage and the M8 seat

### 8.1 Lift springs [EST, `pad_geom2.py` §6]
- Three extension springs at 60/180/300°, from the floor-plate eyelet (R 28.5, z 36) to the skirt-frame hook (R 55.5, z 77).
- Spring: music wire 0.20 mm, OD 2.5, ≈ 108 active coils, L0 30 between hook centres, k ≈ 0.012 N/mm, initial tension ≈ 0.09 N.
- Stretched 19 mm at home (0.32 N each).
- **Lift 0.63–0.81 N** over every pose to the cage; centring pull ≤ 0.47 N.
- The block + yoke weighs 57 g (0.56 N), so the block stays up on the plateau with pins vented at the vertex by 0.07–0.25 N [VERIFY A3, §13.7]. If it sags: shorten the hook by one coil (+0.1 N).

### 8.2 Yaw
- There is no PP parallelogram (CONFLICTS P11).
- **Yaw is held by** the three tendons pulling outward on posts at R 10: 71 N·mm/rad = 1.24 N·mm/° at 2 N pretension, plus dome friction (≈ ±2.6 N·mm dead band).
- **Yaw torques** from uneven nail drag are ≤ 2–5 N·mm, giving ±2–4° wander [EST].
- The C8 and pocket sweeps were run at ±5° yaw and pass.
- Test it on the A3 ink rig: draw a yaw mark on the block; after 5 minutes of PLINE it must read ≤ ±5°.

### 8.3 Cage
- At |d| ≈ 18 the lift-spring lugs touch the skirt frame's bottom ring (R 51). That is the hard cage.
- The domes are then on the plateau; nothing else touches (`check_assembly.py` sweep, 145 poses).

### 8.4 M8 seat: RCC about the nail plane (CONFLICTS P12)
- HALO's spider balls (Ø 5 at R 55) rest on three deck seats cut on a **sphere SR 122.5 centred on the nail-plane point**:
  - the **270° seat is a 90° meridional V-groove** (yaw key);
  - **30° and 150° are spherical facets**.
- With the float pushing the pad down, the pad can tilt about the nail-plane point but cannot slide or yaw. Drag at the nails makes no tipping moment (true RCC), so the skids seat themselves.
- **Range:** ±3°, limited by the magnet-to-disc gap.
- HALO's Ø 6 × 3 magnets at R 42 attract **Ø 8 × 1 steel discs** in the deck's three bosses: nominal gap 2.5 mm, breakaway ≈ 3 N [EST, VERIFY B3].

---

## 9. C8 clearance sweep and hair self-score

### 9.1 C8 sweep [EST, `pad_geom2.py` §4–5; `check_assembly.py`]

The sweep covers every pose |d| ≤ 18 (cage) at all headings, with yaw −5/0/+5°, tilt and rise from the dish model.

| Check (ruling C8 / spec) | Required | Result |
|---|---|---|
| Nail to skid foot, 3D, incl. tilt 6.1° and rise 9 | ≥ 8 mm | **≥ 15.0 mm** |
| Block underside above the scalp, R 85 | ≥ 30 mm | **≥ 34.4 mm** |
| Block underside, R 65 (skid at zero / at its +7.1 setting) | ≥ 30 | 27.8 / 34.9 |
| Block-top features (yoke, gallery plate, lugs, stalks) to any pocket ceiling | > 3, or booted | **≥ 1.87 mm**: inside the closed pad (deck above, PP cover band around), ≥ 83 mm above the scalp; no hair can reach (CONFLICTS P3) |
| Block rim to skirt frame (whole height) | > 3 or covered | ≥ 1.3 mm, covered by the band; first contact at the cage |
| Pockets apart | > 0 | 1.77 mm |
| Fence (nail-tip reach from the pad axis) | — | **41.3 mm** (HALO stops must use this + 15) |
| STL interference at home | none | only the two intended press fits (bead on sleeve flange, PTFE ball in socket) |
| STL sweep, 145 poses, moving block vs deck/frame/stops/skids | none | none, except the designed cage contact at d = 18 |

### 9.2 Hair rules applied (spec §7.4, PAD items)

- **Within 25 mm of the scalp:** only nail cones and lands (behind zero-gap wipers) and static skid feet, ≥ 15 mm from any nail.
- **No rotation on the pad:** the balls are fixed in their sockets and slide; they do not roll.
- **Nail profile is monotonic (C2):** no neck, sleeve, ferrule or step below the guard.
- **No PTFE in the pile:** PTFE is at ≥ 34 mm (bushes) and ≥ 91 mm (balls).
- **Tool-free cleaning:** nails pull out at 0.15 N; the skirt plate snaps off; cartridges lift out after 3 screws.
- **Lift before reversal by geometry:** ≥ 5.3 mm at the 16.9 mm no-reversal radius.

### 9.3 H-6.8 checklist self-score [JUDG]

| # | Item (G = gating) | Score | Note |
|---|---|---|---|
| 1 | No rotation in zone (G) | 2 | |
| 2 | Joint methods (G) | 2 | nose: zero-gap wiper; insert joint is at the land top, inside the cartridge |
| 3 | No changing / 40 µm–3 mm gap within 25 mm (G) | 2 | nail–skid ≥ 15 |
| 4 | Lift before reversal (G) | 1 | by design: 5.3 mm lift, still in a 10–25 mm pile |
| 5 | Rigid group (G) | 2 | one block; skids static during play |
| 6 | Drafted nail, no re-entrants (G) | 2 | C2 constant-stem option |
| 7 | Yield ≤ 0.15 N tangential (G) | 1 | tangential still 2.0 N coupling; axial 0.15 N |
| 8 | Protrusion | 1 | 32 mm (35 for 8 cm hair) |
| 9 | Spacing ≥ 8 | 2 | 18 |
| 10 | Low-friction surfaces | 2 | |
| 11 | Breakaway 3–5 N, no tether | 1 | pad mount ≈ 3 N [VERIFY]; nails 0.15 N |
| 12 | Guard pass-throughs | 2 | drafted nose holes; land constant through the guard |
| 13 | Grain map | 2 | firmware |
| 14 | Dwell limits | 2 | firmware |
| 15 | Snag reflex | 2 | ELECTRONICS |
| 16 | Antistatic | 1 | POM; no PTFE in the pile; no ground path |
| 17 | Tool-free removal | 2 | |
| 18 | Variants stated | 1 | long/coarse hair OK; curly untested; parietal anisotropy partial (P5) |
| | **Total** | **30/36, no gating zero** | same as the ruling's estimate |

---

## 10. Mass by part

Printed parts are from CAD volumes (`cad/mass_by_part.csv`) at SLA 1.15, MJF 1.01, PETG 1.27, POM 1.41 g/cm³. Bought parts are [EST].

| Part | Process | Qty | g each | g total |
|---|---|---|---|---|
| PD01 deck | SLA | 1 | 33.4 | 33.4 |
| PD02 skirt frame | MJF PA12 | 1 | 12.5 | 12.5 |
| PD05 floor plate | SLA | 1 | 9.8 | 9.8 |
| PD06 cartridge | SLA | 6 | 1.78 | 10.7 |
| PD07 gallery plate | SLA | 1 | 14.6 | 14.6 |
| PD08 wiper skirt plate | MJF PA12 | 1 | 4.1 | 4.1 |
| PD09 piston | SLA | 6 | 0.12 | 0.7 |
| PD10 yoke | SLA | 1 | 1.9 | 1.9 |
| PD11 stop block | PETG | 3 | 0.74 | 2.2 |
| PD12 skid stem | PETG | 3 | 1.43 | 4.3 |
| PD13 skid foot | SLA | 3 | 1.93 | 5.8 |
| PD14 skid knob | PETG | 3 | 0.68 | 2.1 |
| PD15 nail | POM (turned) | 6 | 1.01 | 6.0 |
| **Printed / turned subtotal** | | | | **108.1** |
| C1 magnets D21B-N52 | | 6 | 0.09 | 0.6 |
| Coupling magnets D42-N52 | | 3 | 0.75 | 2.3 |
| Washers, steel discs (M8), dowels | | 3 + 3 + 6 | | 2.3 |
| PTFE balls 1/4 in | | 3 | 0.29 | 0.9 |
| PTFE bushes (4 × 6 × 4) | | 12 | 0.10 | 1.2 |
| Penrose sleeves, wipers, return springs | | 6 each | | 2.2 |
| Lift springs, series springs | | 3 + 3 | | 0.9 |
| M2/M3 screws (nylon M3 × 40), M3 inserts | | 9 + 3 + 6 | | 4.0 |
| PP cover band 0.5 mm | | 1 | | 5.0 |
| On-pad tube loops, cable stubs, ferrules, glue | | | | 4.0 |
| **Bought subtotal** | | | | **≈ 23.4** |
| **PAD total** | | | | **≈ 132 g** (spec 81.5; B1 gate ≤ 90: fails, CONFLICTS P4) |
| Moving group (block + yoke + nails + bought on them) | | | | ≈ 57 g (spec 47) |

**Diet path to ≈ 100 g** (in order of ease):
1. 0.25 mm PET cover band: −2.5.
2. Nylon screws everywhere: −2.
3. Deck shells 0.8 mm: −5.
4. Gallery lugs ribbed, columns hollow: −4.
5. Floor plate pocketing: −3.
6. Skid feet hollow: −2.
7. Deck in MJF with PTFE film on the pockets: −5 [VERIFY smoothness].
8. Cartridge wall 1.0 (SLA minimum): −2.

---

## 11. Parts: material, process, tolerances, fasteners

| ID | Part | Material / process | Print orientation | Critical tolerances | Fasteners / inserts | Service OK? |
|---|---|---|---|---|---|---|
| PD01 | Deck | SLA standard resin (JLC "Imagine Black" / 8001 class), 0.05 layers | top face down (pockets up), supports on the top face only | pocket surfaces as printed ±0.1, then 1500-grit + PTFE dry film; seat sphere ±0.1; disc pockets Ø 8.1 | 6 × M2 × 10 pan screws up into post pilots (Ø 1.7) | **print service OK** (SLA) |
| PD02 | Skirt frame | MJF PA12, dyed black | as modelled (rings horizontal) | skid guide Ø 6.3 ±0.1; post holes Ø 2.4 | skid adjuster M3 × 40 nylon screw passes the top-ring boss (captive by its knob); 2 × M2 × 8 per stop block | **print service OK** (MJF) |
| PD05 | Floor plate | SLA (tough resin, e.g. JLC 9600 class) | underside down | bush bores Ø 5.95 (+0.00/−0.05; ream); sockets Ø 9.55 ±0.05; pin positions ±0.1 | 3 × M2 × 8 into the columns | **print service OK** (SLA) |
| PD06 | Cartridge ×6 (+2) | SLA tough resin | upright, top up; no supports inside the bore | bore Ø 7.0 +0.05/−0; bush seat Ø 5.95; OD 9.4 −0.05 | none | **print service OK** (SLA) |
| PD07 | Gallery plate | SLA standard resin | plate face up, columns down, supports on columns' ends | channels must drain: flush with IPA through each port; ball sockets Ø 6.25 (press); washer pockets | 3 × M2 × 8 from below | **print service OK**; ask for "internal channels, no supports inside" |
| PD08 | Wiper skirt plate | MJF PA12, then bead-blast; seal underside with 2 coats of thin CA, sand 1500 | flat | wiper pocket Ø 9.1 × 1.0; hooks flex | snap | **print service OK** (MJF) |
| PD09 | Piston ×6 (+2) | SLA tough; or POM rod Ø 6 turned on a drill | flat face down | Ø 5.8 ±0.05; magnet pocket Ø 3.25 × 1.62 | magnet with a drop of CA | **print service OK** |
| PD10 | Yoke | SLA | face down | magnet pockets Ø 6.45; notch apex | magnets CA | **print service OK** |
| PD11 | Stop block ×3 | PETG, 0.12 layers, 5 walls | on its side (bore horizontal) | spring bore Ø 5.2 | M3 heat-set (Ø 4.0 × 4) for the barrel adjuster; 2 × M2 × 8 | **home printer recommended** (iterate) or service MJF |
| PD12 | Skid stem ×3 | PETG, 100 % infill | upright | Ø 6.0 −0.1 (slides in 6.3) | M3 heat-set at the top | home or service |
| PD13 | Skid foot ×3 | SLA, polished 1500 grit + PTFE film | cap up | R 15 ±0.1; edge R ≥ 1 | stem bonded (CA) | **print service OK** |
| PD14 | Skid knob ×3 | PETG | flat | M3 nut hex | M3 nylon nut glued | home |
| PD15 | Nail ×6 (+12 spares) | **CNC-turned POM-C** (JLCCNC / PCBWay / Xometry turning) | — | §6.1 | Ø 2 × 4 hardened dowel pressed | **turning service** |
| PD16–18 | Hang cups ×2, shadow card, skid gauge | PETG | flat | gauge steps 0.5 ±0.05 (check with calipers) | — | home or service |

**Heat-set inserts:** M3 brass, Ø 4.0 × 4 holes (spec §5 says Ø 4.0 × 5.7 holes for the 5.7 mm long type; either works). Press with a soldering iron at 230 °C (PETG) or 220 °C (PA12). Not used in SLA parts (SLA cracks): M2 screws go straight into Ø 1.7 pilots there.

---

## 12. Assembly for a first-timer

**Tools:**
- digital calipers;
- 0.01 g jewellery scale and a 5 kg kitchen/luggage scale;
- soldering iron with a heat-set tip;
- hobby knife and fresh blades;
- 1.5 mm and 9 mm hollow punches;
- needle files;
- 600/1000/1500 wet-and-dry paper and a glass plate;
- pin vise with Ø 0.3 and Ø 1.7 drills;
- small Phillips and 1.5/2.0 mm hex drivers;
- tweezers;
- thin CA, 5-minute epoxy, IPA;
- PTFE dry-film spray;
- a cardboard box as a spray booth;
- nitrile gloves;
- safety glasses (magnets snap).

**Before you start:** wash every SLA part in IPA and let it dry 24 h. Remove supports with flush cutters, then sand the support nubs flush with 600 grit. Count the parts against §10.

**Step 1: Nails (30 min).**
1. Check each nail with the shadowgraph (§6.4) and calipers: land Ø 3.90–3.92 at three places.
2. Press a Ø 2 × 4 dowel into each top with the vise and a flat jaw pad, until flush (feel with a fingernail: no step).
3. Polish the tip rim with 1500 grit, holding the nail in a drill at low speed, the paper folded over the tip. Wipe with IPA.
- **Good:** a smooth, round, red cone with no burr when you drag it across the back of your hand.

**Step 2: Floor plate and wipers (20 min).**
1. Press a 4 mm PTFE bush into each of the six Ø 5.95 bores, flush on both faces.
   - Cut the bushes from 4 × 6 tube with a fresh blade, rolling the tube under the blade for a square cut.
2. Ream each bush by spinning a nail in it (drill, slow, 5 s).
- **Good:** the nail slides through under its own weight but does not wobble.

**Step 3: Cartridges (40 min).**
1. Press a PTFE bush into each cartridge's Ø 5.95 seat from the top, down to the step at z 54 (a Ø 5.5 rod as the pusher). Ream it.
2. Check the rod-side vent hole is open (blow through it).
3. Glue a D21B-N52 into each piston's face pocket with a pin-head of CA.
   - **All six with the same pole out:** mark one face with a dot of nail varnish using a reference magnet. It does not matter which pole, only that they match.
4. Fit the return spring over a nail land. Make a Penrose sleeve (§5.3), fit the piston, and push the assembly into the cartridge.
5. Fold the sleeve flange.

**Step 4: Block stack (30 min).**
1. Stand the floor plate on the bench, top up.
2. Drop the six cartridges into their sockets: the centre one first, then P0 (+x). P0 is the pin next to the V-notch moulded in the floor plate's rim at 0°.
3. Lay the gallery plate on top so its three columns meet the floor-plate holes and the six beads land on the sleeve flanges.
4. From below, drive 3 × M2 × 8 screws up through the floor plate into the columns. Tighten alternately until the plate just stops moving, then a quarter turn more. Do not crush the cartridges.
- **Good:** with an aquarium pump on one port and a finger on the other, every sleeve in that group pushes its piston down.

**Step 5: Wipers and skirt plate (10 min).**
1. Punch six Ø 9 discs from 1.0 mm 40A silicone sheet, each with a Ø 1.5 centre hole and four 1 mm slits (§5.4).
2. Lay them in the skirt plate pockets.
3. Snap the skirt plate onto the floor plate rim: hooks at 36/156/276°.
4. Push each nail up from below through its wiper and bushes until it clicks onto its magnet.
- **Good:** each nail hangs by its magnet; a 20 g cup drops it; reinserting it is a click.

**Step 6: Bleeds and tubes (30 min).**
1. Drill Ø 0.32 radially through each port column at z 70 into the vertical channel (pin vise; mark with the template on the column).
2. Cut 4 mm of a 30 G needle and epoxy it in, flush outside.
3. Push the 1/8 in PIN A tube onto the 252° barb and PIN B onto the 108° barb, past the ridge. Bind each with 3 turns of waxed thread.
- **Good:** with 3 kPa in a line and the far end capped, the line falls below 2 kPa within 1 s (§13.2).

**Step 7: Yoke and coupling (20 min).**
1. Glue three D42-N52 into the yoke pockets, all the same pole down. Check: each attracts the washers on the gallery plate.
2. Press three M3 washers into the gallery-plate pockets (CA).
3. Stick a 0.25 mm PTFE sheet disc (Ø 28) under the yoke. Set the yoke on the gallery plate.
4. Calibrate the coupling to 2.0 ± 0.3 N (§7.3) after the tendons are on.

**Step 8: Deck (40 min).**
1. Sand the three pocket ceilings with 1000 then 1500 grit wrapped on a Ø 6 dowel (a pencil). Work in small circles; the ball must glide.
2. Spray two light coats of PTFE dry film; let dry 10 min.
3. Press a 1/4 in PTFE ball into each lug socket of the gallery plate with the vise (soft jaws). The lip snaps over the equator.
4. Glue the three Ø 8 × 1 steel discs into the deck's R 42 bosses (epoxy).

**Step 9: Skirt frame, skids, stops (60 min).**
1. Heat-set an M3 insert into the top of each skid stem and into each stop block.
2. Stems:
   - slide each stem up through its bottom-ring guide;
   - put an M3 × 40 nylon screw down through the top-ring boss into the stem;
   - fit the knob (PD14, nylon nut glued in its hex) on the screw head above the boss;
   - glue the foot (PD13) onto each stem bottom with CA. The foot's tilt points inward toward the pad axis.
3. Bolt the three stop blocks onto the stop arms (2 × M2 × 8 each).
4. Hook the three lift springs onto the skirt-frame hooks (inner face of the top ring, at 60/180/300°).
5. Wrap the 0.5 mm PP cover band around the frame, cut from the template in `cad/README.md` §6. Clip it with the frame's struts on the outside; cut its two tube windows (108°, 252°).

**Step 10: Close the pad (20 min).**
1. Lower the block into the skirt frame. Hook each lift spring's lower end into its floor-plate eyelet (bent paperclip as a hook tool).
2. Lower the deck onto the six posts so the three balls enter their pockets.
3. Drive 6 × M2 × 10 up through the top ring into the posts.
- **Good:** the block hangs from its springs with all three balls touching their ceilings, and a finger moves it ±17 mm in every direction with no scrape and no click. The domes rise and the nails lift near the rim.

**Step 11: Tendons (with DRIVE BOX, 30 min).**
1. Feed each cable through its stop block (barrel adjuster, spring, ferrule cup) and the cable exit.
2. Hook it into the yoke notch at R 10; crimp the ferrule into the ferrule pocket.
3. Set 2.0 N per cable with the barrel adjusters (ELECTRONICS reads tensions).
4. Calibrate the coupling (§7.3).

**Step 12: Skids to the station group (5 min, repeated per group).** §13.6.

---

## 13. Bench checks (what good looks like)

| # | Check | How | Pass | Stage |
|---|---|---|---|---|
| 13.1 | **C1 breakaway** each nail | §6.3, 10 pulls each, straight and with a 50 g side load | 15.3 ± 3 g straight; ≤ 35.7 g with side load; range ≤ ±1.5 g | A2 |
| 13.2 | **C3 bleed** | 3 kPa in line A, far end capped, gallery sensor tee | < 2 kPa in < 1 s | A2 |
| 13.3 | **Red line 9 proofs** | 3.1 N axial pull on each dowel (insert proof, nail held in a vice); 3.1 N compression on the tip (nail on its magnet, piston on a stop); 3.0 N lateral at the tip in the guides (no set, back to straight); stop arm 10 N along the cable; tape test on tips and skid feet | no movement or set; tape not snagged | B3 |
| 13.4 | **Force constant** | one pin at 10.0 kPa pushing a 0.01 g scale through a spacer | 0.32 ± 0.04 N net of spring (0.0322 N/kPa × 10 − 0.08) → firmware table | A2 |
| 13.5 | **Springs** | return spring: compress on the 0.01 g scale; series spring: on the kitchen scale; lift spring: hang 20/30 g | 0.005 ± 0.002 N/mm; 2.0 ± 0.3 N/mm; 0.012 ± 0.003 N/mm | A2/A3 |
| 13.6 | **Skid height for a station group** | 1. On the head (or the matching mock) at the station, retracted. 2. Lower the pad by hand until the skids touch. 3. Read how far the centre nail's tip must travel to touch: slide a 0.5 mm feeler-strip stack between the tip and the scalp. 4. Turn the three knobs equal amounts (count clicks; check with gauge PD18 against the skirt-frame face) until the earliest nail just touches at e = 15.0, i.e. the centre nail tip is 15.0 mm from the retracted position, measured with the calipers' depth rod through the skirt-plate hole. | all six nails reach (feel each with a fingertip under the pad); retract margin ≥ 15 | C1 |
| 13.7 | **Lift seated** | pad axis vertical (vertex pose), pins vented, block on the plateau (\|d\| 17) | all three balls stay on their ceilings (look through the cover window with a torch); no sag | A3 |
| 13.8 | **Yaw** | ink mark on the block top, 5 min PLINE | ≤ ±5° | A3 |
| 13.9 | **Coupling** | §7.3 | 2.0 ± 0.3 N in three directions; zero nuisance releases in 20 min each mode | A3 |
| 13.10 | **C5 gate** | 240 fps on R 85 / R 65 / side mocks, feelers | landing ≤ 35°; lift ≥ 5 mm at reversal; rake ≥ 17 mm (ink) | A3 |
| 13.11 | **C6** | 15 mm block under each nail, float at R2b | ≤ 0.77 N (R1b cap at the new area) | A3/B |
| 13.12 | **C7** | group B vented while A runs, 240 fps | every B nail ≥ 8 mm up within 200 ms, new and after 20 min | A2/A3 |
| 13.13 | **C8 feelers** | Stage B pad: 8 mm rod between each nail and skid at the cage in 6 headings; 30 mm block on R 85 ball under the skirt plate | clears | B |
| 13.14 | **Mass** | weigh the pad on the kitchen scale | record (expect 125–135 g; B1 ≤ 90 fails, CONFLICTS P4) | B1 |
| 13.15 | **Stick-slip** (V-D3) | phone accelerometer taped to the deck, 140 mm/s lines | no line at 50–500 Hz above the drum ripple | S0/A3 |
