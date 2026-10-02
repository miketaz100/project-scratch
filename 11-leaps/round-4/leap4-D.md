# LEAP 4-D: Is the puppet drive worth it?

**Project SCRATCH · 11-leaps/round-4 · Agent D · 2026-10-02**
**Provocation:** the air synchro is a large share of the baseline's hours, leak-hunting and risk. It has a master in the box, 3 sealed lines, finger-cot sleeves, bell cranks, and charge, relief and vacuum breakers. Re-open the drive using the newest cheap parts and say what wins.
**Read:** LEAP4-BRIEF; 12-sp1v2 DECISION-2 (including the north-star amendment), decision-analysis, SYSTEM-SPEC §0–2 and §4, redteam-1/2/3 (the synchro and hours sections); leap3-B and leap3-D in full; leap3-A L1/L4; servo-alternatives; scratch-model §1–3, §7–8; hair-interaction §4–6; tip-interface §5.4; safety §7. Firewall kept: I read no other round-4 file.
**Tags:** [KNOWN] = a project file or a cited vendor page. [EST] = my arithmetic (script `l4d.py` in the session scratchpad). [JUDG] = judgement. [UNKNOWN] = only a bench test can answer it.

---

## 0. What the synchro actually costs, and what it quietly does

**Its share of the baseline** [JUDG, with RT3's 1.5× first-timer factor]:

| Synchro-specific work | Hours |
|---|---|
| 6 cylinders (printed bore, POM piston, finger-cot sleeve); 6 bell cranks (3 on the head, 3 replica in the box) | 12–18 |
| Charge valve, 3 duckbills, 3 reliefs, 3 NO dumps, 3 vacuum breakers, 3 sensors, about 12 joints | 6–10 |
| Leak hunt to ≤ 0.5 kPa/min per line | 4–12 |
| Charge, re-zero and dump firmware; drag model | 4–8 |
| Sleeve-life rig with the park cycle (V4); area-mismatch ink trace (V5) | 6–11 |
| **Total synchro** | **≈ 32–59 h** |
| XY master stage that feeds it | 8–12 h |

- **Share of 165–230 h:** about 20–25 %.
- **Parts:** ≈ $105, plus the $70 XY master.
- **Head mass:** ≈ 36 g per pad with light lines (24 g of slaves and bell cranks, 9 g of line on the helmet, 3 g of loop share) [EST].
- **Open risks it carries:** sleeve life (V4), leak budget (V5), reverse pressure on the sleeves (RT2 #9), the rupture slam and two-sided cap (RT2 #3), bell-crank yaw.

**What it does that people overlook.** These are the yardsticks every replacement has to meet:

1. **No source of sound on the head.**
2. **No wires and no heat on the pad.**
3. **Path independence.** Pressure does not care how the tube bends as the bail travels 143° and the head turns.
4. **A free drag vector** from 3 sensors.
5. **A two-sided tangential cap of 2.5 N** (with RT2's fix).
6. **Compliance of 0.9 N/mm at the plate** [EST, p₀ 8 kPa]. This is the one nobody priced. Because it is soft, it is also a **mechanical low-pass filter between the box motors and the skull** (§1.2). Every stiffer puppet loses it.

---

## 1. The noise yardstick: bone conduction, 2 kHz against 250 Hz

### 1.1 Thresholds

Leap3-D's anchor is ISO 389-3 bone-conduction force thresholds at the mastoid:
- **2.2 mN at 250 Hz**;
- 0.27 mN at 750 Hz;
- 0.13 mN at 1 kHz;
- **35 µN at 2 kHz**.

So the ear is **63× (36 dB) more sensitive in force at 2 kHz than at 250 Hz**. Below 250 Hz I extrapolate the threshold at about 10–12 dB per octave: **≈ 10 mN at 125 Hz and ≈ 30 mN at 63 Hz** [EST]. The crown and forehead are about 10 dB less sensitive than the mastoid. A pad coupled through 0.15 N skids and nails is coupled far worse than a 5.4 N audiometric vibrator.

That coupling loss is [UNKNOWN]: I guess 20–40 dB. **So I quote everything as dB above the mastoid threshold *before* coupling loss, and as dB relative to the air baseline.** Relative numbers are robust even where the absolute ones are not.

### 1.2 The finding that reframes the provocation

Any puppet transmits the box master's motion **ripple**, and the ripple force it delivers is roughly k × x_ripple, where k is the puppet's stiffness.
- A stepper under stealthChop on a 12 mm drum (or a GT2 20T pulley) at 132 mm/s steps at **≈ 700 Hz** [EST].
- A ripple of 1 % of a full step is **≈ 1.9 µm**.

Force per µm of master ripple [EST]:

| Puppet | Plate stiffness | Ripple force per µm | vs 750 Hz threshold (pre-coupling) | vs air |
|---|---|---|---|---|
| Air synchro (baseline) | 0.9 N/mm | 0.9 mN | +11 dB | 0 dB |
| Tendon with 2 N/mm series springs | 1.9 N/mm | 1.9 mN | +17 dB | **+6 dB** |
| Rigid tendon | 4.8 N/mm | 4.8 mN | +25 dB | +15 dB |
| **Water (hydraulic)** | **63 N/mm** | **63 mN** | **+48 dB** | **+37 dB** |

**The air's softness is a feature.** A stiffer puppet is a better megaphone for the box. Hydraulics would carry the stepper tune straight into the skull. Any stiff puppet must either add a series spring or use a smoother master.

### 1.3 On-head motor sources

- **Direct-drive gimbal BLDC.** At scrub speeds the electrical frequency is 7–20 Hz and the cogging fundamental (84 per revolution for 12N14P) is **40–120 Hz**. Gearless puts the *tones* in the deaf band, but **not automatically below threshold**. Cogging of 0.5–2 mN·m [UNKNOWN for these motors] on a 7.5 mm crank is 67–267 mN at the block: **+16 to +29 dB over the extrapolated 125 Hz threshold**. On an 18 mm five-bar arm it is +8 to +20 dB. A feed-forward anti-cogging table (−15 dB) brings it to about −7…+14 dB.
- **FOC control noise** lands in the sensitive band. A 12-bit encoder with a position stiffness of 0.67 N·m/rad dithers about 15 mN rms at the block. In the 2 kHz third-octave, after a second-order low-pass on the torque command at 200 Hz, that is 45 µN (**+2 dB**). A **14-bit encoder gives 11 µN (−10 dB)**. Naive SimpleFOC angle loops that "sing" are a real failure mode; a filtered, feed-forward-dominated loop is not.
- **N20 gearmotor reference** (leap3-D): +30 dB at 1–3 kHz.

---

## 2. The candidates on one sheet

Common conditions: the 30 mm line, PLINE at ε 0.025, circle R 0–15 mm; 0.5 N typical drag with 1 N spikes; a 40 g block; twin limit 500 g.

| Drive | Path error, line / PLINE | Path error, circle | Max scrub rate | Head-side sound source (bone) | Δ head mass per pad vs air | Synchro + master hours | Δ cost (both pads) | Dominant failure | One-person build |
|---|---|---|---|---|---|---|---|---|---|
| **Air synchro (baseline)** | 0.5 mm shrink at 0.5 N; bow ≤ 0.4 | same; 25 Hz ring at landings | 2.0 Hz line (H-5.4); R 10 at 3 Hz | none; box ripple 0 dB ref | 0 (≈ 36 g) | 40–71 | 0 | sleeve life, leaks, reverse pressure | hard (leak hunting) |
| **T: three-drum tendon puppet** (L1) | ≤ 0.3 mm; dead band crossed only at ends, where pins are lifted | 0.4–1.0 mm flats raw, ≤ 0.3 after compensation | same, no 25 Hz ring | none on head; box ripple +6 dB; creak [UNKNOWN] | **−8** (≈ 28 g) | **22–36** | **−$70 to −100** | dead band varies with pose; cable fray | moderate |
| **G: gimbal FOC on the pad** (L2) | ≤ 0.1 mm, software path | ≤ 0.1 mm | 2.0 Hz line; 4 Hz small circles | cogging 60–120 Hz −7…+14 dB; 2 kHz −10 dB at 14-bit | **+26 to +31** (62–67 g) | 26–46 (deletes the XY master too) | ≈ +$0–60 | **twin over 500 g**; heat (five-bar); control noise | moderate (FOC tuning) |
| **H: water puppet, syringes** (L3) | ≤ 0.05 mm | ≤ 0.05 mm | 2 Hz (inertance fine) | box ripple **+37 dB** | **+10** (water) | 35–55 | ≈ −$10 | wet leak; thermal over-constraint; seal wear | moderate, messy |
| **P: two push-pull Bowdens + PP flexure XY** (L4) | 1–2.4 mm backlash at every reversal; 1.9 mm cosine cross-talk (needs warp) | kinks at axis reversals | 2 Hz | box ripple +15 dB; backlash clacks | +5 to +15 (solid inner) | 25–40 | ≈ −$60 | backlash, stiff inner resists travel | moderate |
| Voice-coil or linear-motor XY | excellent | excellent | 10 Hz | ≈ silent | **+150 to +210** (leap3-B: ≈ 250 g) | — | +$150 | mass | reject |

---

## LEAP 1 — THE THREE-DRUM TENDON PUPPET: the same puppet, made of string instead of air

**(a) Assumption broken.** "A puppet copies the master through a fluid, so it must be sealed, charged, relieved and re-zeroed." A **cable-driven parallel mechanism** also copies position through any path, as long as its housing is stiff in compression and the tensions stay positive.
- Three tension-only cables at 120° fix x and y.
- Their common mode is position-free, exactly as the air's p₀ is.
- Nothing has to be sealed, charged, leak-hunted, or protected from reverse pressure.

**(b) Principle and dimensioned sketch.**

*Box.* There is no XY stage. Three NEMA 17 pancake steppers on the existing TMC2209s each carry a **Ø 12 mm printed drum**.
- 30 mm of stroke is 0.8 turn; 1/16 microstep gives 12 µm resolution.
- Firmware computes the slave's exact cable lengths (inverse kinematics), so the replica geometry, bell cranks and the cosine errors of RT2 #3 all disappear.
- **Pad B:** each drum is double-grooved. Pad B's cables sit at 60°, 180° and 300°, its point mirror. Each of its cables then sees exactly the same length change as pad A's cable on the same drum, so the twin needs **no extra motors**, only cables (the analogue of C25's 6-cylinder master).
- **Housing stops at the box:** each sits on a stiff printed flexure (≈ 20 N/mm) with a $2 Hall sensor. That gives per-cable tension to about 0.1–0.2 N, which is the drag vector and the snag signal, at parity with the air sensors.
- **Common-mode tensioner:** all three stops share one floating plate with a 6 N spring. It absorbs equal length changes (bail travel, temperature, head turns) without moving the slave, because Σeᵢ = 0.

*Lines.*
- 0.45 mm nylon-coated 7×7 stainless (0.36 mm metal), inside a **close-wound stainless coil housing about 1.2 × 0.6 mm**.
- 1.6 m long, with ≈ 7.2 g/m together.
- Housing bending stiffness ≈ 30 N·mm², softer than the 4 × 2.5 PU tube (320 N·mm²), so it does not fight the hub servos or head turns.
- Box end: a three-ferrule hook block that releases when the box latch opens.

*Pad (replaces the 3 slaves and bell cranks).*
- Three housing stops with barrel adjusters on the deck rim at R 45 mm.
- Each cable passes a **2 N/mm series spring** (the deliberate low-pass of §1.2) and anchors on a **tendon plate** above the pin block.
- The tendon plate grips the block through a **magnetic shear coupling set at 2.0 N**. The block rides caged on its three balls and is held square by the PP parallelogram (unchanged).
- If the coupling parts, the box sees the tension pattern change, vents the pins, and re-homes the plate to recouple.

```
 BOX                                     HELMET harness (with pin tubes)         PAD (plan)
 stepper A ─ drum Ø12 ═╗ (2 grooves: A + B) ════════ coil housing 1.2/0.6 ══════▶ stop ─ spring 2 N/mm ─╮
 stepper B ─ drum Ø12 ═╬═════════════════════════════════════════════════════▶ stop ─ spring ──── tendon plate
 stepper C ─ drum Ø12 ═╝                                                         stop ─ spring ─╯   ⇣ magnetic shear 2.0 N
 housing stops on Hall flexures (drag vector) + common-mode spring plate          pin block (caged, PP-square)
 path(t) = IK in firmware → three cable lengths; backlash comp per cable
```

**(c) What it moves** [EST].

*Head mass.* ≈ 28 g per pad against ≈ 36 g (−8 g):
- tendon plate and magnets 7 g;
- stops 3 g;
- springs 1.5 g;
- housings on the helmet 14 g;
- loop share 2 g.

Single: 386 → **≈ 378 g**. Twin: 480 → **≈ 464 g**, so the twin margin goes from 20 g to 36 g.

*Hours.* The synchro plus XY master took 40–71 h; this takes **22–36 h**:

| Task | Hours |
|---|---|
| Terminating 6 cables (3 now, 3 later) | 3–5 |
| Drums, tensioner and Hall stops | 5–8 |
| Pad stops, tendon plate and coupling | 4–6 |
| IK and backlash firmware | 3–6 |
| Ink trace and pose sweep | 4–7 |
| Cable-life rig | 3–4 |

That saves **≈ 18–35 h**.

*Cost.*
- **Deleted:** ≈ $175 (finger cots, 3 reliefs, 4 valves, 3 pressure sensors, breakers, MR63s, push-fits, PU, and the $70 XY stage).
- **Added:** ≈ $75–105 (one more pancake stepper +$8, coil housing $20–40 [UNKNOWN price per metre], coated wire $8, crimps $8, springs $6, magnets $5, Halls $6, one TMC2209 $5).

Net **−$70 to −100**.

*Risk retired:* V4 sleeve life, V5 leaks, RT2 #9 reverse pressure, the rupture slam, bell-crank yaw (RT2 §3), and the area-mismatch calibration. **The tangential cap becomes a magnetic constant**, the same 2.0 N whatever the firmware does (red lines 3 and 13), backed by the stepper current limit set by VREF.

**(d) Plausibility.**

*Stiffness.* The cable is EA ≈ 5.2 kN, so 3.2 N/mm per cable over 1.6 m. With the series springs that is 1.2 N/mm per cable and **1.9 N/mm at the plate**.
- Shrink under 0.5 N: **0.26 mm** (air: 0.5 mm).
- Plate resonance: 34 Hz, damped by cable friction (air: 25 Hz with ζ ≈ 0.3, RT1 #13).

*Tensions.* A 1 N pad load changes cable tensions by at most ±0.67 N, so a **1.5 N pretension** never goes slack.

*Friction dead band.* ΔT = T(e^{μθ} − 1), with θ the total bend from drum to pad. Dead band = 2ΔT / k_cable [EST]:

| μ | θ | Dead band |
|---|---|---|
| 0.15 | 1.5π | 0.96 mm |
| 0.15 | 2π | 1.96 mm |
| 0.08 (PTFE-lined housing) | 1.5π | 0.43 mm |

On the **line and the precessing line**, every cable length is in phase with s(t), so every cable reverses at the stroke ends, **where the pins are already lifted** (lift at |s| = 0.85). The dead band then only shortens the unloaded end-zone. On the **circle**, each cable reverses mid-contact, giving 0.4–1 mm flats. Per-cable backlash compensation in the IK (a standard CNC trick) leaves ±30 % of that as the friction varies with pose: **≤ 0.3 mm**. That is below the 0.5 mm pass line and 50× under scalp acuity.

*Pose drift.* The inner sits up to 0.12 mm off the housing centreline, times up to 4.3 rad of bend change as the bail travels and the head turns: **≤ 0.5 mm, common to all three cables, absorbed by the tensioner.** The differential residue is ≤ 0.1 mm [EST].

*Path accuracy* (all inside the 0.5 mm pass line):
- line and PLINE: ≤ 0.3 mm;
- circle: ≤ 0.3 mm after compensation;
- heading jumps: instant.

*Max scrub rate:* 2.0 Hz on the line, as for every option (H-5.4, not the drive). R 10 circles at 3 Hz. Drums are good past 5 Hz.

*Noise at the ear.* There is no source on the head. Box ripple is +6 dB relative to air (§1.2); a 1 N/mm spring makes it 0 dB at a cost of 0.5 mm shrink. If the earplug test still hears the box, swap the three steppers for **box-side gimbal motors** (GM3506/4108 class; no mass limit in the box; sine drive with no step ripple; ≈ +$100).

The new head-side risk is **cable creak**: stick-slip of coated wire in the coil at 0.1 m/s radiates at 1–4 kHz, where the threshold is 30–35 µN. Greased PTFE-lined housing is the fix [UNKNOWN until the test].

**(e) Cheapest experiment (≈ $45, one weekend).**

*Build:*
- three $8 pancake steppers on the TMC2209s already in the cart;
- three printed Ø 12 drums;
- 3 × 1.6 m of coated 7×7 wire in two housings for an A/B: 1.2 mm stainless coil (or a long close-wound spring), against bicycle shift housing with its PTFE liner;
- a printed slave plate on three marbles with a felt pen, and the leap3-B PP hinge.

*Run:* line, PLINE rosette and R 12 circles at 1.4 Hz, with the housings coiled through 1, 1.5 and 2 turns; then a 50 g drag weight on the pen; then tape the deck to the $20 bike helmet and do the earplug A/B (leap3-D protocol).

*Pass:*
- bow ≤ 0.5 mm;
- circle flats ≤ 0.3 mm after compensation;
- shrink ≤ 0.5 mm at 0.5 N;
- centre drift ≤ 0.5 mm across the coil changes;
- with earplugs, the slave running is indistinguishable from off.

**(f) Replaces / combines.**
- **Replaces:** the XY master, 6 cylinders, 6 bell cranks, the charge valve, 3 reliefs, 3 dumps, 3 breakers, 3 pressure sensors and the re-zero firmware.
- **Keeps:** the air pins, the halo, the PP parallelogram, the RCC palm and fail-to-free (a power loss leaves the cables limp and the pins vented). The "puppet" binding is kept in spirit: the master stays in the box.
- **Changes:** DECISION-2's "three sealed lines" becomes "three tendons". That needs Michael's one-line OK.

**(g) Honest reasons it might fail.**
- Friction may vary with pose more than ±30 %, leaving visible circle flats. The fallback is PTFE-lined housing, or circle only at R ≤ 8 mm.
- The coated wire may fray at the drum or the crimp at 10⁴ cycles per session. Wire is cheap, but it is a consumable.
- The coil housing may squeak in the 1–4 kHz band.
- Routing three housings through the ear-axis hub (RT2 #2) is new fiddly work.
- The magnetic coupling may part on plough spikes (1 N spikes against a 2 N set; margin 2).

---

## LEAP 2 — SILENT HANDS: gimbal FOC motors on the pad, and why the twin kills them

**(a) Assumption broken.** "Motors on the head are loud." Gearless gimbal BLDCs under FOC put their tones at 7–120 Hz, the bone-conduction deaf band. The path becomes pure software on the head: no master and no synchro, so it deletes the XY stage, the synchro and the box master noise together.

**(b) Two geometries** [EST, `l4d.py`].

| | **G2: stacked two-crank** (leap2-B kinematics) | **G5: five-bar** |
|---|---|---|
| Layout | Motor A on the deck drives a stage-1 plate on 3 parallel eccentrics (r 7.5 mm). Motor B rides that plate and drives the block on 3 eccentrics. | Both motors fixed to the deck. Best search: d 40, L1 18, L2 45, workspace centre 42.5 mm out |
| Change points / singularities | Three parallel eccentrics have no change point and need no PP hinge. (A two-motor rhombus would hit a change point at every stroke centre, because O is always the second solution, so it is rejected.) | Worst case 19 mN·m per N; footprint about 100 mm |
| Torque per motor | 3.0 mN·m typical, 7.5 at a 1 N spike | 7.7 typical, 19 at spikes |
| Heat per PM1806 (20 g, 5.9 Ω, Km ≈ 0.011) | **0.08 W** | **0.5 W, 3 W spikes** |
| Hardware torque cap at a 3.3 V driver supply (Kt·V/R) | 14 mN·m = **1.9 N** at the crank | — |
| Mass per pad | 2 × 20 g motors, eccentrics 6, plates 10, encoders 4, harness 7 = **≈ 67 g** | **≈ 62 g** |

The torque cap is a **physical constant, not firmware** (red line 13), as the pump stall is for the pins.

**(c) What it moves.**
- Path ≤ 0.1 mm in all modes; switching in < 50 ms.
- Grain freedom: 4 Hz small circles; stroke length free per stroke.
- Box noise down (no master).
- Hours: synchro plus master 40–71 h → **26–46 h** (FOC bring-up and noise tuning are the long pole for a first-timer).
- **Mass +26–31 g per pad.** Single ≈ 412–417 g (legal, over the 400 g spec target). **Twin ≈ 532–542 g: it breaks red line 10 (and the 500 g twin binding).** Even the 4-pin twin (456 g) lands at 508–518 g.

**(d) Plausibility.**
- Heat is fine for G2.
- Noise is fine only with 14-bit encoders (MT6701 or AS5047), a 200 Hz torque low-pass, PWM ≥ 25 kHz and an anti-cogging table (§1.3). Cogging is the residual risk: −7…+14 dB.
- Wires to the pad: 10 cores (or 4 if the drivers ride the carriage).
- DECISION-2's "no wires on the pad" is not binding.

**(e) Cheapest experiment ($45).** One PM1806 or 2204 with an MT6701 and a SimpleFOC Mini. Build a 7.5 mm crank with a 40 g mass on a deck taped to the bike helmet; run it at 1.4 Hz. Put an MPU-6050 ($3) on the deck to log the 60–120 Hz cogging line with and without anti-cogging. Then the earplug A/B. **Pass:** inaudible with earplugs, and the cogging line ≤ 10 mN.

**(f) Replaces / combines.** It replaces the master and synchro. It is the **SP2 drive** if a later helmet frees 60 g, and the single-pad fallback if both L1 and the air fail.

**(g) Why it fails for SP1.** Mass, against a binding twin. Also: cogging is unknown for these motors; FOC tuning is a new skill; heat in G5.

---

## LEAP 3 — THE WATER PUPPET: stiffest, cheapest, and the wrong answer

**(a) Assumption broken.** Rolling diaphragms are needed only because air has stiction and compliance problems. Water lets cheap BD syringes work.

**(b) Principle.** The same 3-line pinwheel, filled with degassed water (or 30 % propylene glycol against growth). Use 10 ml syringes, or Ø 20 printed bores with syringe plungers.

**(c, d) Numbers** [EST]:
- Per-line stiffness A²/(dV/dP) = **42 N/mm**, 47× air.
- Syringe stiction of 1–3 N moves only 0.03 mm, so there is **no stick-slip**. Copy error ≤ 0.05 mm.

The costs:
1. **Box ripple +37 dB over air** (§1.2). It needs a series spring, which gives back the air's compliance.
2. **Thermal over-constraint.** 18 ml × 2.1×10⁻⁴/K is 3.8 µl/K, which is 12 µm/K per line against 42 N/mm. A 10 K box warm-up is about 5 N of preload change per line, so it needs a compliance or a re-zero valve again. That is the same hardware it was meant to delete.
3. **Mass +10 g per pad** (water in the lines).
4. **A leak is water in the hair;** filling and bleeding is a new skill.
5. **The cap is not natural.** It needs the L1 magnetic coupling anyway.

**(e) Test ($15).** Two 10 ml syringes and 1.5 m of water line. A kitchen-scale stiffness test, then a hot-water-bath thermal test.

**(f, g)** It replaces nothing net. **Park it.** Its only use is as a stiffness fallback if Michael ever asks for "crisper" tangential, and L1 with stiffer springs gives that dry.

---

## LEAP 4 — PUSH-PULL BOWDENS INTO A FLEXURE XY: the obvious mechanical puppet, and why three tendons beat two rods

**(a) Assumption broken.** "A Bowden puppet needs a replica." Two push-pull cables, X and Y, from the box XY stage into a two-stage PP flexure XY on the pad (leap3-B L4).

**(c, d) Numbers** [EST]:
- **Backlash.** A push-pull inner needs radial clearance: 0.1–0.2 mm × 5–6 rad of total bend × 2 gives **1–2.4 mm of backlash at every axis reversal**. In circle mode that is mid-contact. In a line off the axes, both axes reverse at the ends (lifted), so it survives.
- **Cross-talk.** Two orthogonal rods at the block need cross-slides, which are sliding keys that tick (the Oldham problem). Without them, ball-ended links at 60 mm give y²/2L = **1.9 mm** of cosine cross-talk (warpable in software).
- **No common-mode rejection.** Two cables for two DOF means bail-travel path changes move the pad centre directly (±0.5 mm).
- **Stiff inner.** A solid Ø 0.9 mm inner has EI ≈ 6,400 N·mm², 20× the PU tube, so it resists head turns and hub travel.
- **Backlash clacks** are impulsive and broadband: the worst spectrum for a 2 kHz ear.

Head mass is about +5 to +15 g per pad over air.

**(e) Test ($10).** A Sullivan-style push-pull rod and a dial gauge at 1.5 turns. **Expected result:** ≥ 1 mm of lost motion.

**(f, g)** **Reject in favour of L1.** Tension-only cables have no clearance to take up; three of them reject common mode; and they need no cross-slide. The flexure half of the idea, the PP parallelogram, is already in the baseline and stays.

---

## 3. Best bet: keep the puppet, drop the air. The three-drum tendon puppet (L1), with a 2 N/mm series spring and a 2.0 N magnetic tangential fuse

**The case.** The provocation asked whether the puppet is worth it. **It is.** Each alternative fails as follows:

| Option | Why it fails for SP1 |
|---|---|
| Motor on the pad (G2/G5) | It is the only way to get software paths without a master, and with 14-bit FOC it can be quiet. But it costs **+26–31 g per pad**, and the binding twin goes to **532–542 g**, past red line 10. It also brings the one source on the head that must be tuned below a 35 µN, 2 kHz threshold. |
| Water | Stiffest copy, but **37 dB louder** for the box's stepper ripple. It needs back the compliance and re-zero it was meant to remove, and it puts water in the hair. |
| Two push-pull rods | Clearance backlash, cross-slides, no common-mode rejection. |

**What is not worth it is air as the medium.** Air's three virtues have to be kept; three tendons on three drums keep them, and delete almost everything else:

| Air virtue | How the tendon puppet keeps it |
|---|---|
| Nothing on the head that makes sound or heat | still true |
| Path-independent copy through a travelling bail | common-mode tensioner (Σeᵢ = 0) |
| Soft, filtering compliance | a 2 N/mm series spring per cable |

What goes: the sealed cylinders, the sleeves and their life test, the bell cranks and their replica, the charge/relief/dump/breaker set, the leak hunt and the re-zero firmware. The XY stage collapses into three drums, because inverse kinematics replaces the replica. Pad B rides the same drums as a point mirror, so no extra motors are bought. The tangential cap becomes a magnet: a constant, not a pressure budget. Hall-flexure stops keep the drag vector.

**Revised numbers if L1 is adopted** [EST/JUDG]:

| | Baseline | With L1 |
|---|---|---|
| Hands-on hours | 165–230 | **≈ 140–205** (−18 to −35 h; the largest single block of leak-hunting gone) |
| Parts cost | ≈ $1,450–1,500 | **≈ $1,360–1,420** (+ tools unchanged) |
| Head mass, single | 386 g (370 light) | **≈ 378 g** (≈ 362 light) |
| Head mass, twin | 480 g | **≈ 464 g** (margin 20 → 36 g) |
| Path error | shrink 0.5 mm; bow ≤ 0.4 mm | **≤ 0.3 mm** in every mode after compensation; no 25 Hz ring |
| Max scrub rate | 2.0 Hz line | unchanged (2.0 Hz; R 10 circles at 3 Hz) |
| Noise at the ear | none on head; box ripple ref | none on head; box ripple +6 dB vs air (0 dB with a 1 N/mm spring); cable creak [UNKNOWN] |
| P(on-par \| full session) | 0.40 | **≈ 0.40–0.42**: the pins set the sensation; slightly crisper copy and no ring |
| P(reach) | ≈ 0.50 | **≈ 0.55**: V4, V5, RT2 #9 and the rupture slam retired; dead band and cable life added |
| **P(≥ 7/10 in 26 weekends)** | ≈ 0.20 | **≈ 0.22–0.23** |

This is an honest **moderate** leap, not a step change. The drive was never what limited the rating; the pins and the hair are. The step change on offer here is **risk and hours**: the most failure-prone and least sensation-relevant subsystem in the baseline is replaced by string, three drums and a magnet. That is settled by a $45 ink-and-earplug weekend before the Day-0 cart commits to finger cots, reliefs and breakers.

**Decision asked of Michael:** "three sealed lines" → "three tendons" in DECISION-2, conditional on the L1 bench pass. If the test fails (circle flats > 0.3 mm or audible creak), keep the air synchro unchanged. Keep G2 (the stacked two-crank gimbal) on file as the SP2 drive for a lighter helmet.
