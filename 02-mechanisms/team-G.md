# TEAM G — Unseeded first-principles mechanism: **ARC-RAKE**

**Seed family:** none (first-principles). **Author:** Mechanism Team G. **Date:** 2026-10-01.
**Inputs read:** BRIEF.md; scratch-model.md §1–3, §4.4, §7, §8; hair-interaction.md (rules H-4/H-5/H-6, checklist §6.8); safety-requirements.md (13 red lines, §3.1 force-cap principle); tip-interface.md (SP1-TM1 adopted); component-landscape.md (parts and prices). Nothing else in 02-mechanisms/ and not prior-art.md.

---

## 0. What the physics demands, before any mechanism

Working backwards from the sensation spec, the device must produce, per contact:

| Requirement | Number (scratch-model) | What it forces mechanically |
|---|---|---|
| Stiff narrow edge reaching skin | E > 1 GPa, edge R 0.2–0.5 mm, 2–8 mm line, 45° attack (§1.2, §3.11) | A real nail-like blade on a stem long enough to pass the hair pile (≥ 25 mm, H-4.5). Tip subsystem solved by tip-interface; adopt it. |
| Light normal force, mechanically capped | 0.15–0.3 N typical, ≤ 0.6 N useful, hard cap ≤ 2.5 N (§3.2, safety §2.1) | A spring between actuator and blade with a hard stop: F_max = F0 + k·x_max. Actuator torque must be irrelevant. |
| Finger-like compliance | 0.1–0.5 N/mm, ≥ 5–10 mm travel (§3.12, §8 item 9) | Soft spring per blade, independent per blade across scalp curvature (sagitta 2.2 mm over 40 mm span). |
| Slides 10–50 mm at 2–20 cm/s, 1–4 Hz | §3.6–3.8 | A tangential stroke of 20–60 mm along the scalp; peak speed ≤ 200 mm/s (H-5.4). |
| Lift-off before every reversal | H-5.2 gating; ≥ 5 mm at zero force, full canopy clearance every 10–20 s | Either a second DOF (lift) or a geometry that lifts the tip automatically at the stroke ends. |
| 3–5 contacts at ~20 mm pitch, moving as a rigid group, not phase-locked | §8 item 7, H-5.6 | One rigid "hand" carrying 3 blades on independent springs: group motion with per-blade force/landing spread. |
| Irregularity: length, speed, force, direction, location jitter, pauses | §4.4, §7 rank 1 (priority 25) | Programmable actuators, not a fixed cam. Must also run a "fully periodic" control condition. |
| No rotation, no gap 40 µm–3 mm within 30 mm of scalp | H-6.1, red line 1 | All joints above a smooth guard; the only things in the hair are blades, stems and a smooth hand. |
| Fail-safe de-energised | red line 8 | Hand lifts or goes limp on power loss. |

The single most consequential observation from the spec: **two things are unique to a scratch — a stiff edge at the skin, and lift-off between strokes.** Every concept below is judged first on whether it gets those two for free.

---

## 1. Concepts (five, structurally different)

### Concept 1 — SWING-RAKE (head-worn, one actuator, geometric lift-off)

One servo swings a rigid 3-blade hand on a 60 mm arm about a pivot ~60 mm above the scalp. Because the arm radius (60 mm) is smaller than the scalp radius (80–90 mm), the tip's arc is **not concentric with the scalp**: the blade touches only within ±11–16° of the arc centre and rises off the skin toward both ends of the swing. The lift happens while the hand is still moving forward (H-5.3), with force tapering to zero before reversal (DR4). Over-swinging to ±25° gives 6–10 mm of clearance at zero force. Normal force is set by how far the pivot block is screwed down (sets spring compression at centre). Stroke chord is fixed by that same screw (23–40 mm). Timing, pauses and per-stroke speed are programmable; stroke length and location are not.

```
            pivot (servo)  z = 60 mm
               o
              /|\   arm R = 60
             / | \
   lift     /  |  \    lift
   zone    /   |   \   zone
  ........*....|....*........   tip arc (R 60)
       ___---- + ----___        scalp (R 80-90)
   ~~~/   contact ±16°  \~~~
```
Verdict: cheapest possible rig that is a true scratcher (edge, light force, slide, lift). Weak on the rank-1 variable (irregularity of length/location).

### Concept 2 — ARC-RAKE (head-worn, two actuators: shoulder lift + elbow sweep) — SELECTED

Concept 1 plus a second servo that raises/lowers the sweep pivot. The two joints form a planar 2-link arm (shoulder = lift, elbow = sweep) whose hand can be placed anywhere along a 60 mm arc of scalp at any depth. Stroke length, start position, landing ramp, lift height and per-stroke force (via depth) become firmware variables; the Concept-1 geometric lift remains as a passive backup (over-swing lifts the tip even with the shoulder frozen). Hand = 3 nail blades at 20 mm pitch, each on a steel leaf spring with a hard stop.

```
   shoulder servo (lift)      frame / guard plate at z ≈ 58
        o======\
                \  upper link 42 mm
                 o  elbow servo (sweep)   z ≈ 75
                 |  stem
            ___[=|=]___  hand carrier (3 leaf springs, 20 mm pitch)
            |    |    |  fingers 30 mm, nails at 45°
   ~~~~~~~~~V~~~~V~~~~V~~~~~~~  canopy
   ---------------------------  scalp
```

### Concept 3 — PRONE GANTRY (frame-mounted, multi-actuator)

User lies prone with the face in a massage-table face cradle; occiput and crown face up and are gravity-registered. A desk-clamped 2020 frame carries an MGN9 rail + GT2 belt + NEMA 17/TMC2209 carriage (StallGuard as a snag detector) with a servo-lifted 3-blade hand. Coverage ~120 × 60 mm in one seating; actuators off the head so weight is free (STS3215 servos).

```
   ===================== 2020 rail over the head =====================
          [carriage]--(lift servo)--[hand]
                               V V V
                        (   back of head, face down in cradle   )
```
Verdict: best coverage, worst registration (head-to-frame distance drifts 5–15 mm with breathing/posture); belt, rail and stepper are all noisier and heavier; posture is unnatural for a 20-minute relaxation test.

### Concept 4 — PENDULUM-ON-BOOM (frame-mounted, one actuator, dead-weight preload)

A mic-boom arm holds a gravity-preloaded pendulum hand over a seated user's occiput; an N20 crank (DRV8871, current-limited) rocks it; tip force = counterweight × g (cleanest possible cap, safety §3.1 "dead-weight" variant); lift by the non-concentric arc as in Concept 1.

```
   boom ----------o pivot
                 /|\  counterweight <- -> hand
   head  (  ~~~~~*~~~~  )
```
Verdict: beautiful force physics, fixed kinematics (fails §8 item 8 unless treated as the control condition), and the user's head must hold still.

### Concept 5 — WILDCARD: BOWDEN "SPIDER" (head-worn hand, desk-mounted motors, independent fingers)

Three XL330 on the desk pull Dyneema tendons through PTFE-lined Bowden housings to three independently curling printed fingers on a headband. Mimics P4 "finger-wiggle". Tendon friction/hysteresis (10–20 %) kills force fidelity, and independent fingers in the canopy violate H-5.6 unless they lift before changing relative position — which removes the point of independence. Rejected; kept as an SP2 idea once the rigid-hand result is known.

### Selection: expected (scratch realism) × P(works first time in an apartment)

| Concept | Realism (0–1) | Why | P(works) | Why | Product |
|---|---|---|---|---|---|
| 1 Swing-rake | 0.60 | right contact physics, auto lift; no length/location jitter | 0.85 | one servo, one bracket | 0.51 |
| **2 Arc-rake** | **0.80** | adds length/location/landing/force jitter and clean 25 mm lifts; contains Concept 1 as a mode | **0.65** | second servo + 2-link IK (~100 lines); leaf springs absorb IK error | **0.52** |
| 3 Prone gantry | 0.70 | coverage; registration drift eats the 0.2 N window | 0.40 | rail, belt, stepper, cradle, frame | 0.28 |
| 4 Pendulum-on-boom | 0.45 | fixed kinematics; head must hold still | 0.70 | crank + weight | 0.32 |
| 5 Bowden spider | 0.50 | wiggle is interesting but force fidelity poor | 0.35 | tendon routing/hysteresis | 0.18 |

Concepts 1 and 2 are a wash on the raw product; Concept 2 wins because it **strictly contains Concept 1** (freeze the shoulder, you have the swing-rake), it exposes the rank-1 sensory variable (pattern irregularity, priority 25) as firmware, and its added part count is one $27 servo and one printed link. Day-1 bring-up is literally Concept 1.

---

## 2. ARC-RAKE: concept-level engineering design

### 2a. Working principle and why it reads as fingernails, not a massager

Human scratching = a stiff keratin edge (not a pad) backed by a soft spring (~0.3 N/mm pulp/joint give), dragged 20–50 mm at 5–15 cm/s under 0.15–0.3 N, lifted at the end of each stroke, three or four of them at ~20 mm pitch landing out of phase, repeated with 20–50 % jitter and occasional pauses (scratch-model §1.2, §3, §4). Each of those is produced by a specific part of ARC-RAKE and by nothing else:

- **Edge** — tip A geometry (press-on-nail/PETG blade, 12 mm wide, edge R 0.3–0.5 mm, 45° attack) on a 30 mm drafted stem, so the edge reaches the skin through a 5–20 mm pile and deflects hair within 2–5 mm of the root (the 1/L² follicle-moment argument, §2.3). This is component A + B of the sensation.
- **Soft spring behind a rigid edge** — a 0.25–0.3 mm spring-steel leaf per blade, k ≈ 0.2 N/mm (adjustable 0.15–0.6), 10 mm travel to a hard stop. Force per blade = k × set depth; depth is what the shoulder servo controls, so force is a firmware setpoint while the cap is a spring constant (safety §3.1).
- **Slide** — the elbow sweeps the hand 20–50 mm along the scalp at 50–150 mm/s; the shoulder tracks the sphere so the depth (force) stays within ±0.5 mm (±0.1 N) over the stroke.
- **Lift at every reversal** — commanded (shoulder up 10 mm while still moving forward, then the return in the air) and passive (over-swing geometry lifts the tip even if the shoulder is dead).
- **Three contacts, not phase-locked** — rigid group in x (H-5.6) but independent in z: scalp curvature, leaf tolerance and the ±1 mm carrier-curvature mismatch give a 20–40 % force spread and a 20–60 ms landing spread without any control effort (§4.2 "fingers are not phase-locked").
- **Irregularity** — PATTERN SPEC v1 (§4.4) implemented directly: per-stroke length, speed, depth, start position, pause and direction sampled; a "periodic" switch for the control condition.
- **Nothing that a massager has** — no pad, no vibration, no rotating head, no force above 2 N anywhere, no scalp displacement (0.2 N friction cannot move the scalp over the skull).

On the §1.2 table the mechanism lands in the SCRATCH column on every row: hard edge R 0.3, 0.15–0.5 N per contact, 100–300 kPa line pressure, < 1 mm scalp translation, 20–50 mm slip, 5–15 cm/s, 1–3 Hz, parts the canopy near the root.

### 2b. Architecture

- **Mounting:** head-worn. A ratchet headband (welding-helmet type, $16) + a printed/aluminium **arch** over the crown (replaces the band's top strap, carries a 25 × 50 mm closed-cell crown pad ≤ 5 kPa). The module hangs from the arch's rear extension over the **occiput / lower crown**, with the guard plate ~55 mm above the scalp. No straps cross the working window. Module can be re-seated in ~30 s to the crown or the parietal sides by rotating the band/arch. Head-borne mass ≈ 300 g (band 100, arch 55, frame/guard 70, 2 × XL330 36, link/stem/hand 40). Quick release = ratchet knob, one hand, < 3 s.
- **Coverage per seating:** 60 mm (along stroke, x) × 40 mm (across, y); 3 blades at 20 mm pitch; ~24 cm² — roughly one hand-width. Four or five seatings cover occiput + crown + upper sides (the two highest-value regions per §5; nape/temples deliberately excluded for SP1).
- **DOF:** 2 active (shoulder lift φ, elbow sweep θ, both revolute about the transverse y-axis — a planar 2R arm) + 3 passive (one leaf per blade, normal to scalp) + 1 passive tangential flexure per finger (the finger paddle itself). Manual: standoff (arch slot), yaw of the module 0/90° (stroke with vs across the lie), carrier curvature shims.
- **Guard:** the module's underside is a smooth 4 mm PETG plate (edges R 2 mm, drafted window) that separates every joint and servo from the hair; only the forearm stem passes through a 32 × 14 mm window with ≥ 4 mm clearance all round, and the stem widens above the plate, never below.
- **Bench mode:** the same module bolts to a 2020 extrusion stub over the mannequin head; all bench tests use that.

```
 plan view (looking down at the scalp)            side view (x–z)
      y                                            shoulder o (lift, frame)
      ^  carrier 60 x 18                                   \ 42 mm
      |  ┌────────────────┐                                 o elbow (sweep)
      |  │ clamp clamp clamp│                               | stem
      |  └──┬─────┬─────┬──┘                      ─────[guard]────── z 58
      |  leaf│  leaf│  leaf│  (free length 35 mm)       [carrier] z 44–52
      |     ▣     ▣     ▣   tang blocks (TM1)         leaf ──▣
      |     |     |     |   fingers, 20 mm pitch           │ 30 mm finger
      +-----┴-----┴-----┴-----> x (stroke)                 ╲ nail 45°
                                             ~~~~~~~~~~~~~~~~~~~~ canopy 5–20
                                             ────────────────── scalp
```

### 2c. Kinematics with numbers

Geometry (local frame: P0 = patch centre on the scalp, x = stroke direction, z = scalp normal; scalp modelled as a sphere R_h = 80 mm at the occiput, 90 mm at the crown — a firmware parameter):

| Item | Value |
|---|---|
| Elbow axis, nominal | x = 0, z = 75 mm |
| Shoulder axis (frame) | x = −30, z = 105 mm; upper link 42 mm at −45° |
| Nail edge, nominal (θ = 0) | x = +35 (leaves extend forward), z = 0 → elbow-to-nail radius 83 mm |
| Elbow sweep range | ±35° hard stops; contact strokes within ±18° (±26 mm) → **≤ 52 mm stroke** |
| Shoulder range | 60°; elbow height 62–105 mm (set depth +4 mm … tip 25 mm clear of scalp) |
| Lift stop (mechanical) | upper-link boss hits an M3 stop screw at elbow z = 62 → max blade compression 4 mm at nominal standoff, 9 mm if the head sits 5 mm closer (never bottomed; x_max = 10 mm) |

**Sphere tracking.** With the elbow fixed, the nail rises above the sphere by Δz(θ) ≈ 83(1 − cos θ) + (83 sin θ)²/(2R_h): 3.5 mm at 15°, 6.2 mm at 20°, 9 mm at 25°. The shoulder lowers the elbow by Δz(θ) during a contact stroke so depth stays at the setpoint; residual error from a wrong R_h (80 vs 90) is < 1 mm, absorbed by the leaves. Attack angle relative to the *local* scalp tangent changes only by s·(1/83 − 1/80) ≈ 1° plus ~4° of shoulder coupling over a 50 mm stroke: 45° ± 5°, inside the 25–65° window.

**Stroke primitives (firmware, PATTERN SPEC v1 numbers):**

| Primitive | θ excursion | Tip speed | Cycle | Lift |
|---|---|---|---|---|
| P1 rake | 15–45 mm contact, L ~ N(30, 25 %) | 50–150 mm/s in contact, 250 mm/s air return | 1.5–3.5 Hz | 10 mm (zero force) each reversal; full 25 mm clearance every 10–20 s |
| P2 sweep | 50 mm (two consecutive 50 mm rakes shifted 25 mm emulate a 75 mm sweep) | 50–120 mm/s | single pass + lifted return | 25 mm |
| P4 wiggle | 5–15 mm | 3–6 Hz, depth ≤ 1 mm (F ≤ 0.15 N) | 2–6 s | passive asynchrony only (fingers are a rigid group) |
| P5 pause | hand lifted 10–25 mm | — | U(0.3, 2 s) | yes |
| P6 region change | shift stroke centre by ±20 mm along x | land at 30 mm/s, depth ramp 0 → target over 0.3 s | — | 25 mm |

**Velocity profile:** trapezoidal in contact (accel ≤ 2 m/s², H-5.4), lift beginning at 70 % of stroke length while still at ≥ 50 % speed (H-5.3), re-entry at ≤ 20° to the skin (the arc is tangent, so entry is naturally shallow). Peak tip speed capped at 200 mm/s in contact.

**Direction-of-stroke modes:** (i) D-cycle: contact with-grain, air return (default, H-5.1); (ii) alternating with lift at both ends (both directions in contact, uses the symmetric wedge tip variant); (iii) short against-grain rake ≤ 25 mm with lift, p = 0.2.

**Irregularity:** sampled per stroke — L, v, depth (force) ~ N(set, 30 %), start-x drift U(−20, +20 mm), pause with p = 0.5, episode type weights P1 60 / P2 20 / P4 15 / P3 0; never the same (L, f, F, direction) tuple > 3 cycles; one slow episode (20–50 mm/s, ≤ 0.15 N) per minute. Switch: "PERIODIC" (control) / "HUMAN" (jittered).

**Passive backup lift:** if the shoulder is frozen at depth 2 mm, over-swinging the elbow to ±25° lifts the tip 8 mm at zero force — Concept 1 behaviour, and the reason an IK bug cannot produce an under-load reversal.

**Servo adequacy (XL330-M288, 0.52 N·m stall, 618°/s no-load):** elbow load = 3 × 0.3 N drag × 0.083 m + J·α (hand+stem 30 g at 83 mm: 2.1e-4 kg·m²; 30 mm stroke at 3 Hz → α ≈ 100 rad/s²) ≈ 0.075 + 0.02 = 0.1 N·m (20 % of stall; ~0.25 A). Shoulder load = 3 × 0.3 N × 0.042 m + bias spring 0.04 N·m ≈ 0.08 N·m nominal; at the lift stop with all three blades at cap (6 N) it is 0.29 N·m, still under stall, and the stop takes the excess. Resolution 0.088°/count → 0.13 mm at the nail.

### 2d. Force path

Normal: scalp ← nail ← finger paddle (axially rigid) ← tang block ← **leaf spring** (0.25–0.3 mm × 12.7 mm feeler-gauge steel, free length 30–45 mm, k = 0.15–0.6 N/mm; baseline 0.3 mm × 35 mm = **0.4 N/mm**, soft option 0.25 mm × 40 mm = 0.16 N/mm) ← carrier ← magnet coupling ← stem ← elbow horn ← upper link ← shoulder horn ← frame ← arch ← headband.

- **Cap per blade:** F_max = F0 + k·x_max = 0 + 0.2 × 10 mm = **2.0 N** (soft leaf) or 0.4 × 6 mm = 2.4 N with the stiffer leaf and a 6 mm stop shim — both ≤ 2.5 N (red line 2). Total 3 blades ≤ 7.2 N ≤ 12 N (red line 3). Optional preload F0 = 0–0.3 N by a 0–1.5 mm shim under the leaf clamp (gives the human "jump to 0.15 N on contact, dip at reversal" profile).
- **Actuator stop:** the shoulder's lowest position is a screw stop sized so that at nominal standoff the blades compress 4 mm and at the closest credible head position (+5 mm) 9 mm < x_max = 10 mm; verified on the kitchen scale at build (safety §3.1 condition 2).
- **Operating setpoints:** depth 0.5–2.5 mm → **0.1–0.5 N per blade** with the 0.2 N/mm leaf.
- **Tangential (drag) path:** nail ← finger paddle: a 1.0 mm PETG/nylon sheet, 12 → 20 mm wide tapered, 22 mm long, is a cantilever with k_x ≈ 0.35 N/mm (0.8 mm sheet: 0.18 N/mm). Scratch drag 0.05–0.2 N bends it < 1 mm; a snag adding 0.3 N tilts the nail back ~1 mm and reduces its bite (self-limiting, like a finger's DIP give). Beyond that: elbow goal-current clutch at ~0.8 N total tip force (electronic, second layer); **hand-level magnetic breakaway** (2 × D61 in shallow cups, ≈ 3 N shear) — the whole passive hand detaches with no tether (red line 3, H-6.4); tip-level TM1 magnet breakaway 4–8 N axial.
- **Compliance across curvature:** the carrier's three leaf seats are printed on an 85 mm radius (outer blades 2.2 mm lower than the centre) so all three land within ±1 mm on R 70–100 mm; the ±1 mm residual is the desired 20–40 % force spread.

### 2e. Hair safety

Exclusion volume = 30 mm above the scalp (design basis, 2–8 cm hair); everything inside it, listed:

| Within 30 mm | What | Exclusion method |
|---|---|---|
| 0–8 mm | nail blades ×3 | smooth convex, edge R 0.3–0.5, corners R 1.5, polished (H-4.1–4.3, 4.8) |
| 8–30 mm | finger paddles ×3 | single piece of sheet, 10°/side plan draft, long edges full-round R 0.5, no steps/necks; the only joint is the heat-formed 45° bend |
| 30 mm | TM1 pocket mouth seam ×3 (0.15 mm) — the one gap in the trap band | sits at the zone boundary; the finger root carries a printed flange that overlaps the pocket mouth (labyrinth with a static lip) and the fit is sleeved with a 1 mm TPU collar; both are tool-free |
| none | no pins, bearings, slots, screws, gears, cables, rotation | — |

Just outside the zone (30–60 mm, reachable by hair that is stood up by the fingers): leaf springs (smooth steel, corners R 2, static clamp seams), carrier (smooth PETG, R 1 mm edges), magnet coupling (static flat faces). Above the guard (≥ 58 mm): elbow horn (oscillates < 70°, never a full turn), elbow servo, upper link, shoulder horn, bias spring, stop screw, servo cables (sleeved, service loop).

Hair-variant statement (§1.9): in scope = short to medium (2–8 cm) straight/wavy, fine to coarse (coarse needs +1 mm depth); buzz cut = easiest; **long (> 15 cm) and curly/coily are out of scope for SP1** (long hair can drape over the guard onto the elbow; curly hair pre-loops and the D-cycle would need with-grain-only operation).

**Self-score, hair checklist §6.8 (gating items marked G):**

| # | Item | Score | Note |
|---|---|---|---|
| 1 G | no exposed rotation in zone | 2 | nearest rotation at 75 mm, above guard |
| 2 G | every zone joint named + excluded | 2 | only TM1 seams; flanged + TPU collar |
| 3 G | no changing / 40 µm–3 mm gap < 25 mm | 2 | nothing below 30 mm but fingers |
| 4 G | lift-off before every reversal | 2 | firmware + passive over-swing geometry |
| 5 G | canopy elements move as a rigid group | 2 | one carrier |
| 6 G | radiused blade, drafted root, no re-entrants | 2 | tapered paddle, flanged root |
| 7 G | mount yields ≤ 0.15 N tangential on snag | 1 | paddle flexure 0.2–0.35 N/mm + current clutch + 3 N breakaway; true ≤ 0.15 N yield before 3 mm is not met and is incompatible with 0.2 N of scratch drag (hair doc §4.11 acknowledges) — bench test 7.3.6 decides |
| 8 | protrusion ≥ 25 mm | 2 | 30 mm |
| 9 | spacing ≥ 8 mm | 2 | 20 mm |
| 10 | low-friction polished, no TPU/silicone sliding | 2 | PETG/nylon fingers; TPU only as the pocket collar above the canopy |
| 11 | breakaway 3–5 N, no tether | 2 | hand magnets ≈ 3 N shear; tips 4–8 N |
| 12 | guard with drafted pass-through | 2 | 32 × 14 window, ≥ 4 mm clearance, stem widens above |
| 13 | with-grain bias + grain map | 2 | per-seating "down-grain direction" setting; D-cycle default |
| 14 | dwell/repetition limits | 2 | ≤ 8 strokes per ±15 mm, then forced shift; no loaded stationary > 1 s |
| 15 | snag reflex lift-and-retract | 2 | current spike > 50 ms → shoulder up 15 mm, elbow hold, never reverse |
| 16 | antistatic | 1 | PETG is an insulator; leaves/frame grounded; RH ≥ 40 %; nylon or CF-nylon fingers as the fix |
| 17 | tool-free removal for cleaning | 2 | hand (magnets) and tips (magnets) |
| 18 | states hair variants tolerated | 2 | above |
| | **Total** | **34 / 36** | ≥ 28, no gating 0 |

### 2f. Safety: 13 red lines, e-stop, fail-safe, release

| Red line | Status | How |
|---|---|---|
| 1 no exposed rotation/slot within 30 mm | ✓ | elbow at 75 mm above a guard; window is a drafted opening at 58 mm, not a slot at hair level |
| 2 force bounded by a mechanical constant ≤ 2.5 N | ✓ | leaf k × x_max = 2.0–2.4 N; stop screw on the shoulder |
| 3 ≤ 12 N total; ≤ 2 N tangential before yield | ✓ | ≤ 7.2 N; paddle flexure, 0.8 N current clutch, 3 N hand breakaway |
| 4 NC e-stop in series with motor power + hold-to-run | ✓ | 22 mm NC mushroom in the 5 V servo rail before the OpenRB power pass-through; foot pedal in series for staged tests; MCU on its own 5 V branch |
| 5 no mains, ≤ 24 V, no lithium | ✓ | 5 V 4 A UL-listed desktop brick, fused |
| 6 nothing anterior to hairline / near ears / above eyes | ✓ | occiput and crown only; arch passes over the crown ≥ 60 mm from the ear canals |
| 7 no self-locking drive without downstream spring cap + spring-return lift | ✓ (to verify) | XL330 is a geared servo; leaf cap downstream; **bias spring on the upper link lifts the hand when torque is off** — depends on XL330 back-drive torque (expected 0.02–0.05 N·m, UNKNOWN: measure day 1; fallback = GM3506 gimbal motor on the shoulder, $24, fully back-drivable) |
| 8 de-energised = lifted or limp | ✓ (same caveat) | e-stop/watchdog/stall → torque off → bias spring lifts ≥ 10 mm |
| 9 tips positively retained, tough, proof-loaded | ✓ | TM1 magnet + 12 mm pocket walls; PETG/nylon, never PLA; 3× proof load (6 N) before use |
| 10 one-hand release ≤ 3 s, ≤ 500 g, no chin strap | ✓ | ratchet knob; ~300 g |
| 11 edges ≥ 1 mm; tips ≥ 0.4 mm | ✓ with note | first human sessions use the 0.5 mm-edge tip (tip B); 0.3 mm tip A is a later experiment after the Safety Gate reconciles tip-interface (0.3) with safety (0.4) |
| 12 checklist, wig test, glasses, ≤ 5 min | procedural | adopted verbatim from safety §6 |
| 13 no firmware-only barrier for S ≥ 3 | ✓ | every S ≥ 3 hazard has a spring, stop, magnet or wire |

Other: motion timeout 20 min; soft-start ramp 500 ms; INA219 rail watchdog (trip at 1.2 A sustained); watchdog pulls servo torque-enable low; stall = Present Current > 1.5× stroke baseline for 200 ms → torque off + re-arm. Thermal: XL330 bodies are ≥ 75 mm from the scalp. Noise: XL330 plastic gears, measured at the ear during bench test; target ≤ 60 dBA.

### 2g. Adjustability

| Variable | Adjustable? | How |
|---|---|---|
| Force per blade | yes, continuous, with readout | depth setpoint (knob 1 → 0.05–0.6 N via k); leaf swap/clamp position for k; shim for preload; FSR under the mannequin for calibration |
| Speed | yes | knob 2 (20–200 mm/s scale) |
| Stroke length | yes | firmware (5–52 mm) |
| Frequency | yes (coupled to L and v) | firmware |
| Attack angle | yes | tip swap: paddles bent at 35 / 45 / 55° (the TM1 pocket stays vertical) |
| Contact count | yes | pull outer tips (1 blade) or the centre tip (2 at 40 mm) — magnets, tool-free |
| Spacing | reprint | carrier variants at 16 / 20 / 24 mm pitch (one 30 g print each) |
| Pattern | yes | PERIODIC / HUMAN switch; episode weights, jitter %, with/against/alternating in a boot-time config table; OLED shows current setpoints and measured current |
| Tip geometry/material | yes | TM1 family A–H, plus the 90°-included symmetric wedge for alternating mode |
| Direction vs lie | manual | module yaw 0 / 90° on the arch (two bolt patterns); grain direction flag in firmware |
| Region | manual | re-seat band/arch (30 s) |

### 2h. Components and cost (prices from component-landscape.md)

| Qty | Part | Unit | Ext. |
|---|---|---|---|
| 2 | Dynamixel XL330-M288-T (shoulder, elbow) | $27.49 | $55 |
| 1 | OpenRB-150 controller | $28.64 | $29 |
| 1 | 5 V 4 A UL-listed desktop supply (Adafruit #1466) | $18 | $18 |
| 1 | 22 mm NC mushroom e-stop + foot pedal (hold-to-run) | $12 + $8 | $20 |
| 1 | INA219 breakout | $9.95 | $10 |
| 1 | 2 × 10 kΩ pots, toggle switch, SSD1306 OLED, rocker switch, fuse holder + fuses, JST/Dupont/22 AWG wire, heat-shrink | — | $35 |
| 1 | Welding-helmet ratchet headband | $16 | $16 |
| 1 | 3 × 20 mm aluminium flat bar 500 mm (arch) or printed arch; 25 mm closed-cell foam pad | $8 | $8 |
| 1 | Feeler-gauge set (0.2–0.5 mm × 12.7 mm blades) — leaf springs | $8 | $8 |
| 1 | PETG sheet 1.0 mm (and/or nylon 1.0 mm) 300 × 300 — fingers | $10 | $10 |
| 1 | Press-on nails (ABS) assorted — blades | $6 | $6 |
| 10 | N52 6 × 2 magnets, 4 × D61 magnets, M3 washers/steel discs | — | $8 |
| 1 | Extension-spring assortment (bias spring) | $10 | $10 |
| 1 | M3 hardware + heat-set inserts | $15 | $15 |
| 1 | TPU collars (3) + all PETG prints ≈ 280 g (library $0.10–0.20/g or JLC3DP) | — | $30–50 |
| | **Build subtotal** | | **≈ $280–300** |
| 1 | Mannequin head with human hair + clamp | $35 + $8 | $43 |
| 1 | Kitchen scale 0.1 g; digital luggage scale; FSR 402 | $12 + $12 + $7 | $31 |
| | **Build + test gear** | | **≈ $355–375** |

Printed parts (PETG unless noted):

| Part | Approx. size (mm) | Notes |
|---|---|---|
| Frame + guard plate | 110 × 90 × 4 plate, two towers to z 110, 32 × 14 drafted window | 4 perimeters; R 2 edges; shoulder servo bolts to one tower, idler bore in the other; arch bolt pattern 0/90° |
| Upper link | 60 × 30 × 25 | horn + idler bosses, elbow-servo cradle, stop boss, spring tab |
| Stem (forearm) | 28 × 14 → 10 × 8 taper | horn mount at top, D61 cup at foot |
| Hand carrier | 60 × 18 × 8 | 3 leaf seats on an R 85 curve, D61 cup, clamp screws |
| Leaf clamp blocks ×3 | 14 × 10 × 6 | M3 × 2 each |
| TM1 tang blocks ×3 | 14 × 8 × 16 | pocket 10.3 × 4.3 × 12.5 with keyed chamfer; N52 6 × 2 at floor; leaf slot on top |
| TPU 95A collars ×3 | Ø 12 × 4 | pocket-mouth seal |
| Arch end clamps ×2 | 30 × 25 × 15 | fit the band's side pivots |
| Control box | 100 × 70 × 40 | e-stop on top, pots, OLED |
| Bench adapter | 60 × 40 × 20 | 2020 T-nut interface |
| Attack-angle bending jig | 40 × 20 × 20 | 35/45/55° forms for the finger bend |

### 2i. Buildability in an apartment

Tools: soldering iron (Pinecil), heat-set tips, calipers, needle files, 400/1000/2000 wet-dry, flush cutters, tin snips (feeler blades), heat gun (finger bends), hex keys, multimeter, kitchen scale, 10× loupe. No drilling, no machining.

Steps (≈ 30–38 h total):
1. Order day 0: Robotis (XL330 ×2, OpenRB-150), Amazon (band, feeler set, PETG sheet, nails, magnets, springs, e-stop, PSU, electronics, mannequin), prints to library/JLC. — 1 h
2. Fingers: cut six 1.0 mm PETG paddles oversize, file to plan-form (12 → 20 mm, 10° draft), full-round the long edges, heat-bend the lower 8 mm at 45° over the jig, file the nail edge to R 0.5 (first set) and R 0.3 (second set), polish 400→2000, flame-kiss PETG; or CA-bond a trimmed press-on nail onto a straight paddle's 45° foot. Burr test (cotton ball). — 3 h
3. Tang blocks: epoxy N52 magnets into pockets, steel disc into each finger root, press TPU collar. Measure pull-out on the luggage scale (target 4–8 N). — 1 h
4. Leaves: cut 0.3 mm feeler blades to 50 mm, round corners R 2, clamp into the carrier at 35 mm free length; press the carrier on the kitchen scale at 2/4/6/8 mm (ruler) → record k; adjust clamp position. — 1.5 h
5. Frame/link/stem assembly: heat-set inserts, mount servos (horn + idler), set shoulder stop screw, fit bias spring, magnet cups, hand coupling. — 3 h
6. Arch: bend the flat bar over the mannequin (or print), clamp to the band pivots, fit crown pad, set the standoff slot so the guard plate sits 55 mm above the scalp. — 2 h
7. Electronics: 5 V brick → fuse → e-stop (NC) → pedal → OpenRB power-in → servo bus; logic 5 V branch before the e-stop; INA219 in the servo rail; pots/OLED/switch; sleeve cables with a service loop at the shoulder. — 3 h
8. Firmware: Dynamixel SDK (OpenRB examples), current-based position mode, 2R IK with the sphere model, D-cycle primitive, PATTERN SPEC sampler, limits table printed at boot, watchdog, stall trip, INA219 trip. — 10–14 h
9. Calibration: zero depth on the mannequin (contact detected by elbow-current rise), kitchen-scale force vs depth table, stop-screw check (push head form in 5 mm → blades not bottomed), bias-spring lift test with torque off, e-stop/pedal → 0 V on the rail. — 2 h
10. Bench tests per hair §7.3 and safety §6, then the staged human protocol. — 4 h+

Risky tolerances: TM1 pocket clearance 0.15/side (print orientation: opening up); leaf clamp must not slip (two M3 screws, 1 mm serration printed into the seat); finger bend angle ±5° (jig); nail-edge radius (loupe vs 0.6/1.0 mm drill shank); stem/elbow horn fit (XL330 horn screws, M2). None requires better than ±0.2 mm.

### 2j. Honest weaknesses, top 5 risks, retiring bench tests

Weaknesses: single ~24 cm² patch per seating (coverage is manual); orientation of the hand is not an independent DOF (2R arm), so attack angle is a tip-swap variable, not a knob; three fingers in a rigid line cannot do true per-finger wiggle (P4 is emulated as a low-force group jitter); a 130 mm tall module on the back of the head looks absurd and loads the band in moment; the lifting fail-safe relies on an unmeasured back-drive torque; PETG paddle fatigue at the 45° bend is unknown; the rule-7 tangential yield is only partially met.

| # | Risk | Likelihood / impact | Bench test that retires it |
|---|---|---|---|
| 1 | Nails do not reach skin in Michael's hair at ≤ 0.3 N (ride on the pile) | M / fatal to sensation | Static tip test (hair §7.3.1) on the real-hair mannequin at 0.2/0.5/1 N with side photos; fix = +5 mm finger length, +depth, coarser-hair stiffer leaf |
| 2 | Shoulder does not back-drive: hand stays loaded after e-stop | M / red line 8 | Day-1: torque off, hang the luggage scale on a 50 mm lever, read torque; set bias spring 1.5×; if > 0.1 N·m swap shoulder for GM3506 + SimpleFOC Mini (+$45) |
| 3 | Band/arch rocks under 1 N of stroke reaction so depth (force) drifts ±1 mm | M / spoils force control | Module on the mannequin on the band; log elbow/shoulder current while a 1 N lateral pull is applied; fix = stiffer arch section, nape pad, or snugger ratchet |
| 4 | Feels like a machine despite jitter (sweep too smooth/regular, servo micro-steps) | M / the whole point | PERIODIC vs HUMAN A/B in the first human session, blinded by a helper flipping the switch; add force/landing noise; if still "machine", test the frozen-shoulder Concept-1 mode (different velocity profile) |
| 5 | Servo gear noise at 10 cm from the ear masks the scratch hiss | H / moderate | Phone SPL at the ear position on the mannequin; foam-isolate servo mounts; ear-plug A/B per scratch-model §9 Q9 |
| 6 | Finger paddle cracks at the bend after thousands of strokes; fragment near the scalp | L / S3 | 10,000-stroke endurance on the mannequin, loupe inspection every 2,000; nylon sheet if PETG whitens |

### 2k. Massager-vs-scratcher self-score (scratch-model §8)

| # | Criterion | Score | Evidence |
|---|---|---|---|
| 1 | Edge, not pad | PASS | tip A/B blade, E > 2 GPa, R 0.3–0.5, 12 mm line |
| 2 | Reaches the skin | PASS (verify) | 30 mm fingers at 45° vs ≤ 20 mm pile; bench test 7.3.1 |
| 3 | Light | PASS | 0.1–0.5 N setpoints; 2.0–2.4 N mechanical cap; total ≤ 7.2 N |
| 4 | Slides | PASS | 15–52 mm slip per stroke; 0.2 N cannot move the scalp |
| 5 | Right speed band | PASS | 50–200 mm/s, 1–3.5 Hz; no vibration source (plastic-gear servo ripple to be checked, expected < 0.05 mm at the nail) |
| 6 | Deflects hair near the root | PASS | edge at the skin, finger stem narrow (12 mm blade, 1 mm thick) |
| 7 | Multiple independent contacts | PASS / UNSURE | 3 at 20 mm, independent leaves; asynchrony is passive (curvature + tolerance), not driven |
| 8 | Irregular | PASS | PATTERN SPEC v1 implemented; PERIODIC control condition included |
| 9 | Compliant at the tip | PASS | 0.16–0.4 N/mm, 10 mm travel |
| 10 | Unloads at reversal, lifts between bouts | PASS | commanded + passive geometric lift |
| 11 | Hair-safe geometry | PASS | 34/36, no gating zero |
| 12 | Sounds like a scratch, not a motor | UNSURE | measure; mitigate |

No FAIL on items 1–6.

---

## 3. SVG schematic — side view through the stroke plane

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 540" width="820" height="540" font-family="Helvetica, Arial, sans-serif" font-size="12">
  <rect x="0" y="0" width="820" height="540" fill="#ffffff"/>
  <!-- skull and scalp -->
  <path d="M 60 500 Q 400 400 760 500 L 760 540 L 60 540 Z" fill="#f3e9dc" stroke="none"/>
  <path d="M 60 500 Q 400 400 760 500" fill="none" stroke="#8a5a3c" stroke-width="3"/>
  <text x="640" y="525" fill="#8a5a3c">scalp (R 80–90 mm), x → stroke direction</text>
  <!-- hair canopy -->
  <g stroke="#555" stroke-width="1">
    <line x1="120" y1="486" x2="135" y2="455"/><line x1="160" y1="476" x2="175" y2="446"/>
    <line x1="200" y1="467" x2="215" y2="437"/><line x1="240" y1="459" x2="255" y2="430"/>
    <line x1="280" y1="453" x2="295" y2="424"/><line x1="320" y1="448" x2="335" y2="420"/>
    <line x1="360" y1="445" x2="375" y2="417"/><line x1="500" y1="449" x2="515" y2="421"/>
    <line x1="540" y1="454" x2="555" y2="426"/><line x1="580" y1="461" x2="595" y2="433"/>
    <line x1="620" y1="469" x2="635" y2="441"/><line x1="660" y1="478" x2="675" y2="450"/>
    <line x1="700" y1="488" x2="715" y2="460"/>
  </g>
  <text x="120" y="440" fill="#555">hair canopy, pile 5–20 mm</text>
  <!-- finger: nail + paddle -->
  <line x1="446" y1="444" x2="424" y2="422" stroke="#1a1a1a" stroke-width="4" stroke-linecap="round"/>
  <line x1="424" y1="422" x2="424" y2="368" stroke="#1a1a1a" stroke-width="3"/>
  <text x="456" y="440" fill="#1a1a1a">nail blade, edge R 0.3–0.5, 45°</text>
  <text x="432" y="392" fill="#1a1a1a">finger paddle 1 mm PETG, 30 mm (tangential flexure)</text>
  <!-- tang block (TM1) -->
  <rect x="414" y="334" width="20" height="34" rx="3" fill="#cfd8dc" stroke="#37474f" stroke-width="1.5"/>
  <text x="440" y="352" fill="#37474f">TM1 tang block + magnet</text>
  <!-- leaf spring -->
  <line x1="414" y1="336" x2="330" y2="336" stroke="#0277bd" stroke-width="3"/>
  <text x="300" y="356" fill="#0277bd">leaf spring 0.3 mm steel, k ≈ 0.2–0.4 N/mm, 10 mm travel to stop</text>
  <!-- carrier -->
  <rect x="300" y="318" width="44" height="22" rx="3" fill="#b0bec5" stroke="#37474f" stroke-width="1.5"/>
  <text x="200" y="332" fill="#37474f">hand carrier</text>
  <!-- magnet coupling -->
  <rect x="314" y="306" width="16" height="12" fill="#ffcc80" stroke="#e65100" stroke-width="1.5"/>
  <text x="160" y="312" fill="#e65100">magnet breakaway ≈ 3 N</text>
  <!-- guard plate with window -->
  <rect x="80" y="286" width="212" height="8" rx="2" fill="#9e9e9e" stroke="#424242"/>
  <rect x="352" y="286" width="380" height="8" rx="2" fill="#9e9e9e" stroke="#424242"/>
  <text x="560" y="280" fill="#424242">guard plate (smooth, R 2 edges), z ≈ 58 mm</text>
  <text x="296" y="280" fill="#424242" font-size="10">window ≥4 mm clear</text>
  <!-- stem -->
  <polygon points="314,306 330,306 334,246 310,246" fill="#78909c" stroke="#37474f" stroke-width="1.5"/>
  <text x="340" y="262" fill="#37474f">stem (widens above guard)</text>
  <!-- elbow servo -->
  <circle cx="322" cy="246" r="9" fill="#fff" stroke="#c62828" stroke-width="3"/>
  <rect x="306" y="196" width="32" height="42" rx="3" fill="#ef9a9a" stroke="#c62828" stroke-width="1.5"/>
  <text x="346" y="240" fill="#c62828">elbow: XL330 sweep ±35° (z 75 mm)</text>
  <!-- upper link -->
  <polygon points="312,250 332,242 262,176 246,190" fill="#a5d6a7" stroke="#2e7d32" stroke-width="1.5"/>
  <text x="190" y="226" fill="#2e7d32">upper link 42 mm</text>
  <!-- shoulder servo -->
  <circle cx="254" cy="183" r="9" fill="#fff" stroke="#c62828" stroke-width="3"/>
  <rect x="206" y="130" width="42" height="34" rx="3" fill="#ef9a9a" stroke="#c62828" stroke-width="1.5"/>
  <text x="256" y="150" fill="#c62828">shoulder: XL330 lift (z 105 mm)</text>
  <!-- frame tower -->
  <polygon points="200,286 200,120 212,120 226,286" fill="#e0e0e0" stroke="#424242" stroke-width="1.5"/>
  <text x="86" y="150" fill="#424242">frame tower</text>
  <!-- stop screw -->
  <line x1="236" y1="262" x2="262" y2="262" stroke="#6a1b9a" stroke-width="4"/>
  <text x="90" y="266" fill="#6a1b9a">lift stop screw (actuator stop)</text>
  <!-- bias spring -->
  <path d="M 212 128 l 8 -6 l -8 -6 l 8 -6 l -8 -6 l 8 -6 l -8 -6 l 8 -6 L 246 76" fill="none" stroke="#f9a825" stroke-width="2"/>
  <line x1="246" y1="76" x2="262" y2="176" stroke="#f9a825" stroke-width="1.5" stroke-dasharray="4 3"/>
  <text x="260" y="76" fill="#f9a825">bias spring: lifts hand when torque is off</text>
  <!-- arch and headband -->
  <path d="M 80 290 Q 60 120 20 60" fill="none" stroke="#5d4037" stroke-width="5"/>
  <text x="26" y="48" fill="#5d4037">arch over crown → ratchet headband</text>
  <path d="M 740 300 Q 790 380 770 500" fill="none" stroke="#5d4037" stroke-width="5"/>
  <text x="690" y="330" fill="#5d4037">to band (nape)</text>
  <!-- stroke arrow -->
  <line x1="380" y1="470" x2="520" y2="470" stroke="#1565c0" stroke-width="2" marker-end="url(#a)"/>
  <defs><marker id="a" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#1565c0"/></marker></defs>
  <text x="380" y="488" fill="#1565c0">contact stroke 15–52 mm, 50–150 mm/s; lift 10 mm; air return</text>
  <!-- scale -->
  <line x1="60" y1="520" x2="110" y2="520" stroke="#000" stroke-width="2"/>
  <text x="62" y="534">≈ 20 mm (schematic, not to scale)</text>
</svg>

---

## 4. One-paragraph summary for the tournament

ARC-RAKE is a head-worn, two-servo planar finger-arm (XL330 shoulder lift + XL330 elbow sweep, both above a smooth guard) carrying a passive three-nail hand: press-on-nail/PETG blades at 45° on 30 mm drafted paddles, each on its own 0.2–0.4 N/mm steel leaf with a 10 mm hard stop, so per-blade force is 0.1–0.5 N in use and capped at ≤ 2.4 N by a spring constant regardless of servo torque. The elbow slides the hand 15–52 mm along the scalp at 50–150 mm/s while the shoulder tracks the scalp sphere and lifts 10–25 mm at every reversal; the non-concentric arc geometry lifts the tip passively even if the shoulder freezes. All five sensation components (edge at skin, light force, slide, lift, three asynchronous contacts with programmable jitter) come from parts that each do exactly one job; cost ≈ $290 build / $370 with test gear; hair checklist 34/36; red lines all addressed, with the lift fail-safe (servo back-drive) flagged as the first thing to measure.
