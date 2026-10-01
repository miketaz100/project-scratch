# PROJECT SCRATCH — Simplicity / Value-Engineering Review and Hybrid Architecture

**Role:** Simplicity & Value Engineer, Hybrid Architect (not a scoring judge). **Date:** 2026-10-01.
**Inputs:** BRIEF.md (§13–16 governing), all six foundations, JUDGE-BRIEF.md, DIRECTOR-LOG.md, team-A…G in full. Firewall lifted.
**Tags:** [FOUND] foundation document · [TEAM-x] from team x · [EST] my estimate · [TEST] only the bench/scalp decides.

---

## 0. The one-paragraph read

Seven firewalled teams, seeded with different physics, independently arrived at the same scalp-side object: three nail blades at ~20 mm pitch, each on a soft steel leaf with a hard stop, moved as one rigid group along a 25–50 mm chord at 50–150 mm/s, lifted clear before every reversal, with all rotation above a smooth guard. That object is now a high-confidence design element and is not where SP1's risk lives. The teams diverged only on *what moves the hand* and *what the hand is attached to*, and that is one real trade-off — how much of the rank-1 sensation variable (pattern irregularity) to buy with motors versus borrow from the user's own head — plus some taste. The hybrid takes Team G's two-servo planar arm as the mover (it strictly contains the one-servo swing-rake as a week-1 subset), the G/C leaf hand, Team F's dip-stage dead-man and wand/headband dual mount, Team B's solenoid-latched fail-safe lift and pattern engine, Team D's bench instrumentation, and Team E's force-readback idea in its cheapest surrogate (XL330 current + one FSR). It costs ≈ $310 to build, ≈ $400 with test gear, ≈ 40 hands-on hours, and nothing in it is built before the Day-0 hand wand has shown it matters.

---

## 1. Convergence and divergence

### 1.1 Where all seven converged (now high-confidence)

| # | Shared decision | Who | Note |
|---|---|---|---|
| C1 | **Tip = SP1-TM1 pocket, tip A/B geometry (press-on nail or 1 mm PETG/nylon blade, 12 mm wide, edge R 0.3–0.6 mm) at 45°**; tip B (0.5–0.6 mm) for first scalp sessions because of the safety-vs-tip-interface radius conflict | 7/7 | Every team adopted TM1 unmodified and flagged the 0.3 vs 0.4 mm conflict identically. The tip subsystem is done. |
| C2 | **Three contacts at 20 mm pitch on one rigid carrier** (B: four at 22 mm) | 6/7 | H-5.6 forbids relative motion in the canopy, so "independent fingers" collapsed to "independent compliance" everywhere. |
| C3 | **Per-nail normal compliance 0.15–0.4 N/mm, 7–10 mm travel, hard stop → F_max 1.5–2.4 N per nail** | 7/7 | Steel leaf (A, C, D, E, G), printed flexure (F), coil spring (B). Steel leaf is the majority and the only one without creep. |
| C4 | **Force bounded by a mechanical constant; actuator torque irrelevant**; intensity = depth/standoff (A, F screw; B, C, G servo setpoint) or dead weight (D) | 7/7 | Nobody credits a current limit as the cap. |
| C5 | **Lift-off at every reversal; default primitive = unidirectional rake with lifted air return** | 7/7 | Nobody reciprocates in contact. A, C, F, G lift by geometry (ellipse / non-concentric arc); B, D, E command it; G and C do both. |
| C6 | **All rotation ≥ 44 mm (A) to 130 mm (E) above scalp behind a smooth drafted guard; only blades, stems and lower leaves in the hair** | 7/7 | Same exclusion inventory in every file. |
| C7 | **TM1 pocket seam sleeved** (TPU collar / heat-shrink / silicone band) as the one trap-band gap | 7/7 | Same weakest gap, same fix. |
| C8 | **Magnetic breakaways at two levels**: TM1 tip (4–8 N axial) plus a hand- or knuckle-level detent | 6/7 | Only E relies on actuator saturation instead. |
| C9 | **Hair checklist item 7 (≤ 0.15 N tangential yield) scored 1 by every team** and argued incompatible with 0.3–0.5 N of scratch drag | 7/7 | A real finding: the number is unachievable at element level with any rigid carrier. The Safety Gate should accept 0.4–0.8 N at the hand, judged by the 15 g / 50 g tether test. |
| C10 | **Coverage = one ~40 mm-wide patch, 25–55 mm long, at occiput / rear crown; region change manual** (D: 250 mm band) | 7/7 | BRIEF §15 taken at its word; sides, nape, temples out of SP1. |
| C11 | **PATTERN SPEC v1 in firmware with a PERIODIC control condition** | 7/7 | A/F: time-domain jitter only. The control condition is the one experiment every team wants. |
| C12 | **Certified ≤ 12 V brick → fuse → NC e-stop → foot-pedal hold-to-run → actuator rail; logic separate; INA219 watchdog** | 7/7 | Safety §4 verbatim. |
| C13 | **Long (> 15 cm) and curly/coily hair out of scope** | 7/7 | |
| C14 | **Hand wand / passive hand first** (A-W1, B step 2, C step 1, D mode 0, F wand mode) | 5/7 | Tip-interface T0 independently re-proposed five times. |
| C15 | **Noise UNSURE (§8 item 12) for every design; real-hair mannequin as bench target; press-on nails as day-1 tips** | 7/7 | Same gaps, same test gear. |

### 1.2 Where they diverged

| # | Divergence | Positions | Real trade-off or taste? |
|---|---|---|---|
| D1 | **Head-worn vs frame-mounted** | Head: A, B, C, F, G. Frame: D (lean-in cage), E (monitor arm) | **Real.** A geometric force cap needs the hand registered to the skull: a ratchet suspension gives ±3 mm [TEAM-A/C/F EST]; a seated head under a frame wanders ±10–20 mm [TEAM-D/E/G EST], forcing force control (E) or a dead-weight float (D) plus a forehead cradle that makes a 20-minute session un-relaxing (D weakness 4). Frame wins on mass, noise distance, instrumentation and "withdraw-head" release. |
| D2 | **Motor count and where irregularity comes from** | 1 motor geometric (A, F) · 2-DOF arm (G; C via tendons; D yoke+lift) · 4+1 fingers (B) · direct-drive impedance (E) | **Real, and central.** Scratch-model §7 ranks irregularity first *because its uncertainty is 5*: nobody knows whether a fixed stroke goes dead in 10 s or 10 min. One-motor rigs jitter time only; the 2-DOF arm adds length, location, depth, landing; B adds per-finger phase (largely redundant: compliance already gives 20–60 ms and H-5.6 forbids using it in contact); E adds force fidelity and readout. Resolved by staging (§4), not by guessing. |
| D3 | **Motor on vs off the head** | On: A, B, F, G. Tendon: C. Frame: D, E | **Real, second-order.** Tendons cost ±30 % force hysteresis [TEAM-E EST] and strap wobble [TEAM-C]; on-head XL330s cost noise 75–105 mm from the ear [TEAM-G] and ~36 g. Measured, not argued. |
| D4 | **Direct-drive FOC vs geared servo** | E alone | **Real.** E's own numbers: resolution and bandwidth are fine; heat (2.6 W at 0.75 N) and the FOC skill gate are not. Since the leaf already supplies compliance and cap, FOC's unique gifts are readout and silence, both of which have cheaper surrogates. |
| D5 | **Bidirectional rake vs unidirectional with air return** | Uni: A, C, D, F. Both: B, E, G | **Open question.** D risk 2 and C's symmetric-wedge tip agree: the wand decides it in 40 s. |
| D6 | **Fail-safe lift on power loss** | Solenoid latch (B) · tendon springs (C) · bias spring needing servo back-drive (G) · counterbalance (E) · pedal dip stage (F) · "limp" (A, D) | **Real (red line 8).** Only B and F are independent of servo back-drivability. |
| D7 | **Instrumentation** | Load cell in path (D) · servo current (B, E, G) · pointer (F) · none (A, C) | **Real for a research rig.** D is right that force must be logged; wrong that it must ride on the head. |
| D8 | 3 vs 4 contacts; 20 vs 22 mm; leaf vs flexure vs coil; shroud vs plate; OpenRB vs ESP32 vs Pico | various | **Taste or settled**: 3 × 20 (tip-interface §6), steel leaf, plate guard, OpenRB-150 for Dynamixel. |

---

## 2. Could a radically simpler mechanism win?

### 2.1 The strongest case

The north star is sensation. The foundations rank its carriers: **A** near-root canopy sweep and **B** edge-on-skin plough-and-release first and second; **C** irregular multi-point rhythm third [FOUND scratch-model §1.3]. A and B are *per-stroke physics* — a 0.3 mm edge, 0.3–0.9 N on a 6 mm line, 45°, 50–150 mm/s, 25–40 mm of slip, lift at the end [FOUND tip-interface §2.5]. All seven mechanisms produce A and B equally because all seven move the *same* TM1 hand on the *same* leaves; they differ only in C. Team F's §4 argument is correct as far as it goes: if the predictability penalty acts in minutes, an $85 one-motor rig with speed jitter, pauses and the user's own head micro-motion matches a $400 servo hand on the north star at a fifth of the cost.

Three foundation facts push further — the simplest rig is *more* informative than the complex ones in week 1:

1. **The human reference does not exist.** Scratch-model §9.13 and prior-art §8.1 both call instrumenting a human scratch the highest-value experiment in the programme. Every number every team designed to is ESTIMATED. A hand-held nail on a calibrated spring, used by Michael on his own scalp against a kitchen scale, turns estimates into measurements in an afternoon; a motorised rig built to unmeasured numbers may be wrong in every axis at once.
2. **Six of the thirteen open questions need no motor.** Q1, Q3, Q6, Q8 are tip-and-force; Q4 and Q7 need only a hand that holds one or three nails and can be turned.
3. **Self-generated irregularity is a perfect calibration pattern.** The wand's weakness (self-touch is centrally attenuated [FOUND §4.3]) is its strength as an instrument: if the wand in Michael's own hand does not feel *mechanically* like a scratch — edge reaching skin, satisfying bite, no snag — no motor will fix that, and the programme should go back to the tip, not forward to the arm.

### 2.2 The Day-0 hand wand (before any motor exists)

Tip-interface T0 with Team G's tang block and a three-nail option:

- One printed **TM1 tang block** (pocket 10.3 × 4.3 × 12.5 at 45°, N52 6×2, TPU collar) on a **0.3 mm × 12.7 mm feeler-gauge leaf**, free length 35 mm (k ≈ 0.4 N/mm; slide the clamp to 45 mm for 0.2), in a printed pen-sized handle with an 8 mm depth-stop lug [TEAM-G; FOUND tip-interface §5.4].
- A **three-leaf carrier** (G's 60 × 18 mm print, seats on R 85) on the same handle — this *is* tip D and *is* the hybrid's hand; nothing is thrown away.
- Six tips: **A** (0.3), **B** (0.6), **C** (nail corner), **F** (POM, friction A/B), **H** (3 mm ball control), **W** symmetric wedge for bidirectional strokes [TEAM-C/G].
- Kitchen scale, 10× loupe, lint roller.

What it answers (T1–T3, ≈ 3 sessions over 3 days): (1) **reach** — side photos on the real-hair mannequin at 0.3/0.5/1 N: does a 12 mm curved edge reach skin through Michael's hair? (G risk 1, "fatal to sensation"); (2) **force band and radius** — forearm screen, then blind scalp H vs A; if the ball is not an overwhelming loser the setup is wrong before any motor matters [FOUND tip-interface §9]; (3) **1 vs 3 nails, A vs F, A vs C, uni vs W-bidirectional, with/across/against lie** — 40-second paired comparisons; (4) **compliance** 0.2 vs 0.4 N/mm by sliding the clamp; (5) **element-level hair safety** — 200 strokes per tip on the wig, 15 g / 50 g tethers, gap probe at the collar: C7 is cleared or fixed here, once, for every mechanism. Cost ≈ $30 of consumables; 3 hours. **No motorised part is installed until step 1 passes.**

*Day-0b (optional, one evening):* the three-leaf hand on a fixed 2020 stub, Michael moves his head under it (A-W1 / D mode 0 / F4). Tests whether hands-free contact without a motor reads as "someone" or "a post", and measures head wander against a fixed hand.

### 2.3 The simplest viable motorised rig

Two candidates pass every gating rule at one motor: **F's WR-1** (N20 + double eccentric, $85–148, 12 h) and **G's Concept 1 "Swing-Rake"** (one XL330 swinging the hand on an 83 mm arm; the non-concentric arc lifts the tips at both ends of the swing; ≈ $150 with Stack-A electronics, ≈ 14 h). One difference decides it:

| | WR-1 (F) | Swing-Rake (G concept 1) |
|---|---|---|
| Length / location jitter | none (eccentric fixed) | **yes** — servo amplitude and centre are free within ±18°: length ±25 %, start drift ±20 mm in firmware |
| Speed / pause jitter | yes | yes |
| Depth (force) jitter | no (screw) | no (screw) — needs the second servo |
| Lift | ellipse, 13 mm every cycle | arc, ≈ 6–15 mm at ±18–25°, amplitude-dependent |
| Contact duty | 23–31 % (F risk 2: may read as flicks) | ~50 % at ±18° |
| Fail-safe lift | pedal dip stage | needs adding (§3.3) |
| Upgrade path | new crank + traverse servo; ~$150 of parts discarded | **bolt on one XL330 and one printed link → full ARC-RAKE; nothing discarded** |

The swing-rake is the simplest viable rig *that is also stage one of the full one*. That is the answer to BRIEF §14: a one-motor machine can plausibly match the seven on the north star, and the way to find out is to build the one-motor machine that is a strict subset of the two-motor one, run PERIODIC vs HUMAN on Michael's scalp in week 1, and let the data buy the second servo.

### 2.4 Honest verdict

Can something simpler *outperform* all seven? Not demonstrably: they share the per-stroke physics, and the only lever left is C, where "simpler" means "less of it". Can something simpler **match** them and tell us whether the rest is needed? Yes, and that is worth more in week 1 than any complete design. The wand is mandatory; the single-servo swing-rake is the right first motor; the second servo is a $27 decision made with data.

---

## 3. The hybrid: SP1-H "LEAF-ARM"

### 3.1 Decisions on the three axes

**(a) Head-worn primary, one module for three mounts.** The leaf cap is only a constant if the hand is registered to the skull within its spring travel; a ratchet suspension does that, a frame does not [D1]. Michael sits normally, no forehead cradle, ratchet knob = ≤ 3 s release. The module's frame plate carries one 40 × 40 mm M4 bolt pattern that mates to (i) the **arch clamp** on the suspension, (ii) a **2020 bench stub** over the mannequin (every bench test and calibration — Team D's instrumented frame, shrunk), and (iii) a **VESA-100 plate** for a monitor arm if head-worn fails on noise or band rocking (Team E's mount; Team B's mount-agnostic note). The frame option is free insurance, not a second design. Head-borne ≈ 350 g [EST].

**(b) 2-DOF planar servo arm (Team G), built single-motor first.** Against the alternatives: one motor cannot jitter length, location or depth, nor land softly (A, F; §2.3); five servos on the head (B) buys per-finger phase that compliance supplies and H-5.6 forbids using; direct drive (E) buys readout and silence at the cost of heat, $60/axis and a tuning gate, to render a compliance the leaf already has. The XL330 in current-based position mode with a low Goal Current on the **shoulder** — target below the scalp, current ceiling sets the push — is the cheap surrogate for E's impedance idea; E's GM3506 + SimpleFOC Mini stays documented as the shoulder drop-in (G's own red-line-7 fallback) if servo texture or whine is perceptible.

**(c) Passive cap and active control, in the safety track's order.** Layer 1: leaf + 10 mm stop (2.0–2.4 N/nail) and a shoulder stop screw sized so the leaves cannot bottom at the closest credible head position (safety §3.1 cond. 2). Layer 2: Goal Current on both joints (≈ 0.8 N tip on the elbow, ≈ 1 N on the shoulder). Layer 3: firmware depth setpoint, jitter, snag reflex. Readout: shoulder Present Current calibrated on the kitchen scale, one FSR 402 under the centre leaf root, and a 1 kg bar load cell under the mannequin on the bench stub [TEAM-D, off the head].

**Contacts: 3 at 20 mm**, 1 and 2 by pulling tips. **Coverage: one 50 × 40 mm patch per seating**, two printed sockets (rear crown; occiput) × four orientations [TEAM-F]. **Lift: triple** — geometric arc, commanded shoulder, fail-safe stage. **Primitive: D-cycle default** (with-grain contact, air return) plus bidirectional with the W tip, chosen by the wand.

### 3.2 Borrowed subsystems and why each beats its alternatives

| Subsystem | From | Beats | Because |
|---|---|---|---|
| Hand: 3 TM1 tang blocks on 0.25–0.3 mm feeler leaves (k 0.2–0.4 N/mm, 10 mm stop), carrier on R 85, 1 mm PETG/nylon paddles 30 mm with heat-formed 45° foot, hand-level D61 breakaway ≈ 3 N | **G** (carrier, tang blocks, paddles); **C** (steel leaf as pulp, heat-shrunk leaves, arc landing); **A** (leaf trailing the carrier, preload shim) | B's coil-spring sleeves (sliding gap, mass); F's PETG flexures (creep, fatigue); C/A knuckle pins + detents (pins and magnets in the hair-reach volume) | Gapless, no sliding seams, no creep; the paddle's own flexure (0.2–0.35 N/mm [TEAM-G]) gives the self-limiting "DIP give". C's knuckle detent is the named fix if the 50 g tether lifts. |
| Mover: XL330 shoulder (lift/depth) at z ≈ 105, 42 mm link, XL330 elbow (sweep ±35°) at z ≈ 75, 83 mm radius to nail, both above a 4 mm guard plate at z ≈ 58 with a 32 × 14 mm drafted window | **G** | A/F one-motor paths; B five servos; C tendons; D yoke (frame-only); E FOC | Contains the one-motor swing-rake; exposes every PATTERN SPEC variable; two $27 actuators; ~100 lines of IK with the leaves absorbing error. |
| Geometric lift as backup | **G/C/A/F** | pure commanded lift (B, D, E) | An IK bug cannot produce an under-load reversal; lift exists with the shoulder frozen (week 1). |
| Fail-safe: 12 mm sprung **dip stage** between frame plate and arch, latched down by a 5 V pull solenoid on the actuator rail; any rail loss (e-stop, pedal, fuse, watchdog) drops the pin and the module rises 12 mm at zero force | **F** (dip stage); **B** (solenoid latch, 20× plug-pull test) | G's bias spring (needs unmeasured back-drive); A/D "limp"; C tendon springs | Independent of servo back-drivability; purely mechanical once the pin drops; doubles as the coarse standoff thumbscrew, so A/F's "intensity is a mechanical setting" survives. |
| Pattern engine: seeded PRNG; per-cycle resampling of L, v, depth, start-x, pause, episode; 3-cycle no-repeat; `PERIODIC` / `LOCKED_PHASE`; snag reflex = shoulder up, elbow hold, never reverse | **B** (most complete), **A** (bout/pause engine, slow CT bout per minute), **G** (D-cycle, sphere R_h parameter) | ad-hoc jitter | B wrote scratch-model §4.4 as code; it ports to any 2-DOF arm unchanged. |
| Mounts: hard-hat 4-pt ratchet suspension + printed ring with two sockets × 4 orientations; arch with crown pad; same module on wand handle, bench stub, VESA plate | **F** (ring, sockets, wand mode); **G** (arch); **B/E** (VESA) | A's cut hard-hat shell (+250 g); D's cage; C's bridge | Lightest registered mount; mount-agnostic by one bolt pattern. |
| Instrumentation: bench load cell under the mannequin (HX711, 80 Hz CSV); FSR under centre leaf; servo current; 240 fps side video; F's pointer scale on each leaf | **D** (log force, do not assume it), **E** (contact fraction from position vs force), **F** (zero-cost pointer) | none (A, C) | A research rig without a force log answers nothing in §9. |
| Tangential protection: paddle flexure → elbow Goal Current (0.8 N) → hand D61 breakaway (3 N shear, falls away) → TM1 magnet (4–8 N axial); normal softness lifts a trapped strand at ~0.15 N upward | **G**, **A/F** | 0.15 N element yield (unachievable, C9) | Four measured layers; the tether test judges. |
| Electronics: OpenRB-150, 5 V 4 A brick, fuse, NC e-stop, pedal, INA219, two pots, solenoid MOSFET; logic on USB; Bus Watchdog 100 ms | **Stack A** [FOUND], **B** | E's SimpleFOC, F's Pico+DRV8871, C's Waveshare+STS3215 | Zero-fuss Dynamixel path; two servos on one cable; e-stop breaks the rail with the controller alive. |

### 3.3 Kinematics and force summary

- Elbow radius 83 mm, scalp R 80–90. Shoulder frozen, set depth 3–4 mm: the arc meets the sphere over ≈ ±11–13° → **chord ≈ 30–36 mm**; force bell-shaped 0 → 0.6–0.8 N → 0 at k 0.2 N/mm (0.3 → 1.1 N with a 0.3 N preload shim); over-swing to ±25° lifts ≈ 15 mm at zero force [EST from G's geometry; G quotes a smaller rise — the week-1 240 fps side video settles it]. Shoulder tracking: strokes 15–52 mm, depth held ±0.5 mm, commanded lift 10–25 mm.
- Speed 50–150 mm/s in contact (cap 200), 1.5–3.5 Hz; trapezoid, ≤ 2 m/s²; lift begins at 70 % of stroke at ≥ 50 % speed; re-entry ≤ 20–30° [TEAM-G; FOUND H-5.3/5.4].
- Caps: per nail 2.0 N (0.2 × 10) or 2.4 N (0.4 × 6 mm shim); total ≤ 7.2 N; tangential ≤ 1 N at the hand before breakaway; tip ≤ 0.3 m/s; moving element ≈ 30 g; head-borne ≈ 350 g [EST]. Inside red lines 2, 3, 10 and safety §2.4.
- Hair checklist expected **34/36** (G's inventory; the dip stage adds nothing to the zone); items 7 and 16 at 1, as in every candidate.

### 3.4 Rough BOM

| Qty | Item | Ext. | Source |
|---|---|---|---|
| 2 | Dynamixel XL330-M288-T (elbow week 1; shoulder week 2) | $55 | robotis.us |
| 1 | OpenRB-150 | $29 | robotis.us |
| 1 | 5 V 4 A UL-listed brick (Adafruit #1466) | $18 | Adafruit |
| 1 | 22 mm NC mushroom e-stop (boxed) + momentary foot pedal | $20 | Amazon |
| 1 | INA219 | $10 | Adafruit |
| 1 | 5 V mini pull solenoid + MOSFET + flyback diode | $6 | Amazon |
| 1 | 2 × 10 kΩ pots, PERIODIC/HUMAN toggle, rocker, fuse holder + fuses, JST/22 AWG/heat-shrink | $30 | Amazon |
| 1 | FSR 402 | $7 | Adafruit |
| 1 | Hard-hat 4-point ratchet suspension | $15 | Amazon |
| 1 | 3 × 20 mm aluminium flat bar 500 mm (arch) + 25 mm closed-cell pad | $8 | hardware store |
| 1 | Feeler-gauge set 0.2–0.5 mm × 12.7 mm (leaves) | $8 | Amazon |
| 1 | 1.0 mm PETG and/or nylon sheet (paddles) | $10 | Amazon |
| 1 | Press-on nails (24) + Tortex 1.14 and nylon .88 picks | $11 | drugstore / music shop |
| — | N52 6×2 ×10, D61 ×4, M3 steel washers | $8 | K&J / Amazon |
| 1 | Compression + extension spring assortment (dip stage, shoulder bias) | $12 | Amazon |
| — | M3/M4 screws, heat-set inserts, thumbscrews, 3 mm pins | $18 | Amazon |
| — | PETG prints ≈ 320 g + TPU 95A collars (library or one JLC3DP order) | $35–50 | library / JLC3DP |
| 1 | 2020 extrusion 300 mm + 4 corner brackets (bench stub) | $12 | Amazon |
| | **Build subtotal** | **≈ $300–315** | |
| 1 | Mannequin head, 100 % human hair, + clamp | $43 | Amazon |
| 1 | Kitchen scale 0.1 g; luggage scale; 1 kg bar load cell + HX711; 10× loupe; lint roller; hygrometer | $50 | Amazon / SparkFun |
| | **Build + test gear** | **≈ $395–410** | |
| opt. | Gas-spring VESA monitor arm (boom mode, only if head-worn fails) | +$36 | Amazon |
| opt. | GM3506 + AS5048A + SimpleFOC Mini (direct-drive shoulder swap) | +$60 | iFlight |

Week-1 exposure if the wand fails and the project pauses: electronics + one servo + suspension + leaves + nails ≈ $190, all reusable.

**Build hours [EST]:** wand and tips 3 h · week-1 swing-rake (frame, guard, hand, arch, electronics, 1-DOF firmware, bench) 14 h · week-2 shoulder, dip stage/solenoid, IK, pattern engine, FSR logging 12 h · week-3 calibration, hair bench, safety checklist, staged sessions 10 h → **≈ 40 hands-on hours**, printing excluded.

### 3.5 Top five risks

| # | Risk | Named by | Retiring test |
|---|---|---|---|
| 1 | **Nails ride on the pile in Michael's hair at ≤ 0.3 N** — fatal and invisible to every design | G risk 1; F, E item 2 | Day-0 wand, static tip test with side photos at 0.3/0.5/1 N; fix = +5 mm paddle, +depth, coarser leaf, tip C |
| 2 | **"A machine" within 30 s despite jitter** | A, E, F, G risk 1/4 | Week-1 blind PERIODIC vs HUMAN on the single-servo rig, rated every 30 s for 3 min; week 2 adds depth/landing jitter; if still "machine", test 1-nail jittered vs 3-nail rigid (E) and the frozen-shoulder velocity profile (G) |
| 3 | **Servo whine / bone conduction 75–105 mm from the ear masks the hiss** | B, D, F, G | Phone SPL at the ear on the mannequin; ear-plug A/B (Q9); then TPU-isolated servo pockets, XL330-M077, GM3506 shoulder, boom mount |
| 4 | **Band/arch rocks under ~1 N stroke reaction → depth drifts ±1 mm = ±0.2–0.4 N** | G risk 3, A risk 4, C R2 | FSR + servo current during a 5-min wear with deliberate head motion; fix = stiffer arch, nape pad, snugger ratchet; last resort boom mount, same module |
| 5 | **Fail-safe lift binds or is slow** (solenoid pin under load, weak spring) | B risk 4, G risk 2 | Pull the plug 20× mid-stroke at the 2.4 N cap; up-stop within 200 ms every time; repeat for pedal release and watchdog halt |

Honourable mention: hair capture at the TM1 collar (F risk 3, C item 3) — cleared on Day 0 by the gap probe.

---

## 4. Staged build — nothing built before it is known to matter

| Stage | Build | Answers | Gate |
|---|---|---|---|
| **Day 0** | Place all orders in parallel. Print wand handle, tang block, three-leaf carrier, 6 tangs. Make tips A, B, C, F, H, W. | — | — |
| **Days 1–3: HAND WAND** (§2.2) | Wand + kitchen scale + mannequin. T1 bench (breakaway, k, 200 strokes/tip, collar probe, tethers), T2 forearm, T3 blind scalp pairs. | Q1 reach, Q3 force band, Q4 count, Q6 edge, Q7 direction, Q8 penetration; the tip, force band, k, angle and direction the mechanism must reproduce; red line 11 forearm screen. | **Tip reaches skin; A beats H decisively.** If not, fix the tip; no motor. |
| **Week 1: SWING-RAKE** (G concept 1 on the hybrid frame) | Frame + guard plate, hand carrier (from the wand), frozen-shoulder bracket, one XL330 elbow, OpenRB, brick, fuse, e-stop, pedal, INA219, pots, PERIODIC toggle. Arch + ring with one socket; depth by arch standoff thumbscrew. Bench stub + load cell. 1-DOF firmware: amplitude, centre, speed, pause jitter; bout engine; stall trip. Hair bench 7.3.1–7.3.9; safety §6 A–D. | First motorised sensory data: Q2 speed, Q5 predictability penalty, noise (risk 3), band rocking (risk 4), motor stroke vs own-hand stroke, force-vs-angle map. | **HUMAN mode stays "person-like" > 2 min and ≤ 60 dBA.** If PERIODIC equals HUMAN, the second servo is bought for lift/depth only; if neither feels like a person, the fault is per-stroke physics or noise — back to the wand before adding anything. |
| **Week 2: ARC-RAKE + fail-safe** | Shoulder XL330, upper link, bias spring, stop screw; dip stage with solenoid latch; second socket; FSR; 2R IK with sphere model; full PATTERN SPEC (B's engine); snag reflex; 20× plug-pull; limits table at boot. | Depth/force jitter, soft landings, long strokes at constant depth, commanded lift, in-session force log; red line 8 closed without trusting back-drive. | Safety checklist; wig-head entanglement pass; staged exposure (forearm → palm → scalp 2 min). |
| **Week 3: experiment matrix** | No new hardware unless gated. Tip A after B; k 0.2 vs 0.4; 1/2/3 nails; uni vs bidirectional; with/across/against; slow CT bouts; 5 → 10 → 20 min sessions with scalp and hair audit. | Q2–5, Q9–12; the SP2 decision (direct-drive shoulder? traverse axis? fingers? boom?). | SP1 report and iteration map. |

Deferred until a gate opens: monitor arm (risk 3/4), GM3506 kit (servo texture/noise), C's knuckle detents (50 g tether lifts), 4th-finger carrier (3 reads as "a hand"), F's air-jet nozzle (Q1 says skin contact may be unnecessary).

---

## 5. Every part, against "does this help determine whether automated human-like scratching can feel excellent?"

**Kept — one job each.** TM1 tang blocks and tips A/B/C/F/H/W: the stimulus, with edge, radius, friction and width as variables (§7 ranks 5, 12). Steel leaves, carrier, clamps, preload shim: the pulp (§3.12), the cap (red line 2), and free asynchrony (§8 item 7). Paddles with 45° foot: reach through the pile (H-4.5) and tangential give, gapless. TPU collars: the one trap-band gap (C7). Hand D61 breakaway: no-tether overload release (H-6.4). Elbow XL330: the stroke with length/location/speed/pause jitter (rank 1). Shoulder XL330, link, stop screw, bias spring: depth setpoint and jitter, sphere tracking, soft landing, commanded lift (ranks 1–3); week 2. Guard plate: makes the rotation rule true (H-6.3). Dip stage + solenoid + spring: red line 8 and the coarse depth stop. Suspension, ring with two sockets, arch, crown pad: skull registration (the cap's precondition), 5 s region/direction change, 3 s release. Bench stub + load cell + HX711: the force–pleasure curve (Q3) needs a number. FSR: in-session relative force at $7 and 1 g. OpenRB-150, brick, fuse, NC e-stop, pedal, INA219, rocker: the mandated chain (red line 4). Two pots + PERIODIC toggle: intensity, speed and the control condition as knobs a blindfolded tester can use. Mannequin, scales, loupe, lint roller, hygrometer: the hair tests and calibration cannot be done without them. Wand handle: Day 0, then the tip-swap jig.

**Removed or deferred — fails the question, or a cheaper part answers it.** OLED (every team): a laptop over USB shows the same table; removed. Cut hard-hat shell (A): +250 g for what the guard plate does; removed. Moving shroud + skirt (A): needed only because A's crank sat 44 mm up; removed. Load cell on the head (D): the bench cell and FSR measure the same thing; kept on the bench only. Knuckle pins + detents (C, A): pins and magnets in the hair-reach volume to move item 7 from 1 to ~1.5; deferred to the tether result. Fourth finger, 22/25 mm carriers (B, C, D): 1/2/3 covers Q4; SP2. Independent finger drives (B): H-5.6 forbids using them in contact; compliance gives the spread; removed. Gimbal motors, SimpleFOC, fan, NTCs, counterweight (E): the leaf already renders the compliance, readout has a $7 surrogate, heat and tuning cost more than they answer; deferred to the shoulder swap. Bowden cables, spools, desk box (C, E2, F pedal cable): ±30 % hysteresis; the solenoid latch does the dead-man job without a cable; removed. Yoke, pivots, counterweight, forehead cradle, side shields (D): coverage along a band is not the core experiment (§15); removed. Double eccentric, lift frame, slide rods (F): the arc gets the same lift from one servo and keeps length/location jitter; removed. AS5600 crank sensor and ω(θ) tables (A): a servo knows its angle; removed. Monitor arm: insurance, bought only if head-worn fails. Hard hat, welding headgear: suspension + arch is lighter; removed. Air-jet, pantograph proxy, magnetic pucks, voice-coil arms (F-W1, D-W2, B/E-W1, C-W1): good SP2 probes, none on the path to the first excellent scratch; deferred.

---

## 6. Note to the Director and judges

The tournament's useful output is not a ranking of seven mechanisms; it is the discovery that seven independent teams built the same hand and disagreed only about the arm. The hand is settled. The arm question — how much motorised irregularity the scalp actually needs — is the one experiment nobody can reason their way out of, and it is answered cheapest by building the hand first (Day 0), the one-servo arm second (week 1), and the second servo third (week 2), on a module whose single bolt pattern lets it ride a headband, a bench stub or a monitor arm without redesign. If week 1 says fixed strokes go dead in seconds, the second servo is already in the drawer; if it says they do not, Michael has a $190 machine that scratches and $200 of parts he never had to build.
