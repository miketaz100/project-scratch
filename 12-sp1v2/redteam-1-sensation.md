# RED TEAM 1 (SENSATION) — SP1 v2 "PUPPET HALO" will not feel like a person's fingernails

**Project SCRATCH · 12-sp1v2 · 2026-10-02 · Target: SYSTEM-SPEC.md (design freeze v2), DECISION-2.md**
**Mandate:** argue, with physics and numbers, that the frozen design will not feel like fingernails, then rank the fixes. The attack is one-sided by design. Where an attack is weak I say so, because a weak attack ranked high wastes build time. Tags follow the spec: [KNOWN], [EST] (arithmetic shown), [UNSURE] (needs a bench).

---

## 0. Thesis

The freeze fixed what killed earlier designs. Landings plough in rather than tap. Every stroke is a bidirectional rake that lifts at reversal. Force is capped by a constant, and the pad travels. What is left sits in the **substrate**, the layer under the score, which the κ-grammar and the ledger cannot touch:

1. **A crank clock.** Inside each phrase the stroke length, speed profile and period are fixed, lifts are not jittered, and the heading turns monotonically.
2. **A hover comb.** Eight or nine idle nails sweep the hair pile at 5 mm on every cycle, ungated.
3. **An air pin that rises freely but falls at ≤ 50 mm/s.** On curved regions it drops 55–90 % of its force on the outward flank of the edge rows. Its light end, where the first sessions run, is mostly spring and collar parasitics.
4. **A neck that is the softest element in the tangential chain.**
5. **Unbudgeted machine cues on the head.** Pad-side bleed hiss, a hat that leans as the pad travels, scrub reaction rocking the band, and servo hunting in a balanced geared axis.

None is fatal alone. Together they give the most likely first verdict: "a very good machine, scratching through my hair with a comb of pins."

**P(first good session rated "someone's fingernails") ≈ 0.12 as drafted, ≈ 0.28 after the top three fixes.** Those fixes are mostly firmware and cost almost nothing.

---

## 1. Attack 1 — Air-pin landings and drag: a crisp edge or a soft push?

### 1.1 Credit first

At contact, the Ø 0.22 restrictor closes off the pin chamber (≈ 0.8–1.0 ml at 20 mm extension). For small motions the chamber is therefore a **gas spring**:
- at 8 kPa: 109 kPa × 38.5/900 per mm = 4.7 kPa/mm, i.e. **0.18 N/mm**;
- with a 0.5 ml chamber: ≈ 0.34 N/mm.

That is pulp stiffness (tip-interface §1.3) over the first ~1.7 mm, where scalp micro-relief lives. Hover-and-bite lands at ≤ 35° with a 0.05–0.08 N transient and a ≤ 20 ms force ramp while moving, which is a nail-like tapered entry.

### 1.2 The light end belongs to the parasitics, and the spec contradicts itself

Three parasitic forces act on the nail:
- the return spring opposes the air with 0.05 N at hover, more at 5 mm extension;
- the collar adds or subtracts 0.08 N whenever travel exceeds the 5 mm lost motion;
- the diaphragm adds 0.01–0.03 N of hysteresis [EST].

Firmware sets rail = F/A, so:

| Commanded | Rail | Delivered (spring subtracted) | With collar slipping |
|---|---|---|---|
| 0.08 N | 2.1 kPa | 0.02–0.03 N (−70 %) | −0.06 to +0.11 N |
| **0.15 N (D1/D2)** | 3.9 kPa | **0.09–0.10 N (−40 %)** | 0.01–0.18 N |
| 0.30 N | 7.8 kPa | 0.24–0.25 N (−17 %) | 0.16–0.33 N |
| 0.45 N | 11.7 kPa | 0.39–0.40 N (−12 %) | 0.31–0.48 N |

**The A4 gate does not fit the design.** The gate reads "10 kPa → 0.385 ± 0.03 N". A pin built to §4.1 delivers ≈ 0.33 N at 10 kPa, so either it fails its own gate or the gate is passed by a pin that does not hover.

**The first sessions run where force is least reliable.** The Stage D protocol starts at 0.15 N, the setting where the parasitics dominate. At 0.09 N net, a Ø 2 nail does not part a 10–25 mm pile; it rests on it.

### 1.3 The restrictor ratchet: constant force only while the skin holds still

The duckbill vents freely, so the pin **rises freely**. It can **fall** only as fast as air flows in through the orifice:
- v_d ≈ 50 mm/s at ≈ 6.5 kPa of net drive;
- the orifice loss is ΔP = K·v², independent of the rail.

On a curved scalp, pins on a flat rigid block see the skin fall away at v_n = (x/R)·v_t.
- The edge rows (along-stroke offset ±27 mm) are the 3-nail rows the virtual hand steps into half the time. They sweep x from 18 to 39.75 mm.
- The contact window (s −0.6 → +0.85) lasts 189 ms at 1.4 Hz.

| Region | Row | Skin drop in the window | Mean v_n | Force lost, outward flank (0.3 N phrase) |
|---|---|---|---|---|
| Crown, R 90 | edge | 7.0 mm | 37 mm/s | **≈ 55 %** |
| Crown, R 90 | inner (±9) | 2.6 mm | 14 mm/s | ≈ 8 % |
| Bun, R 70 | edge | 9.0 mm | 48 mm/s | **≈ 90 % (skims)** |
| Bun, R 70 | inner | 3.4 mm | 18 mm/s | ≈ 13 % |

**What this does to the occiput.** On the inward flank the same row is pushed up past its lost motion, so it carries rail force plus 0.08 N. The edge-row rake on the occiput, the scratch-model's sweet spot (§5), is therefore one-directional and deterministic: strong inbound, skimming outbound, on every stroke. That is the opposite of a hand's random ±30–50 % per-finger force spread.

**Hair clumps get the same treatment.** Above ~1.7 mm (where the gas spring runs out) the nail clears a clump instantly, then descends at ≤ 50 mm/s.
- The steepest down-slope it can follow is atan(50/110) ≈ **24°**.
- A 2 mm clump costs ~40 ms airborne, i.e. **4–5 mm of track**, and the 20 ms force ramp restarts.
- A finger re-descends at once on its pulp spring.

So the air pin **ratchets toward the top of the mat**. The scratch-model gives 40–70 % skin contact in medium hair (§3.14, UNKNOWN). I expect 25–50 % from this pin [EST, UNSURE].

**Verdict:** the landing is crisp. Sustained contact is a soft, skating push on the edge rows, on curved regions and in medium hair, and at light force the hair can hold it off.

**Fixes:**
- Feed forward each pin's spring offset, and rewrite A4 as net force.
- Floor of **0.20 N net** for D1–D3.
- Every down pin in a row shares the same along-stroke geometry, so one rail *can* compensate. Boost the rail by K·v_n² (3.6 kPa at R 90, 6 kPa at R 70) on outward flanks, feed-forward from the scan curvature. This fits the 60 ms up-slew in a 357 ms half-stroke.
- Use inner rows or short strokes where R < 80.
- Bench: a kitchen scale under a 25° ramp moving at 130 mm/s, and an ink trace on an R 70 dome.

---

## 2. Attack 2 — Synchro compliance: rubbery strokes? Mostly not

This attack is **weak**.

- **Series compliance.** The neck and shaft are 0.12–0.2 N/mm tangential (§4.1), the synchro 1.0 N/mm. In series, the synchro adds only **7–17 %** of the compliance. If anything is rubbery, it is the neck (§5).
- **Stroke shrink.** 0.5 mm on a 22 mm contact stroke is 2 %, against a scalp acuity of 15–39 mm.
- **Filtering.** The air link is a 25 Hz low-pass: stepper full-step ripple (~280 Hz) arrives about 42 dB down. That is a real virtue of the puppet.

**What remains is a 25 Hz block ring.**
- The block is 40 g on 1.0 N/mm. From the §4.4 viscous drop (0.8 kPa at 1 Hz) I estimate ~4 N·s/m of damping, so **ζ ≈ 0.3** [EST].
- When a row lands together (σ_t = 0, as in the spec's own score line ph 1), drag steps by 0.37–0.74 N within 20 ms.
- The block lags 0.4–0.7 mm, overshoots ~35 % and rings for 40–80 ms: a ±20–35 mm/s, 25 Hz velocity ripple on the landed nails, in the RA flutter band.
- With σ_t ≥ 30 ms the drag rises over ~100 ms and the ring mostly vanishes.

**Verdict:** minor (P 0.25). **Fix:** never schedule σ_t < 20 ms; fit a Ø 0.8 mm damping orifice at each slave port (ζ ≈ 0.7); add a phone accelerometer to A3.

---

## 3. Attack 3 — The default precessing line is still machine-regular

### 3.1 The irregularity budget

Scratch-model §4.2–4.4 asks for:
- length ±25–35 %, speed ±20 %, interval ±20 %;
- force ±30–50 % per finger;
- direction wander ±15–30°;
- no (L, f, F, direction) tuple repeated more than 3 cycles.

| Dimension | Human | PLINE as frozen | Grade |
|---|---|---|---|
| Landing spread | 20–80 ms | σ_t 20–80 ms per pin per stroke | human |
| Lift time | varies | t_close has **no noise term** (§8.3): isochronous ±5 ms | machine |
| Stroke length | ±25–35 % | master path fixed at 30 mm (r₁ = r₂); windows fixed per phrase | machine |
| Speed, interval | ±20 % | f constant inside a phrase; pure sinusoid; steps at phrase edges | machine |
| Force | ±30–50 % per finger | σ_F 0.1–0.3 per stroke, **common to all pins** | half |
| Direction | ±15–30° random | 4.5° per cycle, smooth, monotonic (2.7–6.3° with the ε walk) | machine |
| Location | 3–6 changes/min | drift plus ledger moves | human (restless, §6) |

Four of seven dimensions are machine-grade. The worst is the one the brain tracks best, **timing**. Landing jitter of 3–11 % of the period is detectable, which is good. But it rides on a crank whose period, reversal points and lift instants are exact. The stroke *ends*, where force drops and hair springs back, are the most salient events, and they form a 2.8 Hz metronome.

### 3.2 The rosette has a pivot

Every PLINE stroke is a line through the master centre, and every window contains s = 0. So **every stroke of every pin crosses that pin's rest point**.
- With the pad parked, that point gets 2.8 passes/s = **168 passes/min**, 3.4× scratch-model §3.24's 50/min rule.
- The heading rotates about a fixed hub: a wiper or a sprinkler, not a hand.
- The pattern is legal only while it roams (§6).

### 3.3 Irregularity at $0

The steppers are open-loop step counters, so the firmware owns θ_A(t) completely. Each of these is free:

1. **Rubato.** Any monotonic time-warp of θ_A, with θ_B = −(1−ε)θ_A, keeps the same line and changes only the speed profile and period.
   - Draw each half-stroke duration from N(1, 0.2).
   - Add 0.2–0.8 s hover pauses at line ends.
   - Let f drift as pink noise *inside* phrases.
   - Gate times stay analytic if the warp is planned one stroke ahead.
2. **Rocking crank.** Oscillate θ_A about mid-line instead of spinning it, and the amplitude becomes 15·sin(A).
   - This gives 10–20 mm rakes at 2.5–3.5 Hz (v_peak = π·f·L ≈ 110–140 mm/s), the human P1 core band and leap-A's "grain".
   - The spec's alternating sets apply above 1.7 Hz.
3. **Heading kicks.** The spec already allows heading jumps during a lift. Make ±10–30° kicks at most end-zone hovers the default texture, with the 4.5° precession as background.
4. **Lift and window jitter.** Lift σ 20–40 ms; per-stroke s_land in [0.45, 0.8] and s_lift in [0.75, 0.9], giving 15–25 mm contacts.

**P(reads as "a machine" by 30 s):** ≈ 0.6 as drafted, ≈ 0.35 with these. This is the largest single lever here.

---

## 4. Attack 4 — Twelve pins at 18 mm on one rigid pad: hand, stamp or comb?

**How many are down, and what they share.** ROW3 or ROW4 puts 3–4 nails down per flank (6–8 for ~20–60 ms at a hand-off). Count and pitch are hand-like. But every down nail has:
- identical velocity (rigid block);
- identical force (one rail);
- identical lift instants.

Per-pin gating spreads only the landings. Leap2-F called this "a stamp moving" (F4, P 0.35) and offered tilting pins and counter-orbiting halves. C4 chose the rigid block, so **F4 is open**. Three or four points at 18 mm are marginal at 15–39 mm acuity, so the "hand" percept rests on exactly the temporal and force pattern that the block and the single rail fix in place.

**The hover comb (new).** The other **8–9 nails hover 5 mm above last touch, inside a 10–25 mm pile**. They move with the block at full speed through every cycle, ungated. Each has a Ø 7 flare at 5–7.5 mm, and 12 Ø 1 shafts stand through the rest of the pile.

Swept root-zone area [EST]:
- biting: 3.5 × ~5 mm × 44 mm × 1.4 Hz ≈ 1,100 mm²/s;
- hovering: 8.5 × 7 mm × 60 mm × 1.4 Hz ≈ 5,000 mm²/s.

Weighted by per-hair moment (2.6 mN at 2 mm vs 0.17 mN at 5 mm; scratch-model §2.3), the hover comb supplies **≈ 30 % of follicle drive**. It is the only part of the stimulus that is 12-fold, perfectly periodic and identical every cycle: the clock, delivered through the channel the model ranks first.

**Ghost fingers.** Idle collars keep "last touch + 5 mm" while the pad drifts 50–150 mm over a curved head.
- Some idle nails drag the skin at the spring/collar force (0.05–0.13 N), ungated.
- Others end up ≥ 10 mm high and land late when their row is called.

**Fixes:**
- **Park every pin outside the active and next row**; schedule rows ≥ 0.5 s ahead (an un-park is a 15–20 mm descent); check the vacuum flow.
- Jitter lifts.
- For per-pin force spread now: a random single 5–10 ms vent "dip" on one pin mid-contact (−20 to −50 % for ~30 ms; not PWM).
- The bore-mix kit gives only a fixed spread, which is learned in a few strokes.

---

## 5. Attack 5 — The omni nail on a 0.38 mm neck

**Edge presentation is not the problem.** The tip is a body of revolution, so the leading rim is the same in every heading. The loaded rim arc is ≈ 3 mm, so 0.3 N gives ≈ 0.1 N/mm, mid-window at R 0.4 (tip-interface §2.5). A Ø 2 punch at 0.3 N sinks ~1.5–2.5 mm, enough for the cone flank to join: ploughing, not pressing.

**The neck is the problem.**
- Spec values: 0.12–0.2 N/mm tangential, 5–15° lean under drag, stability margin 1.5 at the cap.
- Axial load softens the column toward (17 − F·L)/L² ≈ **0.08 N/mm at 0.5 N**.
- Friction of 0.1–0.2 N, fluctuating ±50 % with sebum and clumps, therefore moves the tip ±0.5–1 mm, along **and across** the stroke.
- A real nail edge is rigid (≈ 30 N/mm, tip-interface §1.2); its compliance sits *behind* it, at 0.3–1 N/mm.

**Why it matters.** Crispness is skin-fold stick-slip at 10–100 Hz against a stiff edge (tip-interface §2.6). A ~0.1 N/mm spring in series stores that energy over 0.5–1 mm. It either low-passes it into a glide or turns it into a coarse ~300 Hz chatter (neck plus 0.1 g nail) [UNSURE which].

Under lean, the trailing face is the Ø 2 flat at 5–15° to the skin. Scratch-model §3.11f: "< 20°: … becomes a rub."

Add the ratchet (§1.3) and the result is **a soft-mounted stylus that skates over clumps**.

**Verdict:** major, P 0.35 (spec R10: 0.30).

**Fix ($5, a day):**
- A/B necks: 8 mm free on 0.5 mm wire (lateral stiffness ×4–8, lean 2–4°) against the frozen neck, with D-6 as the control.
- Add "edge or stylus?" to B7 in 8 headings.
- Move the H-4.13 breakaway to the TM1-P clip.

---

## 6. Attack 6 — Travel and drift: real, but servo-stepped and restless

**Stepwise?**
- Drift is genuine servo motion, but its goals arrive at 50 Hz: a 0.5 mm staircase at 25 mm/s.
- Hobby servos at ≤ 18 rpm output commonly cog.
- Without the STS speed/acceleration profile, a 50 Hz ripple rides under the scrub [UNSURE].

**Backlash.**
- Scrub drag of 0.37–0.74 N acting at r ≈ 90 mm from O reverses at 1.4 Hz. That is 0.03–0.07 N·m at the bail, 0.01–0.02 N·m at the α servo.
- The zero-length balancer is designed to cancel gravity, and **a perfectly balanced geared axis has no bias**. The scrub rocks it through its backlash: ~0.5° at the servo [EST] → 0.17° at the bail → ≈ 0.5 mm at the pad.
- With a tight deadband the servo instead buzzes into the parietal bone at every reversal (§7).

**Region-change rate.**
- H-5.5 (≤ 8 strokes per ±15 mm patch; "8" is a placeholder per hair-interaction §9.5) is applied to an 84 × 54 mm contact field.
- A patch fills in ≈ 1.7 s counted per pass, 5.7 s counted per cycle.
- Together with the rosette pivot (§3.2), this forces near-continuous drift (≥ 7–14 mm/s average) or a comb-out every few seconds, which is itself a rhythm.
- A human P1 bout keeps the hand still for 2–8 s and gives 32–200 passes per region. The egg's "stay 6–10 s" cannot be honoured literally.

**Verdict:** major, P 0.4: "it won't stay where I like it."

**Fixes:**
- STS speed/acceleration mode with goals at ≥ 100 Hz.
- **Offset the balancer by ≥ 0.05 N·m at the bail** so the gears never reverse ($0).
- Replace the placeholder 8 with the Stage B wig matting test.
- Count per pin track, not per patch.
- Implement STAY as in-pad row steps plus heading kicks.

---

## 7. Attack 7 — The helmet intrudes

**Lean that changes every few seconds.**
- Spec: 0.03 N·m at the vertex, 0.24 N·m at the bun, CoM wander 85 mm, and the pad changing region every 2–6 s.
- At an assumed 5–15 N·m/rad of helmet pitch stiffness on soft tissue [EST], that is **0.8–2.4° of hat rotation**, 1.4–4 mm of band slide on the forehead (48 units/cm²).
- That is about ±20 % of the ~1 N·m the neck normally carries, above a ~10 % Weber fraction [EST].
- C3 *accepts* 3° of slip. R5 (0.35) is low, because the pattern layer makes the swing continuous.

**Scrub reaction.**
- Scalp drag is an internal force pair between head and helmet. The pads carry 0.4–0.7 N plus a couple of 0.05–0.11 N·m, reversing every stroke.
- At an assumed 10–30 N·m/rad of small-amplitude stiffness [EST] that is 0.2–0.6°, i.e. **0.4–1.1 mm at the band, in time with the scratch**.
- Twin point-mirror lockstep cancels the net force and the pitch/roll couples but **doubles the yaw couple** (r×F about Z adds under R_Z(180°)).

**Air on the head.** §4.8 budgets no pad-side vents, yet the pad carries three kinds:
- **12 × Ø 0.15 pin bleeds.** 115–147 m/s, 1.2–1.6 ml/s each, pulsed with every bite.
- **One Ø 0.3 float bleed.** Continuous, ≈ 6 ml/s, 150 m/s.
- **12 duckbills.** These pass chamber air at each lift and are prone to squeal at low ΔP [UNSURE].

Lighthill scaling (K 3×10⁻⁵–10⁻⁴) gives sound power of ≈ 51 dB per pin bleed and ≈ 58 dB for the float bleed. Both peak ultrasonically (200 and 100 kHz), but the audible tail at 0.10–0.15 m from the ear is roughly **25–38 dB(A)** [EST ±10 dB].
- That is level with the "wanted nail hiss" (30–40 dBA) the spec says must never be masked.
- It fails B8 ("pad-side SPL = room level").
- It sounds like "tss-tss" at the bite rate over a steady "ssss": pneumatic, not fingers.

**Bone-path servo hunting.** The servo pods' inner faces *are* the parietal pads, 64 mm from the canal. A geared position servo holding a load that reverses at 2.8 Hz either rattles or corrects in bursts, rhythmically and locked to the scratch. R6 treats servo noise as a travel issue; it is a **holding** issue.

**Fixes:**
- Sintered or porous-PE mufflers on every pad vent (≈ 0.3 g each, $5–10), or return the bleeds via the spare palm line. Add them to §4.8 and A5/B8.
- Gear bias (§6).
- Counter-mass on the β return run (+30–40 g, inside the 48 g reserve), or an earlier twin.
- C3 pass at ≤ 1°.
- Ask at D2: "did the hat move with the strokes?"

---

## 8. Attack 8 — The 20-minute session

**Dose.**
- At 1.4 Hz, ~70 % play and 3.5 nails: ≈ 8,200 passes, 180 m of track.
- At a 2–3 mm swath that is ≈ 4,500 cm², or **~9 passes per point** over the ~520 cm² reached (~30 where favoured).
- Abrasion binds only second by second (rosette pivots), never at session scale. The session is spread thin where a hand would linger.

**Habituation.** The ledger can change region, mode, f, ε, F, window and rows. It cannot change:
- crank periodicity;
- the hover comb;
- identical velocity and force;
- the hiss;
- the nail itself.

Those stay at h → 1 for 20 minutes. Scratch-model §4.3 gives 10–30 s before a fixed substrate reads as a machine; leap2-D cites satiety over 100–300 s. Expect realism to sag after minute 3–5 **whatever the ledger does**, unless the substrate varies. The ledger's constants are forearm guesses, and its hard counters (H-5.5) will dominate scheduling more than novelty does.

**Operator load.**
- **Hold-to-run.** The user holds a 2.5 N lever for 20 minutes while trying to relax. Each lapse means vent, retract and ≥ 4.5 s of APPROACH.
- **Snag reflex.** Drag > 3× baseline will false-trip against the grain in medium hair, where per-nail spikes to 0.3 N are normal (scratch-model §3.5). Each trip is an all-vent plus a 10 mm retract: **a flinch**. Three in 10 s is a FAULT.
- **Session cap.** "Session > 20 min" is itself a FAULT trip (§8.1).

**Fixes:**
- An **armrest pad closed by the relaxed weight of the forearm** (≈ 4 N available; red line 4 intact).
- Snag criterion: absolute 0.8 N, or 3× baseline sustained ≥ 30 ms. First response: pins to hover.
- A 60 s P2 wind-down before the cap.

---

## 9. The §8 checklist, item by item

| # | Item | Verdict | Reasoning |
|---|---|---|---|
| 1 | Edge, not pad | PASS (marginal) | POM, rim R 0.4, loaded arc ~3 mm (short end of 2–8); the trailing flat at 5–15° is skid-like |
| 2 | Reaches skin ≥ 40 % at ≤ 0.3 N, 5–10 cm hair | UNSURE → leaning FAIL | Restrictor ratchet; 0.09 N net at the 0.15 N setting; nothing measures contact fraction before D1 |
| 3 | Light | PASS | 0.08–0.50 N, 3–4 down ≤ 2 N, cap 0.96 N; the light end is inaccurate, not heavy |
| 4 | Slides ≥ 10 mm with slip | PASS | 15–25 mm per flank; 0.15 N skids cannot move the scalp |
| 5 | 2–20 cm/s, 1–4 Hz, nothing > 20 Hz | PASS / UNSURE | 70–132 mm/s at 1.4 Hz; possible 25 Hz ring, 50 Hz servo staircase, neck chatter |
| 6 | Deflects hair near the root | PASS | Biting cones at 0–2.5 mm; hover beads at 5 mm too, but periodic |
| 7 | ≥ 3 independent contacts, ≥ 20 ms / ≥ 20 % spread | **FAIL as drafted** | Timing spread yes; force spread is common-mode (one rail) or deterministic (curvature); velocity identical; one crank |
| 8 | Irregular in length, speed, force, direction, location | UNSURE | 4 of 7 machine-grade; master stroke kinematically fixed at 30 mm; PASS with the §3.3 firmware |
| 9 | Compliant tip | PASS | Gas spring 0.18–0.34 N/mm for ~1.7 mm, then constant force over 24 mm; fails by drop-out, not spikes |
| 10 | Unloads at reversal, lifts between bouts | PASS | Hover in every end zone; park at region changes |
| 11 | Hair-safe geometry | PASS | Nothing rotates in the zone; hover beads in long hair to be checked at B5 |
| 12 | Sounds like a scratch | UNSURE → likely FAIL | Unbudgeted pad-side hiss; servo bone path under reversing load |

There is no FAIL among items 1–6, where v0 had two. There is a FAIL on item 7, and three UNSUREs that lean the wrong way. The freeze can produce *scratching*. Whether it produces *a person* is the open question.

---

## 10. The bet

**What I am rating.** "First good session" is read as the first full-score session (D4) with nothing broken, judged blind: realism ≥ 7/10 and "machine on my head" ≤ 3/10. D1 (LINE, one spot, 0.15 N, no travel) is the device's worst stimulus by construction. It is a safety ramp and should not be rated.

| Gate | As drafted | After top 3 fixes |
|---|---|---|
| Contact reads as a nail in Michael's hair | 0.60 | 0.70 |
| Motion reads as a person, not clock, stamp or comb (first 60 s) | 0.40 | 0.60 |
| No head-side intrusion dominates (lean, rocking, servo, hiss, lever) | 0.55 | 0.75 |
| Holds from minute 3 to 20 | 0.75 | 0.80 |
| Product | 0.10 | 0.25 |
| **With positive correlation** | **≈ 0.12 (0.08–0.18)** | **≈ 0.28 (0.20–0.36)** |

The top three fixes:
1. **Rubato master plus jitter everywhere.**
2. **Hover hygiene plus force truth:** park idle rows, spring feed-forward, the 0.20 N floor and the curvature rail boost.
3. **Quiet the head:** vent mufflers, gear bias and counter-mass.

With the whole table, including the neck A/B and the armrest lever, the estimate is ≈ 0.35.

**Cross-check against the spec.** The risk register alone implies a ceiling near 0.3: (1 − R10)(1 − R5)(1 − R6) = 0.70 × 0.65 × 0.70 = 0.32.

**Cheapest test, before Stage A ($0; add it to the cue-card evening).**

The helper uses two props:
- a rigid 4-point chopstick rake at 18 mm pitch;
- a 4 × 4 chopstick grid, one row pressed and the rest held 5 mm up in the hair.

Run blind 20 s blocks:
- (a) a 1.4 Hz metronome, constant 30 mm, heading +5° per stroke (the frozen PLINE);
- (b) the same with rubato and ±20° kicks;
- (c) (b) with the grid hovering;
- (d) the helper's own fingers.

Ask two questions each time: "person or machine?" and "fingernails, 0–10".
- If (b) does not clearly beat (a), attack 1 is wrong.
- If (c) does not lose to (b), the hover comb is harmless.

---

## RANKED ATTACK TABLE

| Rank | Attack | Severity | Likelihood | Fix | Cost |
|---|---|---|---|---|---|
| 1 | **Crank clock.** Fixed f, 30 mm line and sinusoid per phrase; isochronous lifts; monotonic precession about a fixed pivot (168 passes/min when parked); 4 of 7 irregularity dimensions machine-grade | fatal to the rating | 0.6 | Rubato time-warp, pink f inside phrases, rocking-crank 10–20 mm rakes at 2.5–3.5 Hz, ±10–30° heading kicks, lift σ 20–40 ms, per-stroke windows | firmware 3–5 days, $0; rubato ink gate in A3 |
| 2 | **Hover comb and ghost fingers.** 8–9 idle nails at 5 mm in the pile, ungated, ≈ 30 % of follicle drive; drifted collars drag the skin or land late | major | 0.5 (hair ≥ 3 cm) | Park pins outside the active and next row; rows scheduled ≥ 0.5 s ahead; hover 8 mm in long hair | firmware 1–2 days, $0–10 |
| 3 | **Restrictor ratchet and light-end parasitics.** Edge rows lose 55–90 % of force on outward flanks (R 90–70); 4–5 mm hops off clumps; 0.15 N commanded → 0.09 N; A4 gate inconsistent | major | 0.5 | Spring feed-forward; net-force A4; 0.20 N floor for D1–D3; per-flank rail boost K·v_n²; inner rows or short strokes where R < 80 | firmware 2 days, bench 1 day, $0–5 |
| 4 | **Head-side air hiss.** Pin and float bleeds plus duckbills, 0.10–0.15 m from the ear, ≈ 25–38 dBA EST, unbudgeted; fails B8 | major | 0.45 | Porous mufflers on every pad vent, or bleeds routed home; add to §4.8, A5, B8 | $5–15, 2 h |
| 5 | **Hat lean and rocking.** 0.03 → 0.24 N·m swing every 2–6 s (0.8–2.4°); scrub couple rocks the band 0.4–1.1 mm per stroke; twin doubles the yaw couple | major | 0.45 | Counter-mass on the β return or early twin; C3 ≤ 1°; slower region moves; D2 question | +30–40 g, $10 |
| 6 | **Balanced geared axes rattle or hunt** under reversing scrub load; ≈ 0.5 mm pad rock; bursts into the parietal bone; 50 Hz goal staircase | major | 0.4 | Balancer offset ≥ 0.05 N·m at the bail; STS profile mode, goals ≥ 100 Hz; tune the deadband on C5 | $0, 1 day |
| 7 | **Stamp.** Common-mode force, identical velocity, simultaneous lifts; §8 item 7 FAIL; leap2-F F4 open | major for "a hand" | 0.4 | Lift jitter; per-pin single-pulse vent dips; bore-mix as A/B only; SP2 tilting pins or second rail | firmware 1 day, $0 |
| 8 | **Restless roaming.** H-5.5 placeholder on an 84 × 54 mm field forces relocation every 1.7–5.7 s; STAY impossible | major | 0.4 | Wig matting test to set the limit; count per pin track; STAY = row steps plus kicks | 1 wig day |
| 9 | **Soft neck.** 0.08–0.2 N/mm, the softest tangential element; 5–15° lean presents a skid; stick-slip smeared or chattering | major | 0.35 | Neck A/B 8 mm × 0.5 mm wire; D-6 control; B7 "edge or stylus?"; breakaway to the clip | $5, 1 day |
| 10 | **Operator load.** 20 min holding a 2.5 N lever; lapses cost ≥ 4.5 s re-approach | minor–major | 0.4 | Forearm-weight armrest hold-to-run | $5, 2 h |
| 11 | **Snag-reflex flinches** in medium hair; 3 in 10 s = FAULT; 20-min cap is a FAULT | minor–major | 0.3 | Absolute or sustained criterion; first response hover; 60 s wind-down | firmware 0.5 day |
| 12 | **Substrate habituation.** Ledger cannot vary crank, comb, hiss, nail or common force; sag after minute 3–5 | major (late) | 0.5 conditional | Fixes 1, 2, 4, 7; D5 ledger on/off with a minute 3–6 slope | $0 |
| 13 | **Synchro 25 Hz ring** at synchronous landings (ζ ≈ 0.3) | minor | 0.25 | σ_t ≥ 20 ms; Ø 0.8 damping orifice at the slaves; accelerometer in A3 | $2, 1 h |
| 14 | **Synchro stroke shrink, "rubbery"** | not an attack | — | none: 2 % of stroke, below acuity; the neck is 5–8× softer | — |
| 15 | **Omni-nail edge by heading** | not an attack | — | none: axisymmetric, mid-window at 0.3 N | — |
