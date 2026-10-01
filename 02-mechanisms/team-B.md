# TEAM B — Servo-Articulated Independent Fingers ("robot hand")

**Project SCRATCH · 02-mechanisms · Team B · 2026-10-01**
**Seed family:** 3–5 independently driven fingers, each with 1–2 DOF, SP1-TM1 tips on spring-capped compliant holders.
**Inputs used:** BRIEF.md, scratch-model.md (§1–3, 4.4, 7, 8), hair-interaction.md (H-4.x/5.x/6.x, §6.8 checklist), safety-requirements.md (13 red lines, §3.1 force-cap principle), tip-interface.md (SP1-TM1, tip family A–H), component-landscape.md (parts and prices). No other team file and no prior-art file was read.

---

## 0. Framing: what a "finger" has to do, in this family's terms

A servo finger is attractive because it is the only family in which **every sensation-critical variable ranked 1–10 in scratch-model §7 is a firmware or spring parameter** — phase jitter, stroke length, speed, pauses, lift-offs, region wander, force (preload and lift height), contact count. Its cost is what the brief warns about most: a position-controlled servo pushes to stall unless something downstream yields. So the design questions for this family are: (1) where the compliance and the hard force cap live (in the finger, never in the current register alone); (2) how to lift off at every reversal (H-5.2 is gating; a pivot finger reciprocating in contact is the textbook loop-former of hair-interaction §3.4); (3) how to keep horns, hubs and sliding joints out of the 30 mm exclusion volume while reaching skin through a 5–20 mm pile; (4) how to make four servos not feel like a machine. Each concept is judged on those four first, cost and weight second.

---

## 1. Concepts in the seed family (and one wildcard)

### B-1 "Claw": 2-DOF two-link fingers (3 fingers × 2 servos)

Each finger is a planar two-link chain — a proximal link ("MCP") driven by one XL330 and a distal link ("PIP") driven by a second XL330 riding on the first — moving in a plane normal to the scalp. The tip can trace any closed path: a flat 30–50 mm stroke, a curling 15–20 mm lift, a fast air return, a soft landing. It is the most human-like kinematics available and the only concept that does the P4 "spider" properly, since every finger has its own lift. Costs: six servos ($165) for three fingers; the distal servo is moving mass (18 g, pushing the finger over the 30 g limit unless tendon-driven from the palm); two pivots per finger, with the knee at 40–50 mm above the scalp needing a shroud; and a two-joint force cap that must be verified for every joint combination. Verdict: the SP2 finger if the sensation gate says per-finger lift matters; too heavy and too jointed for the first head-worn rig.

```
   palm ─┬─[S1]            S1: MCP sweep servo (on palm)
          \                S2: PIP curl servo (on link 1)
           \ link 1
            \
            [S2]╮
                 \ link 2
                  \
                  [TM1 holder + spring]
                     \_ nail  → path: ──── flat stroke ────╮
   ~~~~~~~~~~~~~~ scalp ~~~~~~~~~~~~~~~~~~~~~~~    air return ╰──
```

### B-2 "Pendulum Hand": 4 single-pivot fingers + 1 shared palm lift  ← SELECTED

Four fingers hang like pendulums from four sweep servos whose axes are parallel to the scalp and perpendicular to the stroke. Each finger swings in its own plane, so the four tips run on four parallel tracks 22 mm apart and can never touch (H-5.6). Lift-off is a separate, shared DOF: the whole palm (the plate carrying the four sweep servos) rocks about a hinge driven by a fifth servo, raising all four tips 15 mm clear of the canopy at every reversal. Five servos, one bus, ~440 g on the head. The pendulum geometry gives three things for free: a natural rise of the tip at the stroke ends (3.7 mm at ±18°, which helps H-5.3's "lift while still moving"), a nail attack angle that sweeps from ~63° at entry to ~27° at exit like a finger flattening through its stroke, and a hub 80 mm above the scalp, far outside the exclusion zone. Developed in §2.

```
                  [S1][S2][S3][S4]  sweep servos on palm plate (axes ⟂ page)
   lift ─[S5]──hinge━━━━━━━━━━━━━━━━━┓ palm
                     │   │   │   │   ┃
                     │   │   │   │   ┃   fingers (pendulums, 22 mm pitch)
      guard ───────┄┄┼┄┄┄┼┄┄┄┼┄┄┄┼┄┄┄     (windows, ≥3 mm clearance)
                     ▽   ▽   ▽   ▽       TM1 sleeve + spring + nail
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ scalp
```

### B-3 "Cam-lift finger": 4 single-servo fingers with a face cam at the hub

Same pendulum fingers as B-2 but no lift servo: each hub rides on a stationary V-shaped face cam printed into the servo mount, so that past ±12° of swing the finger is pushed axially up its own pin, lifting the tip 10 mm by ±18°. Lift-off at every reversal is mechanical, with one servo per finger ($110, ~380 g), and the fingers are fully independent. Its faults are structural: the contact fraction of every stroke is fixed by the cam (short ±10° strokes never lift, so H-5.2 holds only at full amplitude); the finger cannot park lifted mid-stroke, so pauses and soft landings (P5, P6) are impossible; and the cam puts an axial thrust on the servo's output bearing. Verdict: an excellent kinematically-fixed control rig (scratch-model §8 item 8) and the fallback if the five-servo mass budget fails. Not the research rig.

```
   stationary V-cam ramp ╲        ╱   hub rides up the ramp at |θ|>12°
                 [S]──────╲──┬──╱
                           ▼ finger axis moves up as it swings out
                     ╱───┼───╲    tip path: ∪  (lifted at both ends)
   ~~~~~~~~~~~~~~~~~~~~ scalp ~~~~~~~~~~~~~~
```

### B-4 "Flat wiper": vertical-axis arms (explored and rejected)

Four wiper arms with servo axes normal to the scalp, each 40 mm long, sweeping ±35° parallel to the surface: zero arc rise, so force stays constant without lift compensation. It fails on layout. An arm longer than the finger pitch must either overlap its neighbours' hubs (finger 3's hub sits where finger 1's tip is) or be stacked at four heights with four stem lengths; and if the arms sweep laterally instead, adjacent ±23 mm tracks cross and out-of-phase tips collide (H-5.6). The only non-colliding version has arms ≤10 mm and ±17 mm strokes — too short for P1. Rejected; recorded so the tournament does not re-propose it.

### W-1 Wildcard (outside the family): "Ouija puck" — magnetically coupled tips through a sealed shell

A closed, smooth PETG dome sits 26 mm above the scalp. On the hair side, free pucks (one per nail) each carry a TM1 sleeve/spring/nail pointing down and a steel disc pointing up; on the dry side, servo-driven magnet carriages drag the pucks through the 2 mm shell. No joint, gap or shaft exists on the hair side: the puck is a convex blob riding on three polished PTFE domes against the shell. Lift-off is a second magnet pair that retracts the nail into the puck; a snag simply decouples the puck (1–2 N, no tether) and it drops into the hair, 8 g and bright-coloured. Why it is not a contender yet: hair that reaches between puck and shell is pressed under a sliding dome; the force setpoint is a reprint (puck spring), not a knob; and magnet lag adds 2–4 mm of hysteresis. It is the cleanest hair-safety story in the project and deserves a one-evening wig-head trial if any finger concept fails the wrap test.

```
   servo/carriage ──[magnet]──┐        above shell (dry side)
   ═══════════════════════════╪═══════  2 mm smooth PETG shell (26 mm above scalp)
                     ( steel ◉ ) puck  ← slides on 3 PTFE domes
                       ╲ spring+TM1
                        ╲_ nail
   ~~~~~~~~~~~~~~~~~~~~~~~~~ scalp ~~~~~~~~
```

**Selection.** B-2 wins because it is the only in-family concept that gives firmware control over stroke length, pauses, landings and lift timing (ranks 1, 2, 9, 14 in scratch-model §7) with one guaranteed lift per cycle (H-5.2) at five actuators and under 500 g. B-1 does more but weighs and costs more and multiplies joints; B-3 is cheaper but fixes the very variable (stroke/contact fraction) we most need to vary.

---

## 2. Selected concept: B-2 "Pendulum Hand" — concept-level engineering design

### 2a. Working principle and why it reads as fingernails

The scalp sees four things, each a row of scratch-model §1.2's first column:

- **A stiff narrow edge reaching the skin.** Tip A/B/C/F from the TM1 family (R 0.3–0.6 mm, PETG/nylon, E > 1 GPa) on a stem protruding 26 mm below the guard, so the edge is under a 5–20 mm pile with margin (H-4.5). Normal force 0.2–0.9 N per nail from a 0.2 N/mm spring at 1–4 mm compression — the 0.03–0.15 N/mm line load the tip document calls the "crisp scratch" window — with a 2.3 N hard cap.
- **Sliding, not pressing.** 30–46 mm per stroke at 50–150 mm/s, 1–2.5 Hz, with the scalp sliding under the edge (the hub breakaway makes the finger tangentially compliant, so the edge does not carry the scalp with it).
- **Hair deflected at the root.** With the edge at skin level every hair is bent at the follicle exit (the 1/L² argument of scratch-model §2.3); the sleeve above is a smooth cylinder above the pile, so nothing combs.
- **Four lines that are alive.** Four tips at 22 mm pitch on four servos start each stroke 0–60 ms apart, lengths ±25% and speeds ±20% resampled every cycle, with pauses and lift-offs; the palm lift dithers ±1 mm (±0.2 N); the stroke centre wanders ±8 mm. The periodic control condition is one flag.
- **A finger's motion.** A pendulum about a pivot 80 mm up rotates the nail ~36° through a 46 mm stroke — steep at entry (~63°), flattening to ~27° as it rises out — as a curling finger does through a rake. The first tips are real press-on nails, so the nail-on-hair hiss (component D) is genuine.

Weaker than a hand: force per finger is not individually commandable, stroke direction is set by hand per region, and strokes >46 mm (P2 sweeps) are impossible.

### 2b. Architecture

| Item | Design |
|---|---|
| Mount | Head-worn. Welding-helmet ratchet headgear ($16); its two side pivots carry printed slotted arms to a rear cross-bar from which the module hangs. The pivots rotate the module about the ear-to-ear axis from the **occiput** (default) to the **crown**. A VESA-100 adapter on the cross-bar hangs the same module from a monitor arm over the mannequin (and is the lean-in stationary option if head-mount fails). |
| Coverage per placement | 4 tracks × 46 mm ≈ 66 × 46 mm ≈ 30 cm². Region and stroke-direction changes are manual (arm rotation; 15° detent ring). Partial coverage per BRIEF §15. |
| Contacts | 4 (populate 1, 2 or 4 for the contact-count experiment). Tip pitch 22 mm. |
| DOF | 4 × sweep (XL330-M288-T, current-based position mode) + 1 × palm lift (XL330-M288-T) = 5 active; 4 × passive spring plunger (10 mm); 4 × magnetic hub breakaway; 1 × solenoid fail-safe latch on the lift link. |
| Guard | A smooth PETG plate at 26 mm standoff fixed to the frame (not to the palm), with four 60 × 18 mm windows the fingers pass through with ≥3 mm clearance in every position; removable by two magnets for cleaning. |
| Electronics | OpenRB-150 on the desk; one 3-wire tether to the head; e-stop and hold-to-run pedal in the 5 V actuator rail. |

Servo layout: the four sweep servos sit in two rows on the palm plate (fingers 1, 3 front; 2, 4 in a rear row 36 mm behind), 44 mm apart within a row, so the 22 mm tip pitch does not depend on the XL330's shaft-axis dimension. Rear-row beams are cranked 36 mm forward (effective radius 83 mm instead of 75; the 0.4 mm arc-rise difference is absorbed by the spring).

### 2c. Kinematics with numbers

**Finger.** Pivot 80 mm above the nominal scalp with the palm down. Beam 45 mm (PETG, 12→8 mm taper) → telescoping sleeve 36 mm → TM1 pocket at 45° → tip stem 20 mm → nail. Pivot-to-edge radius R = 75 mm (front row).

**Stroke.** Sweep ±18° → chord **46 mm** maximum; default P1 strokes 20–40 mm. Arc rise at ±18°: 3.7 mm; scalp curvature drop at ±23 mm: 2.9 mm (crown, R 90) to 3.8 mm (occiput, R 70); total gap change centre-to-end 6.6–7.5 mm. The lift servo runs a **feed-forward height profile** z(φ) = R(1 − cos φ) + (R sin φ)²/(2 R_scalp), R_scalp a per-region parameter, so spring compression stays within ±1.5 mm for the mean finger phase; the residual for a finger 60 ms out of phase is ≤1 mm (±0.2 N), inside the human ±30–50% force jitter and kept as a feature.

**Velocity profile.** Trapezoidal via the XL330 Profile Velocity/Acceleration registers: accelerate over the first 15% of the stroke at ≤2 m/s² (H-5.4), cruise at 50–150 mm/s (40–115°/s at the horn, trivial for a 618°/s servo), no deceleration in contact — the lift begins with the tip still at ≥60% of cruise (H-5.3). Air return up to 300 mm/s (within the 0.4 m/s cap).

**Cycle.** Default is the unidirectional rake of H-5.7: land (lift servo lowers 15 → 0 mm over 150 ms while the sweep is already moving, plough-in ≈30°) → stroke (finger i starts at t₀ + δᵢ, δᵢ ~ U(0, 60 ms); Lᵢ ~ N(30 mm, 25%); vᵢ ~ N(100 mm/s, 20%)) → lift (15 mm in 80 ms when the first finger reaches 90% of its stroke, all four still moving forward) → air return → optional lifted pause, p = 0.5, U(0.3, 2 s). Cycle 450–700 ms → **1.4–2.2 Hz**. A bidirectional mode (direction alternates after each lift) serves the against-grain experiment (≤25 mm, H-5.1).

**Lift-off geometry.** The palm hinge is 55 mm behind the finger line and 32 mm above the scalp. Rotating the palm 15° moves the tip +15.3 mm normal to the scalp and +6.4 mm forward, so lift-off overruns hair pushed ahead of the edge instead of reversing over it. The spring unloads in the first 4 mm of lift (<25 ms); H-5.2's "≥5 mm at zero force" clause is met after 9 mm and full canopy clearance at the top.

**Irregularity.** A seeded PRNG resamples every cycle: per-finger start delay, stroke length, speed, lift-height dither (±1 mm → ±0.2 N), stroke-centre wander (±8 mm mean-reverting random walk), pause probability and length, episode type (P1 60%, short-stroke P4-like 15%, P5 pauses 10%, P6 micro-region changes 15%), episodes 5–20 s. A 3-cycle history check enforces "never repeat the same tuple more than 3 cycles". A `PERIODIC` flag disables all resampling for the control condition.

**Region changes.** Within the 46 mm window: firmware. Occiput ↔ crown, or stroke direction vs. hair lie: manual (rotate the headgear arms or the detent ring, 5 s, logged). Scratch-model §5 calls those two regions the highest-value and simplest-curvature ones; that is SP1's coverage.

**Single pivot vs two-link, resolved.** B-1's second servo buys only per-finger lift timing and the P4 spider. A single pivot plus shared lift gives the same nail path (flat-ish stroke, rising exit, air return) with one joint per finger and five servos instead of six to eight; the price is that the four nails must end their strokes within ~40 ms of each other. Scratch-model §4.2 puts human within-rake asynchrony at 20–80 ms, so a 0–60 ms spread is inside the human range. "Per-finger lift matters" is deferred to SP2.

### 2d. Force path

```
servo horn ─► magnetic breakaway hub (slips at 0.5 N tangential at the tip)
          ─► PETG finger beam (rigid)
          ─► inner post ─► compression spring (k = 0.2 N/mm, 10 mm travel, preload 0.1–0.4 N, hard stop)
          ─► outer sleeve (slides on post, mouth facing UP at ≥45 mm above scalp)
          ─► TM1 pocket at 45° with N52 6×2 magnet (axial breakaway 4–8 N, no tether)
          ─► tip tang + 20 mm stem + nail
```

**Normal force.** Set by how far the lift servo holds the palm down, read as spring compression x: F = F_pre + k·x. Default F_pre = 0.3 N (threaded preload cap, 0–0.4 N), k = 0.2 N/mm, x operating 0–3 mm → **0.3–0.9 N**. Hard cap: plunger stop at x_max = 10 mm → **F_max = 0.3 + 2.0 = 2.3 N** ≤ 2.5 N (red line 2). Total at cap 4 × 2.3 = 9.2 N ≤ 12 N (red line 3).

**Actuator stop check (safety §3.1 condition 2).** The palm's down hard stop places the tip edge 6 mm below the nominal scalp surface with the spring free; the closest credible head position (band compliance) is 3 mm closer → worst-case compression 9 mm < 10 mm. The firmware limit sits 2° inside the stop; the stop boss is screw-adjustable and its depth is a measured bench item. Lift-servo stall through the 2:1 lever would be ~17 N at the tips, which is why the stop, not the servo, is the cap.

**Tangential.** Three layers: (1) the finger hub is held to the horn by two D41 magnets in a V-detent and pops free at ≈0.5 N at the tip (0.037 N·m), then swings freely on the horn screw — H-4.11's preload-and-yield scheme at the top of its band, not the 0.15 N target (scored honestly below); (2) XL330 Goal Current caps horn torque at ~1.0 N at the tip (≈130 mA plus friction offset, calibrated on the kitchen scale); (3) TM1 magnet breakaway 4–8 N axial. H-6.5's ≤1.0 N bottomed limit and red line 3's ≤2 N are met.

**Compliance across curvature.** Each tip has 10 mm of independent travel; the sagitta across the 66 mm span on R 70–90 is 6–8 mm, so the outer fingers are shimmed 4 mm lower and all four sit in the spring's working band. Head motion of a few mm changes force by ≤0.6 N without spikes (scratch-model §8 item 9).

### 2e. Hair safety

**Every feature within 30 mm of the scalp, from the skin upward:**

| Height | Feature | Exclusion method |
|---|---|---|
| 0–6 mm | Nail edge and plate (tip A/B) | Convex, polished, R 0.3–0.6 mm, corners R 1.5; no re-entrant feature (H-4.1–4.4) |
| 6–26 mm | Tip stem (PETG, 8 mm wide, 10° draft widening upward, root fillet 1.5 mm) | Smooth wedge, nothing wider below than above (H-4.3) |
| 26 mm | TM1 pocket mouth (tang/pocket seam, 0.15 mm/side) | Faces the scalp but sits just outside H-4.9's 25 mm band; a 0.8 mm TPU wiper lip closes the seam; declared the weakest gap |
| 26 mm | Guard underside (fixed to frame) | Smooth, R 2 mm edges; windows 60 × 18 mm with ≥3 mm clearance in every finger position; sleeve widens above the guard (H-6.3) |
| 26–45 mm | Outer sleeve exterior (PETG, 11→12 mm taper) | Smooth; the sleeve/post sliding seam is at the sleeve **mouth, facing up at ≥45 mm** — a hair must climb 20 mm past the guard and turn 180° to enter (labyrinth, H-6.2 (5)); optional TPU boot for longer hair |
| 32 mm | Palm hinge pin (±15°, <1 turn) | Outside the zone; pin in a closed boss, arm shoulder covers the seam |
| 80 mm | Finger hubs, horns, servos | Outside the zone, above the guard |

No continuously rotating surface exists on the module; no 40 µm–3 mm gap exists below 26 mm; the only changing gaps (sleeve/post, hinge, horn) are at ≥32 mm with seams facing away from the scalp.

**Checklist §6.8 self-score (2 / 1 / 0):**

| # | Item | Score | Note |
|---|---|---|---|
| 1 | No exposed rotation in zone | 2 | None anywhere |
| 2 | Every joint named with method | 2 | Table above |
| 3 | No changing / 40 µm–3 mm gap within 25 mm | 2 | Pocket seam at 26 mm with TPU lip; nearest changing gap at 45 mm |
| 4 | Lift before every reversal | 2 | Palm lift every cycle; sweep direction change is gated on lift state |
| 5 | Elements in canopy move as rigid group | 1 | Parallel tracks at fixed 22 mm (never <20 mm apart), but 0–60 ms phase offsets change relative longitudinal position in contact; `LOCKED_PHASE` mode scores 2 |
| 6 | Radiused blade, drafted root, no re-entrants | 2 | TM1 tip A/B on a drafted stem |
| 7 | Mount yields at ≤0.15 N tangential | 1 | Hub breakaway at ~0.5 N (preload-and-yield scheme), current limit at 1.0 N; 0.15 N not met |
| 8 | Protrusion ≥25 mm beyond adjacent surface | 2 | 26 mm below guard |
| 9 | Tip spacing ≥8 mm | 2 | 22 mm |
| 10 | Low-friction polished sliding surfaces | 2 | Nylon/PETG tips, smoothed PETG sleeve; TPU only in the lip |
| 11 | Breakaway 3–5 N, no tether | 2 | TM1 magnet 4–8 N axial; hub 0.5 N; nothing tethered |
| 12 | Hair-shedding guard with drafted pass-throughs | 2 | Fixed guard, 4 windows |
| 13 | With-grain bias and grain map | 2 | Module orientation is logged; firmware default is unidirectional with-grain; against-grain only in ≤25 mm bidirectional mode |
| 14 | Dwell/repetition limits | 2 | Centre wander forces ≥20 mm relocation within 8 strokes; no loaded stationary tip >1 s |
| 15 | Snag reflex = lift and retract | 2 | Current spike on any sweep servo → lift servo up + solenoid drop within ~60 ms; never reverse |
| 16 | Antistatic | 1 | Nylon tips, CF-nylon optional; frame is plastic, not grounded |
| 17 | Tool-free removal for cleaning | 2 | Guard on magnets; fingers lift off their horn screws |
| 18 | Hair variants declared | 2 | In scope: short–medium (2–8 cm), straight–wavy, fine–coarse (coarse needs preload 0.4). Out of scope: long (>15 cm; windows and sleeve mouths become reachable) and curly/coily |
| | **Total** | **33 / 36** | ≥28, no gating 0 |

### 2f. Safety: 13 red lines, e-stop, fail-safe, release

| Red line | Status |
|---|---|
| 1 Exposed rotation / open sliding slot in hair zone | Pass — none; guard windows are clearance pass-throughs (H-6.3), not sliding fits |
| 2 Mechanical cap ≤2.5 N per element | Pass — spring + plunger stop, 2.3 N, independent of servo torque |
| 3 ≤12 N total, ≤2 N tangential before yield | Pass — 9.2 N; hub breakaway 0.5 N |
| 4 NC e-stop in series with motor power, in reach | Pass — 22 mm mushroom on the desk box within reach of the free hand; foot-pedal hold-to-run for staged tests |
| 5 No mains, ≤24 V, no lithium | Pass — 5 V 4 A certified brick |
| 6 Nothing anterior to hairline / near ear / above eyes | Pass — occiput or crown only; arm hard stops prevent rotation past the vertex; >60 mm from the ears |
| 7 No self-locking drive in force path without downstream cap and spring-return lift | Pass — spring plunger downstream of the non-back-drivable XL330; spring-return lift released by a solenoid latch |
| 8 De-energised state lifted or limp | Pass — the lift link's pin is held by a 5 V pull solenoid on the actuator rail; any loss of rail power (e-stop, pedal, fuse, watchdog pulling the MOSFET low) drops the pin and a 0.1 N·m torsion spring raises the palm to its up-stop in ~100 ms, independent of servo back-drivability. Bench: pull the plug mid-stroke 20× |
| 9 No push-fit-only, PLA or brittle tips | Pass — TM1 magnet + pocket walls; PETG/nylon/press-on nails; 3× proof load |
| 10 One-hand ≤3 s release, no chin strap, ≤500 g | Pass — ratchet knob ~2 s; ≈450 g estimated, a weigh-in item |
| 11 Edges ≥1 mm; tips ≥0.4 mm | **Conflict to flag:** tip-interface baseline tip A is 0.3 mm; red line 11 fails tips <0.4 mm. Team B runs first human sessions on tip B (0.6) and a 0.4 variant and asks the Director to reconcile at the Safety Gate |
| 12 Checklist, wig test, glasses, ≤5 min | Procedural; adopted |
| 13 Firmware never the only barrier for S≥3 | Pass — every S≥3 row has a spring, stop, magnet, solenoid or e-stop |

**Why the current limit is not the cap.** XL330 current-based position control limits horn torque, which is tangential at the tip; normal force comes from the lift axis, whose servo would stall at ~17 N total before current limiting meant anything at the nail. Current-to-force through a 288:1 plastic train has ±30% friction hysteresis, is reset by any firmware fault, and a stalled non-back-drivable train holds whatever force exists at zero current. It is a good second layer and a usable contact sensor, not the constant that bounds F.

**Electrical.** 5 V 4 A brick → 3 A blade fuse → e-stop NC → pedal NO (hold-to-run) → OpenRB-150 DC input (bus pass-through to the five servos) and the solenoid MOSFET. Logic on USB from the laptop, so the controller stays up when the rail dies. INA219 on the rail trips at 2.5 A for >200 ms. Bus Watchdog register on each XL330 set to 100 ms. Soft-start ramp 500 ms. One clamped limits table printed at boot.

### 2g. Adjustability

| Variable | How | Range |
|---|---|---|
| Force per contact | Preload cap (0–0.4 N, threaded, reprint-free) + lift setpoint knob (pot → spring compression 0–4 mm) | 0.1–1.1 N operating, 2.3 N cap |
| Speed | Pot / firmware | 20–200 mm/s |
| Stroke length | Firmware, per finger, resampled | 10–46 mm |
| Frequency | Firmware (follows from length, speed, pause) | 0.5–2.5 Hz |
| Attack angle | Three sleeve prints (35/45/55° pocket) per tip-interface §5.2; the pendulum adds ±18° through the stroke | 27–73° |
| Contacts | Populate 1–4 fingers (hub lifts off horn screw) | 1–4 |
| Spacing | 22 mm; a 26 mm palm plate variant is one reprint | 22 / 26 |
| Pattern | Firmware: jitter amplitudes, episode weights, `PERIODIC`, `LOCKED_PHASE`, unidirectional/bidirectional | full PATTERN SPEC v1 |
| Direction vs. lie | Manual detent ring (15° steps) and arm rotation (occiput/crown) | any |
| Tip compliance | Spring swap (0.1 / 0.2 / 0.4 N/mm) | per tip-interface §5.4 |
| Tip geometry | TM1 swap, <10 s | A–H |

### 2h. Components and cost

| Qty | Part | Unit | Ext. | Source |
|---|---|---|---|---|
| 5 | Dynamixel XL330-M288-T | $27.49 | $137 | robotis.us |
| 1 | OpenRB-150 | $28.64 | $29 | robotis.us |
| 1 | 5 V 4 A UL-listed supply (Adafruit #1466) | $18 | $18 | Adafruit |
| 1 | 22 mm NC mushroom e-stop | $12 | $12 | Amazon |
| 1 | Momentary foot pedal (hold-to-run) | ~$10 | $10 | Amazon (~unverified) |
| 1 | 5 V mini pull solenoid (~0.3 A) + logic MOSFET | ~$6 | $6 | Amazon (~unverified) |
| 1 | INA219 breakout | $9.95 | $10 | Adafruit |
| 1 | Welding-helmet ratchet headgear | $16 | $16 | Tractor Supply / Amazon |
| 2 | Compression + torsion spring assortments | $12–14 | $26 | Amazon |
| — | Magnets: 10 × K&J D41, 8 × N52 6×2 + steel washers | — | $11 | K&J / Amazon |
| — | M2/M3 hardware, heat-set inserts, nylocs; fuse holder, rocker, JST/22 AWG/sleeving | — | $45 | Amazon |
| — | 2 × 10 kΩ pots + SSD1306 OLED; press-on nails + 3 guitar picks | — | $21 | Amazon |
| — | Printed parts ≈ 400 g PETG (library $0.10–0.20/g or JLC3DP) | — | $45–70 | — |
| | **Build subtotal** | | **≈ $390–415** | |
| 1 | Mannequin head with human hair, kitchen scale, FSR 402 | — | $51 | Amazon / Adafruit |
| | **Total with test gear** | | **≈ $445–465** | |

Fallback if the lift servo stalls on the bench: swap the 2:1 lever for 3:1 (reprint, $0). Fallback if the 500 g line is missed: populate three fingers (−45 g) and replace the welding headgear with a hard-hat ratchet suspension (−40 g).

**Head-borne mass estimate:** 5 × XL330 90 g; palm bracket 45 g; 4 fingers (beam, sleeve, spring, pocket, magnets, tip) 4 × 12 = 48 g; guard 25 g; arms + cross-bar 60 g; lift link, hinge, solenoid, stops 30 g; headgear 140 g (~unverified); cable on head 15 g → **≈ 450 g**. Moving mass per finger 12 g (≤30 g). Tip speed ≤0.2 m/s in contact, ≤0.3 m/s in air.

**Printed parts (PETG unless noted):**

| Part | Qty | Approx. size / notes |
|---|---|---|
| Palm plate | 1 | 120 × 80 × 4 mm, two rows of XL330 pockets, rear leg 80 × 40 × 5 mm to hinge bosses; 4 perimeters |
| Finger beam (front / rear-row cranked) | 2 + 2 | 12→8 mm taper, 45 mm (rear adds a 36 mm crank); hub Ø18 × 3 mm with 2 magnet pockets and V-detent; layers parallel to stroke |
| Inner post | 4 | Ø8 × 40 mm, spring seat, 10 mm travel stop collar |
| Outer sleeve with TM1 pocket | 4 (+35°/55° variants) | OD 11→12 mm, bore 8.3 mm, 36 mm; pocket 10.3 × 4.3 × 12.5 mm at 45°; N52 pocket; TPU lip groove; print pocket-up, smooth exterior |
| Tip carrier (tang + 20 mm stem) | 8 | TM1 tang 10 × 4 × 12 + stem; nail CA-glued; print edge-up |
| Guard plate | 1 | 130 × 90 × 2.5 mm, 4 windows 60 × 18 mm, R 2 edges, magnet pockets, locating pins; smoothed underside |
| Side arms / cross-bar | 2 / 1 | 130 × 22 × 5 mm slotted arms on the headgear pivots; 140 × 28 × 6 mm bar with lift-servo pocket, hinge bosses, detent ring, VESA holes |
| Lift lever + link, up/down stops, solenoid bracket, strain-relief clip | 1 set | 2:1 lever 40 mm; link 45 mm with pin and solenoid-pin holes; screw-adjustable stop bosses |
| TPU 95A pocket lips | 4 | Ø10 × 1.5 mm |

### 2i. Buildability in an apartment

Tools: component-landscape §8 (soldering iron, calipers, hex keys, files, CA glue, multimeter) plus a kitchen scale. No machining; nothing tighter than ±0.15 mm.

Steps (≈30 h): (1) print and dry-fit palm plate, one finger, guard — 3 h; (2) build the **hand wand** (sleeve + spring + TM1 on a pen handle, tip-interface T0) and run T1/T2 — 3 h; (3) wire Stack A (OpenRB-150, five XL330 IDs, current-based position mode, Goal Current, Profile Velocity, Bus Watchdog, e-stop/pedal/fuse/INA219, solenoid MOSFET) — 4 h; (4) assemble palm, hubs, fingers, sleeves; calibrate each spring on the kitchen scale; set preload caps — 3 h; (5) headgear arms, cross-bar, hinge, torsion spring, lift lever/link/solenoid, up/down stops; measure down-stop depth on the mannequin — 4 h; (6) firmware: pattern engine, lift feed-forward, snag reflex, limits table, OLED/pots — 8 h; (7) bench and wig-head tests — 5 h.

Risky tolerances: sleeve bore on post (0.3 mm; ream with an 8.2 mm drill if it binds); hub V-detent depth vs. magnet gap (sets the 0.5 N breakaway — measure, shim); XL330 pocket fit (print 0.2 mm oversize); window clearance with the finger at ±18° and the palm lifted 15° (≥3 mm); down-stop depth (measured, never assumed).

### 2j. Honest weaknesses, top 5 risks, and the test that retires each

Weaknesses: five servos plus a solenoid on the head is close to the 500 g line and stands 115 mm proud of the occiput (no lying back); force per finger is not individually commandable; strokes ≤46 mm; stroke direction is manual; servo noise reaches the ear by bone conduction; the nail's attack angle swings 36° per stroke, which may or may not be how a finger feels.

| # | Risk | Bench test that retires it |
|---|---|---|
| 1 | **Attack-angle swing** (63° → 27°) makes entry a dig and exit a rub | Wand A/B on forearm and scalp: fixed 45° sleeve vs. pendulum at ±18° and ±10°. If the swing loses, SP2 adopts a parallelogram finger (constant tip orientation) |
| 2 | **Force variation across the stroke** (arc + curvature with a shared lift): contact loss at the ends or 2× force at centre | FSR 402 under the track on the mannequin; log F(φ) at 1–2 Hz with feed-forward on/off; accept if 0.3 ≤ F ≤ 1.0 N over ≥80% of the stroke |
| 3 | **Servo whine / bone conduction** dominates the hiss | Phone SPL at the ear, mannequin then Michael; TPU-isolated servo pockets first, XL330-M077 (lower ratio) second |
| 4 | **Fail-safe lift fails** (solenoid pin binds under load, spring too weak) | Pull the plug 20× mid-stroke at the 2.3 N cap; palm must reach its up-stop within 200 ms every time; repeat for pedal release and watchdog halt |
| 5 | **Hair in the windows or pocket seam** at the long end of the design basis (8 cm) | hair-interaction §7.3 tests 4–5: long wig draped in every orientation for 5 min; tweezer-fed strands into every window, pocket mouth and sleeve mouth. Any capture → TPU boot on the sleeve mouth and/or per-finger bellows |

Secondary: XL330 plastic gears stripping on a head bump (low Goal Current; $27 spares); headgear slipping under 3.6 N tip reaction (verify ratchet friction >10 N); PETG hub creep shifting the breakaway (re-measure weekly).

### 2k. Massager-vs-scratcher self-score (scratch-model §8)

| # | Criterion | Score | Evidence |
|---|---|---|---|
| 1 | Edge, not pad | PASS | TM1 tip A/B/C/F, 0.3–0.6 mm radius, PETG/nylon |
| 2 | Reaches the skin | PASS | 26 mm protrusion below guard, 0.3–0.9 N, spring follows ±5 mm |
| 3 | Light | PASS | 0.1–1.1 N operating, 2.3 N cap, 9.2 N total; not strap-tension controlled |
| 4 | Slides | PASS | 20–46 mm translation per stroke on the skin; tangential compliance at the hub lets the scalp slip |
| 5 | Right speed band | PASS | 50–150 mm/s, 1.4–2.2 Hz; no component >20 Hz (servo gear ripple is at the horn, filtered by the 0.2 N/mm spring) |
| 6 | Deflects hair near the root | PASS | Edge at skin; nothing else in the pile but a drafted stem |
| 7 | Multiple independent contacts | PASS | 4 at 22 mm, separate servos, 0–60 ms spread, ±25% length |
| 8 | Irregular | PASS | Full PATTERN SPEC v1 minus direction drift and P2; `PERIODIC` control available |
| 9 | Compliant at the tip | PASS | 0.2 N/mm, 10 mm travel |
| 10 | Unloads at reversal, lifts between bouts | PASS | Palm lift every cycle; pauses are lifted |
| 11 | Hair-safe geometry | PASS | No rotation, no closed aperture in reach; 33/36 on the hair checklist |
| 12 | Sounds like a scratch | UNSURE | Real nails give the hiss; five geared servos 80 mm from the skull are the risk (test 3) |

---

## 3. SVG schematic — side view through one front-row finger (stroke direction → right)

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 600" width="860" height="600" font-family="Helvetica, Arial, sans-serif" font-size="11">
  <defs>
    <marker id="arr" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#333"/></marker>
  </defs>
  <rect x="0" y="0" width="860" height="600" fill="#fff"/>
  <!-- scalp -->
  <path d="M 60 480 Q 430 400 800 480" fill="none" stroke="#333" stroke-width="2.5"/>
  <path d="M 60 480 Q 430 400 800 480 L 800 600 L 60 600 Z" fill="#f3e6d8" stroke="none"/>
  <text x="70" y="560" fill="#333">SCALP (R ≈ 70–90 mm)</text>
  <!-- hair canopy: short strokes -->
  <g stroke="#8a6d3b" stroke-width="1">
    <line x1="120" y1="470" x2="128" y2="446"/><line x1="150" y1="462" x2="156" y2="438"/><line x1="180" y1="455" x2="188" y2="431"/>
    <line x1="210" y1="449" x2="216" y2="425"/><line x1="240" y1="444" x2="248" y2="420"/><line x1="270" y1="439" x2="276" y2="415"/>
    <line x1="300" y1="434" x2="308" y2="410"/><line x1="330" y1="430" x2="336" y2="406"/><line x1="360" y1="427" x2="368" y2="403"/>
    <line x1="390" y1="424" x2="396" y2="400"/><line x1="420" y1="422" x2="428" y2="398"/><line x1="520" y1="423" x2="528" y2="399"/>
    <line x1="550" y1="425" x2="556" y2="401"/><line x1="580" y1="428" x2="588" y2="404"/><line x1="610" y1="432" x2="616" y2="408"/>
    <line x1="640" y1="437" x2="648" y2="413"/><line x1="670" y1="442" x2="676" y2="418"/><line x1="700" y1="448" x2="708" y2="424"/>
    <line x1="730" y1="455" x2="736" y2="431"/><line x1="760" y1="462" x2="768" y2="438"/>
  </g>
  <text x="620" y="398" fill="#8a6d3b">hair canopy (pile 5–20 mm)</text>
  <!-- exclusion zone line -->
  <path d="M 60 408 Q 430 328 800 408" fill="none" stroke="#c33" stroke-width="1" stroke-dasharray="6,4"/>
  <text x="66" y="402" fill="#c33">30 mm hair-exclusion boundary</text>
  <!-- guard plate (fixed to frame), with window around finger -->
  <path d="M 140 420 Q 300 388 400 378" fill="none" stroke="#555" stroke-width="6" stroke-linecap="round"/>
  <path d="M 545 376 Q 650 384 760 418" fill="none" stroke="#555" stroke-width="6" stroke-linecap="round"/>
  <text x="150" y="438" fill="#555">GUARD PLATE, 26 mm standoff (fixed, magnet-removable)</text>
  <line x1="400" y1="366" x2="545" y2="366" stroke="#555" stroke-width="1" marker-start="url(#arr)" marker-end="url(#arr)"/>
  <text x="430" y="362" fill="#555">window 60 × 18 mm, ≥3 mm clearance</text>
  <!-- headgear band at left -->
  <path d="M 90 150 Q 60 300 95 470" fill="none" stroke="#333" stroke-width="5"/>
  <text x="20" y="300" fill="#333" transform="rotate(-90 20 300)">RATCHET HEADGEAR BAND</text>
  <!-- cross-bar (fixed frame) -->
  <rect x="100" y="330" width="250" height="10" fill="#999" stroke="#333"/>
  <text x="110" y="356" fill="#333">cross-bar (fixed to headgear arms)</text>
  <!-- lift servo on cross-bar -->
  <rect x="150" y="248" width="48" height="82" fill="#d9e8f5" stroke="#333"/>
  <text x="152" y="243" fill="#333">LIFT SERVO (XL330)</text>
  <circle cx="174" cy="318" r="5" fill="#333"/>
  <!-- lift lever and link to palm rear leg -->
  <line x1="174" y1="318" x2="230" y2="300" stroke="#333" stroke-width="3"/>
  <line x1="230" y1="300" x2="318" y2="268" stroke="#333" stroke-width="3"/>
  <circle cx="230" cy="300" r="3" fill="#fff" stroke="#333"/>
  <!-- solenoid latch pin at link/leg joint -->
  <rect x="300" y="252" width="26" height="12" fill="#f5d9d9" stroke="#333"/>
  <circle cx="318" cy="268" r="4" fill="#c33"/>
  <text x="226" y="246" fill="#c33">solenoid latch pin (drops on power loss)</text>
  <!-- palm hinge at z=32 -->
  <circle cx="330" cy="400" r="7" fill="#fff" stroke="#333" stroke-width="2"/>
  <text x="250" y="422" fill="#333">palm hinge (32 mm up)</text>
  <!-- torsion spring symbol at hinge -->
  <path d="M 322 392 q -6 -6 0 -12 q 6 -6 12 0 q 6 6 0 12" fill="none" stroke="#2a7" stroke-width="2"/>
  <text x="340" y="392" fill="#2a7">lift-return spring 0.1 N·m</text>
  <!-- palm rear leg from hinge up to plate -->
  <line x1="330" y1="400" x2="312" y2="160" stroke="#333" stroke-width="6"/>
  <!-- palm plate -->
  <rect x="300" y="152" width="330" height="10" fill="#bbb" stroke="#333"/>
  <text x="400" y="146" fill="#333">PALM PLATE (rocks ±15° about hinge → tips lift 15 mm, +6 mm forward)</text>
  <!-- sweep servo hanging below plate -->
  <rect x="446" y="162" width="48" height="82" fill="#d9e8f5" stroke="#333"/>
  <text x="500" y="200" fill="#333">SWEEP SERVO (XL330, axis ⟂ page)</text>
  <text x="500" y="214" fill="#333">current-based position mode</text>
  <!-- horn / hub with magnetic breakaway -->
  <circle cx="470" cy="236" r="14" fill="#eee" stroke="#333" stroke-width="2"/>
  <circle cx="470" cy="236" r="3" fill="#333"/>
  <circle cx="461" cy="230" r="2.5" fill="#c33"/><circle cx="479" cy="230" r="2.5" fill="#c33"/>
  <text x="500" y="240" fill="#333">hub, pivot 80 mm above scalp;</text>
  <text x="500" y="254" fill="#c33">magnet V-detent breakaway ≈0.5 N at tip</text>
  <!-- finger beam -->
  <path d="M 464 250 L 476 250 L 474 300 L 466 300 Z" fill="#ccc" stroke="#333"/>
  <text x="486" y="284" fill="#333">finger beam, PETG, 12→8 mm taper</text>
  <!-- inner post -->
  <rect x="466" y="300" width="8" height="52" fill="#aaa" stroke="#333"/>
  <!-- spring inside sleeve (drawn as zigzag) -->
  <path d="M 470 306 l 5 4 l -10 4 l 10 4 l -10 4 l 10 4 l -10 4 l 10 4 l -10 4 l 5 4" fill="none" stroke="#2a7" stroke-width="1.5"/>
  <!-- outer sleeve: mouth faces up at ~45 mm -->
  <path d="M 458 312 L 482 312 L 484 416 L 456 416 Z" fill="none" stroke="#333" stroke-width="2"/>
  <text x="494" y="318" fill="#333">sleeve mouth faces UP, 45 mm above scalp</text>
  <text x="494" y="332" fill="#2a7">spring k = 0.2 N/mm, 10 mm travel, hard stop</text>
  <text x="494" y="346" fill="#2a7">F_max = 0.3 + 0.2×10 = 2.3 N</text>
  <!-- TM1 pocket at 45deg at sleeve bottom -->
  <path d="M 456 416 L 484 416 L 470 436 L 442 436 Z" fill="#ddd" stroke="#333"/>
  <circle cx="462" cy="426" r="2.5" fill="#c33"/>
  <text x="494" y="430" fill="#333">TM1 pocket at 45°, N52 magnet (4–8 N breakaway)</text>
  <!-- TPU lip -->
  <path d="M 442 436 L 470 436" stroke="#e8a" stroke-width="3"/>
  <text x="494" y="446" fill="#c6a">TPU lip seals pocket seam (26 mm up)</text>
  <!-- tip: stem + nail plate rising backward (left), edge at bottom right -->
  <path d="M 452 438 L 466 438 L 486 472 L 478 476 Z" fill="#f7f1d6" stroke="#333"/>
  <text x="494" y="466" fill="#333">tip stem 20 mm + nail (tip A/B), edge R 0.3–0.6</text>
  <!-- edge contact point -->
  <circle cx="482" cy="475" r="3" fill="#c33"/>
  <text x="494" y="486" fill="#c33">edge at skin, 0.3–0.9 N, 27–63° attack</text>
  <!-- stroke arc (dashed) -->
  <path d="M 420 470 Q 482 490 545 470" fill="none" stroke="#06c" stroke-width="1.5" stroke-dasharray="5,3"/>
  <text x="400" y="500" fill="#06c">tip arc, ±18° → 46 mm, rise 3.7 mm at ends; lift feed-forward keeps F flat</text>
  <!-- stroke direction arrow -->
  <line x1="430" y1="520" x2="530" y2="520" stroke="#06c" stroke-width="2" marker-end="url(#arr)"/>
  <text x="440" y="536" fill="#06c">stroke (with-grain), 50–150 mm/s</text>
  <!-- lift arrow -->
  <line x1="600" y1="470" x2="608" y2="420" stroke="#2a7" stroke-width="2" marker-end="url(#arr)"/>
  <text x="614" y="450" fill="#2a7">lift 15 mm at every reversal</text>
  <!-- legend -->
  <rect x="640" y="40" width="200" height="86" fill="#fafafa" stroke="#999"/>
  <text x="648" y="56" fill="#333" font-weight="bold">B-2 "Pendulum Hand"</text>
  <text x="648" y="72" fill="#333">4 sweep fingers + 1 palm lift</text>
  <text x="648" y="86" fill="#2a7">green = compliance / cap</text>
  <text x="648" y="100" fill="#c33">red = breakaway / fail-safe</text>
  <text x="648" y="114" fill="#06c">blue = motion</text>
</svg>

---

## 4. Notes for the tournament

- The number to distrust most is the 0.5 N hub breakaway against the hair track's 0.15 N target. The 0.15 N fix is a 0.3 mm spring-steel leaf (10 × 15 mm) between hub and beam at ~0.05 N/mm; it costs 7 mm of tip lag under normal scratch friction and risks chatter, which is why it is not the default.
- The module is mount-agnostic: on a monitor arm over a headrest it becomes the stationary-frame variant the safety track prefers, at the cost of head stillness.
- B-3 (cam-lift) is a strict parts-subset of B-2 and is the fallback if mass or cost fails; W-1 (magnetic puck) deserves a one-evening wig-head trial regardless, being the only idea with no joint on the hair side.
