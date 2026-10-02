# LEAP 4 · AGENT E — Cut the hours: buy, hack, outsource

**Project SCRATCH · 11-leaps/round-4 · 2026-10-02**
**Provocation:** halve the 165–230 hands-on hours without breaking a binding decision, by buying, harvesting and outsourcing.
**Read:** LEAP4-BRIEF, DECISION-2 (+ North Star amendment), decision-analysis, SYSTEM-SPEC (§0–2, 4.3–4.5, 4.7, 13), redteam-3-buildability (in full), bom-verified (in full), scratch-model §1–3, §7–8, hair-interaction §4–6 rules, safety red lines, round-2/3 leap headings.
**Tags:** [KNOWN] = project file or a vendor page checked today (Sources at the end) · [EST] = my arithmetic · [JUDG] = judgement · [VERIFY] = check before ordering.
**Constraint respected:** Michael declined outsourcing the *build* on 2026-10-01 (RESUME.md). Everything below outsources *parts and software*, never labour.

---

## 0. Where the 165–230 hours actually go

The baseline hours are judgement figures. I reallocated them across RT3's stages, using the decision-analysis §4.3 stage totals, so that each leap can be scored against a line item.

| Stage | Work package | Baseline h [JUDG] |
|---|---|---|
| S0 | One-nail rig, coin/helmet evening, earplug servo test | 8–10 |
| A | Electronics: carrier board (≈ 120 TH joints), harness, safety loop, sensors, power | 12–16 |
| A | Firmware bring-up: step generation, 1 kHz gate scheduler, 3 PIDs, sensor scan, servo bus, watchdog, serial | 10–14 |
| A | Rail, palm and vac pneumatics; first valves | 6–8 |
| A | XY master (MGN12 stack, GT2, mounts, homing) | 6–8 |
| A | Three synchro lines (6 cylinders, sleeves, bell cranks, PP parallelogram, charging, ink traces) | 8–10 |
| A | Pin block on the bench + sleeve-life rig | 3–4 |
| B | Pad: RCC, skids, Airpel float, QEV, filters, mufflers | 10–14 |
| B | Pins finished (6 + pad-B parts) | 4–6 |
| B | Static halo with indexed poses | 6–8 |
| B | Apache box fit-out; remaining valves and plumbing | 8–12 |
| B | Sensation firmware (jitter, subsets, dwell ledger) | 5–7 |
| B | Wig, force, proof and fail-to-free gates | 7–8 |
| C | Hub pods ×2 (bearings, GT2 3:1, servo bays, parietal pads) | 12–16 |
| C | Bail bend + splice; carriage + β tendon | 12–15 |
| C | Servo firmware, zero jig, β stops, gear bias | 4–6 |
| C | Umbilical, hanger, pogo breakaway, light lines, head switch | 10–14 |
| C | C-gates: mass, noise, bone path, doff, lean; rework | 12–14 |
| D | Sessions, buttons, armrest switch | 10–20 |
| — | **Total** (with the must-fix work spread through it) | **≈ 165–230** |

Three blocks dominate: **powered travel (C, ≈ 50–65 h)**, **custom electronics + firmware (≈ 27–37 h including sensation firmware)**, and **pneumatic fabrication and plumbing (≈ 35–45 h)**. Buying can only help where a commodity product already does the job. I searched each block for one.

---

## LEAP E1 — THE KLIPPER BOX: buy the controller, write no real-time firmware

**(a) Assumption broken.** "The puppet needs bespoke ESP32-S3 firmware: a 1 kHz gate scheduler with analytic path prediction, two stepper phase generators, three PIDs and a watchdog." In fact this is exactly what an open-source 3D-printer stack does. It moves steppers along a path and switches outputs *in sync with that path*. Sync to the path is the hard part of the hover-and-bite windows.

**(b) Principle and sketch.**

```
 12 V 5 A brick ─► fuse ─► E-STOP(NC) ─► HOLD-TO-RUN relay ─► ACTUATOR RAIL ──┐  (hardware loop unchanged)
                                                                              │
 BTT Manta M8P V2.0 (STM32H723, Klipper MCU)  ◄─ BTB ─►  CB1 / CM4 (Linux: Klipper host + Moonraker + score.py)
   ├ 2 × TMC2209 ─► XY master (cartesian kinematics, homing on endstops)
   ├ HE0–HE3, HB, FAN0–FAN6 = 12 switched outputs (12 V):  6 pin valves (pwm_tool) · LIFT · PALM · CHARGE · SYNC-DUMP · 2 pumps
   │     (+ 1 output on a $3 MOSFET board for pump 3)
   ├ TH0–TH3, TB = 5 ADCs ─► XGZP6847A: rail, palm, synchro ×3   (+ ADS1115 on host I²C for vac/egg)
   └ endstop inputs ─► THERE / MOVE-ON / lever-state buttons (gcode_button)
 Hardware snag reflex: LM393 comparator on each synchro sensor ─► opens the valve-common ─► all pins vent (lift) in < 20 ms
 Optional (powered travel later): Waveshare Bus Servo Adapter (A), USB ─► STS3032 bus, driven from score.py
```

How each spec function maps onto stock Klipper [KNOWN, Klipper source and Config Reference checked today]:

| Spec function | Klipper feature |
|---|---|
| PLINE / LINE / CIRCLE path, stroke-length and heading jitter | `score.py` writes G1 segments: a precessing line is a run of short lines with rotating heading. Stroke length and velocity profile become free per stroke. This exceeds the crank, which had a fixed 30 mm sinusoid. |
| Per-pin bite and lift windows phase-locked to the path | `[pwm_tool]` outputs ("capable of high speed updates"). `SET_PIN` goes through `register_lookahead_callback`, so it fires at the exact print-time between two G1 moves. Pin lead times (valve plus line, 5–15 ms) are set by splitting a move at t − lead. **Note:** plain `[output_pin]` enforces `MIN_SCHEDULE_TIME = 0.100 s` between changes on one pin (mcu.py). At 1.4 Hz, bite to lift is ≥ 126 ms, but use `pwm_tool` anyway. |
| Rail and palm pressure PID | `[adc_temperature]` with a voltage → "°C" table reading kPa, plus `[heater_generic]` with the pump as the "heater". The PID, min/max limits and a host-independent MCU range check come free. Disable or relax `verify_heater`. |
| Watchdog / fail-to-vent | `maximum_mcu_duration` on each `pwm_tool`, plus MCU shutdown on host loss. Every pin goes to `shutdown_value = 0`, which is de-energised = vent = lift. A secondary barrier only; red line 13 stays on the hardware loop. |
| Egg / buttons / lever state | `[gcode_button]` runs host macros (PAUSE, STAY, MOVE ON). |
| Score, ledger, logs | Plain Python on the CB1. The box runs standalone; the laptop is optional. |

**(c) Numbers it moves.**
- **Hours:** electronics 12–16 → 5–7; firmware bring-up 10–14 → 4–6; sensation firmware 5–7 → 3–4; servo firmware (if travel is powered) 4–6 → 2–3. **Saves ≈ 18–27 h.**
- **Skills:** removes "real-time ESP32-S3 bring-up" and "perfboard at scale" from RT3's 14-skill list. These are the two most likely stall points after casting.
- **Cost:** M8P V2 + CB1 bundle **$154.59** (BIQU); the board alone is $65–82. TMC2209 **$7.89** each. Against the baseline core (ESP32, 3 × MCP3208, 3 × TPIC6B595, TMC2209s, JLC carrier ≈ $85) the delta is **≈ +$75–95** [EST].
- **P(on-par):** +0.00 to +0.02. A constant-speed contact phase with quick lifted turnarounds, and free per-stroke length, are easier to write than on the crank or the RT3 XY.

**(d) Plausibility.** Klipper drives printers at 200–500 mm/s and 5–20 m/s². This load is 5 N at ≤ 2 m/s² and ≤ 188 mm/s. Valve events are 2 per pin per cycle: 6 pins × 2 × 2 Hz = 24 events/s, trivial. Command latency through the lookahead queue is ≈ 0.3–2 s. That is fine for THERE and MOVE-ON. It is **not** fine for the snag reflex (H-6.6 needs a lift within 100 ms), which is why E1 adds a $3 hardware comparator that dumps the valve common. This makes the snag reflex a hardware barrier, better than the spec's firmware reflex.

**(e) Cheapest experiment (≈ $35, one evening).** Install Klipper on a Raspberry Pi Pico ($5) as the MCU, with the host on a Pi Zero 2 W or in a Linux VM on the Mac. Use one 17HS08 stepper (already on the Day-0 list) and one LED as a stand-in valve. Stream a 30 mm PLINE with `SET_PIN` windows. Film it at 240 fps against a printed scale. **Pass:** LED edges land within ±2 ms of the commanded path point over 500 strokes, and the heading jitter and stroke-length change from `score.py` are visible.

**(f) Replaces.** ESP32-S3 carrier board, MCP3208s, TPIC6B595s, the 1 kHz scheduler, the step generator, the PID code, the charge-pump watchdog code (kept as hardware) and the servo-bus firmware.

**(g) Why it might fail.** Klipper's heater safety layer fights a "heater" that reads 0 °C. It needs `min_temp: -20` and tuned `verify_heater`, about 1 h of forum time. Pump-PID tuning on a 15 ml accumulator may oscillate, though the bleed and relief still bound it mechanically. BTT stock and board revisions churn. The CB1 adds a Linux box to maintain. None of these touches safety, because the hardware loop is unchanged.

---

## LEAP E2 — BUY THE VALVE ISLAND: a stock S070 manifold, push-fit everywhere, aquarium and BP-monitor parts for the small stuff

**(a) Assumption broken.** "The drive box is plumbed: about 78 joints, printed galleries, barbs and tees." SMC already sells the exact topology. Its S070 base manifolds have a common P port (= the rail gallery), a common R/exhaust (= the lift manifold) and one A port per station (= the pin line).

**(b) Principle.**

```
 RAIL ─► P ┌──────────── SS0755 6-station base (≈ 7 mm pitch, ≈ 50 × 60 mm) ────────────┐ R ─► LIFT SELECT ─► VAC / ATM
           │  S070A-?AC  S070A  S070A  S070A  S070A  S070A   (12 V coil code [VERIFY])   │
           └── A1 ── A2 ── A3 ── A4 ── A5 ── A6 ── M5 → 1/8 in push-fit ─► Ø0.5 sense tee ─► pin lines ┘
 NO dumps (rail, palm, synchro ×3): BP-monitor / massage-chair 12 V NO mini valves, 185 mA class
 Duckbills: aquarium check valves (4 mm barbs, 10-packs)   Restrictors: 27G/30G Luer needles (RT3)   Reliefs: McMaster 4277T51 (RT3)
```

**(c) Numbers.**
- **Joints:** about 78 → ≈ 55. Two joints are removed per pin valve (P and R), plus the printed rail gallery and lift manifold.
- **Hours:** box pneumatics and plumbing 6–8 + 8–12 → 5–7 + 3–5. **Saves ≈ 6–8 h**, most of it leak hunting.
- **Cost:** manifold **$80.90** [KNOWN, smcpneumatics listing]; S070A valves **$35** each, the same as the S070C [KNOWN]. You lose RT3's cheap-valve A/B option (up to −$168 at 6 pins), because cheap valves do not fit the base. **Net ≈ +$70**, or ≈ +$240 if the cheap valves would have won.
- **Mass:** no head change.
- **Noise:** base mounting on one sorbothane pad is easier to isolate than 6 loose valves.

**(d) Plausibility.** The S070 is the spec's chosen valve, and the base-mounted variant shares its 0.35–0.5 W coil and 0.1 MPa rating. The spec already sends the S070 exhaust port to the lift manifold (vacuum for park), so a common R under −8 kPa is the same duty. [VERIFY with SMC: −8 kPa on R with a de-energised valve.]

**(e) Cheapest experiment ($0, part of S0).** Put the single S0 S070C on a printed P/R block. Run it at −8 kPa on R and +13 kPa on P. Log the leak-down on the sense sensor over 10 min. If it holds, order the manifold at gate A.

**(f) Replaces.** Printed rail and lift galleries, about 24 barbs and tees, and the cheap-valve A/B.

**(g) Why it might fail.** The 12 V base-mount code may be a long-lead item: the page I reached showed only the 24 VDC part. The fallback is a 24 V coil on a $5 boost, or the M8P running at 24 V with a 24 V brick. The M5 ports need M5-to-1/8 in push-fits ($2 each). If the latency A/B at Stage A favours the cheap valves, E2 loses its cost case and keeps only about 4 h.

---

## LEAP E3 — OUTSOURCE THE PRECISION PRINTS: JLC3DP SLA bores, MJF PA12 head-borne parts

**(a) Assumption broken.** "Every part is FDM-printed at home." The fits that cost iteration are the Ø7 pin bores, the Ø20 synchro bores and pistons where a rolling sleeve must not scuff, the bell-crank pivots, and thin head-borne nodes. These are exactly where FDM ovality (0.1–0.2 mm) and layer lines cost reprints and sanding. The spec's error budget already assumes a ±2 % area match between master and slave.

**(b) Principle.**
- **Iterate on the home FDM printer until a part works once. Then freeze it and send the batch out.**
- **SLA** (8001 clear or Ledo 6060): pin cartridges ×12 (pad A + pad B), synchro cylinders ×9 (3 master + 3 slave + pad B's 3), pistons, bell cranks. Bores hold ≈ ±0.05–0.1 mm, glass-smooth, with no sanding.
- **MJF PA12:** pad deck, RCC nodes, carriage, hinge bosses and cradle nodes. Lighter and stronger than PETG at equal stiffness (RT3 §6), IPA-wipeable, and dyed black.

**(c) Numbers.**
- **Hours:** synchro 8–10 → 6–8; pins 3–4 + 4–6 → 2–3 + 3–4; pad 10–14 → 8–11. **Saves ≈ 6–9 h** of reprints, sanding, reaming and sleeve-scuff debugging.
- **Cost:** SLA from **$0.30** a part, MJF from **$1**, build 2–3 days, DHL 3–7 days [KNOWN, JLC3DP]. My estimate for this part set is **$60–110 plus ≈ $20–30 shipping** [EST, VERIFY by upload].
- **Mass:** −5 to −10 g on head-borne PA12 parts versus PETG [JUDG].
- **P:** +0.01, from better copy fidelity and fewer leak-driven synchro drifts.

**(d) Plausibility.** The parts are small, and the batch costs less than one evening of reprints. SLA resin is not on a hair-contacting surface: nails stay POM, and the pin noses are above the canopy. Cured resin is IPA-safe.

**(e) Cheapest experiment (≈ $30–40, 10 days elapsed, 1 h hands-on).** Order one SLA Ø7 cartridge, one SLA Ø20 cylinder and piston, and one MJF deck coupon. Compare them with the FDM versions on Penrose-sleeve rolling force (spring scale), leak-down and a 10⁴-cycle drill rig.

**(f) Replaces.** Home-printed precision parts after freeze. The home printer remains for fixtures and iteration.

**(g) Why it might fail.** A 10-day loop kills fast iteration if used before freeze, so the rule is "freeze first". Resin can be brittle at thin flanges, so keep walls ≥ 1.2 mm. Customs and DHL fees vary.

---

## LEAP E4 — HAND-INDEXED HALO ON BOUGHT FRICTION HINGES: powered travel leaves the critical path

**(a) Assumption broken.** "Travel must be motorised." DECISION-2 bound ear-axis travel motors, but LEAP4-BRIEF releases the halo. Under the North Star amendment the person-illusion of a hand that wanders by itself is a nice-to-have. What is required is coverage, staying where it is wanted, and no habituation. A person getting scratched also says "there… a bit left". Here Michael does the "a bit left" with one hand between bouts, while the pad is already lifted.

**(b) Principle and sketch.**

```
 side view (ear axis Y into page)                         per side, 120 mm off midline, 45 mm above canal
        bail (bent Al 10×1, R 210)                         ┌───────────────┐
            ╲                                              │ Southco E6-type│ acetal, adjustable, ≈ 0.25 N·m
             ╲   friction carriage: O-ring on tube +       │ friction hinge │ (or Al E6-10-208, 0.90 N·m, ≈ 23 g)
              ●  printed detent every 10° of β              └──────┬────────┘
             ╱   (hand slides it; holds ≥ 3 N)                    │ leaf screwed to the PA12 hub boss on the cradle
  hub ◉─────╱    α holds by friction at any angle                 │ no motor, no drum, no balancer, no capstan
             ── dial cradle under the occiput ──
 Stops: printed α −25°/+100°, β ±40° (RT2 must-fix, now mechanical only). Twin: the right hub boss takes a 2nd hinge (split bail).
```

- **Holding torque needed:** worst gravity moment 0.24 N·m + typical scrub reaction 0.11 N·m = 0.35 N·m. Two hinges at 0.25 N·m give 0.50 N·m, a margin of 1.4. Two at 0.9 N·m give 1.8 N·m, a margin of 5. An overload above the hinge torque simply swings the bail: it is back-drivable by construction (red line 7 satisfied, and it adds a breakaway).
- **The motion rule (H-5.8):** the pad is only moved after the hold-to-run lever is released, and release vents every pin and lifts the pad. The firmware's dwell ledger (H-5.5) stops biting after the patch budget and chimes "move me". The MOVED button re-arms it.

**(c) Numbers.**
- **Hours:** removes hub pods, the GT2 3:1, servo bays, β tendon, the servo zero jig, gear bias, the bone-path and servo-noise gates and their rework: **≈ 40–50 h** out of C. Adds ≈ 4–6 h over the static halo for hinges, friction carriage and stops. **Net ≈ −35–45 h. This is the single biggest lever.**
- **Cost:** removes 3 × STS3032 ($120 at ≈ $40), bus board ($6), GT2 3:1 kits ($15), 6800-2RS and shaft ($14), Dyneema and balancer springs (≈ $14), 6 V servo buck (≈ $5). Adds 2–4 hinges at **$10–23** each [KNOWN, Amazon Southco listings]. **Net ≈ −$130.** The pad-B servo leaves pad B's parts list, because the twin is hand-indexed too.
- **Mass, single:** removes 2 servos (41 g), pod internals (≈ 20 g), tendon and idlers (6 g) and servo harness (≈ 3 g). Adds hinges (2 × 5–23 g) and a carriage lock (3 g). **≈ −40 to −60 g → single ≈ 330–345 g.**
- **Mass, twin:** also removes α_R (21 g) and the crossed tendon (4 g). **≈ 415–430 g against the 500 g line: about 70 g of margin instead of 20.** This also removes the need for RT2's light lines as a twin must-fix.
- **P(on-par):** G5 (stays where wanted, coverage) 0.85 → 0.78. G4 (no habituation) loses the automatic drift, 0.80 → 0.77. G3 (no intrusion) **gains**, 0.80 → 0.84, because the servo hunt or buzz into the parietal bone (RT1 #6, a MUST) and the "does the hat move" lean disappear. **Net ≈ −0.02 to −0.04** [JUDG].
- **Safety:** red line 4 now applies only to the box. Nothing on the head is powered.

**(d) Plausibility.** RT3 and the decision analysis already run Stage B on a static, manually indexed halo. E4 makes that the SP1 deliverable, with continuous instead of detented α, and moves powered travel to an optional SP1.5. The right hub boss keeps the second-hinge provision, so the twin addition needs no redesign (decision 4).

**(e) Cheapest experiment (≈ $25 plus the $20 Day-0 bike helmet).** Screw one E6-type hinge to each side of the coin-test helmet. Fit a bent-Al bail stub carrying the coin bag at r = 105 mm (≈ 0.35 N·m). **Pass:**
- it holds at α = 0, 45° and 90° for 20 minutes of TV;
- Michael can re-index it eyes-closed in under 3 s;
- after the Stage B fixed-pose sessions, he rates "having to move it" ≤ 3/10 as intrusion.

**(f) Replaces.** Hub pods, both travel servos (and pad B's), capstan or GT2 reduction, β tendon and drum, spring balancers, the servo bus and its firmware, the servo noise and bone-path gates, and the β ±36° firmware fence (now mechanical stops).

**(g) Why it might fail.** He may simply want it to wander by itself. "Lie back and be scratched" may be the core of on-par satisfaction, which would make G5 worse than I assume. Moving the pad uses the e-stop hand, so the e-stop puck must sit under the lever hand's thumb, and the armrest switch from RT1 #10 becomes more important. The hinge torque drifts with wear, so the adjustable acetal type is preferred. **If the E4 test or the Stage B sessions say "motor it", the pods come back as SP1.5.** E1 makes that cheaper: STS servos are driven from `score.py` over a $4.99 Waveshare adapter, with no firmware. The pods would cost ≈ 25–30 h then, not 40–50.

---

## LEAP E5 (minor) — HARVEST A CoreXY PEN-PLOTTER KIT AS THE XY MASTER

A5 CoreXY plotter kits (Doesbot / IKRANBIRD AX5: 2 × NEMA 17, CoreXY belts, Ø6 rods + linear bearings, 210 × 148 mm stroke [KNOWN]) can be cut to ±25 mm (≈ 160 × 160 mm footprint, fits the Apache 2800) and run as `kinematics: corexy` on E1's board, the master plate bolted to the pen carriage. It saves ≈ 2–3 h of XY design and belt fiddling for ≈ +$40–70 [EST; kit price VERIFY]; Ø6 rods over 50 mm carry 5 N trivially. Test: shortened kit, PLINE at 2 Hz, ink-trace bow ≤ 0.3 mm. It may fail because cutting, squaring and re-tensioning eat the saving: **a coin-flip, used only if the MGN12 stage stalls.**

---

## Harvests I checked and rejected

| Idea | Finding | Verdict |
|---|---|---|
| Bellofram diaphragm cylinders for the synchro (no sleeves, no leak) | Spring-return only; 0.384 in² area (≈ Ø18 effective) and 0.7–1.75 in stroke fit, but $99 used to $343 new each, ×9 including pad B [KNOWN] | Too costly (+$900–3,000). Keep as the fallback if finger-cot sleeves fail the 10⁴-cycle gate. |
| Airpel anti-stiction cylinders as the pins (no sleeve, no hover-collar friction) | E9 (Ø9.3) weighs 31.7 + 0.375 × stroke g ≈ **41 g each** [KNOWN] | Kills the head mass (6 × 41 g). Reject for pins; keep Airpel only for the float (RT3). |
| Programmable-Air kit as the S0/A pneumatics | 2 pumps, 3 valves, sensor, Nano, ±50 kPa, **$150–200** [KNOWN] | Saves ≈ 2–3 h of S0 plumbing; its valves are not the S070 class. Optional luxury, not in the cart. |
| SMC 6-station base manifold | $80.90 [KNOWN] | **Adopted (E2).** |
| Air-compression leg massager control unit (pump + valves) | 1 pump + 2 valves, cycles in seconds [KNOWN] | Too few, too slow. Use BP or massage-chair NO valves as dumps only. |
| VR halo straps, welding-helmet headgear as the halo with ear pivots | Bought ear-axis pivot and dial, but 120–250 g against 56 g for cradle + band + temple pads [JUDG] | Breaks the twin mass. The bike dial (RT3) stays. |
| Electric scalp massagers, hair-washing robots | Rotating silicone nubs: massage, not scratch (scratch-model §1.2) | No harvestable sub-assembly worth its mass. |
| Bought motorised XY stages (FUYU FPB30 class) | ≈ $225 per axis [KNOWN] | +$380 for ≈ 3 h saved. Reject. |
| Fully custom JLCPCB PCBA controller | $8 setup, $3 per extended part, ≈ 2 weeks [KNOWN]; a one-spin error risk | E1's stock board beats it. A small PCBA "valve + comparator + sensor" daughterboard is worth it **only after** gate B freezes the I/O (−≈ 3 h, +$40). |

---

## Revised build plan (best bet = E1 + E2 + E3 + E4; E5 only on a stall)

Same sensation-first staging and gates as RT3 §8 and the decision analysis §4.3. Only the content changes.

| Stage | Build (what changed) | Hours [JUDG] | Baseline | Sensation data point |
|---|---|---|---|---|
| **S0, week 1** | One-nail rig (S070C on a printed P/R block: E2 test). Coin-helmet evening **with friction hinges** (E4 test). Earplug servo test **dropped**. Klipper LED-sync test on a $5 Pico (E1 test). | **7–9** | 8–10 | Omni-nail ≥ 6/8 headings nail-like |
| **A, bench puppet, 3 weekends** | M8P + CB1 + Klipper; hardware safety loop + snag comparator; rail and palm with reliefs; SMC manifold (if S0 passes); MGN12 XY (or E5); 3 synchro lines on SLA cylinders; 6 SLA pins on the bench; sleeve-life rig. `score.py` v1: PLINE, LINE, CIRCLE, windows, jitter. | **26–36** | 45–60 | Hand-held 6-pin pad on the crown ≥ 6/10 |
| **B, pad + hand-indexed halo, 3–4 weekends** | Pad (RCC, skids, Airpel float, QEV, filters, mufflers) on MJF parts; **bail bent + friction hinges + friction carriage + stops** (this *is* the SP1 halo); Apache box; wig, force, proof, fail-to-free gates; dwell ledger with chime and MOVED button. | **36–48** | 40–55 | **The hypothesis:** 5 → 10 → 20 min, "as good as a good scratch" ≥ 7/10 |
| **C′, finish, 1–2 weekends** | Umbilical with ear-axis exit, hanger, pogo breakaway, head-present switch; doff and mass gates (no servo gates). | **11–15** | 50–65 | "Does the hat move?" |
| **D, sessions** | Armrest switch, buttons, 20 min sessions; deferred layers as A/B. | **10–18** | 10–20 | Spec D1–D5 |
| Must-fix spread | Fewer: gear bias, β firmware fence, servo noise and bone path are gone | **8–14** | (inside) | — |
| **Total** | | **≈ 98–140 h** (central ≈ 118) | 165–230 (central ≈ 197) | |

**Hours saved by leap** [JUDG]: E4 ≈ 35–45 · E1 ≈ 18–27 · E2 ≈ 6–8 · E3 ≈ 6–9 · overlap and must-fix shrink ≈ 5–8. Total ≈ **70–90 h, or −40 % central.**

The provocation's "halve it" is reached only at the optimistic end. Honestly it is **−40 %**. Without E4, keeping motors but using E1 to run the servos, the plan is **≈ 125–175 h (−23 %)**. E4 is the leap that makes this a step change. E1 is the one that de-risks it.

---

## Day-0 cart (deltas against the baseline Day-0; S0 + Stage A long-lead)

| Vendor | Item | Qty | Price | Why Day 0 |
|---|---|---|---|---|
| BIQU / Amazon | **BTT Manta M8P V2.0 + CB1 bundle** | 1 | **$154.59** | E1; replaces the ESP32 carrier order |
| BIQU / Amazon | BTT TMC2209 | 3 (1 spare) | **$7.89** each = $23.67 | E1 |
| Adafruit / Amazon | Raspberry Pi Pico (S0 Klipper sync test) | 1 | ≈ $5 | E1 test |
| Amazon | ADS1115 module; LM393 comparator modules (pack) | 1 + 1 pack | ≈ $6 + $6 [est] | vac/egg ADC; hardware snag reflex |
| Automation Distribution | **SMC S070C-6DC-32** (S0 valve; RT3 part) | 1 | **$35.00** | S0 rig and the E2 R-port vacuum test |
| smcpneumatics / SMC distributor | SS0755-class 6-station base + S070A 12 V × 6 | — | **$80.90** + 6 × $35 | **Gate A, not Day 0.** Ask SMC now for the 12 V code and lead time. |
| Amazon | **Southco E6-10-101-20** adjustable acetal hinge (or E6-10-208-50, 0.90 N·m) | 2 (+2 for pad B: binding) | **$10–23** each [VERIFY each listing] | E4 test on the coin helmet; pad-B hinges are pad-B parts |
| Amazon | Aquarium check valves (10-pack); BP-monitor 12 V NO mini valves (5) | 1 + 1 | ≈ $6 + ≈ $15 [est] | duckbills and dumps |
| JLC3DP | SLA trial: Ø7 cartridge, Ø20 cylinder + piston; MJF deck coupon | 1 lot | ≈ $10–20 + DHL ≈ $15–20 [VERIFY by upload] | E3 test; 10-day lead, so start now |
| StepperOnline | 17HS08-1004S (RT3) | 2 | $7.99 each | XY master and the E1 test |
| AliExpress / LCSC | XGZP6847A (0–40 kPa, −40–0, 0–100) | 8 (5 + 3 pad B) | ≈ $5 each delivered | 2–4 week lead (RT3) |
| Unchanged from RT3 | McMaster 4277T51 reliefs, Penrose 1/4 in, 27G/30G needles, Kamoer KVP04, rail pump, PU 1/8 in, push-fits, UltAlt dial + $20 helmet, e-stop, 12 V 5 A brick, PETG/TPU | — | ≈ $260 | — |
| **Removed** | 3 × STS3032 (≈ $120), XIAO bus board ($6), GT2 3:1 kits, 6800-2RS, Dyneema/balancer springs, the ESP32/MCP3208/TPIC/JLC carrier order | — | **−$175 to −$185** | E4, E1 |

**Day-0 cash ≈ $560–620**, against RT3's ≈ $700 Day-0 (the decision analysis's leaner S0 cart was ≈ $350). Gate-A cart: manifold + 6 S070A ≈ $290, then pad parts and the JLC3DP production batch ≈ $120 at freeze.

---

## Best bet

**E4 + E1, with E2 and E3 as cheap multipliers.** The box becomes a stock Klipper printer controller that streams a scratch "score" as G-code with synced valve windows. The head carries no motor at all: Michael flips the bail on two bought friction hinges between bouts, while the pins are already lifted.

**The case.**
1. The two largest hour sinks were custom real-time firmware and powered travel. They are also the two least connected to a *scratch*. One is plumbing for the person-illusion the North Star dropped. The other is a job a mature open-source stack already does.
2. E4 also pays in mass: the twin moves from 480 g to ≈ 420 g, so 6 pins stop being a hard ceiling. It also deletes an RT1 MUST (servo buzz into the parietal bone) and a set of C-gates.
3. E1 turns the riskiest amateur skill (bring-up of a 1 kHz scheduler on an ESP32) into configuration. It also gives a free stroke-length and velocity profile that the crank never had.
4. Nothing binding is broken:
   - helmet ✓;
   - PLINE, LINE and CIRCLE ✓ (as G-code);
   - portable box ✓ (standalone, with the CB1 inside);
   - one pad built + pad B's parts bought ✓ (pad-B hinges and parts in the cart);
   - all red lines ✓. The hardware loop is unchanged, and the snag reflex becomes hardware.
5. Nothing is outsourced as labour.

**Revised estimate if adopted** (E1 + E2 + E3 + E4):

| | Baseline (6-pin hybrid) | **Best bet** |
|---|---|---|
| Hands-on hours | 165–230 | **≈ 98–140 (central ≈ 118, −40 %)** |
| Parts cost | ≈ $1,450–1,500 + $185 tools | **≈ $1,530–1,620 + $185 tools.** That is +$75–95 for E1, +$70 for E2, +$80–140 for E3 and −$130 for E4. About **+$100 for ≈ 80 h saved**, or **+$270 if the cheap valves would have won the A/B**. |
| Head mass, single / twin | 386 (370 light) / 480 g | **≈ 330–345 / ≈ 415–430 g** |
| P(full session ≥ 7/10 on-par), conditional [JUDG] | 0.40 | **≈ 0.38 (0.28–0.48).** E4 costs about 0.03; E1 and E3 give back about 0.01–0.02. |
| P(reach the session within 26 weekends) [JUDG] | ≈ 0.50 | **≈ 0.70** (11–13 weekends of work, and fewer stall skills) |
| P(≥ 7/10 within 26 weekends) | ≈ 0.20 | **≈ 0.27** |

**Kill switch.** If the Stage B sessions score ≥ 7/10 but Michael says "I want it to wander on its own", build SP1.5 powered travel on E1. That means STS servos on the existing hub bosses, driven from Python over a $4.99 adapter, ≈ 25–30 h. The bet then costs nothing but a delay, and the twin keeps its 70 g margin until then.

---

### Sources (checked 2026-10-02)
- Klipper `output_pin.py` (SET_PIN queued via `register_lookahead_callback`), `mcu.py` (`MIN_SCHEDULE_TIME = 0.100`), `pwm_tool.py`, Config Reference (`[pwm_tool]` "high speed updates", `maximum_mcu_duration`, `[adc_temperature]`, `[heater_generic]`, `[ads1x1x]`, `[gcode_button]`): [github.com/Klipper3d/klipper](https://github.com/Klipper3d/klipper/blob/master/klippy/extras/output_pin.py), [Config Reference](https://www.klipper3d.org/Config_Reference.html)
- BTT Manta M8P V2.0 (4 HE + HB + 7 PWM fan outputs, CB1/CM4 BTB): [BTT wiki](https://global.bttwiki.com/M8P-V2_0.html), [BIQU Manta](https://biqu.equipment/products/manta-m4p-m8p), [BIQU kit $154.59](https://biqu.equipment/products/bigtreetech-stealthy-hi-speed-solution), [Amazon B0FVVXY7P4](https://www.amazon.com/BTT-Manta-M8P-V2-0-Motherboard/dp/B0FVVXY7P4); TMC2209 $7.89: [BIQU](https://biqu.equipment/products/btt-tmc2209-stepper-driver)
- Waveshare Bus Servo Adapter (A), $4.99: [waveshare.com](https://www.waveshare.com/bus-servo-adapter-a.htm)
- SMC SS0755-05M5C 6-station S070 manifold $80.90: [smcpneumatics.com](https://www.smcpneumatics.com/SS0755-05M5C.html); S070A-5AC $35, base mounted: [Automation Distribution](https://automationdistribution.com/s070a-5ac/); S070C-6DC-32 $35 (RT3)
- JLC3DP SLA from $0.30 (2 days), MJF from $1 (3 days), DHL 3–7 days: [jlc3dp.com](https://jlc3dp.com/), [SLA](https://jlc3dp.com/3d-printing/stereolithography), [MJF](https://jlc3dp.com/3d-printing/multi-jet-fusion); JLCPCB PCBA fees: [JLCPCB](https://jlcpcb.com/help/article/pcb-assembly-price)
- Southco E6 constant/adjustable-torque hinges (E6-10-101-20 acetal 2.19 in·lbf; E6-10-208-50 0.903 N·m, 0.8 oz; E6-10-212F-50 $22.87): [Amazon E6-10-101-20](https://www.amazon.com/Southco-Adjustable-Position-Copolymer-Symmetric/dp/B00FRLZKFW), [Amazon E6-10-208-50](https://www.amazon.com/Southco-Constant-Position-Aluminum-Symmetric/dp/B00GM5G42A), [Southco E6](https://southco.com/en_us_int/hinges/positioning-hinges/e6-adjustable-torque-position-control-hinges)
- Bellofram small-bore diaphragm cylinders (0.384 in², 0.7–1.75 in, spring return): [Rustco](https://shop.rustco.com/Product/s/dQg2eZ/Small-Bore-Diaphragm-Air-Cylinder); 900-006-000 $342.71: [ACI Controls](https://www.aci-controls.com/itemdetail/900-006-000); used $98.99: [eBay](https://www.ebay.com/itm/313360699344)
- Airpel E9 mass formula and prices: [Airpel catalogue](https://www.airoil.com/uploads/assets/downloads/AirpelCat10-06.pdf), [eBay E9-D-1.0-S](https://www.ebay.com/itm/325545939010), [Airpot FAQ](https://www.airpot.com/faqs/)
- Programmable-Air ($150–200, 2 pumps, 3 valves, ±50 kPa): [programmableair.com](https://programmableair.com/products/programmable-air-deluxe-kit), [SparkFun](https://www.sparkfun.com/crowd-supply-programmable-air-starter-kit.html)
- AX5 CoreXY plotter kits (210 × 148 mm, NEMA 17, Ø6 rods): [Doesbot AX5](https://www.amazon.com/Doesbot-AX5-Plotter-Programming-Assemble/dp/B0D1GK9TV8), [IKRANBIRD AX5](https://www.amazon.com/IKRANBIRD-Plotter-Baseplate-Programming-Assemble/dp/B0F9WNKLBJ); FUYU FPB30 ≈ $225/axis: [Oyostepper](https://www.oyostepper.com/goods-1402-FPB30-Linear-Guide-Belt-Drive-Linear-Module-Linear-Stage-with-Nema-17-Stepper-Motor-CNC.html)
- Leg-massager internals (1 pump + 2 valves): [device.report manual](https://device.report/manuals/air-compression-pneumatic-full-leg-massager-user-guide); massage-chair 12 V mini valves (185 mA, 2/3-way): [micro-airpumps](https://www.micro-airpumps.com/sale-36763701-micro-mini-electric-solenoid-valve-12v-dc-normally-open-close-for-massager-armchair.html)
