# LEAP B — ACTUATION: make independence cost a valve, not a motor

**Project SCRATCH · 11-leaps · Leap Agent B · 2026-10-01**
Provocation: "What if each contact could be its own ~1 g actuator, so independence, timing jitter and per-finger force become free?"
Inputs: LEAP-BRIEF; scratch-model §1–4, §6–9; prior-art §3–4; hair-interaction rules (via pin-unit §1); safety red lines §7; DECISION; redteam-1 §1–2; PORCUPINE-BRIEF; pin-unit §0–3; 02-mechanisms summaries. Firewall kept (no other 11-leaps files read).
Tags: **[KNOWN]** sourced (link) · **[EST]** computed here (arithmetic shown or scriptable) · **[UNKNOWN]** only a bench answers it.

---

## 0. The shared assumption, and what the physics actually asks of a contact

Every architecture so far (Float-Arm, crown hand, porcupine) shares one assumption: **a few rotary motors near the contacts generate the motion and distribute it mechanically, so contacts that share a motor share its motion.** The porcupine's 3–5 active pins still ride one inner shell: same stroke, instant, speed and direction. Red Team 1 showed why that matters: a fixed stagger "is learned in three to five strokes"; the hand percept lives in per-finger timing and force *re-drawn every stroke* (scratch-model §4.2: 20–80 ms landing spread, ±30–50 % force, ±15–30° direction).

Split what a contact needs by axis and bandwidth (scratch-model §3–4):

| Axis | Stroke | Speed / bandwidth | Force | Power per contact |
|---|---|---|---|---|
| **Tangential** (the scratch) | 15–40 mm (rake), 60–140 mm (sweep) | 50–150 mm/s, 1–4 Hz | 0.05–0.1 N steady, 0.3 N spikes (§3.5) | 0.1 N × 0.1 m/s ≈ **10 mW** mechanical [EST] |
| **Normal** (landing, force, lift-off at reversal) | 5–15 mm lift, plus ±5–10 mm of seating error to absorb | transitions in **30–80 ms** (reversal 50–120 ms, §3.10), 2–8 events/s | 0.1–0.6 N, capped ≤ 2.5 N | ≈ 1–3 mW [EST] |
| **Slow** (which pins are active, region, dwell) | park/release | 0.3–20 s (P5 pauses, P6 region change, 5–20 s dwell) | — | ≈ 0 |

Two facts fall out.

1. **Power is not the problem; stroke and heat are.** Four nails need ~40 mW of mechanical power. The hard part is 30 mm of stroke at 2 Hz from a 1 g device without a hot coil or wire 20 mm from the skin.
2. **The hand does not give each finger its own tangential drive either.** In P1 (60 % of the time) the wrist supplies one shared reciprocation. The fingers act alone on the *normal* axis (who lands first, presses harder, rides over a bundle), and move tangentially on their own only in P4 (10–20 %). The hand is **one shared tangential source plus per-finger normal modulation**.

So the answer to the provocation is in two parts. A 1 g per-contact **tangential** actuator does not exist at acceptable heat and cost (§1). A per-contact **normal-axis gate** does, and it is cheap if its power comes from a shared source.

---

## 1. Actuator survey with real numbers (the evidence for the leaps)

Requirement for a fully independent tangential contact: ≥ 20 mm stroke, ≥ 100 mm/s, ≥ 0.3 N peak, 1–4 Hz, ≤ ~5 g at the head, ≤ ~$10 per contact at qty 40, nothing > 41 °C at the skin or > 43 °C within 10 mm of it (safety §2.6), bus ≤ 24 V (red line 5).

| Actuator | Real specs | Tangential per contact? | Normal-axis gate? | Heat near skin | Noise at head | Cost @ 40 |
|---|---|---|---|---|---|---|
| **SMA wire (Flexinol)** | Strain 3–5 % (7 % reverse bias); 0.10 mm: 143 g pull, cools 1.1/0.9 s (LT/HT); 0.038 mm: 20 g, 0.24/0.20 s; forced air ×4 faster; tens of millions of cycles < 103 MPa ([Dynalloy TCF1140](https://dynalloy.com/wp-content/uploads/2025/03/TCF1140.pdf)) [KNOWN] | **No.** 30 mm at 4 % = 750 mm of wire, or a 10:1 lever cutting 143 g to 0.14 N; ≤ 0.5–1 Hz in still air | **Slowly.** 100 mm × 0.10 mm, 3:1 lever → 12 mm at ~0.45 N, ~1 s cycle: fits P5/P6 and selection | Wire 90–110 °C, 0.3–0.5 W held [EST]; efficiency 1–2 % | Silent | ~$3–6/m ([price guide](https://dynalloy.com/flexinol-actuator-wire-price-guide/)) → **≈ $1/pin** |
| **EM coils moving magnets through a shell** ("magnetic puck"; [Actuated Workbench](https://dl.acm.org/doi/10.1145/571985.572011), [coil-array haptics](https://arxiv.org/pdf/2211.14163)) | 6×3 mm N52, m ≈ 0.088 A·m²: 0.3 N needs ∇B ≈ 3.4 T/m; a 10 mm-radius coil at 500 A-turns gives that only within ~1 radius, at ≈ 5 W copper loss [EST]. Workbench pucks moved by slow 10 Hz vibration-walking [KNOWN] | **Only at 2–5 W per contact** (coil chain over 15–30 mm); 10–25 W for 5 active, 20 mm above scalp | Short stroke, 1–3 W held | **Fails** without cooling | Silent | ~$1.5/coil × 3–4 per contact |
| **Voice coil (moving coil or magnet)** | Moticont LVCM-013-013-02: 6.35 mm stroke, 0.86 N continuous, 2.7 N at 10 % duty, 13 g total, **$202** ([Moticont](https://www.moticont.com/lvcm-013-013-02.htm)); LVCM-010-013-01: 0.28 N, 12.7 mm, $200 ([pwr-con](http://pwr-con.com/lvcm-010-013-01.htm)) [KNOWN] | Too short or too weak, and $8,000 at qty 40. | Technically ideal (pure force ∝ current, silent, fast); priced out. | ~0.5–2 W held | Silent | **$8,000** |
| **Piezo bender** | Thorlabs PB4VB2S: ±135 µm, 1.4 N blocking, 150 V ([Thorlabs](https://www.thorlabs.com/piezoelectric-benders)) [KNOWN] | **No.** 30 mm needs ×200 amplification, leaving mN. | No (sub-mm). Useful only as a 100–300 Hz "fizz" overlay, which scratch-model §2.1 warns against. | Cool | Audible at kHz drive | $40–100 each, plus 150 V (red line 5) |
| **Ultrasonic piezo motor (Squiggle)** | SQL-RV-1.8: 0.3 N, >10 mm/s, 2.8×2.8×6 mm; SQL-RV-3.4: 3 N, >7 mm/s; self-locking ([New Scale](https://newscaletech.com/resources/technology/squiggle-rv-reduced-voltage-linear-micro-motor-piezo-motor/)) [KNOWN] | **No.** 10× too slow (10 mm/s against 100 mm/s), and self-locking in the force path (red line 7). | Too slow. | Cool | Ultrasonic, inaudible | ~$100+ each with driver |
| **DEA / HASEL electrohydraulic** | 2–10 kV typical, 6–16 kV fields; strains 40–79 %; blocking 18–45 N ([HASEL review, MDPI 2025](https://www.mdpi.com/2313-7673/10/3/152)) [KNOWN] | Performance would do it. | Yes. | Cool | Silent | **Fails red line 5** (kV on a head). Rejected outright. |
| **Electroadhesive clutch** (gate on a moving band) | 22 N/cm² at 100 V; < 1 g; ms engage/release; < 1–3 mW ([Sci. Adv. 2024](https://www.science.org/doi/10.1126/sciadv.ads0766); [Diller et al.](https://journals.sagepub.com/doi/full/10.1177/1045389X18799474)) [KNOWN] | As a **gate** on a shared moving band, yes: a 1 cm² clutch holds 20× the 0.3 N needed. | — | Cool | Silent | Cheap film, but **100–300 V** breaks red line 5 as written (µA, low energy; would need a safety waiver) |
| **Electropermanent magnet latch** | Flux switched by a µs–ms pulse, zero holding power; force ∝ area, switching energy ∝ volume, so favourable at small scale ([Knaian MIT thesis](https://cba.mit.edu/docs/theses/10.06.knaian.pdf); [EPM valves for soft robots](https://www.nature.com/articles/s44172-024-00251-y)) [KNOWN] | No | As a per-pin **latch** (replaces the selector): yes. As a stroke-rate gate: unproven DIY. | Cool (pulse only) | Click | DIY; not off-the-shelf |
| **Pneumatic bladder/piston + valve at the desk** | Blood-pressure (BP) monitor pump 1.8 L/min, > 53 kPa ([KPM27C](https://www.amazon.com/KPM27C-6B1-Pressure-Monitor-Inflator-Aquarium/dp/B0DYXTW732)), KPM08C $3.28 ([listing](https://www.amazon.com/Diaphragm-Sphygmomanometer-Pressure-Monitor-Aquarium/dp/B0DCRHD52B)); KOGE KSV05A valve 3 V, < 130 mA, 40 kPa ([datasheet](https://koge-europe.com/wp-content/uploads/datasheet-KSV05A.pdf)); 3 V NC micro valve 10 g, ~$2.75 ([eBay](https://www.ebay.com/itm/262893410793)); XGZP6847A sensor $4–8 ([eBay](https://www.ebay.com/itm/225673132043)); pneumatic haptics: 7–34 Hz bandwidth, 10–165 ms latency by hose and valve ([1](https://arxiv.org/html/2604.01390), [2](https://arxiv.org/html/2609.00612)) [KNOWN] | Only as a slow bending finger (Team C's C4) | **Yes:** 7 mm bore = 0.385 N at 10 kPa, 1.54 N at 40 kPa; **30–60 ms** transitions [EST] | **None at the head** | **Silent at the head** (box on the desk) | **$4–8 per pin** |
| **Hydraulic tendon** (servo + syringe at desk, water tube, bellows at head) | SG90-class servos ~$2 at qty; water in 2 mm ID × 1.2 m: 13 kPa viscous drop at 150 mm/s through a 6 mm slave, so 0.37 N drag [EST, Poiseuille]; incompressible, so position-stiff | **Yes**, with all motors off the head; 1 tube per axis. | Yes. | None | Silent at the head | ~$4–6 per axis |

**Survey verdict.** No 1 g device at the contact delivers the tangential stroke at acceptable heat (SMA, EM, VCA), voltage (DEA, HASEL, electroadhesion) or speed (Squiggle). The two classes that keep **the head cool, silent and light with per-contact control** both put power on the desk and send fluid down a tube: pneumatic for the normal axis (constant force) and hydraulic for the tangential axis (position). SMA wins on cost per pin, but only on the slow axis.

---

## LEAP 1 — PRESSURE-BUS PINS: each contact is a constant-force air piston, and its valve lives on the desk

**(a) Assumption broken.** "Contact force is set by a spring: stiffness × displacement, fixed at build time." Also: "selection is a mechanical latch and cam."

**(b) Principle.** Replace each porcupine pin's 40 mm soft spring, latch and selector with a 7 mm bore holding a thin latex/silicone bladder that pushes a free-sliding PTFE pin. A 1.5 mm ID tube runs to a manifold in a desk box. Each pin has one 3-way valve that connects it to either the **force rail** or the **lift rail**. The force rail is regulated at 5–15 kPa (0.2–0.6 N). The lift rail is vacuum from the same pump's inlet, or plain vent plus a 0.05 N return spring. With several force rails (for example 6/10/14 kPa) and two valves per pin, each pin can take a different force on every stroke. A mechanical relief valve on the supply (40 kPa) is the force cap: 40 kPa × 38.5 mm² = 1.54 N, a physical constant below the 2.5 N red line, independent of firmware. The diaphragm pump's own stall pressure (~53 kPa → 2.0 N) is a second constant.

```
   DESK BOX (noise lives here)                      HEAD (silent, cool)
 ┌──────────────────────────────────┐   12–40 tubes    inner shell
 │ BP pump ─► reservoir ─► relief 40 kPa│  1.5 ID bundle  ═══╤═══════╤═══
 │   │            │                  │   ~15–20 mm Ø      │bore 7  │
 │   │      regulators R1 R2 R3      │ ─────────────────► │bladder │  ← pressure = force
 │   │      (6/10/14 kPa rails)      │                    │  ▼     │
 │ inlet = vacuum rail (lift)        │                    │PTFE pin│  ← free slide, no seal
 │ per pin: 3-way valve + P-sensor   │                    ╧══╤═════╧══ smooth drafted nose
 │ MCU: valve timing per pin/stroke  │                       │ neck + nail (TM1 / pin-unit tip)
 └──────────────────────────────────┘                    ~~~~▼~~~~ hair / scalp
   force(t) per pin = P_rail(t) × A        lift = vacuum or vent + 0.05 N return spring
```

**(c) Why it could step-change the sensation.**
- **Force reference solved for any seating error.** A pin open to a large regulated rail pushes P·A whatever its position. The only error is flow drop: ~280 Pa ≈ 0.01 N at 50 mm/s through 1 m of tube [EST]. Pin-unit §0's spring swung ±0.10 N over ±5 mm and needed a 40 mm housing; here ±15 mm of slop gives the same force. Judge-2 F1 is dissolved, not mitigated. (A pin behind a *closed* valve becomes a 0.056 N/mm gas spring [EST: k = P_abs·A²/V, V = 3 ml], so active pins must stay open to a rail, never "fill and hold".)
- **Per-contact force re-drawn every stroke** (§7 rank 3; §4.4 "per-finger force scale U(0.7, 1.3)"). Rail choice per stroke gives the human ±30–50 %, which Red Team 1 showed a passive leaf cannot.
- **Per-contact landing and lift at reversal** (§7 ranks 1, 6; DR4). A 20–80 ms landing spread re-drawn every stroke; 30–60 ms transitions fit the 50–120 ms reversal window.
- **Soft landings, no tap** (Red Team 1). Landing speed is the fill rate, so a needle valve on the rail gives the 0.2–0.5 s P6 ramp.
- **Penetration** (§7 rank 2). Constant force over 30 mm of travel, where a spring would be weakest exactly in thick hair.
- **Sound** (§1 D). Nothing at the head makes noise; the nail-on-hair hiss is the only sound.

**(d) Plausibility (numbers).** Bore 7 mm: 0.19 / 0.39 / 0.58 N at 5 / 10 / 15 kPa [EST]. Air use ≈ 1 ml free air per landing × 5 pins × 2–4/s ≈ 0.6–1.2 L/min, inside one 1.8 L/min BP pump with a 0.5–1 L bottle as reservoir [EST]. Response: tube RC ≈ 4 ms (1 m × 1.5 mm ID); a 0.8 mm orifice passes ~55 ml/s at 20 kPa, so ~20 ms to fill; solenoid 5–15 ms; **30–60 ms** total [EST]. The literature spans 10–165 ms [KNOWN], so latency is the first thing to measure. Friction: a free PTFE pin in a 0.2 mm-clearance bore at µ ≈ 0.1 under 0.1–0.3 N side load gives 0.01–0.03 N [EST]; bladder hysteresis [UNKNOWN]. The premium piston is an Airpel graphite-in-glass unit (9.3 mm bore, friction 1–2 % of load) ([Airpot](https://www.airoil.com/uploads/assets/downloads/AirpelCat10-06.pdf)). Umbilical: 40 × 2.5 mm OD tubes pack to ~17 mm diameter, 12 tubes to ~10 mm [EST]. Head mass ≈ 2–3 g per pin [EST]. Cost at qty 40 **≈ $250–400** [EST]. Fail-safe (red line 8): de-energised valves sit on the vent/vacuum port, so every pin lifts; e-stop also opens a normally-open dump valve on the reservoir.

**(e) Cheapest experiment (< $40, one weekend).** Build three pins. Each is a 7 mm printed bore, a finger-cot or balloon bladder and a 3 mm PTFE rod with a pin-unit nail. Add one KPM08C pump ($3), three 3 V micro valves ($9), one XGZP6847A ($4), a 1 m PU tube each, an aquarium needle valve as regulator, and the existing ESP32.
- Bench 1: kitchen scale under the nail; record force at extensions 10/20/30 mm at 10 kPa. Pass if the variation is < ±0.05 N.
- Bench 2: phone at 240 fps; time from command to the scale reading at landing and at lift. Pass if < 60 ms.
- Bench 3: hold the three-pin block in your hand and do the scratching motion yourself on your own head. Compare "all pins always down" with "firmware randomly gates landing (0–80 ms) and force rail per stroke". You supply the shared motion, the firmware supplies the per-finger normal modulation. That is the hand architecture, and the A/B isolates exactly what this leap adds.

**(f) What it replaces or combines with.** It replaces the pin spring, latch, selector motor and cam, and lift-by-path. It keeps the porcupine's outer and inner shells, pin field and nail tips. The **selector becomes firmware**: any subset, any shape, any walk pattern, including non-adjacent pins. It combines naturally with Leap 2.

**(g) Honest reasons it might fail.** (1) Latency over 80 ms with cheap valves and long tubes would put the lift after the reversal. Fixes: a manifold on the neck or shoulder, larger orifices. (2) Bladder hysteresis and bore friction could eat 0.05–0.1 N of a 0.2 N target. (3) A 17 mm hose umbilical: fine at a desk, not portable. (4) Never PWM a valve for force: 50–100 Hz ripple is Pacinian-band vibration (scratch-model §2.1). Force must come from discrete rails. (5) Many fittings mean many leaks; the per-pin sensor flags them.

---

## LEAP 2 — PHASE-GATED ORBIT: one continuous motion, and each pin chooses which piece of it to scratch with

**(a) Assumption broken.** "A contact's stroke is the carrier's stroke, so per-contact direction, length and timing need per-contact tangential actuators (or a yaw servo)."

**(b) Principle.** Drive the inner shell (or any carrier) in **continuous circular translation**: an orbit of radius r_o with no rotation and no reversals, at a slowly wandering speed. Each pin is down only during a phase window [φ₁, φ₂] that it chooses on every revolution. The orbit is shared; the stroke is private. A pin down over Δφ scratches an arc of length r_o·Δφ, with chord 2·r_o·sin(Δφ/2) and mean direction set by (φ₁+φ₂)/2. A bidirectional rake (P1) is one window at φ ≈ 0 and another at φ ≈ 180°, which gives two strokes per revolution. Rotating both windows rotates the rake axis, so direction wander comes free with no yaw servo. Shrinking the windows shortens the stroke. Shifting one pin's window by 20–80 ms gives the per-finger landing spread. Short random windows on each pin give a spider-like P4 (shared speed, independent timing and direction).

```
  top view of one orbit (r_o = 20 mm), shell translates around the circle, never reverses
                 φ=90°
             .-""""""-.          pin A down  φ ∈ [-45°, 45°]  → stroke ≈ 28 mm, heading ↑
           .'   ↖  ↑   '.       pin A down  φ ∈ [135°, 225°] → stroke ≈ 28 mm, heading ↓   (= P1 rake)
   φ=180° |  B ◄──  ──► A |φ=0   pin B same windows shifted +30 ms → asynchrony re-drawn each rev
           '.   ↙  ↓   .'       pin C window [60°, 100°]     → 14 mm diagonal flick         (= P4 element)
             '-.____.-'          all pins lifted outside their windows → no pin ever reverses under load
                 φ=270°
  Orbit radius 20 mm at 1 Hz: 126 mm/s; Δφ = 90° → 31 mm arc / 28 mm chord / 250 ms dwell   [EST]
  Orbit radius 20 mm at 0.5 Hz: 63 mm/s (slow CT mode); radius 15 mm at 1.5 Hz: 141 mm/s
```

P2 sweeps (60–140 mm) cannot come from a 20 mm orbit. They come from **spatial sequencing**: neighbouring pins along a line land one after another, each scratching its own short arc, which gives tactile apparent motion along the line. That is the sequential lateral-slip illusion already in prior-art §3.4 ([SHIFTS](https://arxiv.org/pdf/2003.00954)). At scalp two-point acuity of 15–40 mm (prior-art §3.3), pins at ~20 mm pitch firing at 100–150 ms intervals should fuse into one long sweep [UNKNOWN; testable].

**(c) Why it could step-change the sensation.** It copies the hand's control architecture (one smooth proximal motion, per-finger normal modulation) and makes §7 ranks 1, 6, 8 and 9 (irregularity, asynchrony, direction, stroke length) **per contact and per stroke** using only normal-axis gates. It also removes two machine signatures Red Team 1 attacked. The motor **never reverses**: no backlash knock, no "metronome", and constant speed is any gearbox's quietest regime. And **no pin reverses under load** (DR4, H-5.2 by construction), because the orbit has no reversal. Fixed windows on a fixed orbit remain available as the PERIODIC control.

**(d) Plausibility.** The orbit is the porcupine's two-servo shell drive, or one motor with Team A's twin "locomotive" eccentrics enclosed above the shell (red line 1). Speed 63–141 mm/s for r_o = 15–20 mm at 0.5–1.5 Hz [EST]. A 90° window at 1 Hz lasts 250 ms, so a 30–60 ms gate lands and lifts while moving, which is Red Team 1's anti-tap fix. At 1.5 Hz a 60° window (111 ms) is at the gate's limit. A 90° window bends direction ±45° along the stroke, more than human wander (±15–30°), so 60° windows are the default [EST].

**(e) Cheapest experiment (< $20, an afternoon, on top of Leap 1's bench).** Mount the three-pin block on a printed plate driven in circular translation by one N20 gearmotor and two eccentric pins (Team A geometry), and hang it over a wig head on paper with ink-dipped tips. Run the gating firmware and photograph the traces: rakes in chosen directions, lengths varying, pins out of step. Then put it on your own head and compare a fixed window set (PERIODIC) with re-drawn windows. If the Leap 1 bench isn't built yet, the gate can be a hobby servo lifting each pin; it is too slow for the fine timing but enough to see the strokes.

**(f) Replaces or combines.** It replaces the porcupine's reciprocating shell program, its "lift-off by path" and the stroke-direction/yaw question. It needs a fast per-pin normal gate. Leap 1 is the best gate; a stroke-rate SMA gate with forced-air cooling (Leap 4 variant) is the fallback.

**(g) Why it might not work.** (1) **Hair stirring.** A lifted pin left in the canopy while the shell orbits stirs hair in loops, and stirring tangles. Pins must retract out of the canopy (≥ 15–25 mm, cheap with pneumatics), and the shell underside still sweeps a 40 mm circle over long hair (a porcupine risk too). The wig-head test comes first. (2) If arcs read as "circling", windows ≤ 60° cap strokes at ~20 mm unless the orbit grows. (3) All active pins share one instantaneous speed; the wrist imposes the same on human fingers [UNKNOWN].

---

## LEAP 3 — HYDRAULIC FINGERS: real per-contact tangential independence, with every motor on the desk

**(a) Assumption broken.** "Independent tangential motion per contact means a motor per contact on the head, which is too heavy, loud and hot."

**(b) Principle.** Each independent axis is a **closed water line**. At the desk, a cheap servo drives a 1–3 ml master syringe; the servo's friction and noise don't matter there. At the head, a frictionless slave (silicone bellows or rolling diaphragm, ~6 mm effective bore) tilts a pin about a **bonded silicone diaphragm pivot** in the shell. The hair side has no joint, no sliding seal and no gap: the diaphragm flexes. The pin keeps its own small axial spring (or a Leap 1 pneumatic bore) for force, so the stiff hydraulic position drive never sets normal force (red lines 2 and 7). With the pivot ~22 mm above the nail, a ±30° tilt gives ±12 mm of tip travel and the arc rises ~3.6 mm at its ends, giving free geometric lift (the Float-Arm principle per contact).

```
 DESK                                   HEAD
 [servo]─arm─[master syringe 1 ml]══ water, 2 mm ID nylon, 1.2 m ══[bellows]─┐ above shell
 [servo]─arm─[master syringe]════════════════════════════════════════[bellows]┤ (antagonist or spring return)
                                                                             pin
                                                 ═══════════════════════╪═══════ shell
                                                 bonded silicone diaphragm ◯  ← pivot, sealed, no gap
                                                                             ╲  ±30°
                                                                              ╲ nail: ±12 mm, arc lift 3.6 mm
```

**(c) Sensation.** The only option in the survey that gives **true P4** (§4.1: fingers "out of phase, 3–6 Hz per finger", "highest unpredictability; strong tingle driver") and simultaneous per-finger direction and speed differences, which Leap 2 only approximates. A four-finger hydraulic module could serve as the spider and "treat" (P7 hairline, nape) module.

**(d) Plausibility.** At 150 mm/s through a 6 mm slave and 2 mm × 1.2 m tube, viscous drop is 13 kPa (0.37 N), which the servo absorbs; 2.5 mm ID cuts it 2.4× [EST]. Wave delay ~3 ms in nylon [EST]. P4's 30–90 mm/s is inside an SG90's 0.1 s/60° on a 10 mm arm [EST]. Head mass ~3–4 g per axis; cost ~$4–6 per axis [EST]. The servo noise stays in the desk box.

**(e) Cheapest experiment (< $30, a weekend).** One finger, one axis. SG90 plus 1 ml syringe, 1.2 m of 2 mm nylon tube, a silicone pipette bulb as the slave, and a pin through a silicone-sheet diaphragm in a printed plate. Fill bubble-free (boiled water, tube submerged). Measure tip position against command at 1–6 Hz with phone slow-motion, and check leaks, sponginess and the diaphragm over 10⁴ tilts. Then build four fingers and run P4 against "locked together".

**(f) Replaces or combines.** A P4/P7 module beside the Leap 1/2 field. If P4 proves decisive, it can instead be a slowly relocating 4–5 finger "hand": Team B's robot hand with its motors moved off the head.

**(g) Why it might not work.** (1) A leaking fitting puts water on the head: benign but wet. (2) Bubbles make the drive spongy and drifting, so it needs a bleed procedure. (3) Tube count: 12 lines for 4 two-axis fingers, which doesn't scale to 40 contacts. (4) Diaphragm fatigue: ~5,000 cycles per session [UNKNOWN].

---

## LEAP 4 — THERMAL-MUSCLE PINS: SMA replaces the selector, so "which pins are active" becomes free and per-pin

**(a) Assumption broken.** "Choosing the active group needs a motor and a cam, so groups are adjacent, fixed-size and move on a track."

**(b) Principle.** Each pin gets 100 mm of 0.10 mm HT Flexinol, folded over a polished pulley in a PTFE sleeve inside the shell, with a 3:1 lever. The arrangement is fail-safe: a bias spring parks the pin up, and the energised wire pulls the pin's spring seat down to release it. (Energised = active; de-energised = parked, so red line 8 holds by construction.) Stroke 4 % × 100 mm × 3 = 12 mm at ~0.45 N [EST from 143 g pull]. Contraction is ~0.2–1 s depending on current; release is ~0.9 s in still air, ~0.25 s with forced air [KNOWN ×4 factor]. **That timescale matches P5 pauses (0.3–3 s) and P6 soft landings (0.2–0.5 s ramp)**, so the actuator's slowness becomes the soft landing.

```
   shell ═══════╤════════════════╤════
                │ pin housing    │  ◄─ 0.10 mm SMA, 100 mm, folded, PTFE-sleeved (90 °C inside)
          lever ╞═══╗  bias spring (parks pin UP when wire is cold)
                │   ╚═ wire pulls seat DOWN → pin released onto its force spring / bladder
                ▼ nail
```

**(c) Sensation.** It gives per-pin selection (§7 rank 6) in any pattern: 1–5 contacts, non-adjacent groups, continuous wander instead of cam steps, irregular dwell (§4.2), and natural soft landings. It does **not** give stroke-rate asynchrony (that needs Leap 1 or 2). It is the cheapest per-pin independence available, about $1 per pin.

**(d) Plausibility.** 0.3–0.5 W held per active pin, so ~2.5 W for 5 pins in a ventilated shell 20+ mm above the scalp [EST]. The wire runs at 90–110 °C inside PTFE, and the outer surface must be IR-checked ≤ 43 °C. Life is "tens of millions of cycles" at ≤ 103 MPa [KNOWN], against ~10³ selections per session. A stroke-rate variant (3 × 0.038 mm wires, 0.6 N, ~50 ms with forced air from the Leap 1 pump) could gate at 2–4 Hz, at ~60 mJ per wire per cycle (≈ 0.5 W per pin at 3 Hz) and only 4 mm of stroke per 100 mm of wire [EST]. That is marginal; pneumatics does it better.

**(e) Cheapest experiment (< $15, an evening).** 0.5 m of 0.10 mm HT Flexinol (~$4), a logic MOSFET, a printed lever and one porcupine pin. Time the cycles by phone, IR-check the sleeve after 20 min, and count cycles to any stroke loss.

**(f) Replaces or combines.** It replaces the selector motor, cams and latches with nothing else changed: the low-risk path, a "leap" only in removing the group constraint.

**(g) Why it might not work.** A hot wire in a worn shell needs a thermal audit. Cooling time drifts with ambient temperature and airflow [KNOWN, Dynalloy §4]. Amateur crimps fail. And it does nothing for rank 1 at stroke rate.

---

## 2. Ranking

Scores 1–5 (5 best). "Variables unlocked" counts scratch-model §7 ranks moved to per-contact, per-stroke control.

| Leap | Independence achieved | §7 variables unlocked | Plausibility | Hair / safety | Buildability | Total |
|---|---|---|---|---|---|---|
| **L1 Pressure-bus pins** | 4 (normal axis per pin, per stroke) | 5 (ranks 1, 2, 3, 6, 7, 15; plus force reference solved) | 4 (latency the open question) | 5 (cool, silent, relief-valve cap, vent-to-lift fail-safe) | 4 (BP-monitor parts, many tubes) | **22** |
| **L2 Phase-gated orbit** (needs a gate) | 4 (direction, length, timing per pin from one motion) | 5 (ranks 1, 6, 8, 9; no reversals) | 4 | 3 (stirring risk if lift is short) | 4 | **20** |
| **L3 Hydraulic fingers** | 5 (full tangential per finger) | 4 (P4, per-finger speed and direction) | 3 (bubbles, leaks) | 4 (water; sealed diaphragm) | 2 (bleeding, many lines) | **18** |
| **L4 SMA selector pins** | 2 (slow axis only) | 2 (ranks 6, 14; soft landing) | 4 | 3 (hot wire inside shell) | 5 | **16** |
| Magnetic puck / coil array (survey only) | 5 in principle | 5 | 1 (2–5 W per contact) | 1 (heat; puck-on-shell slide is a pinch line, red line 1) | 2 | 14 |
| VCA / piezo / Squiggle / DEA (survey only) | — | — | priced out / too short / too slow / kV | — | — | rejected |

---

## 3. Best bet: L1 + L2, the "pressure-gated orbit"

**Build the porcupine's pin field with pneumatic constant-force pins on a continuously orbiting shell, and make every pin's landing, force and lift a per-stroke valve decision on the desk.** The scratch-model's top variables (irregularity, reaching the skin, per-contact force, asynchrony, direction, stroke length) are per-finger *normal-axis* decisions layered on a shared motion; that is how a real hand makes them. A $1–3 blood-pressure valve, a 1.5 mm tube and a 7 mm bore make that decision in 30–60 ms, with no heat, noise or machinery at the head. Constant pressure dissolves the force-reference problem that drove the program to 40 mm springs, and a relief valve makes the 2.5 N cap a physical constant. The orbit turns one smooth, never-reversing motor into per-pin rakes of chosen direction and length, with no pin reversing under load. The selector, latches, long springs, lift-by-path and yaw servo all disappear into firmware. Run the weekend test first: three bladder pins, a $3 pump and three $3 valves, held in your hand on your own head, randomised gating against locked pins. It answers the deciding question (does per-finger normal modulation alone make it feel like a hand?) before anything is built on a shell. Hydraulic fingers (L3) follow if P4 proves decisive. SMA selection (L4) is the fallback if the tube bundle is unwelcome.
