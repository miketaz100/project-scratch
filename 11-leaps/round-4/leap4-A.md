# LEAP-4 A: Collapse the pin and air system

**Project SCRATCH · 11-leaps/round-4 · Agent A · 2026-10-02**
**Provocation:** with 6 pins and an on-par-scratch goal (not a human illusion), does each pin still need its own valve, tube, restrictor, bleed and hover collar?
**Tags:** [KNOWN] from a project file · [EST] my arithmetic (scripts `dish.py`, `tri.py` in the session scratchpad) · [JUDG] judgement · [VERIFY] a bench check is needed.

---

## 0. Verdict

1. The baseline already has **one force rail** for all pins. Its 6 valves, lines, sensors, restrictors, bleeds and collars buy only **when each pin bites and lifts**. Under the amended goal that is worth little: the analysis scored "stamp" IRRELEVANT, and the surviving anti-habituation levers come from the path and the rail.
2. Half the per-pin hardware patches **a flat block scrubbing a round head**. Each edge pin chases 4–8 mm of skin per stroke [EST], which is what forces the 24 mm stroke, the metered descent (RT1's ratchet) and the friction collar (RT1's parasitic).
3. **Best bet, the DISH GATE (L3).** The block rides a printed seat concentric with the scalp, so pins stay within ≤ 1.3 mm of their skin distance (≤ 2.9 mm on the sides). The seat's rim rises 8.5 mm, so **the stroke path does the gating**: past an offset of ≈ 9–11 mm every nail lifts 5–7 mm. The six pins become passive air springs on **one open line**: no pin valves, restrictors, collars, per-pin sensors or vacuum.
4. **If adopted** (built as L3-2, two pin lines): ≈ 130–195 h, ≈ $1,220–1,350, ≈ 362 / 463 g (twin legal even without the ladder), tubes 11 → 6, joints ≈ 78 → 46, sensors 16 → 6, P(on-par) ≈ 0.43–0.44, P(≥ 7/10 in 26 weekends) ≈ 0.26. The cost is programmable landing order and free subset choice (two fixed groups remain).

---

## 1. What the per-pin air system costs, and what it actually buys

### 1.1 Inventory [KNOWN from the spec and decision-analysis; counts EST]

- **Per pin (×6, plus 6 pad-B cartridges):** a Penrose sleeve, piston, shaft, guide and wiper (the actual force element); a needle restrictor with a duckbill bypass; a bleed; an O-ring hover collar and a return spring.
- **In the box, per pin:** an S070 valve, a sense orifice, a sensor and a 1.4 m line.
- **Shared:** a vacuum pump, accumulator, breaker, LIFT SELECT and lift manifold; the 6-lumen pad loop; 6 pad-B tees; the per-pin gate scheduler, latency calibration and subset tables in firmware.
- **Totals:** ≈ 78 pneumatic joints (≈ 96 twin), 11 tubes (14 twin) and 16 sensors (10 staged). Each pin adds ≈ 7.0 g to the head, of which 3.7 g is tube.

### 1.2 What the per-pin valves buy under the amended goal

- **Force per pin:** nothing. One rail sets every pin's force (spec C7).
- **Landing jitter (σ_t ≥ 20 ms):** RT1 #7 "stamp" is now IRRELEVANT. The jitter still guards against habituation and the synchro's 25 Hz ring (RT1 #13), and pins landing at different heights supply it for free (§4).
- **Subsets** (all-6, 3-rows, single pins): a real anti-habituation lever. This is the one genuine loss.
- **One-flank bites** (with-grain rakes): useful for hair (H-5.1). A path recovers them (§4, "D-paths").

### 1.3 The hidden root cause: a flat block on a round head

The block translates ±15 mm in a plane; the scalp falls away beneath it. Spread of nail-to-skin distance across the six pins, worst heading [EST, `dish.py`]:

| Region (radius) | Flat block, contact zone (\|d\| ≤ 10.5) | Flat block, full stroke | **Concentric seat**, contact zone | Concentric seat, full stroke |
|---|---|---|---|---|
| Bun R 65 | 5.5 mm | 7.9 | **1.3** | 1.9 |
| R 70 | 5.1 | 7.3 | **0.9** | 1.3 |
| Crown R 85 | 4.2 | 6.0 | **0.0** | 0.0 |
| R 100 | 3.6 | 5.1 | **0.6** | 0.9 |
| Sides 70 × 150 | 5.1 | 7.3 | **2.2** | 2.9 |

That 4–8 mm is why the spec needs a 24 mm stroke, metered descents and last-touch collars. It also causes RT1's ratchet: outward-flank edge pins lose 55–90 % of their force. **Fix the geometry and most of the per-pin air system has no job left.**

---

## 2. LEAP 1: ONE VALVE, ONE LINE (common-mode bite, collars kept)

**(a) Assumption broken.** "Bite and lift must be per pin."

**(b) Principle and sketch.** The six pins share one printed gallery in the block, fed by **one 3×2 line** from the box.
- **BITE** (S070): rail → one Ø 0.5 needle (sized for 6 pins at 50 mm/s) → line.
- **HOLD** (cheap 3-way): opens ≈ 60 ms after the bite, bypassing the needle, so pins in contact follow the skin both ways at near-constant force.
- **Both de-energised:** the line vents and the pins lift on their return springs. Fail-to-free is kept.
- The passive O-ring collars still give each pin a hover 5 mm above its own last touch.
- The vacuum system goes; parking for hops uses vent plus float retract.

```
 RAIL ─┬─[BITE S070]─[Ø0.5 needle]─┬─► one 3×2 line ─► block gallery ─┬─ pin 1 (collar, return spring)
       └─[HOLD 3-way]──────────────┘   (Ø0.15 bleed at gallery)       ├─ … pins 2–6 (no restrictor, no duckbill)
       both off = vent                                                └─ pad B: one tee at the rear node
```

**(c) Numbers moved.** Valves 6 → 2. Pin lines 6 → 1, so umbilical tubes 11 → 6. Sensors −5. Joints ≈ 78 → ≈ 50.
- **Hours:** −15 to −25 h (no gate scheduler, no per-pin latency calibration, no V6/V8 per pin, no vacuum).
- **Cost:** −$150–230 with S070s (−$60–90 if the cheap-valve A/B had won).
- **Mass:** −5 lines × ≈ 2.2 g (light) ≈ −11 g single, ≈ −22 g twin [EST].

**(d) Plausibility.**
- **Line flow:** 6 pins × 38.5 mm² × 40 mm/s = 9.2 ml/s, which drops 0.6 kPa (0.02 N) along a 2 mm ID, 1.4 m line [EST, Poiseuille]. So HOLD removes the ratchet.
- **Collar parasitic:** stays wherever an edge pin chases more than its 5 mm of lost motion (curved regions, §1.3): ±0.08 N on 0.25 N.
- **Landing spread:** sleeve and collar friction scatter plus skin-height scatter give ≈ 10–30 ms [JUDG].

**(e) Cheapest experiment (≈ $20, an evening).** Three Penrose pins on one tee, one S070, one 27G needle plus a bypass valve. Drag over an R 70 dome with ink on the nails, and compare against one pin fed through its own needle. GO if HOLD shows unbroken ink on both flanks and the single-needle pin shows the outward-flank skips.

**(f) Replaces** the per-pin plumbing, vacuum and gate scheduler. **Keeps** collars, the flat block and the 24 mm stroke.

**(g) Might fail because** the collars stay (the tightest-tolerance part, RT3 2.6, and RT1's parasitic), and a late HOLD brings the ratchet back.

---

## 3. LEAP 2: TWO TRIANGLES (alternating halves, no collars)

**(a) Assumption broken.** "Every pin must bite on both flanks, so it must hover."

**(b) Principle.**
- **Layout:** six pins on a hexagon at R 18, wired as two interleaved triangles (side 31 mm) on **two lines**.
- **Timing:** group A bites outbound, group B inbound. Each pin's contact path is then **monotonic** (one direction, lifted for the return), which H-5.7 calls hair-positive.
- **No hover needed:** each pin is off the skin for ≈ 525 ms per cycle at 1.4 Hz (357 ms return + 168 ms end zones) [EST]. That is enough to vent to a fixed park, then descend 13 mm (worst flat-block spread 8 mm + 5 mm lift) at 50 mm/s in 260 ms. **Collars disappear.**
- **Modes:** A, B, alternating, or both on both flanks (f ≤ 1.0 Hz). A PWM servo on line B gives A ≠ B force contrast.

**(c) Numbers moved.**
- **Valves:** 6 → 4 (BITE/HOLD per group, or 2 valves plus 2 pressure servos).
- **Lines, sensors, joints:** lines 6 → 2 (tubes 11 → 7); sensors 6 → 2; joints ≈ 78 → ≈ 58.
- **Hours:** −12 to −20 h. **Cost:** −$100–160. **Mass:** ≈ −9 g single, ≈ −18 g twin.

**(d) Plausibility.**
- **Tracks per triangle:** 2.7 on average. Two pins share a track (within 5 mm) in **32 %** of headings [EST, `tri.py`]; all six give 4.25 tracks.
- **Edges per flank:** alternating mode gives 3 per flank, against 6 in the hybrid. The analysis called six-in-two-ranks "the strongest scratch-quality argument for 6", but a hand uses 4.
- **Descent:** the metered descent still exists per group, so the restrictor ratchet needs a HOLD path per group.

**(e) Cheapest experiment (≈ $25).** Two 3-nail syringe triangles on two valves; rate alternating against both-flanks blind at 1.0 and 1.4 Hz.

**(f) Replaces** collars, the per-pin plumbing and the vacuum. **Keeps** the flat block.

**(g) Might fail because** 3 edges per flank may feel thin, and the four valves keep all of L1's timing dependencies.

---

## 4. LEAP 3 (BEST BET): THE DISH GATE. The path does the gating

**(a) Assumptions broken.**
1. "The pin block scrubs in a plane." It should scrub on a sphere concentric with the scalp.
2. "Lift and bite are actuator events." They become positions on the path.
3. "Descent must be metered by an orifice." The slope of a printed surface meters it instead.

**(b) Principle and dimensioned sketch.** The deck's underside, above the block, is printed as a **dish**.

- **Centre (offset \|d\| ≤ 7 mm):** a sphere of R ≈ 160 mm (scalp R 85 + ≈ 75 mm follower height) about the skid-registered scalp centre. The block tilts ≤ 5.5°, so nails keep a constant gap to an R 85 scalp.
- **Rim:** the ceiling rises 4.5 mm at 38° (to r ≈ 12.8), then 4 mm more at 65° (to r ≈ 14.7). Working amplitude ±15.5 mm, inside the Ø 20 slaves' 34 mm stroke.
- **Support:** three POM domes on the block ride PTFE tape on the dish. The pins' reaction (Σ ≈ 1.2–1.8 N) presses the block up while in contact; a 0.5–0.6 N deck-to-block tension carries its ≈ 35 g on the rim.

```
 SECTION through the pad axis (not to scale; heights above skin)
                 deck (still) ──────────────────────────────────────────────
  dish ceiling:  rim 65°  ╲ rim 38° ╲___ sphere R≈160 (|d| ≤ 7) ___╱ 38° ╱ 65°
  (PTFE tape)      +8.5     +4.5        0                          +4.5   +8.5
                  ▲ dome  ▲ dome   ▲ dome      (3 POM domes on the block)
               ┌────────────── pin block (moves ±15.5 mm, tilts ≤ 5.5°) ─────┐
               │ gallery ◄─ ONE 3×2 line (from box: rail ─ PIN 3-way ─ 250 ml) │
               │  │    │    │    │    │    │   six Penrose pins on one gallery │
               └──┼────┼────┼────┼────┼────┼───────────── underside ≥ 32 mm ──┘
                  ┃    ┃    ┃    ┃    ┃    ┃   rigid Ø1 shafts, drafted POM cones
       ~~~~~~~~~~ ▼ ~~ ▼ ~~ ▼ ~~ ▼ ~~ ▼ ~~ ▼ ~~~~~~~~~~ skin (constant gap ±1–3 mm)

 PLAN: offset of the block d (mm). Pins down inside the inner ring, lifted outside it.
        ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·       |d| 0–7      concentric: pins at constant force
     ·        ╭───────────────╮        ·      |d| 8.3–11.5 each pin lands or lifts (by its reserve)
   ·     ╭────┤  contact disk ├────╮     ·    |d| ≥ 12.8   all pins ≥ 5 mm clear
     ·        ╰───────────────╯        ·      |d| 14.7     top of rim (+8.5)
        ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·
 LINE / PLINE: a 31 mm line through the centre: lands, rakes 17–23 mm, lifts at both ends.
 D-PATH: chord through the centre (pins down), return round the rim (pins up): one-way rakes.
 CIRCLE: R 11.5 offset 3.5: |d| 8 → 15 once per rev, contact on ≈ 40 % of each revolution.
```

**The pins.** Sleeve, piston, rigid Ø 1 shaft with the must-fix drafted cone, guide, wiper, 0.03 N return spring; 12 mm stroke (from 24). No collar, restrictor, duckbill or per-pin bleed; one Ø 0.15 bleed on the gallery is the trapped-pressure backstop. Force is **rail × area, constant on both flanks**: the line is open, so a pin rising over a clump pushes air away and a pin whose skin drops refills at once. Each landing exchanges ≈ 0.6 ml [EST]; a **250 ml bottle accumulator** in the box holds the ripple to ≈ 0.6 kPa (0.02 N). One **PIN 3-way valve** feeds the line and vents it when de-energised (fail-to-free backup, full park).

**How a stroke works.** A pin's "reserve" (extension left before its stop) varies 1–3.5 mm with residual curvature. Running down the rim, each pin lands when the block height equals its reserve: plough-in is the printed **38°** (66 mm/s vertical at 1.4 Hz [EST]; the spec accepts 35°, so print 33–35° if the rim fits). Reserves differ by up to 2.5 mm, so landings spread **≈ 30–40 ms**, natural asynchrony above RT1's 20 ms floor with no firmware. Going outward, pins leave the skin at ≈ 0.7 v_peak (H-5.3 asks ≥ 0.3) and rise 5–7.5 mm clear.

**Modes** (they need the **XY belt master**, already pending Michael's OK). PLINE and LINE run through the centre; the rim is round, so every heading works. CIRCLE runs offset, crossing the rim once per revolution, which is E3's lift-per-revolution by construction; a full canopy exit is one PIN vent on the rim (refill ≈ 1.1 kPa from the bottle [EST]). New, for free: **D-paths** (one-way with-grain rakes, H-5.1/5.7) and **off-centre chords** (5–17 mm contacts, the stroke-length jitter RT1 #1 wanted). Rests park the block on the rim; hops add the usual float retract.

**(c) Numbers moved.**

| | Baseline hybrid | Dish gate |
|---|---|---|
| Pin valves | 6 S070 + LIFT SELECT + vacuum system | **1 cheap 3-way (PIN)** |
| Umbilical tubes, single / twin | 11 / 14 | **5 / 9** (10 with a separate pad-B force line); Ø ≈ 17 → ≈ 12 mm |
| Pneumatic joints, single / twin | ≈ 78 / ≈ 96 | **≈ 42 / ≈ 52** |
| Sensors (staged A–C) | 16 (10) | **5**: rail, palm, 3 synchro (+3 egg later) |
| Per-pin parts on the pad | sleeve + collar + restrictor + duckbill + bleed + spring | sleeve + spring |
| Air use, line mode | ≈ 1.0 L/min (a vented bite every stroke) | **≈ 0.1 L/min** (bleeds only): pump at low duty, no exhaust puffs, no valve clicks |
| Head mass, single / twin (light lines, ladder) | 369 / 480 g | **≈ 360 / ≈ 460 g**; twin ≈ 489 g **without** the ladder |
| Hands-on hours | 165–230 | **≈ 130–195** |
| Parts cost | $1,450–1,500 | **≈ $1,200–1,330** |

**Mass** [EST]: −11 g (5 light lines) −1.8 g (12 mm cartridges, no collar) +3.5 g (dish, domes, tape, lift spring) +0.6 g (3×2 line for flow) ≈ −9 g per pad, plus ≈ −3 g from the thinner loop.

**How the hours were worked out** [EST]:

| Removed | h | Added | h |
|---|---|---|---|
| valves, sense orifices, sensors, wiring | 6–9 | dish CAD + 2–3 print iterations, domes, tape, spring | 8–12 |
| vacuum system | 2–4 | ink-trace gate on R 85 and R 65/side mocks | (in above) |
| needles, duckbills, bleeds, collars ×12 | 6–10 | path rules: rim reversals, D-paths, chords, offset circles + checker | 4–6 |
| V6/V7/V8 per pin, latency calibration | 6–10 | 250 ml accumulator | 0.5 |
| harness routing, tees, leak hunting (≈ 36 fewer joints) | 5–8 | | |
| gate scheduler, subsets, alternating sets, collar/vacuum park firmware | 12–20 | | |
| **Total** | **37–61** | **Total** | **12–18** |

That is a net of **−25 to −43 h**.

**Cost** [EST]: −6 S070s ($210, or ≈ $45 at cheap-valve prices), −5 sensors (≈ $40), −vacuum set (≈ $35), −needles/duckbills/O-rings (≈ $15), −5 lines and tees (≈ $30), +≈ $26 → **−$140 to −$300**.

**(d) Plausibility, with numbers.**
- **Residual excursion per pin within one contact stroke:** ≤ 0.7 mm (R 100), ≤ 1.4 mm (R 65), ≤ 1.9 mm (sides) [EST], against 4–8 mm for a flat block. At constant air force this costs nothing; even a 0.02 N/mm spring pin would vary only ±0.04 N (that is L4).
- **Rim loads:** ≈ 1.7 N inward on either rim flank [EST], i.e. ≈ 1.7 mm of copy shrink where pins are lifting anyway, inside the 4 N tangential cap. PTFE on POM (μ ≈ 0.1) adds ≈ 0.25 N drag in contact (0.25 mm shrink).
- **Hair zone:** the block underside only rises (≥ 32 mm); dish, domes and tape sit ≥ 70 mm up. No new joint enters the exclusion volume.
- **Red lines:** line 2 is still the rail relief (0.96 N) with the pump-stall backup; line 3 the float relief; line 8 the float spring plus a de-energised PIN vent. Lift-before-reversal now rests on geometry (any reversal outside \|d\| = 12.8 lifts every nail) plus one checked path rule, not on six valve latencies and a scheduler.
- **Prior art:** round-2 C2 also gated by geometry but needed an 8 µm lapped commutator seal; the dish needs no seal.

**(e) Cheapest experiment (≈ $30, one weekend).**
Print a Ø 70 mm deck with the dish underside (PTFE-taped) and a block with 3 POM domes and 3 drafted-cone nails on three 1 ml syringes teed to the S0 pump line (relief + bleed), or on 0.02 N/mm pen springs the first evening. Stand it on skids on a paper-covered Ø 170 play ball (R 85); drive the block by hand through printed templates (line, D, offset circle). Measure ink chords (15–23 mm), lift with feelers (≥ 5 mm), landing angle and spread on a 240 fps phone (≤ 38°, ≥ 20 ms); repeat on a 70 × 150 side mock. Then a helper holds it on the scalp: "scratch, not brush" and "crisp on both flanks" against the S0 single pin. **GO:** chords ≥ 15 mm, lift ≥ 5 mm everywhere, ≥ 6/10.

**(f) Replaces** the pin valves, vacuum system, 5 pin lines, 6 sensors, 12 collars, restrictors and duckbills, 11 bleeds, the 6-lumen loop and the gate scheduler. **Keeps** synchro, float, RCC palm, skids, rails, halo and twin provisions. **Needs** the XY master. **Spin-off:** even with per-pin gating, a concentric seat alone removes RT1 #3 (the ratchet) at its root.

**(g) Honest reasons it might fail.**
1. **Snag pull.** A nail caught by a strand is lifted by the block's lift tension, ≈ 0.5–0.6 N, against ≈ 0.05 N (return spring) to 0.31 N (vacuum park) in the baseline. The gating stop also limits pin reserve to ≈ 3.5 mm, below RT2's must-fix of ≥ 12 mm. Mitigations:
   - the drafted cone (no neck) makes capture rare;
   - give the block ≥ 12 mm of vertical free travel below the dish, so the deck can retract 12 mm while a held block hangs on ≤ 0.6 N;
   - snag reflex = stop the path and vent;
   - SP2 option: drive the lift tension from an inverted pin cartridge on the PIN line, so a vent makes the block limp.
   **For RT2 to rule on.**
2. **Dish noise or stick-slip.** If PTFE-on-POM squeaks or stick-slips at 130 mm/s, the pad buzzes into the skull (RT1 #6's vibration cue). Bench it with a phone accelerometer.
3. **Anisotropic sides** (2.9 mm spread) eat the 3.5 mm reserve budget. A region-keyed rim height (a second dish) is the fallback.
4. **Contact length** is capped at ≈ 23 mm by the rim (baseline ≈ 22 mm). Longer rakes come only from travel sweeps (P2).
5. **One rail for all pins:** subsets and landing order are no longer programmable. If blind sessions show habituation that path variety cannot fix, go to L3-2 below.

**Variant L3-2 (two lines, ≈ +$25, +2 h).** Split the six pins into two gallery groups on two lines and two PIN valves, with a PWM pressure servo on line B. A vented group retracts and sits out; the switch happens while the block is on the rim, so **no metering is needed**. This restores A / B / all subsets and A ≠ B force contrast for one extra tube and sensor.

---

## 5. LEAP 4: SPRING NAILS (no pin air at all), on the dish

**(a) Assumption broken.** "Constant force needs air." On the dish, a pin only has to hold force over ≤ 2 mm of in-stroke excursion plus clumps. That is exactly the "small residual travel" the provocation names.

**(b) Principle.** Each pin is a shaft in a PTFE bushing, pushed by a **long soft compression spring** (0.015–0.02 N/mm, ≈ 50 mm free length, preloaded to 0.25 N) against the same gating stop.
- **Force spread:** ±0.03–0.04 N over ±2 mm (±15 %), inside the human ±30–50 %.
- **Intensity:** a manual **three-detent spring-seat ring** on the block (0.15 / 0.25 / 0.35 N), set before donning. A centre zone printed 1.5 mm deeper than the outer contact annulus makes centre strokes bite ≈ 0.03 N harder than chords: a little "force by path".
- **Tensators:** catalogue minimum loads ≈ 0.25–0.5 N and fatigue at 3,400 cycles per session are both [VERIFY]; a long coil spring is the honest SP1 choice.
- **Block lift:** a Ø 10 sleeve on the deck, teed off the existing palm line, pulls the block up through a short tendon (0.8–1.3 N at 10–17 kPa). A palm vent then also makes the block limp, which answers L3's snag-pull item for free.

**(c) Numbers moved against L3.**
- **Deleted:** the PIN line (tubes 5 → 4 single, 9 → 8 twin), the rail pump P1, accumulator, R1a/R1b, rail bleed, rail dump, rail sensor, the PIN valve and the 6 + 6 Penrose sleeves, which **retires the V4 sleeve-life risk on the pins**. SYNC CHARGE moves to the palm rail; the must-fix p₀ of 8–12 kPa is inside its range.
- **Savings against L3:** ≈ −$45–60, −5 to −8 h, ≈ −3 g per pad.
- **Red line 2 gets simpler:** spring at its stop ≤ 0.6 N, a pure mechanical constant.

**(d–f)** 0.015–0.02 N/mm in Ø 3–4 × 50 mm is assortment stock [VERIFY]; a bore stops buckling. Experiment ($15, inside L3's): a spring assortment and a kitchen scale, then L3's bench with spring pins. Replaces the pin rail and every pin sleeve.

**(g) Might fail because** there is **no per-stroke force variation** (scratch-model §4.4 resamples force every cycle) and no in-session intensity control except stopping to turn a ring. I score it about −0.04 on G1 and G4 combined against L3. It is the fallback if the pin sleeves fail life, or if Michael finds he never touches the force knob.

---

## 6. Considered and rejected

The float as the lift (skids pat at 2.8 Hz: tapping). Rigid nails loaded by the float (fails scratch-model criterion 9; load collapses onto 1–2 nails). A radial cam on a flat block (needs a 13–15 mm lift per reversal). A common lifter plate with per-pin friction clutches (the collar parasitic returns at ≥ 0.4 N).

---

## 7. Comparison and what each loses

| | Valves (pins) | Tubes s/t | Joints s/t | Sensors | Δ mass s/t (g) | Δ hours | Δ cost | What is lost [JUDG gate deltas] | P(on-par \| session) |
|---|---|---|---|---|---|---|---|---|---|
| Baseline hybrid | 6 + vac | 11/14 | 78/96 | 16 | 0 | 0 | 0 | — | 0.40 |
| L1 one valve | 2 | 6/9 | 50/60 | 11 | −11/−22 | −15…−25 | −$60…−230 | subsets, σ control (G4 −0.03); collars stay | ≈ 0.40 |
| L2 two triangles | 4 | 7/10 | 58/70 | 12 | −9/−18 | −12…−20 | −$100…−160 | 3 edges per flank, both-flank mode ≤ 1 Hz (G2 −0.03); collars gone (G1 +0.02) | ≈ 0.39 |
| **L3 dish gate** | **1** | **5/9** | **42/52** | **5** | **−9/−20** | **−25…−43** | **−$140…−300** | subsets, landing order (G4 −0.04); no ratchet or parasitics (G1 +0.07); quieter (G3 +0.03) | **≈ 0.43** |
| L3-2 two lines | 2 | 6/10 | 46/56 | 6 | −7/−17 | −23…−41 | −$115…−275 | A/B subsets back (G4 −0.02) | ≈ 0.44 |
| L4 spring nails | 0 | 4/8 | 34/44 | 4 | −12/−26 | −30…−51 | −$185…−360 | per-stroke force, live intensity (−0.04) | ≈ 0.39 |

**Gate arithmetic for L3** (RT1's gate method, as in decision-analysis §1.4):
- **G1 crisp edge at intended force** 0.75 → **0.82**: constant force on both flanks, pins chase ≤ 2 mm, no ratchet, no collar parasitic.
- **G2 scratch, not brush** 0.85 → 0.85: all-active, no comb.
- **G3 no intrusion** 0.80 → **0.83**: no valve clicks, no exhaust puffs, pump at ≈ 10 % duty; dish noise is the new risk.
- **G4 no habituation** 0.80 → **0.76**: subsets and σ control lost; D-paths, chords and natural 30–40 ms spread gained.
- **G5 coverage and steering** 0.85.

The product is 0.374 against the baseline's 0.347. Scaled onto the baseline's correlated 0.40, that gives **≈ 0.43**.

---

## 8. Best bet and its case

**Adopt L3, the dish gate. Build it as L3-2 (two pin lines)** if the Day-0 cart can take one more 3-way valve and a sensor, and keep L4's spring nails as the drop-in fallback for the pin sleeves.

**The case.** Most per-pin hardware exists because a flat block scrubs a round head. On a concentric seat each pin chases ≤ 1–3 mm, so one open rail gives constant force on both flanks, and RT1's ratchet and parasitics vanish at their cause. The rim lets the path lift every nail before every reversal, at a printed plough-in angle and with a natural 30–40 ms landing spread, instead of through six valves, six latencies and a scheduler. Air use falls tenfold and the box stops clicking. Tubes go 11 → 5, joints halve, sensors fall 16 → 5, three [VERIFY] gates (V6, V7, V8) disappear, and the twin becomes legal without the mass ladder. What is given up (programmable subsets and landing order) is hand-likeness first and anti-habituation second; L3-2 buys most of the latter back for one tube.

**Revised estimate if the best bet (L3-2) is adopted** [EST / JUDG]:

| | Baseline hybrid | **Dish gate (L3-2)** |
|---|---|---|
| Hands-on hours | 165–230 | **≈ 130–195** |
| Parts cost (+ ≈ $185 tools) | ≈ $1,450–1,500 | **≈ $1,220–1,350** |
| Head mass, single / twin | ≈ 369 (light) / 480 g with ladder | **≈ 362 / ≈ 463 g with ladder; ≈ 492 g without** |
| Umbilical | 11 tubes, Ø ≈ 17 | **6 tubes, Ø ≈ 12** |
| P(≥ 7/10 \| full session) | ≈ 0.40 | **≈ 0.43** |
| P(reach a full session in 26 weekends) | ≈ 0.50 | **≈ 0.60** (−17 % hours, 3 fewer gates, half the leak hunt; new dish gate) |
| **P(≥ 7/10 within 26 weekends)** | **≈ 0.20** | **≈ 0.26** |

**Staging change.** Add the dish bench to the S0 week ($30). Stage A builds the dish block in place of the 6-valve manifold; the cart drops 6 S070s and the vacuum set. Stage A GO: chords ≥ 15 mm, lift ≥ 5 mm, plough-in ≤ 38°, spread ≥ 20 ms, rim shrink ≤ 2 mm, and the hand-held crown rating ≥ 6/10. If the dish fails, fall back to L1 (same pins, most of the savings).

**Sign-offs needed from Michael:**
1. the XY master, already pending, because offset circles and D-paths need it;
2. dropping pin subsets as a requirement;
3. RT2's ruling on the ≈ 0.6 N snag-pull bound against its ≥ 12 mm reserve fix.
