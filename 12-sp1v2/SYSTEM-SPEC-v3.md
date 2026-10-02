# SP1 "PUPPET HALO, LEAN" — SYSTEM SPECIFICATION (Design Freeze v3)

**Project SCRATCH · 12-sp1v2 · System Architect · 2026-10-02**
**Binds to:** 12-sp1v2/DECISION-3.md (binding), DECISION-2.md including the NORTH STAR AMENDMENT, 12-sp1v2/safety-ruling-dish-gate.md (conditions C1–C8 are requirements), 12-sp1v2/decision-analysis.md (must-fix list; 6 pins, centre + pentagon R 18), 01-foundations/safety-requirements.md (13 red lines), hair-interaction.md (H-rules), tip-interface.md (edge R ≥ 0.4 mm).
**Builds on:** 11-leaps/round-4: leap4-A §4 (dish gate, variant L3-2), leap4-D L1 (three-drum tendon puppet), leap4-E E1 (Klipper box), E3 (outsourced prints), E4 (hand-moved halo), leap4-F L4 (stations, detents), leap4-C C3 (feather chassis). The three v2 red teams (redteam-1/2/3) for everything still open.
**Supersedes:** SYSTEM-SPEC.md (freeze v2). v2 stays in the repo as reference. Where this file and any leap, red-team or v2 text disagree, **this file governs**.
**Director ruling folded in (2026-10-02):** the three-drum tendon puppet *is* the path synthesiser. There is **no separate XY belt stage**. DECISION-3 item 2 ("XY belt master") is satisfied by the drums: the path is computed in firmware and written to three cable lengths.

**Tags.** **[KNOWN]** = sourced in a project file or a vendor or documentation page cited here. **[EST]** = computed here or carried from a leap estimate (scripts in 12-sp1v2/scripts/, including the new `mass_v3.py`). **[JUDG]** = a judgement figure. **[VERIFY]** = an open item that a named bench test or vendor check must close before the dependent part is ordered, printed or trusted. Every [VERIFY] is collected in §12.2.

---

## 0. SP1 v3 in one page

SP1 v3 is a **motor-free, wire-light skeleton helmet** carrying **one pad of six air-pressure nails** (centre + pentagon at R 18 mm). The nail block rides a **printed dish** under the pad deck that is concentric with the scalp: in the middle of the stroke every nail stays within 1–3 mm of its skin distance, so one open air line gives every nail the same constant force on both flanks; near the end of every stroke the dish **rim lifts every nail 5–7 mm clear by geometry**. The six nails sit on **two pin lines** (groups A and B). The block's motion is made in the drive box by **three stepper-driven drums** and copied to the pad by **three tendons** in coil housings (the "puppet"); the path is pure firmware, so the precessing line, straight line, circle, off-centre chords and one-way D-paths are all just paths. The halo is **moved by hand** between bouts on friction hinges with detents. The box runs **Klipper** on a stock printer controller; a **hardware safety loop** that firmware cannot override cuts every actuator. Each nail is held to its piston by a **0.12–0.25 N magnetic breakaway**, so no fault, reflex, retract or doff can pull a caught strand harder than that. Any stop, power loss or released lever **vents the pins and lifts the pad by spring**.

| Quantity | Frozen value | Tag |
|---|---|---|
| Pins | **6**: centre + pentagon at R 18 mm; two groups: **A** = pentagon P0, P2, P3; **B** = centre C, P1, P4 | KNOWN (decision-analysis) / choice §1 |
| Pin bore / force | Ø 7.0 mm Penrose-sleeve piston (38.5 mm²): **0.0385 N/kPa**; operating rail 2–13 kPa = **0.08–0.50 N** per nail; firmware ceiling 0.60 N | EST |
| Per-nail cap (mechanical) | R1a 20.7 kPa (3 psi fixed) = **0.80 N**; R1b (different make) 24 kPa = 0.92 N; rail pump deadhead ≤ 50 kPa = 1.93 N (red line 2: ≤ 2.5 N) | EST [VERIFY A1] |
| Nail | one-piece drafted POM cone (90°, Ø 2 flat, rim R 0.4) on a rigid Ø 1.0 A228 shaft; profile **never narrows tip → nose** (C2); shaft held to the piston by a **Ø 3 × 2 magnet, axial release 0.12–0.25 N** (C1) | KNOWN (ruling) |
| Pin stroke / reserve | **18.5 mm** stroke, ≥ 15 mm retract margin above contact (C6); reserve below contact 1–3.5 mm | KNOWN (ruling C6) |
| Dish | centre sphere **R 160 mm** (|d| ≤ 7 mm); inner rim **34°** (landing band, C5) to |d| 13.7 mm (+4.5 mm); outer rim **50°** to |d| 17.0 mm (+8.5 mm) | EST (choice §1) |
| Scrub | default **PLINE** 1.4 Hz, ±16 mm, heading precession 4.5° per cycle with jitter; LINE; CIRCLE (offset, lifts once per revolution); **off-centre chords** (contact 5–23 mm); **one-way D-paths**; max 2.0 Hz | binding + EST |
| Puppet | **3 tendons**: 0.45 mm coated 7×7 stainless in PTFE-lined coil housing, **1.6 m**; Ø 12 drums on 3 NEMA 17 pancake steppers; 2 N/mm series springs; **1.9 N/mm** at the block; **2.0 N magnetic shear coupling** (tangential cap; never set above 2.5 N) | EST (leap4-D) |
| Travel | **by hand**, pins vented and pad retracted: α (bail pitch) on two friction hinges with a 15° detent click, β (latitude) on a friction carriage with 10° detents; mechanical stops α −25°/+100° (set to Michael's hairline), β ±40° | EST |
| Head-borne mass | **≈ 286 g single** (≈ 260–320 g); **≈ 440 g twin** when pad 2 is added later (limit 500) | EST (`mass_v3.py`) |
| Worst lean (single) | **0.27 N·m** at the bun pose; cradle form lock 1–1.5 N·m | EST |
| Powered parts on the head | **none** (a head-present switch and the loop wire only) | — |
| Drive box | Harbor Freight Apache 2800 case, **343 × 289 × 152 mm outside**, **≈ 2.6–2.8 kg** loaded; desk, chair back or couch back | KNOWN (case) / EST |
| Umbilical | **1.6 m: 3 PU 1/8 in tubes (PIN A, PIN B, PALM) + 3 tendon housings + one 4-core 26 AWG cable**, loose in a knit sleeve, Ø ≈ 11 mm; exits along the ear axis through the right hub; magnetic pogo lanyard is the shortest member | EST |
| Power | **24 V 60 W certified adapter**; 24 V switched actuator rail; 12 V buck after the loop for valves and pumps; ≈ 30 W typical, ≈ 50 W peak; no mains in the box, no lithium | EST |
| Controller | **BTT Manta M8P V2.0 + CB1, Klipper**; drums as three coordinated G-code axes (A, B, C) with host-side inverse kinematics; hardware safety loop independent of it | §1, §8 |
| Controls | hold-to-run lever (armrest switch by Stage D), NC e-stop puck, SPEED and INTENSITY knobs, MODE selector, MOVED button; PC over the network for experiments | DECISION-3 #9 + §1 C27 |
| Hands-on hours | **≈ 115–175 h** (central ≈ 140), including the 1.5× first-timer factor | EST/JUDG |
| Parts cost | **≈ $1,360** (≈ $1,250–1,420) for one pad, pad-2 parts *not* bought; plus ≈ $185 tools (+ printer if none) | EST, live prices where checked |
| P(full session rated ≥ 7/10 "as satisfying as a good scratch") | **≈ 0.42** (0.32–0.52), conditional on reaching a full session | JUDG |
| P(≥ 7/10 within 26 weekends) | **≈ 0.27** (P(reach) ≈ 0.65 × 0.42) | JUDG |

### 0.1 What changed from v2

| Deleted (DECISION-3) | Replaced by | Kept from v2 (still valid) |
|---|---|---|
| 12 per-pin S070 valves, sense orifices, per-pin sensors, restrictors, duckbills, bleeds, hover collars, gate scheduler | **dish gate**: two open pin lines, geometry does the lift | halo geometry (dial cradle, front band, ear-axis bail R 210), coordinate frames H/B/C/P/S, head model |
| vacuum pump, accumulator, breaker, LIFT SELECT, park | rim park (pins vented on the rim) | rail and palm relief caps as mechanical constants (re-set values) |
| sealed air synchro (6 cylinders, bell cranks, charge, reliefs, dumps, breakers, re-zero) | **three-drum tendon puppet** with magnetic tangential fuse | fail-to-free float with spring retract (now Airpel + QEV + float relief) |
| XY belt stage / crank synthesiser | **the drums are the master** | umbilical breakaway chain (3 N clip, lanyard first, cradle last) |
| travel servos, hub pods, capstans, balancers, β tendon | **hand-moved halo** on friction hinges and detents | hardware safety loop (NC e-stop, hold-to-run, watchdog), red-line mapping |
| squeeze egg, PS1 hard-squeeze switch | knobs, MODE selector, MOVED button | firmware state machine (re-hosted on Klipper + host) |
| head scan, registration, κ-grammar, fatigue/attention ledger | **simple variation generator** + dwell timer per station | RCC palm, 3 dome skids |
| ESP32-S3 firmware, MCP3208/TPIC6B595 board | **Klipper on M8P V2 + CB1** | twin point-mirror concept (pad 2 later) |
| 20-port helmet plug (RT3/RT2) | continuous lines + lanyard loop-wire breakaway | |
| second-pad parts purchase | **provisions only** (DECISION-3 #8) | |
| Al hand-bent bail (RT3) | **carbon polygon bail on printed nodes** (C3) | |

---

## 1. Open choices resolved

Each row closes a choice that the binding inputs, leap documents or red teams left open. "Why" is the deciding reason.

| # | Choice | Decision | Why |
|---|---|---|---|
| C1 | Pin layout and grouping | **Centre + pentagon R 18; group A = P0, P2, P3 (a triangle spanning the field), group B = C, P1, P4 (a chevron through the centre)** | Decision-analysis fixed 6 pins at centre + pentagon. L3-2 needs two fixed galleries. A triangle and a centre chevron each give 2.5–3 distinct tracks over most headings [EST, CAD WP re-runs `pins.py` on these groups]; all-six gives the two-rank rake. |
| C2 | Pin actuator | **Latex Penrose 1/4 in sleeve inverted over a POM piston in a Ø 7.0 bore** (RT3 2.2); SLA cartridge body (E3) | Bought, replaceable in 2 minutes. On the dish a pin moves only 1–3 mm per stroke, so sleeve flex cycles fall by ≈ 5–10× against v2 [EST]. |
| C3 | Nail attachment | **Magnetic axial breakaway** (C1): Ø 3 × 2 N52 in the piston face, A228 shaft end flat-faced, laterally located only by the two guides; release 0.12–0.25 N | The ruling's primary control. It replaces RT2's 12 mm reserve. |
| C4 | Nail | **One-piece: POM cone mechanically hooked and epoxy-filled on the Ø 1.0 shaft**, cone 90° tip from a Ø 2 flat (R 0.4) to Ø 4.5, then a 2.5° per-face draft to the nose; red or orange POM; shaft top domed R 0.5 | C2 profile rule; red line 9 retention (cone-to-shaft proof 3.1 N tension) and red line 11. |
| C5 | Pin stroke | **18.5 mm** (contact at 15.0 + reserve 1–3.5) | C6: ≥ 15 mm retract margin so a 10° pad tilt or a finger cannot bottom a nail. |
| C6 | Dish profile | **Sphere R 160 to |d| = 7; 34° to |d| = 13.7 (+4.5 mm); 50° to |d| = 17.0 (+8.5 mm)** | C5 requires a landing band ≤ 35° (print 33–35°). The outer rim is softened from leap4-A's 65° to 50° so the horizontal rim reaction on pins-up travel drops from ≈ 1.3 to ≈ 0.7 N [EST], keeping total rim load under the 2.0 N tangential coupling. Cost: 2.3 mm more amplitude, free with drums. |
| C7 | Block support on the dish | **3 POM domes on the block, PTFE tape on the dish, 0.5–0.6 N deck-to-block lift tension spring** | As leap4-A. The ruling's A2 (12 mm free travel) is **not built** (C1 makes it unnecessary). |
| C8 | Pin line topology | **Two lines (A, B), one S070C-6DC-32 each** (NC to rail, vent when de-energised); **line B force servo = PWM of its own S070 with a Ø 0.3 inlet needle and a line-B sensor**, downstream of R1a/R1b | C3 vent rule; one valve type in the box; B ≠ A force contrast for anti-habituation. |
| C9 | Accumulator | **250 ml PET bottle on the rail side of both PIN valves** | C3: downstream it would take ≈ 1 s to vent; upstream only ≈ 8 ml must leave. |
| C10 | Reliefs | **R1a = McMaster 4277T51 3 psi (20.7 kPa); R1b = a different make at ≈ 24 kPa; R2 (palm) 3 psi; R2b different make ≈ 24 kPa; rail pump deadhead ≤ 50 kPa, palm pump ≤ 30 kPa** | RT2 #8: diverse "b" reliefs and a measured third barrier. Bought fixed reliefs remove printed-poppet calibration (RT3 2.4). |
| C11 | Total-force cap | **Palm float** (pins react against the pad, the float holds the pad) | v2 logic, unchanged; red line 3 rests on R2/R2b + deadhead, independent of pins. |
| C12 | Float | **Airpot Airpel E16D2.0N** (≈ Ø 16, 2 in stroke) **+ quick-exhaust valve at the float + a relief poppet at the float**; retract spring 1.2 N preload | RT3 2.3 (its clearance leak is a bleed); RT2 #7 (QEV gives 60–90 ms retract; float relief bounds a kinked-and-compressed line). [VERIFY bore and mass] |
| C13 | Puppet medium | **Tendons** (three tension-only cables at 120°), not air | DECISION-3 #3. No seals, charge, re-zero or leak hunt; path in firmware. |
| C14 | Master | **Three Ø 12 mm drums on three NEMA 17 pancake steppers (17HS08-1004S class)**; no XY stage | Director ruling: the drums are the path synthesiser. 0.8 turn per 30 mm; 12 µm per 1/16 microstep. |
| C15 | Tangential cap | **Magnetic shear coupling between tendon yoke and block, 2.0 N** (raise to 2.5 N only if the A-stage 20-minute nuisance test fails; never above) + stepper current capped by **VREF** (hardware) at ≤ 5 N per cable | Two-sided mechanical cap, as the v2 must-fix (2.5 N) required; RT2 #3. |
| C16 | Copy filtering | **2 N/mm series spring in each tendon at the pad** | leap4-D §1.2: keeps box ripple within +6 dB of the air puppet. |
| C17 | Common-mode | **Floating housing-stop plate at the box with a 6 N spring**; Hall flexure on each housing stop (≈ 20 N/mm) gives each cable's tension | Absorbs equal length changes from hand-moved bail and head turns; tensions give the drag vector and snag signal. |
| C18 | Kinematics on Klipper | **Host-side inverse kinematics streamed as three coordinated G-code axes A/B/C** (`MANUAL_STEPPER … GCODE_AXIS=`) with `kinematics: none`. Fallback 1: stock `winch` kinematics. Fallback 2: a custom `tendon3` kinematics module. | Klipper's winch kinematics is documented as "CABLE WINCH SUPPORT IS EXPERIMENTAL. Homing is not implemented" and has no per-cable backlash compensation; it also assumes a fixed-z point toolhead while our block rises 8.5 mm and tilts 5.5° on the rim. Host IK handles the dish z/tilt, dead-band compensation and spring feed-forward exactly (§8.2). |
| C19 | Controller | **BTT Manta M8P V2.0 + CB1** | DECISION-3 #6; leap4-E E1. |
| C20 | Stepper drivers | **TMC2209 in standalone step/dir mode, current set by VREF** (no UART) | VREF is a hardware current cap (RT2 must-fix). Without UART, cutting motor power at every lever release does not trip Klipper's driver-reset shutdown (§8.1). |
| C21 | Supply | **24 V certified 60 W adapter** (Mean Well GST60A24 class) | The M8P's selectable driver supply takes 24 V on a separate motor input, so the safety loop can cut motor power while logic stays up. 24 V meets red line 5 (≤ 24 V). [VERIFY M8P motor-power input wiring] |
| C22 | Snag reflex | **Hardware latch in the safety loop** (comparator on cable tensions, plus a host GPIO from the dish-aware firmware criterion) that **opens the actuator rail** = full fail-to-free | Klipper's motion queue runs up to ≈ 2 s ahead, so a queued "hold and retract 10 mm" cannot be fast. Cutting the rail vents the pins (≤ 100 ms), stops the drums (they cannot reverse unpowered) and retracts the float fully. C1 bounds any pull at ≤ 0.25 N, so a full retract is safe (ruling S5). Deviation from C4's 10 mm wording recorded in §7.3. |
| C23 | Halo travel | **By hand** (DECISION-3 #4): α on two Southco E6-10-101-20 acetal adjustable friction hinges + a spring-ball detent every 15°; β on a friction carriage with detents every 10° | leap4-E E4 + leap4-F L4. No motor, drum or balancer on the head. |
| C24 | Bail | **Carbon polygon**: six 8 × 6 mm chords (20.7°, 75 mm) + two legs, bonded into seven printed nodes; 3 × 1 mm pultruded carbon track strip on the node crowns; vertex node = pad-2 splice | leap4-C C3: −22 g against Al and no bending. |
| C25 | Front band | **20 × 1 mm pultruded carbon strip**, elastically bent; doff lip moulded into its centre node | leap4-C C3. |
| C26 | Umbilical exit | **Along the ear axis through a hollow right hub boss**; clip beside the head; free loop ≥ 450 mm | RT2 #2: the only line the bail never sweeps; a hand-moved bail does not change the housing lengths. |
| C27 | User controls | Hold-to-run lever + NC e-stop + **SPEED** and **INTENSITY** knobs (DECISION-3 #9) **+ a 4-position MODE selector (PLINE / LINE / CIRCLE / MIX) + a MOVED button** | Michael bound "modes switchable at any moment"; MOVED re-arms the station dwell timer (H-5.5). $6 of parts. **Flagged to Michael.** |
| C28 | Hold-to-run switching | **Force-guided relay** driven by the lever (weld check on every release) | RT2 #10: a microswitch closing onto bulk capacitance welds. |
| C29 | Head-present switch | **Microswitch under the forehead pad, in series with the loop wire** | RT2 #12: doff with the lever held. |
| C30 | Printing | **Iterate on the home FDM printer; at freeze, send pin cartridges (SLA) and head-borne nodes, hubs, carriage and deck (MJF PA12) to JLC3DP** | DECISION-3 #7; E3 rule "freeze first". |
| C31 | Pad 2 | **Not bought.** Provisions: split vertex node, right-hub second-hinge seat, second drum groove ×3, blanked box ports (PALM B, tees), spare outputs, twin mass budget | DECISION-3 #8. |

---

## 2. System overview and block diagram

### 2.1 What each block does

**Helmet (head-borne, ≈ 286 g; nothing powered).**
- **Retention.** A carbon front half-band runs hub to hub across the forehead (pad envelope ≥ 45 mm above the brows), closing into a bike-helmet **dial cradle** that hooks under the occipital shelf (form lock ≈ 1–1.5 N·m in pitch, override ≈ 10 N). TPU temple pads resist yaw. No chin strap. A microswitch under the forehead pad is the head-present switch.
- **Hubs.** At |Y| = 120 mm, 45 mm above the ear canal, a printed PA12 hub boss on each side carries a Southco E6 friction hinge on the ear axis (α). The left boss carries a spring-ball detent plate (15° clicks) and printed α stops. The **right boss is hollow**: the umbilical enters the head along the ear axis through it. The right boss also has the seat for pad 2's hinge.
- **Bail.** A carbon polygon arc (R 210 about O) of six chords and two legs on seven printed nodes, with a carbon track strip. The vertex node is bolted (pad-2 splice).
- **Carriage.** Rolls on the track on four POM V-rollers; an O-ring friction pad holds it; a spring ball clicks into 10° detents on the strip; printed β stops at ±40°. Carries the float.
- **Float.** Airpel E16 cylinder, 50 mm stroke, spring retract; QEV and relief poppet on its port. Carries the pad on the v2 three-ball magnetic kinematic mount.

**Pad (≈ 81 g; plastic, silicone, steel, magnets; no wire, no valve).**
- **Deck (still):** the dish ceiling (PTFE-taped), three skid stems with POM R 15 domes on a Ø 116 circle (feet ≤ Ø 8, rotated to the field's open corners), RCC struts to the float ring, three tendon housing stops with barrel adjusters on the deck skirt, the PP parallelogram anchor, the lift-tension spring anchor.
- **Pin block (moves ±17 mm, rises ≤ 8.5 mm, tilts ≤ 5.5°):** two printed galleries (A, B) with a Ø 0.15 bleed each, six SLA pin cartridges, three POM domes on top, PP parallelogram link.
- **Tendon yoke:** a PA12 ring around the block, coupled to it by three magnet pairs (2.0 N total shear release); the three series springs anchor on it.
- **Each pin:** Penrose sleeve, POM piston with the breakaway magnet, Ø 1.0 A228 shaft (nose-guided by two bushes), one-piece cone, cylindrical wiper land, return spring ≥ 2× aged friction (C7).

**Umbilical (1.6 m).** 3 × PU 1/8 in × 2 mm (PIN A, PIN B, PALM); 3 × tendon in PTFE-lined coil housing; 4-core 26 AWG (loop out/return through the head-present switch; 2 spares). Loose in a knit sleeve, Ø ≈ 11 mm. Box end: a latched block (tubes push-fit, housings in a three-ferrule hook block, cable on a GX12). Helmet end: continuous to the pad; the loop wire passes a **2-pin magnetic pogo lanyard** that is the shortest member of the bundle.

**Drive box (Apache 2800, ≈ 2.6–2.8 kg).**
- **Puppet master:** three steppers with Ø 12 double-groove drums (groove 2 for pad 2), the floating housing-stop plate with three Hall flexures and a 6 N common-mode spring, a Hall index per drum.
- **Pneumatics:** P1 rail pump → 250 ml accumulator → R1a/R1b → rail sensor → PIN A and PIN B S070s → line sensors A, B; P3 palm pump → 30 ml accumulator → R2/R2b → PALM 3-way → palm sensor; NO dumps on rail and palm; 10 µm filters; inlet mufflers.
- **Electronics:** M8P V2.0 + CB1 (Klipper MCU and host), 12 V 5 A buck for valves and pumps, ADS1115 for the three cable tensions, snag comparator and latch, force-guided relay, watchdog charge pump, fuses.
- **Front face:** leads to the hand controller and e-stop puck; status LED ring.

**User inputs.** The **hand controller** (hold-to-run lever; SPEED and INTENSITY knobs; MODE selector; MOVED button) on 1.5 m; the **e-stop puck** (NC latching mushroom, weighted) on 1.5 m. By Stage D the lever is replaced by a forearm-weight armrest switch (RT1 #10).

**PC.** Optional. Wi-Fi or Ethernet to the CB1: score upload, `scratchctl` console, logs, blind A/B. Nothing on the PC can energise the rail.

### 2.2 Block diagram

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 720" width="1000" height="720" font-family="Helvetica, Arial, sans-serif" font-size="11">
  <defs>
    <marker id="ar" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#333"/></marker>
  </defs>
  <rect width="1000" height="720" fill="#fff"/>
  <text x="14" y="22" font-size="15" font-weight="bold">SP1 v3 PUPPET HALO, LEAN: blocks (black = mechanical, blue = air, orange = tendon, red = actuator rail, green = signal)</text>
  <!-- HELMET -->
  <rect x="14" y="36" width="440" height="430" fill="#f7f7f2" stroke="#555"/>
  <text x="24" y="54" font-weight="bold" font-size="13">HELMET (≈ 286 g single; nothing powered)</text>
  <rect x="28" y="66" width="200" height="66" fill="#fff" stroke="#333"/>
  <text x="36" y="82" font-weight="bold">Retention</text>
  <text x="36" y="96">carbon front band 20×1 + forehead pad</text>
  <text x="36" y="109">dial cradle under occiput (form lock)</text>
  <text x="36" y="122">head-present switch · no chin strap</text>
  <rect x="240" y="66" width="200" height="66" fill="#fff" stroke="#333"/>
  <text x="248" y="82" font-weight="bold">Carbon polygon bail R 210</text>
  <text x="248" y="96">6 chords 8×6 + 7 printed nodes</text>
  <text x="248" y="109">3×1 carbon track strip</text>
  <text x="248" y="122">vertex node = pad-2 splice</text>
  <rect x="28" y="144" width="200" height="80" fill="#fff" stroke="#333"/>
  <text x="36" y="160" font-weight="bold">LEFT hub boss (α by hand)</text>
  <text x="36" y="174">Southco E6 friction hinge</text>
  <text x="36" y="187">spring-ball detent every 15°</text>
  <text x="36" y="200">stops α −25° / +100° (hairline)</text>
  <text x="36" y="213">no motor, no drum, no balancer</text>
  <rect x="240" y="144" width="200" height="80" fill="#fff" stroke="#333"/>
  <text x="248" y="160" font-weight="bold">RIGHT hub boss (hollow)</text>
  <text x="248" y="174">Southco E6 friction hinge</text>
  <text x="248" y="187">umbilical enters on the ear axis</text>
  <text x="248" y="200">seat for pad-2 hinge (provision)</text>
  <text x="248" y="213">lanyard pogo breakaway here</text>
  <rect x="28" y="236" width="200" height="74" fill="#fff" stroke="#333"/>
  <text x="36" y="252" font-weight="bold">Carriage + float</text>
  <text x="36" y="266">4 POM V-rollers, β detents 10°</text>
  <text x="36" y="279">β stops ±40° (mechanical)</text>
  <text x="36" y="292">Airpel E16 float, QEV, relief</text>
  <text x="36" y="305">spring retract 1.2 N</text>
  <rect x="240" y="236" width="200" height="222" fill="#eef4ff" stroke="#1f5fbf" stroke-width="1.5"/>
  <text x="248" y="252" font-weight="bold">PAD (≈ 81 g, no wires)</text>
  <text x="248" y="266">RCC struts · 3 POM R15 skids Ø116</text>
  <text x="248" y="279">deck underside = DISH (PTFE)</text>
  <text x="248" y="292">  R160 centre · 34° rim · 50° rim</text>
  <text x="248" y="305">PIN BLOCK ±17 mm on 3 POM domes</text>
  <text x="248" y="318">  gallery A (P0 P2 P3) · B (C P1 P4)</text>
  <text x="248" y="331">  6 × Ø7 Penrose pins, 18.5 stroke</text>
  <text x="248" y="344">  magnetic nail breakaway 0.12–0.25 N</text>
  <text x="248" y="357">  one-piece drafted POM cones</text>
  <text x="248" y="370">TENDON YOKE ↔ block: 2.0 N shear</text>
  <text x="248" y="383">  3 series springs 2 N/mm</text>
  <text x="248" y="396">  3 housing stops on deck skirt</text>
  <text x="248" y="409">PP parallelogram (no rotation)</text>
  <text x="248" y="422">underside ≥ 32 mm above skin</text>
  <text x="248" y="435">3-ball magnetic kinematic mount</text>
  <line x1="128" y1="224" x2="128" y2="236" stroke="#333" stroke-width="2"/>
  <line x1="228" y1="280" x2="240" y2="280" stroke="#333" stroke-width="2"/>
  <line x1="340" y1="132" x2="340" y2="144" stroke="#333" stroke-width="2"/>
  <rect x="28" y="322" width="200" height="66" fill="#fff" stroke="#2a8a2a"/>
  <text x="36" y="338" font-weight="bold">Head electrics (passive)</text>
  <text x="36" y="352">loop wire pair → head-present</text>
  <text x="36" y="365">switch → magnetic pogo lanyard</text>
  <text x="36" y="378">(the only wires on the head)</text>
  <!-- UMBILICAL -->
  <rect x="470" y="300" width="140" height="150" fill="#fff8e8" stroke="#a57000"/>
  <text x="478" y="318" font-weight="bold">UMBILICAL 1.6 m</text>
  <text x="478" y="333">PIN A  PU 1/8"</text>
  <text x="478" y="346">PIN B  PU 1/8"</text>
  <text x="478" y="359">PALM   PU 1/8"</text>
  <text x="478" y="372" fill="#c06000">3 tendons in PTFE-</text>
  <text x="478" y="385" fill="#c06000">  lined coil housing</text>
  <text x="478" y="398">4-core 26 AWG (loop)</text>
  <text x="478" y="411">knit sleeve Ø ≈ 11</text>
  <text x="478" y="424">ear-axis exit, 3 N clip</text>
  <text x="478" y="437">box end latched</text>
  <line x1="440" y1="330" x2="470" y2="330" stroke="#1f5fbf" stroke-width="3"/>
  <line x1="440" y1="380" x2="470" y2="380" stroke="#c06000" stroke-width="3"/>
  <line x1="610" y1="330" x2="626" y2="330" stroke="#1f5fbf" stroke-width="3"/>
  <line x1="610" y1="380" x2="626" y2="380" stroke="#c06000" stroke-width="3"/>
  <!-- BOX -->
  <rect x="626" y="36" width="360" height="600" fill="#f2f6fb" stroke="#555"/>
  <text x="636" y="54" font-weight="bold" font-size="13">DRIVE BOX (Apache 2800, ≈ 2.7 kg)</text>
  <rect x="638" y="64" width="336" height="92" fill="#fff" stroke="#c33" stroke-width="1.5"/>
  <text x="646" y="80" font-weight="bold" fill="#c33">HARDWARE SAFETY LOOP</text>
  <text x="646" y="95">24 V adapter → F → E-STOP (NC) → force-guided relay (coil =</text>
  <text x="646" y="108">HOLD-TO-RUN) → REFLEX latch → head-present + lanyard loop</text>
  <text x="646" y="121">→ watchdog charge pump gate → ACTUATOR RAIL 24 V</text>
  <text x="646" y="134">  → M8P motor-power input · → 12 V buck → valves, pumps</text>
  <text x="646" y="147">logic: M8P + CB1 on unswitched 24 V (stays up)</text>
  <rect x="638" y="166" width="164" height="128" fill="#fff" stroke="#c06000" stroke-width="1.5"/>
  <text x="646" y="182" font-weight="bold">PUPPET MASTER</text>
  <text x="646" y="196">3 × NEMA17 pancake</text>
  <text x="646" y="209">Ø12 double-groove drums</text>
  <text x="646" y="222">TMC2209 standalone, VREF</text>
  <text x="646" y="235">Hall index per drum</text>
  <text x="646" y="248">floating stop plate, 6 N</text>
  <text x="646" y="261">3 Hall flexures → tension</text>
  <text x="646" y="274">(= drag vector, snag)</text>
  <rect x="810" y="166" width="164" height="128" fill="#fff" stroke="#1f5fbf"/>
  <text x="818" y="182" font-weight="bold">PNEUMATICS</text>
  <text x="818" y="196">P1 → 250 ml acc → R1a/R1b</text>
  <text x="818" y="209">RAIL DUMP (NO) · S rail</text>
  <text x="818" y="222">S070 PIN A · S070 PIN B</text>
  <text x="818" y="235">  (B: PWM servo, S line B)</text>
  <text x="818" y="248">P3 → 30 ml → R2/R2b</text>
  <text x="818" y="261">PALM 3-way · PALM DUMP (NO)</text>
  <text x="818" y="274">10 µm filters · mufflers</text>
  <rect x="638" y="304" width="336" height="156" fill="#fff" stroke="#2a8a2a"/>
  <text x="646" y="320" font-weight="bold">CONTROLLER: BTT Manta M8P V2.0 + CB1</text>
  <text x="646" y="335">Klipper MCU: 3 steppers = G-code axes A, B, C (kinematics none)</text>
  <text x="646" y="349">  HE/FAN low-side outputs: PIN A, PIN B (pwm), PALM, dumps, pumps</text>
  <text x="646" y="363">  TH ADC: rail, line A, line B, palm, knobs · inputs: rail-sense,</text>
  <text x="646" y="377">  latch state, MODE, MOVED, drum index Halls</text>
  <text x="646" y="391">CB1 host: Klipper host · scorer.py (IK, paths, variation,</text>
  <text x="646" y="405">  path checker) · reflexd (ADS1115 tensions, dish-aware</text>
  <text x="646" y="419">  snag criterion → GPIO → REFLEX latch) · logs · scratchctl</text>
  <text x="646" y="433">watchdog PWM (pwm_tool, maximum_mcu_duration) → charge pump</text>
  <text x="646" y="447">LM393 comparator on tensions → REFLEX latch (hardware)</text>
  <rect x="638" y="470" width="336" height="44" fill="#fff" stroke="#333"/>
  <text x="646" y="486">enclosure: Apache 2800, closed-cell foam, sorbothane feet,</text>
  <text x="646" y="500">chair-back hook plate on lid side, strap slots, vents</text>
  <line x1="720" y1="294" x2="720" y2="304" stroke="#2a8a2a" stroke-width="2"/>
  <line x1="892" y1="294" x2="892" y2="304" stroke="#2a8a2a" stroke-width="2"/>
  <!-- INPUTS -->
  <rect x="14" y="486" width="320" height="130" fill="#f3fbf3" stroke="#2a8a2a"/>
  <text x="24" y="504" font-weight="bold" font-size="13">USER INPUTS</text>
  <text x="24" y="522">Hand controller (1.5 m, GX12 8-pin)</text>
  <text x="24" y="536">  lever = HOLD-TO-RUN (drives the relay coil)</text>
  <text x="24" y="550">  SPEED knob · INTENSITY knob · MODE 4-pos · MOVED</text>
  <text x="24" y="564">  Stage D: forearm-weight armrest switch</text>
  <text x="24" y="582">E-stop puck (1.5 m): 22 mm NC latching mushroom</text>
  <text x="24" y="596">  weighted, under the free hand's thumb</text>
  <line x1="334" y1="540" x2="638" y2="110" stroke="#c33" stroke-width="1.5" marker-end="url(#ar)"/>
  <rect x="360" y="640" width="250" height="64" fill="#fff" stroke="#2a8a2a"/>
  <text x="370" y="658" font-weight="bold">PC (optional)</text>
  <text x="370" y="673">Wi-Fi/Ethernet → CB1: scratchctl, scores,</text>
  <text x="370" y="687">logs, blind A/B. Cannot energise the rail.</text>
  <line x1="610" y1="670" x2="700" y2="514" stroke="#2a8a2a" stroke-width="1.5" marker-end="url(#ar)"/>
  <text x="24" y="640" font-size="10" fill="#555">Everything fast, heavy, hot, noisy or switching lives in the box.</text>
  <text x="24" y="654" font-size="10" fill="#555">The head carries air, string, magnets and one switch.</text>
</svg>

### 2.3 Pneumatic schematic (drive box)

```
 P1 rail pump (deadhead ≤ 50 kPa) ─► 10 µm filter ─► 250 ml ACC ─┬─ R1a 20.7 kPa (McMaster 4277T51) ─ R1b ≈ 24 kPa (other make)
   PWM from Klipper heater_generic PID on S_rail                 ├─ RAIL DUMP (NO, 12 V; energised = closed) to muffler
                                                                 ├─ S_rail (XGZP6847A 0–40 kPa)
                                                                 ├─► S070 PIN A (NC: off = line ↔ exhaust) ─► S_A ─► line A (1/8" PU 1.6 m) ─► gallery A ─ Ø0.15 bleed
                                                                 └─► Ø0.3 needle ─► S070 PIN B (PWM 25 Hz when B < rail) ─► S_B ─► line B ─► gallery B ─ Ø0.15 bleed
 P3 palm pump (deadhead ≤ 30 kPa) ─► 10 µm filter ─► 30 ml ACC ─┬─ R2 20.7 kPa ─ R2b ≈ 24 kPa (other make)
                                                                ├─ PALM DUMP (NO) · Ø0.2 palm bleed
                                                                └─► PALM 3-way (off = vent) ─► S_palm ─► palm line ─► QEV ─► Airpel E16 (relief poppet ≈ 26 kPa at the float)
 Pad-2 provisions: tee ports on line A and line B (capped); PALM B outlet on the palm manifold (capped); output channels reserved.
```

### 2.4 Tendon schematic

```
 BOX                                                                                PAD (plan, deck frame P)
 stepper A ─ drum Ø12 (groove 1 = pad 1 · groove 2 = pad 2, point mirror) ═══╗       stop A (deck skirt, R 48, 90°) ─ spring 2 N/mm ─╮
 stepper B ─ drum Ø12 ════════════════════════════════════════════════════════╬═══►  stop B (210°) ─ spring ──────────────── TENDON YOKE (R 30)
 stepper C ─ drum Ø12 ═══════════════════════════════════════════════════════╝       stop C (330°) ─ spring ─╯                 │ 3 magnet pairs,
 housing stops on ONE floating plate (6 N common-mode spring);                                                               │ 2.0 N shear
 each stop on a printed flexure ≈ 20 N/mm + Hall sensor (tension ±0.1–0.2 N)                                                   PIN BLOCK (PP-square)
 pretension 1.5 N per cable; drum Hall index = block centred
 cable: 0.45 mm nylon-coated 7×7 stainless; housing: PTFE-lined close-wound coil ≈ 1.2/0.6 mm; length 1.6 m
```

---

## 3. Coordinate frames and the head model

### 3.1 Frames (right-handed, mm, degrees)

| Frame | Origin | Axes | Moves with | Used by |
|---|---|---|---|---|
| **H** head | **O, the skull centre**: 45 mm above and 10 mm behind the tragion midpoint, on the midsagittal plane | X forward, Y left, Z up (Frankfurt horizontal) | the head (halo rigid to it within slip) | fences, stations, mass/CoM |
| **B** bail | O | rotated by **α about Y_H**; α = 0 over the vertex; **+α toward the occiput** | bail (hand) | hinge detents, α stops |
| **C** carriage | on the bail arc at latitude **β** (+β toward the left ear) | z_C radial outward from O; x_C along the bail tangent toward +β | carriage (hand) | β detents, float |
| **P** pad | the **nail plane** at the pad axis (where the RCC lines cross) | z_P along the pad axis away from the scalp; x_P = bail tangent at β = 0 | pad body | pin layout, dish, skids, housing stops |
| **S** scrub | pin-block centre projected in P | parallel to P; block offset **d = (x_S, y_S)**, |d| = radial offset | pin block | paths, dish height z(d), tilt t(d) |
| **L** drum (new) | per-cable | cable length change ℓ_i (mm) = drum angle × 6 mm; ℓ = 0 at centred block | drums | IK output = G-code axes A, B, C |

**Direction to the pad centre:** **u(α, β) = R_Y(α) · (0, sin β, cos β)**. The pad sits at r_skin(u) + stack along u.
**Point mirror (pad 2):** pad 2 at **(−α, −β)**; u₂ = R_Z(180°) · u₁; its block offset is −d in its own P frame, so its three cables on the second drum grooves see the same ℓ_i as pad 1's cables.
**Hub axis:** Y_H; hubs at Y = ±120 mm, Z = 0.
**Tendon stop angles in P:** A at 90°, B at 210°, C at 330° (pad 2: 270°, 30°, 150°).

### 3.2 Design head (50th-percentile adult male, [EST]; replaced by Michael's tape fit)

| Quantity | Value |
|---|---|
| Ellipsoid about O, semi-axes | a = 98 (X), b = 77 (Y), c = 88 (Z+) |
| Scalp distance from O | 77–80 sides, 88 vertex, ≈ 98 at the occipital bun |
| Local radius of curvature | crown 85–100, sides 100–150 (vertical), bun 60–80 mm |
| Ear canal (tragion) in H | (−10, ±72, −45) |
| Neck pivot | (−10, 0, −80) |
| Head mass | 4.5 kg |
| Design hair | 2–8 cm, pile 10–25 mm; Michael's length and pile are measured at S0 |

### 3.3 Calibration chain (no scan)

1. **Drum zero.** At every ARMING each drum turns until its Hall index triggers (block centred over the dish, pad retracted, pins vented). Index repeatability ≤ 0.1 mm of cable [VERIFY A3].
2. **Tendon trim.** Once per build and after any cable change: barrel adjusters set equal pretension (1.5 ± 0.1 N on the Hall flexures) with the block centred; the ink rosette (A3) confirms centre ±0.3 mm.
3. **Fit.** Dial set once; band position marked. Seating repeats to ±5–10 mm.
4. **Stations.** α detents every 15°, β every 10°. The hairline and ear fences are **mechanical stops** set once from Michael's head (Stage C1) and verified with the halo displaced ±15 mm. There is no firmware fence and no registration: nothing powered moves the halo.

---

## 4. Frozen numbers

### 4.1 Pins and nails

| Item | Value | Tag / source |
|---|---|---|
| Layout | centre C + pentagon P0…P4 at R 18 mm (P0 on +x_P), axes ∥ z_P; min spacing 18 mm | decision-analysis |
| Groups | A = P0, P2, P3 (gallery A); B = C, P1, P4 (gallery B) | C1 |
| Bore / area | 7.0 mm / 38.5 mm²; 0.0385 N/kPa | arithmetic |
| Operating rail | 2–13 kPa = 0.08–0.50 N; firmware ceiling 15.6 kPa = 0.60 N; **net-force floor 0.20 N for first sessions** (RT1 #3) | EST |
| Caps | R1a 20.7 kPa → **0.80 N**; R1b ≈ 24 kPa → 0.92 N; P1 deadhead ≤ 50 kPa → ≤ 1.93 N | EST [VERIFY V9, V12] |
| Stroke | **18.5 mm**: retract stop at 0; nominal contact at 15.0 mm extension; reserve 1–3.5 mm (worst residual curvature) | C6 |
| Return spring | 0.03 N at contact, **≥ 2× measured aged wiper + bush friction** (C7) | KNOWN (ruling) |
| Breakaway (C1) | Ø 3 × 2 N52 in the piston face; shaft end ground flat; **axial release 0.12–0.25 N**; ≤ 0.35 N with 0.5 N tangential at the tip; **B_min ≥ 3× aged friction**; compression proof ≥ 3.1 N; lateral ≥ 3.0 N in the guides | KNOWN (ruling) |
| Nail (C2, C4) | 90° tip cone from Ø 2.0 flat (rim R 0.4) to Ø 4.5 at 1.25 mm, then 2.5° per face to the nose; no shoulder within 3 mm of the nose at full retract; one piece with the shaft (hook + epoxy fill; tension proof 3.1 N); red/orange POM; shaft top domed R 0.5; mass ≈ 0.3 g | KNOWN (ruling) |
| Wiper | 40A silicone, cylindrical land ≥ stroke + 3 mm = 21.5 mm; recloses after a nail drops | C2 |
| Shaft guides | two POM bushes 12 mm apart, Ø 1.02 bore | EST |
| Block underside | ≥ 32 mm above nominal skin at every pose; drafted ≥ 15° at the rim; Ra ≤ 0.8 µm | H-6.3 |
| Gallery bleed | one Ø 0.15 (30G needle) per gallery: a kinked, pressurised line < 2 kPa in < 1 s | C3 |
| Vent time | gallery force < 0.05 N (< 1.3 kPa) **≤ 100 ms** after de-energise; else fit a gallery QEV | C3 [VERIFY A2] |
| Retracted pin (sat out) | every vented nail retracts ≥ 8 mm within 200 ms (C7) | KNOWN (ruling) |
| Pin installed mass | ≈ 2.5 g (cartridge, sleeve, piston, magnet, nail) | EST |

### 4.2 Dish and stroke geometry

| Item | Value | Tag |
|---|---|---|
| Dish centre | sphere **R 160 mm** about the skid-registered scalp centre (scalp R 85 + 75 mm follower height), for |d| ≤ 7 mm | leap4-A |
| Inner rim (landing band) | **34°** (print 33–35°) from |d| 7.0 to **13.7 mm**, rise 4.5 mm | C5 |
| Outer rim | **50°** from |d| 13.7 to **17.0 mm**, rise 4.0 mm (total +8.5) | §1 C6 |
| Domes / tape | 3 POM domes Ø 6 on the block top at R 22; PTFE 0.13 mm tape on the dish | leap4-A |
| Lift tension | 0.5–0.6 N deck-to-block spring (carries the 35 g block on the rim) | leap4-A |
| Nail landing | each nail lands where block height = its reserve: |d| ≈ 8.5–12.2 mm | EST |
| Lift clearance | ≥ 5 mm at the worst reserve for |d| ≥ 13.7; 5–7.5 mm at the outer rim | C5 |
| No-reversal radius | the path checker rejects any reversal or cusp inside **|d| < 13.7 mm** | C5 |
| Contact chord (through centre) | 17–24 mm (reserve-dependent); off-centre chords 5–23 mm | EST |
| Amplitude | ≤ ±16.5 mm working, rim top 17.0 | EST |
| Spread of nail-to-skin distance in contact | ≤ 1.3 mm (R 65), 0 (R 85), ≤ 0.6 (R 100), ≤ 2.2 mm (sides 70 × 150) | leap4-A [EST] |
| Block tilt / rise | ≤ 5.5° / ≤ 8.5 mm (both modelled in IK, §8.2) | EST |
| Rim reaction (horizontal) | ≈ 1.2 N on the inner rim with pins in contact; ≈ 0.7 N on the outer rim (pins up); + ≈ 0.25 N PTFE drag | EST [VERIFY A3] |
| Landing spread | 30–40 ms natural (reserves differ by up to 2.5 mm) | leap4-A |

### 4.3 Pneumatic rails and caps

| Rail / line | Setpoint | Cap (mechanical) | Regulator | Fail state |
|---|---|---|---|---|
| Pin RAIL | 2–13 kPa (intensity knob × variation) | R1a 20.7 + R1b ≈ 24 kPa; deadhead ≤ 50 | P1 PWM + 250 ml acc; Klipper PID (≈ 3 Hz is enough with 250 ml) | RAIL DUMP (NO) opens |
| Line A | = rail when on; vented when off | as rail | S070 PIN A | vents (S070 de-energised = exhaust) |
| Line B | rail × (0.5–1.0) when contrast is on | as rail (servo is downstream of R1a/R1b) | S070 PIN B PWM 25 Hz + Ø 0.3 inlet needle + S_B | vents |
| PALM | 8–20 kPa → float 1.6–4.0 N push (Ø 16, 2.0 cm²) minus 1.2–1.7 N spring | **R2 20.7 kPa + R2b ≈ 24 kPa + deadhead ≤ 30 kPa + relief poppet at the float ≈ 26 kPa** | P3 PWM + 30 ml acc + Ø 0.2 bleed | PALM 3-way vents + PALM DUMP + Airpel clearance leak + QEV |

**Total scalp normal load (single):** float force at R2 4.1 N − spring ≥ 1.2 N + pad weight ≤ 0.8 N (vertex) = **≤ 3.7 N** at R2; **≤ 4.6 N** at R2b; **≤ 6.8 N** at the 30 kPa deadhead with both reliefs failed; ≤ 12 N (red line 3) in every case. Pins cannot add to it: they react against the pad.

**Force budget consequence [EST]:** with all six nails down, Σ F_pins ≤ net float − 0.45 N skid floor ≈ 2.2–2.4 N, i.e. ≤ 0.37 N per nail at all-six; ≤ 0.50 N per nail with one group down. Firmware enforces Σ F_pins + 0.45 N ≤ F_float (constant support). If Stage B says "not hard enough", the fallback is the Airpel E24 bore (+≈ 15 g [VERIFY]).

**Air budget [EST]:** line mode with an open line exchanges ≈ 0.6 ml per landing; bleeds dominate: ≈ 0.1 L/min plus PWM losses when B-contrast is on (≈ 0.3 L/min). P1 runs at ≈ 10–20 % duty.

### 4.4 Tendon puppet

| Item | Value | Tag |
|---|---|---|
| Cables | 3 × 0.45 mm nylon-coated 7×7 stainless (0.36 mm metal), 1.6 m; crimped ferrules both ends | leap4-D |
| Housings | PTFE-lined close-wound coil ≈ 1.2 OD / 0.6 ID, greased; bending stiffness ≈ 30 N·mm² | leap4-D [VERIFY creak V-T3] |
| Drums | Ø 12 mm printed (SLA), helical groove, double-grooved (groove 2 = pad 2); 30 mm stroke = 0.8 turn | leap4-D |
| Steppers | 3 × 17HS08-1004S class (13 N·cm), TMC2209 standalone 1/16 µstep with interpolation, stealthChop, **VREF ≤ 0.35 A** (≤ 5 N cable pull) | EST |
| Resolution | 12 µm of cable per microstep | arithmetic |
| Pretension | 1.5 N per cable (1 N pad load moves tensions ≤ ±0.67 N; never slack) | leap4-D |
| Series springs | 2 N/mm, ≥ 4 mm linear travel each | leap4-D |
| Stiffness | cable EA ≈ 5.2 kN → 3.2 N/mm per 1.6 m; with spring 1.2 N/mm per cable; **1.9 N/mm at the block** | leap4-D [EST] |
| Plate resonance | ≈ 34 Hz (block + yoke ≈ 47 g), cable-friction damped | EST |
| Tangential cap | **2.0 N** magnetic shear coupling (3 magnet pairs, Ø 6 × 3 N52 on steel discs); never > 2.5 N; VREF backup ≤ 5 N per cable | §1 C15 |
| Tension sensing | Hall flexure per stop, ≈ 20 N/mm, resolution 0.1–0.2 N, read at ≈ 280 Hz per channel (ADS1115) | leap4-D [VERIFY] |
| Dead band (friction) | 0.43 mm (μ 0.08, 1.5π bend) to 1.96 mm (μ 0.15, 2π); compensated per cable to ≤ 0.3 mm residual | leap4-D |
| Common-mode | floating stop plate with 6 N spring; differential pose drift ≤ 0.1 mm | leap4-D |
| Cable life | consumable; inspect every 10 sessions; replace at first broken strand or 50 sessions [VERIFY V-T4] | JUDG |

### 4.5 Modes and paths (block offset d in frame S)

Every mode is a path d(t) planned by the host and checked before it is sent (§8.3). The nails are down only where the dish lets them be (|d| ≲ 8.5–12.2 mm); everything outside is lifted travel.

| Mode | Path | Default (bold) | Range / limits |
|---|---|---|---|
| **PLINE** (default) | straight stroke through the centre, ±A along heading ψ; ψ advances Δψ per cycle | f **1.4 Hz**, A **16 mm**, Δψ **4.5° per out-and-back cycle** (180° in 40 cycles = 28.6 s); per-cycle Δψ jitter ±1.5°; sign flips with p 0.2 at pauses | f 0.6–2.0 Hz; A 14–16.5 |
| LINE | as PLINE with Δψ = 0 | ψ with-grain (set from the MOVED-station default table or by `psi`) | same |
| CIRCLE | circle of radius R about an offset centre c (|c| = e), so |d| sweeps R − e … R + e; nails touch only on the near arc and **lift once per revolution** | **R 11.5, e 3.5** (|d| 8 → 15, contact ≈ 40 % of a revolution) | R 9–13, e such that R + e ≥ 14.5 and R − e ≤ 8.5; 2πfR ≤ 188 mm/s; **offset heading rotates 15–40° per revolution** |
| CHORD (variation) | straight stroke offset e from the centre, perpendicular to ψ | e drawn per stroke | e 0–9 mm → contact 5–23 mm |
| D-PATH (variation) | contact along a chord through the centre in the with-grain direction, return round the rim at |d| ≥ 15 (nails up) | 3–8 D-strokes as a burst | only with-grain; v ≥ 0.3 v_peak at landing and lift |
| REST / PARK | block parked on the rim at |d| = 16.5, nails up | 0.2–0.8 s pauses; ≥ 2 s at station changes | — |
| MIX (MODE position 4) | the variation generator chooses PLINE / LINE / CIRCLE / CHORD / D-PATH phrases | weights 50 / 15 / 10 / 15 / 10 % | — |

**Speeds on the 32 mm PLINE (A 16 mm):**

| f | v_peak | v at landing (|d| ≈ 10) | peak accel in contact | time on the rim per end |
|---|---|---|---|---|
| 1.0 Hz | 101 mm/s | 79 mm/s (0.78 v_peak) | 0.48 m/s² | ≈ 225 ms |
| **1.4 Hz** | **141 mm/s** | **110 mm/s** | **0.94 m/s²** | **≈ 160 ms** |
| 2.0 Hz | 201 mm/s | 157 mm/s | 1.93 m/s² (H-5.4: ≤ 2) | ≈ 110 ms |

The drums are not limited to sinusoids: the host plans **constant-speed contact with quick lifted turnarounds** (trapezoid in |d|, turnaround inside the rim), which raises the time in contact without raising v_peak. Max scrub rate: **2.0 Hz on the line** (v ≤ 200 mm/s, a ≤ 2 m/s² in contact).

### 4.6 Copy error budget (at the nail, in contact, 0.5 N drag) [EST]

| Source | Along-stroke | Lateral | Notes |
|---|---|---|---|
| IK geometry (dish z, tilt, effective anchors) | ≤ 0.1 | ≤ 0.1 | modelled, ink-trace trimmed |
| Step quantisation | 0.012 | 0.012 | — |
| Series + cable compliance (0.5 N / 1.9 N/mm) | −0.26 | ±0.1 | felt as finger-like give |
| Dead band, lines (reversal on the rim) | ≈ 0 in contact | — | reversal happens nails-up |
| Dead band, circles (after compensation) | ≤ 0.3 | ≤ 0.3 | ±30 % friction variation with pose |
| Common-mode residue (bail moved, head turned) | ≤ 0.1 | ≤ 0.1 | tensioner |
| Rim reaction (1.2 N on the landing band) | −0.6 at landing only | — | nails landing; shortens the chord slightly |
| **RSS in contact** | **≤ 0.45 mm** | **≤ 0.35 mm** | pass line: bow ≤ 0.5 mm; scalp acuity 15–39 mm |

### 4.7 Halo, stations and coverage

**Radial chain at the pad axis** (above the skin): skin 0 → block underside 32 → pin tops ≈ 62 → dish ceiling and deck top ≈ 75 → RCC float ring 80 → float (working extension) → carriage → bail centreline. The float's 50 mm stroke splits into 25 mm to absorb scalp radius (77–98 mm) and 25 mm of retract. **R_bail = 98 + 80 + 25 + 7 ≈ 210 mm** (unchanged from v2).

| Axis | Range | Holding | Indexing | Stops |
|---|---|---|---|---|
| α (bail pitch) | −25° … +100° (set to the hairline: α_stop = α_hairline + 20°) | 2 × Southco E6-10-101-20 (≈ 0.25 N·m each [KNOWN, catalogue 2.19 in·lbf]) + detent ≈ 0.15 N·m → ≈ 0.65 N·m against a worst 0.27 N·m gravity + 0.11 N·m scrub = 0.38 N·m (margin 1.7) | spring-ball click every 15° | printed bosses on the left hub |
| β (latitude) | ±40° | carriage O-ring friction ≥ 3 N along the track | spring ball into 10° notches on the track strip | printed end blocks with TPU bumpers at ±40° (RT2: pads reach the hub bosses past β ≈ 41–46°) |
| Float (radial) | 0–50 mm | palm pressure / spring | — | piston ends |

**Stations:** 9 α detents × 9 β detents (with the hairline and side stops removing ≈ 20 corner poses) ≈ **60 usable stations**. Moving between stations happens only with the lever released (pins vented, pad retracted ≥ 25 mm), so no element moves on the scalp during a move (H-5.8).

**Coverage (reachable)** [EST, v2 model with β trimmed to ±40°]: crown/vertex 100 %; upper occiput 100 %; bun/lower occiput ≈ 90 %; parietal sides ≈ 80 % (β ±40°); frontal top ≈ 80 %; low sides/temples ≈ 55 %. **Total ≈ 85 %** (v2 claimed 90 % at β ±55°, which RT2 showed collides). [VERIFY V18 on Michael's head]

**Overload behaviour:** above the hinge torque the bail simply swings (back-drivable; red line 7 is not engaged, nothing is self-locking).

### 4.8 Mass budget and centre of mass (single pad)

Ledger [EST, `12-sp1v2/scripts/mass_v3.py`]:

| Part | g | Basis |
|---|---|---|
| Carbon front band 20 × 1 | 8 | leap4-C C3 |
| Forehead pad + sleeve + head-present switch | 6 | leap4-C |
| Dial cradle (harvested bike retention) | 30 | leap3-D/E |
| Temple pads ×2 | 6 | v2 |
| Doff lip node | 3 | leap4-C |
| Hub bosses ×2 (PA12) + 2 E6 acetal hinges + detent | 30 | EST [VERIFY hinge mass] |
| Carbon polygon bail with nodes and track | 36 | leap4-C C3 |
| Carriage (rollers, detent, friction pad) | 10 | v2 |
| Float: Airpel E16 + rods/spring + QEV + float relief | 24 | EST [VERIFY Airpel mass ≤ 16 g] |
| **Pad**: deck + dish + skids + RCC + cover 28; block + 6 pins + domes + galleries 35; yoke + coupling + springs + stops 12; PP 2; lift spring + tape 1.5; jumpers 3 | **81.5** | EST |
| Head-side harness on the bail (3 tubes + 3 housings + cable, ≈ 0.5 m at ≈ 43 g/m) | 21 | EST |
| Umbilical head share (½ of a 0.45 m loop) | 11 | EST |
| Lanyard pogo, clips | 5 | EST |
| Fasteners, glue, misc | 10 | EST |
| Pad-2 provisions (hinge seat, splice node hardware) | 2 | EST |
| **Total** | **≈ 286 g** (≈ 260–320 g) | red line 10: ≤ 500 g |

**Pad 2 (later):** + pad 81.5 + float 24 + carriage 10 + hinge 7 + harness B 21 + umbilical share 5 ≈ **+150 g → ≈ 440 g twin**, ≈ 60 g under the 500 g line with full-size tubes; no mass ladder needed.

**Centre of mass** (`mass_v3.py`, single pad):

| Pose (α, β) | CoM in H (X, Y, Z) mm | Gravity moment about O, upright |
|---|---|---|
| (−25°, 0) front | (+33, −6, 78) | 0.09 N·m |
| (0, 0) vertex | (−4, −6, 85) | 0.02 N·m |
| (45°, 0) upper occiput | (−67, −6, 61) | 0.19 N·m |
| (90°, 0) bun | (−95, −6, −2) | **0.27 N·m (worst)** |
| (0, ±40°) sides | (−4, +38 / −50, 67) | 0.11 / 0.14 N·m |

- **Hold:** dial cradle form lock 1–1.5 N·m gives a margin of ≥ 3.7 on the worst lean plus 0.11 N·m scrub reaction.
- **Felt lean** is [VERIFY C3 coin test]. The −6 mm Y offset is the right-side umbilical. Pad 2 later cancels the lean (v2: twin ≈ 0.03 N·m).

### 4.9 Noise budget (A-weighted at the ear, box 0.7–1.2 m away) [EST]

| Source | Path | Mitigation | At ear |
|---|---|---|---|
| Steppers ×3 (stealthChop, 24 V) | air | foam-lined case, rubber motor mounts | ≤ 22 dBA |
| Stepper ripple through the tendons | bone via the pad | 2 N/mm series springs (+6 dB vs air puppet; 0 dB with 1 N/mm) | inaudible target [VERIFY earplug A/B at S0] |
| Pumps P1, P3 | air | low duty (≈ 10–20 %), sorbothane, inlet mufflers | ≤ 25 dBA |
| S070 PIN valves | air | switch only at group changes (rim); B PWM only during contrast phrases | ≤ 20 dBA; PWM ≤ 25 dBA |
| Cable creak in housings | bone + air | PTFE-lined, greased housings | [VERIFY V-T3] |
| Dish PTFE-on-POM stick-slip | bone | tape choice, dome finish | [VERIFY V-D3] |
| Nail landings | bone | 34° ploughing landings, 30–40 ms spread | ≤ 20 dBA |
| **Machine total** | | | **≤ 30 dBA target; ≤ 60 dBA hard** |
| Nail hiss (wanted) | | never masked | 30–40 dBA |

There is no motor, servo or valve on the head: v2's bone-path servo risk (R6) and RT1 #6 (servo hunting) are gone.

### 4.10 Power budget (24 V adapter, 60 W)

| Load | Typical | Peak |
|---|---|---|
| Steppers ×3 (VREF ≤ 0.35 A) | 8 W | 12 W |
| Pumps P1, P3 (12 V, PWM) | 3 W | 10 W |
| S070 ×2 (0.5 W), PALM 3-way (≈ 2 W), NO dumps ×2 held closed (≈ 2 W each) | 7 W | 8 W |
| M8P + CB1 + sensors + comparator | 6 W | 8 W |
| 12 V buck losses | 2 W | 4 W |
| **Total** | **≈ 26 W** | **≈ 42 W** (adapter 60 W; inlet fuse 3.15 A slow) |

### 4.11 Latency budget

| Path | Value | Basis |
|---|---|---|
| Score change (knob, mode) → motion | ≤ 0.5 s (host keeps ≤ 0.5 s of moves queued) | §8.2 [VERIFY V-K2] |
| Group switch (SET_PIN, synchronised to the rim) | at print time ± 1 ms; line fill ≈ 60–150 ms through the needle (B) | Klipper lookahead [KNOWN, leap4-E] |
| Line vent → gallery force < 0.05 N | ≤ 100 ms | C3 [VERIFY] |
| E-stop / lever / reflex latch → rail dead | < 5 ms (relay drop-out) | hardware |
| Rail dead → pins vented | ≤ 100 ms | C3 |
| Rail dead → pad retracted 25 mm | ≤ 150 ms (QEV) | RT2 #7 [VERIFY B4] |
| Rail dead → drums stop driving | immediate (motor power off) | hardware |
| Hardware comparator trip | ≤ 5 ms after threshold | hardware |
| reflexd firmware trip (dish-aware) | ≤ 15 ms (4 ms ADC + compute + GPIO) | EST [VERIFY C4 test: ≤ 50 ms total] |
| Watchdog: MCU halt or host loss → rail open | ≤ 50 ms (charge pump decay) after the watchdog PWM stops | EST |

---

## 5. Interfaces

The owning work package (§11) designs both sides of each interface and changes it only through a revision of this table. Fasteners are M3 into brass heat-set inserts (Ø 4.0 × 5.7 mm holes) unless stated. Hair-zone parts are POM, PETG or PA12, sanded and sealed.

### 5.1 Mechanical

| ID | Interface | Geometry / bolt pattern | Datum | Owner |
|---|---|---|---|---|
| M1 | Hub boss ↔ front band and cradle arms | 3 × M3 on a 24 mm triangle + one Ø 3 dowel | boss flange F1 ⟂ hub axis at |Y| = 95 mm | HALO |
| M2 | Bail leg node ↔ hinge | Southco E6-10-101-20 leaves: one leaf to the boss (2 × M3 per catalogue pattern [VERIFY]), one to the leg node; hinge pin on the ear axis ±0.5 mm | hinge pin = hub axis; α = 0 by a printed zero gauge | HALO |
| M3 | α detent | Ø 4 spring ball in the leg node, 24 notches (15°) on the left boss face; click torque ≈ 0.15 N·m | — | HALO |
| M4 | α stops | printed bosses on the left boss at α_hairline + 20° and +100° (default −25°/+100°), TPU bumpers | from Michael's tape fit | HALO |
| M5 | Bail ↔ carriage | 4 POM V-rollers (groove for the 3 × 1 strip + tube) on Ø 3 pins; O-ring friction pad ≥ 3 N; Ø 3 spring ball into 10° notches cut in the track strip | track strip centreline | HALO |
| M6 | β stops | printed end blocks with TPU bumpers on the bail at β = ±40° | — | HALO |
| M7 | Carriage ↔ float | 2 × M3 on 24 mm + Ø 4 dowel; float axis radial through O within 1° | carriage underside | HALO |
| M8 | Float ↔ pad | v2 3-ball kinematic mount: Ø 5 balls on the float ring (Ø 110, 120°) into V-grooves on the RCC ring; 3 × N52 Ø 6 × 3, ≈ 6 N axial breakaway | ball triangle defines frame P | PAD (grooves) / HALO (balls) |
| M9 | Pin cartridge ↔ block | Ø 10.0 × 38 mm SLA cartridge in a Ø 10.1 bore; O-ring retention; gallery port O-ring face seal; positions ±0.1 mm | block underside plane | PAD |
| M10 | Nail ↔ piston (C1) | Ø 1.0 shaft flat end on a Ø 3 × 2 N52 in the piston face; no other axial retention; two guides give lateral location | piston face | PAD |
| M11 | Block ↔ dish | 3 POM domes Ø 6 at R 22 on the block top; dish PTFE-taped; lift spring 0.5–0.6 N centred | dish vertex = P origin + 75 mm | PAD |
| M12 | Yoke ↔ block | 3 magnet pairs at 120° (Ø 6 × 3 N52 on the yoke, steel discs on the block); 2.0 N total shear release; yoke rises and tilts with the block | block centre | PAD |
| M13 | Tendon stop ↔ deck | 3 printed stops on the deck skirt at R 48 (90°, 210°, 330°), M3 barrel adjuster, ferrule seat for the housing | deck plane | PAD |
| M14 | Tendon ↔ yoke | series spring (2 N/mm) between the cable ferrule and a yoke post at R 30 | yoke plane | PAD |
| M15 | Umbilical ↔ right hub | Ø 14 bore along the ear axis in the right boss; strain-relief clamp inboard; lanyard pogo seat on the outboard face | hub axis | HALO |
| M16 | Box mounting | lid-side hook plate (4 × M5, 200 × 120 mm), 2 × 40 mm strap slots, 4 sorbothane feet, case handle | case rear face | DRIVE BOX |
| M17 | Drum module | three drums on 5 mm motor shafts, grub screw on flat; stop plate on two Ø 4 rods, 6 N spring; Hall index magnets on the drum flanges | module base plate | DRIVE BOX |
| M18 | Pad-2 provisions | vertex node 2 × M3 splice; right boss second-hinge seat (M2 pattern mirrored); second drum groove on each drum | — | HALO / DRIVE BOX |

### 5.2 Pneumatic

| ID | Line | Tube | Length | Ends | Range | Owner |
|---|---|---|---|---|---|---|
| A | PIN A | PU 1/8 in OD × 2 mm ID | 1.6 m box to pad + 0.15 m on-pad jumper to gallery A | S070 barb Ø 3.18 (S070C-6DC-32 "32"); push-fit at the box block; barb at the gallery | 0–24 kPa | DRIVE BOX / PAD |
| B | PIN B | as A | as A | as A | 0–24 kPa | DRIVE BOX / PAD |
| P | PALM | as A | 1.6 m + 0.2 m to the QEV on the float | push-fit; QEV inlet | 0–26 kPa | DRIVE BOX / HALO |
| — | In-box | PU 1/8 in and 4 mm push-fit; bought tees and 5-way manifolds (no printed barbs) | — | — | — | DRIVE BOX |

**Seal spec:** pin lines ≤ 1 kPa/min decay with the gallery bleed plugged; palm line ≤ 2 kPa/min excluding the Airpel leak. **Filters:** 10 µm on both pump outlets (RT2 #14).

### 5.3 Tendon

| ID | Item | Spec | Owner |
|---|---|---|---|
| T1 | Cable | 0.45 mm nylon-coated 7×7 stainless; ferrule crimp at the drum (into a slot) and at the spring (Ø 1.6 brass); proof 30 N | DRIVE BOX |
| T2 | Housing | PTFE-lined coil ≈ 1.2 OD, 1.6 m; ferrule caps both ends; seated in the box stop plate and the deck stops | DRIVE BOX |
| T3 | Box release | the three housing ferrules sit in a hook block that lifts out when the box-end latch opens; cables unhook from the drums by their slotted ferrules | DRIVE BOX |
| T4 | Routing on the head | box → clip → right hub bore (ear axis) → along the bail in a clip track → carriage → 150 mm service loop → deck stops; minimum bend radius 25 mm | HALO |

### 5.4 Electrical

| ID | Interface | Voltage / current | Connector | Wires |
|---|---|---|---|---|
| E1 | Adapter → box | 24 V DC, 60 W, Mean Well GST60A24-P1J class (UL/CE) | 5.5 × 2.1 panel jack | 2 |
| E2 | Logic supply | unswitched 24 V → M8P VIN (CB1 on the board); inlet fuse 3.15 A slow | internal | — |
| E3 | Actuator rail ACT-24 | switched by the safety loop → M8P motor-power input (driver supply jumper set to the separate input) [VERIFY V-E1] | screw terminals | 18 AWG |
| E4 | ACT-12 | 12 V 5 A buck from ACT-24 → **+ side of every valve and pump**; the − side of each load goes to an M8P low-side output (HE0–3, HB, FAN0–4); external flyback diode (SS14) per coil | Wago | 20 AWG |
| E5 | Helmet loop | 3.3 V, 1 mA logic loop: box → umbilical → lanyard pogo → head-present switch → return; gates the rail relay | GX12 4-pin at the box; 2-pin magnetic pogo at the right hub | 2 (+2 spare) |
| E6 | E-stop puck | NC latching, in series with the relay coil supply and with the rail | GX12 4-pin (2 used + 2 sense) | 4 |
| E7 | Hand controller | lever (relay coil feed), SPEED pot, INTENSITY pot, MODE 4-pos (resistor ladder), MOVED button, 3.3 V, GND | GX12 8-pin | 8 |
| E8 | Tension sensors | 3 × linear Hall (DRV5053-class) at 3.3 V → ADS1115 (I²C on the CB1 header) and → LM393 window comparators | internal | — |
| E9 | REFLEX latch | SR latch (74HC74 or a latching relay): SET by any comparator or by CB1 GPIO; RESET only by releasing the lever; output in series with the rail relay coil | internal | — |
| E10 | Watchdog | M8P FAN output as hardware PWM 1 kHz 50 % → charge pump → gate of the rail-enable MOSFET in series with the relay coil | internal | — |
| E11 | Rail sense | ACT-24 divider → M8P endstop input (read-only) | internal | — |
| E12 | PC | Wi-Fi / Ethernet to CB1 (logic domain only) | — | — |

**Wires through the umbilical: 4** (loop out, loop return, 2 spare), 26 AWG. Nothing on the head draws power.

### 5.5 Control (Klipper resource map)

| Function | M8P resource | Klipper object | Rate |
|---|---|---|---|
| Drums A, B, C | Motor 1–3 (TMC2209 standalone) | `[manual_stepper cable_a/b/c]`, assigned `GCODE_AXIS=A/B/C` at start-up; `endstop_pin` = drum Hall index | step ≤ 2 kHz |
| PIN A valve | HE0 (low side) | `[output_pin pin_a]` shutdown_value 0 | at group changes |
| PIN B valve | HE1 | `[pwm_tool pin_b]` cycle_time 0.04, `maximum_mcu_duration` 3 s, shutdown_value 0 | PWM 25 Hz |
| PALM 3-way | HE2 | `[output_pin palm]` shutdown_value 0 | approach / retract |
| RAIL DUMP, PALM DUMP (NO) | HE3, HB | `[output_pin]` value 1 = closed; shutdown_value 0 = open | — |
| P1, P3 pumps | FAN0, FAN1 | `[heater_generic rail]`, `[heater_generic palm]` with `[adc_temperature]` kPa tables on TH0 / TH3; `verify_heater` relaxed; `min_temp: -20` | PID ≈ 3 Hz |
| Line A, line B sensors | TH1, TH2 | `[temperature_sensor]` with kPa tables | 3 Hz (report) |
| Knobs SPEED, INTENSITY, MODE | TB + Pico-free: ADS1115 ch 3 for MODE ladder [EST]; SPEED and INTENSITY on spare TH via ADC expansion | `[temperature_sensor]` (linear tables) | 3 Hz |
| MOVED, rail sense, latch state | endstop inputs | `[gcode_button]` | event |
| Watchdog PWM | FAN2 | `[pwm_tool watchdog]` `maximum_mcu_duration` 1 s, refreshed by the host every 0.25 s | — |
| Cable tensions | CB1 I²C → ADS1115 (3 ch) | read by `reflexd` (outside Klipper) | ≈ 280 Hz/ch |

If the M8P's free ADC count is short, the two pots go on the ADS1115's spare channel through a 2:1 mux or onto a $5 RP2040 as a second Klipper MCU; the CAD/ELECTRONICS WP picks one at A0 [VERIFY V-E3].

---

## 6. Drive box portability (binding)

**Targets:** Apache 2800 case, **343 × 289 × 152 mm outside** (302 × 229 × 135 inside) [KNOWN, Harbor Freight, $29.99, checked 2026-10-02]; loaded **≤ 2.8 kg** [EST: case ≈ 1.4 kg + contents ≈ 1.2 kg; VERIFY A5]; ≤ 30 dBA at 1 m; any orientation (no liquid, no gravity-referenced parts, pumps on sorbothane); all user items on 1.5 m leads from the front face. The 2.5 kg v2 target is relaxed to 2.8 kg: the bought case saves 6–8 h and is IP65, latched and handled.

| Placement | How it sits | Umbilical routing |
|---|---|---|
| **Desk / side table** | flat on 4 sorbothane feet | hanger clamped to the desk edge or chair back; clip beside the right ear, 100–200 mm out |
| **Chair back** | lid-side hook plate, two 30 mm J-hooks over the top rail + 40 mm cam strap; hangs vertically | hanger clamped to the chair-back top |
| **Couch back** | flat on the cushion on its feet + a 600 mm non-slip strip; strapped if narrow | hanger on the couch frame or case handle |

**Heat:** two 25 mm passive vents with foam baffles on the case ends; idle power held ≤ 26 W (RT2 #18). The PCB and drums sit away from the foam on standoffs.

**Never tug the helmet:** riser from the box to a **3 N magnetic clip** beside the right ear; **≥ 450 mm free loop** from the clip to the right hub; tubes and housings loose in the sleeve, never tied (≤ 0.01 N·m at 60° yaw, leap3-D D3). The ear-axis exit keeps the loop out of the bail's sweep at every α (RT2 #2).

**Breakaway chain (RT2 §11, RT3 2.8):**
1. The **3 N clip** pops first (stand-up, lean-back).
2. The **magnetic pogo lanyard** on the loop wire is the shortest member of the bundle: any further pull separates it first → loop open → rail cut → pins vent (≤ 100 ms), float retracts (≤ 150 ms with the QEV), drums lose power.
3. Tubes and housings are continuous to the pad. The **cradle form lock (≈ 10 N)** is the last fuse; the helmet sheds up and back, away from the face. Every nail is on its 0.25 N breakaway, so a shed helmet does not tear hair.

**At the box:** one latched block (≥ 40 N) holds the three push-fits, the tendon hook block and the GX12. Opening it is the packing operation; every line vents through the de-energised valves.

---

## 7. Safety architecture

**Principle (safety-requirements §5).** Every S ≥ 3 hazard is bounded first by a **mechanical constant**, second by **hardware electrical** means, and only third by firmware. Firmware is never credited alone (red line 13). Klipper and the host are firmware.

### 7.1 Hardware safety loop

```
 24 V adapter ─ F 3.15 A ─┬─► M8P VIN (logic: MCU + CB1, never switched)
                          └─► E-STOP (NC, latching) ─► RELAY COIL chain: HOLD-TO-RUN lever (NO) ─ REFLEX latch (opens on trip)
                                ─ helmet LOOP (lanyard pogo + head-present switch) ─ RAIL-ENABLE MOSFET (gate = watchdog charge pump)
                                ─► force-guided relay K1 (coil)
                          E-STOP (NC) ─► K1 contacts (2 × NO in series) ─► ACT-24 ─┬─► M8P motor-power input (drums)
                                                                                    └─► 12 V buck ─► ACT-12 (+ of valves, pumps)
 K1 NC auxiliary contact + ACT-24 divider → M8P inputs (weld check: rail must fall within 50 ms of every lever release)
 Nothing in the logic domain can energise ACT-24: the M8P only sinks the − side of loads that have no + without the loop.
```

**What de-energises, and the resulting state:**

| Element | De-energised state | Effect at the head | Time |
|---|---|---|---|
| S070 PIN A, PIN B (NC to rail) | line ↔ exhaust | nails vent, force < 0.05 N | ≤ 100 ms (C3) |
| RAIL DUMP (NO) | rail → air | no source even if a PIN valve sticks | ≤ 50 ms |
| PALM 3-way + PALM DUMP (NO) + Airpel leak + QEV | float vents | **spring retracts the pad ≥ 25 mm** | ≤ 150 ms |
| Pumps | off | no supply | immediate |
| Drums (motor power off) | free, cannot drive or reverse | yoke settles by ≤ 1 mm of spring recoil | immediate |
| Halo | unpowered by design | stays where it was put | — |

**Restart rule.** When the rail returns, the host goes to ARMING: drums home on their index with the pad retracted and lines vented; the pad reaches the scalp only through APPROACH (lever held 1 s, palm ramp 0.5 s, first strokes at 0.10 N ramping over 3 strokes). **No resume into contact.**

**Weld and stale-output checks (RT2 #10):** K1 is force-guided; the host refuses ARMING if the rail did not fall within 50 ms of the last lever release. Klipper starts every output at its safe value; the loads have no supply until K1 closes, so start-up is lifted by hardware.

### 7.2 Force caps

| Cap | Mechanism (constant) | Value | Backup |
|---|---|---|---|
| Normal, per nail | R1a (3 psi) / R1b (other make) | 0.80 / 0.92 N | P1 deadhead ≤ 50 kPa → ≤ 1.93 N (measured at A1) |
| Normal, bottomed nail | ≥ 15 mm retract margin (C6) | never bottoms in the 10° tilt case | C6 bottoming test ≤ 1.04 N |
| Normal, total | palm float: R2 / R2b / P3 deadhead ≤ 30 kPa / float relief | ≤ 3.7 / 4.6 / 6.8 N single | float relief poppet bounds a kinked-and-compressed palm line (RT2 #7) |
| Lift-direction pull on any strand | **C1 magnetic breakaway** | ≤ 0.25 N (≤ 0.35 N with tangential) | — (mechanical in every state) |
| Tangential, pad | **magnetic shear coupling** | 2.0 N (≤ 2.5 N) | VREF stepper current ≤ 5 N per cable |
| Tangential, per nail on skin | µ × capped normal | ≤ 0.3 N | — |
| Contact pressure (helmet) | pads ≥ 25 mm, closed-cell, dial ≈ 4 N | ≤ 5 kPa | — |
| Fault energy | moving block + yoke ≈ 47 g at ≤ 0.2 m/s | ≈ 1 mJ (limit 50 mJ) | coupling parts at 2 N |

### 7.3 Dish-gate conditions C1–C8: where each is met

| # | Requirement (ruling) | How v3 meets it | Verified at |
|---|---|---|---|
| **C1** | Axial magnetic nail breakaway 0.12–0.25 N; ≤ 0.35 N with 0.5 N side load; B_min ≥ 3× aged friction; released part one piece, ends radiused ≥ 0.5, red/orange; wiper recloses; replaces the 12 mm reserve | §4.1, M10; pin reserve 1–3.5 mm; no block free-travel | A2 (a, b); B5 (c, d); every session (e): 25 g hang test and nail count |
| **C2** | Profile monotonic tip → nose; wiper land ≥ stroke + 3 | §4.1 nail and wiper; shadowgraph template in the PAD WP | A2 shadowgraph + slip-loop 10/10 + 50 reversal strokes, zero loops |
| **C3** | Accumulator rail-side; PIN valves NC to rail, vent de-energised; B servo downstream of R1a/R1b; vent ≤ 100 ms; Ø 0.15 bleed < 2 kPa in < 1 s | §2.3, C8–C9 | A2 scope trace at a gallery tee; kinked-line bleed; R1 calibration with B at 100 % (≤ 1.04 N per nail) |
| **C4** | Snag reflex: vent A and B, master holds (never reverses), float retracts 10 mm, log, prompt nail check; drag baseline subtracts modelled rim reaction | **v3 implements it as a full fail-to-free** (§1 C22): latch opens the rail → nails vent, drums unpowered (cannot reverse), float retracts fully, host logs and prompts the count. The firmware criterion subtracts the rim model R(d, F) (§8.5). **Deviation:** full retract instead of 10 mm, because Klipper's ≈ 2 s motion queue cannot deliver a fast partial retract; C1 bounds the pull of a full retract at ≤ 0.25 N (ruling S5), so it is at least as safe. | A4 wig tether at centre and rim: trip ≤ 50 ms; 20 min each PLINE, D-paths, CIRCLE with no tether: zero false trips |
| **C5** | Landing band ≤ 35°; lift ≥ 5 mm at worst reserve; lift at ≥ 0.3 v_peak; path checker in every mode rejects reversals inside the no-reversal radius | inner rim 34° (print 33–35°); no-reversal radius **13.7 mm** for the 34° rim; checker in `scorer.py` on every token (§8.3) | A3 240 fps + feelers on R 85, R 65, 70 × 150 mocks; checker unit tests with bad tokens |
| **C6** | Retraction margin ≥ 15 mm (stroke ≈ 18.5) or overtravel spring ≤ 2.0 N | stroke 18.5 mm | calipers at each pin on three mocks; 15 mm block bottoming test ≤ 1.04 N |
| **C7** | Return spring ≥ 2× aged friction; vented nails retract ≥ 8 mm in 200 ms | §4.1 | group B vented, all B nails ≥ 8 mm in 200 ms, new and after a 20 min run |
| **C8** | CAD: nail–skid ≥ 8 mm incl. 5.5° tilt and 8.5 mm rise; fence includes ±17 mm amplitude and tilt; block–deck gap > 3 mm (or booted) and ≥ 30 mm from skin at every pose | skid circle Ø 116, feet ≤ Ø 8, rotated (RT2 #5); CAD WP sweep over (ψ, d, tilt) | CAD sweep report; feeler check on the B-stage pad |

**Recommended, not built (ruling §4):** a palm-line latch making the lift tension present only while the palm is pressurised. Re-evaluate at SP2.

### 7.4 Hair rules applied

| Rule | How SP1 v3 meets it |
|---|---|
| No gaps 0.04–3 mm within 25 mm of the scalp; no changing gaps (H-4.9) | Below 32 mm only shafts (behind zero-gap wipers), cones and static skid stems. Block–deck gap at ≥ 32 mm, > 3 mm (C8). No sleeve, ferrule or neck on the nail. |
| No rotation within 30 mm (red line 1) | Nothing rotates on the pad. Drums are in the box. Hinges are at the hubs, outboard of the head, ≥ 60 mm from the canal. |
| Lift before reversal (H-5.2) | **Geometry**: every nail is ≥ 5 mm clear for |d| ≥ 13.7; the checker forbids reversal inside it (C5). |
| Lift kinematics (H-5.3) | landing at 34°; lift at ≈ 0.78 v_peak |
| Rigid group (H-5.6) | one rigid block; skids static during play |
| Circles (H-5.7) | offset circles cross the rim once per revolution; the offset heading rotates so no patch is circled continuously; centred circles with R + e < 14.5 are rejected |
| Dwell / matting (H-5.5) | station dwell timer: ≤ T_dwell contact-seconds per station (placeholder **90 s**, set by the B-stage wig matting run), then chime and nails stay up until MOVED; a with-grain D-path comb-out every 20 strokes |
| With-grain bias (H-5.1) | D-paths and LINE default with-grain per station (grain entered by hand per station); against-grain strokes ≤ 25 mm |
| Snag reflex (H-5.9, H-6.6) | §8.5; C1 below it |
| Breakaway (H-4.13) | C1 per nail (0.25 N); pad kinematic mount ≈ 6 N; coupling 2 N |
| Static (RT2 #15) | no PTFE in the pile (the PTFE tape is at ≥ 70 mm); POM nails; [VERIFY V19 dry-air test] |
| Cleanability (H-6.7) | pad lifts off its magnets; nails drop out by design (count them); cartridges pull out; wiper skirt plate snaps off for washing |

**Checklist self-score (H-6.8):** ≈ **30/36, no gating zero**, as the ruling scored the dish gate with C1–C8. Items 4 and 7 stay at 1 by design.

### 7.5 The 13 red lines, mapped

| # | Red line | SP1 v3 answer | Verified at |
|---|---|---|---|
| 1 | No exposed rotation within 30 mm; no open slot | nothing rotates on the pad; drums in the box; hinges outboard at the hubs | B gap probe; C wrap test |
| 2 | Per-element normal ≤ 2.5 N by a mechanical constant | R1a 0.80 N, R1b 0.92 N, deadhead ≤ 1.93 N; 18.5 mm stroke prevents bottoming | A1 relief calibration; B2 load cell; C6 test |
| 3 | ≤ 12 N total; ≤ 2 N tangential per element | float caps ≤ 6.8 N at a triple fault; coupling 2.0 N; skin shear ≤ 0.3 N per nail; single-strand tangential snag 0.8–2.0 N for ≤ 50 ms is the ruling's accepted residual (S1) | B2 force audit; coupling release test |
| 4 | NC e-stop in series with motor power + hold-to-run | §7.1: e-stop in series with K1's coil and its contacts; lever is K1's coil feed | A0 loop tests |
| 5 | No mains, ≤ 24 V, no lithium | external certified 24 V adapter; CB1 has no battery | A0 visual |
| 6 | Nothing moving anterior to the hairline, within 25 mm of the canal, above the eyes without a guard | nothing powered moves on the head except the block (±17 mm inside the pad); α stop at the hairline; β stops ±40° keep the pad edge ≥ 30 mm from the canal; the front band is the fixed guard | C4 fence measurement with the halo displaced ±15 mm |
| 7 | No self-locking drive in the force path | force path = air pins + air float + springs; drums are back-drivable and in the tangential path behind a 2 N coupling; halo hinges are friction, back-drivable | B power-pull test |
| 8 | Nothing held in contact after power loss, e-stop, watchdog, stall | §7.1 de-energised table; gallery bleeds; Airpel leak; QEV | B4 fault injection ×10 each |
| 9 | Retention; proof 3× | cone-to-shaft tension proof 3.1 N; compression proof 3.1 N on the magnet face; lateral 3.0 N in the guides; axial tension is the deliberate C1 breakaway (H-4.13), magnet + mechanical pocket as §3.6 allows | B3 per-nail proof |
| 10 | One-handed doff ≤ 3 s; breakaway strap only; ≤ 500 g | no strap; form lock ≈ 10 N; ≈ 286 g; head-present switch; doff §7.7 | C7 timed doffs |
| 11 | Edges ≥ 1 mm (tips ≥ 0.4); tape test | rim R 0.4; shaft tops R 0.5 (dropped-nail case); all other skin-side edges R ≥ 1 | B3 tape test |
| 12 | First session only with the checklist, wig test, glasses, ≤ 5 min | Stage B session entry gate (§10) | B6 |
| 13 | Firmware never the only barrier for S ≥ 3 | every S ≥ 3 row in §7.6 has an M or E control | Safety Gate |

### 7.6 Hazards (safety-requirements §1) mapped

| H | Hazard | Mechanical / electrical control | Firmware layer |
|---|---|---|---|
| H1 | Entanglement | no rotation in the zone; no neck; monotonic cone; wipers; offset-circle rule; coupling 2 N | path checker; dwell timer |
| H2 | Strand pulling | **C1 breakaway ≤ 0.25 N**; geometric lift; comparator latch | reflexd dish-aware trip |
| H3 | Excess normal force | R1a/R1b, deadhead; float R2/R2b/deadhead/float relief | rail clamp 15.6 kPa; Σ F_pins ≤ F_float |
| H4 | Excess shear | magnetic coupling 2 N; VREF | tension trip |
| H5 | Sharp edges | R ≥ 1 skin-side; tape test | — |
| H6 | Pinch | bail/boss gaps ≥ 25 mm or ≤ 4 mm; carriage covered; β stops with bumpers before the bosses | — |
| H7 | Motor stall | VREF current cap; drums behind a 2 N coupling | — |
| H8 | Runaway | block travel bounded by the dish rim and the yoke cage (±18 mm hard); halo unpowered | path limits |
| H9 | Printed part failure | ≥ 4 perimeters / MJF; proof 2× (bail node 10 N, cradle 20 N); inspection log | — |
| H10 | Loose fasteners | inserts + threadlocker; torque marks | — |
| H11 | Broken / dropped tips | POM; proof 3×; red/orange; per-session count; breakaway nails are blunt both ends | nail-count prompt |
| H12 | Abrasion | force caps; finish Ra ≤ 0.8 | dwell timer; ≤ 50 passes/min per spot (precession + chords) |
| H13 | Sustained pad pressure | pads ≥ 25 mm, ≤ 5 kPa; skids ≥ 50 mm² | 20 min session cap |
| H14 | Mains | external certified adapter | — |
| H15 | Shorts / overheating | fuses; sleeved harness; flyback diodes | — |
| H16 | Back-EMF | TVS + 470 µF on ACT-24; SS14 per coil | — |
| H17 | Lithium | none | — |
| H18 | Eyes / ears | front band guard; hairline stop; β stops | — |
| H19 | Failed e-stop | e-stop + hold-to-run + loop + latch + watchdog in series; force-guided relay; weld check | rail-sense → PAUSED |
| H20 | Hygiene | removable pad; drop-out nails; washable skirt plate and sleeve; 10 µm filters | — |
| H21 | Hot parts | no heat source on the head | — |
| H22 | Noise | §4.9 | — |
| H23 | Head-mounting | 286 g; form lock; no strap | — |
| H24 | Cannot remove quickly | §7.7; lever release = vent + retract | — |
| H25 | Firmware faults | everything above holds with Klipper and the host dead (watchdog opens the rail) | Klipper shutdown values |

### 7.7 Doffing (≤ 3 s, one hand, eyes closed)

1. **Release the lever.** Nails vent ≤ 100 ms; pad retracts ≤ 150 ms.
2. **Grab the band's doff lip** (0.5–0.8 s).
3. **Tilt up and back**; the cradle leaves the occipital shelf (≈ 10 N) in ≈ 0.5 s.

If the lever is still held, the head-present switch opens the loop as the forehead pad lifts. **Posture rule (RT2 #12):** sessions in a seat whose headrest is ≥ 120 mm behind the bun, or no headrest; bun stations (α > 75°) are not used reclined. **Gate (C7):** 10 eyes-closed trials ≤ 3 s, max ≤ 2.5 s; lift force at the lip ≤ 20 N.

### 7.8 Failure modes and states

| Failure | Detection | State reached | Bound |
|---|---|---|---|
| PIN valve stuck energised | line sensor at rail with the valve commanded off for > 0.5 s | FAULT (host): opens the latch → rail dead → RAIL DUMP opens | that group ≤ 0.80 N until the dump (≤ 50 ms after rail loss) |
| PIN valve stuck de-energised | no pressure on command | group disabled, logged; play with the other group | benign |
| Pin line kinked, pressurised | blind | gallery bleed < 2 kPa in < 1 s | ≤ 0.80 N, < 1 s |
| Palm line kinked | S_palm with PALM off | Airpel leak + float relief; FAULT; doff | ≤ 6.8 N; float relief bounds compression |
| Cable breaks | tension pattern (one cable → 0) | latch trip → fail-to-free; replace cable | coupling and springs keep the block caged |
| Coupling parts (snag or nuisance) | tension pattern changes | latch trip; re-seat by recentring at ARMING | ≤ 2 N |
| Drum skips steps | index check at every ARMING (> 0.3 mm error → FAULT) | re-home | coupling-capped |
| Klipper shutdown / MCU reset | watchdog PWM stops | rail opens | ≤ 50 ms |
| Host (CB1) hang | watchdog not refreshed → `maximum_mcu_duration` → PWM off | rail opens | ≤ 1 s |
| Power loss | — | all de-energised | free |
| Lanyard pulled / helmet doffed with lever held | loop open | rail cut | — |
| Halo slips on the head | none (no sensor) | fences are mechanical and move with the halo | registration-free by design |
| User falls asleep | lever released → rail off; 20 min session cap | free | — |

---

## 8. Firmware architecture (Klipper + host)

**Split.** Klipper (MCU on the M8P, host process on the CB1) moves the drums and switches valves in sync with motion. Two plain Python services on the CB1 do everything else: **`scorer.py`** (paths, variation, IK, path checker, controls, state machine, logging) streams G-code to Klipper over its API socket; **`reflexd`** reads the cable tensions and can trip the hardware latch. `scratchctl` is the PC/console front end. The safety-relevant ports from v2/05-engineering are kept: one limits table printed at boot, one clamp point, a settings code on every log line, the BLIND / `bset` / `reveal` machinery, the rail-sense → PAUSED rule, and "no restart without an explicit act".

### 8.1 State machine (scorer.py)

```
 BOOT ─► SELFTEST (rail off: sensor zeros, outputs safe, tension baselines, Klipper ready) ─► SAFE
 SAFE ── lever held + rail present ─► ARMING: dumps close, pumps charge rail and palm, lines A/B vented,
         drums home on index (pad retracted), tension trim check, weld check passed
 ARMING ─ ok ─► READY (block parked on the rim, pad retracted)
 READY ─ lever held 1 s ─► APPROACH: PALM on, float extends to skid contact (0.5 s ramp), lines pressurised
         to 0.10 N with the block on the rim, 3 ramp strokes ─► PLAY
 PLAY ⇄ REST (block parked on the rim, nails up, 0.2–3 s)
 PLAY ─ dwell timer spent ─► STATION-WAIT (nails up, chime; lever may be released to move the halo) ─ MOVED ─► APPROACH
 PLAY ─ 20-min cap / 'stop' ─► RETRACT ─► READY
 any ─ rail lost (lever, e-stop, loop, latch, watchdog) ─► PAUSED (hardware already vented) ─ rail back ─► ARMING
 any ─ trip ─► FAULT (host opens the latch; all streams stop; LED 10 Hz; only 'reset' + lever re-press leaves)
```

Because the TMC2209s run standalone (no UART), cutting motor power at every lever release does not make Klipper declare a driver error; the drums simply lose position, and ARMING re-homes them (≈ 2 s). The host stops streaming the instant rail-sense falls and flushes Klipper's queue (`M400`-free: it sends no more moves; Klipper idles out).

**Trips (each → FAULT):** sensor out of band 0.5 s; valve command/sensor mismatch; weld check failed; index error > 0.3 mm; cable tension pattern lost; session > 20 min; Klipper shutdown; reflexd heartbeat lost.

### 8.2 Kinematics: host-side IK on three coordinated axes

**Why not Klipper's winch kinematics.** The Klipper Config Reference states: *"CABLE WINCH SUPPORT IS EXPERIMENTAL. Homing is not implemented on cable winch kinematics."* It models each stepper as the straight distance from a fixed anchor to a point toolhead, with no per-cable dead-band (backlash) compensation and no way to express the block's dish-driven rise (8.5 mm) and tilt (5.5°) — and its forward kinematics (trilateration) is ill-conditioned with three anchors nearly coplanar with the toolhead. It would work for lines (cables reverse on the rim, nails up) but not cleanly for circles.

**Chosen: plain coordinated stepper moves generated host-side.** Klipper's `MANUAL_STEPPER … GCODE_AXIS=<letter>` makes a manual stepper "an extra axis on G1 move commands", moving "synchronously with the associated toolhead xyz movements" (Klipper G-Codes reference). Configuration: `kinematics: none`; `[manual_stepper cable_a]`, `cable_b`, `cable_c` (rotation_distance = π × 12 mm = 37.70 mm, 16 µsteps, `endstop_pin` = the drum Hall index); a start-up macro assigns `GCODE_AXIS=A`, `B`, `C`; `INSTANTANEOUS_CORNER_VELOCITY` raised so that dense segments do not decelerate at every junction [VERIFY V-K1]. `scorer.py` then:

1. plans the block path d(t) for the next ≤ 0.5 s (mode, variation, checker);
2. samples it every 1 mm of path (≤ 200 segments/s at 2 Hz);
3. computes each cable length:
   ℓᵢ = |Aᵢ − (pᵢ(t) + d(t), z(d), tilt(d))| − ℓᵢ⁰, with Aᵢ the deck stop, pᵢ the yoke post (rotating with the block's tilt), z and tilt from the printed dish profile;
4. adds **series-spring feed-forward** ΔTᵢ/k from the modelled drag and rim reaction;
5. adds **per-cable dead-band compensation**: when dℓᵢ/dt changes sign, a smoothed ±bᵢ/2 step spread over 3 mm of path, with bᵢ calibrated per cable at A3 (and as a function of bail pose class if A3 shows > ±30 % variation);
6. streams `G1 A… B… C… F…` with F chosen so each segment's duration matches the plan [VERIFY V-K1 that move timing with only extra axes follows F as expected].

Path error from linear interpolation in cable space between 1 mm samples is < 0.01 mm [EST].

**Fallbacks, in order** (decided at the S0 Klipper test, V-K1):
1. **Stock `[printer] kinematics: winch`** with effective anchors (Aᵢ − pᵢ) given a +20 mm z offset to keep trilateration well conditioned; XY G-code from the host; no dead-band compensation (circles restricted to R ≤ 10 if A3 flats exceed 0.5 mm); homing by `SET_KINEMATIC_POSITION` after the drum index.
2. **A custom `tendon3` kinematics module** (≈ 150 lines of Python + C itersolve callbacks, modelled on `winch.py`) adding the dish z/tilt terms: ≈ 6–10 h for a hired engineer, more for Michael.

### 8.3 Paths, modes and the path checker

**Path primitives** (all in frame S, all planned by `scorer.py`): `line(ψ, A, e)` (e = chord offset), `circle(R, c)`, `dpath(ψ, e)` (contact chord + rim return), `park(θ)`, `turn(Δψ)` (heading change only while |d| ≥ 13.7). PLINE is a sequence of `line` strokes with ψ advancing Δψ per cycle; it is generated stroke by stroke, so stroke length, period and heading are free per stroke (RT1 #1).

**Contact profile:** trapezoidal in path speed: constant v inside |d| ≤ 12.2; accelerate and decelerate in the rim zones; turnaround at |d| = 15–16.5.

**Path checker (C5; runs on every token before it is sent; unit-tested with deliberately bad tokens):**
- reject any velocity reversal, cusp, or heading change > 30° per 50 ms inside **|d| < 13.7 mm**;
- reject landing or lift (crossing |d| = 8.5…12.2) at path speed < 0.3 v_peak;
- reject any segment with |d| > 16.5 mm, v > 200 mm/s, or in-contact acceleration > 2 m/s²;
- CIRCLE: require R + e ≥ 14.5 and R − e ≤ 8.5; require the offset heading to rotate ≥ 15° per revolution; reject centred circles;
- reject any change of group valve state while |d| < 13.7 (group switches only on the rim);
- reject Σ F_pins + 0.45 N > F_float (constant support).

### 8.4 Simple anti-habituation variation (required; DECISION-3 #9)

A seeded random generator draws per stroke (σ values are defaults; all are in the limits table):

| Dimension | Draw | Source |
|---|---|---|
| Stroke length | chord offset e ~ U(0, 7) mm on 40 % of strokes → contact 13–23 mm | RT1 #1 |
| Period | half-stroke duration × N(1, 0.15), clamped ±30 % | RT1 #1 |
| Heading | ±10–30° kick at 30 % of rim turnarounds; precession sign flips with p 0.2 at pauses | RT1 #1 |
| Pauses | 0.2–0.8 s rim park with p 0.08 per stroke; 2–4 s every 30–90 s | RT1 #1 |
| Force | rail per phrase N(F_knob, 0.15 F) clamped [0.20, 0.60] N; slewed on the rim | scratch-model §4.4 |
| Pins | group pattern A / B / A+B changed every 4–12 strokes; B at 0.5–1.0 × rail during contrast phrases | L3-2 |
| Mode texture (MIX) | phrase of 5–20 s: PLINE 50 %, LINE 15 %, CIRCLE 10 %, CHORD 15 %, D-PATH bursts 10 % | — |
| No repeat | no (length, period, heading, group) tuple repeated for > 3 strokes | scratch-model §4.2 |

**Dwell timer (H-5.5):** contact-seconds at the current station; chime at T_dwell (placeholder 90 s, set at B5); MOVED re-arms; MOVED held 2 s = STAY (one extension of 50 %). The timer is firmware (S1–S2 hazard), acceptable alone.

**Controls:** SPEED knob → f 0.6–2.0 Hz (PLINE default 1.4 at mid). INTENSITY knob → F 0.20–0.45 N in Stage B, 0.10–0.50 N after D1 (clamped 0.60 N; relief 0.80 N). MODE → PLINE / LINE / CIRCLE / MIX; a mode change takes effect at the next rim turnaround (≤ 0.5 s).

### 8.5 Snag reflex (C4; three layers)

| Layer | Mechanism | Threshold | Action |
|---|---|---|---|
| **M** | C1 nail breakaway | 0.12–0.25 N axial | nail drops; wiper recloses |
| **M** | yoke coupling | 2.0 N tangential | yoke parts; tension pattern collapses → E layer |
| **E** | LM393 window comparators on each cable's Hall flexure | ΔTᵢ > +1.8 N or < −1.2 N from pretension (above the worst modelled rim load per cable ≈ 1.0 N) [VERIFY zero false trips] | set REFLEX latch → rail dead (= fail-to-free) |
| **F** | `reflexd`: drag vector from three tensions minus the modelled rim reaction R(d, F) and PTFE drag, using the planned d(t) shared by `scorer.py` (timestamp-aligned to Klipper print time ±20 ms) | residual > 0.8 N absolute, or > 0.5 N opposing motion for 60 ms | CB1 GPIO → REFLEX latch; log; prompt a nail count |

**After a trip:** Michael releases the lever (resets the latch), counts the nails (6 present?), presses MOVED or re-holds the lever → ARMING re-homes the drums and recentres the yoke onto the block (magnets re-seat when the yoke passes centre with the pad retracted).

### 8.6 Commands (`scratchctl`, network console on the CB1)

| Group | Commands |
|---|---|
| State | `status` `limits` `arm` `play` `rest` `stop` `retract` `reset` |
| Drive | `mode pline\|line\|circle\|mix` `f <Hz>` `amp <mm>` `dpsi <deg>` `psi <deg>` `R <mm>` `e <mm>` `chord on\|off` `dpath <n>` `park` |
| Force | `force <N>` `sF <0..0.3>` `groups a\|b\|ab\|auto` `bratio <0.5..1>` `palm <kPa>\|auto` |
| Variation | `vary on\|off` `seed <n>` `dwell <s>` |
| Calibrate | `cal drums` (index, trim) `cal deadband` (per-cable b) `cal rim` (rim-reaction model from a no-contact sweep) `cal lines` (vent timing) |
| Experiment | `bset <slot> <json>` `blind <n>` `next` `reveal` `rate <0-10>` |
| Diagnostics (pad retracted only) | `valve <a\|b\|palm> <ms>` `sensors` `tensions` `pump <n> <duty>` |
| Fault injection (wig head only) | `inject snag\|hang\|cable\|stuckvalve` |

**Logs** (CSV; first field is a letter; t in ms): `H` 1 Hz health; `B` per stroke (mode, ψ, e, f, groups, rail, peak residual drag); `T` tensions at 100 Hz (optional); `E` events (controls, MOVED, station timer); `F` faults; `C` settings behind a code; `S` session marks and ratings. To the CB1's SD card and to the PC.

---

## 9. Pad-2 provisions (parts not bought)

**Twin concept (unchanged):** pad 2 rides the right half-bail at (−α, −β) (point mirror); its nails tee onto lines A and B (lockstep); its three cables run on the second groove of each drum (same ℓᵢ, no extra motors); its own palm line and float. Collision: mechanical twin stop at |β| ≥ 36° near the vertex (RT2 #4), plus pad-2 palm interlock (a parked pad 2 must not extend its nails).

| Provision built now | Where |
|---|---|
| Bail vertex node bolted (2 × M3) so the half-bails can separate | HALO |
| Right hub boss: second-hinge seat (M2 pattern), umbilical bore sized for two harnesses | HALO |
| Drums double-grooved; stop plate has six housing seats | DRIVE BOX |
| Tee ports on lines A and B and a PALM B outlet, capped | DRIVE BOX |
| M8P outputs reserved: PALM B valve, PALM B dump; one TH input for S_palm B; ADS1115 has a fourth channel | ELECTRONICS |
| Firmware: `twin on` stub (palm B, Σ-force per pad, twin stop check) | FIRMWARE |
| Twin relief note: per-pad palm R2/R2b at 15/16 kPa, palm deadhead ≤ 25 kPa → ≤ 11.9 N total at a double fault | DRIVE BOX |
| Twin mass budget ≈ 440 g (§4.8) | — |

**Install later (≈ one weekend + ≈ $170 of parts [EST]):** build pad 2 and carriage 2 from the same files (mirrored where marked); second hinge; split the vertex; run harness B through the right bore; three more cables on groove 2; unblank the tees and PALM B; set twin reliefs; force audit ≤ 12 N; mass ≤ 480 g measured; collision test at the vertex.

---

## 10. Build staging with go/no-go gates

Assumes ≈ 11 focused hours per weekend. **Every stage ends with a sensation data point on Michael's head.** The next cart is bought only on GO. Hours include the 1.5× first-timer factor.

### Stage S0 — week 1 (≈ 12–16 h, ≈ $420 Day-0 cart)

| Build | Gate (pass line) | Sensation data point |
|---|---|---|
| Tape fit of Michael's head (V1); $20 bike helmet + UltAlt dial + two Southco E6 hinges + stick bail + coin bag (E4 test) | holds at α 0/45/90° for 20 min of TV; re-index eyes-closed < 3 s; cradle lean ≤ 3/10 | "having to move it" ≤ 3/10 |
| **Dish bench** (leap4-A (e)): Ø 70 printed deck with dish (34°/50°), block on 3 POM domes, 3 drafted cones on syringes from one pump + relief + bleed, on a paper-covered Ø 170 ball (R 85) and a 70 × 150 side mock; driven by hand through templates | chords ≥ 15 mm; lift ≥ 5 mm everywhere; landing ≤ 35°; spread ≥ 20 ms (240 fps) | **helper holds it on Michael's crown: "scratch, not brush", "crisp on both flanks", ≥ 6/10** |
| **Klipper test** (leap4-E (e)): Klipper on a $5 Pico + CB1 or a Linux VM; three steppers (Day-0) as `GCODE_AXIS` A/B/C; streamed PLINE in cable space; an LED as a valve on SET_PIN | V-K1: G1 A/B/C timing follows F; no stutter at 200 segments/s; SET_PIN edges within ±2 ms of the path point over 500 strokes | — |
| **Tendon ink rig** (leap4-D (e)): three drums, 1.6 m cables in two housing types, pen plate on marbles + PP hinge, earplug A/B with the deck taped to the bike helmet | bow ≤ 0.5 mm; circle flats ≤ 0.3 mm after compensation; shrink ≤ 0.5 mm at 0.5 N; drift ≤ 0.5 mm across housing coils; earplugs: indistinguishable on/off | earplug A/B on Michael |

**GO S0:** all four pass. **NO-GO:** dish fails → fall back to leap4-A L1 (one valve, collars) on the same box; tendon fails → keep tendons for lines only and restrict circles, or revisit; Klipper fails → fallback 1 kinematics (§8.2).

### Stage A — bench puppet (3–4 weekends, ≈ 40–55 h, Cart 2 ≈ $520)

| Step | Build | Gate |
|---|---|---|
| A0 | Safety loop on a board: adapter, e-stop puck, lever + K1, latch, comparator, watchdog, loop jumper + head-present switch, rail sense | each element opens ACT-24 within 5 ms (logic analyser), logic stays up; weld check fires on a jumpered K1; 10 cycles each |
| A1 | Pneumatics: P1 + 250 ml + R1a/R1b; P3 + R2/R2b; sensors; dumps; filters | R1a 20.7 ± 1.5, R1b ≈ 24 ± 1.5, R2, R2b (5 trials each); **deadheads measured** (P1 ≤ 50, P3 ≤ 30 kPa); rail PID ±0.5 kPa |
| A2 | Six pins in an SLA bench block on the real gallery A/B, lines, S070s, breakaway magnets | C1 (a)(b); C2 shadowgraph + slip loop; C3 scope trace ≤ 100 ms, bleed < 1 s, relief with B at 100 % ≤ 1.04 N; C6 calipers; C7 retract ≥ 8 mm in 200 ms; force at 10 kPa = 0.385 ± 0.04 N net of spring |
| A3 | Drum module in the box layout + three tendons + the real pad deck with dish, block, yoke, coupling on the R 85 ball | ink rosette: PLINE never retraces within 2 mm in 60 s; LINE bow ≤ 0.5 mm; offset circle flats ≤ 0.3 mm; rim reaction measured (V-D1); coupling: zero nuisance releases in 20 min each mode at 2.0 N; C5 240 fps on R 85 / R 65 / side mock; checker unit tests |
| A4 | reflexd + comparator on the wig tether | C4: trip ≤ 50 ms at centre and rim; 20 min PLINE, D-paths, CIRCLE without tether: zero false trips |
| A5 | Everything into the Apache case | ≤ 30 dBA at 1 m; ≤ 2.8 kg; runs on its back, side and face |

**Sensation data point:** the bench pad, hand-held by a helper on Michael's crown and occiput (pad retracted float bypassed, skids on the scalp), PLINE vs LINE vs CIRCLE vs MIX, blind: **≥ 6/10 "as satisfying as a good scratch", "scratch not brush" in ≥ 6/8 headings.**
**GO A:** all gates + ≥ 6/10. **NO-GO:** sensation < 6/10 → tip, force and variation A/B before any halo work.

### Stage B — pad on a fixed-pose halo, first sessions (3–4 weekends, ≈ 40–55 h, Cart 3 ≈ $300)

Build: complete pad (RCC, skids Ø 116, cover, kinematic mount), Airpel float + QEV + float relief; carriage; **halo with carbon band, dial cradle, hub bosses with hinges, carbon polygon bail** (this is the SP1 halo); umbilical with the ear-axis exit, lanyard and clip; JLC3DP production batch for frozen parts.

| Step | Gate |
|---|---|
| B1 Mass | pad ≤ 90 g; moving group ≤ 125 g; helmet ≤ 320 g |
| B2 Force audit | all six nails at R1a + palm at R2 on a load cell under a foam dome: total ≤ 12 N (expect ≤ 4.6); one nail ≤ 0.92 N; tangential pull at the coupling 2.0 ± 0.3 N |
| B3 Proof | each nail: cone-to-shaft 3.1 N tension; 3.1 N compression; 3.0 N lateral in guides; kinematic mount 6 ± 2 N; tape test |
| B4 Fail-to-free | power pull ×10, lanyard pull ×10, latch trip ×10, `hang` ×5: pad ≥ 25 mm retracted in ≤ 150 ms (240 fps), no nail in contact |
| B5 Hair | real-hair wig 3–5 cm and long + Kanekalon: 20 min PLINE + 5 min CIRCLE + 5 min LINE + 5 min D-paths: zero wraps, captures, knots; shed ≤ 2× combing; **C1 (c)(d) rim-snag tether ≤ 0.30 N peak, ≤ 20 ms above 0.15 N**; **matting run sets T_dwell** |
| B6 Session entry | safety checklist signed, glasses, e-stop under the free thumb, ≤ 5 min |

**Sensation data point (the hypothesis, fixed poses):** 2 → 5 → 10 → 20 min sessions on Michael's head at 3–6 stations (vertex, upper occiput, both parietals), moving the halo by hand between bouts. **GO B: ≥ 7/10 "as satisfying as being scratched well", "machine on my head" ≤ 3/10, zero pulls, nail count intact every session.** NO-GO: < 5/10 → fix pad (cone, force, variation) before Stage C; 5–6/10 → Stage D experiment matrix first.

### Stage C — finish and wearability (1–2 weekends, ≈ 12–18 h, Cart 4 ≈ $60)

| Step | Gate |
|---|---|
| C1 Fit | cradle seats under the shelf; bun free ≥ 60 mm above the cradle edge; 20 min no mark beyond 10 min; mechanical α/β stops set from Michael's hairline and ears |
| C2 Mass | helmet ≤ 320 g measured |
| C3 Lean | coin bag at the pad pose, moved every 2 min for 20 min of TV: lean ≤ 2/10, slip ≤ 3° |
| C4 Fences | ear ≥ 25 mm (expect ≥ 30) and hairline guard verified with the halo displaced ±15 mm |
| C5 Noise | at the tragus within 3 dB of room level with pins up; earplug A/B indistinguishable |
| C6 Umbilical | head share ≤ 15 g; yaw torque at ±60° ≤ 0.02 N·m; clip pops at 3 ± 1 N; lanyard parts before any tube is taut; stand-up ×5 |
| C7 Doff | 10 eyes-closed trials ≤ 3 s (max ≤ 2.5 s) |
| C8 Whole-system wig | 20 min MIX with station moves: B5 pass lines again |

**Sensation data point:** a 20-minute MIX session with ≥ 4 station moves: "does the hat move?" ≤ 2/10; "having to move it" ≤ 3/10.

### Stage D — sessions and the experiment matrix (ongoing, ≈ 10–20 h)

D1–D4: 20-minute evenings with the armrest switch (RT1 #10). D5 blind matrix (≤ 1 variable per block): PLINE vs MIX; F 0.2 / 0.3 / 0.45 N; variation on/off; B-contrast on/off; chords on/off; D-paths on/off; stations moved by Michael vs by a helper.
**Go/no-go D (SP1 hypothesis, amended north star):** ≥ 7/10 "as satisfying as being scratched well"; "machine on my head" ≤ 3/10; wants it again tomorrow; zero tuft pulls over 5 sessions. Then, on evidence: powered drift (leap4-C C2 box-driven cables, ≈ 15–25 h) if "having to move it" > 3/10; pad 2 if lean is felt.

**Hours roll-up [EST]:** S0 12–16 · A 40–55 · B 40–55 · C 12–18 · D 10–20 · rework allowance 0–10 → **≈ 115–175 h (central ≈ 140)**, ≈ 11–16 weekends to the Stage B hypothesis session.

---

## 11. Work packages

| WP | Scope | Inputs | Outputs | Owns interfaces |
|---|---|---|---|---|
| **HALO** | carbon band, forehead pad + head-present switch, dial cradle adaptation, temple pads, hub bosses (hinges, detent, stops, hollow right bore), carbon polygon bail + nodes + track strip, carriage (rollers, detent, friction, stops), float mount, harness clip track, umbilical clip, zero gauge | §3, §4.7–4.8, §5.1; Michael's tape fit | drawings; node bonding procedure; hinge torque check; mass ledger by part; stop-setting procedure | M1–M8 (ball side), M15, M18 (bail/boss) |
| **PAD** | dish deck (profile, tape), skids, RCC, cover, pin block with galleries and bleeds, pin cartridge (Penrose, piston, magnet, guides, wiper, spring), nail (cone + shaft), yoke + coupling, series springs, deck stops, PP parallelogram, lift spring, kinematic grooves, wiper skirt plate | §4.1–4.2, §7.3–7.4, ruling C1–C8 | drawings; nail shadowgraph template; breakaway calibration procedure; C8 CAD sweep (with CAD); hair self-score | M8 (grooves)–M14 |
| **DRIVE BOX** | drum module (drums, index, stop plate, flexures, tensioner), pneumatics (pumps, accumulators, reliefs, valves, dumps, filters, mufflers, manifolds), case fit-out, mounts, umbilical build, box-end latched block, hanger | §2.3–2.4, §4.3–4.4, §5.2–5.3, §6 | layout; final schematics; relief and deadhead procedure; umbilical build sheet; portability test | M16–M17, A/B/P lines, T1–T4 |
| **ELECTRONICS + FIRMWARE** | safety loop (K1, latch, comparators, watchdog, weld check), M8P wiring (low-side loads, flyback, motor-power input), ADS1115 + Halls, hand controller, e-stop puck; Klipper config; `scorer.py`, `reflexd`, `scratchctl` | §5.4–5.5, §7.1, §8 | wiring table; `printer.cfg`; repo `firmware/sp1v3/` (Python 3, unit tests for the IK and the path checker); bring-up procedure; limits table | E1–E12, the control map, the score format |
| **TEST PROTOCOLS** | S0–D procedures and data sheets; safety checklist for v3; hair bench incl. C1 tether rig; feedback form; blind matrix | §10, §7 | test-protocols-v3.md; log templates; pass/fail sheets | gate definitions |
| **CAD** | OpenSCAD/Fusion models of every part; assembly on the head ellipsoid; C8 sweep over (ψ, d, tilt) and all stations; interference with the bosses at β ±40°; STL + JLC3DP files | all WPs; this spec's datums | `cad/sp1v3/`, CONFLICTS.md | geometric consistency of M1–M18 |
| **BOM** | live-verified BOM by WP and stage; carts S0/A/B/C; substitutes; [VERIFY] closures for parts | §13 | bom-sp1v3.md; Day-0 cart | cost |

**Sequencing:** Day 0 BOM places the S0 cart; DRIVE BOX + ELECTRONICS start with the S0 Klipper and tendon rigs; PAD starts with the dish bench and one SLA cartridge order (10-day lead); HALO starts after the tape fit; CAD runs alongside. If a hired engineer is engaged (open item, 13-outsourcing), this table is their statement of work; ELECTRONICS + FIRMWARE and PAD are the two packages most worth buying.

---

## 12. Risks and open items

### 12.1 Risks, each with the bench test that retires it

| # | Risk | P [JUDG] | Consequence | Retiring test | Fallback |
|---|---|---|---|---|---|
| R1 | **Dish gate on a real head:** reserves, side anisotropy (2.2–2.9 mm) and Michael's pile leave nails skimming or not lifting 5 mm; rim reaction higher than modelled | 0.30 | weak or uneven scratch; nuisance coupling releases | S0 dish bench on R 85/R 65/side mocks; A3 rim-reaction and 240 fps | region-keyed second dish; outer rim 45°; coupling to 2.5 N; leap4-A L1 |
| R2 | **Tendon puppet:** dead band varies with pose > ±30 %, cable creak in 1–4 kHz, fray at drum or crimp | 0.25 | circle flats, audible creak, cable changes | S0 ink rig + earplug A/B; 10⁵-stroke cable-life rig at A3 | PTFE-lined bike housing; circles R ≤ 10; 1 N/mm springs; box gimbal motors (+$100) |
| R3 | **Breakaway and snag reflex:** C1 nuisance releases on vents/rim; rim-snag peak > 0.30 N; false reflex trips break sessions (RT1 #11) | 0.25 | dropped nails; flinches | A2 C1 (a)(b); B5 C1 (c)(d); A4 zero-false-trip runs | adjust magnet gap (shim); raise comparator thresholds; firmware criterion only as advisory |
| R4 | **Hand-moved stations break the spell** or the wig sets T_dwell < 60 s | 0.30 | G5/G4 drop; P(on-par) −0.05 | S0 hinge evening; B sessions ("having to move it" ≤ 3/10); B5 matting run | box-driven α cable travel (leap4-C C2, +15–25 h, +$70) |
| R5 | **Klipper integration:** GCODE_AXIS timing/stutter at 200 segments/s; queue latency; standalone TMC current set by VREF only; M8P motor-power input wiring | 0.20 | jerky strokes; slow controls | S0 Klipper test (V-K1, V-K2); A0 | fallback 1 winch kinematics; fallback 2 `tendon3` module |
| R6 | **Force budget:** Airpel E16 limits Σ pins ≈ 2.2 N; scratch "not hard enough" at all-six | 0.20 | G1 drop | B2 audit + B sessions | Airpel E24 (+15 g) |
| R7 | **Penrose sleeve life / pin friction drift** (C7) and sebum in guides | 0.20 | slow retract, nuisance releases | 10⁵-cycle sleeve rig with the group-vent cycle (A2); C7 after 20 min | nitrile cot sleeves; wiper skirt plate weekly |
| R8 | **Lean felt** (0.27 N·m) | 0.30 | "machine on my head" | C3 coin test; D question | bring pad 2 forward (+150 g, legal) |
| R9 | **Box mass/heat** > 2.8 kg or +20 K on a cushion | 0.20 | portability complaint | A5 weigh; 1 h thermal log | custom ply box (−0.8 kg, +6 h) |
| R10 | **Hours and parts creep** (ledgers on this project run low; RT3 found +20 %) | 0.35 | delay | staged carts; S0 gates | the build-route decision (DIY vs hired) |

### 12.2 Every remaining [VERIFY]

| # | Item | Closed by |
|---|---|---|
| V1 | Design-head dimensions vs Michael's tape fit | S0 (HALO) |
| V2 | S070C-6DC-32: 12 V, 0.5 W, barb Ø 3.18/Ø 2 — **closed** ($35, 1,723 in stock, checked 2026-10-02) | — |
| V4 | Penrose sleeve life ≥ 10⁵ group-vent cycles | A2 rig |
| V9 | McMaster 4277T51 (3 psi) repeatability ±1.5 kPa; R1b/R2b make, setpoint and price | A1, BOM |
| V12 | Pump deadheads: P1 ≤ 50 kPa, P3 ≤ 30 kPa for the parts bought | A1 |
| V15 | Cradle override ≈ 10 N and pitch hold ≥ 1 N·m | S0 / C1 |
| V17 | Mass ledger: pad ≤ 90 g, helmet ≤ 320 g | B1, C2 |
| V18 | Coverage ≈ 85 % and fences on Michael's head | C4 |
| V19 | POM static at < 40 % RH | B5 |
| V-N1 | Nail: hook + epoxy cone joint passes 3.1 N tension; profile per template | A2 / B3 |
| V-N2 | C1 magnet release 0.12–0.25 N with Ø 3 × 2 N52 on a Ø 1.0 A228 flat end (gap shim set per pin) | A2 |
| V-D1 | Rim reaction ≤ 1.3 N inner / ≤ 0.8 N outer; total < coupling with margin ≥ 1.25 | A3 |
| V-D2 | Lift ≥ 5 mm at worst reserve; landing ≤ 35°; spread ≥ 20 ms | S0, A3 |
| V-D3 | PTFE-on-POM dome stick-slip silent at 140 mm/s (phone accelerometer) | S0, A3 |
| V-P1 | Gallery vent ≤ 100 ms through 1.6 m 1/8 in PU and the S070 exhaust | A2 |
| V-P2 | Airpel E16D2.0N bore (≈ 16 mm), stroke, mass ≤ 16 g, leak rate; QEV retract ≤ 150 ms | B4 |
| V-T1 | Tendon stiffness ≥ 1.7 N/mm at the block; shrink ≤ 0.3 mm at 0.5 N | A3 |
| V-T2 | Dead band per cable and its variation with bail pose ≤ ±30 % | S0 / A3 |
| V-T3 | No audible creak with earplugs | S0 |
| V-T4 | Cable and crimp life ≥ 50 sessions (10⁵-stroke rig) | A3 |
| V-T5 | Hall flexure tension resolution ≤ 0.2 N at 280 Hz | A3 |
| V-T6 | Drum index repeatability ≤ 0.1 mm of cable | A3 |
| V-K1 | Klipper `GCODE_AXIS` moves with `kinematics: none`: timing follows F, no junction stalls at 200 segments/s with a raised instantaneous corner velocity | S0 |
| V-K2 | Host throttle keeps ≤ 0.5 s queued without underrun pauses | S0 |
| V-K3 | `maximum_mcu_duration` watchdog behaviour on host loss | A0 |
| V-E1 | M8P V2.0 driver supply: separate motor-power input at 24 V, selectable by jumper (BTT wiki lists "Driver Input Voltage: 24V, HV (24–60V) Selectable") | A0 |
| V-E2 | M8P low-side outputs with load + on a separate 12 V rail (common ground; flyback per coil) | A0 |
| V-E3 | ADC count: 4 pressures + 2 pots + MODE on M8P TH inputs / ADS1115 spare | A0 |
| V-E4 | CB1 GPIO and I²C reachable on the M8P V2 header | A0 |
| V-H1 | Southco E6-10-101-20 torque ≈ 0.25 N·m and mass; leaf screw pattern | S0 |
| V-H2 | Carbon polygon bail ≤ 40 g, vertex drop ≤ 0.5 mm under 100 g; track strip holds at nodes | B (HALO) |
| V-B1 | Box ≤ 2.8 kg, ≤ 30 dBA, ≤ +20 K after 1 h | A5 |
| V24 | All prices in §13 | BOM |

---

## 13. Cost roll-up

**Scope:** one-pad SP1 v3; pad-2 parts **not** bought; tools, printer and bench kit excluded (as v2). Prices are 2026 US retail; **[L]** = live-checked 2026-10-02 (here or in leap4-E / RT3 that day), others [EST ±15 %].

| Group | Main lines | $ |
|---|---|---|
| **Controller + electronics** | BTT Manta M8P V2.0 + CB1 ≈ 155 [L leap4-E $154.59; the BIQU bundle page shows configurations from $84.38 today, VERIFY the M8P + CB1 option]; TMC2209 × 4 @ 7.89 = 32 [L]; 24 V 60 W certified adapter 30; 12 V 5 A buck 10; force-guided relay + latch + LM393 + charge pump 15; e-stop puck 15; hand controller (lever, 2 pots, 4-pos switch, button, GX12, lead) 20; ADS1115 + 3 Halls 12; head-present switch, magnetic pogo lanyard 11; fuses, TVS, diodes, Wago, wire 20 | **340** |
| **Puppet master** | 3 × 17HS08-1004S @ 7.99 = 24 [L RT3]; coated 7×7 wire 8; PTFE-lined coil housing 35; crimps/ferrules 8; series springs 6; coupling magnets 8; drum bearings and rods 10; tensioner spring 3 | **102** |
| **Pneumatics** | 2 × S070C-6DC-32 @ 35 = 70 [L]; PALM 3-way (uxcell 2-pack) 14; 2 NO dumps 15; 2 pumps 30; reliefs: 2 × McMaster 4277T51 ≈ 16 + 2 diverse ≈ 30; 4 × XGZP6847A @ 5 = 20; QEV + float relief 14; filters, mufflers, needles 24; push-fits, tees, manifolds 30; PU 1/8 in 16; accumulator 3 | **282** |
| **Pad** | Airpel E16D2.0N 45 [L RT3 $32–50]; Penrose 1/4 in pack 15; Ø 3 × 2 magnets 6; A228 wire, POM rod, bushes 20; PTFE tape 8; springs assortment 10; PP sheet, balls, kinematic magnets 12 | **116** |
| **Helmet** | bike helmet 20 + UltAlt dial 12; carbon 8 × 6 tube 2 m 25; carbon strips (track + band) 15; 2 × Southco E6-10-101-20 ≈ 11 each = 22 [L: $5.70–10.92 single units]; detent balls/springs 5; rollers, carriage hardware 8; foam, sleeve, TPU pads 12 | **119** |
| **Box** | Apache 2800 29.99 [L]; foam, sorbothane, hook plate, strap, latches, vents 35 | **65** |
| **Umbilical + hanger** | knit sleeve 5; 4-core cable 5; box-end latched block 10; hanger rod, clamp, 3 N clip 15 | **35** |
| **Printing + consumables** | JLC3DP SLA cartridges/drums + MJF nodes/hubs/carriage/deck batch 80–140 + DHL 25 [L E3: SLA from $0.30, MJF from $1; batch EST]; PETG/TPU 46; inserts, fasteners, epoxy, CA 60 | **≈ 240** |
| **Shipping** (≈ 8 vendors) | | **≈ 60** |
| **Total** | | **≈ $1,360** (range ≈ $1,250–1,420) |

**Staged cash:** S0 Day-0 ≈ $420 (steppers, drivers, Pico/CB1 bundle, hinges, helmet + dial, dish-bench parts, cable and housings, one S070, one SLA order); Cart 2 after S0 ≈ $520; Cart 3 after A ≈ $300; Cart 4 after B ≈ $60. **Tools** ≈ $185 (RT3 list: soldering, calipers, scales, logic analyser, tube cutter) + a printer if none ($299–349). **Pad 2 later** ≈ $170.

**Against the inputs:** decision-analysis baseline ≈ $1,450–1,500 including pad-2 parts (≈ $120); leap4-A L3-2 −$115…−275; leap4-D −$70…−100; leap4-E E1 +$75–95, E3 +$80–140, E4 −$130. This bottom-up figure is ≈ $100–200 above a straight sum of those deltas because it carries the 24 V supply, the relay/latch/comparator, diverse reliefs, the float QEV and relief, and realistic consumables.

---

## 14. Change control, decisions for Michael, next actions

- This file is **design freeze v3**. Work packages build to it. Deviations go to a numbered ADDENDUM in 12-sp1v2/, never silently into this file.

**Decisions taken in this freeze that Michael should know about:**
1. **No XY stage; the drums are the master** (Director ruling).
2. **Klipper drives the drums as three coordinated G-code axes with the geometry computed on the CB1**, not with Klipper's experimental cable-winch kinematics (no homing, no backlash compensation, no dish rise/tilt). Two fallbacks are defined (§8.2).
3. **Snag reflex = full fail-to-free** (vent, drums unpowered, float fully retracted) instead of the ruling's "retract 10 mm", because Klipper's ≈ 2 s motion queue cannot do a fast partial; C1 keeps any pull ≤ 0.25 N, so it is at least as safe.
4. **24 V supply** and **TMC2209s in standalone mode with a VREF current cap**, so the safety loop cuts motor power without Klipper shutting down.
5. **Two small controls added:** a 4-position MODE selector and a MOVED button (≈ $6), so modes switch at any moment and the station dwell timer can be re-armed.
6. **Dish rims:** inner 34° (ruling C5), outer softened 65° → 50° to keep the rim reaction under the **2.0 N tangential coupling** (allowed up to 2.5 N only if nuisance releases appear).
7. **Nail cap 0.80 N** (bought 3 psi reliefs), **pin stroke 18.5 mm** (C6).
8. **Float force budget:** the Airpel E16 float limits the six nails to ≈ 0.37 N each when all are down; E24 is the fallback.
9. **Drive box ≈ 2.6–2.8 kg** in the bought Apache case (v2 target was 2.5 kg).
10. Coverage is quoted at **≈ 85 %**, not 90 %, because β is stopped at ±40° (RT2's hub collision).

**Still open (not architecture):** who builds (DIY vs hired engineer + local builder; budget ceiling, date, drive distance, apartment access).

**Immediate next actions (Director):** place the S0 cart; launch the seven WPs of §11 (HALO after the tape fit); run the four S0 rigs before Cart 2; update the sp1-puppet-halo overview page to v3.

### Sources checked for this freeze (2026-10-02)
- Klipper Config Reference, cable winch kinematics ("CABLE WINCH SUPPORT IS EXPERIMENTAL. Homing is not implemented…"): https://www.klipper3d.org/Config_Reference.html
- Klipper G-Codes, `MANUAL_STEPPER … GCODE_AXIS` (extra axis on G1, synchronous with toolhead moves): https://www.klipper3d.org/G-Codes.html
- BTT Manta M8P V2.0 wiki (VIN 12/24 V; driver input "24V, HV (24–60V) Selectable"; 8 driver sockets; HE0–3, HB, 7 PWM fans, 5 thermistor inputs): https://global.bttwiki.com/M8P-V2_0.html
- BIQU Manta M8P bundle page: https://biqu.equipment/products/bigtreetech-stealthy-hi-speed-solution
- SMC S070C-6DC-32, $35.00, factory stock 1,723, 12 VDC, 0.5 W: https://automationdistribution.com/s070c-6dc-32/
- Harbor Freight Apache 2800, $29.99, inside 11-7/8 × 9 × 5-5/16 in, outside 13-1/2 × 11-3/8 × 6 in: https://www.harborfreight.com/2800-weatherproof-protective-case-medium-black-64551.html
- Southco E6-10-101-20 single-unit prices $5.70–10.92: https://americas.bossard.com/products/e6-10-101-20-by-southco.html, https://shop.southco.com/en_us/e6-10-101-20
- Other prices carried from leap4-E and redteam-3 (checked 2026-10-02 there).
