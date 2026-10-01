# Tournament Judge 3 — Experimental-Value & Product Lens

**Project SCRATCH · 03-tournament · 2026-10-01**
**Read:** 00-brief/BRIEF.md; all six 01-foundations files including prior-art.md; team-A through team-G in full.
**Lens:** SP1 is a research rig. Its job is to answer "can automated fingernail scratching feel excellent, and which variables matter?" as fast and cleanly as possible. I score each candidate on information yield per dollar and per build-hour, on which variables it can sweep without a rebuild, on whether it can run the periodic-vs-jittered control, on whether it can host instrumentation, on how fast it can be rebuilt after a lesson, on whether its results transfer to a full-coverage product, and on whether Michael will actually finish and use it.

---

## 0. Three cross-cutting findings before any scores

**1. The seven teams converged on the contact, so the tournament is really about three things.** Every candidate carries 3 (or 4) SP1-TM1 nail blades at ~20 mm pitch on independent springs at 45°, with lift-off at every reversal. What differs is (a) mount, (b) how the stroke is generated and how many of its parameters are programmable, (c) how force is set, capped and *measured*. I weight those three heavily.

**2. Head-worn rigs cannot run the force experiment cleanly.** Every head-worn candidate (A, B, C, F, G) sets normal force as spring-rate × (geometric depth relative to the headband). The teams' own numbers put ratchet-suspension seating slop at about ±3 mm (A §2d, C §2d). At 0.15–0.4 N/mm that is ±0.45–1.2 N of per-nail force uncertainty — equal to or larger than the entire 0.05–0.6 N window that scratch-model §9 Q3 (the force–pleasure curve) must sweep. Only D (dead weight over a 20 mm constant-force float, logged by a load cell in the force path) and E (torque-controlled axis) make force independent of head position. G partially mitigates with a contact-detect zero at session start; no head-worn design has an in-session readout except A's optional FSR and F's visual pointer. For the #3-ranked sensation variable, this is decisive.

**3. Everyone claims the periodic control; only F produces it faithfully.** A fixed-kinematics machine (F, and A in "metronome" mode) is the honest "fully periodic" condition that scratch-model §7 rank 1 demands; a servo rig with jitter switched off still carries micro-stepping and trajectory-generator artifacts. F's $85 module is therefore worth building regardless of the winner: it is the control instrument, it validates the tip family under real stroke kinematics in a weekend, and it measures the predictability penalty every other team's firmware is guessing at (F §4 makes this argument and it is correct).

---

## 1. Experimental-capability matrix (the judge-3 lens)

| | A FEED-DOG | B Pendulum Hand | C LEAFHAND | D CRADLE | E LH-1 | F WR-1 | G ARC-RAKE |
|---|---|---|---|---|---|---|---|
| Force without rebuild | depth screw (coupled to chord), no readout | lift setpoint + preload cap, weak readout | lift screw + servo, Bowden hysteresis ±30% | slugs 20 g steps + trim spring + tendon unload; **load cell readout** | firmware setpoint 0.05–0.6 N, inferred readout (±8%/20 °C) | dip screw (coupled to chord), pointer scale | depth setpoint × k, contact-detect zero, current readout |
| Velocity (mm/s) / frequency (Hz) | 25–180 / 1.2–2 | 20–200 / 0.5–2.5 | 70–130 / 1–1.5 (one pass per cycle) | 20–200 / 1–2.5 | 20–200 / 1–3.5 | 57–184 ±40% jitter / 0.5–1.6 | 20–200 / 1–3.5 |
| Stroke length (mm) | pin swap 22–30 | firmware 10–46 | lift-coupled 22–42; 55 in 2-DOF | firmware 15–140 | firmware 10–90 | eccentric swap 16–35 | firmware 5–52 |
| Attack angle | holder reprint ± rod tilt | sleeve reprint; swings 63→27° in-stroke | stalk reprint | holder reprint; constant along stroke | holder reprint; ±14° wander | finger reprint | paddle bend; ±5° |
| Contact count | 1–3 | 1–4, independent | 1–4 | 1–3 | 1–3 | 1–3 | 1–3 |
| Per-finger phase (Q4) | passive only | **driven, 0–60 ms + LOCKED_PHASE** | passive | passive | passive | passive ~10–15 ms | passive |
| Pattern irregularity dims | time only | length, speed, phase, wander, pauses | speed, depth, pause, amplitude | length, speed, force, start, pause | length, speed, force, direction bias, pause, lift, **compliance** | speed, pause | length, speed, depth, start-x, pause |
| Periodic control | yes (true fixed path) | yes (flag) | yes (flag) | yes (flag) | yes (flag) | **yes (true fixed path)** | yes (flag) |
| Instrumentation hosting | FSR optional, INA219 | servo current | servo current via Bowden | **1 kg load cell in path**, current, wrist switch | torque/position inference, lag, contact fraction | Hall period, pointer | current, FSR at calibration |
| Rebuild after a lesson | pin/hanger reprint + re-balance; 8 pivots | 4× every finger part; firmware | one JLC order of passive parts; Bowden retune | hand on magnets; palm 20-min reprint; twin palm +3 h | holder/rake reprints; firmware | eccentric 8 g / finger 10 g, minutes | carrier/paddle reprints; firmware |
| Build hours / cost | 26–32 h / $270 | ~30 h / $400 | 24–32 h / $340 | ~30 h / $470–535 | 28–36 h / $390 | **12 h / $85–148** | 30–38 h / $290 |
| Product transfer | module plausible; one-patch | independent-finger hand is product-shaping | tendon hand is the most wearable-product-like | yoke is pure instrument; hand + findings transfer | rig is pure instrument; specs transfer | **module is the most product-like** | 2-servo arm module plausible |
| P(Michael finishes and keeps using it) | low–med | medium | medium | **med–high** (bolt-together; posture is the risk) | **low** (FOC skill gate) | **high** | medium (IK firmware) |

---

## 2. Scoring table (common rubric, 1–10, weights in brackets)

| # | Criterion (w) | A | B | C | D | E | F | G |
|---|---|---|---|---|---|---|---|---|
| 1 | Scratch realism (5) | 6 | 7 | 6 | 7 | 8 | 5 | 7 |
| 2 | Contact across curvature / head motion (3) | 6 | 7 | 5 | 8 | 8 | 6 | 7 |
| 3 | Hair safety (4) | 7 | 7 | 8 | 8 | 8 | 7 | 8 |
| 4 | Force controllability + mechanical cap (3) | 5 | 6 | 4 | 9 | 8 | 5 | 6 |
| 5 | Simplicity / parts count (2) | 5 | 3 | 5 | 4 | 6 | 8 | 6 |
| 6 | Apartment buildability (4) | 5 | 5 | 5 | 6 | 4 | 9 | 5 |
| 7 | Availability and cost (2) | 6 | 5 | 6 | 4 | 5 | 10 | 7 |
| 8 | Noise (2) | 4 | 4 | 9 | 7 | 9 | 4 | 5 |
| 9 | Reliability 20 min / weeks (2) | 5 | 5 | 5 | 8 | 6 | 6 | 6 |
| 10 | Adjustability as research rig (3) | 5 | 8 | 5 | 8 | 9 | 5 | 7 |
| 11 | Ease of iteration (2) | 5 | 6 | 5 | 7 | 8 | 7 | 7 |
| 12 | Coverage / region change (1) | 3 | 5 | 4 | 7 | 5 | 5 | 5 |
| 13 | Failure modes, fail-safe, red lines (3) | 5 | 7 | 8 | 7 | 8 | 7 | 6 |
| 14 | P(works first time) (3) | 5 | 5 | 5 | 7 | 4 | 8 | 5 |
| | **Weighted total (max 390)** | **209** | **233** | **227** | **275** | **272** | **257** | **247** |
| | **Rank** | 7 | 5 | 6 | **1** | **2** | **3** | 4 |

### Justifications (one line per cell, grouped by criterion)

**1 Realism.** A: good single stroke (27 mm chord, 18 mm lift) but one patch with time-jitter only; 25° plough-in firmer than a finger. B: four driven fingers give the only true asynchrony, but the 63→27° attack swing and shared-lift force variation are unmodelled confounds. C: one 33 mm pass per cycle at ≤1.5 Hz through a hysteretic cable; silent head helps. D: constant attack angle along a great-circle sweep, dead-weight force, 15–140 mm strokes; one-direction unless twin-palm. E: force-rendered, silent, bidirectional with lift, full pattern spec; rigid rake, possible cogging grain. F: bell-shaped force from geometry, but 23% contact duty, one pass per cycle and phase-locked fingers risk "flicks". G: full pattern spec with sphere tracking and passive lift backup; rigid rake, plastic-gear servos 10 cm from the ear.

**2 Contact quality.** A/F: 8 mm leaves ride on the head, but force and chord drift with seating. B: 10 mm plungers plus per-region lift feed-forward, a tuning burden. C: 7 mm leaves on TPU straps that wobble ±1–2 mm; headgear lifts under reaction. D: the sweep *is* the curvature; 20 mm constant-force float. E: ±15 mm normal / ±10 mm tangential by force control; cheap arm may bounce. G: IK tracking with <1 mm residual; band rocking under 1 N is their own risk 3.

**3 Hair safety (self-scores audited in §5).** A: rotation boxed at ≥44 mm, but the TM1 seam sits inside the pile (item 3 should be 1). B: four guard windows and an upward-facing sleeve seam at 45 mm, inside 8 cm hair reach. C: nothing rotates on the head; sleeved seams. D: zone holds only tips/stems; seams sleeved at 28 mm. E: zone empty, but rotating bells at 130 mm are within 11 cm hair reach; 10 ms reflex. F: eccentric at 50 mm above an open floor window — needs the wrap test. G: 34/36 largely earned.

**4 Force.** A/F: one screw sets both force and chord; no in-session readout. B: lift setpoint through a 2:1 lever on a plastic-gear servo; current→force ±30%. C: Bowden hysteresis equals the experimental resolution; worst case relies on the headgear lifting, unmeasured. D: dead weight is the cleanest cap and the only direct force log. E: force is the command; stall torque is a physics cap; voltage-mode drift, cogging ±0.02–0.03 N. G: depth × k with contact-detect zero; drifts with band seating.

**5 Simplicity.** F one motor, five printed parts; E two motors and a rod; G two servos and a link; A eight pivots and a counterweighted crank; C a passive hand plus two Bowdens; D a cage, yoke, float, load cell; B five servos, four sleeve/post assemblies, hinge, solenoid.

**6 Buildability.** F: 12 h, 80-line firmware, usable as a wand before the band exists. D: bolt-together 2020 with one ±1 mm alignment; 6 h position-mode firmware; needs desk space. A/B/C/G: 24–38 h each with a known cliff (A velocity loop + pin rattle; B lift feed-forward + solenoid; C Bowden + TPU straps; G 2R IK, 10–14 h firmware). E: SimpleFOC bring-up, Kt measurement, two-axis impedance tuning — the highest skill gate for a first-time builder.

**7 Availability/cost.** F $85–148 all Amazon; G $290; A $270 (one unverified Pololu SKU); C $340; E $390 (gimbal motors and SimpleFOC Minis are available but niche); B $400; D $470–535.

**8 Noise.** C and E are silent at the head; D has metal-gear servos on the frame in muffs with an isolated forehead bar; G two plastic-gear servos on the head; A/F a gearmotor 60–70 mm from the ears; B five servos bone-conducting through the skull.

**9 Reliability.** D: extrusion and bearings. F/G: PETG flexure/paddle fatigue is a stated risk. E: heating above 0.6 N, thermal drift. A/B/C: TPU creep, plastic gears, detent drift, Bowden wear.

**10 Research adjustability.** E exposes compliance, lift height, bidirectionality and the full pattern spec as firmware. B exposes per-finger phase (unique) and most pattern dimensions. D exposes stroke 15–140 mm, force with readout, start position, Mode 0. G exposes length, depth, speed, start-x. A/C/F jitter time (and depth for C) only.

**11 Iteration.** E and G: mostly firmware plus cheap reprints. D: hand swaps on magnets, 20-minute palm reprints. F: minutes per eccentric/finger swap, but the kinematic family is fixed. B: four of everything. A: linkage changes need re-balance. C: every change retunes the cable.

**12 Coverage.** D: a 40 × 250 mm band in three lanes; the rest one patch with manual re-seating; F's wand mode reaches anywhere by hand.

**13 Fail-safe / red lines.** C and E lift on power loss by construction; B via a solenoid latch (a binding failure mode); D and F are "limp" or pedal-lifted, D with an $8 electromagnet option; G's lift depends on an unmeasured back-drive torque; A's stopped crank is not a lifted crank (red lines 7/8 partial, honestly flagged).

**14 P(works first time).** F highest (one motor, printed path). D next (known servo mode, dead weight, bolt-together). A/B/C/G each carry one integration cliff. E lowest: FOC tuning, cogging and heat are three independent ways to end up with a humming hand that does not scratch.

---

## 3. Rulings on the three decision axes

### (a) Head-worn vs frame/arm-mounted for SP1 — **frame-mounted.**

Reasoning from the experiment, not the product. The highest-value unknowns (scratch-model §7 ranks 1–4: irregularity, penetration, force, velocity) require force to be a repeatable independent variable with a readout. Head-worn designs couple force to headband seating at ±0.5–1.2 N per nail (§0.2), have no room for a load cell in the force path, put the motor within 10 cm of the ear (sound is scratch-model component D and a confound), and cap head-borne mass at 500 g, which forced B to a solenoid latch and G to an unmeasured back-drive assumption. A frame makes mass free, hosts the load cell, isolates noise, and makes "withdraw the head" the release (safety §5 principle 5). The cost is posture and head stillness for 20 minutes, and the frame itself does not transfer to a product — but everything measured on it does. Two caveats: (i) the first scalp contact should be hand-positioned (the TM1 wand, D's Mode 0, or F's wand mode), because a hand supplies free irregularity and lets the tip family be validated before any mount exists; (ii) a head-worn SP2 is the right follow-on once the force band and pattern are known, and C's motor-free tendon hand is the best-placed candidate for it.

### (b) Single-motor geometric path vs 2-DOF programmable servo arm vs force-controlled direct drive — **2-DOF programmable with a mechanical force constant downstream; direct drive as the one-axis upgrade; the single-motor path as the control instrument.**

A single-motor closed path (A, F) freezes stroke length, direction and location — three of the top nine variables — and can only jitter time. It cannot run Q4 or most of Q5, so as the *only* rig it is a dead end for the pattern question, which is rank 1. It is, however, the cheapest and most faithful periodic control, and F's version is a weekend. A 2-DOF programmable arm (B, D, G) makes length, speed, start position, pauses and lift firmware variables while leaving force to a spring or a dead weight; D additionally reaches P2 sweeps nobody else can. Force-controlled direct drive (E) has the highest ceiling — compliance becomes a knob and the drive is silent — but its unique contribution (compliance, rank 7) is lower-ranked than what it costs in P(works), and its force readout is inferred rather than measured. Ruling: build the 2-DOF arm with a dead-weight or spring cap; put one gimbal motor on the sweep pivot in SP2 (D's own Stack-C suggestion) or an E3 voice coil on the normal axis if cogging or sound become the question.

### (c) Passive spring/dead-weight force cap vs active impedance — **both, with the passive element bounding and the active element only modulating.**

The safety track is explicit that a torque limit does not count as the cap. E's argument that stall torque at 12 V is physics, not firmware, is correct in spirit and the Safety Gate should rule on it, but a cap that moves 8% per 20 °C of winding temperature is not a constant in the experimental sense either. D's pattern — dead weight sets F_max, a tendon can only *reduce* force, a load cell reports what actually happened — is the best structure in the tournament: force jitter can never exceed the dead weight, and the number logged is measured rather than commanded. The hybrid in §7 keeps that structure and adds E's impedance law as an SP2 overlay on a back-drivable sweep axis, not on the normal axis.

---

## 4. The strongest idea in each candidate, worth carrying regardless of rank

- **A — phase-aware speed modulation.** A $4 AS5600 on a crank converts any fixed path into per-stroke drag/return speed jitter, pauses at the lifted phase and a metronome mode. It should be added to F's module. Also A's W1: a dead-weight comb bar the user moves his own head under — the correct first scalp contact.
- **B — per-finger driven sweep under a shared lift.** The only way to run scratch-model Q4 (locked vs jittered phase) as a controlled variable; also the LOCKED_PHASE flag that turns four fingers into a rigid rake for comparison. B notes the module is mount-agnostic (VESA adapter) — it can hang from D's crossbar in SP2.
- **C — actuators that can only pull, springs that only lift.** A runaway pulls the hand to its arc end with nails in the air; power loss parks it lifted; nothing electrical or rotating on the head. Also C's sliding leaf clamp (continuous 0.19–0.63 N/mm without a part swap) and the symmetric-wedge tip W for bidirectional strokes without a second lift.
- **D — dead weight + load cell in the force path, on a yoke about the head centre.** Force becomes a measured mechanical constant; attack angle and radius are constant along a 250 mm arc; Mode 0 (CAT-POST) answers Q1 before any motor turns; the forehead pad is a hardware dead-man. W1 Resting Hand is the best SP2 hand concept in the project.
- **E — compliance as a firmware variable, and silence.** Only E can sweep tip stiffness 0.05–1 N/mm without a part swap, and only E removes motor sound entirely so the sound confound (Q9) can be isolated. Its Kt-measurement-as-day-1-gate and its honest heat budget are the model for how to treat actuator numbers.
- **F — wand mode as the first mount.** A motorized, lift-every-reversal stroke on Michael's scalp in a weekend for $85; the true periodic control; the bell-shaped force profile from ellipse-plus-convexity; and the W1 air-jet for isolating component A (near-root hair deflection without contact) at zero hair risk.
- **G — non-concentric-arc passive lift as a backup to commanded lift.** An IK bug or a dead shoulder cannot produce a loaded reversal because over-swing lifts the tip geometrically. Also the "Concept 1 is day 1" incremental path and the finger paddle as a tangential flexure that reduces bite under a snag.

---

## 5. Self-scores I believe are inflated

- **A:** hair item 3 scored 2 while the TM1 seam sits at 8–26 mm *inside* the pile with a "1 mm overlapping skirt" that is a claim, not a drawing — should be 1. "26–32 hands-on hours" is light for eight pivots, a counterweighted crank, an offset L-hanger and an 8–12 h velocity-loop firmware item the team itself flags as "most likely to slip".
- **B:** hair item 3 scored 2 by placing the pocket seam at 26 mm, one millimetre outside the 25 mm band — boundary gaming; item 13 scored 2 for a manually logged orientation. The ≈450 g mass carries an "~unverified" 140 g headgear and five servos; with cables, guard magnets and the solenoid it will plausibly cross 500 g (red line 10), which the team's own fallback (drop to three fingers) concedes.
- **C:** "12/12 PASS" on the massager checklist is the most generous in the field — item 7 (20–40 ms passive stagger) and item 8 (no direction wander, one pass per cycle, 1–1.5 Hz) should be UNSURE. Red line 2 is claimed as "pass" while the worst-case stack goes 1.5 mm past the leaf stop and the backstop is "the headgear lifts off at an estimated 3–6 N — to be measured"; a gating cap that depends on strap grip is not yet a mechanical constant.
- **D:** hair item 13 scored 2 for a manual remount with a stored map — generous. Honest elsewhere, including the highest cost and the "limp, not lifted" red-line-8 admission.
- **E:** red line 2 "pass" via stall torque needs a Safety Gate ruling (safety §3.2: servo/actuator limits are a secondary layer). The 4–6 h FOC bring-up estimate is optimistic for a first-timer; SimpleFOC community threads describe closed-loop smooth motion as "routine" for people who already do it.
- **F:** hair item 1 scored 2 while the eccentric sits at 50 mm above an open floor window through which the lift-frame columns pass; 8 cm hair stood up by the fingers can reach it, and the wrap test (hair §7.3.4) must be run before this is a 2. Massager item 8 "PASS with caveat" is really UNSURE by the team's own definition (fixed stroke/direction is the control condition). Otherwise the most honest file in the tournament.
- **G:** red lines 7/8 ticked "✓ (to verify)" on an unmeasured XL330 back-drive torque — a gating item claimed with a caveat; the 0.65 P(works) in the selection table is optimistic for a 2R IK with a sphere model and 10–14 h of firmware on a first build.

---

## 6. Top two

### 1. D — CRADLE (275)

CRADLE wins the experimental lens because it is the only candidate in which the three highest-value independent variables — force, velocity, stroke/pattern — are all repeatable *and* one of them is measured. The dead weight makes force a mechanical constant independent of head position; the load cell turns the force–pleasure curve (Q3) from ratings-versus-setpoint into ratings-versus-measured-newtons, and gives contact fraction (Q8) and snag events as data. The yoke about the head centre gives constant attack angle and radius over a 250 mm arc, so it alone can run P2 sweeps against P1 rakes, and Mode 0 answers Q1 before any motor is powered. Fabrication is the lowest-risk of the frame designs (2020 extrusion, two 608 bearings, one ±1 mm alignment) and the firmware is position-mode servo control plus logging, so P(works) is high for a builder without controls experience. It is the most expensive candidate, but it buys the most information per build-hour of anything here, and the hand module, float and all findings transfer to any later carriage or wearable. **The single biggest reason it could still be wrong:** posture. Twenty minutes with the forehead on a bar inside a desk cage may be tolerable on a massage table and intolerable as a relaxation experiment; if Michael stops using it after three sessions, its yield is zero. Close second: the one-direction sweep may read as "sweeping" rather than "scratching" (D's own risk 2), which is why the twin-palm module belongs before the first machine session, not after.

### 2. E — LH-1 Listening Hand (272)

LH-1 is the rig with the highest ceiling: everything the sensation model lists is a firmware knob, including the one variable no one else can sweep (tip compliance), it is silent so the sound confound can be isolated, it runs bidirectional rakes at 1–3.5 Hz with lift at every reversal, and it logs force, lag and contact fraction. If it works, it is a haptic rendering instrument for the scalp and would generate the specification a product needs. It ranks second rather than first only on expectation: its P(works first time) is the lowest in the field. **The single biggest reason it could still be wrong:** the SimpleFOC skill gate. A first-time builder can spend the entire budget of evenings on pole-pair detection, encoder direction, PID tuning, anticogging and thermal drift and arrive at a hand that hums at 0.3 N and heats at 0.75 N without ever running a sensation session. E's own numbers (2.6 W in a 60 g can at 0.75 N; ±0.02–0.03 N cogging on a 0.25 N stroke) say the vigorous end of the force band is where this design is weakest, and that is also where the itch literature puts "satisfying scratch".

### Honourable mention: F — WR-1 (257)

F is not the best rig, but it is the best *first* rig, and it should be built in week one whichever architecture wins: $85, twelve hours, one motor, a true periodic control, and a wand mode that puts a lift-every-reversal nail stroke on Michael's scalp before any mount exists. It is also the most product-like module in the field. Its result — "does a single excellent fixed stroke with time-jitter feel like a person, and for how long?" — is the number every other team's firmware is assuming.

---

## 7. Proposed hybrid — "CRADLE-X" (D's rig, F's instrument, with parts from C, E and G)

I believe a combination beats all seven as a research rig. Subsystem by subsystem:

| Subsystem | From | Why |
|---|---|---|
| Frame, yoke about the head centre, pivots, counterweight, forehead dead-man pad, hard-stop ring | **D** | constant attack angle and radius; 15–140 mm strokes; head withdrawal = release; load cell hosting |
| Normal-force path: parallelogram float, dead weight (0–140 g slugs), 1 kg load cell, tendon that can only lift | **D** | measured mechanical constant; jitter can never exceed the dead weight |
| Fail-safe lift | **D's $8 electromagnet "strict option" as standard**, applying **C's** principle (de-energised = lifted) | closes red line 8 outright instead of "limp" |
| Hand: 3 TM1 blades at 20 mm on steel leaves with **C's sliding clamp** (continuous 0.19–0.63 N/mm) and **G's finger paddles** as tangential flexures | C, G | compliance becomes a 1-minute setting; snag reduces bite |
| Bidirectional P1 from day one | **D's twin-palm** (+$15, +3 h) or **C's symmetric-wedge tip W** | retires D's risk 2 before the first machine session |
| Pattern engine | **G/B/E's** PATTERN SPEC v1 implementation with a PERIODIC flag, plus **A's** time-jitter table | full rank-1 variable coverage minus per-finger phase |
| Sweep drive | XL430 (D) for SP1; **E's GM3506 + SimpleFOC Mini at the pivot** as the SP2 upgrade (D already proposes it) | silent, back-drivable, impedance on the one axis where it is safe |
| Day-0 instruments built in parallel | **F's WR-1 in wand mode** ($85) with **A's AS5600 phase modulation** added; **D's Mode 0** as the first scalp contact; **F's W1 air-jet** as a one-evening component-A probe | tip validation, periodic control, predictability penalty and Q1 answered before the yoke is finished |
| Per-finger asynchrony (Q4) | deferred to SP2: **B's** four-finger module hung from D's crossbar via its VESA adapter, or **D's W1 Resting Hand** | the one variable the hybrid cannot sweep in SP1; cheap to add on the same frame |

Cost ≈ $470 (Feetech variant) + $85–115 (WR-1) + $25 (electromagnet, twin palm, clamp) ≈ **$600**; hours ≈ 30 + 12. Every scratch-model §9 question except Q4 and Q13 becomes runnable in SP1 with a measured force axis, a true periodic control, and a silent-drive upgrade path. The frame does not transfer to a product; the hand, the force-path pattern (constant cap + reduce-only modulation + sensor), the tip results, the force/speed/stroke bands and the pattern engine all do, and F's module remains the candidate product building block. Build order: week 1 the wand, WR-1 and Mode 0 (first scalp contact, periodic-vs-jittered, tip forced-choice); weeks 2–3 the yoke, twin palm, electromagnet, pattern engine and logging; week 4+ the force × velocity × stroke matrix, then choose SP2 (B's fingers on the crossbar, E's gimbal at the pivot, or C's tendon hand on a head).
