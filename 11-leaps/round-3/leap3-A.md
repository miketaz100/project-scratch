# LEAP 3-A — How the pad travels on a helmet without wrecking its balance

Leap-3 agent A · Project SCRATCH · 2026-10-02.
**Read:** the brief's list. Firewall kept.
**Tags:**
- [KNOWN] sourced;
- [EST] computed here, with Python in the session scratchpad. The model is an ellipsoid head, a/b/c = 96/75/88 mm about the skull centre C, with every legal pad pose on a 5° grid and ±20° of head tilt;
- [UNKNOWN] needs a bench.

---

## 0. What actually tips the helmet

**Frame.** C is the skull centre, 45 mm above and 10 mm behind the ear canal, so the ear axis passes through C. Pitch α runs from vertical toward the back, and latitude β runs toward an ear. The pad's centre of mass (CoM) sits at the scalp + 40 mm, which is 128–136 mm from C.

| Moment about C [EST] | Size | Character |
|---|---|---|
| **Pad gravity offset** (pad + carriage + bail) at the occiput | **0.17–0.23 N·m** (105–150 g pad) | static; changes with travel; "the hat leans" |
| Scrub drag (4 pins × 0.55 N × µ 0.5 at 0.1 m) | 0.11 N·m | oscillates at 1–3 Hz |
| Tilt of the whole helmet (M·g·h·sin 20°, h ≈ 33 mm) | 0.03–0.06 N·m | static |
| Hop of 200 mm/s in 0.1 s | 0.035 N·m | impulse, pins lifted |
| Drift of 2–5 cm/s, or an 80 mm/s sweep ramped over 0.2 s | 0.002–0.007 N·m | negligible |
| Umbilical (hanging share at a 90 mm lever) | 0.015 N·m | static |

**Hold.** Concept-A §3.2 gives µ·ΣN·R = 0.49 N·m at µ 0.3 with 3 N of preload per pad [KNOWN]. At **4 N per pad**, ΣN ≈ 22 N, which gives **0.59 N·m** (0.99 at µ 0.5) at a mean pad pressure of 3.5 kPa, inside the 5 kPa limit [EST].

**Finding 1: the travel drive's reaction torques are 20–50× smaller than the pad's gravity offset.** For a drifting pad, balance is a centre-of-mass problem, not a reaction problem.

**Finding 2: a static trim makes things worse.** Moving the 70 g motor pack into the visor took the worst case from 0.174 to 0.219 N·m. 60 g of dead trim gave 0.212 [EST]. Coverage runs from the hairline (α −50 to −70°) to the occiput (+100°), nearly symmetric front to back, so a fixed offset only moves the worst case to the other end. **The wander has to be cancelled by something that moves.**

**Finding 3: the head has no opposite side for the occiput.** Reflecting the occiput through the vertical axis lands on the face, so a mirroring counter-mass must stop at the hairline fence (red line 6).

---

## 1. Round-2 topologies transplanted onto a helmet

| Topology | Moving mass [EST] | Singularity | Hair zone | Verdict |
|---|---|---|---|---|
| **Ear-axis bail** (pitch α about the ear axis, carriage along β): leap2-A L1 on the head | bail 23 + carriage 10 + pad | at the ears, which are already fenced | bail ≥ 65 mm off the scalp; hubs sealed, 35 mm lateral | **base** |
| Latitude ring + meridian arc | + ring rotor ~40 g | **at the crown whorl**: the pad must spin to pass the pole | ring bearing at band level, in long hair | reject |
| Fixed arch rails with a self-propelled carriage | + 25–30 g moving; 75 g fixed, high | none | outside the zone | reject: coverage only 35–45 % in strips |
| **Twin half-bails**, one per hemisphere (L2) | 2 × (14 + 10 + pad) | at the ears | as the bail | **the leap** |

Two more were rejected. A ring above the crown on a rear spine also puts the singularity on the crown and raises the CoM 60–80 mm. A cable polargraph needs a shell of ~250 g. A skull-centred two-ring gimbal's outer ring would pass under the chin, so it reduces to the ear-axis bail.

---

## LEAP 1 — CAPSTAN HUBS ON THE EAR AXIS: motors on the suspension, only a 23 g whisker and the pad move

**(a) Assumption broken.** That the travel motors ride the arc or carriage and the scrub drive rides the pad. The brief's path synthesiser adds ~40–55 g to the pad (leap2-B L3/L4), and leap2-E's 105 g moving group gives 49 mm of wander.

**(b) Principle.**
- **Hub pods.** Two pods sit on the band on the ear axis, 110 mm off the midline (35 mm outboard of the scalp, ≥ 60 mm from each canal). Each pod's inner face is the parietal suspension pad.
- **Pitch α (left pod).** A 2804-class gimbal motor under FOC with an AS5600 encoder drives a Ø 48 mm sector through a **Dyneema capstan at 8:1**. The drive has no gears, no backlash, and can be back-driven.
- **Latitude β (right pod).** A second motor drives a Dyneema loop running **inside** the hollow carbon bail. The pitch coupling (8/165 = 0.05 rad/rad) is removed in firmware.
- **Spring balance.** A zero-length spring in each pod (k·d·e = m·g·r, 0.22 N/mm at d = e = 25 mm) balances the bail for an upright head. Unpowered, the bail stays put instead of swinging down with ~0.2 J, 4× the 50 mJ limit.
- **Pad.** The pad is leap2-C C1's **synchro slave**. The two-motor path synthesiser moves to the desk as the **master**. Three sealed lines copy any planar translation (circle, 30 mm line, precessing line, heading jump), because the bellows volumes sum to a constant for every (x, y). The head carries only bellows and flexures.

```
 FRONT VIEW, upright head
            .-~~~~~~~~~~~[carriage]~~~~~~~~~-.   bail R165, carbon 10×8, β-loop inside
          .'               ║ radial park piston '.     (50 mm, spring-out)
         /            pad ▼▼▼▼  synchro slave,   \     12 pins, palm skids, 105 g, no wires
  [HUB L]●═════ ear axis through C ══════════════●[HUB R]
  α motor  ( .-""""""-. )   hub pad = parietal   β motor        DESK: path-synth MASTER
  capstan  |    C     |     suspension pad       capstan        (2 one-way N20s → 3 syringes),
  balancer  '-.____.-'      ≥ 60 mm above canal  balancer       valves, pump
      ear ●        ● ear   band 4 N/pad · forehead pad · nuchal cradle (rear)
```

**(c) Variables moved.**

| | Motorised pad | L1 |
|---|---|---|
| Moving mass | 176 g | **138 g** |
| Worst gravity moment | 0.228 N·m | **0.174 N·m (−24 %)** [EST] |

- **Carriage motor penalty.** A latitude motor riding the carriage would add +0.05 N·m.
- **Low CoM.** The helmet CoM is ~33 mm above C, against 122 mm for the concept-A portal, so 20° of tilt adds only 0.005 N·m.
- **Sound (rank 15).** An FOC gimbal motor at 20–30 dBA at 0.3 m gives **34–44 dBA at the canal** (60 mm away). A geared bus servo in the same place gives 59–64 dBA, which fails the 60 dBA target [EST].

**(d) Plausibility [EST].**
- **Pitch torque.** Unbalanced, the bail needs 0.18 N·m against gravity plus 0.11 N·m of drag, 0.29 N·m peak. Through 8:1 that is 0.036 N·m at the motor, inside the 2804 class (vendor value to check). Balanced, the peak is ≈ 0.17 N·m.
- **Speed.** Drift is 0.15–0.38 rad/s and sweeps are 0.6 rad/s at the bail.
- **Synchro stiffness.** 2–3 N/mm, so 1 N of drag costs 0.4 mm of path.
- **Bail stiffness.** A 1 N tip load deflects a 260 mm arm (EI ≈ 2 × 10⁷ N·mm²) by ≈ 0.3 mm.

**(e) Cheapest experiment (≈ $45, a weekend).**
1. Build one hub on a $15 hard-hat suspension: a printed pod, a wire bail at R 165, a 105 g coin pad, a gimbal motor with a SimpleFOC mini and AS5600 ($25), a Dyneema capstan and a pen-spring balancer.
2. On a wig head, measure:
   - dBA at the ear;
   - drift tracking from a pen trace;
   - drift with the power off.
3. **Pass:** ≤ 40 dBA, ±1 mm, and < 5°/min unpowered.

**(f) Replaces or combines.**
- It replaces leap2-E's arc motors and leap2-B's motors on the pad.
- It **rejects leap2-E L2 (travel motors drawing the orbit) on a helmet.** A ±12° oscillation at 1 Hz puts 0.15 N·m peak into four feet of 1 N/mm. That rocks the helmet 0.27°, which is **0.4 mm at the forehead skin at 1 Hz**, above vibrotactile threshold [EST]. The scrub belongs in the pad, and the bail only drifts.

**(g) Why it might fail.**
- Synchro bellows may fatigue or buckle, and line viscosity rounds the line ends at ~3 Hz.
- Bone-conducted hum through the hub pad is untested.
- The 0.17 N·m lean is still there. L2 exists to remove it.

---

## LEAP 2 — THE SECOND HAND IS THE COUNTERWEIGHT: twin half-bails in point mirror

**(a) Assumption broken.** That balance needs a counter-mass, and that a counter-mass is dead weight (the brief's valve pack, motors or battery).

**The gram trade for cancelling the worst case, 17.7 g·m (0.174 N·m) [EST]:**

| Counter-mass | Lever | Grams | Cancels | Verdict |
|---|---|---|---|---|
| Rotor inside an ear-hub housing | ≤ 45 mm | **≈ 395** | pitch | ✗ |
| Slug in a sealed band channel, fusee-coupled to α | 80–100 mm | 180–225 per axis | pitch | ✗, and roll needs a second |
| Counter-bail under the visor (stop at −40°, R 180) | 116 mm | ≈ 153 | pitch, limited at the front | too heavy |
| **Valve pack** (12 × S070, manifold, sensors) on a brim shuttle | 90 mm | it is 110 g: **56 %** | pitch | ✗: ~510 g (red line 10), solenoid clicks at the ear |
| **Drive motors** as a cable shuttle | 90 mm | 70 g: **36 %** | pitch | partial |
| **Battery** | — | — | — | ✗ red line 5 (no lithium) |
| Dead slug on a mirror half-bail, parking out to R 205 | ≤ 205 mm | +100 all-in | 55–80 % | dead weight |
| **Second working pad on a mirror half-bail** | its own r; ×1.3 when parked out | **+86 all-in** | **≈ 100 %** | **chosen** |

A useful counter-mass must sit as far from C as the pad does. The only thing that can go there is another pad.

**(b) Principle.**
- **Two half-bails.** Split the bail at the top into left and right half-bails on the same ear axis. Each has a pitch motor in its hub.
- **One latitude motor.** It drives both carriages through a crossed loop, so **β_R = −β_L**. The right loop's wrap sense is reversed, so the pitch coupling mirrors too.
- **Point mirror.** Firmware commands **α_R = −α_L**. Pad B is then pad A rotated 180° about the vertical through C, since u(−α, −β) = R_z(180°)·u(α, β), and the pair's CoM stays on that vertical.
- **When the mirror would hit the face** (A on the occiput puts B on the face), B stops at the hairline fence. Its radial piston **parks it 40 mm outward** (vented, spring-out), which raises its lever 1/sin 50° ≈ 1.3×, and it still balances A. Parked is the de-energised state (red line 8).

```
 SIDE VIEW: A scratching the left occiput, B parked over the right front-top
         visor guard  [B] parked +40 mm, ≥ 60 mm above the brow
        ┌─────────╲    ║  .-~~~~~~~~-.     half-bail R swings forward
   brow │ fence    ╲  .'     C ●       '.   half-bail L swings back
        │ α −50°    |     (ear axis ⊙)   |▼▼▼ [A] α +90°
                     '.                .'◄─ nuchal cradle;  nape plug ─► umbilical down the back
 PLAN, mirror mode at the sides:  B ▼▼▼ (β −55°)   ●C   ▼▼▼ A (β +55°)  both stroke "up toward the crown"
```

**Pneumatics stay the size of one hand.**
- **Shared valves.** Each pad is 6 pins as two 3-nail half-plates (L3). At the nape-plug manifold, desk valve *k* tees to pin *k* on both pads, so **6 valves drive 12 nails**. The 3 synchro lines tee to both slave plates. Each pad has its own palm (radial) line.
- **Interlock.** A 4 g diaphragm pilot feeds a pad's pins **only while its palm line is pressurised**. A parked pad cannot fire into air, and no pin can chase a lifted head.
- **Drag.** Identical pads mounted R_z-symmetric make R_z-rotated motions, so their drag moments cancel in pitch and roll and add only in yaw. "Up toward the crown" on the left maps to "up toward the crown" on the right, which is consistent with the hair lie.

**(c) Variables moved [EST].**

| | Single (L1) | Twin (L2) |
|---|---|---|
| CoM wander | **84 mm** front–back, 65 mm sideways | **7 mm** |
| Worst gravity moment, upright | 0.178 N·m | **0.027 N·m** |
| Worst gravity moment, ±20° tilt | 0.18 N·m | 0.105 N·m |

- **Where B is.** Across A's legal positions, B is an exact mirror and scratching **76–81 %** of the time and parked out 12–18 %. The worst residual is **0.026 N·m**, with A on the occiput midline.
- **Sensory gain: two hands at once.** Two separated contact zones at once is ranks 6 and 13 together, and mirror-stroking both sides is how people scratch someone else's head [UNKNOWN on Michael].
- **Fewer parts.** 11 tubes (6 + 3 + 2) and **6 S070s ($204)**, against 16 tubes and 12 valves ($408) for a 12-pin single.

**(d) Plausibility. Mass ledger [EST; weigh everything]:**

| Item | g |
|---|---|
| Band + rear dial ratchet | 50 |
| 4 pads: forehead, 2 parietal (on the hubs), nuchal cradle | 30 |
| 2 hub pods (thin bearings, sectors, balancers) | 40 |
| 3 gimbal motors + encoders + 3-channel FOC board | 88 |
| 2 half-bails | 28 |
| 2 carriages with park piston | 20 |
| **2 pads** (6 pins, split plates, bellows, palm, pilot) | **150** |
| Visor guard / doff handle | 15 |
| Chin strap + 12 N fuse | 14 |
| Nape plug + tee manifold + umbilical share | 25 |
| Wiring, fasteners | 15 |
| **Total** | **≈ 475** |

- **Mass margin.** 25 g under red line 10. Concept-A found that ledgers under-count, so L4 is the reserve. The single-hand L1 helmet is **≈ 394 g** on the same band and hubs.
- **Air.** Sharing doubles the swept volume per valve. With hover-and-bite (leap2-F L3: 5 mm bites, ¼ of the air), a landing still takes ≈ 14 ms through 0.5 mm² (leap2-C basis). 12 pins × 0.28 ml × 3 landings/s is ≈ 0.6 L/min, so one KPM27C.
- **Collision.** Only near the vertex (α_L ≈ α_R, β ≈ 0). Firmware holds |β| ≥ 15° there, which puts the two hands either side of the whorl; soft bumpers are the backstop.
- **"Both hands on the occiput"** is a deliberate non-mirror burst at 0.25 N·m. With the hands in antiphase the drags cancel, so the demand is 0.27 against 0.59. The fatigue ledger (leap2-D D5) keeps it short.

**(e) Cheapest experiment (≈ $20, an evening, a partner).**
1. **Balance.** On the hard-hat suspension, tape 100 g of coins at the left occiput. Wear it for 15 min of TV and score lean (0–10) and forehead slip (pen line across skin and band). Repeat with 75 + 75 g in the twin pose (left occiput, right front-top parked out). **Pass:** lean ≤ 2 and slip ≤ 1 mm.
2. **Hands.** Blind, 2 min each, with the partner using one hand, two hands in mirror lockstep, then two hands independently. Rate pleasure and "is this a person?" **Pass:** lockstep ≥ one hand and within 1 point of independent.

**(f) Combines.** It replaces every counter-mass and the "hat leans toward the pad" penalty. It needs L1's hubs and synchro pad, and the palm datum.

**(g) Why it might fail.**
- **Lockstep may read as a machine.** Two hands that start, stop and turn in perfect sync may feel uncanny. The 3-motor kinematics can break the mirror, but shared valves cannot. The fix is per-pad valves: +6 valves, +6 tubes.
- **Thin margin.** 475 g leaves little slack.
- **B parks 15–25 % of the time.**
- **Two pads mean twice the shedding surfaces near long hair.**

---

## LEAP 3 — A SCRUB THAT CANCELS ITSELF: no 1.5 Hz hat jiggle

**(a) Assumption broken.** That scrub drag doesn't matter on a helmet because 0.11 N·m ≪ 0.59. For holding that is true. For feeling it is not. Concept-A's feet are ≈ 1 N/mm in shear [KNOWN], so 0.11 N·m at 1.5 Hz rocks the helmet ≈ 0.19°: **±0.3 mm at the forehead pad on every stroke**. That is above the tens-of-µm low-frequency vibrotactile threshold [EST]. The forehead reports the machine's metronome while the nails try to be a person.

**(b) Principle.** Split each pad's plate into two half-plates on the same three synchro lines, with half B's bellows mounted on the opposite faces. B then moves in exact antiphase (x_B = −x_A) with no extra tube. The drags reduce to a couple of 1 N × ~30 mm = **0.03 N·m in yaw**, against 0.11 N·m in pitch. This is leap2-F L4's counter-orbiting halves, fed by one synchro.

```
 line k ═╦═ bellows A(θk) [plate A ▼▼▼] ⇄ [plate B ▼▼▼] bellows B(θk+180°) ═╦═ line k   (k = 1..3)
```

**(c) Variables moved.**
- **Forehead jiggle:** ±0.3 mm becomes ±0.08 mm, and the couple sits about yaw, the strongest-held axis.
- **Shaking force:** leap2-B's 0.08 N cancels as well.
- **Hold:** single-pad demand falls from 0.34 to 0.26 N·m.

**(d) Plausibility.** +5 g per pad. Six bellows on three lines halve the stiffness per plate to ~1.2 N/mm, which costs ~0.4 mm of path under 0.5 N.

**(e) Cheapest experiment ($10).** Tape a phone (accelerometer app) to the forehead pad of the hard hat. A partner scrubs the crown at 1.5 Hz under ~1 N, first with one hand, then with two hands moving in opposite directions. **Pass:** the 1.5 Hz peak drops ≥ 10 dB, and the wearer says "no" to "does the hat move?"

**(f)** Works with L1 and L2.

**(g) Why it might fail.**
- Rows come in pairs, one 3-nail row per half.
- If the gap between the halves ever drops below 3 mm they scissor hair (H-6.1), so the minimum spacing must be ≥ 15 mm (leap2-A L4's rule).

---

## LEAP 4 — NECK-YOKE MOTOR POD: the Bowdens carry displacement, the head carries nothing

**(a) Assumption broken.** That a helmet carries its own travel motors. A Bowden cable transmits displacement regardless of the path its housing takes (to first order).

**(b) Principle.** Move the three motors and their board (88 g) to a soft yoke on the shoulders, at the umbilical's collar clip. Three 5 mm Bowdens in 250 mm slack loops run to the hub capstans. Each ends in a magnetic dog clutch that parts at 15 N.

**(c) Variables moved.**
- **Head mass:** twin 475 → **≈ 390 g**.
- **Motor noise:** −10 dB, since the motors are ≥ 200 mm from the ear.
- **CoM wander:** unchanged, because the motors were already at C.

**(d) Plausibility [EST].** Three housings (EI ≈ 2 × 10⁴ N·mm² each) bent 85 mm by ±60° of yaw push back ≈ 1 N at 90 mm: **0.09 N·m resisting every head turn**. Backlash is 1–2° (3–6 mm at the scalp), at 70–80 % efficiency.

**(e) Cheapest experiment ($20).** Run two bike brake cables from a neck pillow to a hub on the hard hat. Measure yaw resistance at ±60° with a luggage scale, and backlash at a 165 mm arm. **Pass:** ≤ 0.05 N·m and ≤ 2 mm.

**(f)** This is the **reserve** if the scale puts the twin over 480 g.

**(g) Why it might fail.** A head-to-shoulder tether is the CPAP pattern leap2-E warned about. The clutches add 45 N to the lift, which threatens the ≤ 3 s doff.

---

## 2. The helmet around the leaps

**Suspension: four pads with a ratchet, moved off the scratch map.** Concept-A's rear pad sat on the upper occiput, which is the sweet spot.
- **F:** forehead, on skin below the hairline.
- **L and R:** the parietal faces of the hub pods, ≥ 60 mm above the canals. Together with F they carry the weight on the parietal slope.
- **Rear:** a **nuchal cradle** below the bun at the occipital ridge, the bike-helmet retention position.
- **Ratchet:** a rear dial set to 4 N per pad.

**Chin strap.** Anchored at the hubs, so its line passes within a few mm of C and adds no pitch bias (concept-A §3.3). Elastic, 1.5 N per side, with a **12 ± 3 N magnetic fuse**.

**Hold budget at µ 0.3 [EST].** Capacity is 0.59 N·m in pitch and roll and ≈ 0.56 N·m in yaw.

| Configuration | Mass (g) | Gravity, incl. 20° tilt | Drag | Hop | Umbilical | Demand | Margin |
|---|---|---|---|---|---|---|---|
| leap2-E helmet | 455 | 0.15–0.18 | 0.11 | 0.035 | 0.015 | 0.31–0.34 | 1.7–1.9 |
| L1 single | 389 | 0.18 | 0.11 | 0.035 | 0.015 | 0.34 | 1.7 |
| L1 + L3 single | 394 | 0.18 | 0.03 | 0.035 | 0.015 | 0.26 | 2.3 |
| **L2 + L3 twin, B scratching** | **475** | 0.105 | 0 (yaw 0.06) | 0 | 0.015 | **0.12** | **4.9** |
| L2 + L3 twin, B parked | 475 | 0.105 | 0.03 | 0.035 | 0.015 | 0.19 | 3.1 |
| Twin, both hands on the occiput | 475 | 0.25 | 0 | 0 | 0.015 | 0.27 | 2.2 |

**Coverage (footprint ±22°) [EST].**

| Region | Coverage | Limit |
|---|---|---|
| Crown, top | **100 %** | top is fenced at the frontal hairline |
| Occiput / bun | **100 %** to α ≈ 120° | — |
| Sides | **≈ 90 %** | the hub pads cover ~16 cm² each above the ears |
| Nape | **upper ½–¾** | the cradle blocks the lower midline; scratch-model defers the nape anyway |
| **All hair-bearing scalp** | **≈ 90 %** | each twin pad covers its own hemisphere and reaches the midline from β ≈ ±5–15° |

**Noise at the ear [EST].** Hub motors through the capstans give **34–44 dBA** (bone path [UNKNOWN]; TPU hub pads give −20 dB above 36 Hz, concept-A §7). The synchro pad adds room level plus nail hiss, and the desk box 35–40 dBA at 1.5 m. That meets the ≤ 60 dBA target and the 70 dBA red line.

**Doffing (≤ 3 s, one hand, eyes closed).**
1. Let go of the hold-to-run switch. Pins vent in 50–90 ms, and both pads spring out 40 mm in ≈ 150 ms.
2. Grab the **visor guard**, the one fixed handle (0.5–0.8 s).
3. Lift up and back. The chin fuse pops at 12 N and the cradle slides off the ridge with the ratchet still set (≈ 0.4 s).

That is **≈ 1.2–1.8 s**. The umbilical stays plugged into the helmet, and its collar clip parts at 15 N only if he stands up still wearing it. **Test:** 10 timed trials on phone video, plus a luggage-scale pull at the visor (≤ 20 N with the ratchet set).

**Umbilical down the back.**
- **Contents:** 11 PU tubes at 2.5 mm OD (twin) or 16 (single), plus a 4-core power/CAN cable.
- **Size:** ≈ 12–13 mm, ~65 g/m.
- **Route:** a magnetic face-seal **nape plug** at the cradle centre (leap2-E L3: 12–18 N pull-off; unplugged means all pins vented), then a **300 mm service loop**, then a breakaway collar clip at T1, then down the chair back to the desk.
- **Load on the head.** ≈ 0.02 N of bending push-back at ±70° of yaw, and ≈ 0.15 N of hanging weight at 90 mm (0.015 N·m).

---

## 3. Ranking

| Leap | Balance | Sensation | Mass / safety | Build / cost | Risk | /25 |
|---|---|---|---|---|---|---|
| L3 self-cancelling scrub (add-on) | 3 | 4 | 5 | 5 | 4 | 21 |
| L1 capstan hubs + synchro pad (base) | 3 | 4 | 5 | 4 | 4 | 20 |
| **L2 twin point mirror** | **5** | **5** | 3 | 3 | 3 | **19**, the only one that removes the lean |
| L4 neck-yoke Bowdens (reserve) | 2 | 3 | 4 | 3 | 2 | 14 |

---

## 4. Best bet: L1 + L3 as a ~394 g single-hand helmet, then L2's mirror twin at ~475 g

**The case.** On a helmet the travel drive hardly pushes: drift, sweeps and hops react with only 0.002–0.035 N·m. What tips the hat is where the pad's 105–150 g sits: 0.17–0.23 N·m and 80–95 mm of CoM wander between the hairline and the occiput. Coverage is nearly symmetric front to back, so a static trim does nothing; the model shows it making things worse. Every dead counter-mass costs 150–400 g, because the only places on a head that can carry one are short levers (hubs, band) or the face. **The one object that can sit opposite the pad, at the pad's radius, is another pad.**

**Stage 1 (≈ 394 g):** L1 + L3. The drive sits on the ear axis in capstan hubs that double as the parietal pads; the path synthesiser moves to the desk as a synchro master; the split plates stop the forehead ticking. Hold margin 2.3, ≈ 90 % coverage, 1.2–1.8 s doffing, 34–44 dBA at the ear. It already beats round 2's 455 g helmet.

**Stage 2 (≈ 475 g):** L2. Split the bail into point-mirror half-bails and tee a second 75 g pad onto the same 6 valves and 3 synchro lines. The CoM stays within **7 mm** of the vertical through C, the worst upright moment falls to **0.027 N·m**, drag cancels in pitch and roll, and the hold margin is ~5. Michael gets **two hands** mirror-stroking both sides of his head. L4's yoke is the reserve if the scale disagrees.

**The deciding tests cost $20 and an evening:** coins on a hard hat (does the twin pose stop the lean and the slip?) and a partner's two hands in lockstep (do they read as a person?). If lockstep reads as a machine, stage 1 stands on its own, and the twin waits for per-pad valves.
