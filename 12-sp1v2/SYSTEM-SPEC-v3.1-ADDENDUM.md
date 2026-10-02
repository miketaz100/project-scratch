# SP1 v3.1 — ADDENDUM to SYSTEM-SPEC-v3 (integration freeze)

**Project SCRATCH · 12-sp1v2 · Integration engineer · 2026-10-02**

**What this is.** This is the numbered addendum that SYSTEM-SPEC-v3 §14 calls for. It is not a rewrite. It does three things:
- It resolves every conflict the six build packages raised against freeze v3 into one consistent design, **v3.1**.
- It names the package that must change and gives the new values.
- It flags, without deciding them, the items that need Michael. Those are items that change cost by more than $50, change the experience, or relax a safety limit.

Where this addendum and SYSTEM-SPEC-v3 disagree, **this addendum governs**. Every spec line it does not touch stays frozen.

**Read:**
- DECISION-3.md, SYSTEM-SPEC-v3.md, safety-ruling-dish-gate.md (C1–C8).
- All six packages and their CONFLICTS.md:
  - 14-build/S0;
  - pad;
  - halo;
  - drivebox;
  - electronics, including firmware/ and its tests;
  - tests.
- 14-build/cost-down.md, only where it touches an interface.
- DIRECTOR-LOG entries dated 2026-10-02.

**Director rulings already made, folded in as resolved:**
- **Float:** the Penrose-sleeve float (≤ 20 g) replaces the Airpel.
- **Tendon anchor layouts:** the anchor layouts that passed the ELECTRONICS audit were stops R 70 / posts R 15 and R 65 / R 10. **They do not pass once the PAD dish is modelled; see I-1.**
- **No XY stage.**
- **Hinges and halo:** E6-10-301-20 hinges plus brakes; hubs at |Y| 141.5; bail R 220, which is now superseded by the pad height (§2); side stops ±35°, now ±28° by the same rule (M2); front stop set from the hairline.
- **S0 bench:** spring nails.
- **Pump deadhead:** the Director has made this a safety item (S-1).

**Tags:** **[KNOWN]**, **[EST]**, **[JUDG]** and **[VERIFY]** as in the spec.

**New evidence from this pass:**
- `12-sp1v2/scripts/v31_tendon_audit.py`: the firmware's own tendon statics, run with PAD's v3b pose.
- `14-build/halo/cad/halo_design.py`, re-run with these settings:
  - `--light-float --set PAD_STACK=115.5 --set CH_DEG=16.7`;
  - pad mass 136 g, float 20 g, reach 41.3 mm (scratch copy).
  - Results are in §2 and §5.

---

## 1. Decisions for Michael (flagged, NOT decided here)

Each item has a recommended default. Nothing in it is built or bought past S0 until Michael answers.

| ID | Decision | Why it is his | Options | Recommended |
|---|---|---|---|---|
| **M1** | **Helmet mass and size.** As designed it weighs **≈ 472 g single** (spec 286 g, target ≤ 400 g, red line 10 ≤ 500 g). The diet path reaches **≈ 425 g**. **≤ 400 g is not reachable** with the parts the safety and torque checks need. The helmet is also bigger: the bail is R 249 and 393 mm wide, and the pad sits 30 mm further out. Worst lean is 0.56 N·m against a cradle lock of 1–1.5 N·m. **Pad 2 (twin) can no longer fit under 500 g.** | experience | (a) accept ≈ 425 g as the target, with a hard gate ≤ 480 g at B1/C2; (b) also try ≈ 390 g by going back to the small E6-10-101 hinges with doubled brakes and a monthly retighten. That needs the Director to reopen his hinge ruling: the worn margin falls to ≈ 1.0–1.4, and a slipping bail moves the pad mid-session. (c) Stop and redesign the pad stack. | **(a)**. Keep only the pad-2 provisions that weigh nothing (§3 H13). |
| **M2** | **Side and front stops.** The real nail reach is 41.3 mm (PAD P20), not 35. Keeping the ear at ≥ 25 mm after a 15 mm halo slip (red line 6 + C4) needs **β ≈ ±28° and α_front ≈ −25° on the design head**. Coverage falls from ≈ 82 % to **≈ 78 %** [EST]. | experience; the alternative relaxes a safety margin | (a) set the stops by the procedure (≥ 40 mm from the canal seated): ≈ ±28°; (b) keep the Director's ±35°, which leaves ≈ 31 mm seated and ≈ 16 mm after a 15 mm slip, **below red line 6**. | **(a)**. The stops are measured on his head, so his real angle may be wider. |
| **M3** | **Drive-box mass.** It comes to ≈ 3.8 kg (3.6–4.0), not ≤ 2.8 kg (DRIVE BOX C1). | experience: he carries it and hangs it | (a) accept ≤ 4.0 kg with the free trims, ≈ 3.5 kg; (b) a custom ply box, −0.8 kg, +6 h. | **(a)** |
| **M4** | **Test kit ≈ $230** (Lean ≈ $143) is not in the spec BOM. It includes the C1(c) fast force logger. | cost > $50 | Choose through the cost-down scenario (14-build/cost-down.md §3). The safety-gate items cannot be dropped: logger, TAL221 load cells, manometer, gauge, real-hair wig. | Lean test kit |
| **M5** (conditional) | **Diverse reliefs R1b/R2b.** No stock "different make" relief at ≈ 24 kPa exists (DRIVE BOX C8). Generant needs a quote. | Ask Michael only if the diverse pair costs > $50 over the $30 budget, or none can be had. Same-make reliefs on the head would relax RT2 #8. | pay; delay head sessions; or accept same make (a safety relaxation) | pay, if ≤ ≈ $80 |
| **M6** (conditional) | **S0a "frozen dish wins".** If the frozen V1 dish rates within 1 point of V2, S0-guide §11 currently lets the Director keep the small frozen dish. That dish lands the nails at 48–62° on the scalp, against C5's ≤ 35°: **a safety relaxation**. | safety limit | keep v3b regardless (recommended); or a new safety ruling | keep the **v3b** dish. A tie means "the smaller pad would have been fine", not "build it". |
| **M7** (minor) | **Parietal stations.** On 70 × 150 side curvature one nail of six can skim, 0.2–0.7 mm short, at some headings, even with the skid adjuster (PAD P5). | experience, minor | accept for the first build; or add a region-keyed second dish later (spec R1 fallback) | accept; B-S sessions judge it |

**No other item below changes cost by > $50, changes the experience, or relaxes a safety limit.**

---

## 2. The v3.1 frozen values (what replaces what)

| Quantity | v3 (spec) | **v3.1** | Source |
|---|---|---|---|
| Dish | R 160 sphere to 7; 34° to 13.7 (+4.5); 50° to 17.0 (+8.5) | **PAD v3b at the nail plane:** <br>• half-roll tilt φ = 0.5·asin(\|d\|/85), with the block z axis tilting **outward**; <br>• nail-plane origin at (d, √(85² − d²) − 85 + h); <br>• h = 0 to 6.5; 30° to +4.5 at 14.29; 60° to +9.0 at 16.89; then a plateau to the cage at 18.0 | PAD P1, P15 |
| Domes / deck | 3 POM Ø 6 at R 22; deck Ø 116 | **3 × 1/4 in PTFE balls on lugs at R 38** (30/150/270°), centre z 91.5; one pocket each; deck **Ø 132**; pockets SLA, 1500-grit + PTFE dry film (no tape) | PAD P1, S0 #12 |
| Gate on R 85 | chord 17–24, landing ≤ 35°, lift ≥ 5 | rake 17.9–24.7 mm; landing/lift ≤ 34.0°; lift at reversal ≥ 5.34 mm | PAD P1 |
| No-reversal radius | 13.7 | **geometric 16.9; commanded ≥ 17.2** (I-4) | PAD P15 + I-4 |
| Amplitude / D_MAX / cage | 16.5 / 16.5 / 18 | PLINE/LINE A **17.2–17.6** (default 17.4); D_MAX **17.6**; cage **18.0** | I-4 |
| Landing radii | 8.5–12.2 | **7.8–12.6** | PAD P15 |
| Group-valve switch | only at \|d\| ≥ 13.7 | unchanged (13.7 > 12.6) | — |
| CIRCLE | R 9–13; R + e ≥ 14.5; R − e ≤ 8.5 | **R 9–12.7; 17.0 ≤ R + e ≤ 17.6; R − e ≤ 7.8; e ≥ 3; f ≤ 1.5 Hz**; precession 15–40°/rev; default R 12.0, e 5.2 | E-C9 + PAD P15 |
| Pad stack | ring at 80 above the skin | ball seats **109.5**; float spider top **115.5** | PAD P3 |
| Pad mass / moving block | 81.5 g / 47 g | **135 g** (diet target 110) / 57 g | PAD P4, P22 |
| Nail | Ø 1 A228 shaft + cone | **one-piece POM:** <br>• Ø 2.0 flat (R 0.4), 90° cone to Ø 3.92; <br>• constant Ø 3.92 land, 59.9 mm; <br>• Ø 2 × 4 dowel on top, R 0.5; <br>• 1.0 g. <br>Two PTFE 4 × 6 bushes, 16 mm span. | PAD P6, P7 |
| Breakaway (C1) | 0.12–0.25 N | the band is unchanged; **set to 0.15 ± 0.03 N** | PAD P7 |
| Pin force constant | 0.0385 N/kPa | **0.0322 N/kPa** [VERIFY A2]; return spring **0.08 N** | PAD P8, P9 |
| Per-nail caps | R1a 0.80 / R1b 0.92 / deadhead 1.93 N | **0.67 / 0.77 / 1.61 N** (deadhead ≤ 50 kPa: S-1) | P8 |
| Firmware ceiling / rail | 0.60 N @ 15.6 kPa; rail 2–13 | **0.50 N net @ 18.0 kPa**; working **0.10–0.50 N net = 5.6–18.0 kPa**; first-session floor 0.20 N = 8.7 kPa | P8 |
| Float | Airpel E16 (24 g in the ledger); 0.20 N/kPa; spring 1.2–1.7 N | **Penrose-sleeve float ≤ 20 g** (Director), **bore Ø 20, 3/4 in sleeve, ≈ 0.27 N/kPa** [VERIFY]; constant-force retract **≥ 2.0 N (2.2 N class)**; fixed Ø 0.2 bleed; QEV + float relief on its port | I-5 |
| Palm range | 8–20 kPa | **10–18 kPa** (stays below R2's 20.7 − 1.5 tolerance) | I-5 |
| Force budget, all six down | ≤ 0.37 N/nail | **≈ 0.37 N/nail** (0.27 × 18 − 2.2 − 0.45 = 2.21 N); ≤ 0.50 N with one group down | I-5 |
| Total normal (vertex) | ≤ 3.7 / 4.6 / 6.8 N | **≤ 4.7 N at R2; 5.6 N at R2b; 6.1 N at the float relief; 7.2 N at the 30 kPa deadhead limiter** (red line 3 ≤ 12 N) | I-5, S-1 |
| Tendon anchors | stops R 48 / posts R 30 | **posts R 10 at block z 85.5 (Ø 28 yoke); stops R 90 at 90/210/330°, deck z 85.5**; series spring in each stop block | I-1 |
| Pretension | 1.5 N/cable; "6 N spring" | **2.0 N/cable = 6.0 N at the floating plate's W tick** (adjustable 4.5–7.5) | I-1, DB C2 |
| Drums | Ø 12 | **Ø 20** (rotation_distance 62.83 mm); 19.6 µm per 1/16 microstep; cable span ±26 mm = 0.83 turn | I-6 |
| Cable pull cap | VREF ≤ 0.35 A "≤ 5 N" | **block-side stall pull ≤ 5.0 N per cable, measured**; VREF set at A3 between 0.25 and 0.45 A (start 0.35 V) | I-6, DB C5, E-C6 |
| Housings | PTFE-lined coil 1.2/0.6, 1.6 m | **1.9 m**; head segment (clip → pad, ≈ 1.0 m) **≤ 8 g/m each**, so **no 4 mm bike housing on the head**; SP41 allowed box → clip | I-10, DB C3/C4 |
| Comparator window | ΔT +1.8 / −1.2 N relative | **absolute 0.2 N (slack) / 3.6 N (over)** per channel; 4.0 N if the 7.5 N total is used | E-C15 |
| Tension front end | ADS1115 on CB1 I²C | **Pico (RP2040) on CB1 USB**; ADS1115 on the Pico's I²C if V-T5 fails | E-C2 |
| Halo | R 210; 20.7° chords; hubs \|Y\| 120 | **R_BAIL 249, CH_DEG 16.7** (6 × 64.3 mm to β ±50.1°), width 393 mm; hubs \|Y\| 141.5 (E6-10-301-20 + brakes); δ = **5.2°**; spider magnets **Ø 8 × 3** | §3 HALO rows |
| Stops | α_hairline + 20°; β ±40° | set by procedure: nail reach (**41.3 mm**) ≥ 15 mm behind the hairline and ≥ 40 mm from the canal seated → **design head α_front ≈ −25°, β ≈ ±28°** | M2 |
| Rail-off timing | rail dead < 5 ms | **K1 open ≤ 20 ms; ACT-24 < 4 V ≤ 35 ms; pins vented ≤ 135 ms; pad retracted ≤ 185 ms**, all from the trigger | E-C3 |
| Host-hang bound | ≤ 1 s | ≤ 1.3 s | E-C8 |
| Umbilical | 1.6 m | **1.9 m**; desk rule: box ≤ 0.5 m from the hanger clip | DB C4 |
| Box | ≤ 2.8 kg | **≤ 4.0 kg** (pending M3); user leads on the left end wall | DB C1, C10 |
| Pumps | deadhead P1 ≤ 50, P3 ≤ 30 kPa (V12) | **unchanged limits; mechanism per S-1** | S-1 |

---

## 3. Integration findings this pass adds (not raised by any single package)

| ID | Finding | Evidence | Resolution | Owner |
|---|---|---|---|---|
| **S-1** (safety, Director) | **Pump deadhead.** The BODENFLO BD-02A store listing gives a 120 kPa (1.5 L) or 150 kPa (3 L) deadhead (cost-down O4). DRIVE BOX C9 read it as 50 kPa. If the pump really reaches 120–150 kPa, then: <br>• R1a + R1b failed (a double fault) gives 3.9–4.8 N per nail, **breaking red line 2**; <br>• R2 + R2b + float relief failed, with the new 0.27 N/kPa float, gives ≈ 40 N, **breaking red line 3**. | cost-down O4 (cited) | **No pump is bought until DRIVE BOX does one of these:** <br>• **(a)** names pumps with a published max pressure **≤ 50 kPa (P1) and ≤ 30 kPa (P3)**, each ≤ 0.8 A at 12 V for FAN3; or <br>• **(b)** adds a **fixed-orifice deadhead limiter** (mechanical constant: a blunt needle to air at each pump outlet, behind the 10 µm filter), sized at A1 so that the equilibrium with every relief blocked is **≤ 45 kPa (P1) / ≤ 27 kPa (P3)**. <br>Measure it with the external gauge at A1, at every A1 re-test, and before each Stage B/C/D session block. <br>A supply-voltage limit alone is **not** accepted: it moves the barrier from M to E and would need a safety re-ruling. | DRIVE BOX, before Cart 2a |
| **I-1** | **The "passing" tendon layouts fail with the dish actually adopted.** ELECTRONICS audited R 65/R 10 and R 70/R 15 on the spec's dish (posts at block z 0, ±16.5 mm). PAD's v3b puts the posts at z 85.5 and tilts the block outward, so the posts travel **25.9 mm** at \|d\| 17.2. On that pose both layouts leave a cable at **0.13 N with no load at all**, below the 0.3 N audit floor and close to the 0.2 N slack trip, at \|d\| 17.6 between two stops. | `v31_tendon_audit.py`. At 6.0 N total: <br>• R65/R10: 0.13–2.94 N unloaded, capacity < 0; <br>• **R90/R10: 0.96–2.53 N, any-direction capacity 0.71 N on the plateau, 1.23 N in contact**; <br>• R100/R10: 0.91 / 1.37 N; <br>• crossed R65/R10: 0.58 / 1.14 N, and it hits the dome lugs. | **Stops R 90** (posts R 10, z 85.5 both), **2.0 N/cable**. This is the same layout in PAD, DRIVE BOX (nothing changes in the box) and firmware `config.json` (`stop_radius 90, post_radius 10`, PAD pose). <br>**A3 audit must add in-plane gravity** of the 57 g block (≤ 0.56 N at α 90°, 0.32 N at β 35°) by running the ink/pad rig tilted 90°. <br>If the slack window trips: **first** 7.5 N total (over-window 4.0 N; block stall still ≤ 5.0 N); **then** R 100. | PAD, ELECTRONICS, S0 (rig), TESTS |
| **I-2** | **Sign of the rim reaction.** The lift springs press the domes **up** into ceilings that rise away from home, so the dish pushes the block **outward and down**. The springs' centring pull (≤ 0.47 N) pushes it inward. Spec §4.2 and `forcemodel.py` model the reaction as inward. | statics of a ball under a rising ceiling; PAD P10/P14 | `ForceModel` becomes a **signed table R(d, pins on/off)** filled by `cal rim` (a no-contact sweep, done upright and with the rig tilted 90°). <br>Default before calibration [EST]: <br>• band 6.5–14.29: 1.1 N outward; <br>• outer rim 14.29–16.89: 1.3 N outward; <br>• minus the 0–0.47 N centring pull; <br>• plateau 0.5 N. <br>reflexd and the feed-forward use only the calibrated table. | ELECTRONICS |
| **I-3** | **The firmware pose model is wrong for v3b.** `DishModel` puts the posts at block z 0 and tilts the leading side **up**, so the z axis tilts toward −d. v3b tilts the z axis toward **+d**, with the posts 85.5 mm up. That puts the posts **≈ 9 mm** off at the plateau. | ik.py `block_pose`; PAD P15 | `ik.py` takes PAD's pose: origin, h(d), outward half-roll, `posts_local` z 85.5, stops z 85.5. Unit tests are rebuilt on it (§7). | ELECTRONICS |
| **I-4** | **The amplitude window collapses.** The geometric no-reversal radius is 16.9, the working amplitude 17.2 and the cage 18.0. A 0.3 mm window is smaller than the copy residual on the rim: dead band ≤ 0.3 mm plus IK ≤ 0.1 mm. | spec §4.6; PAD P15 | Commanded **no-reversal ≥ 17.2**, A **17.2–17.6** (default 17.4), **D_MAX 17.6**, cage 18.0. **Stroke-length variation now comes only from the chord offset e** (U(0, 7) on 40 % of strokes), not from A. Heading changes only at \|d\| ≥ 17.2. v ≤ 200 mm/s still caps f; ≈ 1.8 Hz on a sinusoid at A 17.4. PAD confirms the plateau is flat to the cage. | ELECTRONICS, PAD |
| **I-5** | **The float bore must grow.** The heavier pad (1.33 N) needs a ≥ 2.0 N retract spring. With HALO's proposed Ø 16 Penrose float (≈ 0.165 N/kPa), the six-nail budget at 18 kPa collapses to ≈ 0.09 N/nail. | arithmetic | **Bore Ø 20, 3/4 in Penrose, ≈ 0.27 N/kPa** [VERIFY B2]: 0.37 N/nail all-six, as in the spec. Mass ≈ 17–19 g, inside the Director's ≤ 20 g. Retract ≈ 125 ms after rail-sense low [EST; B4 ≤ 150]. | HALO |
| **I-6** | **The drum index is ambiguous with Ø 12 drums.** A ±26 mm cable span is 1.38 turns, so the single Hall index triggers twice inside the travel (DB C14). | arithmetic | **Ø 20 drums**: 0.83 turn, one trigger. Homing winds in and searches ≤ 1.0 turn, reversing once. The VREF rule is measured at the block (row DB C5). | DRIVE BOX, ELECTRONICS |
| **I-7** | Fence reach is 41.3 mm, not 35 (PAD P20). | halo_design re-run | Stops are set by procedure (M2); the `reach` constant in `halo_design.py` becomes 41.3. | HALO, TESTS |
| **I-8** | Stage gates are written for 286 g. | §5 | **B1:** pad ≤ 140 g; moving group (carriage + float + pad) ≤ 200 g; helmet ≤ 480 g hard. **C2:** helmet ≤ 480 g. The design target follows M1. | TESTS |
| **I-9** | The stock series spring is 1.65 N/mm, and the housings are now 1.9 m. | DB C6 arithmetic | Block stiffness ≈ 1.46 N/mm [EST]. **V-T1 becomes ≥ 1.4 N/mm**; the copy pass lines (bow ≤ 0.5 mm, RSS ≤ 0.5) govern. | DRIVE BOX, TESTS |
| **I-10** | **Housing mass on the head.** Full-length Shimano SP41 (≈ 15–20 g/m) adds ≈ 29 g on the head, taking it to **≈ 501 g, over red line 10**. Cost-down's Lean scenario ("bike housing only") assumes it. | DB C3; HALO harness ledger | **The head segment needs ≤ 8 g/m per housing**: <br>• the thin sheath spring + PTFE liner (cost-down B6) [VERIFY]; or <br>• Motion Dynamics 304V when restocked. <br>SP41 is allowed box → clip only, with a butt-ferrule joint in a 30 mm brass sleeve at the clip. The S0b ink rig tests the hybrid. | DRIVE BOX, HALO, S0, cost-down |
| **I-11** | **In-plane gravity at tilted stations** (≤ 0.56 N) is invisible to reflexd, because nothing senses the halo pose. It would eat most of the 0.8 N F-layer threshold. | P22 + spec §8.5 | **Station tare**: at every APPROACH, with the block parked at d = 0 and pins up, reflexd averages 0.5 s of tensions and subtracts the static in-plane vector until the next MOVED. The tare is logged (`E tare`). A tare > 0.8 N → FAULT ("pad not seated"). | ELECTRONICS |
| **I-12** | **R 90 stops make the cables sweep into PAD's deck posts.** The cables move ±10.4 mm at R 58, and the deck posts sit at ±12° (±12 mm) around each stop angle. | geometry | PAD moves the six deck posts so that each cable clears by ≥ 3 mm at full sweep, and re-runs check_assembly with the cable sweep. PAD also confirms the PP cover band closes the block–skirt annulus at every pose, so the 1.87 mm yoke–ceiling gap (z ≥ 83) is "booted" in C8's sense. | PAD |
| **I-13** | **Cost-down scenarios assume small hinges and bike housing.** "Light float + small hinges" (Balanced/Lean) and "bike housing only" (Lean) are not valid with a 135 g pad: the small-hinge worn margin is ≈ 1.0, and the bike housing breaks red line 10. | §5; halo_design | Cost-down re-prices Balanced/Lean with **medium hinges** and the I-10 hybrid housing. **Cost-down O8 (one hinge pair):** buy the **medium E6-10-301-20 pair at S0a** too (≈ +$5). | cost-down, S0 |

---

## 4. Every conflict raised by every package, with its resolution

Columns:
- **Src** is the package CONFLICTS.md item.
- **Owner** is the package whose files must change; "—" means record only.
- **M?** gives the Michael item from §1, or "No".

### 4.1 S0 (14-build/S0/CONFLICTS.md)

| # | Src | Raised | v3.1 resolution / new values | Owner | M? |
|---|---|---|---|---|---|
| 1 | S0 #1 | Concentric R 160 dish: 10.2–10.4 mm rake, 48–62° landing | **Adopt PAD v3b** (§2). The frozen dish is not used for the pad. | PAD (done), FIRMWARE (I-3), S0 (wording) | No (M6 if S0a ties) |
| 2 | S0 #1a | Director: build V1 frozen + V2 corrected (full roll, Ø 168, 13.1°) | **S0a keeps V1 + V2 as the blind sensation comparison.** V2's scalp-side rake (18.5–18.9 mm) and landing (29–33°) fall inside v3b's (17.9–24.7, ≤ 34°), so a V2 rating stands in for v3b's feel. V2 is a test article, not the pad. <br>**Add PAD PD19** (single v3b pocket) to S0a: ball-path finish, stick-slip (V-D3) and lift ≥ 5.3 mm with feelers. <br>S0-guide §11 "GO: frozen dish" row changes to: "the concept passes; the pad is still v3b (C5)". | S0 | M6 (conditional) |
| 3 | S0 #2 | Lift line at 13.7 inconsistent | v3b: lift ≥ 5.34 mm at reversal on every nail. Worst reserve is held by the skid adjuster (PAD P5). No-reversal is geometric 16.9 / commanded 17.2 (I-4). | PAD, FIRMWARE, TESTS | No |
| 4 | S0 #3 | Balls R 26 vs R 22; deck Ø 116 | Superseded: PTFE balls at R 38, deck Ø 132. Spec M11 is rewritten to match. | PAD (done) | No |
| 5 | S0 #4 | Rise along the pad axis per ball | Adopted (h along z_P; ceilings are the exact envelope, `pad_geom2.py`). | PAD (done) | No |
| 6 | S0 #5 | Spring nails, not syringes | **Director ruled: accepted for S0.** Constant air force is first tested at A2. | TESTS (note) | No |
| 7 | S0 #6 | Bench nail Ø 4.5 resin stem | Accepted for S0. The production nail is PAD P6. | — | No |
| 8 | S0 #7 | Bench lift elastic 1.5 N | Bench only. The pad uses 3 inclined springs, 0.63–0.81 N (P10). | — | No |
| 9 | S0 #8 | Spec tendon layout does not fit | v3.1: posts R 10 / stops R 90 (I-1). **The S0b ink-rig deck changes:** stops R 90, posts R 10, pen travel ±26 mm, Ø 20 drums, springs may stay at the box. | S0 | No |
| 10 | S0 #9 | Stock substitutions | Accept: <br>• 9654K959 springs at 1.65 N/mm (I-9); <br>• 16 N·cm motor; <br>• 2 × 5 m Surflon; <br>• housing per I-10; <br>• add 4 × TMC2209, heatsinks and microSD (cost-down A2/A3/A7). | S0, DRIVE BOX | No |
| 11 | S0 #10 | S0b on M8P + CB1 | Accept (Pico variant = cost-down Lean). | — | No |
| 12 | S0 #11 | Landing spread on a ball | Accept mixed nail lengths; spread in mm at S0, in ms at A3 (30–40 ms target; v3b adds +0.7 mm spread). | — | No |
| 13 | S0 #12 | PTFE film won't lie in the pockets | No tape. SLA pockets 1500-grit + PTFE dry film; wax on the bench. V-D3 is tested on PD19. | PAD (done) | No |

### 4.2 PAD (14-build/pad/CONFLICTS.md)

| # | Src | Raised | v3.1 resolution / new values | Owner | M? |
|---|---|---|---|---|---|
| 14 | P1 | Dish redefined (v3b) | **Adopted as the v3.1 dish** (§2). | FIRMWARE (I-3), HALO, S0 | No |
| 15 | P2 | Tendons: stops R 65 / posts R 10 | **Posts kept; stops moved to R 90** (I-1), at 90/210/330°, z 85.5; series springs in the stop blocks; 2.0 N/cable. <br>PAD lengthens the skirt-frame arms (+≈ 3 g) and moves the deck posts (I-12). | PAD | No |
| 16 | P3 | Ball seats at 109.5, not 80 | Adopted. HALO: `PAD_STACK` 86 → **115.5**, **R_BAIL 249** (with CH_DEG 16.7), retract 25 mm kept. The halo_design sweep passes: spider 3.0 mm under the tube, carriage/node 0 mm³ at 16.7°. Height-recovery options are not taken. | HALO | No (bulk in M1) |
| 17 | P4 | Pad ≈ 130 g; B1 ≤ 90 fails | **Pad 135 g as designed** (+3 g R 90 arms); diet to **≈ 110 g** (pad.md §10 list, −26 g); B1 pad ≤ 140 g hard (I-8). | PAD, TESTS | **M1** |
| 18 | P5 | Fixed skids gate only on R 85–90 | **Skid-height adjuster accepted** (±9 mm, 0.5 mm/turn, gauge PD18). One setting per station group goes in HALO's station table; TESTS adds "set skid height" to every station move and a PHC-B check. Parietal partial → M7. | PAD (done), HALO, TESTS | M7 |
| 19 | P6 | No Ø 1 shaft: POM land Ø 3.92 | Accepted. Spec §0, §1 C4, §4.1, M10 are superseded by the §2 nail. The C1 magnet is whichever of D21B-N52 / Ø 3 × 2 passes A2 (cost-down O7). | PAD | No |
| 20 | P7 | Guide friction vs C1(ii) | Accepted: 2 PTFE bushes, 16 mm span; **B = 0.15 ± 0.03 N**. A2(a) (≤ 0.35 N with 0.5 N side load) decides. Fallback is LM4UU + hardened Ø 4 land (+15 g, −4 mm). **The limit is not relaxed.** | PAD, TESTS | No |
| 21 | P8 | 0.0322 N/kPa | Adopted; firmware limits in §2. A2 force gate: **10 kPa → 0.24 ± 0.04 N net**. Relief check with B at 100 %: **≤ 0.82 N**. C6 bottoming: **≤ 0.82 N**. | ELECTRONICS, TESTS | No |
| 22 | P9 | Return spring 0.08 N | Adopted; `PIN_SPRING_N = 0.08`. | ELECTRONICS | No |
| 23 | P10 | Three inclined lift springs | Accepted. A3 checks the block seats on the plateau at α 0 with pins vented. The centring pull enters R(d) (I-2). | TESTS | No |
| 24 | P11 | No PP parallelogram; yaw by tendons | Accepted (≈ 68 N·mm/rad at R 90, 2.0 N). IK assumes yaw 0. A3 yaw mark ≤ 3°. Fallback is the 4th passive-cable boss. | PAD, TESTS | No |
| 25 | P12 | M8 = spherical seat; breakaway ≈ 3 N; float ≥ 1.6 N | Accepted seat. **Restore 6 ± 2 N with Ø 8 × 3 N52 spider magnets** at the 2.5 mm gap [VERIFY B3]. Retract spring **2.2 N class** (I-5). | HALO | No |
| 26 | P13 | Angles | Accepted. HALO confirms the spider arms clear the pocket shells by ≥ 1 mm at ±3° pad tilt. | HALO | No |
| 27 | P14 | Coupling 2.0 N may be exceeded | Keep 2.0 N; the A3 20-min test decides 2.0 vs 2.5 (spec cap unchanged). The comparator acts ≤ 0.2 ms, well inside 30 ms. | TESTS | No |
| 28 | P15 | Numbers for firmware | Adopted with I-3/I-4 (§2). | ELECTRONICS | No |
| 29 | P16 | Cartridge Ø 9.4 × 42 | Accepted; spec M9 rewritten. | — | No |
| 30 | P17 | 30G gallery bleeds, drilled | Accepted; PAD buys the 30G (DB C18). | PAD | No |
| 31 | P18 | Wipers in a snap-off skirt plate | Accepted. | — | No |
| 32 | P19 | Block underside 27.8 on R 65 unless the skid is set | Accepted. C8 (≥ 30) holds only with the station-group skid setting, so PHC-B checks it. | TESTS | No |
| 33 | P20 | Fence reach 41.3 mm | Adopted: fence = 41.3 + 15 (I-7). | HALO, TESTS | **M2** |
| 34 | P21 | Rod-side vent path | Accepted. | — | No |
| 35 | P22 | Moving block 57 g, 31 Hz | Accepted (spec §4.4/§7.2: 1.1 mJ ≪ 50 mJ). Its gravity enters I-1 and I-11. | — | No |
| 36 | P23 | Cage = lugs on the skirt ring at 18.0 | Accepted; D_MAX 17.6. | — | No |
| 37 | P24 | Prices unchecked | BOM / cost-down. | cost-down | No |

### 4.3 HALO (14-build/halo/CONFLICTS.md)

| # | Src | Raised | v3.1 resolution / new values | Owner | M? |
|---|---|---|---|---|---|
| 38 | H1 | Airpel is 96 g | **Resolved (Director): Penrose float ≤ 20 g.** v3.1 adds: bore Ø 20, 3/4 in sleeve, ≈ 0.27 N/kPa, Ø 0.2 bleed, QEV + float relief on its port (I-5). Bench at A2/A3: friction < 0.1 N, 50 mm stroke, 10⁴ cycles. | HALO | No |
| 39 | H2 | Small hinges can't hold | **Resolved (Director): E6-10-301-20 + brakes.** v3.1 re-check: needs 0.66 N·m; worn + brakes 1.18 N·m, **margin 1.80**. | HALO | No |
| 40 | H3 | Hubs \|Y\| 141.5; M1 gone | **Resolved (Director).** Spec M1/F1 deleted; hub plate merged. | — | No |
| 41 | H4 | Pad axis δ ahead of the bail | Accepted. With R_SI 262, **δ = 5.2°**. Every α is the pad α. | HALO | No |
| 42 | H5 | R_BAIL 220 | **Superseded by the pad stack: R_BAIL 249** (#16). | HALO | No (M1) |
| 43 | H6 | 10 × 1 strip on posts | Accepted; spec C24/M5 rewritten. | — | No |
| 44 | H7 | Front stop rule puts nails past the hairline | **Resolved (Director): set from the hairline.** With the 41.3 reach: **α_pad ≥ −25°** on the design head; measured on Michael. | HALO, TESTS | No |
| 45 | H8 | β ±40 too near the ear | Director ruled ±35°. With the 41.3 reach the same ≥ 40 mm rule gives **≈ ±28°** on the design head. | HALO | **M2** |
| 46 | H9 | Harness 0.72 m | **Resolved (Director).** At R 249 it is ≈ 0.78 m, 33.5 g [EST]; housings ≤ 8 g/m on the head (I-10). | HALO | No |
| 47 | H10 | Umbilical exits from the foot stub | Accepted; spec M15 rewritten. | — | No |
| 48 | H11 | Mass ledger 488 / 373 g | **v3.1 ledger, §5: ≈ 472 g as designed, ≈ 425 g after the diet.** | HALO, PAD | **M1** |
| 49 | H12 | Bail 400 mm wide | **Adopt CH_DEG 16.7** (C24 released): 393 mm at R 249 (453 mm at 20.7°). | HALO | No |
| 50 | H13 | Pad-2 second-hinge seat impossible; twin mass | Twin cannot fit under 500 g (472 + ≈ 190). Keep the zero-mass provisions only: split vertex node, exit-stub second clamp, drum/plate seats, box tees. **Drop the second-hinge seat.** | HALO, DRIVE BOX | **M1** |
| 51 | H14 | M8 ball-side choices | Consistent with P12; magnets Ø 8 × 3 (#25). | HALO | No |
| 52 | H15 | Front band = 2 × 10 × 1 strips | Accepted [VERIFY 24 h bend soak]; spec C25 rewritten. | — | No |
| 53 | H16 | D2F-01FL head switch | Accepted. It now sits in the 24 V coil chain (E-C7), so it must be rated ≥ 50 mA at 24 V DC [VERIFY]. | HALO | No |
| 54 | H17 | O vs tragion contradiction | **§3.2 table governs:** tragion at (−10, ±72, −45) in H. §3.1 text is corrected to "10 mm in front of". | — (spec text) | No |
| 55 | H18 | Retract spring | **Constant-force spring ≥ 2.0 N (2.2 N class)** [VERIFY McMaster PN]. | HALO | No |
| 56 | H19 | JLC 40 % tariff | Cost-down (already counted). | cost-down | No |
| 57 | H20 | Notches, fold range, hair zone | Accepted. Notch tables are recomputed for R_SI 262 / δ 5.2°. | HALO | No |

### 4.4 DRIVE BOX (14-build/drivebox/CONFLICTS.md)

| # | Src | Raised | v3.1 resolution / new values | Owner | M? |
|---|---|---|---|---|---|
| 58 | C1 | Box ≈ 3.8 kg vs ≤ 2.8 | **Recommend ≤ 4.0 kg** with the trims (≈ 3.5 kg). R9 ply box stays the fallback. | DRIVE BOX | **M3** |
| 59 | C2 | 6 N plate vs 1.5 N/cable | **6.0 N at the W tick = 2.0 N/cable** (shim the springs +6.7 mm); range 4.5–7.5 N (I-1 fallback). `pretension_n = 2.0`. | DRIVE BOX, ELECTRONICS | No |
| 60 | C3 | 1.2/0.6 coil not stocked | **I-10:** no SP41 on the head segment. Use a hybrid (SP41 box → clip, ≤ 8 g/m clip → pad); the S0b ink rig tests it. Ask Chamfr for a restock date. | DRIVE BOX, HALO, S0 | No |
| 61 | C4 | 1.6 m limits the riser to 0.47 m | **1.9 m** tubes, housings and wire (+≈ $5). Chair-back is the default; desk use only with the box ≤ 0.5 m from the clip. Stiffness per I-9. | DRIVE BOX, HALO | No |
| 62 | C5 | VREF 0.35 A ≈ 9 N | **The cap is defined where spec §7.2 puts it, at the pad:** block-side stall pull **≤ 5.0 N** per cable, measured with a luggage scale at the yoke end. VREF is set at A3 in **0.25–0.45 A** (start 0.35 V) and must also run 20 min per mode without skipped steps at 2.0 N. Measured at the block, this leaves an inherent 1.5× margin (5.0 / 3.3 N maximum working tension) whatever the housing friction. **No limit is relaxed.** | DRIVE BOX, ELECTRONICS, TESTS | No |
| 63 | C6 | 1.9 → 1.8 N/mm with the flexure | ≈ 1.46 N/mm with stock springs at 1.9 m; **V-T1 ≥ 1.4** (I-9). | TESTS | No |
| 64 | C7 | Hall resolution marginal | V-T5 on day 1 of A3 on the Pico ADC. If > 0.2 N: **ADS1115 on the Pico I²C** (GP4/5, ≈ $3) and/or a 2.0 mm tongue. The comparators are unaffected. | DRIVE BOX, ELECTRONICS | No |
| 65 | C8 | No diverse 3.5 psi relief | Get the Generant VRV ×2 quote now. Same-make 4277T51 is allowed **for the A1/A2 bench only**. **Diverse parts must be fitted before any head session (A-S onward).** | DRIVE BOX | M5 (cond.) |
| 66 | C9 | No ≤ 30 kPa palm pump; fixed bleed | **Folded into S-1:** a fixed-orifice limiter is accepted as the mechanical deadhead constant for **both** P1 (≤ 45 kPa) and P3 (≤ 27 kPa), unless a pump with a published in-range maximum is named. | DRIVE BOX | No |
| 67 | C10 | Leads on the left end wall | Accepted. Lid foam above the M8P removed. | — | No |
| 68 | C11 | Housings can't sit in the latched block | Accepted (thumb screws, separate GX12-4). Spec §6 sentence rewritten. | — | No |
| 69 | C12 | Two "clips" | DRIVE BOX DB15/16 is **the 3 N clip**. HALO's is the strain relief. This also closes cost-down O5. | HALO | No |
| 70 | C13 | QEV + float relief location | **HALO buys and owns them** (on the float port); closes cost-down O2. | HALO | No |
| 71 | C14 | Index triggers twice past a turn | **Ø 20 drums** (I-6); wind-in search ≤ 1.0 turn. | DRIVE BOX, ELECTRONICS | No |
| 72 | C15 | Pad-2 seats above pad 1 | Record only. | — | No |
| 73 | C16 | M5 hook-plate pattern | Accepted. | — | No |
| 74 | C17 | TIUB01 tubing | Accepted; spec §5.2. | — | No |
| 75 | C18 | No 30G in the kit | PAD buys 30G. | PAD | No |
| 76 | C19 | Case wall unknown | Measure; regenerate DB08. | DRIVE BOX | No |
| 77 | C20 | 30 dBA unmeasurable | Per T-A5 (#100). | TESTS | No |
| 78 | C21 | 3.18 × 1.59 magnets | Accepted. | — | No |

### 4.5 ELECTRONICS + FIRMWARE (14-build/electronics/CONFLICTS.md)

| # | Src | Raised | v3.1 resolution / new values | Owner | M? |
|---|---|---|---|---|---|
| 79 | E-C1 | Spec tendons can't hold the block | **Stops R 90 / posts R 10, 2.0 N (I-1)**, on the PAD pose (I-3). The boot audit now uses the PAD pose: unloaded 0.3–3.3 N over \|d\| ≤ 17.6, and it prints the any-direction capacity. | ELECTRONICS, PAD | No |
| 80 | E-C2 | CB1 I²C unusable → Pico | Accepted (BOM: −ADS1115, +Pico). | — | No |
| 81 | E-C3 | Relay drop-out 20 ms, not < 5 ms | Spec §4.11 restated: **K1 contacts open ≤ 20 ms; ACT-24 < 4 V ≤ 35 ms** (4.7 Ω 5 W bleeder on K1 NC-a); pins vented ≤ 135 ms; pad retracted ≤ 185 ms from the trigger (≤ 150 ms from rail-sense low). Ruling C3 (≤ 100 ms from de-energise) and C4 (trip ≤ 50 ms to rail-sense low: E ≤ 35, F ≤ 44) are unchanged and met. A spec budget line is corrected; **no ruling or red-line limit is relaxed.** | TESTS (A0, B4) | No |
| 82 | E-C4 | Queue ≈ 1 s; extra-axis moves; ICV no effect | Accepted. Spec C18/C22/§8.1–8.2 wording: the queue is ≈ 1 s and the host owns the velocity profile. Full fail-to-free is unchanged. | — | No |
| 83 | E-C5 | Valves as `pwm_tool` | Accepted; electronics.md §4 replaces spec §5.5. | — | No |
| 84 | E-C6 | VREF wording | As #62. | — | No |
| 85 | E-C7 | Helmet loop in the 24 V coil chain | Accepted; E5 rewritten. Pogo pins and switch rated ≥ 50 mA at 24 V. | HALO | No |
| 86 | E-C8 | Heartbeat; host hang ≤ 1.3 s | Accepted; spec §7.8 bound ≤ 1.3 s. | — | No |
| 87 | E-C9 | No valid circle at R 13 | v3b CIRCLE limits (§2). | ELECTRONICS | No |
| 88 | E-C10 | GX12-8 rare → GX16-8 | Accepted. | — | No |
| 89 | E-C11 | Resource map revised | electronics.md §4 governs. The S-1 pump must be ≤ 0.8 A on FAN3. | DRIVE BOX | No |
| 90 | E-C12 | HE "+" = VBB; VFAN diode back-feed | **A0-7 dead-rail output test is a hard gate** on the A0 sheet. | TESTS | No |
| 91 | E-C13 | 50 ms weld check meaningless in software | Accepted: force-guided NC state check in firmware; the timing is measured once at A0 with the logic analyser. | TESTS | No |
| 92 | E-C14 | Latch inputs | Accepted. | — | No |
| 93 | E-C15 | Relative comparator window trips on the rim | **Absolute 0.2 / 3.6 N** (4.0 N at the 7.5 N fallback); re-derived after `cal rim`. | ELECTRONICS | No |
| 94 | E-C16 | Mode change ≤ 2.5 s in CIRCLE | Accepted: ≤ 0.5 s in the other modes, ≤ 2.5 s in CIRCLE (at the next token). | — | No |
| 95 | E-C17 | BOM line | Cost-down. | cost-down | No |

### 4.6 TEST PROTOCOLS (14-build/tests/CONFLICTS.md)

**A. Pass lines not testable as written**

| # | Src | Raised | v3.1 resolution / new values | Owner | M? |
|---|---|---|---|---|---|
| 96 | T-A1 | HX711 can't do 1 kHz | Ruling C1(c) is read as "**a load cell read at ≥ 800 samples/s**": Pico + ADS1115 at 860 SPS + TAL221 100 g. | TESTS | No (cost in M4) |
| 97 | T-A2 | 0–40 kPa sensors vs 50 kPa deadhead | A1 deadheads are measured with an **external 0–15 psi gauge on a tee**; the in-box sensors stay. | TESTS, DRIVE BOX | No |
| 98 | T-A3 | 5 ms rail-off untestable | A0 line: "each element: **K1 NC-aux closed ≤ 20 ms and ACT-24 < 4 V ≤ 35 ms**, 10 × each, logic stays up". Use the 4.7 Ω switched bleeder, not 2.2 kΩ. | TESTS | No |
| 99 | T-A4 | "PLINE never retraces" fails by design | A3: "**over 60 s, no heading gap > 15° and no trace visibly darker than its neighbours; the `B` log passes the §8.4 no-repeat rule (±1 mm, ±5 %, ±2°)**". | TESTS | No |
| 100 | T-A5 | 30 dBA below the app floor | **A5 (box):** ≤ 30 dBA at 1 m, background-corrected; if the room is > 30 dBA, measure at 0.25 m and subtract 12 dB. **C5 (ear):** within 3 dB of the room with pins up (DB C20) + earplug A/B (#111). | TESTS | No |
| 101 | T-A6 | Head session before the wig gate; helper force uncapped | **A-S needs HB-mini + PHC-A (bench).** The bench pad rests under its own weight + a slug, **total ≤ 4 N measured**; the helper only steadies it. Diverse reliefs are fitted (#65). PAD adds the slug seat. | TESTS, PAD | No |
| 102 | T-A7 | No 10 mm partial retract | RC1(d) reads: "with an e-stop, a latch trip (`inject snag`) and a lanyard pull". | TESTS | No |
| 103 | T-A8 | Trip start point undefined | "0.25 mm monofilament tether to the load cell; **tether > 0.8 N → rail-sense low ≤ 50 ms** (E or F)". Real hair stays in C1(c)(d). | TESTS | No |
| 104 | T-A9 | Moving group undefined | Carriage + float + pad: **≈ 193 g; gate ≤ 200 g** (I-8). | TESTS | M1 |
| 105 | T-A10 | GO B aggregation | Adopt: ratings at the 20-min B-S4, confirmed by ≥ 7 at one other B session or at B-S4's 10-min form; zero felt pulls in every B session. | TESTS | No |
| 106 | T-A11 | Matting criterion | Adopt: comb-through > 1.5×, a visible clump, or shed > 2× in a step. T_dwell = last clean step of 30/60/90/120/180 s (cap 180 s). | TESTS | No |
| 107 | T-A12 | "With pins up" has no command | FIRMWARE `dryrun on/off`: allowed only with rail sense and the lever held; logs `E dryrun`. | ELECTRONICS | No |
| 108 | T-A13 | GO D aggregation | Adopt: 5 consecutive D sessions; median Q1 ≥ 7; median "machine on my head" ≤ 3; "again tomorrow" ≥ 4/5; zero tuft pulls. | TESTS | No |
| 109 | T-A14 | 0.45 N exceeds the all-six budget | The D5 force block runs **single groups alternating A/B, bratio 1, at F 0.20 / 0.30 / 0.45 N**. All-six is limited to ≈ 0.37 N/nail (I-5). | TESTS, ELECTRONICS | No |
| 110 | T-A15 | Helper-moved stations can't be blind | Marked open-label. | TESTS | No |
| 111 | T-A16 | Earplug A/B undefined | **10 random on/off trials; pass ≤ 7 correct.** | TESTS, S0 | No |
| 112 | T-A17 | C7 reading | **Every one of 10 trials ≤ 2.5 s.** | TESTS | No |
| 113 | T-A18 | Shed normalisation | Adopt: per 100 strokes ≤ 2× per 100 comb strokes; > 5 bulb hairs in any 5-min block = stop and look. | TESTS | No |

**B. Testability requests to other packages (all accepted)**

| # | Src | Request | v3.1 resolution | Owner | M? |
|---|---|---|---|---|---|
| 114 | T-B FW-1 | `dryrun` | as #107 | ELECTRONICS | No |
| 115 | T-B FW-2 | `hold centre` | block at d = 0, pins pressurised; retract only by command; only with rail sense + lever | ELECTRONICS | No |
| 116 | T-B FW-3 | 1,000-cycle vent loop | `cal lines cycles=1000` | ELECTRONICS | No |
| 117 | T-B FW-4 | blind / bset / next / reveal from one key | documented; in BLIND mode a **MOVED double-press = `next`** | ELECTRONICS | No |
| 118 | T-B FW-5 | contact-seconds per station in `status` | yes, plus the station tare (I-11) | ELECTRONICS | No |
| 119 | T-B EL-1 | ACT-12 LED + test header | yes | ELECTRONICS | No |
| 120 | T-B EL-2 | K1 NC-aux test header | yes (PF0 header) | ELECTRONICS | No |
| 121 | T-B EL-3 | ACT-24 bleeder if > 50 ms | already fitted (4.7 Ω on K1 NC-a): closed | — | No |
| 122 | T-B PAD-1 | nail-reach line on the skirt | painted reach radius from the C8 sweep (41.3 mm incl. yaw 5°) | PAD | No |
| 123 | T-B PAD-2 | shadowgraph + rim template | PD17 card; **rim templates 30° (band) and 60° (outer)**, not 34° | PAD | No |
| 124 | T-B PAD-3 | slug seat on the bench deck | yes (#101) | PAD | No |
| 125 | T-B PAD-4 | nail IDs N1–N6, S1… | yes, paint mark on each nail top | PAD | No |
| 126 | T-B PAD/HALO | eyelets on yoke and block | yes, 1 mm eyelet on each | PAD, HALO | No |
| 127 | T-B HALO | α/β zero gauge ±2° | H19 confirmed at δ 5.2° | HALO | No |
| 128 | T-B BOM | test kit ≈ $230 | into the cost-down carts | cost-down | **M4** |

**Tally:**
- **128 package items. 117 are resolved outright, including the Director rulings folded in.**
- **11 point to a Michael item:**
  - M1: #17, #48, #50, #104;
  - M2: #33, #45;
  - M3: #58;
  - M4: #128;
  - M5: #65 (conditional);
  - M6: #2 (conditional);
  - M7: #18.
- **Each of those 11 still has a recommended default.**
- **Plus 14 integration findings** (S-1, I-1…I-13), all resolved, including the Director's safety item S-1.

---

## 5. Updated mass budget (single pad, head-borne)

These are halo_design.py ledger rows. Inputs: R_BAIL 249, CH_DEG 16.7, medium hinges, Penrose float 20 g, pad from PAD CAD plus the R 90 arms, harness 0.78 m. [EST unless measured]

| Group | Spec v3 g | HALO as delivered (Airpel) g | **v3.1 as designed g** | Diet step | **v3.1 diet target g** |
|---|---|---|---|---|---|
| Retention (band, forehead node, switch, dial cradle, arms, temple pads) | 53 | 57 | **57.1** | lighter cradle −8 [VERIFY scale] | 49 |
| Hubs (plates, 2 × E6-10-301-20, feet, α stops, plunger, brakes) | 30 | 105 | **104.4** | pocket the plates and feet −8; Al M3 −2 | 94 |
| Bail (R 249 tubes 720 mm, nodes, strip, β stops, clips, epoxy, hardware) | 36 | 69 | **71.8** | Al M3 −3 | 69 |
| Carriage | 10 | 16 | **16.4** | — | 16.4 |
| Float group (Penrose Ø 20 ≤ 20; QEV + relief 8; spider + 3 balls + Ø 8 × 3 magnets 10.6; CF spring + rod 3.4) | 24 | 117 | **42** | — | 42 |
| Pad (v3b, R 90 stop arms) | 81.5 | 81.5 (spec) | **135** | PAD §10 diet −26 | 109 |
| Harness 0.78 m (≤ 8 g/m housings) + umbilical share + lanyard | 37 | 43 | **45.5** | — | 45.5 |
| Fasteners / provisions | 12 | in rows | in rows | — | — |
| **Total** | **286** | **488** | **≈ 472** | −47 | **≈ 425** |
| Worst lean (bun) | 0.27 N·m | 0.63 N·m | **0.56 N·m** (form-lock margin 1.8–2.7) | | 0.52 N·m |
| Hinge margin, worn, with brakes | 1.7 | 1.6 | **1.80** | | 1.93 |
| Moving group (carriage + float + pad) | ≈ 115 | — | **≈ 193** | | ≈ 167 |
| If SP41 is used on the head | — | — | **≈ 501: breaks red line 10** | not allowed | — |
| Twin (pad 2) | ≈ 440 | impossible | **≈ 660: impossible** | | — |

**≤ 400 g** would need the small hinges as well (−35 g → ≈ 390 g). That is M1 option (b), and it needs the Director to reopen the hinge ruling.

---

## 6. What changed for the builder (short list)

1. **The pad is bigger and heavier.**
   - Deck Ø 132; tendon stops on arms at R 90, so the top of the pad is ≈ Ø 196.
   - Ball seats 109.5 mm above the skin.
   - ≈ 135 g; nails are one-piece turned POM.
2. **The bail is R 249 with 16.7° chords** (6 × 64.3 mm tube cuts). Hubs sit at |Y| 141.5 on the medium E6-10-301-20 hinges with brakes.
3. **Float:** print a Ø 20 Penrose float (3/4 in sleeve), with a 2.2 N constant-force retract spring and Ø 8 × 3 spider magnets. **No Airpel.**
4. **Stops:**
   - Set the α front stop and β stops on your head with the procedure, using a 41.3 mm reach.
   - Expect ≈ −25° and ≈ ±28° (pending M2).
5. **Skid height:** set it per station group with gauge PD18 every time you move between groups.
6. **Drums are Ø 20, not Ø 12.**
   - Pretension 2.0 N per cable (6.0 N at the W tick).
   - Set VREF at A3 by pulling a luggage scale at the yoke until the drum stalls: **≤ 5.0 N**.
7. **Umbilical is 1.9 m.**
   - Housings on the head must be the light kind (≤ 8 g/m).
   - Bike housing only from the box to the clip.
8. **Pumps: buy none until DRIVE BOX names one with a published deadhead in range or fits the needle limiters (S-1).**
   - Measure every deadhead with the external gauge.
9. **Diverse reliefs must be in before your head is under any powered pad**, including the Stage A bench session.
10. **Firmware numbers change:**
    - 0.0322 N/kPa; 0.50 N cap at 18 kPa; palm 10–18 kPa;
    - stroke amplitude 17.2–17.6 mm; new circle limits;
    - a station tare at each approach;
    - new commands: `dryrun`, `hold centre`, `cal lines cycles=`, MOVED double-press = `next`.
11. **Safety board timing to expect at A0:** rail below 4 V within 35 ms. The A0-7 dead-rail output test is a hard gate.
12. **S0a is unchanged** (V1 + V2 + hand rake), with two changes:
    - add the PD19 single-pocket check;
    - buy the medium hinge pair now.
    - A frozen-dish tie does **not** change the pad.

---

## 7. Package files that must be edited

**S0**
- `S0-guide.md`: the §11 decision table "GO: frozen dish" row (M6 wording); add a PD19 v3b pocket step; the §10 ink rig moves to stops R 90 / posts R 10, ±26 mm, Ø 20 drums; earplug pass line (10 trials, ≤ 7 correct).
- `cart-S0a.md`: medium E6-10-301-20 pair; PD19 print line.
- `cart-S0b.md`: hybrid housing (SP41 + ≤ 8 g/m head segment); TMC2209 × 4, heatsinks, microSD.
- `cad/tendon_rig.scad`, `cad/gen_s0_stl.py`: T01 drum Ø 20, T05 deck stops R 90 / posts R 10.
- `klipper/printer.cfg`: rotation_distance 62.83.
- `klipper/s0_stream.py`: rig geometry.
- `build-doc-part1.html`: PD19 step, hinge size, frozen-dish wording; republish.
- `CONFLICTS.md`: mark the items resolved by this addendum.

**PAD**
- `pad.md`: §0 table; §2 plan (stops R 90, deck posts moved); §7.4; §8.4 (Ø 8 × 3 magnets on the HALO side, 2.2 N retract); §10 mass (+3 g arms, 135 g); §13 (A2 0.24 N at 10 kPa, ≤ 0.82 N checks); C8 cover-band boot confirmation.
- `parts.md`: 30G needles; 9654K959 springs; slug-seat hardware.
- `cad/lib_pad.scad`, `cad/pd02_skirt_frame.scad` (arms to R 90, deck-post relocation), `cad/pd11_stop_block.scad`, `cad/pd01_deck.scad` (posts).
- `cad/pad_geom2.py` (cable sweep ±26 mm vs posts, lugs and skirt), `cad/check_assembly.py`, `cad/gen_pad_stl.py`, `stl/` regenerate.
- `cad/README.md`, `CONFLICTS.md`.

**HALO**
- `cad/halo_params.scad`: PAD_STACK 115.5, CH_DEG 16.7, float bore Ø 20, CF spring 2.2 N, spider magnet pockets Ø 8.2 × 3.2.
- `cad/halo_design.py`: pad mass from PAD (135), float 20 g, reach 41.3, ear check at β 26–40, harness 0.78 m.
- `cad/halo_parts.py`: Penrose float body, spider, CF spool.
- `cad/gen_halo_stl.py` re-run; `cad/stl/*` and `_part_table.csv`; `cad/bail_template.svg` regenerate.
- `halo.md`: mass ledger; stop-setting procedure numbers; coverage ≈ 78 %; float build; notch tables for δ 5.2°; station table with a skid setting per group; drop the second-hinge seat.
- `parts.md`: remove Airpel; add the 3/4 in Penrose, CF spring 2.2 N class, Ø 8 × 3 N52, QEV + float relief (owned here), medium hinges.
- `CONFLICTS.md`.

**DRIVE BOX**
- `drivebox.md`:
  - §9 mass (≤ 4.0 kg + trims);
  - tendon routing text (stops R 90, posts R 10);
  - W tick at 6.0 N (shims);
  - Ø 20 drums;
  - 1.9 m umbilical and the hybrid housing;
  - VREF measurement rule;
  - pump selection or orifice limiter per S-1;
  - relief diversity plan;
  - homing search ≤ 1.0 turn.
- `parts.md`: pumps per S-1; SP41 box segment + head-segment housing; 1.9 m lengths; Generant quote; optional ADS1115 (on the Pico).
- `cad/db01_drum.scad`, `cad/db02_db05_drum_module.scad` (Ø 20 drum flange clearance; W tick at 6.0 N), `cad/lib_drivebox.scad`, `cad/gen_drivebox_stl.py`, `cad/stl/*`.
- `CONFLICTS.md`.

**ELECTRONICS + FIRMWARE**
- `electronics.md`: §6 timing statement as §2 here; §7 limits table; §8 IK pose model; VREF rule; station tare.
- `parts.md`: pumps ≤ 0.8 A; optional ADS1115.
- `firmware/sp1v3/limits.py`:
  - `N_PER_KPA_PIN 0.0322`, `PIN_SPRING_N 0.08`, `RAIL_MAX_KPA 18.0`, `F_NAIL_MAX 0.50`;
  - `FLOAT_N_PER_KPA 0.27`, `FLOAT_SPRING_N 2.2`, `PALM_MAX_KPA 18.0` (palm lo 10);
  - `D_MAX 17.6`, `R_NO_REVERSAL 17.2`, `R_LAND_INNER 7.8`, `R_LAND_OUTER 12.6`, `R_PARK 17.4`;
  - `CIRCLE_RPE_MIN 17.0` (+ max 17.6), `CIRCLE_RME_MAX 7.8`, R 9–12.7;
  - `amp` 17.2–17.6 (default 17.4);
  - `force` hi 0.50 and `force_lo_B` 0.20–0.40;
  - `rail` 5.6–18.0.
- `ik.py`: PAD v3b pose (outward half-roll, posts z 85.5); `Geometry` 90/10.
- `forcemodel.py`: signed calibrated R(d) table (I-2); gravity tare input.
- `scorer.py`:
  - config geometry and `pretension_n 2.0`;
  - boot audit on the PAD pose;
  - station tare at APPROACH;
  - `dryrun`, `hold centre`, contact-seconds;
  - MOVED double-press = `next`.
- `reflexd.py`: subtract the tare.
- `checker.py`, `paths.py`, `planner.py`: new limits; heading turns only at \|d\| ≥ 17.2.
- `scratchctl.py`: `cal lines cycles=`, `dryrun`, `hold centre`.
- `printer.cfg`: rotation_distance 62.83; homing search ≤ 1.0 turn.
- `pico/main.py`: optional ADS1115 path.
- `tests/test_ik.py`: replace the "R70/R15, R65/R10 pass" case with "v3b pose: R65/R10 fails, R90/R10 passes unloaded ≥ 0.9 N at 6 N".
- `tests/test_checker.py`: new limits.
- `tests/test_reflex.py`: tare.

**TESTS**
- `test-protocols-v3.md`:
  - **A0:** 20/35 ms lines; A0-7 hard gate; weld check per E-C13.
  - **A1:** external gauge; deadhead/limiter per S-1.
  - **A2:** 0.24 ± 0.04 N at 10 kPa; ≤ 0.82 N relief and C6 checks; float bench.
  - **A3:** retrace wording; VREF stall pull ≤ 5.0 N; tilted-rig tension audit (I-1); `cal rim` signed; V-T1 ≥ 1.4; yaw ≤ 3°.
  - **A5:** noise wording.
  - **A-S:** prerequisites and ≤ 4 N.
  - **B1:** masses (I-8).
  - **B3:** M8 6 ± 2 N with Ø 8 × 3.
  - **B4:** ≤ 150 ms from rail-sense low / ≤ 185 ms from the trigger.
  - **C4:** reach 41.3 mm.
  - **C5/S0:** earplug count.
  - **C7, D5, GO B/D:** aggregation per #105–#113.
  - **Skid-height step** on every station move; PHC-B skid check.
- `CONFLICTS.md`.

**cost-down (14-build/cost-down.md)**
- Re-price Balanced/Lean with medium hinges and the hybrid housing (I-13).
- O1: moot (no Airpel). O2: HALO owns. O4: S-1. O5: DRIVE BOX clip. O8: medium pair.

**SYSTEM-SPEC-v3 lines superseded by this addendum:**
- §0 table rows: pins, nail, dish, puppet, head mass, box.
- §1: C4, C6, C7, C12, C15–C18, C22 wording, C23–C25.
- §2.4 tendon schematic.
- §3.1 O text.
- §4.1–4.5, §4.7, §4.8, §4.11.
- §5.1: M1, M2, M5, M8, M9, M11, M13, M14, M15.
- §5.4 E5, E7, E8; §5.5.
- §6: mass, front face, latched block.
- §7.2 caps; §7.3 C5/C8 values; §7.8 host hang.
- §8.2 pose model; §8.3 checker numbers.
- §10: S0 dish row; gates A0, A2, A3, A5, B1, B4, C2.
- §13: lines touched by I-5, I-6 and I-10.
- **The ruling (C1–C8) and the 13 red lines are unchanged.**
