# TEAM E — Smooth, back-drivable, force-controlled direct drive and remote (tendon) actuation

**Project SCRATCH · 02-mechanisms · Team E · 2026-10-01**
Inputs read: BRIEF.md, scratch-model.md, hair-interaction.md, safety-requirements.md, tip-interface.md, component-landscape.md. Firewall respected: no other team file, no prior-art.md.

Tag convention as in the foundations: **KNOWN** (sourced), **EST** (derived here, derivation shown), **UNKNOWN** (test).

---

## 0. The seed-family thesis in one paragraph

Every foundation document converges on the same mechanical fact: a scratch is a stiff edge on a *soft, force-bounded* mount (pulp ≈ 0.3–0.5 N/mm, force 0.1–0.6 N per nail, yields before hair does). Geared servos give you position; they are rigid, non-back-drivable and noisy, so every other team has to add springs, clutches and breakaways to get back the softness a hand has for free. Our family starts from the other end: an actuator whose output *is* a force (torque ∝ current, no gearbox, back-drivable), so the mount's compliance, the force ceiling, the force jitter and the snag-yield are all the same thing — the commanded torque — bounded physically by the motor's stall torque at 12 V. The question we have to answer honestly is whether cheap FOC hardware (a $40 gimbal motor and a $18 driver) actually delivers force fidelity in the 0.05–0.6 N band at 1–4 Hz, silently, and whether the extra "listening" (impedance control, snag reflex in 10 ms) is worth more than a crank and a spring. Section 1 puts numbers on that; sections 2–5 are the concepts and the selected design.

---

## 1. What cheap FOC actually buys you (quantified)

Reference motor: iPower GM3506 with AS5048A encoder, $41.90 (component-landscape §1.5). Landscape figures: 0.06–0.1 N·m peak, 40 mm, ~60 g. Phase resistance and torque constant are not in the landscape; listings for this class give R ≈ 5–6 Ω and ~2 A at 12 V — I use **R = 5.6 Ω, Kt = 0.05 N·m/A, L ≈ 2.5 mH** (all EST; Day-1 bench test measures Kt with a kitchen scale, §4i). GM2804 (0.03 N·m, 40 g, $18.90) is the smaller sibling.

| Quantity | GM3506 on 45 mm lever (normal axis) | GM3506 on 100 mm lever (stroke axis) | GM2804 on 70 mm lever | Basis |
|---|---|---|---|---|
| Physical stall torque at 12 V | 0.107 N·m (12 V / 5.6 Ω × Kt) | same | ~0.03 N·m | EST |
| **Physical tip-force cap** (no firmware involved) | **2.2 N** | **1.0 N tangential** | 0.43 N | τ_stall / lever |
| Torque command resolution (ESP32 12-bit PWM, 12 V) | 2.9 mV → 0.52 mA → 26 µN·m → **0.4 mN at tip** | 0.26 mN | ~0.5 mN | EST |
| Practical force floor (cogging + bearing friction, ~1–2 % of rated) | **±0.02–0.03 N ripple** | ±0.01–0.02 N | ±0.01 N | EST; SimpleFOC anticogging table reduces ~5× |
| Electrical bandwidth L/R | τ = 0.45 ms → ~350 Hz | same | similar | EST |
| Encoder resolution at tip (AS5048A 14-bit) | 0.023 mm | 0.038 mm | AS5600 12-bit: 0.11 mm | KNOWN bits |
| Control loop rate (SimpleFOC on ESP32, 2 motors, SPI encoders) | 2–4 kHz FOC loop; 1 kHz impedance loop | | | KNOWN (library) |
| Renderable virtual stiffness, stable | 0.05–3 N/mm (we need 0.1–1) | | | EST (haptics rule: K·Δx_enc ≪ friction) |
| Back-EMF at scratch speed (1 rad/s, 10 cm/s at 100 mm) | 0.05 V vs 12 V bus → voltage-mode torque error < 1 % | | | EST |
| Moving-mass inertia and lift speed | J ≈ 4×10⁻⁴ kg·m² (110 g at 45 mm): 8 mm lift in ~60–80 ms | J ≈ 2.3×10⁻⁴: 2 m/s² needs 0.005 N·m | | EST |
| Heating at sustained tip force (I²R) | 0.45 N → 1.6 W; 0.75 N → 2.6 W; 1.0 N → 4.6 W | 0.3 N drag → 2 W during stroke, ~1 W average | | EST — **this is the real limit of direct drive** |
| Noise | PWM 25–30 kHz, no gears: inaudible; scratch hiss dominates | | | KNOWN (gimbal FOC) |
| Cost per force-controlled axis | $41.90 motor+encoder + $18 SimpleFOC Mini = **$60** | | $37 | landscape |

Three conclusions. (1) **Force resolution is not the problem**: the command step is ~1000× finer than a 0.05 N experimental step; the real floor is cogging/friction at ±0.02 N, i.e. ~10 % of a 0.25 N stroke force — acceptable for SP1, improvable in firmware. (2) **Bandwidth is not the problem**: electrical 350 Hz, mechanical tens of Hz; the 1–4 Hz stroke and the 100 ms lift are slow for this hardware. (3) **Heat is the problem**: a direct-drive motor holding 0.75 N through a 45 mm lever dissipates 2.6 W in a 60 g can. The design therefore (a) keeps the mean normal force low (the sensation model wants 0.15–0.3 N per nail anyway), (b) lifts for ~40 % of each cycle, (c) fits a $3 fan and an NTC, and (d) offers a dead-weight bias knob for the vigorous end (§4d).

**Tendons, quantified.** A Bowden cable loses force by e^(−µθ) over its total bend angle θ; with a PTFE-lined housing µ ≈ 0.05–0.12 (EST). For a 90° total bend: 8–17 % loss; for 180°: 15–31 %. The hysteresis band (push vs pull) is twice the loss, so a desk-box motor commanding 0.25 N at the nail can deliver anywhere in 0.17–0.33 N depending on the previous direction of motion — ±30 %, which is the whole experimental resolution of the force–pleasure curve. Tendons therefore need a *head-end* sensor (an AS5600 at the head pivot, $3) and a position loop closed around the cable, at which point the force is inferred from a head-end spring, not from the motor. That is a fine architecture for a wearable but it gives away the family's main advantage. This is why the selected concept is frame-mounted direct drive and the tendon version is kept as the SP2 wearable path.

---

## 2. Concepts

### E1 — "Listening Hand": two direct-drive gimbal motors render a 3-nail rake as a programmable spring (SELECTED)

A planar two-joint "finger" hangs from a desk-clamped monitor arm above the seated user's crown (or behind the occiput). Joint M2 (shoulder, 45 mm arm, horizontal axis) sets normal force and lift; joint M1 (knuckle, 100 mm arm, parallel axis) sweeps the stroke. Both are GM3506 gimbal motors under SimpleFOC in torque mode with an impedance law on top, so the rake behaves as a spring of commandable stiffness (0.1–1 N/mm) and commandable preload (0.05–0.6 N per nail) that follows scalp curvature and head motion within ±15 mm, lifts 8 mm at zero force before every reversal, and retracts in 10 ms if the stroke axis lags its target by 3 mm (snag). The rake bar carries three SP1-TM1 holders on 0.4 mm spring-steel leaves (0.3 N/mm, 8 mm travel) at 20 mm pitch. Nothing within 30 mm of the scalp moves relative to anything else; the motors are ≥130 mm up and shrouded. Head withdrawal is the release.

```
          monitor arm ──┐
   counterweight ═══╗   │ spine plate
            M2 (●)══╬═══┤      M2: shoulder, GM3506, lift/force, 45 mm arm
                45 mm   │      counterbalance spring + hard stops
            M1 (●)      │      M1: knuckle, GM3506, stroke ±24 mm, 100 mm arm
             │ smooth 10 mm rod, 100 mm
             │
        ┌────┴────┐  rake bar / palm shell (convex underside)
        ╲   ╲   ╲      3 × spring-steel leaves 0.4×8×45 mm, 20 mm pitch
         ▲   ▲   ▲     3 × TM1 holders, tips at 45°
 ~~~~~~~~~~~~~~~~~~~~  hair canopy
 ───────────────────   scalp
```

### E2 — "Remote Hand": motors in a desk box, two Bowden tendons to a 120 g head-worn rake

Same rake and leaves as E1, but the carrier is a 60 mm MGN7 slide (or a 60 mm swing arm) on a hard-hat ratchet suspension. Tendon 1 (1.2 mm shift cable in 4 mm lined housing) pulls the stroke; an extension spring returns it. Tendon 2 pulls the rake *down* onto the scalp against a lift spring, so a slack or cut cable, power loss or e-stop all mean "lifted" — the fail-safe is in the geometry. Two STS3215 or gimbal motors sit in a box on the desk; an AS5600 at the head pivot closes the position loop around the cable's hysteresis. Pros: 120 g on the head, motors and heat away from hair, user mobile. Cons: ±30 % force uncertainty unless sensed at the head (§1), cable sway and friction change with head pose, the lift-at-reversal must be sequenced through a cable with 50–100 ms of slack take-up, and a cable is itself a wrap hazard unless fully sheathed to the housing stop (it can be).

```
 desk box [M-stroke][M-lift] ══ housing 1.2 m ══╗
                                              ╔══╝ hard-hat suspension ring
                                  lift spring ║ (pulls UP; cable pulls DOWN)
                                     slide ═══╬═══ return spring
                                      rake ──┴── 3 leaves + TM1 tips
```

### E3 — "Floating Nail": a voice-coil normal axis with zero cogging riding on a rotary stroke

Normal force is the sensory variable the model is least sure about (§3.2, §9.3), and gimbal motors have ~1–2 % cogging. A voice-coil has none. Two cheap sources: the arm actuator from a dead 3.5" hard drive (free; ~30° swing on a 50–60 mm arm = 25–30 mm of travel, coil 10–20 Ω, torque constant tens of mN·m/A, EST) or a 2–3" speaker driver with a pushrod (~$5, Bl ≈ 2–5 N/A so 0.3 N at ~0.1 A and 0.08 W, but only ±3–5 mm of travel). The HDD arm carries one TM1 holder and is swept by a gimbal motor or a crank; the arm's current sets the nail's force to within ~0.005 N with no texture of its own, so whatever "grain" the user feels is real hair and skin. Cons: single nail (a 3-nail rake needs three arms), unknown HDD arm constants until measured, exposed pivot bearing must be shrouded, and speaker drivers lack the travel to follow curvature.

```
    stroke motor ──► ╔═══════════╗ HDD voice-coil magnet yoke (frame-mounted)
                     ║  coil ▣   ║
                     ╚═╤═════════╝
                   arm │ 55 mm, pivot shrouded      current ∝ nail force
                       └──▲ TM1 tip
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~ canopy / scalp
```

### E4 — "Tendon Rake with mechanical lift": one tendon reciprocates, a spring returns, a cam lifts the return

The brief's hybrid. A single desk-box motor (N20 crank or STS3215) pulls a tendon that drives the rake forward along a 40 mm slide on the headgear; an extension spring returns it. The rake bar rides on two short rocker links so that the forward (pulled) stroke pushes the tips down (links lean back, nails engage at 45°) while the spring return lets the links lean forward and lift the tips 8–10 mm — the lift at reversal (H-5.2) is a property of the linkage, not of the controller. Normal force is a dead-weight/constant-force spring in the carrier, so the cap is a mechanical constant. One motor, one cable, mechanically safe, nearly no firmware. Cons: stroke is one-directional and fixed in length (crank radius), the irregularity the sensation model ranks #1 has to come from a crude speed/pause modulation, the rocker-link lift is unloaded only if the return spring is weaker than the tip preload, and force readout is nil.

```
   tendon ──►  ┌──rake bar──┐        pull: links lean back, tips engage ▼
               /            /        return (spring): links lean forward, tips lift ▲
      rocker  /   rocker   /
        ─────┴────────────┴─────  carrier on headgear, CF-spring preload
         ▲ TM1    ▲ TM1    ▲ TM1
```

### W1 — Wildcard (outside the family): "Through-shell magnetic pucks" — no actuator, joint or gap anywhere near hair

A thin smooth PETG/polycarbonate shell (1.5 mm) sits 15–20 mm above the scalp on a ratchet suspension. *Inside* the shell, a small carriage on an MGN9 rail carries a disc magnet. *Under* the shell, a free puck with a steel disc and a TM1 tip on a 0.3 N/mm leaf is held to the shell's underside by the magnet through the shell and dragged by it. The hair sees one smooth shell and one smooth puck: zero joints, zero gaps, zero rotation in the exclusion zone; the magnetic coupling is a contactless slip clutch (shear hold ≈ 1/3–1/5 of axial pull, so a 9 N D61 pair gives ~2–3 N of drag before the puck simply stays behind — set to 0.5–1 N with a 1 mm shim); the puck is the breakaway (it falls off, no tether). Lift at reversal is done by a 2 mm ramp moulded into the shell underside at each end of the stroke that the puck's leaf rides up. Weaknesses: the puck slides on the shell underside, which is a sliding contact in the 50–200 µm band if a hair gets between them (mitigate: three 1 mm hemispherical feet so the puck stands 1 mm off the shell with a > 3 mm open gap elsewhere, but a feet-to-shell pinch is still conceivable); normal force comes only from the leaf preload against the shell standoff (no modulation); and the magnet carriage above still needs a stroke drive (a crank is fine because it is sealed inside the shell). It is radically simpler than E1 in the hair zone and would be the correct SP2 answer if the sensation gate says "a fixed 0.3 N rake with lift already feels like a hand".

```
   ═══════[crank]═══[magnet carriage on rail]═══   sealed inside shell
   ────────────────────────────────────────────    shell 1.5 mm, smooth, 15–20 mm off scalp
                 [steel disc puck] held through shell, drag-limited by magnet shear
                       ╲ leaf 0.3 N/mm
                        ▲ TM1 tip
   ~~~~~~~~~~~~~~~~~~~~~~~~~ canopy / scalp
```

### Selection

| Criterion (brief §13) | E1 Listening Hand | E2 Remote Hand | E3 Floating Nail | E4 Tendon Rake | W1 Pucks |
|---|---|---|---|---|---|
| Expected scratch realism (force fidelity, irregularity, lift) | **high** | medium (hysteresis) | high but 1 nail | medium-low (fixed kinematics) | medium |
| Hair safety | high (empty exclusion zone, 10 ms reflex) | medium (cable near head) | medium (pivot) | high | **highest** |
| Force controllability / readout | **best** | poor | best (1 axis) | none | none |
| Apartment buildability | medium (FOC tuning) | medium-hard | hard (unknown HDD) | **easy** | medium |
| Cost | ~$385 | ~$330 | ~$300 | ~$180 | ~$220 |
| Noise | silent | servo whine in box | silent | box whine | crank inside shell |
| Adjustability / research value | **highest** (everything is a knob) | medium | high on 1 variable | low | low |
| Answers the core question (does force-rendered scratching feel like fingernails)? | **yes, directly** | partly | partly | no (not a force-rendered design) | no |

E1 wins because SP1 is a research rig and E1 turns the top four sensation variables (irregularity, penetration/force, velocity, compliance; scratch-model §7) into firmware knobs with readout, while remaining mechanically bounded. E4 and W1 are kept as the "radically simpler" alternatives the red team should press on; E3's voice-coil axis is a drop-in upgrade to E1's M2 if cogging turns out to be perceptible.

---

## 3. Selected concept: LISTENING HAND (LH-1)

### 3a. Working principle and why it will feel like fingernails

Scratch-model §1.2 lists what separates a scratch from its neighbours: a stiff narrow edge (component B) that reaches the skin through hair, deflecting shafts within 2–5 mm of the root (component A), moved tangentially at 2–20 cm/s with 1–4 Hz reciprocation, at 0.1–0.5 N per contact, on a mount of 0.1–0.5 N/mm, with irregular multi-point rhythm (component C). LH-1 supplies each:

- **Edge**: unchanged SP1-TM1 tips A/B/C/F (0.3 mm radius PETG/nylon/POM blades), presented at 45° (35/55° holder variants). The mechanism adds nothing to the edge: the sound and the micro stick-slip "fizz" come from real keratin-on-hair physics, not from the actuator (the FOC drive is silent, so §8 item 12 is attainable).
- **Reaches the skin**: M2 is a torque source. It descends until the three leaves report (through M2's position) that the commanded force is reached; it does not stop at a programmed height. A tip that lands on a hair bundle sees the leaf (0.3 N/mm) yield first and the arm follow; the model's "penetration" variable becomes a force setpoint plus tip protrusion (30 mm), both adjustable.
- **Light and compliant like a finger**: the effective stiffness seen by the scalp is the series combination of the leaf (0.3 N/mm) and the virtual stiffness of M2 (0.1–1 N/mm by firmware). At K_virtual = 0.3 N/mm the combination is 0.15 N/mm with 8 + 30 mm of travel — softer than a relaxed finger (0.3 N/mm, §3.12), so a 1 mm scalp irregularity changes force by ~0.15 N and head motion of 10 mm by ≤1.5 N (then capped at 2.2 N by physics).
- **Slides, right speed band**: M1 sweeps ±24 mm (adjustable 10–90 mm) at 20–200 mm/s with 1–4 Hz cycles; velocity profile is any shape the pattern engine draws, with acceleration ≤2 m/s² in contact (H-5.4) and faster returns above the skin.
- **Irregular**: PATTERN SPEC v1 (scratch-model §4.4) is implemented as written: per-cycle resampling of stroke length, speed, force, direction drift (M1 arc), pauses, lifts, slow CT-mode episodes. The hand "lands" with a 0.3 s force ramp (P6).
- **Multi-point asynchrony**: three tips on a rigid bar (H-5.6) but with independent leaves: on a convex R ≈ 90 mm scalp the centre tip lands ~2 mm before the outer tips (sagitta over a 40 mm span, tip-interface §6), i.e. 50–100 ms earlier at a 20–40 mm/s descent, and the leaf preloads are set deliberately unequal (0.7×/1×/1.3×, model §4.4) so force spread ≥20 % is guaranteed. Phase spread by independent drive (P4 "spider") is not available in SP1 — see 3j.

The thing this family adds that no spring-and-crank design can: the hand *measures while it scratches*. Force per cycle, lag, contact fraction (from M2 position vs. commanded force) and snags are logged, so the experiment matrix in brief §19N gets data, not just ratings.

### 3b. Architecture

- **Mount**: stationary lean-in frame — a gas-spring VESA monitor arm clamped to a desk edge ($36), carrying a printed spine plate. The seated user sits with the crown under the hand (finger vertical) or, with the module rotated 90° on the arm, with the occiput in front of it (finger horizontal). An optional desk-clamped massage face cradle ($20) steadies the forehead for the crown position. Head withdrawal is the quick-release (safety §5 item 5); nothing is strapped to the head.
- **Coverage**: one hand covers a 50 × 40 mm patch (stroke × rake span) per placement; the user or a helper re-aims the floating monitor arm between episodes, or the user turns the head. Crown and occiput are the targets (scratch-model §5, highest value, simplest curvature); temples/nape are explicitly a later experiment.
- **Contacts**: 3 (20 mm pitch); the rake bar also accepts 1 or 2 holders for the contact-count experiment.
- **DOF**: 2 active (stroke, lift/force), both torque-controlled; 3 passive (leaves); 6 static adjustments on the monitor arm; stroke direction relative to the hair lie set by rotating the module in 15° detents.

### 3c. Kinematics

Geometry: M2 axis 130 mm above the nominal scalp, arm 45 mm horizontal to M1; M1 arm (finger rod) 100 mm down to the rake bar; leaves 45 mm; tip edge 30 mm below the rake-bar underside.

| Parameter | Value | How produced | Adjustable? |
|---|---|---|---|
| Stroke length | 10–90 mm; default 30 mm (P1), 50–90 mm (P2 short sweep) | M1 angle ±3° to ±27° on the 100 mm arm | firmware, per cycle |
| Arc error | tip arc rises 2.9 mm at ±24 mm; scalp falls 3.2 mm → 6 mm total, absorbed by M2 force control + leaves | — | — |
| Attack-angle wander | ±14° at ±24 mm (45° → 31–59°), inside the 25–65° human range | pendulum geometry; curved like a curling finger | holder 35/45/55° |
| Velocity | 20–200 mm/s in contact; up to 300 mm/s lifted return | M1 trajectory generator (trapezoid or minimum-jerk) | firmware |
| Cycle rate | 1–3.5 Hz bidirectional rake (each direction a stroke, lift at each end) | budget at 2 Hz: stroke 25 mm in 170 ms (avg 150 mm/s, peak 200), lift 40 ms, re-entry 40 ms = 250 ms per half-cycle | firmware |
| **Lift-off at every reversal (H-5.2)** | M2 raises the hand 8 mm with commanded force → 0 while M1 is still moving at ≥30 % speed (H-5.3); return above the skin; re-entry at ≤30° plough-in by blending M1 and M2 | impedance target z_ref steps up; lift completes in ~60–80 ms (J = 4×10⁻⁴ kg·m², 0.07 N·m available) | lift height 5–25 mm firmware |
| Full lift / park | 25 mm above canopy every 10–20 s, at every episode change and on any fault | M2 to upper hard stop | — |
| Irregularity | per-cycle resampling: L ±25 %, v ±20 %, F ±30 %, inter-stroke interval ±20 %, direction drift ±20° (small M1 bias plus manual module rotation), pauses 0.3–2 s, episodes 5–20 s; a "periodic control" mode freezes all jitter | pattern engine on the ESP32 (seeded PRNG so a session is repeatable) | firmware, pots for intensity/speed |
| Region change | manual: park, re-aim the arm or move the head; a "nudge" mode advances the stroke centre 10–20 mm per episode along the arc so one placement rasters a 70 mm band | — | — |
| Head motion tolerance | ±15 mm normal (M2 travel ±20° × 45 mm minus margins), ±10 mm tangential (M1 impedance) | force control, no re-aim needed | — |

### 3d. Force path and caps

Force path: motor torque → arm → rod → rake bar → leaf → TM1 holder → tip → skin. No gears, screws, worms or clutches anywhere in it; every element is back-drivable by hand.

**Normal force per hand = L2⁻¹ · τ_M2 − bias**, where the bias is set by a sliding counterweight on the M2 arm:

1. **Config A (default, first human tests)**: counterbalance trimmed to a −0.1 N lift bias. Power off, e-stop, watchdog or stall → the hand rises to the upper stop by itself (red line 8 by spring-return). All scratch force comes from M2 torque; sustained total force ≤0.6 N keeps M2 under ~2 W (fan fitted).
2. **Config B (vigorous settings)**: counterweight slid to a +0.3 to +0.5 N dead-weight bias (safety §3.1 "dead-weight preload… the cleanest cap"). M2 then only modulates and lifts; de-energised state is *limp* (back-drivable axis, safety §4.8) with the dead weight resting on the scalp, and the stationary frame makes the head the release. The firmware refuses Config B unless the counterweight position switch confirms it, and the session log says so.

**Mechanical cap (red line 2).** F_max,normal per hand = τ_stall(12 V)/L2 + bias = 0.107/0.045 + 0.5 = **2.9 N worst case in Config B, 2.1 N in Config A** — τ_stall is a property of Kt, R and the certified 12 V brick, not a firmware value; a 1.5 A fast fuse on each motor branch caps sustained current at ~70 % of stall. Spread over three leaves at 20 mm pitch that is ≤1 N per tip; with a single tip fitted, the whole hand force lands on one nail, so the per-element cap of 2.5 N (safety §2.1) is met in Config A and Config B is firmware-locked to ≤0.3 N bias when fewer than three tips are declared. In addition: **lower hard stop** on M2 at nominal scalp −15 mm (bosses on the shoulder bracket) so the arm cannot drive the leaves to their 8 mm stop even with the head pushed in; **leaf stop** at 8 mm (TPU bumper on the rake bar); **tip breakaway** 4–8 N axial by the TM1 magnet. Positional check required by safety §3.1 item 2: at full M2 descent with the head at the face-cradle limit, leaf compression ≤ 5 mm (margin 3 mm) — a dimension to verify on the wig head before every session.

**Tangential**: F_t,max = τ_stall/L1 = **1.0 N** physical (exactly H-6.5's never-exceed); firmware saturation of the M1 impedance law at 0.4 N (preload band 0.3–0.5 N per H-4.11, set by test); snag flag when the finger lags the reference by > 3 mm with torque saturated for > 20 ms → M2 lifts and M1 holds (never reverses, H-5.9), within ~10 ms of detection. The leaf is stiff in-plane (~100 N/mm), so tangential yield is the hand, not the tip — see 3e item 7.

**Compliance across curvature**: three independent leaves 0.3 N/mm × 8 mm absorb the 2.2 mm sagitta across the 40 mm span plus 5 mm of local shape; M2 absorbs the rest. Total compliant travel 38 mm.

### 3e. Hair safety — 18-item self-score

Exclusion zone (H-6.1): everything within 30 mm of the scalp (design basis); hair reach for 8 cm hair ≈ 100 mm. **Inventory of parts inside 30 mm**: three tips, three TM1 holders, the lower ~20 mm of the three leaves. Inside 100 mm: the leaves' clamped roots, the rake bar, the 10 mm aluminium finger rod. **Joints/gaps inside 30 mm**: (1) TM1 tang-to-pocket seam, fixed gap 0.15 mm/side, 8 mm above the edge, *below* the canopy → **sealed with a 2 mm TPU 85A collar stretched over the holder mouth** (removable for tip swap). (2) Nothing else — the leaf-to-holder junction is a bonded PETG saddle with a ≥1 mm fillet. **Joints inside 100 mm**: (3) leaf-to-rake-bar clamp: fixed, M3 from above, epoxy-filleted (no gap). (4) rake-bar-to-rod clamp: fixed thumbscrew, filleted. **Rotating parts**: M1 bell at 130 mm (rotating cap inside a stationary labyrinth cup, exposed seam is a stationary lip, 0.6 mm clearance — method H-6.2(5)); M2 bell at 130 mm, same treatment, plus a fan shroud. Hair longer than ~11 cm can reach them: **long hair is out of scope for SP1** (§1.9), stated on the rig.

| # | Item | Score | Note |
|---|---|---|---|
| 1 | No rotating surface in zone (gating) | 2 | nearest rotation 130 mm, shrouded |
| 2 | Every zone joint has an exclusion method (gating) | 2 | TM1 seam collared; others bonded |
| 3 | No changing gap / 40 µm–3 mm gap within 25 mm (gating) | 2 | collar covers the only one |
| 4 | Lift before every reversal (gating) | 2 | 8 mm zero-force lift, built into the stroke primitive; H-5.3 timing |
| 5 | Elements in canopy move as a rigid group (gating) | 2 | one rake bar |
| 6 | Radiused blade, drafted root, no re-entrants (gating) | 2 | TM1 family; holder drafted 12° |
| 7 | Mount yields ≤0.15 N tangential on a snag (gating) | **1** | yield is the torque-saturated stroke axis at 0.4 N above zero (physics cap 1.0 N) plus 10 ms lift reflex; not a passive ≤0.15 N element — see risk 5 |
| 8 | Protrusion ≥25 mm | 2 | 30 mm edge to rake-bar underside |
| 9 | Tip spacing ≥8 mm | 2 | 20 mm |
| 10 | Low-friction polished sliding surfaces | 2 | PETG/nylon/POM tips, polished steel leaves; TPU only on the collar above the canopy |
| 11 | Breakaway 3–5 N, no tether | 2 | TM1 magnet 4–8 N (tuned to the low end); nothing wired to the tip |
| 12 | Hair-shedding guard | 1 | the rake bar's convex underside is the only "shell"; the exclusion zone is otherwise empty, so no full guard is fitted |
| 13 | With-grain bias and grain map | 1 | direction is set by rotating the module; firmware carries a per-region "with-grain = +x" flag and limits against-grain strokes to ≤25 mm with lift |
| 14 | Dwell/repetition limits | 2 | ≤8 strokes per ±15 mm patch, nudge mode, comb-out pass |
| 15 | Snag reflex lift-and-retract, never reverse | 2 | impedance lag detector |
| 16 | Antistatic | 1 | steel leaves and rod bonded to PSU ground via a 1 mm wire; tips are insulating PETG (CF-nylon tips as a variant) |
| 17 | Tool-free removal of zone parts | 2 | tips magnetic; rake bar on a thumbscrew |
| 18 | Hair-variant statement | 2 | short–medium straight/wavy in scope; long (>11 cm) and curly out of scope; coarse OK with +force |
| | **Total** | **32/36** | no gating zero |

### 3f. Safety — 13 red lines

1 exposed rotation/open slot in the hair zone: none (3e). 2 mechanical cap ≤2.5 N per element: 2.1 N physical in Config A; Config B ≤2.9 N per hand over three tips and firmware-locked to three tips (3d). 3 ≤12 N total / ≤2 N tangential before yield: 2.9 N total max; 1.0 N tangential physical. 4 NC e-stop in series with motor power, within reach: 22 mm mushroom on the desk under the free hand, in series with the 12 V motor rail between fuse and both SimpleFOC Minis; momentary foot pedal (hold-to-run) in the same loop for all staged tests; ESP32 powered from a buck upstream of the e-stop so it logs the event. 5 no mains inside, ≤24 V, no lithium: Mean Well GST60A12 12 V brick only. 6 nothing anterior to the hairline or near the ear: crown/occiput only; the monitor arm's reach is physically limited by a printed stop ring so the hand cannot swing forward past the vertex. 7 no self-locking drive: direct drive, back-drivable, spring-return lift in Config A. 8 de-energised = lifted (Config A) or limp (Config B, back-drivable, stationary frame). 9 tips positively retained (magnet + pocket), PETG/nylon/POM, proof-loaded 3×. 10 head-mounted mass: zero; release = withdraw head. 11 edges ≥1 mm (rake bar, holders 1.5 mm; tips 0.3 mm as specified). 12 first human session only after the §6 checklist, wig-head test, glasses, ≤5 min. 13 firmware never the only barrier: every S≥3 hazard has a physics cap (stall torque, stops, magnet, fuse).

E-stop/power-loss behaviour, Config A: motor rail → 0 V; M1 limp (the finger hangs plumb); M2 rises under the counterbalance to the upper stop at ~0.1 N-equivalent, i.e. gently, in < 1 s. Encoder alignment at boot (SimpleFOC twitches the rotor ±1 pole) is interlocked: the firmware runs it only with the hand parked on the upper stop and the pedal released, then waits for an explicit "arm".

### 3g. Adjustability

| Variable | How | Range |
|---|---|---|
| Force per nail | pot → F setpoint (×0.5–1.5 intensity), log-displayed; counterweight knob for bias | 0.05–0.6 N firmware; 2.1 N physics |
| Speed / cycle rate | pot; pattern engine | 20–200 mm/s; 1–3.5 Hz |
| Stroke | firmware (per cycle) | 10–90 mm |
| Frequency | coupled to stroke/speed; firmware | 1–3.5 Hz |
| Compliance | firmware K_virtual 0.1–1 N/mm; leaf swap (0.3/0.4 mm stock) | 0.05–1 N/mm effective |
| Angle | holder reprint 35/45/55° (10-minute swap) | 31–59° dynamic wander |
| Contacts | fit 1, 2 or 3 holders | 1–3 |
| Spacing | rake bar reprint (16/20/24 mm) | 16–24 mm |
| Pattern | firmware, seeded; "periodic control" switch | PATTERN SPEC v1 |
| Direction vs lie | rotate module (15° detents) | any |
| Lift height | firmware | 5–25 mm |

### 3h. Components (BOM, US retail, landscape prices unless noted)

| Qty | Item | Unit | Ext. |
|---|---|---|---|
| 2 | iPower GM3506 + AS5048A encoder (M1, M2) | $41.90 | $83.80 |
| 2 | SimpleFOC Mini v1 (DRV8313) | $18 | $36 |
| 1 | ESP32 DevKitC WROOM-32E | $12 | $12 |
| 1 | Mean Well GST60A12-P1J 12 V 5 A | $19 | $19 |
| 1 | 12→5 V buck module for logic (upstream of e-stop) | $4 | $4 |
| 1 | 22 mm NC mushroom e-stop, boxed | $12 | $12 |
| 1 | Momentary foot pedal (hold-to-run) | $10 | $10 |
| 1 | Rocker switch, blade fuse holder, 1.5 A ×4 and 3 A fuses | $10 | $10 |
| 1 | INA219 (motor rail watchdog) | $9.95 | $10 |
| 2+1 | 10 kΩ pots, SSD1306 OLED | — | $10 |
| 2+1 | 10 kΩ NTC on each motor, 30 mm 12 V fan | — | $6 |
| 1 | JST/Dupont/22 AWG silicone wire/heat-shrink | — | $20 |
| 1 | Gas-spring VESA monitor arm, desk clamp | $36 | $36 |
| 1 | Massage face cradle, desk clamp (optional) | $20 | $20 |
| 1 | 10 mm aluminium rod, 100 mm (or acetal) | $5 | $5 |
| 1 | 0.4 mm (0.016") feeler-gauge / spring-steel strip, 8 mm wide | $8 | $8 |
| 1 | Press-on nails (ABS) + Dunlop Tortex 1.14 picks (tips A/C/F) | — | $15 |
| 10 | N52 6×2 mm discs + M3 steel washers (TM1) | — | $8 |
| 1 | Extension spring assortment + M4 rod/nuts/washers (counterbalance) | — | $10 |
| 1 | M3/M4 screws, nyloc, heat-set inserts, thumbscrews (share of assortment) | — | $15 |
| ~250 g | PETG + 20 g TPU printed parts (library or JLC3DP) | — | $40 |
| | **Build subtotal** | | **≈ $390** |
| 1 | Mannequin head with human hair, kitchen scale 0.1 g, FSR 402 | — | $51 |
| | **Total with test gear** | | **≈ $440** |

Substitutes: GM2804+AS5600 for M1 (−$23; tangential cap drops to 0.3 N at 100 mm — too low; use a 70 mm rod); SimpleFOC Shield v3 with current sensing instead of two Minis (+$10; gives true current-mode torque and force readout independent of winding temperature — recommended if budget allows); STS3215 for nothing (no geared servo in the force path).

**Printed parts** (PETG unless stated, 4 perimeters, 0.2 mm layers):

| Part | Approx. size | Notes |
|---|---|---|
| Spine plate (VESA 100 adapter) | 110 × 110 × 6 mm | 4× M4 to the arm, slots for the shoulder bracket |
| Shoulder bracket (M2 cradle) with upper/lower stop bosses and counterweight rail guide | 70 × 60 × 35 mm | M2 stator bolts; stop bosses M3-adjustable |
| M2 arm with bell flange, 45 mm c-c, counterweight rail 70 mm opposite | 130 × 22 × 8 mm | bolts to the GM3506 rotor's threaded holes |
| M1 cradle (stator mount) on the arm end | 45 × 45 × 20 mm | |
| M1 rotating cap with 10 mm rod socket | Ø46 × 20 mm | glued/bolted to the bell; socket coaxial ±0.2 mm |
| M1 stationary labyrinth cup | Ø56 × 24 mm | 0.6 mm radial clearance to the cap |
| M2 cap + labyrinth cup + fan shroud | Ø46/Ø56, 40 × 40 fan ring | |
| Rake bar / palm shell | 62 × 22 × 14 mm, convex underside R 60 | 3 leaf slots at 20 mm, M3 clamps from the top, thumbscrew rod clamp |
| TM1 holder blocks ×3 (+3 spares at 35°/55°) | 16 × 12 × 14 mm | 45° pocket, 6.2 mm magnet pocket, leaf saddle, 12° draft |
| TPU 85A seam collars ×6 | Ø12 × 4 mm | |
| Counterweight cup | Ø20 × 15 mm | holds M4 washers |
| Electronics box with e-stop mount | 130 × 90 × 50 mm | |
| Arm reach stop ring | Ø40 × 10 mm | clamps on the monitor arm joint |

### 3i. Buildability in an apartment

Tools: landscape §8 kit (soldering iron, calipers, hex keys, needle files, deburring tool, multimeter, CA, epoxy, threadlocker) plus a 10× loupe and a hacksaw/shears for the leaves. No lathe, no mill, no drill press.

Steps (≈ 28–36 h over 2–3 weeks, dominated by print lead time and FOC tuning):
1. Order (Day 0): iFlight (motors), SimpleFOC/Amazon (Minis, ESP32, PSU, e-stop, pedal, arm, cradle, rod, feeler stock, magnets, springs, fasteners), Mouser (Mean Well). Submit the print batch (library same week; JLC3DP as the PETG backup).
2. Bench FOC bring-up (4–6 h): one motor on the bench, SimpleFOC `MotorFOC` example, find pole pairs (11) and encoder direction, tune velocity/position PIDs with the arm free. Repeat for the second motor on the second MCPWM bank, two CS lines on one SPI bus.
3. **Kt measurement (1 h, Day-1 gate)**: arm horizontal, command 0.2/0.4/0.6 A, rest the tip on the kitchen scale; τ = F·L. Record Kt and R (multimeter, phase-to-phase/2). Every force number in the firmware limits table derives from these two measurements.
4. Mechanical assembly (4 h): cut three leaves 45 × 8 mm, radius the corners (1 mm), polish; bond each to a TM1 holder saddle with epoxy, fillet; clamp into the rake bar; fit the rod, caps, labyrinth cups, arm, counterweight rail. Check: finger hangs plumb; M2 arm swings freely between stops; trim the counterbalance so the unpowered hand rises slowly.
5. Electronics (4 h): 12 V → fuse → e-stop (NC) → pedal → rail → two Minis; buck → ESP32 upstream of the e-stop; INA219 on the rail; pots, OLED, NTCs, fan; INA219 star ground. Verify with the multimeter that the rail is 0 V with the e-stop pressed or the pedal released while the ESP32 stays up.
6. Impedance firmware (6–10 h): torque-mode drivers; per-axis impedance law with gravity/bias compensation; limits table; lift-at-reversal primitive; snag detector; pattern engine (PATTERN SPEC v1); logging over USB serial.
7. Calibration (2 h): hand on the kitchen scale: commanded F vs. measured F at 0.1–1.0 N, three leaf preloads; lift height vs. encoder; thermal run (step 3j, risk 2).
8. Hair bench (3 h): hair-interaction §7.3 tests 1–8 on the mannequin head; tethered-strand yield test with 15 g and 50 g weights.
9. Safety checklist (safety §6) and staged exposure (forearm, palm, scalp 2 min).

Risky tolerances: (a) rod socket coaxiality in the M1 cap (a 0.5 mm offset makes the tip wobble 0.5 mm per revolution-equivalent — check by spinning the cap by hand before gluing); (b) labyrinth clearance 0.6 mm (print the cup 0.3 mm oversize and sand); (c) leaf clamp must have no gap after epoxy (probe with 100 µm fishing line, safety §6B); (d) monitor-arm stiffness — a cheap arm may bounce at 2 Hz with a 350 g module; the reaction force is only ~0.3 N but the lever is long; test on the wig head and add the reach stop ring; (e) encoder magnet (pre-mounted on iFlight units — do not disassemble).

### 3j. Weaknesses, top 5 risks, retiring tests

Honest weaknesses: no independent per-finger drive (P4 impossible); only one hand → 50 × 40 mm per placement and manual region changes; M2 heats at the vigorous end; voltage-mode torque drifts ~8 % per 20 °C of winding temperature (NTC compensation, or the current-sense Shield); FOC bring-up is a real skill gate for a first-timer (two evenings with the SimpleFOC docs); the tangential snag yield relies on the actuator rather than a passive ≤0.15 N element; long and curly hair out of scope; the face cradle makes a 20-minute session less relaxing than a chair.

| # | Risk | Bench test that retires it |
|---|---|---|
| 1 | A rigid 3-nail rake on one stroke reads as "a machine" despite jitter (model §4.3) | Blind A/B on the scalp: 1 vs 3 tips, equal vs 0.7/1/1.3 leaf preloads, periodic vs jittered; if 3-rigid loses to 1-jittered, SP2 adds a 3 g voice-coil per leaf for phase spread |
| 2 | M2 overheats at sustained >0.6 N (2.6 W at 0.75 N, EST) | 20-min bench run at 0.75 N and 1.0 N with IR thermometer and NTC log; pass = winding ≤ 70 °C, housing ≤ 48 °C; mitigations: fan, Config B dead-weight bias, GM4108, SimpleFOC Shield (lower R loss not helped, but true current limit) |
| 3 | Cogging/friction ripple (±0.02–0.03 N) is perceptible as "grainy" or heard as hum | Tip on a 100 g load cell + HX711, sweep at 50 mm/s, FFT; pass = ripple < 10 % of setpoint; mitigations: SimpleFOC anticogging table, E3 voice-coil M2 |
| 4 | Head motion or monitor-arm bounce exceeds ±15 mm and the hand loses contact or spikes | Wig head on a wobble board, ±10 mm at 0.5 Hz; log force; pass = force within ±30 % of setpoint, no stop hits; mitigation: face cradle, stiffer arm, K_virtual lower |
| 5 | Tangential snag yield at 0.4 N (not ≤0.15 N) plucks a hair before the 10 ms reflex | Tethered-strand test (hair-interaction §7.3.6) with 15 g and 50 g: pass = 50 g never lifts, lift reflex fires before 15 g lifts; mitigations: F_sat 0.3 N, add a magnetic lateral detent between rake bar and rod (yields at 0.3 N, swings 10 mm) |

### 3k. Massager-vs-scratcher self-score (scratch-model §8)

1 Edge not pad — PASS (TM1 blades). 2 Reaches the skin — PASS/UNSURE (force-controlled descent, 30 mm protrusion; contact fraction in 5–10 cm hair is logged and UNKNOWN until test 7.3.1). 3 Light — PASS (0.05–0.6 N per nail; total ≤2.1 N physics). 4 Slides — PASS (10–90 mm tangential, scalp slip < 1 mm at these forces). 5 Right speed band — PASS (20–200 mm/s, 1–3.5 Hz, no component > 20 Hz; the FOC loop is silent and the tremor option is off by default). 6 Deflects hair near the root — PASS (edge at skin, 45°). 7 Multiple independent contacts — UNSURE (3 at 20 mm, force spread ≥20 % by leaf preload, phase spread ~50–100 ms by curvature, but no independent drive). 8 Irregular — PASS (full PATTERN SPEC v1 with a periodic control condition). 9 Compliant at the tip — PASS (0.15 N/mm effective, 38 mm travel). 10 Unloads at reversal / lifts between bouts — PASS (8 mm zero-force lift every reversal; 25 mm park every episode). 11 Hair-safe geometry — PASS (3e). 12 Sounds like a scratch — PASS/UNSURE (no gears; verify ≤60 dBA and that the scratch hiss is audible over the fan).

Sanity row (model §1.2): line contact 0.3 mm radius × 4–6 mm, 0.1–0.5 N, slip 10–90 mm at 3–20 cm/s, 1–3.5 Hz, parts the canopy — first column.

---

## 4. SVG schematic — LH-1 side view (not to scale; stroke direction is left–right; the three tips sit in a row perpendicular to the page)

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 780 500" width="780" height="500" font-family="Helvetica, Arial, sans-serif" font-size="11">
  <defs>
    <marker id="ah" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#333"/></marker>
  </defs>
  <!-- scalp and hair canopy -->
  <path d="M 40 452 Q 300 392 560 452" fill="none" stroke="#8b5a2b" stroke-width="3"/>
  <text x="44" y="470" fill="#8b5a2b">scalp (R ≈ 90 mm, crown)</text>
  <g stroke="#555" stroke-width="1">
    <line x1="80" y1="440" x2="92" y2="420"/><line x1="110" y1="432" x2="122" y2="412"/><line x1="140" y1="426" x2="152" y2="406"/>
    <line x1="170" y1="420" x2="182" y2="400"/><line x1="200" y1="415" x2="212" y2="395"/><line x1="230" y1="411" x2="242" y2="391"/>
    <line x1="260" y1="408" x2="272" y2="388"/><line x1="330" y1="407" x2="342" y2="387"/><line x1="360" y1="409" x2="372" y2="389"/>
    <line x1="390" y1="413" x2="402" y2="393"/><line x1="420" y1="418" x2="432" y2="398"/><line x1="450" y1="424" x2="462" y2="404"/>
    <line x1="480" y1="431" x2="492" y2="411"/><line x1="510" y1="439" x2="522" y2="419"/>
  </g>
  <text x="400" y="384" fill="#555">hair canopy (pile 5–20 mm)</text>
  <!-- exclusion zone and hair reach lines -->
  <line x1="40" y1="372" x2="600" y2="372" stroke="#c00" stroke-dasharray="6 4" stroke-width="1"/>
  <text x="44" y="368" fill="#c00">30 mm hair-exclusion zone: only tips, holders and leaves below this line</text>
  <line x1="40" y1="286" x2="600" y2="286" stroke="#c60" stroke-dasharray="3 4" stroke-width="1"/>
  <text x="44" y="282" fill="#c60">hair reach for 8 cm hair (≈100 mm): no rotation below this line</text>
  <!-- tip, holder, leaf -->
  <line x1="300" y1="404" x2="287" y2="391" stroke="#000" stroke-width="3.5" stroke-linecap="round"/>
  <text x="306" y="408">TM1 tip A, 45°, edge R 0.3 mm (×3 at 20 mm pitch)</text>
  <polygon points="287,391 279,383 268,390 276,398" fill="#ddd" stroke="#000" stroke-width="1"/>
  <text x="306" y="392">TM1 holder + magnet (seam collared, TPU)</text>
  <path d="M 272 386 C 262 372, 272 352, 290 346" fill="none" stroke="#06c" stroke-width="2.5"/>
  <text x="186" y="372" fill="#06c" text-anchor="end">leaf spring 0.4×8×45 mm</text>
  <text x="186" y="384" fill="#06c" text-anchor="end">0.3 N/mm, 8 mm travel</text>
  <!-- rake bar / palm -->
  <path d="M 258 332 L 322 332 L 322 342 Q 290 352 258 342 Z" fill="#eee" stroke="#000" stroke-width="1.5"/>
  <text x="330" y="342">rake bar / palm shell (convex, R ≥ 1 mm edges)</text>
  <!-- finger rod -->
  <rect x="285" y="214" width="10" height="118" fill="#ccc" stroke="#000"/>
  <text x="300" y="300" fill="#000">finger rod Ø10 mm Al, 100 mm, smooth</text>
  <!-- M1 -->
  <circle cx="290" cy="196" r="28" fill="none" stroke="#000" stroke-width="1.2" stroke-dasharray="4 3"/>
  <circle cx="290" cy="196" r="22" fill="#f4d9a8" stroke="#000" stroke-width="1.5"/>
  <circle cx="290" cy="196" r="3" fill="#000"/>
  <text x="212" y="176" text-anchor="end">M1 stroke: GM3506 direct drive</text>
  <text x="212" y="188" text-anchor="end">torque mode, cap 1.0 N tangential</text>
  <text x="212" y="200" text-anchor="end">rotating cap inside stationary</text>
  <text x="212" y="212" text-anchor="end">labyrinth cup (dashed)</text>
  <!-- M2 arm -->
  <rect x="290" y="190" width="54" height="12" fill="#bbb" stroke="#000"/>
  <text x="296" y="186">arm 45 mm</text>
  <!-- M2 -->
  <circle cx="344" cy="196" r="28" fill="none" stroke="#000" stroke-width="1.2" stroke-dasharray="4 3"/>
  <circle cx="344" cy="196" r="22" fill="#f4d9a8" stroke="#000" stroke-width="1.5"/>
  <circle cx="344" cy="196" r="3" fill="#000"/>
  <text x="372" y="236">M2 lift/force: GM3506, torque mode,</text>
  <text x="372" y="248">cap 2.1 N normal (τ_stall / 45 mm); fan + NTC</text>
  <!-- counterweight rail -->
  <rect x="344" y="193" width="80" height="6" fill="#bbb" stroke="#000"/>
  <rect x="396" y="184" width="18" height="24" fill="#999" stroke="#000"/>
  <text x="372" y="176">counterweight knob: −0.1 N lift bias (A) … +0.5 N dead weight (B)</text>
  <!-- hard stops -->
  <rect x="268" y="150" width="14" height="8" fill="#c00"/>
  <rect x="268" y="234" width="14" height="8" fill="#c00"/>
  <text x="212" y="156" text-anchor="end" fill="#c00">upper hard stop (park, +25 mm)</text>
  <text x="212" y="240" text-anchor="end" fill="#c00">lower hard stop (scalp −15 mm)</text>
  <!-- counterbalance spring -->
  <polyline points="300,184 304,170 296,160 304,150 296,140 304,130 300,118" fill="none" stroke="#090" stroke-width="2"/>
  <text x="308" y="124" fill="#090">counterbalance spring (unpowered: hand rises)</text>
  <!-- shoulder bracket and spine -->
  <rect x="318" y="140" width="52" height="112" fill="none" stroke="#000" stroke-width="1.2"/>
  <rect x="440" y="100" width="12" height="190" fill="#ddd" stroke="#000"/>
  <line x1="370" y1="150" x2="440" y2="150" stroke="#000" stroke-width="3"/>
  <line x1="370" y1="240" x2="440" y2="240" stroke="#000" stroke-width="3"/>
  <text x="458" y="110">spine plate → gas-spring monitor arm → desk clamp</text>
  <text x="458" y="122">(stationary lean-in frame; head withdrawal = release)</text>
  <line x1="452" y1="130" x2="600" y2="60" stroke="#000" stroke-width="4"/>
  <rect x="596" y="40" width="60" height="30" fill="#ddd" stroke="#000"/>
  <text x="600" y="58">arm</text>
  <!-- motion arrows -->
  <path d="M 236 356 Q 290 372 344 356" fill="none" stroke="#333" stroke-width="1.5" marker-start="url(#ah)" marker-end="url(#ah)"/>
  <text x="236" y="352" fill="#333">stroke ±24 mm (M1), 20–200 mm/s, lift 8 mm at each end</text>
  <line x1="236" y1="300" x2="236" y2="260" stroke="#333" stroke-width="1.5" marker-start="url(#ah)" marker-end="url(#ah)"/>
  <text x="120" y="283" fill="#333">lift / force (M2)</text>
  <text x="120" y="295" fill="#333">±15 mm head motion</text>
  <!-- e-stop -->
  <rect x="640" y="400" width="110" height="70" fill="#f8f8f8" stroke="#000"/>
  <circle cx="665" cy="425" r="12" fill="#c00"/>
  <text x="684" y="420">NC e-stop</text>
  <text x="684" y="432">+ foot pedal</text>
  <text x="646" y="456">in series with 12 V</text>
  <text x="646" y="466">motor rail</text>
  <text x="40" y="490" fill="#333">LH-1 "Listening Hand" — Team E — nothing within 30 mm of the scalp moves relative to anything else; both motors are torque sources with physical caps.</text>
</svg>

---

## 5. Summary for the Director

**Concept: LH-1 "Listening Hand"** — two silent, back-drivable GM3506 gimbal motors under SimpleFOC render a 3-nail SP1-TM1 rake as a programmable spring (0.05–0.6 N per nail, 0.1–1 N/mm) that follows the scalp, lifts at every reversal and retracts on a snag, hanging from a desk-clamped monitor arm over the seated user's crown or occiput. **Cost ≈ $390** build (+$50 test gear). **Contacts: 3** at 20 mm (1–3 selectable). **Coverage: 50 × 40 mm** per placement, crown and occiput, manual re-aim. **Physical caps**: 2.1 N normal per hand, 1.0 N tangential, from stall torque through 45/100 mm levers — no firmware in the chain. **Hair checklist 32/36**, no gating zero; **massager checklist** 10 PASS, 2 UNSURE. **Biggest risk**: a rigid 3-nail rake on a single stroke may still read as "a machine" despite full pattern jitter — retired by a blind 1-vs-3-tip, periodic-vs-jittered scalp A/B; second is M2 heating above 0.6 N sustained (2.6 W at 0.75 N), retired by a 20-minute thermal run with fan and the dead-weight bias config. Keep W1 (through-shell magnetic pucks) and E4 (tendon rake with linkage lift) as the radically simpler fall-backs if the sensation gate says force rendering is not what makes it feel like fingernails.
