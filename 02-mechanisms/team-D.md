# PROJECT SCRATCH — Mechanism Team D: Stationary Lean-In Frame with a Traveling Carriage

**Team:** D (seed family: stationary lean-in frame, traveling carriage, nothing worn on the head) · **Date:** 2026-10-01
**Inputs read:** BRIEF.md, scratch-model.md, hair-interaction.md, safety-requirements.md, tip-interface.md, component-landscape.md. Firewall respected (no other team files, no prior-art.md).
**Selected concept:** **D2 "CRADLE"** — a counterbalanced C-arm (yoke) pivoting about the head's own centre, carrying a dead-weight-loaded three-nail hand with a tendon lift. Everything else in this document is either an alternative we rejected or a module CRADLE can host.

Tags: **[KNOWN]** from the foundation docs · **[EST]** our engineering estimate · **[UNKNOWN]** must be tested.

---

## 0. The family's physics in one paragraph

A stationary frame removes every head-worn constraint at once: mass is free, so NEMA/XL430-class actuators and a 1 kg counterweight are allowed; the frame can hold a load cell in the force path, so SP1 becomes an instrumented rig by default; and the head itself is the quick-release (safety §5 principle 5 — "withdraw head"). The family's two problems are geometric: (1) the scratching element must track a sphere of R ≈ 60–100 mm while a Cartesian machine naturally moves in straight lines, and (2) the user must hold still-ish against a rest for 10–20 minutes. Our answer to (1) is to stop fighting the sphere: put the carriage's axis of travel *through the head centre* so the element moves on a constant-radius arc and the attack angle never changes. Our answer to (2) is the massage-chair face-cradle posture (forehead on a padded bar, hands on the desk), which also makes the forehead pad a hardware dead-man switch.

---

## 1. Concepts in the family (one paragraph + sketch each)

### D1 — ARC-RAIL: carriage on a printed curved V-rail

A 170°, R ≈ 175 mm arc rail printed in three PETG segments (V-groove profile) bolted to a 2020 frame over the seated head in the sagittal plane; a carriage on four Delrin mini V-wheels rides the arc; a GT2 belt is clamped along the arc groove as a "rack" and a NEMA 17 + 20T pulley on the carriage climbs it (TMC2209, StealthChop, StallGuard for collision). The 3-nail hand hangs under the carriage on a radial float with a dead weight; a small servo lifts it at stroke ends. Strengths: long sweeps (P2) at constant radius; stepper is silent. Weaknesses: a printed arc rail in three segments has joint steps (hair-irrelevant, but wheel bump and noise), the moving motor drags its cable, belt-on-arc needs a groove of good fidelity, and the rail costs ~300 g of PETG with ±0.3 mm tolerance over 500 mm — the riskiest print in the family.

```
          printed V-groove arc (R175, 3 segments)         frame 2020
      _.-"""""""""""-._                                      ||
   .-'   carriage ⊡==NEMA17 (belt-on-arc)                    ||
  /       | float + dead weight                              ||
 |        |  [hand: 3 nails]                                 ||
 |      ,-'''-.   <- scalp R90                               ||
 |     /  head \                                             ||
 |    | forehead|--[pad]                                     ||
```

### D2 — CRADLE: counterbalanced C-arm pivoting about the head centre (SELECTED)

Two pivot stubs on 608 bearings at ear height, ±140 mm from the mid-sagittal plane, carry a U-shaped yoke (two 2020 arms + crossbar) that swings over the crown from −45° (top, just behind the hairline) to +115° (nape). Because the axis passes through the head centre, the hand hanging from the crossbar sweeps the sagittal great circle at constant radius: no curved parts, one rotary drive (Dynamixel XL430 at one pivot), and the attack angle is constant along the whole sweep. The hand is a palm with three tip-A nails at 20 mm pitch on individual 0.4 N/mm leaves, floated radially on an inclined parallelogram under a dead weight (0.6–2.0 N total, a mechanical constant), with a Dyneema tendon to a second XL430 that can only *lift* (it can never add force). A 1 kg bar load cell sits in the float, so normal force is logged in real time. Michael sits at a desk with his forehead on a padded bar that doubles as the hardware dead-man switch. Developed in §2.

```
        lift servo
      [XL430]--tendon        crossbar (2020)
   ======+=========================+======   <- yoke, pivots outboard at ±140 mm
         |   parallelogram float   |
         |  [load cell]  (m)dead wt|
         |   palm ──┬──┬──┐        |
         |   guard  │  │  │ nails (3 @ 20 mm, tip A)
      ~~~~~~~~~~~~~~~~~~~~~~~~~  hair canopy
   ,--'''''''''''''''''''''''''''--.
  /         scalp  R90              \      ⊙ pivot axis through head centre
 |   forehead pad [==]   ⊙           |     (ear height, outboard)
 |   = dead-man switch               |
```

### D3 — SAGITTAL GANTRY + ROLL: straight rail, roll axis, reciprocating nail module

An MGN12H 300 mm rail runs front-to-back above the crown (GT2 belt, NEMA 17); the carriage carries a roll stage (XL430) about the sagittal axis so the module can be swung ±60° to the sides; the module itself is a "finger" — an XL330 crank with a spring-loaded follower producing a 15–40 mm reciprocating rake with a cam-driven lift at each end. This is the most capable machine (crown, top, both parietals from one setup; strokes decoupled from carriage travel) and the most complex (3 motorised DOF + reciprocating module, two of which must be interlocked for lift-off). The straight rail fights the sphere: over a 100 mm carriage sweep the sagitta is 14 mm and the attack angle wanders ±32°, so sweeps (P2) are poor unless the float travel is ≥15 mm and angle is actively corrected. Rejected for SP1: the complexity buys coverage, not scratch quality, and brief §15 says coverage is not the core experiment.

```
   NEMA17 ==GT2== [carriage]==MGN12 rail============
                     |roll (XL430)
                     +--[XL330 crank finger: 15-40 mm rake + cam lift]
                            ↓ ↑
      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~  canopy
   ,--''''''''''''''''''''''''''--.    sagitta over 100 mm = 14 mm  (!)
```

### D4 — HOOD: salon-dryer hood with four fixed finger modules, no carriage

A hemispherical printed/acrylic hood on a dryer stand hovers 60 mm over the head; four XL330 "fingers" (torsion-spring knuckle, magnet-breakaway tip A, 40 mm arc rake with lift inherent in the arc) are bolted through the hood at the crown, left/right parietal and occiput. No carriage: each finger works a 40 × 20 mm patch; region "changes" are which finger is active; hood is repositioned by hand for other patches. Cheap to control (Stack A as-is), four independent contacts (asynchrony and P4 "spider" come free), but each patch is small, the hood must be refitted per head position, and four fingers through a shell near hair means four pass-throughs to seal. A strong SP2 add-on to CRADLE (its hand could be replaced by a four-finger cluster) but a weaker core experiment because strokes are only ever 40 mm.

```
          _.-=====-._   hood on salon stand
       .-'  F1   F2  '-.     F = XL330 finger module (arc rake 40 mm)
      /   F3      F4    \
     |   ~~~~~~~~~~~~~   |   canopy
     |  ,-''''''''''-.   |
```

### D5 — CAT-POST: passive dead-weight rake; the head supplies the stroke

No carriage motor at all. The CRADLE hand (or a single tip-A finger) hangs on its float from a fixed arm; Michael moves his head slowly under it — nod, roll, draw forward — like a cat on a post. A single XL330 adds a 5–15 mm "wiggle" on top. This answers the cheapest possible question ("does a dead-weight nail at 0.3 N through my hair feel like a scratch at all?") for ~$60 and is literally Mode 0 of CRADLE (motors off). Its sensory weakness is predictability and self-generation: the cerebellum predicts self-motion, so the "someone else" attribution (scratch-model component E, and the self-tickle argument in §4.3) is lost. Kept as the first human test, not as SP1.

```
      fixed arm ====+
                    | float + (m)
                   [hand]
                     |||  nails
     ~~~~~~~~~~~~~~~~~~~~~~   head nods / rolls underneath  <->
```

### W1 — WILDCARD (outside the family): RESTING HAND — a tendon-curled soft glove that lies on the head

A 120 g printed TPU/PETG "hand" (palm pad 60 × 80 mm, four two-phalanx fingers with TPU living hinges — no pins — each ending in a press-on nail) simply rests on the crown like a real hand; its own weight is the normal force (1.2 N spread over palm pad and four nails, each nail ~0.2 N). Four Bowden tendons (bike shift cable in PTFE-lined housing) run to four XL330s on the desk; pulling a tendon curls the finger so the nail drags 20–30 mm toward the palm — exactly the P1 motion of a human finger — and an elastic return extends it, lifting the nail in an arc at the end of every curl (lift-off is intrinsic to the kinematics, the nail rises leading-edge-first as H-5.2 prefers). Independent fingers give P4 "spider" and asynchrony for free; a hand-warmer pouch in the palm reproduces component E (warmth + weight of a resting hand). Hazards: tendon housings must terminate above the hand (sheathed, no exposed cable near hair), the living hinges must be TPU with no gaps (H-4.9), and Michael's head motion drags a passive object. It is head-*resting* not head-*worn* (no straps; it slides off if he stands). We think this is the most sensorially promising non-frame concept in the project and recommend it to the Director as a cross-team module: it bolts onto CRADLE's crossbar as "Hand v2" without changing the rig.

```
   desk: [XL330][XL330][XL330][XL330] --- 4 Bowden tendons (sheathed) ---.
                                                                          |
                   palm pad (120 g, warm)  ____                            |
                              ,-----------(____)---.  tendon entry (top)   |
          nails -> ╭─╮ ╭─╮ ╭─╮ ╭─╮        <- TPU living-hinge fingers      |
     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ canopy;   curl = 20-30 mm rake toward palm
   ,--'''''''''''''''''''''''''''--.           extension = arc lift-off
```

### W2 — WILDCARD (brief): PANTOGRAPH PROXY

Michael's own free hand "scratches" a dummy pad on the desk; a passive 2-DOF cable pantograph (two Dyneema loops over pulleys, 1:1) copies the motion to the CRADLE hand. Zero motors in the stroke path, human irregularity by construction, and it tests whether the loss of "other-person" attribution matters when the *contact* is not self-generated (the pantograph decouples hand from head). Buildable in a day on the CRADLE frame; listed as an experiment, not a mechanism.

### Selection

| Criterion (brief §13) | D1 arc-rail | **D2 CRADLE** | D3 gantry | D4 hood | D5 cat-post |
|---|---|---|---|---|---|
| Scratch realism potential | good | **good** | good | medium (40 mm only) | low (self-generated) |
| Follows curvature | by rail | **by geometry** | poorly | per-patch | n/a |
| Lift-off | servo | **tendon servo** | cam | arc inherent | none |
| Force cap | dead weight | **dead weight + load cell** | spring | torsion spring | dead weight |
| DOF motorised | 2 | **2** | 4 | 4 | 0–1 |
| Risky fabrication | curved rail print | **none (pivot alignment ±1 mm)** | roll stage | hood shell | none |
| Cost | ~$500 | **~$470–535** | ~$650 | ~$450 | ~$80 |
| Build hours | 35 | **30** | 50 | 35 | 6 |

D2 wins because it is D1 with the curved rail replaced by a pivot: same kinematics, one fewer hard part, better repeatability, lower noise, and the dead weight sits in a load-cell-instrumented float. D5 is absorbed as Mode 0; W1 is proposed as a future hand module.

---

## 2. CRADLE — concept-level engineering design

### 2a. Working principle and why it will feel like fingernails

The scratch model (§1.2–1.3) says the two signatures unique to scratching are a **stiff narrow edge reaching the skin** and **hair deflected within 2–5 mm of the root**; the tip-interface doc adds that the sensation is **skin ploughed and released by a 0.2–0.6 mm edge at 0.05–0.15 N/mm line load behind a ~0.4 N/mm spring**. CRADLE reproduces exactly that stimulus and nothing else:

- **Edge, not pad:** three tip-A nail-mimic blades (press-on ABS nails, R 0.3 mm edge, 12 mm wide, transverse R 9 mm) on 28 mm drafted stems, at a fixed 45° attack referenced to the local scalp normal.
- **Reaches the skin:** the stems protrude 28 mm below the guard (> 20 mm pile + margin, H-4.5); the hand floats radially under dead weight so the blades descend until they are on skin, not on the canopy. Normal force per nail 0.2–0.65 N — the scratch-model band (3.2) and inside the tip window.
- **Light and spring-backed:** 0.4 N/mm leaf per nail + a 20 mm constant-force float. A 1 mm scalp bump changes a nail's force by 0.4 N, not by a stall (scratch-model 3.12).
- **Slides:** 20–140 mm of sliding on the skin per stroke at 20–200 mm/s, reciprocating at 1–2.5 Hz with lift between strokes; scalp displacement over the skull is < 1 mm because the tangential load per nail is 0.1–0.3 N.
- **Deflects hair near the root:** the blade edge is on the skin, so every hair it meets is bent at the follicle exit (the 1/L² argument in scratch-model §2.3), ~10 hairs per mm advanced, ~2,000 hairs per 3-nail 60 mm sweep.
- **Irregular:** the yoke drive is fully programmable (stroke length, speed, start position, dwell, pauses all resampled per stroke per PATTERN SPEC v1), and the tendon can modulate normal force ±30% at 3–6 Hz *by partial unloading only*, so jitter can never exceed the dead weight.
- **Not a massager:** nothing in CRADLE can press (no element > 2 N), vibrate (no component > 6 Hz), knead (scalp does not move with the hand) or brush (the edge is below the canopy).

The honest limitation (§2j): SP1 CRADLE strokes in one direction per setup with a lifted return (like P2 sweeps and the human's "rake outward from the whorl"), not the bidirectional P1. The massager-vs-scratcher argument does not depend on bidirectionality; the realism argument might, and we propose the twin-palm module (§2g) if the first human test says so.

### 2b. Architecture

| Item | Value |
|---|---|
| Mount | Stationary 2020 desk cage, C-clamped to a desk; Michael seated, forehead on a padded bar (massage-cradle posture), elbows on the desk |
| Carriage | U-yoke (two 2020 arms 175 mm + crossbar 300 mm) on two 8 mm stub shafts in 608ZZ pillow blocks at ear height, ±140 mm from the mid-sagittal plane; axis passes through the head centre |
| Motorised DOF | 2: yoke sweep (XL430 at left pivot, direct coupled) + hand lift/unload (XL430 on crossbar via Dyneema tendon) |
| Passive DOF | hand radial float (parallelogram, 20 mm, dead-weight loaded); per-nail leaf (8 mm); hand tangential yield (magnetic wrist detent, 15 mm) |
| Manual settings | hand lateral lane on crossbar (0, ±40 mm) with roll (0, ±25°); hand yaw (0, ±20°); hand facing (forward/backward, 180° remount); head tilt (0/30/45° by rest height); dead weight (0–140 g); yoke hard stops (5° steps) |
| Contacts | 3 nails, 20 mm pitch, span 40 mm (tip-interface §6 recommendation); 1-nail and 2-nail variants by removing tips (empty pockets plugged) |
| Coverage per setup | one band 40 mm wide × up to 250 mm long (−45° to +115° at R 90 = 251 mm arc): top → crown → occiput → nape. Three lanes = 120 mm wide band. Sides/temples: not in SP1 (out of scope by scratch-model §5 conclusion 2) |

Posture and comfort: the forehead pad is 120 × 40 mm closed-cell EVA on a 2020 bar, tiltable ±15°, height-slotted. With elbows on the desk the head's forward lean is ~20–30° and the pad carries 10–20 N [EST] → 2–4 kPa, under the 5 kPa strap/pad limit; reposition every 20 min (safety §2.2). The posture is the one used on massage tables for 30–60 min, so 20 min is conservative. An optional chin bar (second padded 2020) halves the forehead load for the 45° head-forward (nape) configuration. The face is in open air (nothing in front of the eyes), the hands are free, and the exit path (chin down, slide the chair back) moves the head *away* from the yoke.

### 2c. Kinematics with numbers

Geometry (nominal, crown): head centre = pivot axis; scalp R_s = 90 mm; nails on skin at R = 90; hand float range R 80–100 (±10 mm about nominal); guard underside at R 118 (28 mm clearance above skin, > pile); crossbar underside at R 175 (85 mm above skin). Arc length per degree at the tip = 1.57 mm.

| Quantity | Value | Note |
|---|---|---|
| Yoke range | −45° (top, ≥ 20 mm behind hairline with 30° head tilt) to +115° (nape); printed hard-stop bosses in 5° steps; firmware limits 5° inside | red line 6 (hairline/eyes) is met by the stop, not by software |
| Stroke length L | 15–140 mm (10°–89° of yoke); P1 default 30 mm; P2 60–140 mm | resampled per stroke, ±25% |
| Tip velocity | 20–200 mm/s = 0.22–2.2 rad/s; XL430 no-load 6 rad/s, so ≤ 37% of no-load with ~60% stall torque available | hard cap 0.2 m/s (H-5.4); safety cap 0.4 m/s |
| Tangential accel in contact | ≤ 2 m/s² = 22 rad/s² (trapezoid profile) | H-5.4 |
| Yoke inertia | I ≈ 0.012 (carbon-tube arms) – 0.017 (2020 arms) kg·m² including a 1 kg counterweight at 75 mm below the pivot | balance torque < 0.1 N·m residual |
| Reversal torque | I·α ≈ 0.27–0.37 N·m at 22 rad/s² | XL430 1.5 N·m stall; fine |
| Carriage KE at 200 mm/s | ≤ 42 mJ (2020) / 30 mJ (carbon) | ≤ 50 mJ (safety §2.4) |
| Cycle rate | P1 (30 mm, lift-return): stroke 300 ms @ 100 mm/s + lift 40 ms (overlapped) + lifted return 150 ms @ 200 mm/s + controlled lower 60 ms = **~2 Hz**; 15 mm strokes reach 2.5 Hz; P2 (100 mm @ 80 mm/s) 1.25 s + 0.5 s return | 1–4 Hz spec: SP1 covers 1–2.5 Hz; the 3–4 Hz corner is a stated gap |
| Lift mechanism | Dyneema tendon from a 25 mm servo horn to the hand; 5 mm (force-to-zero) lift = 11.5° horn ≈ 35 ms; full 25 mm canopy clearance = 57° ≈ 170–200 ms | H-5.2: ≥ 5 mm with zero force at every reversal, full clearance at region changes and ≥ every 10 s |
| Lift path | parallelogram links inclined 30° from radial toward the stroke direction, so the tip lifts up-and-forward (overruns hair ahead of the edge) and re-enters at ≤ 30° to the skin while already moving | H-5.3 |
| Lift timing | lift command at 80% of stroke while tangential speed ≥ 30%; lower during the first 20% of the next stroke with the tendon paid out at a servo-controlled 0.3 s ramp (soft landing, not a tap) | scratch-model P6 "soft touch-down" |
| Force jitter | tendon partial unload ±30% of dead weight at 3–6 Hz; tendon can only reduce force | safe by construction |
| Irregularity | per stroke: L ~ N(30 mm, 25%), v ~ U(60,140 mm/s), start angle drift ±3° per 3 strokes, inter-stroke pause ~ U(0, 0.4 s) with p = 0.3, F scale ~ U(0.7, 1.3) via tendon; per episode: P1 60% / P2 30% / pause 10%; region change = lifted move ≥ 20 mm (adjacent p 0.8); "fully periodic" control mode | scratch-model §4.4 |
| Per-nail asynchrony | leaves shimmed 0.7× / 1.0× / 1.3× preload; local curvature error gives 20–80 ms contact spread naturally [EST] | checklist item 7 |
| Region changes | automatic along the band (start-angle jumps); manual across lanes and for head tilt | partial coverage accepted |
| Not available | direction drift ±20° (single plane; hand yaw is manual), P4 spider (no independent fingers), bidirectional P1 without the twin-palm module | declared gaps |

How the hand follows curvature: along the stroke, the sweep *is* the curvature (constant R about the head centre); across the three nails, the palm is printed with its pockets on an R 90 transverse arc (sagitta 2.2 mm over 40 mm) and an R 75 variant for the occiput; residual error (±1 mm) is taken by the 0.4 N/mm leaves (±0.4 N spread — within the ≥ 20% force spread the model wants); head mis-centering and radius variation (±10 mm) are taken by the float at constant force. The attack angle is constant because the pockets are referenced to the hand's radial axis, which always points at the pivot.

Mode 0 (CAT-POST): motors unpowered, yoke parked and clamped, hand lowered; Michael nods/rolls against the dead-weight rake. First human test, zero motion hazards.

### 2d. Force path

```
 scalp ← tip A blade ← 28 mm stem/TM1 tang ← TM1 pocket + magnet (4–8 N) ← leaf 0.4 N/mm, 8 mm, hard stop
       ← palm (R90 pre-curve) ← wrist magnetic detent (~0.5 N tangential, 15 mm swing, soft stop)
       ← load cell (1 kg bar) ← parallelogram float (20 mm, 623ZZ pivots) ← DEAD WEIGHT m·g
       ← [tendon: pull-up only, from lift XL430] ← carrier housing ← crossbar ← yoke ← pivot ← XL430 (sweep)
```

**Normal force (mechanical constant).** F_total = (m_hand + m_added)·g·cos(θ) where θ is the yoke angle from vertical. m_hand ≈ 60 g → 0.59 N; added slugs 0–140 g in 20 g steps on a post whose capacity is physically 140 g → **F_max,total = 2.0 N** when the yoke is vertical, independent of any actuator. A soft trim spring (k ≈ 0.02 N/mm from the assortment) can be hooked to subtract up to 0.4 N (nape/temple work, ≤ 0.15 N per nail) or add 0.4 N for off-vertical angles. In the formula of safety §3.1, preload = m·g, k·x_max = 0 for the float (constant force), and the per-nail leaf contributes nothing beyond the float because the palm rises before any leaf can carry more than the whole dead weight: **per-element worst case = 2.0 N (one nail carrying all), total ≤ 2.0 N**, both inside the 2.5 N / 12 N red lines.

**Stop placement check (safety §3.1 condition 2).** The float's up-stop is at +20 mm above nominal and the crossbar underside is 85 mm above the skin. For the carrier to push through the bottomed float, the head would have to rise 20 mm above its set position — which lifts the forehead off the pad and opens the dead-man contact (motor rail off) before contact force can rise through the structure. Margin: 20 mm float vs ~8 mm of pad compression before the switch opens. Verified on the bench by pushing a mannequin up into the hand on a kitchen scale.

**Angle dependence.** At θ = 45° the dead weight gives 0.71·F; at the nape (θ ≈ 100°) gravity no longer loads the nails. We do not fight this: the occiput/nape are reached by tilting the head forward 30–45° (massage-cradle posture), which brings them under the top ±45° of the sweep where F ≥ 0.7 m·g, and the trim spring restores the rest. The load cell shows the actual force at every angle; the firmware displays it and the pattern scales the tendon unload to flatten it. [EST]; retire by load-cell log vs angle on the mannequin.

**Tangential yield.** Scratch drag at 0.3 N per nail × µ 0.5–1.0 is 0.15–0.3 N per nail, ~0.5–0.9 N per hand. The wrist detent (two D41 magnets with a 0.3–0.6 mm printed shim, cup-registered, tuned to break at 0.8–1.2 N measured at the tips) holds the palm rigid in normal scratching; a snag adds to the drag and breaks the detent, after which the palm swings freely 15 mm in the stroke direction against a TPU bumper. Breaking force falls off steeply with gap, so the residual tangential force on a caught strand after release is ~0.1–0.2 N [EST]. A lever microswitch sees the swing → firmware reflex: lift tendon, stop yoke (never reverse, H-5.9). This is yield at the *hand* level, not 0.15 N per element (checklist item 7 = 1, see §2e). The yoke drive's goal-current register is the electrical second layer (set to ~2 N at the tip); hair protection does not depend on it.

**Compliance summary.** Normal: 0.4 N/mm per nail for 8 mm, then constant-force float for 20 mm (effective stiffness ~0 over the float range), then hard stop. Tangential: rigid to ~1 N, then ~free for 15 mm. Across curvature: 2.2 mm pre-curve + leaves.

### 2e. Hair safety — self-score and exclusion-zone inventory

Exclusion volume: everything within 30 mm of the scalp (design basis 2–8 cm hair). Items inside it, with method:

| Item inside 30 mm | Type | Exclusion method |
|---|---|---|
| Three tip-A blades + 28 mm drafted stems | static elements | smooth convex, draft ≥ 10°, no re-entrant features, R ≥ 0.5 mm edges, press-on nail CA-bonded into a pocket with ≥ 1 mm fillet (H-4.3, H-4.4) |
| Guard shell underside (at 28 mm) | static surface | convex PETG, vapour-smoothed/sanded, edge R ≥ 2 mm, standoff > pile; three pass-throughs 3.5 mm clear all round with the stem widening *inside* the shell (H-6.3) |
| TM1 pocket seam | static seam, at 28–30 mm | sits at the pass-through plane; covered by a 1 mm TPU 95A sleeve stretched over the pocket mouth (H-4.4 sealed/sleeved); tool-free |
| Nothing else | — | leaves, TM1 magnets, wrist detent, load cell, parallelogram bearings, tendon, lift servo horn are all ≥ 35 mm above the skin *and* inside the closed carrier/guard shell; the yoke pivots are 65 mm from the ear canal behind fixed side shields; no belt, no lead screw, no continuous rotation anywhere on the machine |

| # | Checklist item (hair-interaction §6.8) | Gating | Score | Note |
|---|---|---|---|---|
| 1 | No exposed continuous rotation in zone | Y | 2 | servo horns rotate < 90°, 100 mm above skin |
| 2 | Every joint in zone has an exclusion method | Y | 2 | no joints in zone; seam sleeved |
| 3 | No changing gap, no 40 µm–3 mm gap within 25 mm | Y | 2 | pass-throughs 3.5 mm open; sleeve seals the pocket |
| 4 | Lift before every reversal | Y | 2 | tendon lift is in the stroke primitive; one-direction pattern with lifted return |
| 5 | Elements in canopy move as a rigid group | Y | 2 | one palm; leaves move radially only, spacing fixed |
| 6 | Radiused blade, drafted root, no re-entrants | Y | 2 | tip A per spec |
| 7 | Compliant mount yields ≤ 0.15 N tangential | Y | 1 | hand-level detent ~1 N then free; per-element 0.15 N not met; snag-yield test with 15 g and 50 g tethers decides |
| 8 | Protrusion ≥ 25 mm | | 2 | 28 mm |
| 9 | Tip spacing ≥ 8 mm | | 2 | 20 mm |
| 10 | Low-friction polished sliding surfaces, no silicone/TPU | | 2 | ABS/nylon blades, sealed PETG stems; TPU sleeve is above canopy |
| 11 | Breakaway 3–5 N, no tether | | 2 | TM1 magnet 4–8 N (tune to 5); hand module detaches from float at ~5 N (D61 pair) with a 50 mm leash *above the guard* |
| 12 | Hair-shedding guard with drafted pass-throughs | | 2 | |
| 13 | With-grain bias and grain map | | 2 | stroke direction is set per lane/region by hand facing + sweep sign; firmware stores the map |
| 14 | Dwell/repetition limits | | 2 | ≤ 8 strokes per ±15 mm then start-angle shift ≥ 20 mm; no stationary loaded dwell > 1 s |
| 15 | Snag reflex = lift and retract | | 2 | load cell drop/spike, yoke current, wrist switch → lift + stop |
| 16 | Antistatic | | 1 | aluminium frame grounded, ABS nails; no dissipative tip in SP1 (CF-nylon stems are an option) |
| 17 | Tool-free removal of zone parts | | 2 | hand module pulls off its magnet; guard shell snaps off; tips magnet-out |
| 18 | States tolerated hair variants | | 2 | see below |
| | **Total** | | **33/36** | no gating 0 |

Hair variants: **short/medium straight-wavy (design basis): tolerated.** **Buzz cut:** tolerated (easiest). **Coarse:** tolerated with +40 g dead weight and the R 0.6 tip B comparison. **Long (> 15 cm):** NOT tolerated in SP1 — strands could reach the yoke pivots and the carrier housing from the side; would need full side shields and a closed carrier skirt. **Curly/coily:** out of scope (hair doc §1.9).

### 2f. Safety — 13 red lines, e-stop, fail-safe, release

| Red line | Status | How |
|---|---|---|
| 1 No exposed rotation/open slot within 30 mm of hair | Pass | nothing rotates below 100 mm; no slots; pivots 65 mm from ear behind fixed shields |
| 2 Normal force bounded by a mechanical constant ≤ 2.5 N | Pass | dead weight, post capacity 140 g → 2.0 N total; measured on the kitchen scale with the hand pushed to its stop |
| 3 ≤ 12 N total; ≤ 2 N tangential before yield | Pass | 2.0 N total; wrist detent ~1 N; TM1 magnet 4–8 N axial backstop |
| 4 NC e-stop in series with motor power, within reach; hold-to-run for staged tests | Pass | 22 mm NC mushroom on the desk at the right hand → foot pedal (hold-to-run) → **forehead-pad dead-man microswitch** → 12 V motor rail; OpenRB-150 logic on USB stays alive |
| 5 No mains in enclosure, ≤ 24 V, no lithium | Pass | Mean Well GST60A12 12 V 5 A certified brick; nothing else |
| 6 No moving element anterior to hairline / within 25 mm of ear / above eyes unguarded | Pass | −45° hard stop keeps tips ≥ 20 mm behind the hairline; yoke arms 65 mm from the ear canal, 45 mm from the pinna, with fixed acrylic side shields; nothing in front of the eyes (the forehead bar is fixed and padded) |
| 7 No self-locking drive in the force path without downstream spring cap and spring-return lift | Pass with argument | XL430s are non-back-drivable but are not in the normal-force path: the sweep servo acts tangentially through the wrist detent (yields ~1 N), and the lift servo can only *reduce* force. The normal path is gravity → float → leaves. Spring-return lift on power loss is *not* provided (see red line 8) |
| 8 De-energised state is lifted-off or limp | Pass as "limp", with an optional strict mod | On any cut, the yoke stops (balanced, does not fall), the lift servo holds its last position, and the hand either stays lifted or rests on the scalp at ≤ 2.0 N with 20 mm of free travel — no actuator holds force, and the head withdraws forward/down unobstructed in < 1 s (safety §5 principle 5). **Strict option (if the Safety Gate requires lifted-off):** a 12 V holding electromagnet (door-latch type, ~$6) clamps a lift-stage latch down against a 1.5 N extension spring; the latch's travel ends on a hard stop so it never adds scalp force; power loss releases the magnet and the spring lifts the hand 25 mm in ~50 ms. Adds ~2 h and $8 |
| 9 No push-fit-only, bare PLA or brittle tips; proof-loaded 3× | Pass | TM1 magnet + pocket walls; ABS/nylon blades; proof 6 N normal / 4.5 N lateral per tip before use |
| 10 Head mount release ≤ 3 s, no chin strap, ≤ 500 g | N/A → Pass | nothing on the head; release = withdraw |
| 11 Skin-accessible edges ≥ 1 mm; tips ≥ 0.4 mm or tape test | Pass (tip A is 0.3 mm by spec — tip-interface vs safety disagree) | we build tip A (0.3) *and* tip B (0.6); tape sharpness test on every tip and on the guard; first scalp sessions with tip B, A only after B is characterised |
| 12 First session only after checklist, wig-head test, glasses, ≤ 5 min | Pass | staged plan in §2i |
| 13 Firmware never the sole barrier for S ≥ 3 | Pass | every S ≥ 3 hazard has a mechanical or hard-electrical control above |

Other hazards: pinch points — the parallelogram links and the yoke/frame gaps are either < 4 mm or > 25 mm (ISO 13854 finger value); the yoke arms vs. the fixed uprights could pinch a hand at the extremes of travel → side shields cover that zone. Yoke stall: StallGuard-like detection via XL430 current → cut and lift. Head movement: the dead-man opens on a 10 mm head lift; lateral head motion (±15 mm) is absorbed by the leaves and the float's roll freedom; larger motion breaks the wrist detent; the KE of the yoke is ≤ 42 mJ. Thermal: XL430 bodies are 100–180 mm from skin. Noise: both servos enclosed in printed muffs with 3 mm foam; forehead bar isolated from the drive frame by rubber-washered clamps so skull conduction is avoided (risk 5, §2j); target ≤ 60 dBA at the ear.

### 2g. Adjustability

| Variable | Range | How |
|---|---|---|
| Normal force | 0.2–2.0 N total (0.07–0.65 N per nail) | **knob-equivalent:** 20 g slugs on the post; trim spring hook; tendon partial-unload in firmware (reduce only); readout from the load cell on the OLED |
| Speed | 20–200 mm/s | pot → firmware |
| Stroke | 15–140 mm | pot → firmware |
| Frequency | 1–2.5 Hz (coupled to stroke/speed) | firmware |
| Attack angle | 35° / 45° / 55° | three printed TM1 holders (tip-interface §5.2); hand pitch shim ±5° |
| Contacts | 1 / 2 / 3 | remove tips, plug pockets |
| Spacing | 20 mm (16 and 24 mm palms are 20-minute reprints) | reprint |
| Pattern | P1 lift-return, P2 sweep, pauses, region changes, jitter on/off, fully periodic control | firmware; three pots + one mode button + OLED |
| Direction vs hair lie | with / against (by hand facing + sweep sign); cross-grain by hand yaw ±20° (coarse) | manual remount, 30 s |
| Region | three lanes × head tilt (top / crown-occiput / nape) | manual, 1 min |
| Tip | A–H via TM1 | 10 s swap |
| Twin-palm (SP1 option B) | bidirectional P1 | second palm facing the other way on the same float, cam on the lift servo selects which palm is down; +$15, +3 h |

Priority order (scratch-model §7): pattern irregularity (1) and penetration/force (2, 3) are the knob-level variables; velocity (4) and edge (5) next; contact count (6) and compliance (7, spring-steel thickness swap) are fast swaps.

### 2h. Components (rough BOM)

| Qty | Item | Unit | Ext. | Source |
|---|---|---|---|---|
| 2 | Dynamixel XL430-W250-T (sweep, lift) | $49.90 | $99.80 | Trossen / robotis.us |
| 1 | OpenRB-150 | $28.64 | $28.64 | robotis.us |
| 1 | Mean Well GST60A12-P1J 12 V 5 A | $19.40 | $19.40 | Mouser/DigiKey |
| 1 | 22 mm NC mushroom e-stop (boxed) | $12 | $12 | Amazon |
| 1 | Momentary foot pedal switch (~unverified) | $10 | $10 | Amazon |
| 1 | Lever microswitch 16 A (dead-man under forehead pad) (~unverified) | $3 | $3 | Amazon |
| 1 | INA219 | $9.95 | $9.95 | Adafruit |
| 1 | 1 kg bar load cell + HX711 | $10 | $10 | Amazon/SparkFun |
| 1 | FSR 402 (optional, pad-pressure log) | $7 | $7 | Adafruit |
| 2 | 2020 extrusion 4 × 500 mm packs (frame 6 pcs + yoke 3 pcs) | $28 | $56 | Amazon |
| 1 | 2020 corner-bracket/T-nut kit (40 sets) | $15 | $15 | Amazon |
| 1 | 8 mm hardened rod 300 mm (cut to two 60 mm stubs) | $10 | $10 | Amazon/McMaster |
| 1 | 608ZZ 10-pack | $8 | $8 | Amazon |
| 1 | 623ZZ 10-pack (parallelogram, wrist) | $7 | $7 | Amazon |
| 1 | Feeler-gauge set (0.4/0.5 mm spring-steel leaves) (~unverified) | $8 | $8 | Amazon |
| 1 | Extension/compression spring assortment | $12 | $12 | Amazon |
| 10 | K&J D41 + 2 × D61 magnets, steel washers | — | $9 | K&J, Amazon |
| 1 | Dyneema 50 lb line | $8 | $8 | Amazon |
| 1 | Press-on nail pack + Tortex 1.14 picks | — | $16 | Amazon |
| 1 | M3/M5 hardware assortment + heat-set inserts | — | $29 | Amazon |
| 1 | Pots ×3, OLED, JST/wire kit, fuse holder + fuses, rocker switch | — | $35 | Amazon/Adafruit |
| 1 | EVA closed-cell pad, 2 C-clamps, rubber washers | — | $18 | hardware store |
| 1 | 1 kg counterweight (steel washers or a 1 kg plate) | $8 | $8 | Amazon |
| 1 | Acrylic/PETG sheet for side shields (~unverified) | $12 | $12 | Amazon |
| 1 | Printed parts ≈ 300 g PETG + 20 g TPU (library ~$30; JLC3DP $40–60) | — | $40 | library / JLC3DP |
| 1 | Cosmetology mannequin head (human hair) + clamp | — | $43 | Amazon |
| | **Total** | | **≈ $535** | |

Budget substitute: 2 × Feetech STS3215-12V ($24 ea) + Waveshare Servo Driver with ESP32 ($16) in place of the Dynamixels and OpenRB → **≈ $470**, with Wi-Fi tuning from a phone. Stack C (GM3506 + SimpleFOC) at the sweep pivot is a +$60 smoothness experiment for SP2 — direct drive, silent, back-drivable, torque ∝ current, which would also satisfy red line 7 outright.

Printed parts (PETG unless noted; approximate envelope):

| Part | Qty | Size (mm) | Notes |
|---|---|---|---|
| Pivot pillow block (608ZZ seat) | 2 | 45 × 45 × 28 | bolts to drop bar; bearing lip shields |
| Yoke hub (8 mm shaft clamp → 2020 arm) | 2 | 45 × 35 × 30 | one has the XL430 horn pattern |
| Servo mount, sweep (XL430 to drop bar) | 1 | 60 × 45 × 35 | |
| Hard-stop ring + bosses | 1 + 2 | Ø 70 × 8 | 5° index holes |
| Counterweight holder | 2 | 60 × 40 × 20 | |
| Carrier housing (crossbar clamp, upper link pivots, tendon guide, servo mount) | 1 | 95 × 65 × 55 | closed on all sides but the bottom |
| Parallelogram links (623ZZ both ends) | 2 | 50 × 12 × 8 | 30° inclined geometry set by housing |
| Load-cell adapters | 2 | 40 × 20 × 8 | |
| Wrist plate with magnet cups + swing stop (TPU bumper) | 1 | 60 × 30 × 12 | |
| Dead-weight post | 1 | Ø 8 × 50 | 20 g slugs = M8 washers |
| Palm, R 90 and R 75 variants | 2 | 70 × 30 × 22 | three leaf clamps, pre-curved pocket heights |
| TM1 holder (pocket + leaf clamp), 35/45/55° | 3 + 6 | 16 × 12 × 20 | print pocket opening up |
| Finger stem with TM1 tang and nail pocket | 6 | 30 long, 14 → 6 taper | sealed (UV resin or vapour), bright colour |
| TPU 95A seam sleeve | 4 | Ø 14 × 10, 1 mm wall | |
| Guard shell (convex, 3 pass-throughs) | 2 | 95 × 55 × 30 | sanded, sealed; snaps on |
| Forehead pad carrier with microswitch pocket | 1 | 140 × 50 × 22 | |
| Servo muffs | 2 | 70 × 60 × 50 | foam lined |
| Side shields (if printed instead of acrylic) | 2 | 200 × 150 × 3 | |

### 2i. Buildability in an apartment

**Tools:** hex keys, calipers, hacksaw + mitre box (2020 cuts; or buy cut-to-length), files/sandpaper, soldering iron (Pinecil), multimeter, hot glue/CA/threadlocker, kitchen scale, luggage scale, phone (slow-mo, SPL). Nothing beyond component-landscape §8.

**Steps (≈ 30 h over two weeks, printing in parallel):**
1. Frame (3 h): cut 2020: base 400 × 400, uprights 2 × 600 at ±250 mm, top beam 540, drop bars 2 × 150 ending at ear height, forehead bar 300 slotted for height/tilt. Clamp to the desk; sit; set pivot height to ear height with the chair.
2. Pivots (3 h): press 608ZZ into pillow blocks; fit 8 mm stubs; mount the XL430 on the left drop bar with its horn coupled to the left stub hub; right stub is a free bearing. Check both stubs are coaxial to ±1 mm with a straightedge across the yoke hubs (the printed hubs forgive ±1 mm; beyond that the yoke binds — the one alignment that matters).
3. Yoke (2 h): arms + crossbar; counterweights; balance by hand so the yoke stays put at any angle (residual < 0.1 N·m = it drifts slowly, not swings). Fit hard-stop bosses at −45°/+115°.
4. Hand (6 h): clamp leaves into the palm, fit TM1 holders, bond press-on nails into stems (CA + pocket), file edges to R 0.3/0.6, sand and seal stems, sleeve the pockets; magnet detent in the wrist; load cell between float and wrist; parallelogram into the carrier; dead-weight post. Measure: leaf stiffness on the kitchen scale (target 0.4 N/mm), float force vs. slugs (0.6–2.0 N), detent break force at the tips (0.8–1.2 N), TM1 pull-out (4–8 N).
5. Lift (2 h): XL430 on the crossbar, 25 mm horn, Dyneema to the float; set horn zero so the tendon is slack with the hand at the −10 mm float position.
6. Electronics (4 h): 12 V brick → 3 A blade fuse → e-stop (NC) → foot pedal → dead-man microswitch → OpenRB-150 servo rail; INA219 on the rail; HX711, three pots, OLED, mode button on the OpenRB; USB to laptop for logging. Verify 0 V on the rail with each of the three contacts open.
7. Firmware (6 h): limits table; trapezoid sweeps with lift/lower interleave; PATTERN SPEC v1 subset; load-cell logging at 80 Hz to CSV; snag reflex; watchdog; soft-start; 20-min timeout.
8. Bench (4 h): mannequin head on the rig; hair-interaction §7.3 tests 1–9 (static press, drag, 50 reversals with/without lift, wrap, gap probe with 100 µm line, 15 g/50 g tether snag-yield, 20-min endurance, static); force vs. yoke angle log; noise.

**Risky tolerances:** pivot coaxiality ±1 mm (fixable with slotted blocks); TM1 pocket 10.3 × 4.3 (print test coupons first); leaf clamp (shim to taste); magnet detent gap (shims 0.1–0.6 mm, measure, do not calculate); tendon zero (slack at rest or the lift servo steals dead weight — the load cell shows it instantly).

### 2j. Honest weaknesses, top 5 risks, retiring tests

Weaknesses: (1) no side/temple coverage without re-rigging; (2) no independent fingers, so P4 "spider" and true per-finger asynchrony are absent; (3) one stroke direction per setup unless the twin-palm module is built; (4) the forward-lean posture and the cage look — Michael is "in a device" for 20 min; (5) 3–4 Hz cycles are out of reach with a servo-tendon lift; (6) dead-weight force varies with yoke angle (cos θ) and must be trimmed; (7) no fail-lift without the electromagnet mod.

| # | Risk | Likelihood / impact | Bench test that retires it |
|---|---|---|---|
| 1 | Dead-weight force drifts with angle and parallelogram friction, so the "mechanical constant" is 0.6–1.0× the setting | high / medium | load-cell log vs. yoke angle with the mannequin at three dead-weight settings; pass if F within ±15% over ±45° after trim; else add the constant-force spring (Vulcan 0.25 lb) in parallel |
| 2 | One-direction rake with lifted return reads as "sweeping," not "scratching" | medium / high | hand-wand A/B on Michael's scalp: 20 s bidirectional P1 vs 20 s lift-return P1 at the same force; if bidirectional wins clearly, build the twin-palm module before the first machine session |
| 3 | Lift latency (tendon + XL430) limits P1 to ≤ 2 Hz and the lift is audible/jerky | medium / medium | slow-mo timing of tip-off-skin vs. command; pass if 5 mm lift ≤ 50 ms; else shorter horn radius, XL330-M077 on a 5 V buck, or the electromagnet release (≈ 20 ms) |
| 4 | Skull-conducted servo noise/vibration through the forehead bar makes it "a machine" | medium / high | SPL at the ear + subjective with the bar isolated vs rigid; pass if ≤ 60 dBA and no felt buzz; else rubber isolation, muffs, Stack C gimbal motor at the pivot |
| 5 | Head mis-centering/motion changes attack angle and force enough to catch hair (checklist 7 at 1) | medium / high | mannequin offset ±15 mm in x/y/z and tilted ±10°; 50 g tether snag-yield at 150 mm/s; wig-head 20-min run with hair pushed into pass-throughs; pass = zero captures, tether never lifts |

### 2k. Massager-vs-scratcher self-score (scratch-model §8)

| # | Item | Score | Evidence |
|---|---|---|---|
| 1 | Edge, not pad | PASS | tip A/B, ABS/nylon, R 0.3/0.6, 6 mm loaded edge |
| 2 | Reaches the skin | PASS | 28 mm protrusion, float to skin, ≤ 0.3 N per nail; fraction-in-contact [UNKNOWN] until the mannequin side-photo test |
| 3 | Light | PASS | 0.07–0.65 N per nail, 2.0 N total hard cap; force is set by the dead weight, not by head weight or strap tension |
| 4 | Slides | PASS | 15–140 mm sliding per stroke; scalp displacement < 1 mm at these loads |
| 5 | Right speed band | PASS | 20–200 mm/s, 1–2.5 Hz; no component > 6 Hz |
| 6 | Deflects hair near the root | PASS | edge on skin; parts the canopy |
| 7 | Multiple independent contacts | PASS/UNSURE | 3 at 20 mm, individually sprung with shimmed preloads; not independently driven — spread ≥ 20 ms / ≥ 20% is by compliance and curvature, to be measured |
| 8 | Irregular | PASS | per-stroke resampling, pauses, lifts, region jumps; periodic control mode included |
| 9 | Compliant at the tip | PASS | 0.4 N/mm × 8 mm + constant-force 20 mm float; < 0.3 N per mm of surface error |
| 10 | Unloads at reversal, lifts between bouts | PASS | tendon lift at every stroke end; full clearance at region changes |
| 11 | Hair-safe geometry | PASS | no rotation/aperture within reach |
| 12 | Sounds like a scratch | UNSURE | nail-on-hair hiss present; servo noise isolation to be measured |

Sanity check against scratch-model table 1.2: contact element = hard keratin-like edge R 0.3 mm, 6 mm line; 0.2–0.65 N per contact; 100–200 kPa line pressure; < 1 mm scalp translation; 15–140 mm sliding; 20–200 mm/s; 1–2.5 Hz; parts canopy. Every row lands in the first column.

---

## 3. Schematic — CRADLE side view (left side of the head; front is to the left)

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 780 620" width="780" height="620" font-family="Helvetica, Arial, sans-serif" font-size="12">
  <!-- sweep envelope -->
  <path d="M 217 307 A 230 230 0 0 1 588 567" fill="none" stroke="#999" stroke-width="1" stroke-dasharray="6 4"/>
  <text x="150" y="300" fill="#666">-45° hard stop (top)</text>
  <text x="560" y="590" fill="#666">+115° hard stop (nape)</text>
  <!-- head -->
  <circle cx="380" cy="470" r="144" fill="#fdf1e4" stroke="#333" stroke-width="2"/>
  <text x="350" y="480" fill="#333">head (R 90)</text>
  <!-- hair canopy -->
  <path d="M 236 470 A 144 144 0 0 1 524 470" fill="none" stroke="#8a5a2b" stroke-width="1" stroke-dasharray="2 3" transform="translate(0,-24)"/>
  <g stroke="#8a5a2b" stroke-width="1">
    <line x1="300" y1="352" x2="296" y2="330"/><line x1="320" y1="340" x2="318" y2="318"/><line x1="340" y1="332" x2="340" y2="310"/>
    <line x1="420" y1="332" x2="424" y2="310"/><line x1="440" y1="340" x2="446" y2="318"/><line x1="460" y1="352" x2="468" y2="330"/>
  </g>
  <text x="520" y="318" fill="#8a5a2b">hair canopy (pile 5–20 mm)</text>
  <!-- pivot axis -->
  <circle cx="380" cy="470" r="6" fill="#fff" stroke="#000" stroke-width="2"/>
  <circle cx="380" cy="470" r="1.5" fill="#000"/>
  <text x="392" y="500" fill="#000">yoke pivot axis ⊙ (ear height, bearings outboard ±140 mm, XL430 at left pivot)</text>
  <!-- yoke arm (behind head, outboard) -->
  <line x1="380" y1="470" x2="380" y2="130" stroke="#555" stroke-width="5" stroke-dasharray="10 6"/>
  <text x="392" y="200" fill="#555">yoke arm 2020 (outboard of head)</text>
  <!-- crossbar -->
  <rect x="300" y="116" width="200" height="14" fill="#bbb" stroke="#333"/>
  <text x="505" y="128" fill="#333">crossbar (R 175)</text>
  <!-- sweep arrow -->
  <path d="M 250 150 A 300 300 0 0 1 510 150" fill="none" stroke="#000" stroke-width="1.5"/>
  <polygon points="510,150 500,140 497,152" fill="#000"/>
  <polygon points="250,150 260,140 263,152" fill="#000"/>
  <text x="300" y="100" fill="#000">sweep 20–200 mm/s, stroke 15–140 mm</text>
  <!-- lift servo -->
  <rect x="408" y="80" width="46" height="36" rx="3" fill="#dde" stroke="#333"/>
  <text x="460" y="96" fill="#333">lift servo XL430</text>
  <text x="460" y="110" fill="#333">(tendon: pull-up only)</text>
  <circle cx="416" cy="112" r="5" fill="none" stroke="#333"/>
  <line x1="416" y1="117" x2="416" y2="232" stroke="#06c" stroke-width="1.5" stroke-dasharray="4 3"/>
  <text x="422" y="190" fill="#06c">Dyneema tendon</text>
  <!-- carrier housing -->
  <rect x="330" y="130" width="100" height="42" rx="4" fill="#eee" stroke="#333"/>
  <text x="200" y="150" fill="#333">carrier housing (closed)</text>
  <!-- parallelogram links, inclined 30° -->
  <line x1="345" y1="172" x2="365" y2="226" stroke="#333" stroke-width="3"/>
  <line x1="395" y1="172" x2="415" y2="226" stroke="#333" stroke-width="3"/>
  <circle cx="345" cy="172" r="3" fill="#fff" stroke="#333"/><circle cx="395" cy="172" r="3" fill="#fff" stroke="#333"/>
  <circle cx="365" cy="226" r="3" fill="#fff" stroke="#333"/><circle cx="415" cy="226" r="3" fill="#fff" stroke="#333"/>
  <text x="200" y="200" fill="#333">parallelogram float, 20 mm,</text>
  <text x="200" y="214" fill="#333">inclined 30° (lift up-and-forward)</text>
  <!-- dead weight -->
  <line x1="440" y1="232" x2="440" y2="190" stroke="#333" stroke-width="2"/>
  <rect x="432" y="190" width="16" height="18" fill="#888" stroke="#333"/>
  <text x="452" y="204" fill="#333">dead weight 0–140 g (F ≤ 2.0 N)</text>
  <!-- load cell -->
  <rect x="356" y="226" width="60" height="12" fill="#cfc" stroke="#333"/>
  <text x="200" y="236" fill="#333">1 kg bar load cell</text>
  <!-- wrist detent + palm -->
  <rect x="332" y="238" width="112" height="22" rx="3" fill="#ddd" stroke="#333"/>
  <rect x="338" y="243" width="8" height="5" fill="#c33"/><rect x="348" y="243" width="8" height="5" fill="#33c"/>
  <text x="452" y="254" fill="#333">wrist magnetic detent (~1 N) + palm</text>
  <!-- leaf spring -->
  <line x1="348" y1="258" x2="392" y2="263" stroke="#0a0" stroke-width="2"/>
  <text x="200" y="262" fill="#0a0">leaf 0.4 N/mm × 8 mm (one of three)</text>
  <!-- guard shell -->
  <path d="M 322 262 Q 322 296 350 300 L 426 300 Q 454 296 454 262 Z" fill="#f7e9c8" stroke="#333" stroke-width="1.5"/>
  <text x="458" y="290" fill="#333">hair-shedding guard, 28 mm above skin,</text>
  <text x="458" y="304" fill="#333">pass-throughs 3.5 mm clear</text>
  <!-- finger stem + nail -->
  <polygon points="370,282 392,282 404,322 398,326" fill="#f4c" stroke="#333" stroke-width="1.2"/>
  <line x1="398" y1="326" x2="406" y2="328" stroke="#000" stroke-width="2.5"/>
  <text x="200" y="330" fill="#333">tip A on 28 mm drafted stem,</text>
  <text x="200" y="344" fill="#333">45° attack, edge leads →</text>
  <!-- float travel marker -->
  <line x1="470" y1="306" x2="470" y2="340" stroke="#06c" stroke-width="1"/>
  <text x="474" y="326" fill="#06c">float ±10 mm</text>
  <!-- forehead rest -->
  <rect x="196" y="430" width="30" height="80" rx="6" fill="#cfe" stroke="#333"/>
  <rect x="226" y="455" width="12" height="30" fill="#8cc" stroke="#333"/>
  <text x="60" y="456" fill="#333">forehead pad (EVA)</text>
  <text x="60" y="470" fill="#333">+ dead-man microswitch</text>
  <text x="60" y="484" fill="#333">in the 12 V motor rail</text>
  <!-- exit arrow -->
  <path d="M 300 570 L 260 600" stroke="#000" stroke-width="1.5" fill="none"/>
  <polygon points="260,600 270,598 263,590" fill="#000"/>
  <text x="270" y="612" fill="#000">exit: chin down, slide back (away from yoke)</text>
  <!-- legend -->
  <text x="20" y="30" font-size="13" font-weight="bold">CRADLE — side view, yoke at 0° (crown). Not to scale (head R 90 mm shown at 1.6 px/mm).</text>
  <text x="20" y="48" fill="#444">Force path: dead weight → load cell → wrist detent → leaf → TM1 → tip. Tendon can only lift. Yoke sweeps about the head centre, so radius and attack angle are constant.</text>
</svg>

---

## 4. What CRADLE answers that nothing simpler would

It is a research rig first: the load cell gives the force–pleasure curve (scratch-model §9 Q3) directly; the yoke gives speed (Q2), stroke and direction-vs-lie (Q7) as pots; TM1 gives edge geometry (Q6) in 10 s; the fully periodic control mode gives the predictability penalty (Q5); contact count (Q4) is tip removal. Mode 0 (CAT-POST) answers Q1 (skin contact necessity) by stepping the float stop before any motor turns. If the first human session says "sweeps are not scratches," the twin-palm module makes it bidirectional for $15; if it says "I want fingers," W1 RESTING HAND bolts to the same crossbar.
