# PROJECT SCRATCH — SP1 Safety Requirements (independent safety track)

**Author:** Safety Engineer (independent of mechanism design)
**Date:** 2026-10-01
**Status:** v1 — governs all candidate mechanisms; to be re-reviewed at the Safety Gate (brief §22) against the selected architecture.
**Scope:** one person (Michael) building and self-testing in an apartment. This is not a medical-device or consumer-product compliance document; it borrows numbers from IEC 60601-1, ISO/TS 15066, ISO 13854, UL 1439 as *engineering references*, not as certification targets.

**Governing stance (brief §9):** safety comes from *mechanical constants* (springs, stops, clutches, geometry, a wire that physically opens) first, electrical limits second, firmware last; nothing here is satisfied by a software flag alone. The device must still scratch properly: a "high" human scratch is ~1.6 N per finger, and the limits below keep everything a good scratch does inside the envelope and everything that injures outside it.

Legend: **[SRC]** sourced value · **[EST]** engineering estimate (no direct source; stated reasoning) · S = severity 1–5 (1 nuisance, 2 minor/reversible, 3 first-aid injury or hair-loss patch, 4 medical attention / eye injury / laceration / scalp avulsion, 5 permanent injury, fire, shock) · L = likelihood 1–5 *without controls* (1 remote … 5 expected in normal use).

---

## 1. Hazard analysis (preliminary hazard list / mini-FMEA)

| # | Hazard | Cause | Effect | S | L | Required controls (M = mechanical, E = electrical, F = firmware, P = procedural) |
|---|---|---|---|---|---|---|
| H1 | **Hair entanglement / wind-up** | Exposed rotating shaft, gear, pulley, or orbital element near hair; hair enters a gap >0.1 mm at a joint | Tuft captured, wound, pulled to scalp; worst case scalp avulsion or large patch loss | 4 | 4 | M: **no exposed continuous rotation within 30 mm of hair** — rotation only inside sealed housings; all joints near hair sealed (boots/bellows/lip seals) or gap-free; reciprocating elements through closed guards not open slots. M: magnetic/breakaway coupling so a wound tuft stalls and releases rather than winds. E: stall current cut-off <300 ms. P: hair-tie / wig-head entanglement test before human test. |
| H2 | **Hair pulling (strand capture by a tip)** | Tip geometry with hooks, notches, slots, or a side edge that catches a strand; direction reversal while a strand is wrapped | Single-hair pluck (nuisance at 0.5–0.9 N) through to painful tuft pull | 2–3 | 4 | M: tips are convex, slot-free, polished; no re-entrant features; tangential compliance so a tip lifts/deflects before load exceeds ~1.5 N; tip retracts (lift-off) before direction reversal where the mechanism allows. P: hair-pull count logged per session. |
| H3 | **Excessive normal force** | Actuator stall torque transmitted to tip; user leans in; misalignment; fit for bigger head | Pain, bruising, pressure injury; with sharp tip, laceration | 3 | 4 | M: **force cap as a mechanical constant** (spring + stop, §3.1) ≤2.5 N per element, ≤12 N total; back-drivable approach axis. E: driver current limit. F: current-based stall detection as backup. |
| H4 | **Excessive shear / tangential force** | Tip digs in; high friction tip material; stroke driven by stiff position-controlled servo | Abrasion, scratch wound, hair pulled | 3 | 3 | M: tangential compliance or slip clutch ≤2 N per element; tip edge radius ≥0.4 mm; stroke driven through compliant linkage. E: current limit on stroke actuator. |
| H5 | **Sharp edges** (tips, guard edges, printed layer burrs, screw ends) | Sharp print edges, exposed fastener tips, broken tip | Cuts, abrasion | 3 | 3 | M: all skin-accessible edges radius ≥1.0 mm; tips ≥0.4 mm edge radius and polished; no fastener protrudes toward skin; UL 1439-style tape test (§6). |
| H6 | **Pinch points** | Linkages, levers, slider/carriage, hinge of head mount | Finger/ear/skin pinch | 2–3 | 3 | M: gaps are either <4 mm (finger-safe) or >25 mm (ISO 13854 finger value); linkages covered; nothing closing onto the ear. |
| H7 | **Motor stall** | Tip snagged, hair wrapped, mechanism jammed | Overheating driver/motor, force builds to stall torque, burn | 3 | 4 | M: stall torque made irrelevant by H3/H4 caps. E: driver with hardware current limit; stall → power cut via current sense in <300 ms. F: motion-timeout. |
| H8 | **Runaway actuation** | Firmware bug, PWM glitch, servo loses signal and slews, controller reset mid-motion | Full-speed/stroke excursion into scalp or eye region | 4 | 2 | M: travel stops on every axis set at the safe envelope; force cap. E: hardware watchdog resets driver enable low; hold-to-run contact for first tests; e-stop. |
| H9 | **Mechanical failure of printed parts** | Layer delamination, thin walls, PLA creep, fatigue at a cyclic linkage | Part fragment on scalp, element collapses into head, pinch | 3 | 3 | M: load-bearing prints ≥4 perimeters, orientation per load, no layer line across a bending axis; proof-test 2× max load before human test; inspect after every session. |
| H10 | **Loosened fasteners** | Vibration from reciprocation | Element droops, rattles, falls on face | 3 | 4 | M: nyloc nuts / threadlocker / heat-set inserts; torque-mark fasteners; pre-test check. |
| H11 | **Broken scratching tips / fragments** | Brittle PLA or resin tip snaps under side load; tip chip | Fragment near eye; sharp stub on scalp | 4 | 3 | M: tips in PETG/nylon/acetal/silicone-overmold — never bare PLA or standard brittle resin; proof-load each tip 3× rated force; positive retention (§3.6); safety glasses for the first three human sessions. |
| H12 | **Skin abrasion** | Sustained dwelling at one spot, rough tip finish, high tangential force, repeated pass on same line | Erythema, excoriation, infection | 2–3 | 3 | M: tip polish; limits in §2 (pressure, dwell). F: pattern randomisation / no dwell >2 s. P: session ≤20 min initially; skin inspection. |
| H13 | **Localized sustained pressure (straps, pads, resting elements)** | Head-mounted frame load concentrated on pads; element left parked in contact | Ischemia, headache, pressure mark | 2 | 3 | M: pads ≥25 mm wide, closed-cell foam; parked elements lift off; total head-borne mass ≤500 g [EST]. P: reposition ≥ every 20 min. |
| H14 | **Electrical — mains** | Mains inside enclosure, DIY PSU, exposed terminals | Shock, fire | 5 | 2 | E: **no mains inside the device**; certified external adapter ≤24 V DC; nothing at >60 V DC anywhere on the rig. |
| H15 | **Electrical — low-voltage shorts, overheating drivers** | Chafed wire at moving joint, solder bridge, driver without thermal shutdown, undersized wire | Burn, melted print, fire | 3–4 | 3 | E: fuse per motor branch at 1.5× running current; strain-relief at every moving wire; drivers with OCP/OTP (§4); wiring in sleeving; no bare terminals. |
| H16 | **Motor back-EMF / inductive kick** | Motor driven backwards by head motion; sudden stop | Driver/MCU damage → unpredictable behaviour | 2 | 3 | E: drivers with integrated flyback; TVS on motor bus; separate logic supply. |
| H17 | **LiPo battery** | Any lithium pack in a hobby build | Fire | 5 | 2 | E: **no lithium battery in SP1** (brief §3 excludes battery anyway); mains-adapter power only. |
| H18 | **Moving parts near eyes / ears** | Front-of-hairline elements, side modules over the ear, fragment ejection | Eye injury, ear pinch/cut | 4 | 2 | M: no moving element anterior to the hairline or within 25 mm of the ear canal without a fixed guard; guard between any element and the eyes; safety glasses initially. |
| H19 | **No / failed emergency shutoff** | Software-only stop; e-stop out of reach; stop that needs two hands | Any other hazard escalates | 4 | 3 | E: NC mushroom e-stop in series with motor supply, within reach of the free hand; hold-to-run for first tests; logic stays powered. |
| H20 | **Hygiene (skin flora, sebum, product residue on tips)** | Porous prints, open-cell foam, non-removable tips | Folliculitis, cross-contamination | 2 | 4 | M/P: removable tips; sealed or non-porous skin-contact parts; 70 % IPA wipe-down protocol (§8). |
| H21 | **Thermal — hot motors/drivers near scalp** | Stalled or continuously loaded servo at 10 mm from scalp; driver without heatsink | Burn, discomfort | 3 | 3 | M: motor/driver bodies ≥10 mm from scalp or insulated; E: current limits keep dissipation low; surfaces ≤43 °C (§2.6); temperature check with IR thermometer after 20 min bench run. |
| H22 | **Noise** | Gear noise, servos, reciprocating impact, resonant printed shell near ears | Annoyance, startle, fatigue; negligible hearing risk | 1–2 | 4 | M: damping, isolation mounts, avoid impacts; limit ≤70 dBA at ear [EST]; target ≤60 dBA. |
| H23 | **Head-mounting hazards** | Strap pressure, device slipping/falling, weight on neck, chin strap | Headache, neck strain, device falls on face, strangulation risk from strap | 3 | 3 | M: head-borne mass ≤500 g [EST]; no chin strap unless breakaway; device tethered to frame so it cannot fall >50 mm; or **prefer a stationary frame the user leans into** (§5). |
| H24 | **User cannot remove device quickly** | Buckles behind head, element engaged in hair when powered off, two-hand release | Any hazard prolonged; panic | 4 | 3 | M: single-hand quick-release in ≤3 s; power-off state = elements retract/limp (§4.7); stationary-frame option means "withdraw head" is the release. |
| H25 | **Software / firmware faults** | Infinite loop, bad limit value, integer overflow in position target, lost comms to serial servos | Runaway, no stop, stuck in contact | 3 | 3 | F: hardware watchdog, bounded targets clamped in one place, motion timeout, heartbeat to serial servos; **none of these are credited alone** — mechanical caps bound the worst case. |

Severity/likelihood are pre-control; every S≥4 row has at least one mechanical (M) or hard electrical (E) control, and the firmware column is never the only control.

---

## 2. Quantitative safety limits

All limits are per *SP1 as a self-test rig*; they are deliberately conservative versus the literature ceilings, but above a vigorous human scratch.

### 2.1 Normal force
- **Reference — human scratch:** instrumented ring study, mean normal force 0.36 ± 0.23 N (low), 0.66 ± 0.29 N (medium), **1.56 ± 0.58 N (high)** per finger [SRC: [Nature Comms Med 2023](https://www.nature.com/articles/s43856-023-00345-2)].
- **Reference — scalp pain onset (pressure algometry, ~1 cm² probe):** healthy scalp PPT over bone ~150–225 kPa (frontal/vertex 206, parietal 147–177, occipital 106–226 kPa) [SRC: [scalp pressure-pain map](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4417469/), [Cuadrado et al. 2010](https://doi.org/10.1111/j.1468-2982.2009.01895.x)]; temporalis 171 kPa (0.5 cm² probe) [SRC: [Jensen et al. 1986](https://www.sciencedirect.com/science/article/abs/pii/0304395986902356)] to 282–315 kPa [SRC: [review](https://www.researchgate.net/publication/276066236)]. That is **15–22 N over 1 cm²** to pain onset; a fingernail-sized contact reaches pain at a lower force but higher pressure (spatial summation).
- **Reference — cobot ceiling:** ISO/TS 15066 skull/forehead quasi-static 130 N / 130 N·cm⁻², face 65 N / 65 N·cm⁻², with skull/face contact to be *avoided* [SRC: [ISO/TS 15066](https://www.diag.uniroma1.it/deluca/pHRI_elective/ISO_TS_15066_2016_en.pdf)]. We contact the scalp deliberately, so our limits sit ~50× lower.

**Limits:**
| Quantity | Limit | Basis |
|---|---|---|
| Normal force per scratching element, hard mechanical cap | **≤2.5 N** | ≈1.5× the mean "high" human scratch; ~1/6 of 1 cm² algometer pain onset [EST] |
| Normal force per element, operating target for first tests | 0.3–1.5 N (adjustable) | human scratch range [SRC] |
| Total simultaneous normal force on scalp (all elements) | **≤12 N** | sum over ≤5 elements at cap; <1/10 of ISO/TS 15066 skull limit [EST] |
| Any single structural/mount contact (pad, rest, frame) | ≤20 N static | below 1 cm² algometer PPT [SRC-derived] |
| Any credible fault force (fall, jam, stall) at the head | ≤65 N | ISO/TS 15066 face quasi-static value as absolute never-exceed [SRC] |

### 2.2 Contact pressure (abrasion / pressure injury)
- Fingernail free-edge contact on scalp is roughly a 2–5 mm × 0.3–1 mm patch (≈1–5 mm²) [EST]. A 1 N scratch is therefore ~200–1000 kPa *locally* — scratching works precisely because it is locally intense but transient and moving.
- Capillary closing pressure ~32 mmHg (4.3 kPa); sustained pressure above ~30–40 mmHg produces ischemic injury over time, and low pressure for long duration is worse than high pressure briefly [SRC: [capillary pressure overview](https://www.sciencedirect.com/topics/nursing-and-health-professions/capillary-pressure)].

**Limits:** moving tip, transient: **≤1 MPa** peak nominal contact pressure [EST — 2.5 N over ≥2.5 mm² minimum contact patch; forces tip radius ≥0.4 mm and no point loads]; any tip dwelling stationary on skin: ≤2 s then lift or move [EST]; straps/pads: **≤5 kPa (~37 mmHg)** sustained, reposition every 20 min [SRC-derived]; parked elements: zero contact.

### 2.3 Tangential (shear) force and hair
- Hair epilation force: mean **0.70 N** (anagen 0.85 N, telogen 0.53 N; occipital anagen 0.94 N); n = 30 subjects, 1200 hairs [SRC: [trichotillometer study, PMC5372430](https://pmc.ncbi.nlm.nih.gov/articles/PMC5372430/)]. Hair breaking force ~1 N (≈100 gf) [SRC: [TRI Princeton](https://www.triprinceton.org/single-fiber-tensile-experiments)].
- Consequence: a single trapped strand will be plucked by *any* normal scratch-level tangential force. Hair safety therefore cannot come from force limiting alone; it comes from **geometry that does not capture strands** plus force limiting so a *tuft* can never be loaded hard.

**Limits:** tangential force per element **≤2 N** hard cap (slip clutch / compliant deflection / breakaway) [EST]; element must deflect or lift at ≤1.5 N of unexpected lateral load [EST]; no feature on a tip or guard that can trap a 50–100 µm strand: no slots, grooves, holes, or sliding gaps <2 mm wide in the hair zone — gaps must be sealed (<0.1 mm) or large and shielded [EST]; acceptable session hair loss: a few strands (normal brushing sheds 50–100 hairs/day); **any tuft pull is a stop-and-redesign event**.

### 2.4 Velocity and kinetic energy
- Human scratch strokes are roughly 20–60 mm at 2–5 Hz → tip speeds ~0.1–0.4 m/s [EST — to be refined by the sensation model].

**Limits:** tip speed **≤0.4 m/s**; moving mass per scratching element **≤30 g** (KE at 0.4 m/s ≈ 2.4 mJ); any carriage/arm moving relative to the head: KE **≤50 mJ** (e.g., 600 g at 0.4 m/s) [EST, comfortably below any transient-contact concern; the number mostly protects against startle and pinch]. Acceleration limited by the compliance, not the actuator.

### 2.5 Session duration
- First human sessions **≤5 min**, then ≤10, then ≤20 min continuous; mandatory inspection of scalp (erythema, abrasions) and hair in device after each; strap/pad reposition every 20 min [EST, from pressure-duration reasoning in §2.2].

### 2.6 Temperature
- IEC 60601-1 Table 24 (applied parts, skin contact): **43 °C for ≥10 min**, 48 °C for 1–10 min, 51 °C for <1 min; edition 2 used 41 °C for parts not intended to heat [SRC: [Advanced Energy app note](https://www.advancedenergy.com/getattachment/de0a5180-3b23-4825-8c83-038fc29cde83/AN_Maximum_Allowable_Temperature.pdf?lang=en-US), [MDDI](https://www.mddionline.com/regulatory-quality/iec-60601-1-2005-a-revolutionary-standard-part-2)].

**Limits:** any surface that touches the scalp **≤41 °C**; motor/driver housings within 10 mm of skin ≤43 °C; hand-touchable housings ≤48 °C; measure after a 20-minute worst-case bench run at 25 °C ambient.

### 2.7 Noise
- NIOSH REL 85 dBA 8-h TWA [SRC: [NIOSH 1998](https://www.nonoise.org/hearing/criteria/criteria.htm)]; "quiet massager" benchmark ~50 dB; 60 dBA ≈ conversation at 1 m [SRC: [decibel comparisons](https://sounddecibelmeter.org/comparison/)].

**Limits:** ≤70 dBA at the ear (hard, nuisance/startle not hearing), target ≤60 dBA [EST].

### 2.8 Electrical
- **Operating voltage ≤24 V DC; 12 V preferred** (SELV-class; also keeps servo torque modest). Power from a **certified (UL/ETL/CE-marked) external desktop adapter** with internal short-circuit/over-current protection; **no mains conductors inside any SP1 enclosure or on the rig**. Adapter rated ≥1.5× the sum of running currents, and the adapter's own OCP sets the absolute ceiling. Fuse (or PTC) per motor branch at ~1.5× running current, ≤ driver rating. No lithium cells (H17). Wire gauge ≥ 22 AWG for motor runs ≤1.5 A, 18 AWG above.

---

## 3. Mechanical safety toolkit

The mechanism team should reach for these in roughly this order. Everything here is apartment-buildable.

### 3.1 The spring-suspended head: make maximum force a mechanical constant
The most important idea in this document: put a spring between actuator and scratching element and **limit its compression with a hard stop the actuator cannot push past**. Then:

> **F_max = F_preload + k · x_max**, independent of actuator stall torque.

Worked example: preload 0.3 N, k = 0.1 N/mm, 12 mm compliant travel → F_max = 0.3 + 1.2 = **1.5 N**. A servo with 1 N·m stall (≈25 N at a 40 mm arm) cannot exceed 1.5 N at the tip *provided* the two stops are placed correctly:
1. **Spring stop:** the element bottoms against the carriage at x_max.
2. **Actuator stop:** the actuator's own travel (horn angle, slide length) is mechanically limited so that at full actuator extension *and* the closest credible head position (head pushed fully into the device, strap at its limit), spring compression is still ≤ x_max. If this condition fails, the actuator pushes through the bottomed spring and the cap is lost — so this is a dimension to be checked, not assumed.

Variants: **dead-weight preload** on a stationary frame (element on a pivot, tip force = counterweighted mass × g, e.g. 80 g → 0.8 N — the cleanest cap of all); **constant-force (flat spiral) springs**; **printed TPU/PETG cantilever flexures** (cheap, no sliding gap for hair); compression spring on a telescoping post with a sealed boot. Compliant travel ≥ scalp curvature variation across the stroke plus head motion (≥10 mm [EST]).

Intensity adjustment is a spring or preload swap, not a software torque value — the intensity knob is mechanical, so even a wrong setting is bounded.

### 3.2 Force- and torque-limited actuators
- **Servo current/torque limits:** Dynamixel XL330 (`Current Limit` addr 38, `Goal Current` 102, ~1 mA/LSB) [SRC: [ROBOTIS e-manual](https://emanual.robotis.com/docs/en/dxl/x/xl330-m288/)]; Feetech STS3215 (present current addr 69, 6.5 mA/LSB, torque-limit register; stall 2.7 A at 12 V, spikes ~6.5 A) [SRC: [STS3215 tutorial](https://github.com/commanderfun/STS3215), [review](https://www.aliexpress.com/s/wiki-ssr/article/sts-3215_1005008814548910)]. F_tip = τ / r: 0.15 N·m at a 60 mm arm is 2.5 N. **Credit a servo limit only as a secondary layer** — it is firmware-settable, not a mechanical constant.
- **Slip clutch:** spring-loaded friction washer between drive and lever, nut-adjusted, printable; slip at 1.2–1.5× operating torque.
- **Magnetic breakaway coupling:** two disc magnets (e.g. 10 × 3 mm N35, ~1–2 N) joining tip arm to drive; a snag separates the arm instead of pulling hair, and doubles as a snap-off quick-release.
- **Shear pin:** a length of 1.75 mm filament as the drive pin; breaks before hair or skin does; replaced in seconds.

### 3.3 Travel stops
Every axis gets a *hard* stop at the safe envelope (printed bosses, screw-adjustable stops), set so that the tip cannot reach the eyes/ears/forehead or exceed the spring compression above. Firmware limits sit *inside* the hard stops.

### 3.4 Guards and hair exclusion
- All rotation (motor shafts, gear trains, pulleys, cranks) inside closed housings; the only thing that exits a housing near hair is a tip on a sealed, smooth stem.
- Reciprocating stems through **bellows/boots or long close-fit bushings** (clearance <0.1 mm or boot-covered), never through an open slot.
- A smooth **comb/shield plate** between the mechanism and the hair where practical: the hair sees only the tips and a smooth surface.
- No moving part anterior to the hairline or within 25 mm of the ear canal without a fixed guard.

### 3.5 Rounded geometry
- Skin-accessible non-scratching edges: radius ≥1.0 mm; guard perimeters ≥2 mm.
- Scratching tips: edge radius ≥0.4 mm (a fingernail free-edge is ~0.3–0.6 mm thick [EST]), polished; no edge anywhere that fails a UL 1439-style tape sharpness test [SRC: [UL 1439 description](https://www.bndtestequipment.com/industry-news/ul-1439-sharp-edge-tester-ul-1439-standard-for-sharpness-of-edges-explained/)].

### 3.6 Tip retention
Tips must be positively retained — bayonet with detent, M3 screw, or magnet *plus* mechanical pocket; a push-fit alone is not acceptable. Each tip proof-loaded to 3× rated force (≈7.5 N normal, 6 N lateral) on the bench before first use; any tip that cracks, chips or whitens is discarded. Tip materials: PETG, nylon, acetal (Delrin), silicone-overmolded cores, polished stainless rod ends. **No bare PLA or standard SLA resin tips** (brittle fragments).

### 3.7 Low moving mass
Moving element ≤30 g, driven through compliance so acceleration is spring-bounded. Keep motors on the frame, not on the moving element, where possible.

### 3.8 Drive type and back-drivability
- Standard hobby servos are **not back-drivable** (high-ratio plastic trains) — treat them as rigid position sources and put all compliance *downstream* of the horn.
- **Worm gears and lead screws are forbidden in any force path toward the scalp** unless a spring cap (§3.1) sits downstream, because they hold force after power loss.
- Prefer direct drive or low ratios (≤~1:30) on the approach axis so the head can push the element away.

### 3.9 Quick-release mounting
Single-hand, eyes-closed release in ≤3 s: side-release buckles or a lift-off cradle; no chin strap unless breakaway (<20 N) [EST]; device tethered so it cannot fall >50 mm onto the face.

### 3.10 Hardware emergency stop and hold-to-run
- **E-stop:** 22 mm NC mushroom-head latching button (≈$5–10), rated ≥ the motor bus current, wired **in series with the motor supply positive** between the fuse and the drivers. Pressing it removes motor power regardless of any firmware state. Logic (MCU) stays powered on its own branch so the event is logged and the state is known.
- **Hold-to-run (dead-man):** for all bench-to-human staging, motor power additionally passes through a momentary foot pedal or hand switch; release = power off. Wire it in hardware; the MCU may *read* it but must not be what *implements* it.
- E-stop position: within reach of the free hand without looking, and ideally on both sides of the rig for a head-mounted or frame-mounted device.

---

## 4. Electrical / control safety architecture

1. **Supply:** certified external adapter ≤24 V (12 V preferred) → inline fuse → **e-stop (NC)** → **hold-to-run contact** → motor bus. Separate branch (or a buck regulator *before* the e-stop) for logic, so the MCU never loses power when motors do.
2. **Isolation / separation:** logic and motor grounds joined at one star point; drivers take logic-level inputs so the MCU never sees motor voltage; TVS diode and 100–470 µF bulk capacitance on the motor bus for back-EMF. Opto-isolation is optional at ≤24 V.
3. **Current-limited drivers** with hardware current limiting and OCP/OTP. Brushed DC: **TI DRV8871** (ILIM by one resistor, 2 A default on the Adafruit board) [SRC: [TI DRV8871](https://www.ti.com/lit/gpn/DRV8871)]; **DRV8876** (1.3 A continuous, current-sense *output* for stall detection, VREF-settable limit) [SRC: [Pololu DRV8876](https://www.pololu.com/product/4036)]. Steppers: **TMC2209** (UART-set current, StallGuard). Serial servos: **Dynamixel XL330** (current-based position control, ~$24) or **Feetech STS3215**. Avoid L298N (no current limit). Bus current: INA219/INA226 or ACS712.
4. **Watchdog:** hardware WDT (RP2040, ESP32, AVR all have one); on timeout the driver *enable/sleep* line is pulled low by a resistor, i.e. motors off.
5. **Motion timeout:** motion that fails to reach target in N s, or any run >20 min → stop. Serial-servo buses need a heartbeat; loss → torque off.
6. **Stall detection:** driver current sense or servo current register; ~1.5× running current for >200 ms → cut that axis, require a user re-arm.
7. **Soft-start:** ramp PWM/goal over ≥500 ms on every start; no step inputs to the scalp.
8. **Fail-safe default state:** on power loss, e-stop, watchdog, or stall the approach axis **retracts under spring return** (or goes limp if back-drivable); no axis holds force without power; restart only on explicit user action.
9. **One limits table** in firmware (force/current, position, speed), clamped at runtime and printed at boot, sized *inside* the mechanical envelope so a bad value cannot reach a hazardous state.

---

## 5. Safety design principles, ranked for SP1

1. **Mechanical force cap** (spring + stops, or dead-weight) on every scalp-contacting element — the actuator's stall torque must be irrelevant.
2. **No exposed rotation or open sliding gap within 30 mm of hair**; hair sees only smooth guards and convex tips.
3. **Hardware e-stop in series with motor power**, plus hold-to-run for staged tests.
4. **Fail-safe de-energised state:** lift-off/limp on any loss of power or fault; no self-locking drives in the force path.
5. **User can always withdraw:** prefer a **stationary frame the user leans into** for SP1 (the head is the quick-release); if head-mounted, single-hand ≤3 s release and ≤500 g.
6. **Tip integrity and retention** (tough materials, proof-loaded, positively retained, nothing near the eyes).
7. **Travel stops** bounding every axis inside the safe envelope.
8. **Low-voltage certified power, fused, no mains, no lithium.**
9. **Driver-level current limiting + stall cut-off** (electrical second layer).
10. **Firmware watchdog, timeouts, clamped limits** (convenience layer, never credited alone).
11. **Hygiene by design:** removable, non-porous or sealed contact parts.
12. **Staged exposure protocol** (§6) so the first scalp contact happens with every limit already measured, not assumed.

---

## 6. Pre-human-test safety checklist (template)

Adapt to the selected design; every line gets a date/initial. Any "no" blocks the human test.

**A. Visual**
- [ ] No cracks, delamination, or stringing on printed parts; load-bearing parts unchanged since proof test.
- [ ] Skin-accessible edges radiused; tape sharpness test (probe in 3 tape layers, slide 50 mm, no cut) passed on tips, guards, mount edges.
- [ ] No fastener tip, wire, or burr toward skin; no shaft, gear, or pulley visible from the scalp side.
- [ ] Tips: correct material, polished, unchipped; retention engaged (hand pull ≥10 N).

**B. Mechanical**
- [ ] Spring cap measured (luggage scale or load cell): element pushed to its stop reads ≤2.5 N; record k, preload, x_max.
- [ ] Actuator stop: at full extension and minimum head distance the spring is not bottomed (margin ≥2 mm).
- [ ] Each axis hits its hard stop before the firmware limit; tip cannot reach hairline/ear/eye envelope with the device displaced ±15 mm.
- [ ] Slip clutch / breakaway / shear pin releases at ≤2 N tangential (measured).
- [ ] Hair exclusion: 100 µm nylon fishing line cannot be fed into any gap near the tips; boots intact.
- [ ] Fasteners torque-marked, nyloc/threadlocker present; shake test — nothing rattles.
- [ ] Quick-release: eyes closed, one hand, ≤3 s; tether limits drop to ≤50 mm (N/A for stationary frame).
- [ ] Head-borne mass ≤500 g; pads ≥25 mm wide, closed-cell.
- [ ] Moving element ≤30 g; tip speed ≤0.4 m/s (video frame count).

**C. Electrical**
- [ ] Adapter certification mark visible; output ≤24 V; no mains inside; cord strain-relieved.
- [ ] Fuse per motor branch at correct rating; polarity metered before first power-up.
- [ ] E-stop pressed → 0 V on motor bus with MCU running; hold-to-run released → 0 V.
- [ ] Driver current limit measured under bench stall (clamp meter / INA226) ≤ configured value.
- [ ] Every wire across a moving joint has a service loop and sleeving; no exposed conductors.
- [ ] 20-min worst-case run, IR thermometer: contact ≤41 °C, housings near skin ≤43 °C, elsewhere ≤48 °C.
- [ ] Logic stays up when motors are killed; boot prints the limits table.

**D. Functional (bench)**
- [ ] Watchdog: halt firmware deliberately → motors off within 1 s, element lifts off.
- [ ] Stall: block the element → current cut within 300 ms; re-arm required.
- [ ] Power pulled mid-stroke → element retracts/limps, nothing holds force.
- [ ] Noise ≤70 dBA at 10 cm (phone SPL meter).
- [ ] Runaway: command max/min/garbage targets → motion stays inside stops, force ≤ cap.

**E. Staged human-exposure philosophy**
1. **Bench** — all of the above on a foam/skull form over a load cell.
2. **Wig head** — real-hair or synthetic wig on a mannequin, 20 min continuous; count captured strands; inspect every gap for wind-up; repeat with hair deliberately pushed into the mechanism. Any tuft capture → redesign.
3. **Forearm skin** — volar forearm, 2 min at minimum then operating intensity; check erythema, abrasion, heat.
4. **Own hand** — push the palm into the element at operating settings: it must yield (compliance check) and hold-to-run release must stop it instantly.
5. **Scalp, low force** — safety glasses, e-stop in the free hand, hold-to-run pedal, minimum preload, ≤2 min then 5 min; inspect scalp and device for hair.
6. **Increase** — one variable at a time (force, speed, stroke, pattern), ≤20 min sessions, log hair pulls and discomfort; stop on any pain, tuft pull, heat, or loosening.

---

## 7. Red lines — SP1 must never

1. Have an **exposed rotating shaft, gear, pulley, or crank within 30 mm of hair**, or any open sliding slot in the hair zone.
2. Have any scalp-contacting element whose maximum normal force is not bounded by a **mechanical constant ≤2.5 N** (spring + stop, or dead weight) — actuator torque limits alone do not count.
3. Exceed **12 N total** simultaneous normal force on the scalp, or **2 N tangential** per element before something slips, deflects, or breaks away.
4. **Move with motors energised unless an NC hardware e-stop is in series with motor power** and within reach of the free hand; for staged tests, also a hold-to-run contact.
5. Have **mains voltage inside any enclosure or on the rig**, any bus >24 V DC, or any lithium battery.
6. Place any **moving element anterior to the hairline, within 25 mm of the ear canal, or anywhere above the eyes without a fixed guard** between element and eye.
7. Use a **self-locking drive (worm, lead screw, non-back-drivable servo) in the force path to the scalp** without a downstream spring cap and spring-return lift-off.
8. Hold an element in contact with the scalp after **power loss, e-stop, watchdog, or stall** — the de-energised state is lifted-off or limp.
9. Use **push-fit-only tips, bare PLA or brittle resin tips**, or any tip not proof-loaded to 3× rated force.
10. Mount on the head with **anything that cannot be released one-handed in ≤3 s**, a non-breakaway chin strap, or >500 g head-borne mass.
11. Present any skin-accessible edge **<1 mm radius** (tips: <0.4 mm) or that fails the tape sharpness test.
12. Run a first human session **without the §6 checklist complete, the wig-head entanglement test passed, safety glasses on, and session ≤5 min.**
13. Rely on **firmware as the only barrier** for any hazard rated S≥3 in §1.

---

## 8. Hygiene

- **70 % IPA-wipeable materials:** PETG, nylon, acetal, polypropylene, silicone, stainless, anodised aluminium, closed-cell EVA. PLA and PETG lose no strength after 48 h in 70 % IPA, but PLA softens above ~55 °C [SRC: [UVU food-safe study](https://lt728843.wixsite.com/maskrelief/post/the-final-say-in-food-safe-3d-printing), [filament comparison](https://industrialmonitordirect.com/blogs/knowledgebase/food-safe-filament-for-3d-printing-pla-vs-petg-vs-abs)]. Avoid ABS (crazes in IPA) and open-cell foam near skin.
- **FDM prints are porous:** layer gaps harbour bacteria that wiping does not reach [SRC: [spoolhound food-safety guide](https://spoolhound.com/food-safety-guide)]. Every skin- or hair-contacting printed part is therefore (a) replaced by stock material (acetal rod, silicone, stainless), (b) **sealed** (epoxy or UV-resin coat, vapour-smoothed PETG), or (c) a weekly consumable.
- **Removable tips:** tip plus first 20 mm of stem is a tool-free or single-screw assembly; keep two sets. Wipe with 70 % IPA before and after each session; let it flash off ≥1 min (IPA on freshly scratched skin stings).
- **No crevices** at the tip/stem junction where sebum collects (fillet ≥1 mm, no ledge).
- **Pads/straps:** closed-cell foam or silicone; any fabric must be removable and washable.
- **Single-user device:** anyone else trying it gets a fresh tip set and a full wipe-down.

---

## 9. Notes for the mechanism teams and the Safety Gate

- The whole human scratch envelope (0.3–1.6 N, moving contact, fingernail-radius edge) is inside these limits. If a mechanism needs >2.5 N per element to feel right, the sensation model must move the number with data, and it must still be a mechanical constant.
- Hair entanglement (H1) is the only S4/L4 row; the wig-head test is its gate, and current limiting never substitutes for sealed geometry.
- [EST] values are to be replaced by SP1's own load-cell and bench measurements, recorded in the §6 checklist.
