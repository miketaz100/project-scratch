# HALO work package: conflicts with SYSTEM-SPEC-v3

**SP1 v3 · 14-build/halo · HALO engineer · 2026-10-02**

This file lists every place where the HALO design cannot follow SYSTEM-SPEC-v3.md exactly, or where the spec text contradicts itself. Per the build brief, I did not edit the spec. Each item gives:
- what the spec says;
- what is true or what I built;
- the evidence;
- who has to decide.

All numbers come from `cad/halo_design.py` and `cad/gen_halo_stl.py` unless a source is cited. Item 1 is the blocker. Items 2–8 change geometry. Items 9–20 are smaller.

**Default build in `cad/`:**
- R_BAIL 220.
- Medium E6 hinges.
- Airpel float, as the spec binds.

**Recommended build:** the light float (item 1), with small hinges once item 1 is settled.

---

## 1. BLOCKER: the Airpel E16D2.0N float weighs about 96 g, not 16–24 g

| | Spec (§1 C12, §4.8) | Found |
|---|---|---|
| Float mass | "Float: Airpel E16 + rods/spring + QEV + float relief 24 g [VERIFY Airpel mass ≤ 16 g]" | Airpot catalogue ACC-02M gives mass ≤ 64.6 g + 15.8 g per inch of stroke. For 2.0 in that is **≈ 96 g**, of which the piston and rod are ≈ 23 g. Body OD 20.6 mm, length 107.4 mm. [cited: airoil.com/uploads/assets/downloads/AirpelCat10-06.pdf pp. 4, 8, 9, checked 2026-10-02] |
| Helmet, single pad | ≈ 286 g; gate B1/C2 ≤ 320 g | **≈ 488 g** with the Airpel and the medium hinges it then needs (item 2). That is **12 g under red line 10 (500 g)**. |
| Worst lean | 0.27 N·m; cradle margin ≥ 3.7 | **0.63 N·m**; cradle margin 1.6–2.4 (form lock 1–1.5 N·m) |
| Twin (pad 2) | ≈ 440 g | **Impossible.** It adds ≈ 150 g and goes over 500 g. |
| Airpel height | not stated | The body sits on the carriage beside the bail and stands **235 mm above the vertex scalp**. At bun stations it points ≈ 225 mm behind the head, so bun stations cannot be used near any headrest (this tightens RT2 #12). |

**Proposal (needs a Director decision, with PAD):** a **light float**. Use a 5/8 in Penrose latex sleeve rolling inside a printed PA12 Ø16 bore, the same technology as the pins (C2).
- Mass about 15 g; it keeps the 7/16-20-sized nose so it fits the same carriage plate.
- It is sealed, so add a fixed Ø0.2 bleed in place of the Airpel's clearance leak, as for the palm bleed.
- Bench it in Stage A next to the pins: friction < 0.1 N, stroke 50 mm, 10⁴ cycles, retract ≤ 150 ms.

Result: **≈ 373 g with small hinges, ≈ 407 g with medium hinges; lean 0.42 N·m**. Run `halo_design.py --light-float` to reproduce.

**Even then, the 320 g gate is not reachable with real part masses** (see item 11). The Director should re-baseline the gates B1/C2 to ≈ 380 g.

## 2. Hinge torque: the two small Southco E6-10-101-20 hinges cannot hold the halo with the Airpel

The spec says "2 × 0.25 + detent 0.15 = 0.65 N·m vs 0.38 needed (margin 1.7)". What I found:
- The worst bail-borne gravity moment is **0.62 N·m** with the Airpel (0.40 with the light float). Add 0.11 for scrub.
- Southco's own test sheet TD-E6-3-J shows a 35 in-oz setting decaying to **≈ 19 in-oz (−47 %) by 5,000 cycles**. Retightening the adjustment screw restores it.
- An M4 ball plunger (4.0 N, McMaster 85015A46) on R 26–29 clicks at 0.10–0.12 N·m, not 0.15.

**What I built:**
- `HINGE_SIZE` in `halo_params.scad`.
- **Default 2 = Southco E6-10-301-20 (medium, 0.8 N·m, $12.48)**. Margin 2.3 when new, 1.6 when worn with the brakes set.
- Size 1 (small) is supplied as `stl/variant_small_hinge/` for the light float. Margin 1.56 when new with brakes; when worn it needs a retighten every ≈ 2,000 cycles.
- An **adjustable friction brake** (NBR cord + M3 set screw on each foot, ≈ 0.1 N·m each) added to both hubs.

The medium hinge is 42.9 mm long along the pin, so the hubs move out to |Y| = 141.5 (item 3). Medium dimensions marked [VERIFY] are HINGE_H 6.35, knuckle 12.7, leaf 3.2; check them with calipers before ordering prints.

## 3. Hub position |Y| = 141.5 (medium) or 124 (small), not 120; M1 changed

- **Spec §3.1, §5.1 M1/M2:** hubs at |Y| = 120; F1 at |Y| = 95; a boss bolted to the band and cradle arms by 3 × M3 on a 24 mm triangle + Ø3 dowel.
- **Why it can't stay:** an E6 leaf hinge has its pin on the ear axis and occupies 25.4 or 42.9 mm of that axis. The bail leg must land on the axis outboard of the hinge, or the leg socket hits the leaves. So Y_HUB = hub-plate face + hinge length + 4.6.
- **Built:**
  - Side plate and boss **merged into one hub plate per side** (H01L/H01R), which saves ≈ 9 g a side. The M1 bolt pattern no longer exists.
  - The hub-plate outboard face is at |Y| 94 (12 mm temple pad + 1 + 4 mm plate on a 77 mm half-breadth).
  - Hub-axis to ear canal is 46 mm (red line 6 ≥ 25 ✓).
- **Widths:** 313 mm across the feet (medium) or 278 mm (small); the spec implied about 270 mm.

## 4. The pad axis sits 5.9° in front of the bail plane (δ)

- **Spec:** "R_bail = 98 + 80 + 25 + 7" puts the float in series under the bail centreline.
- **Why it can't:** a 50 mm-stroke float is ≥ 107 mm long and cannot sit inside a 32 mm radial gap. It has to stand beside the bail.
- **Built:**
  - The float axis passes through O, 24 mm in front of the bail plane at the track, so **δ = atan(24/233) = 5.9°**.
  - Every α in HALO (detent clocking, stops, zero gauge) is the **pad** α of the spec's u(α, β), so α_bail = α_pad + 5.9°.
  - FIRMWARE and CAD: no change to u(α, β) if they read α as the pad angle, which HALO guarantees.

## 5. R_BAIL 220, not 210

- **Spec §4.7:** R_bail ≈ 210.
- **Problem:** at the bun (scalp radius 98) with the spec's 25 mm retract, the float spider (top ≈ 86 mm above skin) would reach 209.5 mm from O. The polygon tube's underside at mid-chord is only 210·cos 10.35° − 4 = 202.6 mm. That is **a 7 mm collision**.
- **Fix:** `R_BAIL = ceil((HA + 86 + 25 + 3 + 4) / cos 10.35°) = 220`, which gives 3 mm clearance. The value is parametric in `halo_params.scad`, and the interference sweep checks it.
- **Cost:** about +2 g and +10 mm of height.

## 6. Track: a 10 × 1 strip on 9 mm posts; the carriage rides the strip only

- **Spec C24/M5:** a 3 × 1 strip on the node crowns; V-rollers grooved "for the strip + tube"; detent notches cut in the strip.
- **Problems:**
  - Between nodes, the polygon tube sits up to **3.6 mm lower** than at the nodes, so rollers riding both the strip and the tube would lift off or bind.
  - Notches cut into the face of a 1 mm strip remove up to 75 % of its section.
  - A 3 × 1 × 1000 mm pultruded strip is not stocked in the US. A 10 × 1 × 1000 is $17.94 [cited: Amazon B09Q8FF7RR, 2026-10-02].
- **Built:**
  - A 10 × 1 strip bonded to 3 × 8 mm posts on side B (rear) of nodes N0, N±1 and N±2. The strip's inner face is at R 233.
  - 2 outer + 2 inner MR63ZZ rollers ride the strip only.
  - PTFE-taped lateral guide faces.
  - Notches are 0.75 mm, 90° V-notches **filed in the strip's front edge**, using a jig (H20).
  - The strip runs −45.5° … +45.5°.
- **Mass:** +3.5 g.

## 7. α front-stop rule: "α_hairline + 20°" puts the nails in front of the hairline

- **Spec §4.7, M4:** α_stop = α_hairline + 20°.
- **Problem:** the nails reach **35 mm** from the pad axis (block ±17 mm plus pentagon R 18). 20° on an 88–92 mm scalp radius is only about 31 mm, so the front nails land ≈ 4 mm **in front of** the hairline (red line 6).
- **Built and procedure (halo.md §9):** the front stop is set on Michael's head so that the nail reach is **≥ 15 mm behind** the hairline. The 15 mm is the C4 halo displacement. On the design head this is α_pad ≥ −29° (spec default −25°; with the spec's rule it would have been −41°).
- **Hardware:** the α stops are adjustable blocks (5° steps; pins plus an M3 clamp).

## 8. β stops ±40° are too close to the ear if the halo slips 15 mm (C4)

- **Measured on the design head:** at β 40° the nail reach is **32 mm** from the ear canal when seated. Red line 6 (≥ 25) passes. C4 then moves the halo 15 mm, which leaves 17 mm.
- **Procedure:** set the β stops on Michael's head so the reach is ≥ 40 mm from the canal when seated. That is ≈ β ±35° on the design head.
- **Coverage effect:** total coverage falls from ≈ 85 % to ≈ 82 % [EST] (halo.md §10). The stop blocks clamp anywhere on chord 3, so ±40° is still available if his ears are lower or further back.

## 9. Harness routing on the head: about 0.72 m (31 g), not 0.5 m (21 g)

- **Spec T4:** "box → clip → right hub bore → along the bail in a clip track → carriage → 150 mm service loop".
- **Problem:** the carriage travels ±147 mm along the bail, so a fixed clip track cannot end at it.
- **Built:**
  - Clips (H16) on the right leg and right arc, on the rear side B, up to a zip-tie anchor on the vertex node (H08b).
  - Then a **free 230 mm arch** to the carriage, the way bike-brake housing loops work. It stays ≥ 100 mm above the scalp.
  - Then the 150 mm service loop to the pad.
  - The housings' 25 mm minimum bend radius sets the arch.
- **Mass:** +10 g.
- **Alternatives:** a rolling-loop band (printer-carriage style) or a fourth "skyhook" line. Both are open to the Director; neither is built.

## 10. The umbilical leaves on the ear axis from the rotating right foot, not through a bore in the static boss (M15)

- **Spec M15:** a Ø14 bore along the ear axis in the right boss.
- **Problem:** the hinge knuckle occupies the ear axis between the boss and the foot, so a bore through the static boss cannot connect to the bail.
- **Built:**
  - A 30 mm carbon stub (8 × 6) bonded on the axis into the right foot (H05R).
  - A clamp (H17) at its end that holds the bundle within 12 mm of the axis at |Y| ≈ 160–175 and carries the pogo-lanyard seat.
  - Turning α twists the free loop by up to 125°, spread over ≥ 450 mm; lengths do not change.
  - The housing bend radius (R 25) is what puts the exit about 35 mm outboard of the hub.
- **Pad 2:** "bore sized for two harnesses" becomes a second clamp on the same stub.

## 11. Mass ledger: item by item against spec §4.8 (default build, Airpel + medium hinges)

| Block | Spec g | HALO g | Why |
|---|---|---|---|
| Retention (band, forehead, cradle, temples, doff) | 53 | 57 | cradle arms (7.8) are not in the spec |
| Hubs (plates, hinges, feet, stops, plunger) | 30 | 105 (70 small) | hinges 32 (18 small) plus printed hub plates and feet sized for the hinges |
| Bail (tubes, nodes, strip, stops, clips, epoxy, M3) | 36 | 69 | nodes 2.2 g each, not 1.5; stops, clips, epoxy and hardware were not counted |
| Carriage | 10 | 16 | float nose plate and steady collar, rollers, pins |
| Float | 24 | 117 (36 light) | item 1 |
| Pad | 81.5 | 81.5 | PAD WP |
| Harness + umbilical + lanyard | 37 | 43 | item 9 |
| Fasteners / provisions | 12 | inside the rows above | — |
| **Total** | **286** | **488 (373 light + small)** | |

**Diet still open** (≈ −25 g in total):
- aluminium M3 screws (−5 g);
- 16.7° chords to ±50° instead of 20.7° to ±62° (item 12; −2 g);
- no stop ring if a hinge with built-in stops is found;
- a lighter dial cradle.

Even with the diet, the best realistic single-pad helmet is ≈ 350–370 g.

## 12. The bail is 400 mm wide at the shoulders

- **Cause:** six 20.7° chords at R 220 reach β ±62°, so the shoulder nodes sit at |Y| = 194.
- **Not needed:** β travel is only ±40° (plus a 6° carriage half-length), so the arc only has to reach ≈ ±50°.
- **Proposal:** six 16.7° chords (64 mm each) to ±50°. Width ≈ 330 mm, sagitta 2.3 mm, −1.6 g.
- **Implementation:** a two-number edit (`CH_DEG = 16.7`) once the Director releases C24. The geometry checks would need rerunning.

## 13. Pad-2 provisions: what is kept and what is not possible

**Kept:**
- the split vertex node (H08a/H08b, 2 × M3 splice, M18);
- the right exit stub, which takes a second bundle clamp;
- the 2.0 N tangential coupling and the drums (other WPs).

**Not possible as specified:** "right hub boss: second-hinge seat (M2 pattern)".
- A second coaxial E6 hinge would need the same Y span as the first.
- Pad 2's half-bail needs its own pivot outboard of the right foot. That means a C-bracket hub (≈ +20 g), to be designed when pad 2 is bought.

**Twin mass:** pad 2 adds ≈ 150 g, which puts every option over 500 g. Twin needs the light float **and** the diet in item 11 **and** a lighter pad.

## 14. M8 kinematic mount: ball-side choices PAD must match

- **Spider (H12) arms** at 30°, 150° and 270° in the pad frame P (x_P = track tangent, toward the right ear; y_P = forward). These angles keep clear of the tendon stops at 90°, 210° and 330°.
- **Balls:** Ø5 at R 55, protruding 3.0 mm below the spider underside.
- **Magnets:** N52 Ø6 × 3 at R 42 in the spider. PAD must put **3 steel discs Ø8 × 1 at R 42** under them, plus V-grooves at R 55 on the same angles.
- **Breakaway:** set by the disc-to-magnet air gap; 6 ± 2 N is a B3 test.
- **Spider top:** 86 mm above skin (RCC ring at 80).

## 15. Front band: two 10 × 1 strips, bonded, at 0.76 % bending strain

- **Spec C25:** a 20 × 1 strip at 0.5 % strain.
- **Supply:** 20 × 1 × 1000 pultruded strip is not stocked (the agent checked Amazon, CST, DragonPlate and eBay US). Cutting it from 1 mm plate needs a diamond wheel and carbon dust control, which is not first-timer friendly.
- **Built:** two 10 × 1 pultruded strips edge to edge (same EI), bonded into pockets in the hub plates (+1 M3 cross-bolt) and in the forehead node.
- **Strain:** the forehead node curve (R 66 on the design head) gives **0.76 % strain**. Pultruded carbon fails near 1.5 %. [VERIFY with a 24 h bend soak on a spare strip before bonding.]
- **Forehead node:** no bolts, so no bolt heads under the forehead foam.

## 16. Head-present switch: needs the low-force D2F-01FL and an adjustment step

- **Part change:** the D2F-01L takes 0.78 N to operate; the **D2F-01FL takes 0.25 N** (Omron en-d2f.pdf). Its overtravel is only 0.55 mm.
- **Built:** a sprung trigger plate (H14) on two Ø3 pins with 1–2 mm of proud foam. The switch is epoxied after a click test (halo.md §11 step H7).
- **Wiring:** a NO contact, so the loop is closed when the head is present and open when the switch or a wire fails.

## 17. Spec text contradiction: where O is relative to the ear canal

- **§3.1:** "O … 45 mm above and 10 mm **behind** the tragion midpoint".
- **§3.2 table:** "Ear canal (tragion) in H (−10, ±72, −45)", which puts O 10 mm **in front**.
- **Choice:** HALO uses the table (and measures it: `TRAG_X = −HA + OT`).
- **Action:** CAD/firmware should confirm they use the same.

## 18. Float retract spring

- **Spec:** "retract spring 1.2 N preload" (1.2–1.7 N).
- **Problem:** Airpot's spring-return E16X only gives 0.67 N when retracted, which is below the 0.8 N pad weight.
- **Built:** a McMaster **9293K123 constant-force spring, 1.60 N** ($7.57) [cited: mcmaster.com constant-force springs, 2026-10-02], on a spool fork on the carriage, anchored to the spider.
- **Check:** net retract at the vertex is ≈ 0.58 N, so 25 mm takes ≈ 95 ms (B4 asks ≤ 150 ms) [EST; VERIFY B4].

## 19. Printing cost: JLC3DP charges US individuals a 40 % tariff on nylon and resin (DDP)

- **Source:** jlc3dp.com US tariff FAQ, updated 2026-03-19, checked 2026-10-02.
- **Effect:** the E3 outsourced-print saving shrinks. The HALO MJF batch is ≈ $70–100 including the tariff, plus ≈ $20–30 shipping [EST].

## 20. Smaller notes

- **Detent clocking:** α notches are cut for α_pad = 15k (k −3…7). β notches are at β = 10k. The carriage is installed with its +x toward the right ear (the plunger is 16 mm right of the carriage centre); halo.md §4.4 gives the notch table.
- **Alpha fold range:** the leaves open from 51° to 176° over the α range. The check `hinge fold` in `gen_halo_stl.py` guards it. The E6 rotation limit is not published [VERIFY on arrival: open the hinge flat by hand].
- **Hair zone:** every HALO part except the forehead/temple pads, cradle and cradle arms is ≥ 30 mm from the scalp. The hinge knuckles are at |Y| ≥ 94 (17 mm off the side scalp at hub height) but outboard of the hub plate, and nothing rotates there during play; in the C-stage wrap test, check that no hair reaches the knuckle.
