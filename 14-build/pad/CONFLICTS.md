# PAD work package: conflicts with SYSTEM-SPEC-v3 and with the other packages

**Project SCRATCH · 14-build/pad · PAD engineer · 2026-10-02**

Every number below comes from `cad/pad_geom.py`, `cad/pad_geom2.py`, `cad/gen_pad_stl.py` or `cad/check_assembly.py`. Their outputs are saved in `cad/pad_geom_report1.txt`, `cad/pad_geom_report2.txt` and `cad/gen_report.txt`.

I did not edit SYSTEM-SPEC-v3.md. Each row says what the spec says, what I built, and who must act.

Priority: **A** = blocks another package or changes a safety number. **B** = changes an interface. **C** = for information.

---

## A-level

### P1 · Dish geometry redefined at the nail plane (answers the coordinator's 2nd finding and 14-build/S0/CONFLICTS.md #1)

- **Spec 4.2:** sphere R 160 for |d| ≤ 7; 34° rim to 13.7 mm (+4.5); 50° rim to 17.0 mm (+8.5); domes Ø6 at R 22.
- **Problem:** the R 160 dish rolls the block about the head centre, so the nails travel only ≈ 0.54× the block offset. S0 measured a 10.2–10.4 mm rake and 48–62° landings.
  - Redefined at the nail plane with a full roll, the domes (≈ 92 mm above the nail plane) travel 1.85–2.1× the nail offset: ≈ 31–38 mm.
  - At R 22 the three dome pockets then overlap. The full-roll fix needs domes at R ≥ 43–47 and a deck of Ø ≈ 165 mm. That is S0's number, and I confirm it.
  - I also tried "unwinding" the tilt on the rim to keep the pockets small. It drives the ceiling slope the dome sees to 60–89°, so the rim reaction becomes unbounded. Rejected.
- **Built: the smaller corrected variant (dish v3b).**
  - Block offset d is measured at the nail plane.
  - Tilt = **0.5 × asin(|d|/85)**, i.e. half the concentric roll.
  - Contact zone |d| ≤ 6.5 mm.
  - Landing band at **30°** up to +4.5 mm at |d| = 14.29.
  - Outer rim at **60°** up to **+9.0 mm** at |d| = 16.89, then a plateau.
  - Working amplitude **17.2**, cage **18.0**.
  - Domes are three 1/4 in PTFE balls on lugs at **R 38** (30/150/270°), ball centre **91.5** above the nail plane. Each ball rides its own pocket.
  - Max dome travel 28.0 mm. Pockets clear each other by 1.8 mm. Deck footprint Ø 132 (not 165).
- **Result on R 85:**
  - rake **17.9–24.7 mm** on every nail and heading (≥ 17 ✓);
  - landing/lift ≤ **34.0°** (C5 ✓);
  - lift at reversal ≥ **5.34 mm** for every nail (C5 ✓);
  - extra gap spread in contact +0.7 mm from the half roll (force is air, so this only spreads the landings; 30–40 ms is wanted);
  - steepest dome-path slope **48.1°**.
- **Who acts:**
  - **FIRMWARE** (IK and path checker): see P15.
  - **S0** dish bench: re-print the bench dish from `pad_geom.py` constants, or bench a single pocket. S0's Ø70 deck no longer represents the dish.

### P2 · Tendon layout: deck stops R 65, yoke posts R 10 (coordinator's first finding)

- **Chosen:** stops at **R 65**, posts at **R 10**. Rejected: R 70 / R 15.
- **Why R 65 / R 10:**
  1. The stops then sit just outside the R 60 skid circle on short arms (envelope Ø ≈ 132–140). R 70 adds 10 mm of diameter and longer cantilevered arms.
  2. Posts at R 10 fit inside a Ø 28 yoke, between the three coupling magnets at R 8, so the yoke is 1.9 g. Posts at R 15 need a Ø 36 yoke.
  3. Both layouts force the yoke **above** the block. The cables must cross the pentagon of cartridges, and no 120° set of directions passes between pentagon cartridges (checked: the 72° gaps never contain three directions 120° apart). So hair-zone rules are identical for both; the yoke is ≥ 83 mm above the skin.
- **Interfaces built:**
  - Cable departs the yoke at R 10 (apex of a flared notch, ±22° horizontal, floor sloping 9° outward), z **85.5** at home.
  - Stops at R 65, angles 90/210/330°, cable exit z 85.5.
  - Yoke tension and drag are capped by ELECTRONICS' ≤ 5 N cable pull (VREF ≤ 0.19 A). PAD parts are proofed to 5 N.
- **Change to M14:** the 2 N/mm series spring moves from the yoke post to the **stop**. It is a compression spring under the housing ferrule in each stop block, so the spring rides on the static deck. Same compliance; less moving mass.
- **Who acts:** ELECTRONICS (IK): post R 10 at block-frame z 85.5, stop R 65 at deck z 85.5. The posts move with the block's tilt and rise (P15).

### P3 · Pad stack height: ball seats at ≈ 109.5 mm above the skin, not ≈ 80

The spec's radial chain (block underside 32 → pin tops 62 → deck 75 → float ring 80) cannot hold the parts that C1, C2 and P2 require:

| Layer | Spec | Built | Why |
|---|---|---|---|
| Block underside (wiper plate) | 32 | 32 | H-6.3 / C8 |
| Floor plate + lower bush | — | 34–38 | lower PTFE bush at the nose (C1(ii), P7) |
| Cartridge | Ø10 × 38 | Ø9.4 × 42 (38–80) | C2 land travels 18.5 mm inside the cartridge, plus a 16 mm guide span, spring, piston |
| Gallery plate | — | 80–83.5 | galleries A/B, sleeve clamp |
| Yoke | ring round the block | 83.5–87 | P2: posts at R 10 must sit above the cartridges |
| Clearance to the pocket ceiling | — | ≥ 1.87 (computed) | block rises 9 mm and tilts 6°; the ceilings pass over the yoke |
| Ball centre / ball top | domes on the block top | 91.5 / 94.7 | |
| Pocket ceiling | 75 | 93.0–105.3 | 9 mm rise |
| Deck top / HALO ball seats | 75 / 80 | **108 / 109.5** | |

- The spec's own design would already reach ≈ 97: its Ø 1 shaft still needs the stroke plus the guide stack, and the 8.5 mm rim rise needs the same clearance.
- **Who acts: HALO.** Move the spider ≈ 29.5 mm further out along the float axis: the bail radius, or the float's 25 mm retract margin. The HALO conflict file already shows a 3 mm margin at R 210 and the coordinator has moved to R 220. **This needs ≈ R 250 or a shorter float.**
- **Ways to recover height** (none adopted yet):
  - LM4UU ball-bushing guide with a hardened Ø 4 land: −4 mm, +15 g.
  - Block underside at the C8 minimum of 30: −2 mm.
  - Equal-reserve nails (centre nail 1.93 mm shorter): −1.5 mm, but loses reach on flatter heads.

### P4 · Pad mass ≈ 130 g, not 81.5 g

- Printed parts from CAD volumes: **108 g**. Of that:
  - deck 33.4 (SLA, three 1.0 mm pocket shells);
  - gallery plate 14.6;
  - skirt frame 12.5;
  - cartridges 10.7;
  - floor plate 9.8;
  - nails 6.0;
  - skid feet and stems 10.1.
- Bought parts ≈ 24 g (pad.md 10).
- B1's gate (pad ≤ 90 g) **fails as designed**. Diet path to ≈ 100 g:
  - deck shells 0.8 mm: −5;
  - ribbed gallery lugs and hollow columns: −4;
  - 0.25 mm PET cover instead of 0.5 mm PP: −3;
  - nylon M3 adjuster screws: −4;
  - MJF deck with PTFE film on the pockets: −4, [VERIFY] pocket smoothness.
- **Who acts:** HALO (mass and lean ledger); the director (B1 gate value).

### P5 · Fixed skids cannot hold the dish gate across head shapes: skid-height adjuster added

- **Spec:** "reserve 1–3.5 mm (worst residual curvature)" everywhere.
- **Computed:** with skids at Ø 116–120, the scalp at the pad axis moves relative to the pad by **+7.1 mm (R 65) to −8.7 mm (R 150)**.
- The gate works only where that offset is between **−1.6 and 0 mm**:
  - C6 needs the earliest nail to touch at e ≥ 15;
  - reach needs every nail to touch by 18.5;
  - lift needs reserve ≤ 4.
  - With fixed skids that means **R 85–90 only**.
- Results with fixed skids:

| Head | Fails on |
|---|---|
| R 65–80, bun 65 × 80 | C6 (retract margin 7.9–13.7) and lift |
| R 100+, crown 90 × 100, parietals | reach (pentagon nails never touch) |

- **Built:** each skid stem has a captive M3 adjuster, 0.5 mm per turn, ±9 mm, set with a stepped gauge (PD18) per **station group** (pad.md 4).
- **With the adjuster:** every isotropic head R 65–150, the crown and the bun pass.
- **Parietal sides (70 × 150 anisotropy) still fail:** the contact spread across the six nails is 3.7–4.2 mm, so one nail sits 0.2–0.7 mm short at some headings.
- **Who acts:**
  - TESTS: add "set skid height for the station group" to the station-move procedure.
  - HALO: the station table needs one skid setting per group.
  - Director: accept that parietal stations run with one nail skimming, or add a region-keyed dish later (spec R1 fallback).

### P6 · Nail form: one-piece POM land Ø 3.92 with a steel insert; no Ø 1 A228 shaft

- **Spec C4 / §4.1:** POM cone on a Ø 1.0 A228 shaft, drafted 2.5° to the nose.
- **Problem:** a Ø 1 shaft above a Ø 4.5 cone is a neck. It breaks the ruling's C2 ("no section narrower than any section below"). C2's cylindrical wiper land must therefore be at least as wide as the cone, and it travels the whole stroke.
- **Built:**
  - Ø 2.0 flat with R 0.4 rim, 90° cone to **Ø 3.92**, then a **constant Ø 3.92 land** (C2's "constant stem" option) to the top: 59.9 mm long.
  - A Ø 2 × 4 hardened dowel is pressed flush into the top as the magnet target. The top rim is R 0.5.
  - CNC-turned POM, red if offered. 1.0 g (spec 0.3 g).
  - The cone reaches Ø 3.92, not the spec's Ø 4.5 at 1.25 mm, so the land fits stock 4 × 6 mm PTFE tube bushes. The ruling allows Ø 4–5.

### P7 · Guides and the C1(ii) side-load limit

- The ruling asks for release ≤ 0.35 N with 0.5 N tangential at the tip.
- The tip is ≥ 32 mm below any guide, so guide friction adds μ × (2a + L)/L × F_t.
  - For the spec's two POM bushes 12 mm apart on Ø 1 steel: (2·36 + 12)/12 × 0.2 × 0.5 = 0.70 N on top of B. **Fails by 2×.**
- **Built:** two PTFE (4 × 6 tube) bushes on the POM land.
  - Lower bush in the floor plate at the nose; upper bush in the cartridge.
  - Span 16 → factor 5.5.
  - At μ 0.06–0.08 the added friction is 0.17–0.22 N.
- **Breakaway target narrowed to B = 0.15 ± 0.03 N** (spec band 0.12–0.25). Predicted side-load release 0.30–0.40 N, so it is marginal [VERIFY A2 (a)].
- **Fallback if A2 fails:** an LM4UU linear ball bushing with a Ø 4 hardened land. Friction then becomes negligible, but it costs +15 g and a heavier dropped nail (pad.md 5.7).

### P8 · Pin force constant and caps

- **Spec:** Ø 7.0 bore → 0.0385 N/kPa.
- **Problem:** a rolling Penrose sleeve needs a convolution gap. With a Ø 5.8 piston the effective diameter is ≈ 6.4 mm → **≈ 0.0322 N/kPa** [VERIFY A2: force at 10 kPa].
- **Caps per nail:** R1a 20.7 kPa → **0.67 N**; R1b 24 kPa → 0.77 N; deadhead 50 kPa → 1.61 N. All are lower, so safer.
- **Net force:** the return spring (P9) takes 0.08 N at contact.

| Net force wanted | Rail pressure |
|---|---|
| 0.20 N | 8.7 kPa |
| 0.37 N (all-six budget) | 14.0 kPa |
| 0.50 N | 18.0 kPa |

- The spec's 0.60 N firmware ceiling is unreachable below R1a (max net ≈ 0.59 N).
- **Who acts:** FIRMWARE limits table (rail clamp, net-force floor), from the A2 measurement.

### P10 · Lift tension: three inclined springs, not one centred spring

- **Spec:** one centred 0.5–0.6 N deck-to-block spring.
- **Why that cannot be built:** the three pockets cover the deck centre, the block top swings ±17–27 mm, and HALO's float hub sits on the axis directly above the deck.
- **Built:** three extension springs from floor-plate lugs (R 28.5, z 36) to hooks on the skirt frame (R 55.5, z 77), at 60/180/300°.
  - Spring: L0 30 mm hook-to-hook, k 0.012 N/mm, initial tension 0.09 N.
  - Lift **0.63–0.81 N** over the pose range. Horizontal centring pull ≤ 0.47 N.
- **Margin:** the block plus yoke weighs ≈ 57 g (W = 0.56 N), so the net upward force on the rim at the vertex is only 0.07–0.25 N [VERIFY A3: block stays seated on the plateau at α = 0 with pins vented].
- The centring pull adds to the load the 2.0 N coupling must pass (P14).

### P11 · No PP parallelogram; yaw held by the tendons

- There is no room for a ±18 mm XY yaw-locking flexure: the pockets fill the deck, and the block sweeps the annulus to the skirt.
- **Yaw is held by** the tendon "pendulum" stiffness: 71 N·mm/rad = 1.24 N·mm/° at 2.0 N pretension, plus dome friction (≈ ±2.6 N·mm dead band).
- **Expected yaw wander ±2–4°:**
  - nail position error ≤ 1.2 mm at R 18;
  - IK cable-length error < 0.2 mm;
  - pocket and C8 margins were swept at ±5° yaw.
- **Who acts:**
  - ELECTRONICS: the IK assumes yaw 0; the error is inside the 0.45 mm copy budget only for yaw ≤ 3° [VERIFY on the A3 ink rig with a yaw mark].
  - Fallback if yaw exceeds 5°: a fourth, passive, spring-tensioned cable (no motor) on a pinwheel post. PAD can add one boss.

---

## B-level (interfaces)

### P12 · M8 float-to-pad: a spherical seat about the nail plane replaces the RCC struts

- RCC struts from a Ø 110 ring at z 80 to this deck would be ≤ 13 mm long and would bind after 2–3° of tilt.
- **Built:** HALO's three Ø 5 balls (R 55, 30/150/270°) sit directly on the deck, on a **sphere SR 122.5 centred on the nail-plane point**:
  - the 270° seat is a meridional 90° V-groove (yaw key);
  - the other two are spherical facets.
- The pad tilts about the nail plane, which is a true remote centre: drag at the nails makes no tipping moment.
- **Tilt range ≈ ±3°.** It is limited by HALO's magnet-to-disc gap: the Ø 8 × 1 steel discs at R 42 move ±2.2 mm when the pad tilts.
  - Nominal gap 2.5 mm.
  - Breakaway is likely ≈ 3 N, not HALO's 6 ± 2 N [VERIFY B3].
- **HALO acts:** keep the balls and magnets; shim magnet height to the 2.5 mm gap; accept ≈ 3 N or use Ø 8 × 3 magnets.
- **Float:** the float is HALO's package (spec 2.1, 11), so the Penrose float decision is HALO's. PAD needs from it:
  - ≥ 25 mm retract;
  - the pad's weight, now **1.3 N** (≈ 130 g, P4), not 0.8 N. This raises the vertex normal-load sum by 0.5 N (≤ 4.2 N at R2) and needs ≥ 1.6 N retract force (HALO's constant-force spring is 1.60 N, so zero margin). HALO must raise it to ≥ 2.0 N.

### P13 · Angles in the pad frame

| Feature | Angles |
|---|---|
| Domes / lugs | 30/150/270° |
| Tendons and stops | 90/210/330° |
| Skids | **60/180/300° at R 60** (spec Ø 116 "open corners") |
| Lift springs | 60/180/300° |
| Ports | 108° (B), 252° (A) |
| Deck posts | 78/102/198/222/318/342° |

- Nail-to-skid clearance ≥ **15.0 mm** at every pose, yaw ±5° (C8 ≥ 8 ✓).
- HALO's spider arms at 30/150/270° sit over the pocket shells, about 0.5 mm above the deck top at the seats.

### P14 · Coupling (M12) and the rim-reaction budget

- **Coupling:** three K&J **D42-N52** (6.35 × 3.18) in the yoke, over M3 steel washers in the gallery plate, through a 0.25 mm PTFE slider plus shims. Calibrated to 2.0 ± 0.3 N sideways pull (pad.md 7.3).
- **Loads the coupling must pass:**
  - outer rim, pins up: ≤ 1.11 × dome load (≈ 0.8 N) + centring 0.47 → ≈ 1.3 N;
  - landing band with pins down: tan 24° ≈ 0.45 × (pin sum + lift − weight, ≈ 2.5 N) ≈ 1.1 N + drag (up to 1 N) → **can exceed 2.0 N**.
- **Risk R3:** nuisance releases with all six nails at 0.37 N. A3's 20-minute test decides 2.0 vs 2.5 N.
- **Cage:** the yoke can slide 6 mm inside the cage ring before it pushes the block directly. ELECTRONICS' tension-pattern trip must act within ≈ 30 ms.

### P15 · Numbers FIRMWARE needs (IK and path checker)

- **IK pose:**
  - tilt φ(d) = 0.5·asin(|d|/85) about the axis ⟂ d;
  - block origin at (d, √(85² − d²) − 85 + h(d));
  - h(d) piecewise: 0 to 6.5; 30° to 4.5 at 14.29; 60° to 9.0 at 16.89; plateau.
  - Cable posts: block-frame R 10, z 85.5.
- **Path checker:**
  - **no-reversal radius 16.9 mm** (plateau start, lift ≥ 5.3). This replaces the spec's 13.7.
  - Working amplitude 17.2. Hard cage 18.0.
- **Landing radii (R 85):** 7.8–12.6 mm by nail and heading.
- **CIRCLE mode:** R + e must be ≥ 17.0; R − e ≤ 7.8.
- **Rim-reaction model for the dish-aware snag criterion (C4):**
  - horizontal reaction ≈ (vertical dome load) × tan(slope(d));
  - the dome-path slope is ≤ 15° in the contact zone, ≤ 24° in the band, ≤ 48° on the outer rim and ≤ 18° on the plateau (table in pad.md 3.4).

### P16 · Cartridge interface (M9)

- **Spec:** Ø 10 × 38, O-ring retention.
- **Built:** **Ø 9.4 × 42**, seated in Ø 9.55 sockets in the floor plate and clamped from above by the gallery plate's bead ring. The bead ring also crushes the Penrose sleeve's folded flange: the sleeve is the seal.
- Pin positions are ±0.1 mm by the floor plate.

### P17 · Gallery bleeds

- Each gallery bleed is a 30 G needle stub (ID ≈ 0.16 mm) in a radial Ø 0.32 hole drilled through each port column wall at z 70, into the vertical feed. It vents inside the block, above the hair guard.
- Drilled at assembly, not printed. Pad.md 12, step 6.

---

## C-level (information)

- **P9** Return spring is 0.08 N at contact (spec 0.03).
  - C7 needs ≥ 2× friction over the whole retract, and the only space is 22 mm of free length.
  - The spring is music wire 0.15 mm, OD 5.0, ≈ 9 active coils, k ≈ 0.005 N/mm.
- **P18** Wipers sit in the snap-off skirt plate (RT2). Each is a 1.0 mm 40A silicone disc with a Ø 1.5 hole and four 1 mm slits. It recloses to Ø 1.5 when a nail drops; at 33 mm up that is outside H-4.9's 25 mm zone.
- **P19 Block underside (C8 ≥ 30):** ≥ 34.4 mm on R 85 at every pose. On R 65 it is 27.8 with the skid at zero, and 34.9 with the R 65 setting (+7.1).
- **P20 Fence:** the nail tips reach **41.3 mm** from the pad axis (block 18 + tilt + yaw 5° + cone), not 35. HALO's hairline and ear stops must use 41.3 + 15.
- **P21** Rod-side vent: Ø 1 hole at z 55 → OD groove → gallery-plate underside groove → block rim. The rod side never breathes through the wiper (RT2 1.5).
- **P22** Moving group (block + yoke) ≈ 57 g (spec 47). Plate resonance ≈ 31 Hz (spec 34) [EST]. Fault energy at 0.2 m/s ≈ 1.1 mJ (limit 50).
- **P23** The block reaches the skirt-frame bottom ring at |d| ≈ 18.0 through the lift-spring lugs. That contact is the hard cage, and `check_assembly.py` reports it (4.4 mm³ at d = (−18, 0)) as the intended stop.
- **P24 Web-search budget:** ran out during price checks. Prices are [cited] where a page was fetched and [est] / [verify] otherwise (parts.md).
