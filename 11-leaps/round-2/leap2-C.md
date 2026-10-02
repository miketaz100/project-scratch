# LEAP 2-C — PNEUMATICS, PUSHED FURTHER: an all-air pad

**Project SCRATCH · 11-leaps/round-2 · Leap Agent C · 2026-10-02**
Provocation: fewer tubes, air that also makes the orbit, pressure tricks instead of valves, real parts with honest numbers.
Read: LEAP2-BRIEF; leap-B §1, L1, L2, §3; leap-A L2; scratch-model §1–3, §7; hair-interaction §4–6; safety §2, §7; pin-unit §1; concept-A §1–4; leap-E; leap-F. Firewall kept.
Tags: **[KNOWN]** sourced · **[EST]** computed here · **[UNKNOWN]** bench only.

---

## 0. Where the latency, noise and cost really are

Round-1 design: a hand-sized pad with 8–16 air pins orbiting at r ≈ 10–20 mm, one 1.5 mm tube and one desk valve per pin. Three facts set up every leap below.

**Latency is in the swept volume, not the tube.** 1.2 m of tube adds an acoustic delay of L/c ≈ 3.5 ms and a line-fill time of 32µL²/(d²P) ≈ 2.6 ms (1.5 mm ID) [EST]. The slow part is pushing the pin's swept volume through the valve. A 7 mm bore retracting 25 mm out of the canopy (H-5.2) takes ≈ 1.1 ml of free air per landing at 15 kPa. Through an orifice, Q ≈ 0.6·A·√(2ΔP/ρ). An effective area of 0.5 mm² passes 39 ml/s at 10 kPa (≈ 28 ms per landing); 0.2 mm² takes ≈ 70 ms [EST]. Moving valves to the neck saves ~5 ms, not 30. **Force is pressure, not position:** a 1 ml chamber vents through 0.5 mm² in < 10 ms [EST], long before the pin has risen. The 50–90 ms full retract matters only for hair stirring.

**Cheap BP valves die in a week.** Koge KSV05A has a 30,000-cycle life. Its "300 → 10 mmHg from 100 ml in < 3 s" spec implies ~11 ml/s at 10 kPa, so ~90 ms per landing [EST] ([datasheet](https://koge-europe.com/wp-content/uploads/datasheet-KSV05A.pdf)). FA0520E 3-way: 50,000 cycles, ≤ 400 mA at 6 V (2.4 W held), $1.35–3.75 ([Adafruit](https://www.adafruit.com/product/4663), [Electropeak](https://electropeak.com/fa0520e-three-way-gas-air-electric-solenoid-valve)). A 20-min session at 3 Hz is **3,600 cycles per pin** [EST], so a KSV05A lasts ~8 sessions and an FA0520E ~14. Use them for benches only.

| Valve (datasheet) | Response | Price | Note |
|---|---|---|---|
| SMC S070 3-port, 7 mm, 5 g | **3 ms on / 3 ms off** at rated V; 0.1–0.5 W | **$31–37** ([SMC](https://www.smcpneumatics.com/S070C-SDG-32.html), [catalog](https://www.smcpneumatics.com/pdfs/S070.pdf)) | best value; life [UNKNOWN, industrial class] |
| Festo MHA1 3/2 | 4 ms | $52–57 ([MHA1](https://www.motionworld.com/assets/MHA1_datasheet.pdf)) | |
| Lee LHD 3-way | ≤ 10 ms | $63 ([Lee](https://www.theleeco.com/product/lhd-series-3-way-control-solenoid-valve/)) | tiny |
| Parker X-Valve | ≤ 20 ms | $39 ([Parker](https://ph.parker.com/us/en/product-list/x-valve-miniature-pneumatic-solenoid-valve)) | |
| FA0520E / KSV05A | unspecified (~10–20 ms [EST]) | $1.35–3.75 | bench only |

**Pumps.** KPM27C: > 1.8 L/min free flow, > 53 kPa, **63 dB at 30 cm** ([Koge](https://www.made-in-china.com/showroom/koge-pump/product-detailZqSnehJVfUkj/China-Pressure-Pump-KPM27C-.html)). That is ≈ 52 dBA at 1 m bare and ≈ 37–42 dBA in a lined box with an inlet muffler [EST]. Murata MZB3004T04 piezo: 50–60 kPa, but only 200 ml/min, driven above 20 kHz so inaudible ([Murata](https://www.murata.com/en-us/products/mechatronics/fluid/overview/lineup/microblower_mzb3004t04)): good for topping up a sealed system, no use for pins. **Air budget:** 8 pins × 1.1 ml × 2–3 landings/s ≈ 1.1–1.6 L/min [EST]; one KPM27C at 1 Hz, two at 3 Hz.

**Force cap gap.** 16 pins × 1.54 N (40 kPa relief, 7 mm bore) = 24.6 N, over red line 3's 12 N if all land together. Round-1 trusted firmware for that. C2 makes it mechanical.

---

## LEAP C1 — AIR SYNCHRO ORBIT: three sealed air lines move the pad; nothing on the head turns, ticks or is powered

**(a) Assumption broken.** "The orbit needs a motor on the head." That motor is the head's only source of noise, heat, wires and stiff position drive.

**(b) Principle.** A pneumatic synchro, the fluid equivalent of a three-phase shaft link. At the desk, an N20 gearmotor turns a 3-throw crank (throws at 120°) that strokes three master syringes. Three **sealed** lines run to three silicone bellows at 120° around a pin plate hung on parallel flexures (translation, no rotation). Master volumes v₀ + a·cos(ωt − 2πk/3) drive the plate in **circular translation**. The volumes sum to a constant, so no air is consumed, nothing exhausts, and there is no valve. A charge of p₀ ≈ 15 kPa keeps all bellows pushing. A brake-master-cylinder **compensating port** (a 0.5 mm hole in each syringe wall, open at top dead centre) re-zeroes each line every revolution, so a leak cannot cause drift.

```
 DESK (foam box)                                    PAD: plastic + silicone only (plan)
 N20 ─► 3-throw crank 120°                                  B1 bellows Ø22
  ├─ syringe M1 10 ml ══ line 1, 4/2.5 PU, 1.2 m ══╗          ║
  ├─ syringe M2 ════════ line 2 ══════════════════╗║    ┌─────╨──────┐
  └─ syringe M3 ════════ line 3 ════════════════╗ ║╚═B2─┤ ○  ○  ○    ├─B3   pin plate 60×50,
 compensating port at TDC; relief p₀+8 kPa/line  ║ ╚════┤  ○  ○  ○   │      8 pins @ 20 mm,
                                                 ╚══════└────────────┘      4 flexure legs
 master stroke = r_o·A_slave/A_master = 10 × 3.8/1.65 ≈ 23 mm; plate circle r_o 6–12 mm, 0.5–4 Hz, never reverses
```

**Rejected for the orbit, with numbers.** *Air turbines and vane motors:* 10³–4×10⁵ rpm, so 1–3 Hz needs a 10³–10⁵:1 gear train on the head, plus 20–60 L/min of air and 65–80 dBA exhaust [EST, typical]. *PneuAct 3D-printed pneumatic stepper:* 800 rpm, 3° steps, all plastic ([PneuAct](https://www.researchgate.net/publication/325895726_Introducing_PneuAct_Parametrically-Designed_MRI-Compatible_Pneumatic_Stepper_Actuator)); still ~400:1 reduction, and it clicks every step. *One-tube variant:* a soft ring oscillator gives phased outputs from one constant pressure, but tops out near **1 Hz**, is strictly periodic, and is hard to cast ([Preston 2019](https://www.science.org/doi/10.1126/scirobotics.aaw5496)). The synchro is the continuous, silent relative of all three.

**(c) Sensory variables moved.**
- *Sound (§1 D, §7 rank 15):* head-side noise falls from servo whine (40–50 dBA, bone-conducted [EST]) to about room level. The nail-on-hair hiss becomes the only sound.
- *Tangential compliance and cap (§7 rank 7, H-4.11, red line 3):* air-line stiffness k = P·A²/V ≈ 1.4 N/mm per line (3.8 cm² bellows, 12 ml, 1.15 bar abs), ≈ 2–3 N/mm across the plate [EST]. A 0.5 N scratch drag costs 0.2 mm of orbit. The **relief valve per line** (+8 kPa ≈ 3 N on the plate, ≈ 0.75 N per pin with 4 down) is a mechanical tangential cap: on a snag, the line relieves and the plate stalls while the crank turns on.
- *Irregularity (ranks 1, 4):* orbit speed follows the desk motor, free and smooth, and nothing on the head can reverse.

**(d) Plausibility.**
- *Viscous loss* at 3 Hz, r_o 10 mm: peak flow 72 ml/s gives 1.6 kPa in 2.5 mm ID, 0.25 kPa in 4 mm ID [EST]. It acts as damping, and the desk motor pays for it.
- *Resonance:* a 60 g plate on 2.5 N/mm sits at ≈ 32 Hz, far above the drive and tube-damped [EST; damping UNKNOWN].
- *Mass:* the pad with C2 and 8 pins is **≈ 90 g** with no electronics, against ≈ 130–150 g with two servos [EST].
- *Cost:* ≈ $20.

**(e) Cheapest experiment (≈ $25, a weekend).** A printed 3-throw crank with 10 ml syringes, three bellows suction cups (Ø20–25, 2.5 convolutions, $1–3), 3 × 1.2 m PU lines charged by syringe, and a TPU-flexure pad dragging three nails on felt at 0.3 N each. Phone at 240 fps from above. **Pass:** ≥ 80 % of the no-load radius at 3 Hz; < 1 mm drift in 20 min; dBA at 10 cm from the pad equal to room noise; ≤ 35 dBA at 1 m from the box.

**(f) Combines.** Keeps round-1 pins and firmware. Whatever carries the pad (leash, boom, crown track, leap-F puck) now carries ~90 g and 5–6 tubes (9–13 mm bundle) with no wires.

**(g) Might fail because** bellows may buckle sideways or fatigue at ~11,000 cycles per session [UNKNOWN]; soft flexures let the plate yaw, and yaw drags pins sideways; the radius is fixed by the crank, and varying it per revolution needs an open, valve-driven version that brings back exhaust.

---

## LEAP C2 — THE ORBIT IS THE DISTRIBUTOR: a sample-and-hold commutator writes every pin's force and landing through one supply tube

**(a) Assumption broken.** "Per-pin, per-stroke control needs a valve and a tube per pin." A player-piano tracker bar and an engine distributor both time-share one source using a part that already moves. Here that part is the orbit.

**(b) Principle.** The orbiting plate has a 1.5 mm port per pin on its upper face. A fixed **stator** inside the hood (≥ 30 mm from the scalp) is a PTFE face on float glass, spring-loaded onto the plate. Because the plate translates without rotating, each port traces its own small circle of radius r_o. The stator patterns each circle with three arcs:
- a **write arc** (≈ 20°) open to the shared supply gallery;
- a **hold land** (60–90°), blind and sealed: the pin keeps the pressure it was given;
- a **vent arc** (the rest), open to a return gallery piped back to the pump inlet, so nothing puffs at the head.

Write arcs are staggered so **only one pin is written at a time**. The desk sets the supply pressure as each pin's write arc passes: 0 kPa skips it, 6/10/14 kPa sets its force, and when the pressure rises within the arc sets its landing time. Lift happens at the vent arc, every revolution, by geometry.

```
 one pin's track on the stator (port circle r_o = 10 mm)
            .-‾‾‾ hold land (sealed): force held through the stroke ‾‾-.
  write ┌─/ ●port                                                    \
  20°   └─\                       vent arc → return gallery → pump inlet
            '-.____________________________________________________.-'
 8 pins: group A windows near φ = 0° (rake ↑), group B near 180° (rake ↓) = bidirectional P1
 within a group, write arcs 20° apart (55 ms at 1 Hz): landing spread 0–80 ms, direction spread ±30°
 DESK: 3 rail valves (S070) → ONE supply line → 15 ml plenum on pad → stator gallery
 dead-man seal: stator preload is a piston fed by supply; supply dumped → seal lifts → every pin vents
```

**(c) Sensory variables moved.**
- *Per-pin force and asynchrony re-drawn every stroke (ranks 1, 3, 6),* through one tube, with no head electronics.
- *Timing precision improves.* Landings are referenced to the plate's own position, so the desk path (S070 + tube ≈ 6–10 ms) only has to fit inside a 55 ms write arc. The fill is local, through a 1.8 mm² port: 1.1 ml in ≈ 8 ms [EST], against round-1's 30–60 ms.
- *Lift-before-reversal and the 12 N total become mechanical.* The vent arcs force every lift. The stator geometry caps how many pins are pressurised at once: ≤ 4 for 8 pins in two groups; ≤ 6 for 16 pins (6 × 1.54 N = 9.2 N < 12 N). Red line 13 is met by construction.

**(d) Plausibility.**
- *Seal:* a hold land must keep a 3 ml chamber for ≤ 250 ms. Across a 2 × 5 mm land at 15 kPa, a 5 µm gap leaks 0.02 ml/s (≈ 1 % droop) and a 20 µm gap leaks 1.4 ml/s (≈ 77 %) [EST, h³ law]. The seal needs ≤ ~8 µm: lapped PTFE on glass, achievable, but not a printed part.
- *Friction:* 3–5 N preload × µ 0.1 adds 0.3–0.5 N to the orbit drive.
- *Held pin as a gas spring:* k = P·A²/V ≈ 0.057 N/mm at 3 ml, so ±1 mm of scalp contour changes force by ±0.06 N, inside pin-unit R2 [EST].
- *Supply:* a 15 ml pad plenum sags ~7 kPa per 1.1 ml landing [EST], so refill must come down a 2.5–4 mm ID line, which delivers hundreds of ml/s at a few kPa of drop. The sag also softens landings, which is good.
- *Rate:* a 20° arc lasts 55 / 28 / 18 ms at 1 / 2 / 3 Hz, so **full per-pin writing works to ~2 Hz** and is marginal at 3 Hz. Leap-A's 4–6 Hz grain needs per-pin valves.
- *Valves:* only 3 desk valves, switching ~3 times/s each, so S070s at $105 total instead of 16 × $35. **Each extra pin costs ≈ $2.**

**(e) Cheapest experiment (≈ $20 over round-1's bench).** Two pins and two stator tracks drilled in 3 mm PTFE on a 4 mm glass offcut, orbited by hand or by the C1 rig. Desk side: one FA0520E and a KPM08C. Tee an XGZP6847A ($4) into one pin and log hold droop, cross-talk, and landing time against the commanded write at 1 and 2 Hz. Then ink the nails: skipped strokes, three force levels, 0–50 ms landing shifts.

**(f) Combines.** With C1, the head takes **5 tubes** (3 orbit, supply, return) for 8 or 16 pins. An optional 6th "direction" line drives one bellows and spring that rotate the stator ±30°: a slow oscillation inside the hood (H-6.2 (2)) that rotates every window, i.e. the rake axis.

**(g) Might fail because** (1) the seal is precision work, and dust or shed hair on the glass turns hold into leak; (2) no two pins can be written at the same instant; (3) per-pin *window* freedom (round-1 L2) is lost: windows are fixed relative to the orbit and only the direction line moves them all together, while landing time, force and skip remain per pin; (4) performance degrades above ~2 Hz.

---

## LEAP C3 — PRESSURE-CODED TIMING: capillaries and thresholds make asynchrony, sweeps and damping from one valve

**(a) Assumption broken.** "Different timing per pin needs a different valve event per pin." Also a correction to the provocation: an orifice sets **rate**, and steady force is always P_rail × area. Force is graded per pin by **bore** (6/7/8 mm → 0.28/0.38/0.50 N at 10 kPa). A bleed divider could set force but costs ~0.3 L/min per pin [EST]. Timing is graded by **orifice**.

**(b) Principle.** Pins in a cluster share one line, each through its own capillary (0.25 mm ID PTFE cut to length, or 27G blunt needles at $0.10). Each has a light preload, so it moves at threshold P_th. Landing time is t_i = τ_i·ln(P_s/(P_s − P_th)).

```
 valve ─► line ─┬─[cap  7 mm]─► pin 1  τ 10 ms    P_s 15 kPa: lands  4 /  8 / 16 /  24 ms  (spread 20)
                ├─[cap 15 mm]─► pin 2  τ 20 ms    P_s  7 kPa: lands 13 / 25 / 50 /  75 ms  (spread 62)
                ├─[cap 30 mm]─► pin 3  τ 40 ms    P_s  6 kPa: lands 18 / 36 / 72 / 108 ms  (spread 90)
                └─[cap 45 mm]─► pin 4  τ 60 ms    P_th 5 kPa; C ≈ 7×10⁻¹² m³/Pa (~1 ml); R = 128µL/(πd⁴)
 two-step supply: a short "timing" level, then a step to the "force" level
 row version: capillaries in series along a line of pins = RC ladder → landings travel down the row
```

**(c) Sensory variables moved.**
- *Asynchrony (rank 6; §4.2's 20–80 ms):* re-drawn every stroke by **one regulator level**, from 20 to 90 ms. The two-step supply decouples force (rank 3).
- *P2 sweeps (rank 9):* a row on a series ladder fires in sequence from one valve (sequential-slip apparent motion), and a second valve at the far end reverses the sweep.
- *Soft landings (P6):* a long capillary gives the 0.2–0.5 s ramp.
- *Resonance (§2.1):* a 1.2 m line is a quarter-wave pipe at ≈ 71 Hz, and a pin on its air spring rings at ≈ 22 Hz [EST]. A valve step excites both, in the flutter/Pacinian band that must not appear. The capillary at the pin is the damper round-1 lacked.

**(d) Plausibility.** The arithmetic is first-order. Flow at fill start reaches Re ≈ 1,000: laminar but marginal, so calibrate each capillary [EST]. Two real costs:
- *Fixed order.* Landing **order** is fixed by build, and fixed stagger is learned in 3–5 strokes (Red Team 1). The spread varies every stroke; the order does not, unless the line is fed from both ends.
- *Slow full landings.* A 20 ms capillary also slows a full 25 mm landing to 150–300 ms. That suits hover-height or slow modes, not fast full-retract grain. Venting needs a parallel duckbill check ($0.20).

**(e) Cheapest experiment (≈ $10, an evening).** Four round-1 bladder pins on one FA0520E with 7/15/30/45 mm capillaries. Phone at 240 fps over a ruled card; step the supply to 6/7/10/15 kPa and measure the spread. Tap a sensor at one pin with and without its capillary to watch the 22/71 Hz ringing appear and vanish.

**(f) Combines** with C2 (pins sharing a write arc land with a coded spread), with round-1 L1 (four pins on one valve), and with C4 (sweep generator).

**(g) Might fail because** capillaries clog, so a 10 µm inline filter is mandatory; bladder hysteresis smears the threshold; and a fixed order may still be learned.

---

## LEAP C4 — FINGER BUS ON A LATIN TILING: many pins, few tubes, for the virtual full-head field

**(a) Assumption broken.** "A virtual field needs a tube per pin" (~90 pins at 20 mm pitch over the ~360 cm² top of the head). A physical 8–16-pin pad does not need this leap, since 16 × 2.5 mm OD tubes pack to ~12 mm. Tube count matters only for the virtual field.

**(b) Principle.** Separate *which pins are fingers* (slow) from *what fingers do* (per stroke).
- *Five fast finger lines* F0–F4 come from desk S070s, giving full round-1 control per finger.
- *A Latin tiling wires each pin to one finger line:* line(i, j) = (i + 2j) mod 5. Any 5 pins in a row or column, any 2×2 block and any plus-shape then hold **distinct** lines (the perfect Lee-sphere tiling of the grid), so a hand-shaped group anywhere has independent fingers.
- *A latch per pin selects whether it is active:* a cast bistable snap-through membrane valve ([Rothemund 2018](https://www.researchgate.net/publication/323925161_A_soft_bistable_valve_for_autonomous_control_of_soft_actuators)) sits between the pin and its finger line. It is armed by **coincident row + column pressure** (each 0.6 × snap): core memory in air, a cousin of microfluidic multiplexers that address n channels with 2·log₂n lines ([Thorsen 2002](https://web.mit.edu/Thorsen/www/580.pdf)).

```
 line(i,j) = (i+2j) mod 5      9 × 10 field = 90 pins
  j=0:  0 1 2 3 4 0            tubes: 5 finger + 9 row + 10 column + 1 return = 25 (vs 90)
  j=1:  2 3 4 0 1 2            re-arm a 5-finger "hand": 10 latch writes × ~40 ms ≈ 0.4 s
  j=2:  4 0 1 2 3 4            drift at 3 cm/s = one re-arm every ~0.7 s
```

**(c) Sensory variables moved.** Region and dwell (ranks 13, 14) become free and continuous: the "hand" relocates in 0.4 s with no mechanism, and leap-A's slow carrier becomes a moving armed set. Ranks 1, 3 and 6 stay at round-1 quality.

**(d) Plausibility.** Address lines carry pressure but no flow, so 1 mm ID is enough. If cast snap pressures scatter ±15 % [UNKNOWN], half-selected pins see 0.6 against the weakest latch at 0.85, and the selected pin sees 1.2 against the strongest at 1.15: thin but positive margins [EST]. Material cost ~$0.50 per pin. The orbit becomes a whole-shell C1 (150–250 g, larger bellows).

**(e) Cheapest experiment (≈ $15).** Cast six membranes in printed moulds. Build a 2×3 coincident board and log snap scatter and half-select disturbs over 1,000 writes. If scatter exceeds ±20 %, fall back to per-pin tubes or SMA selectors (round-1 L4).

**(f/g)** This is the pneumatic answer to *virtual* repositioning. It might fail because 90 hand-cast latches must all work, 25 tubes is still a hose, and most of the field's mass sits idle.

---

## 5. System numbers, 8- and 16-pin pad

| | Round-1 (per-pin desk valves, servo orbit) | **C1 + C2 all-air pad** | C1 + per-pin S070s |
|---|---|---|---|
| Tubes to pad | 8–16 + motor wires | **5 (6 with direction)**, no wires | 11–19 |
| Electronics on head | orbit servos | **none** | none |
| Force on/off latency | 30–60 ms | **≈ 8 ms local**; desk latency hidden in the write arc | 15–25 ms |
| Per-pin per-stroke control | land, force, lift, window | land time, force, skip | full |
| Max rate with full per-pin control | ~3 Hz | **~2 Hz** | ~3 Hz |
| Noise at head | 40–50 dBA servo, bone-conducted [EST] | **≈ room noise** | ≈ room noise |
| Desk box at 1 m | 37–42 dBA + clicks + exhaust puffs | 35–40 dBA, no exhaust | 37–42 dBA + clicks |
| Total-force cap | firmware | **stator geometry (≤ 4–6 pressurised)** | firmware |
| Tangential cap | servo torque | **relief per synchro line** | relief |
| Pad mass | 130–150 g | **≈ 90 g** | ≈ 80 g |
| Parts, 8 pins | ≈ $95 bench / $370 S070 | **≈ $180** | ≈ $340 |
| Parts, 16 pins | ≈ $130 / $650 | **≈ $195** | ≈ $620 |

**Failure modes of the all-air pad.**
- *Supply kinked or e-stop:* the dead-man seal lifts and every pin vents. Safe.
- *Return kinked:* a **mandatory** 3 kPa relief from the return gallery to atmosphere at the pad keeps lift working; without it, pins stay down (red line 8).
- *Synchro leak:* the radius shrinks until the compensating port refills the line at TDC. Benign.
- *Snag:* the line relief pops and the plate stalls with nothing reversing. A pressure sensor per line triggers lift-all (H-6.6).
- *Scored seal:* shows as pressure noise on the return-gallery sensor. It degrades the device; it does not harm the user.
- *Bladder fatigue:* 3,600–11,000 cycles per session. Latex cots are the weak link; move to glass/graphite pistons or cast silicone.

---

## Best bet: C1 + C2, the ALL-AIR PAD (build C1 first)

Make the orbit out of air, and let the orbit distribute the air. Three sealed synchro lines translate the hand-sized pin plate in a circle with no motor, gear, wire or valve on the head. A lapped PTFE-on-glass stator above the plate turns that orbit into a tracker bar: once per revolution, each pin is written with its own force and landing time from **one** supply tube, held through its stroke, and vented by geometry. That buys four things round-1 either trusted to firmware or paid for per pin:
1. **Silence at the head:** hair hiss only.
2. **Mechanical safety constants:** lift-before-reversal, the 12 N total and the tangential cap come from stator geometry, relief valves and a dead-man seal (red lines 2, 3, 8, 13).
3. **≈ 8 ms local landings,** with desk latency hidden inside the write arc.
4. **A ~90 g, 5-tube, wire-free pad,** so whichever repositioning carrier wins moves less and drags less. Pins cost ~$2 each, so 16 cost about what 8 do.

The price is per-pin window freedom and a ~2 Hz ceiling for full per-pin writing. C3's capillaries recover cheap asynchrony, a 6th "direction" line recovers rake-axis wander, and leap-A's 4–6 Hz grain can still use per-pin S070s on the same C1 pad. **Cheapest test: C1 alone, ≈ $25, one weekend.** A syringe crank, three bellows cups and a flexure pad dragging three nails on felt. Measure orbit radius under drag at 1–3 Hz, drift over 20 min, and dBA at the pad. If it holds radius and is inaudible, build the two-pin stator track next (≈ $20). Round-1 bench 3, running both firmware modes, answers the deciding perceptual question: does structured per-pin variety read as a hand as well as fully independent gating?
