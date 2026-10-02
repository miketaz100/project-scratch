# SP1 "PUPPET HALO" — SYSTEM SPECIFICATION (Design Freeze v2)

**Project SCRATCH · 12-sp1v2 · System Architect · 2026-10-02**
**Binds to:** 12-sp1v2/DECISION-2.md (binding), 00-brief/BRIEF.md, 01-foundations/safety-requirements.md (13 red lines), hair-interaction.md (H-rules), tip-interface.md (edge R ≥ 0.4 mm).
**Builds on:** 11-leaps/round-3 (A–E), round-2 (B, C, D, F; A and E skimmed), leap-B (L1, L2), 10-porcupine/pin-unit.md, 05-engineering (servo-alternatives, bom-verified, electronics-firmware).
**Supersedes:** 05-engineering/DESIGN-FREEZE.md and ADDENDUM-1 (Float-Arm). Those files stay as reference. Where this file and a leap document disagree, this file governs.

**Tags.** **[KNOWN]** = sourced in a project file or a vendor page cited there. **[EST]** = computed here or carried from a leap estimate; the arithmetic is shown or rerunnable (scripts `sp.py` and `com.py` in the session scratchpad). **[VERIFY]** = an open item that a named bench test or a vendor check must close before the dependent part is ordered or printed. Every [VERIFY] is collected in §12.2.

---

## 0. SP1 in one page

SP1 is a skeleton helmet carrying **one hand-sized pad of 12 air-pressure nails**. The pad drifts slowly over the scalp on a carbon bail that pivots on an axis through the ears, and scrubs in a **slowly precessing straight line** (the default), a fixed straight line, or a circle. Nothing on the head is powered except two slow travel servos in the ear hubs. The scrub motion is made by a **master synthesiser in the drive box** and copied to the pad through **three sealed air lines**. Every nail's force is **rail pressure × piston area**, capped by a relief valve. Every nail **hovers 5 mm above the scalp and bites** in a per-nail, per-stroke time window. Any loss of power, any stop and any pulled plug **lifts the pad clear by spring**.

| Quantity | Frozen value | Tag |
|---|---|---|
| Pins | **12**, 4 × 4 grid minus corners, 18 mm pitch, field 54 × 54 mm | EST (choice §1) |
| Pin bore / force | Ø 7.0 mm (38.5 mm²); 0.04 N per kPa; operating 2–13 kPa = **0.08–0.50 N** | KNOWN arithmetic |
| Per-nail cap | rail relief **25 kPa = 0.96 N** (red line 2: ≤ 2.5 N) | EST |
| Total normal cap | palm-float relief **20 kPa on Ø 20 = 6.3 N, + pad weight 0.9 N = 7.2 N** (red line 3: ≤ 12 N) | EST |
| Hover / bite | hover 5 mm above last touch; bite descent 50 mm/s; plough-in ≤ 35° | EST |
| Nail | POM omni-nail: 90° cone, Ø 2.0 mm flat, **rim R 0.4 mm**, on a 0.38 mm music-wire trailing neck | EST |
| Master | two-stage parallel-crank synthesiser, **r₁ = r₂ = 7.5 mm**, two NEMA 17 pancake steppers on TMC2209 | EST |
| Modes | **PLINE** (default: 30 mm line, ε = 0.025, 4.5° per cycle), LINE (30 mm), CIRCLE (R 8–15 mm) | binding |
| Synchro | **3 sealed air lines**, PU 4 × 2.5 mm, 1.4 m, Ø 20 rolling-diaphragm cylinders, p₀ = 20 kPa | EST |
| Copy stiffness / error | 1.0 N/mm at the pad; ≤ 0.5 mm stroke shrink at 0.5 N drag; bow ≤ 0.3 mm | EST |
| Scrub rate | line ≤ 2.0 Hz (≤ 188 mm/s); default 1.4 Hz | EST |
| Travel | α (bail pitch) −25…+100°, β (latitude) ±55°; drift 20–50 mm/s, sweeps ≤ 80 mm/s | EST |
| Head-borne mass | single **352 g** (target ≤ 400); twin **≈ 479 g** (limit 480; mass ladder §4.7) | EST |
| Drive box | **300 × 220 × 110 mm, ≤ 2.5 kg**; desk, chair back or couch back | EST |
| Umbilical | 1.4 m; 17 tubes + 6 wires, Ø ≈ 17 mm in a loose knit sleeve; latched QD at the box, 12 N magnetic breakaway at the helmet | EST |
| Power | 12 V 5 A certified adapter; ≈ 22 W typical, ≈ 47 W peak; no mains in the box, no lithium | EST |
| Cost | **≈ $1,240** mid-estimate for one-pad SP1 plus second-pad parts (±15 %), against a **≤ $1,200** target; §13 lists the levers | EST |

---

## 1. Open choices resolved

Each row closes a choice the leap documents left open. "Why" is the deciding reason. Numbers come from §4.

| # | Choice | Decision | Why |
|---|---|---|---|
| C1 | Pin count | **12** (4 × 4 minus corners, 18 mm pitch) | A 3-nail rake row ⟂ any heading 100 % of the time and a 4-nail row 61 % (leap2-B L3), which the precessing line needs because its heading rotates continuously. 16 pins buys 4-nail rows at 89 % for +$150, +9 g and a thicker bundle; 8 pins loses all 4-nail rows. |
| C2 | Pin bore | **Ø 7.0 mm, all pins identical** | One part, one diaphragm, one calibration. Per-finger force spread comes from landing asynchrony and per-stroke rail slew; a bore-mix kit (6.5/7.0/7.5) is a Stage D A/B, and a second valve per pin is SP2. |
| C3 | Pin actuator | **Cast-silicone top-hat rolling diaphragm** in a 7.0 mm bore, POM piston, Ø 1.0 mm music-wire shaft in a PTFE guide | It is the only cheap seal with near-zero stiction over 24 mm of stroke. Latex finger-cot bladders are Stage A interim only (life, leap2-C). |
| C4 | Pin mounting | **Rigid translating pin block** (the scrub plate) with its underside ≥ 32 mm above the skin; pins parallel to the pad axis | The tip path equals the master path exactly. The attack angle is constant, with no ±15–23° tilt swing, and there are no 12 diaphragm pivots. The hair zone holds only 1 mm shafts and nails. The still-dome / tilting-pin variant (leap2-F L2) is the SP2 fallback if the Stage B wig test shows hair stirred by the block. |
| C5 | Hover mechanism | **Split-PTFE friction collar, 0.08 N, 5 mm lost motion**; return spring 0.05 N; park by vacuum −8 kPa | As leap2-F L3. It is the only passive way to hover at "last touch + 5 mm" whatever the seating. |
| C6 | Descent metering | **Ø 0.20–0.25 mm restrictor at each pin inlet, with a parallel duckbill** so venting is free; a Ø 0.5 mm sense orifice at the box | Descent ≈ 50 mm/s and the force rises ≤ 20 ms after contact. The box-side sense orifice turns each pin sensor into a flow and landing detector, used for latency calibration and the head scan. |
| C7 | Force rails | **One pin rail** with an electronic regulator: rail pump PWM + 15 ml accumulator + fixed bleed; slew ≤ 60 ms up, ~20 kPa/s down | This allows a per-stroke redraw of force (scratch-model §4.4 resamples force every cycle) without two S070s per pin. A second rail is SP2. |
| C8 | Total-force cap | **Palm-float relief.** Scalp load = float force + pad weight, whatever the pins do. | Pins react against the pad, and the float holds the pad. If the pins push harder than the float, the pad lifts away. Red line 3 then rests on one relief valve, independent of pin count. |
| C9 | Synchro medium | **Air**, not water | Its 1.0 N/mm stiffness is finger-like compliance (scratch-model 3.12). A leak is dry. The box can sit in any orientation. Air inertance is negligible. Relief valves give a true tangential cap. Water would be 50× stiffer but wet, bubble-sensitive and gravity-sensitive in a box that hangs on a chair. |
| C10 | Synchro geometry | **3 lines, Ø 20 rolling-diaphragm cylinders, tangential bodies with 1:1 bell cranks so the three lines of action are radial (concurrent at the plate centre)**; a polypropylene (PP) two-stage parallelogram holds the plate against rotation; the master is an exact replica | Three single-acting pushers at equal p₀ must be concurrent or they apply a net torque. A pinwheel without bell cranks puts 0.57 N·m on the plate. Bell cranks keep the deck about 105 mm across instead of about 220 mm. |
| C11 | Master drive | **Two NEMA 17 pancake steppers + TMC2209 (stealthChop)**, open-loop, with a Hall home index per crank | Phase lock is exact by step count (ε is set by a frequency ratio, not by a control loop), so no encoders are needed. They are silent enough inside a foam box, cost ~$11 each, and have 3–5× the torque needed. |
| C12 | Hub travel motors | **Feetech STS3032** serial bus servos (20.6 g, 0.15 N·m rated, 111 rpm, 12-bit, current-limited); **3:1 Dyneema capstan** on α; Ø 20 drum direct on β | In US stock (servo-alternatives §6). Gear-held when unpowered, so the bail cannot free-fall (leap3-E 8c). One 3-wire bus. A gimbal + FOC cartridge (leap3-A L1) is the fallback if the Stage C bone-conduction test fails, and the pod's motor cartridge interface takes either. |
| C13 | Helmet retention | **Bike dial cradle under the occiput (form lock) + front half-band + temple pads; no chin strap** | Holds ~1–1.5 N·m in pitch by geometry (leap3-E E2), against a 0.24 N·m worst lean. The cradle override (~10 N) is itself the breakaway. A 12 N magnetic-fuse elastic chin strap is bought and fitted only if the Stage C slip test fails. |
| C14 | Bail | **One carbon 10 × 8 mm arc, R 210 mm about the skull centre O**, spanning β ±62°, with legs down to hubs at \|Y\| = 120 mm; **built as two half-bails joined by a bolted vertex splice** | The radius is set by the radial chain (§4.6): skin to pad top 80 mm, float 50 mm (25 mm absorbs scalp radius, 25 mm retract), carriage. The split is the twin provision. |
| C15 | Carriage drive | **Dyneema tendon outside the tube, in a PTFE guide bonded along the bail's outer face**; carriage rolls on 4 POM V-rollers | No slotted tube. Every part is ≥ 120 mm from the skin, far outside the hair zone. |
| C16 | Fail-to-free lift | **Radial air float, Ø 20 bore, 50 mm stroke, spring retract (1.5 N preload, 0.03 N/mm)** on two parallel guide rods; NO palm dump plus a palm-line bleed | Retracts 25 mm in ≈ 80 ms even against gravity on the crown. It has two vent paths, and a de-energised valve means a lifted pad. |
| C17 | Pad registration | **RCC palm (leap3-C C1)**: 3 carbon struts at 35° from a Ø 110 float ring to the pad deck, lines crossing at the nail plane; **3 POM R 15 dome skids on a Ø 100 circle, 0.15 N each**; constant-support gait in firmware | Drag cannot tip the pad, and the skids never pat. There are no sensors on the pad. |
| C18 | Head scan sensing | **Pneumatic only.** Per-pin descent time-of-flight from the box sensors (shape, canopy depth); synchro line pressures (drag rose → grain, whorl); egg (sensitivity, fences) | Keeps "no wires on the pad" (DECISION-2). Per-pin Hall sensors and skid Halls (leap3-C) are dropped. |
| C19 | Circle mode in hair | **Allowed only where the scanned canopy depth is ≤ 12 mm** (pins can exit fully once per revolution, E3), and only at R ≥ 8 mm | The pin stroke is 24 mm. The 20 mm park clears ≤ 15 mm of pile with 5 mm margin. |
| C20 | Squeeze egg + hold-to-run | **One hand controller: a palm grip whose palm lever is the hold-to-run (2.5 N microswitch); a 3-chamber silicone egg at its finger end**; a pneumatic hard-squeeze switch (> 40 kPa) in series with the rail | One hand holds both, with no battery and no radio. The other hand stays free for the e-stop. |
| C21 | E-stop location | **Weighted desk/armrest puck on a 1.5 m lead**, not on the box | The box may hang behind the chair, out of reach. |
| C22 | Umbilical support | **Overhead hanger**: a 700 mm rod with a spring clamp (box, chair back, couch back or desk edge), carrying a **3 N magnetic clip** 100–200 mm above and behind the crown; a 300–350 mm free loop to a plug at the halo's rear node | The helmet carries only the loop (≈ 20 g share; ≤ 0.01 N·m bending with the tubes loose in a knit sleeve, never tied; leap3-D D3). |
| C23 | Connectors | **Same 20-port face-seal block at both ends**: magnetic, 12 ± 3 N at the helmet; two draw latches (≥ 40 N) at the box | One printed design. Unplugged at either end, every helmet-side line is open to the air, so the pins, palm and synchro all vent. |
| C24 | Controller | **ESP32-S3** (dual core): core 1 runs the valve and stepper real-time loop, core 0 the score and serial | Native USB, MCPWM/RMT for step generation, enough I/O through SPI expanders. The OpenRB-150 has no use without Dynamixels. |
| C25 | Twin sharing | **Pad B's 12 pins tee onto the same 12 valves** (lockstep, point mirror); **pad B gets its own 3 synchro lines** from a 6-cylinder master | Two slaves cannot share a closed line: it is indeterminate and halves the amplitude. Per-pad valves are SP2 if lockstep reads as a machine (leap3-A L2 (g)). |
| C26 | Hover/vent in de-energised state | **Valve de-energised = pin ↔ lift manifold; LIFT SELECT de-energised = atmosphere** | A dead box vents every pin. Vacuum park is an energised state. |
| C27 | PLINE default rate | **f = 1.4 Hz, ε = 0.025 ± 0.010 (pink random walk), heading 4.5° per cycle (2.25° per half-stroke), 180° in 40 cycles = 28.6 s** | DECISION-2's "~4.5°/stroke" is read as per out-and-back cycle, the leap3-B derivation (heading change = 180°·ε per revolution). |
| C28 | Tip mount | **TM1-P**: a nail stick (shaft + neck + nail) that drops out through the pin's bayonet cap; 12-stick sets per variant | TM1's 10 × 4 mm magnetic tang suits a holder, not a 7 mm pin. TM1 rules are kept: positive retention, proof 3×, edge ≥ 0.4 mm. |

---
## 2. System overview and block diagram

### 2.1 What each block does

**Helmet (head-borne, 352 g).**
- **Front half-band and dial cradle.** A front half-band runs hub to hub across the forehead (pad 45 mm above the brows). It closes into a bike-helmet dial cradle that hooks under the occipital bun, so the bun stays free to be scratched. Two TPU temple pads resist yaw.
- **Hub pods.** On each side, 45 mm above the ear canal and 120 mm off the midline, sits a sealed hub pod. Its inner face is a parietal suspension pad. Each pod contains the bail bearings (2 × 6800-2RS), a motor cartridge bay, a cable drum, and a zero-length spring balancer for the bail.
  - **Left pod:** the α motor, driving a 3:1 Dyneema capstan sector.
  - **Right pod:** the β motor with a double-groove Ø 20 drum, and an empty, pre-machined second pitch bay (twin provision).
- **Bail.** A carbon arc (R 210 about O) carries the carriage. It is built as two half-bails with a vertex splice.
- **Carriage, float and pad.** The carriage carries the radial air float (50 mm stroke, spring retract). The float carries the **pad** on a three-ball kinematic mount held by magnets, so the pad lifts off tool-free for cleaning and breaks away under overload.
- **Rear node.** A rear node on the cradle carries the helmet half of the umbilical plug and the twin tee-manifold boss.

**Pad (≈ 80 g; plastic, silicone, steel; no wire, valve or motor).**
- **Pad body (still):** the deck, three skid stems with POM R 15 domes on a Ø 100 circle, the RCC strut set up to the float ring, the PP parallelogram anchor, and the 15-port pad manifold.
- **Pin block (moves):** translates ±15 mm in the pad plane, driven by the **synchro follower** (three Ø 20 slave cylinders on the deck with bell cranks). The block carries 12 pin cartridges.
- **Each pin:** a rolling-diaphragm piston, a hover collar, a restrictor with duckbill, a bleed, a PTFE-guided Ø 1.0 mm shaft, and a double wiper at the nose. The nail is a POM omni-nail on a 12 mm, 0.38 mm music-wire trailing neck.
- **Pin tubes:** a 12-lumen flat loop from the manifold to the block, flexing ±15 mm above the deck under a cover.
- **Fail-to-free:** venting the palm line retracts the whole pad 25 mm or more by spring.

**Umbilical (1.4 m).**
- 12 pin lines and 1 palm line (PU 3 × 2), 1 spare palm line (blanked, twin), 3 synchro lines (PU 4 × 2.5), and a 6-core 26 AWG cable. All run loose in a knit sleeve, Ø ≈ 17 mm.
- One 20-port face-seal block at each end: latched at the box, magnetic 12 N at the helmet.
- It is carried by the overhead hanger through a 3 N magnetic clip.

**Drive box (300 × 220 × 110 mm, ≤ 2.5 kg).**
- **Master synthesiser:** two steppers, two crank stages, an Oldham coupling, and a master plate with 3 cylinders fitted plus 3 spare mounts.
- **Air supply:** rail pump, vacuum pump and palm pump, each with an accumulator, bleed and relief.
- **Valves:** 12 SMC S070 pin valves; three cheap utility valves (LIFT SELECT, PALM, SYNC CHARGE); five normally-open dump valves (3 synchro, rail, palm).
- **Instrumentation:** 22 pressure sensors on 3 × MCP3208.
- **Drivers:** 3 × TPIC6B595 valve drivers, pump MOSFETs, 2 × TMC2209.
- **Controller and power:** ESP32-S3; servo bus buffer; 6 V servo buck and 5 V logic buck; the hardware safety loop.
- **Enclosure:** foam-lined.

**User inputs.**
- The **hand controller** (hold-to-run palm lever + 3-chamber squeeze egg + hard-squeeze pressure switch), on a 1.5 m lead of 2 wires and 3 tubes.
- The **e-stop puck** (NC latching mushroom, weighted), on a 1.5 m lead.

**PC.** USB-C serial at 921,600 baud. It handles experiment control, score upload, and logs.

### 2.2 Block diagram

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 700" width="1000" height="700" font-family="Helvetica, Arial, sans-serif" font-size="11">
  <defs>
    <marker id="a" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#333"/></marker>
    <marker id="ab" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#1f5fbf"/></marker>
  </defs>
  <rect width="1000" height="700" fill="#fff"/>
  <text x="14" y="22" font-size="15" font-weight="bold">SP1 PUPPET HALO: system blocks (black = mechanical, blue = air, red = actuator rail, green = signal)</text>

  <!-- HELMET -->
  <rect x="14" y="40" width="430" height="400" fill="#f7f7f2" stroke="#555"/>
  <text x="24" y="58" font-weight="bold" font-size="13">HELMET (head-borne, 352 g single / ≈479 g twin)</text>
  <rect x="28" y="70" width="190" height="62" fill="#fff" stroke="#333"/>
  <text x="36" y="86" font-weight="bold">Halo structure</text>
  <text x="36" y="100">front half-band + forehead pad</text>
  <text x="36" y="113">dial cradle under occiput (form lock)</text>
  <text x="36" y="126">temple pads · no chin strap</text>
  <rect x="232" y="70" width="198" height="62" fill="#fff" stroke="#333"/>
  <text x="240" y="86" font-weight="bold">Bail (2 half-bails + splice)</text>
  <text x="240" y="100">carbon 10×8, R 210 about O</text>
  <text x="240" y="113">β ±62° arc, legs to hubs |Y| 120</text>
  <text x="240" y="126">tendon in PTFE guide on top</text>
  <rect x="28" y="144" width="190" height="88" fill="#fff" stroke="#333"/>
  <text x="36" y="160" font-weight="bold">LEFT hub pod</text>
  <text x="36" y="174">α motor STS3032 → 3:1 capstan</text>
  <text x="36" y="187">2 × 6800-2RS on Ø10 shaft</text>
  <text x="36" y="200">zero-length spring balancer</text>
  <text x="36" y="213">inner face = parietal pad</text>
  <text x="36" y="226">≥ 60 mm from ear canal</text>
  <rect x="232" y="144" width="198" height="88" fill="#fff" stroke="#333"/>
  <text x="240" y="160" font-weight="bold">RIGHT hub pod</text>
  <text x="240" y="174">β motor STS3032 → Ø20 2-groove drum</text>
  <text x="240" y="187">pitch bay #2 empty (twin α_R)</text>
  <text x="240" y="200">bearings, balancer (twin-ready)</text>
  <text x="240" y="213">servo bus daisy-chain socket</text>
  <text x="240" y="226">inner face = parietal pad</text>
  <rect x="28" y="244" width="190" height="62" fill="#fff" stroke="#333"/>
  <text x="36" y="260" font-weight="bold">Carriage + radial float</text>
  <text x="36" y="274">4 POM V-rollers, tendon clamp</text>
  <text x="36" y="287">float Ø20 × 50, spring retract</text>
  <text x="36" y="300">palm line + 0.3 mm bleed</text>
  <rect x="232" y="244" width="198" height="182" fill="#eef4ff" stroke="#1f5fbf" stroke-width="1.5"/>
  <text x="240" y="260" font-weight="bold">PAD (≈80 g, no wires)</text>
  <text x="240" y="274">RCC struts 35° → virtual pivot</text>
  <text x="240" y="287">   at the nail plane</text>
  <text x="240" y="300">3 POM R15 skids, Ø100, 0.15 N</text>
  <text x="240" y="313">deck: 3 Ø20 slave cylinders +</text>
  <text x="240" y="326">   bell cranks (radial, concurrent)</text>
  <text x="240" y="339">PP parallelogram (anti-rotation)</text>
  <text x="240" y="352">PIN BLOCK ±15 mm (follower)</text>
  <text x="240" y="365">12 pins, Ø7 bore, 24 mm stroke,</text>
  <text x="240" y="378">   hover collar, restrictor, bleed</text>
  <text x="240" y="391">omni-nails R0.4 on 0.38 necks</text>
  <text x="240" y="404">underside ≥ 32 mm above skin</text>
  <text x="240" y="417">kinematic 3-ball + magnets mount</text>
  <rect x="28" y="318" width="190" height="108" fill="#fff" stroke="#333"/>
  <text x="36" y="334" font-weight="bold">Rear node + helmet plug</text>
  <text x="36" y="348">20-port face seal + 6 pogo</text>
  <text x="36" y="361">4 × N52 Ø10×3: 12 ± 3 N</text>
  <text x="36" y="374">open ports when pulled → vent</text>
  <text x="36" y="387">loop wire → rail cut</text>
  <text x="36" y="400">twin tee-manifold boss</text>
  <text x="36" y="413">harness to both hub pods</text>
  <line x1="123" y1="232" x2="123" y2="244" stroke="#333" stroke-width="2"/>
  <line x1="218" y1="275" x2="232" y2="275" stroke="#333" stroke-width="2"/>
  <line x1="331" y1="132" x2="331" y2="144" stroke="#333" stroke-width="2"/>

  <!-- UMBILICAL -->
  <rect x="460" y="300" width="130" height="140" fill="#fff8e8" stroke="#a57000"/>
  <text x="468" y="318" font-weight="bold">UMBILICAL 1.4 m</text>
  <text x="468" y="333">12 pin  PU 3×2</text>
  <text x="468" y="346">1 palm (+1 spare)</text>
  <text x="468" y="359">3 synchro PU 4×2.5</text>
  <text x="468" y="372">6-core 26 AWG:</text>
  <text x="468" y="385"> 6V, GND, DATA,</text>
  <text x="468" y="398"> LOOP×2, spare</text>
  <text x="468" y="411">loose knit sleeve Ø≈17</text>
  <text x="468" y="424">hanger clip 3 N</text>
  <line x1="218" y1="372" x2="460" y2="372" stroke="#1f5fbf" stroke-width="3"/>
  <line x1="590" y1="372" x2="612" y2="372" stroke="#1f5fbf" stroke-width="3"/>
  <rect x="460" y="246" width="130" height="44" fill="#fff" stroke="#a57000" stroke-dasharray="4 3"/>
  <text x="468" y="263" font-weight="bold">Overhead hanger</text>
  <text x="468" y="278">700 mm rod + clamp</text>

  <!-- DRIVE BOX -->
  <rect x="612" y="40" width="374" height="560" fill="#f2f6fb" stroke="#555"/>
  <text x="622" y="58" font-weight="bold" font-size="13">DRIVE BOX 300×220×110, ≤2.5 kg</text>
  <rect x="624" y="68" width="350" height="78" fill="#fff" stroke="#c33" stroke-width="1.5"/>
  <text x="632" y="84" font-weight="bold" fill="#c33">POWER + HARDWARE SAFETY LOOP</text>
  <text x="632" y="99">12 V 5 A certified brick → fuse 5 A → E-STOP (NC) → HOLD-TO-RUN (NO)</text>
  <text x="632" y="113">→ EGG hard-squeeze switch (NC) → RAIL-ENABLE MOSFET (gated by</text>
  <text x="632" y="127">watchdog charge pump AND helmet LOOP) → ACTUATOR RAIL 12 V</text>
  <text x="632" y="141">logic: separate 5 V buck before the loop (MCU stays alive)</text>
  <rect x="624" y="156" width="170" height="120" fill="#fff" stroke="#333"/>
  <text x="632" y="172" font-weight="bold">MASTER synthesiser</text>
  <text x="632" y="186">2 × NEMA17 pancake</text>
  <text x="632" y="199">TMC2209 stealthChop</text>
  <text x="632" y="212">stage 1 r₁ 7.5 · stage 2 r₂ 7.5</text>
  <text x="632" y="225">Oldham to stage 2</text>
  <text x="632" y="238">master plate: 3 cyl Ø20 +</text>
  <text x="632" y="251">   3 spare mounts (twin)</text>
  <text x="632" y="264">Hall home per crank</text>
  <rect x="804" y="156" width="170" height="120" fill="#fff" stroke="#1f5fbf"/>
  <text x="812" y="172" font-weight="bold">SYNCHRO circuit</text>
  <text x="812" y="186">3 lines, p₀ 20 kPa</text>
  <text x="812" y="199">relief +8 kPa per line</text>
  <text x="812" y="212">3 × NO DUMP (fail = slack)</text>
  <text x="812" y="225">CHARGE (NC) + 3 duckbills</text>
  <text x="812" y="238">3 sensors = drag vector</text>
  <text x="812" y="251">re-zero every rest / ≤60 s</text>
  <rect x="624" y="286" width="350" height="150" fill="#fff" stroke="#1f5fbf"/>
  <text x="632" y="302" font-weight="bold">PNEUMATICS</text>
  <text x="632" y="317">P1 rail pump → 15 ml acc. → bleed Ø0.25 → RAIL 2–13 kPa</text>
  <text x="632" y="331">   reliefs R1a 25 kPa + R1b 27 kPa · RAIL DUMP (NO)</text>
  <text x="632" y="345">P2 vacuum pump → VAC −8 kPa (breaker −10)</text>
  <text x="632" y="359">P3 palm pump → acc. → PALM RAIL 10–17 kPa, relief R2 20 kPa,</text>
  <text x="632" y="373">   PALM DUMP (NO); PALM 3-way (de-energised = vent)</text>
  <text x="632" y="387">12 × S070 pin valves: energised = rail, off = LIFT manifold</text>
  <text x="632" y="401">LIFT SELECT 3-way: energised = VAC (park), off = air (hover)</text>
  <text x="632" y="415">per pin: Ø0.5 sense orifice + sensor at box;</text>
  <text x="632" y="429">   Ø0.22 restrictor + duckbill + Ø0.15 bleed at pin</text>
  <rect x="624" y="446" width="350" height="96" fill="#fff" stroke="#2a8a2a"/>
  <text x="632" y="462" font-weight="bold">CONTROLLER (ESP32-S3)</text>
  <text x="632" y="477">core 1: 1 kHz valve scheduler + step gen + sensor scan</text>
  <text x="632" y="491">core 0: score player, κ-grammar, ledger, scan, serial</text>
  <text x="632" y="505">SPI: 3 × MCP3208 (24 ch) · 3 × TPIC6B595 (24 out)</text>
  <text x="632" y="519">UART1: STS bus 1 Mbps · UART2: TMC2209 · microSD</text>
  <text x="632" y="533">USB-C CDC 921600 ↔ PC · watchdog charge pump out</text>
  <rect x="624" y="552" width="350" height="38" fill="#fff" stroke="#333"/>
  <text x="632" y="568">enclosure: 6 mm ply/PETG, closed-cell foam, sorbothane</text>
  <text x="632" y="582">feet, chair-back hook plate, strap slots, handle</text>
  <line x1="794" y1="216" x2="804" y2="216" stroke="#1f5fbf" stroke-width="3"/>

  <!-- INPUTS -->
  <rect x="14" y="460" width="300" height="130" fill="#f3fbf3" stroke="#2a8a2a"/>
  <text x="24" y="478" font-weight="bold" font-size="13">USER INPUTS</text>
  <text x="24" y="496">Hand controller (1.5 m: 2 wires + 3 tubes)</text>
  <text x="24" y="510">  palm lever = HOLD-TO-RUN (NO, 2.5 N)</text>
  <text x="24" y="524">  3-chamber silicone egg → 3 sensors (yes / there / move)</text>
  <text x="24" y="538">  hard squeeze > 40 kPa → NC pressure switch in rail</text>
  <text x="24" y="556">E-stop puck (1.5 m): 22 mm NC latching mushroom</text>
  <text x="24" y="570">  weighted, on the armrest / lap / side table</text>
  <text x="24" y="584">Free hand always on the e-stop side</text>
  <line x1="314" y1="520" x2="624" y2="110" stroke="#c33" stroke-width="1.5" marker-end="url(#a)"/>
  <rect x="340" y="610" width="250" height="70" fill="#fff" stroke="#2a8a2a"/>
  <text x="350" y="628" font-weight="bold">PC (laptop)</text>
  <text x="350" y="643">serial console, score upload, live plots,</text>
  <text x="350" y="657">session logs (CSV), blind A/B control</text>
  <text x="350" y="671">nothing on the PC can energise the rail</text>
  <line x1="590" y1="645" x2="700" y2="545" stroke="#2a8a2a" stroke-width="1.5" marker-end="url(#a)"/>
  <text x="620" y="625" fill="#2a8a2a">USB-C</text>
  <text x="24" y="612" font-size="10" fill="#555">Helmet side carries: 2 servos (6 V bus), the loop wire pair, pneumatics only on the pad.</text>
  <text x="24" y="626" font-size="10" fill="#555">Everything that is fast, heavy, hot, noisy or switching lives in the box.</text>
</svg>

### 2.3 Pneumatic schematic (drive box, one pin shown)

```
 P1 rail pump ─► 15 ml ACC ─┬─ R1a 25 kPa ─ R1b 27 kPa (independent reliefs to air)
   (PWM, PID on S13)        ├─ RAIL BLEED Ø0.25 to air (sets down-slew ≈ 20 kPa/s)
                            ├─ RAIL DUMP (NO, BP exhaust valve) to air
                            └─► RAIL GALLERY ──► S070 #k (NC port) ─┐
                                                                    │ COM ─► Ø0.5 sense orifice ─┬─ S(k) sensor
 P2 vac pump inlet ─► 50 ml VAC ACC ─ breaker −10 kPa                │                            └─► pin line k (PU 3×2, 1.4 m)
            └─► LIFT SELECT (3-way: energised = VAC, off = ATM) ─► LIFT MANIFOLD ─► S070 #k (exhaust port)
                                                                                        at the pin: duckbill ∥ Ø0.22 restrictor
                                                                                        → chamber; Ø0.15 bleed to air
 P3 palm pump ─► 30 ml ACC ─┬─ R2 20 kPa ─ R2b 22 kPa (twin 15/16) ── PALM DUMP (NO) ── PALM BLEED Ø0.2
                            └─► PALM 3-way (energised = palm rail, off = ATM) ─► S22 ─► palm line ─► float (Ø0.3 bleed at float)
 RAIL ─► SYNC CHARGE (NC) ─► 3 duckbills ─► synchro lines 1–3 ◄─ master cylinders M1–M3
                                            each line: relief +8 kPa (set 28 kPa abs-gauge), NO DUMP, sensor S16–S18
 Egg chambers E1–E3 ─► sensors S19–S21; all three ─► 3 duckbills ─► hard-squeeze switch volume (Ø0.3 bleed) ─► PS1 (NC, opens > 40 kPa)
```

---
## 3. Coordinate frames and the head model

### 3.1 Frames (right-handed, mm, degrees)

| Frame | Origin | Axes | Moves with | Used by |
|---|---|---|---|---|
| **H** head | **O, the skull centre**: 45 mm above and 10 mm behind the tragion (ear-canal) midpoint, on the midsagittal plane | X forward (toward the nose), Y left, Z up (Frankfurt plane horizontal) | the head (and the halo, which is rigid to it within slip) | everything; the head map, the fences and the ledger cells are stored in H |
| **B** bail | O | rotated by **α about Y_H**; α = 0 puts the bail over the vertex; **+α swings the pad toward the occiput** | bail | α servo, spring balancer |
| **C** carriage | on the bail arc at latitude **β** (+β toward the left ear) | z_C radial outward from O, x_C along the bail tangent toward +β, y_C completes | carriage | β servo, float |
| **P** pad | the **nail plane** at the pad axis (where the RCC lines cross) | z_P along the pad axis away from the scalp; x_P, y_P in the pin plane, x_P = the bail tangent at β = 0 | pad body | pin layout, scrub path, skids |
| **S** scrub | pin-block centre in P | parallel to P; block position (x_S, y_S) = synchro copy of the master | pin block | modes, windows |
| **M** master | master-plate centre in the box | identical to S by construction (replica) | master plate | crank kinematics |

**Direction to the pad centre:** **u(α, β) = R_Y(α) · (0, sin β, cos β)**. The pad sits at r_skin(u) + stack along u.

**Point mirror (twin):** pad B is at **(−α, −β)**, so u_B = R_Z(180°) · u_A (leap3-A L2).

**Hub axis:** the Y_H axis itself. The hubs are at Y = ±120 mm, Z = 0, which is 45 mm above the canal and ≈ 66 mm from it.

### 3.2 Design head (50th-percentile adult male)

All values are [EST] (ANSUR-II-class means as recalled in the project files; [VERIFY] against a published table before CAD freezes the cradle). Michael's own head replaces these at the first-use head scan (§8.6) and by a one-time tape and caliper fit (§10, Stage C).

| Quantity | Value |
|---|---|
| Head length (glabella–opisthocranion) | 197 mm |
| Head breadth | 153 mm |
| Head circumference | 572 mm |
| Tragion to vertex | 133 mm |
| Bitragion breadth | 146 mm |
| Ellipsoid model about O, semi-axes | **a = 98 (X), b = 77 (Y), c = 88 (Z+)** |
| Scalp distance from O | 77–80 mm at the sides, 88 mm at the vertex, **≈ 98 mm at the occipital bun** |
| Local radius of curvature (scratch-model 3.16) | crown 85–100, sides 100–150 (vertical), bun 60–80 mm |
| Frontal hairline | α ≈ −50° on the midline [EST; per user from the scan] |
| Ear canal (tragion) in H | (−10, ±72, −45) → (X, Y, Z) |
| Neck pivot (atlanto-occipital) | (−10, 0, −80) |
| Head mass | 4.5 kg |
| Hair-bearing scalp | ≈ 575–600 cm² |
| Design hair | 2–8 cm, pile 10–25 mm (hair-interaction §1.3); Michael's actual length is recorded at Stage C |

### 3.3 Calibration chain

1. **Mechanical zero.** Each servo's absolute encoder is zeroed with the bail on a printed **zero jig**: α = 0 is the bail perpendicular to the band plane; β = 0 is the carriage at the splice centre. The offsets are written to servo EEPROM.
2. **Fit.** The dial is set once and the band position marked. The halo's seating repeats to ±5–10 mm (leap3-C).
3. **Head scan** (first use, ≈ 5 min, §8.6). It maps shape, canopy depth, grain and whorl in H.
4. **Session registration** (15 s). One drag rose near the stored whorl plus three profile stations solve the helmet's seating offset (yaw ±1°, fore-aft ±3 mm). Soft fences and ledger cells shift with it. Hard stops stay helmet-fixed, with ≥ 10 mm margin.

---

## 4. Frozen numbers

### 4.1 Pad and pins

| Item | Value | Tag / source |
|---|---|---|
| Layout | 12 pins, 4 × 4 grid minus the 4 corners, **18.0 mm pitch**, axes parallel to z_P | C1; leap2-B L3 |
| Field / pad envelope | field 54 × 54 mm; deck Ø 105 mm; skid circle Ø 100 mm; overall Ø 110 mm | EST |
| Rake rows available | 3-nail row ⟂ heading: 100 % of headings; 4-nail: 61 %; virtual drift 1–2 pitches inside the field | KNOWN (leap2-B search) |
| Pin bore / area | 7.0 mm / 38.5 mm² | — |
| Force per kPa | 0.0385 N/kPa | arithmetic |
| Operating rail | 2–13 kPa = **0.08–0.50 N** per nail; firmware hard limit 0.60 N (15.6 kPa) | scratch-model §4.4 |
| Per-nail cap (mechanical) | R1a 25 kPa → **0.96 N**; R1b 27 kPa → 1.04 N; pump stall 53 kPa → 2.04 N (still ≤ 2.5 N) | EST; red line 2 holds even if both reliefs fail |
| Pin stroke | **24 mm**: park at extension 0 (nail 20 mm above nominal skin), skin contact at extension 20, 4 mm reserve | C19 |
| Hover | collar friction **0.08 N (spec window 0.07–0.10 N)**, lost motion 5.0 mm, return spring 0.05 N at hover | leap2-F L3 |
| Park | vacuum −8 kPa → −0.31 N lift; reached from hover in ≤ 120 ms | EST |
| Descent (bite) | restrictor Ø 0.20–0.25 mm sized for **50 ± 10 mm/s**; 5 mm in ≈ 100 ms | EST [VERIFY Stage B] |
| Force rise after contact | ≤ 20 ms (chamber 0.5 ml through the restrictor) | EST |
| Lift (vent) | duckbill bypass; force < 0.05 N in ≤ 20 ms after the valve drops | EST |
| Per-pin bleed | Ø 0.15 mm at the pin cap: a trapped 10 kPa decays below 2 kPa (0.08 N) in < 1 s whatever the tube does | leap2-F §4 |
| Bite (plough-in) angle | descent / tangential speed ≤ tan 35°; firmware lands where v_t ≥ 1.4 × descent speed (≥ 70 mm/s) | H-5.3 (≤ 30° target, 35° accepted) |
| Lift point | where v_t ≥ 0.53 v_peak (\|s\| = 0.85 on the line) | H-5.3 |
| Shaft | Ø 1.0 mm A228 music wire (or 1.0 mm superelastic NiTi), PTFE guide 2.0 × 1.0 × 12 mm + piston as the second guide point | EST |
| Tangential tip compliance | shaft + neck ≈ 0.12–0.2 N/mm (0.15 N gives ~1 mm of yield) | pin-unit §4.1; H-4.11 scores 1, as every design does |
| Nose | drafted 15° POM/PETG cone, tip Ø 4, R 1, double 0.5 mm 40A silicone wiper, at the block underside (≥ 32 mm above skin) | pin-unit §4.6 |
| Block underside | smooth, drafted ≥ 15° at the rim, Ra ≤ 0.8 µm, ≥ 32 mm above nominal skin | H-6.3 |
| Pin moving mass | 0.6 g; installed mass ≈ 2.3 g per pin | EST |

**Omni-nail (default tip, "O-POM-20").**
- **Geometry:** a POM body of revolution; 90° included cone, **Ø 2.0 mm flat, rim R 0.4 mm**, flaring to Ø 7 at 2.5 mm height; 0.1 g.
- **Neck:** 0.38 mm (0.015") music wire, 12 mm free, in a bonded PTFE 1.0 × 2.0 sleeve trimmed to 8 mm, with a Ø 1/16" brass ferrule onto the shaft. It leans 5–15° under drag.
- **Stability margin:** k = 17 N·mm/rad against F_n·L = 0.96 N × 12 mm = 11.5 N·mm/rad at the cap. That leaves a stability margin of 1.5 even at the relief.
- **Lean stop:** 30° (a ferrule lip).
- **Retention:** the neck is hooked into a cross-drilled tip and resin-filleted; proof 1.5 N axial and 1.0 N lateral (3×).

**Tip variant sets (12 sticks each):**
- O-POM-30 (Ø 3 flat);
- O-PETG-20 (matte, friction A/B);
- D-6 (pin-unit 6 mm directional mini-nail, R 0.4, control);
- H-3 (3 mm ball, the massager control).

A45 (R 0.3) is not made for SP1 (tip-interface floor 0.4).

### 4.2 Pneumatic rails and caps

| Rail / line | Setpoint | Cap (mechanical) | Regulator | Fail state |
|---|---|---|---|---|
| Pin RAIL | 2–13 kPa, slewed per stroke | R1a 25 kPa + R1b 27 kPa | P1 PWM + 15 ml accumulator + Ø 0.25 bleed; PID at 1 kHz on S13 | RAIL DUMP (NO) opens |
| VAC | −8 kPa | breaker at −10 kPa | P2 PWM | lift manifold goes to atmosphere (LIFT SELECT off) |
| PALM rail | 10–17 kPa (float force 3.1–5.3 N), slow, gravity-compensated from α/β | **R2 20 kPa + independent R2b 22 kPa → total scalp load ≤ 7.2 N (≤ 7.8 N at a double fault)**; twin: R2/R2b 15/16 kPa → ≤ 5.6 N per pad, ≤ 11.9 N total at a double fault | P3 PWM + 30 ml accumulator + Ø 0.2 bleed | PALM 3-way vents the line; PALM DUMP (NO); 0.3 mm bleed at the float |
| Synchro lines ×3 | p₀ 20 kPa (charged from RAIL during rests) | relief at 28 kPa per line (p₀ + 8): ≤ 2.5 N per line, ≤ 4 N pad tangential in any direction | sealed; CHARGE + DUMP re-zero | 3 NO DUMPs open → plate slack |
| Egg chambers ×3 | atmosphere ± squeeze | hard-squeeze switch opens the actuator rail > 40 kPa | 0.3 mm bleed per chamber (τ ≈ 2 s) | — |

**Air budget [EST, sp.py].**

| Draw | Amount |
|---|---|
| Line mode, 4 pins biting both flanks at 1.4 Hz (0.68 ml free air per bite from a vented line) | 0.49 L/min |
| Bleeds, 4 pins pressed | 0.33 L/min |
| Rail bleed | 0.15 L/min |
| **Total, line mode** | **≈ 1.0 L/min** |
| Circle mode, 8 pins parking every revolution at 1 Hz | 0.61 L/min, plus the same bleeds |

One KPM27C-class pump (> 1.8 L/min free flow, 53 kPa stall) is enough. The vacuum pump handles park only.

### 4.3 Master synthesiser and modes

| Item | Value |
|---|---|
| Kinematics | z(t) = r₁e^{iθ_A} + r₂e^{iθ_B}; **r₁ = r₂ = 7.50 ± 0.05 mm** (machined eccentric bushings, not printed) |
| Stage 1 | parallel-crank plate on 3 eccentrics (1 driven by motor A via a GT2 belt 1:1, 2 idlers), translating without rotation |
| Stage 2 | 3 eccentrics on the stage-1 plate, driven by motor B through a **printed POM Oldham coupling** (1:1 across the moving offset); output = **master plate** |
| Motors | 2 × NEMA 17 pancake (20–25 mm body, ≥ 0.13 N·m holding), TMC2209 at 1/16 microstep, stealthChop, 0.4–0.6 A rms |
| Load | ≤ 5 N net on the master plate (relief-capped) × 7.5 mm = 0.04 N·m per stage; margin ≥ 3 |
| Home | A3144-class Hall + 3 × 2 mm magnet per crank; phase known to ±0.5° after homing |
| Speed range | f = 0.25–2.0 Hz (15–120 rpm) |

**Mode definitions** (θ_A = 2πf·t):

| Mode | θ_B | Path | Parameters (default **bold**) | Limits |
|---|---|---|---|---|
| **PLINE** (default) | −(1 − ε)·θ_A + φ_B | 30 mm line whose heading ψ = (θ_A + θ_B)/2 turns 180°·ε per cycle | f **1.4 Hz**; ε **0.025**, pink random walk ±0.010 every 3 cycles; sign of ε flips with p 0.2 at rests | f ≤ 2.0 Hz; \|ε\| ≤ 0.05 |
| LINE | −θ_A + φ_B | 30 mm line, heading ψ = φ_B/2 | f, ψ (from the grain map: with-grain default, H-5.1) | f ≤ 2.0 Hz |
| CIRCLE | +θ_A + δ | circle R = 15·cos(δ/2) | R **12 mm** (δ = 74°); R ∈ [8, 15] | 2πfR ≤ 188 mm/s; canopy ≤ 12 mm (C19) |
| Heading jump | step φ_B by 2Δψ | heading +Δψ | only during a lift | step ≤ 90° per jump |
| Mode switch | LINE ↔ PLINE: ε change, instant. Any ↔ CIRCLE: motor B reverses with a 150 ms ramp | — | pins parked during any reversal of B | — |

**Speeds and accelerations on the 30 mm line** (amplitude a = 15 mm):

| f | v_peak | v at the lift point (s = 0.85) | Peak acceleration in contact (\|s\| ≤ 0.85) | End-zone time per end |
|---|---|---|---|---|
| 1.0 Hz | 94 mm/s | 50 mm/s | 0.50 m/s² | 177 ms |
| **1.4 Hz** | **132 mm/s** | **70 mm/s** | **0.99 m/s²** | **126 ms** |
| 2.0 Hz | 188 mm/s | 99 mm/s | 2.0 m/s² (H-5.4 limit) | 88 ms |

**Maximum scrub rate: 2.0 Hz on the line** (v ≤ 200 mm/s, a ≤ 2 m/s² in contact, H-5.4). Above 1.7 Hz, firmware uses **alternating sets** (set A bites outbound, set B inbound) so that each pin has a full half-cycle (≥ 250 ms) to lift and land.

### 4.4 Synchro (puppet link)

| Item | Value | Tag |
|---|---|---|
| Lines | **3**, sealed, air, **PU 4 × 2.5 mm, 1.40 m** | C9, C10 |
| Cylinders (master and slave, identical) | Ø 20 bore (3.14 cm²), cast silicone top-hat rolling diaphragm (0.4 mm wall), stroke 34 mm (±15 working), POM piston, ball-ended push link | EST [VERIFY diaphragm life] |
| Geometry | bodies tangential on the deck; 1:1 bell cranks (pivots on 3 × MR63) turn each stroke radial; three lines of action concurrent at the block centre; PP two-stage parallelogram (0.7 mm sheet, 40 mm links) against rotation | C10 |
| Charge p₀ | 20 kPa gauge (from RAIL via CHARGE + duckbills at a P5 rest, master at centre) | EST |
| Gas volume per line | 5.3 (slave half) + 5.3 (master half) + 6.9 (tube) + 0.5 = **18 ml** | sp.py |
| Stiffness | 0.66 N/mm per line; **≈ 1.0 N/mm at the block** (1.5 × per line) | EST |
| Stroke shrink under drag | 0.5 mm at 0.5 N; 1.0 mm at 1 N spikes (finger-like) | EST |
| Viscous drop at the master | 0.8 / 1.2 / 1.6 kPa at 1.0 / 1.5 / 2.0 Hz (Re ≤ 2,000, laminar) | EST |
| Acoustic lag | 4.1 ms; with compliance damping, total common-mode lag **4–6 ms**, measured per build | EST [VERIFY] |
| Block resonance | 40 g on 1.0 N/mm → **25 Hz** (12× the 2 Hz drive), tube-damped | EST |
| Tangential cap | per-line relief at p₀ + 8 kPa = 2.5 N per line; ≤ 4 N on the pad in any direction | C10 |
| Drag sensing | Δp·A: 50 Pa sensor resolution ↔ **16 mN**; drag vector at 1 kHz after subtracting a calibrated viscous model | leap3-B |
| Re-zero | at every P5 rest (5–20 s) and at least every 60 s: master to centre → DUMP 100 ms → CHARGE 150 ms | EST |
| Leak budget | ≤ 0.5 kPa/min per line (≤ 0.3 mm drift per minute) | [VERIFY Stage A] |

### 4.5 Copy error budget and maximum scrub rate

Error at the nail relative to the commanded master path, on a 25 mm contact stroke at 1.4 Hz with 0.5 N drag [EST]:

| Source | Along-stroke | Lateral bow | Notes |
|---|---|---|---|
| r₁ − r₂ mismatch ≤ 0.1 mm | — | 0.05 mm | machined bushings |
| Step quantisation (1/16 µstep = 0.11°) | 0.01 | 0.01 | — |
| Master / slave area mismatch ±2 % | ±0.30 | — | cast diaphragms; calibrated by ink trace |
| Air compliance under 0.5 N drag | −0.50 | ±0.15 (±0.2 N lateral) | the "finger compliance" |
| Bell crank / rod geometry | 0.10 residual | 0.10 | replica cancels to first order |
| Leak drift between re-zeros | ≤ 0.30 | ≤ 0.30 | 60 s worst case |
| Shaft + neck lag (0.15 N/mm × 0.15 N) | 1.0 (uniform offset) | — | felt as lag, not shape |
| **RSS shape error** | **≤ 0.7 mm** | **≤ 0.4 mm** | pass line: bow ≤ 0.5 mm, shrink ≤ 1 mm at 0.5 N (leap3-B) |

Scalp two-point acuity is 15–39 mm, so every term is sub-perceptual. **Maximum scrub rate** is 2.0 Hz (§4.3). Circle mode is limited by 2πfR ≤ 188 mm/s: R 15 at ≤ 2.0 Hz, R 10 at ≤ 3.0 Hz.

### 4.6 Travel, radial chain and coverage

**Radial chain at the pad axis** (above the skin): skin 0 → pin block underside 32 → pin tops 71 → deck cover 78 → RCC float ring 80 → float body (working extension) → carriage → bail centreline.
- Scalp radius from O varies 77–98 mm across the coverage.
- The float stroke of **50 mm** is split into **25 mm to absorb that variation** and **25 mm of retract margin** at the largest radius.
- That fixes **R_bail = 98 (largest scalp radius) + 80 (stack) + 25 (retract) + 7 (carriage half-depth) ≈ 210 mm** [EST].

| Axis | Range (firmware) | Hard stop | Speed | Drive |
|---|---|---|---|---|
| α (bail pitch) | −25° … +100° | −35° / +108° (printed bosses in the left pod) | drift 0.15–0.38 rad/s at the pad; ≤ 0.62 rad/s (80 mm/s) | STS3032 → 3:1 capstan (Ø 15 drum on the horn, R 22.5 sector) |
| β (carriage latitude) | −55° … +55° (twin: +8 … +55 per side) | ±60° (carriage end stops on the arc) | same | STS3032 → Ø 20 drum, tendon loop, pitch coupling 10/210 rad/rad removed in firmware |
| Float (radial) | 0–50 mm | piston ends | extend 0.2–0.5 s ramp; retract ≤ 150 ms | palm pressure / spring |

**Travel speeds:**
- drift 20–50 mm/s concurrent with scrub (κ = v_drift/v_peak ≤ 0.4);
- P2 sweeps (pins down, master parked at centre, path monotonic with-grain) 40–80 mm/s;
- hops between regions with pins parked and the float retracted 10 mm, ≤ 80 mm/s.

**Moving-group kinetic energy:** 0.12 kg at 0.08 m/s = 0.4 mJ (limit 50 mJ).

**Coverage** (pad centre range × pin field ±27 mm; ellipsoid model, cov.py, not area-weighted, [EST]):

| Region (share of hair-bearing scalp) | Reached |
|---|---|
| Crown / vertex (14 %) | 100 % |
| Upper occiput (15 %) | 100 % |
| Bun / lower occiput (17 %) | 93 %; below the cradle's top edge is excluded |
| Parietal sides (31 %) | 94 % |
| Frontal top (11 %) | 80 %; the hairline fence is at α_pad ≥ −25°, the pin field to ≈ −41°, the skids to ≈ −40° |
| Low sides / temples (13 %) | 79 %; the hub pads and the 25 mm ear fence block the rest |
| **Total** | **≈ 90 %** (leap3-A: ≈ 90 %) |

The **nape** and the **temporal fossa** are out of scope by construction (scratch-model §5).

**Fences.**
- **Ear:** at β = ±55° the pad edge stays ≥ 39 mm from the canal (≥ 25 mm, red line 6).
- **Hairline:** the hard stop at α = −35° is behind the fixed front band, which is the guard between the pad envelope and the eyes. The soft fence comes from the scan, at α_hairline + 16° + 4° margin.

### 4.7 Mass budget and centre of mass

| Part | Single (g) | Twin adds (g) | Basis |
|---|---|---|---|
| Front half-band (PA12 or 20 × 1.5 Al) | 20 | — | EST |
| Forehead pad + washable sleeve | 10 | — | leap3-D |
| Dial cradle (harvested bike retention) | 30 | — | leap3-D/E |
| Temple pads ×2 | 6 | — | EST |
| Hub pods ×2 (housing, 2 × 6800-2RS each, capstan, drum, balancer, parietal pad, TPU grommets) | 36 | — | leap3-D (24) + capstan |
| Hub motors STS3032 ×2 | 41 | **+21** (α_R) | KNOWN 20.6 g each |
| Bail (10 × 8 carbon, 0.044 g/mm × 690 mm, nodes, splice, tendon guide) | 40 | −3 (splice off) | EST |
| Carriage | 10 | +10 | EST |
| Radial float + guide rods + spring | 12 | +12 | EST |
| **Pad** | **80** | **+80** | EST, §4.1 |
| Tendon, idlers, spring balancer parts | 6 | +4 (crossed loop) | EST |
| Helmet plug + harness + strain relief | 18 | +2 (tee manifold) | EST |
| Umbilical head-borne share (0.35 m loop × 117 g/m ÷ 2) | 20 | +2 | EST |
| Doff handle / visor guard | 8 | — | EST |
| Fasteners, wiring, misc | 10 | +2 | EST |
| Pre-built twin provisions (empty bay, double drum, blanked ports) | 4 | −3 (dummy cartridge out) | EST |
| **Total** | **≈ 352** (≤ 400 target; 48 g reserve) | **≈ 479** (at the ≤ 480 limit, no reserve: the mass ladder below applies to the twin first) | |

**Mass gates.** At Stage B the pad must weigh ≤ 90 g. At Stage C the helmet must weigh ≤ 400 g measured. Over-budget ladder, in order:
1. thin the cradle and band;
2. Ø 16 slave cylinders (−6 g);
3. drop the RCC struts for a centre ball pivot with 1 N skids (−5 g);
4. twin pads at 8 pins (−8 g each).

**Centre of mass** (com.py, 367 g model mass; moving group 104 g at r_skin + 40 for the pad and r_skin + 105 for the float and carriage) [EST]:

| Pose (α, β) | CoM in H (X, Y, Z) mm | Gravity moment about O, upright head |
|---|---|---|
| (−25°, 0) hairline | (+15, 0, 52) | 0.05 N·m |
| (0, 0) vertex (park pose) | (−9, 0, 57) | 0.03 N·m |
| (45°, 0) upper occiput | (−49, 0, 42) | 0.18 N·m |
| (90°, 0) bun | (−67, 0, 2) | **0.24 N·m (worst)** |
| (0, ±55°) sides | (−9, ±31, 39) | 0.12 N·m |
| Twin, any mirrored pose | (−7, 0, 1–45) | **0.03 N·m** |

- **CoM wander, single:** ≈ 85 mm front to back.
- **Hold:** the form-locked cradle gives ≈ 1–1.5 N·m (leap3-E E2), a margin of ≥ 4 on the worst lean plus 0.11 N·m of scrub reaction. The friction-only fallback gives 0.49 N·m at µ 0.3 (margin 1.4, which is why the cradle form lock is mandatory).
- **Felt lean:** whether 0.24 N·m is felt as "the hat leaning" is [VERIFY Stage C coin test]. The twin removes it.

### 4.8 Noise budget at the ear (A-weighted, ear 0.7–1.2 m from the box) [EST]

| Source | Path | Mitigation | At ear |
|---|---|---|---|
| 12 S070 valve clicks | air | foam-lined box, valves on a sorbothane-mounted manifold | ≤ 20 dBA |
| Pumps P1–P3 (63 dB at 30 cm bare) | air | PWM at low duty, sorbothane, inlet muffler, 15–50 ml accumulators | ≤ 28 dBA |
| Steppers | air | stealthChop, box foam, rubber motor mounts | ≤ 22 dBA |
| Exhaust puffs | air | lift manifold vents through a sintered silencer inside the box | ≤ 15 dBA |
| Hub servos (STS3032, 64 mm from the canal) | air + **bone via the hub pads** | slow (motor output ≤ 18 rpm), TPU grommets, spring-balanced so loads stay low | ≤ 30 dBA air; bone [VERIFY Stage C earplug test] |
| Pin landings and top stops | bone | 0.05–0.08 N hover-and-bite landings; TPU top-stop washers | ≤ 20 dBA |
| Block, bell cranks, PP hinge | bone | no sliding keys, no backlash flank change in contact | ≤ 15 dBA |
| **Machine total** | | | **≤ 32 dBA target; ≤ 60 dBA hard (red line ≤ 70)** |
| Nail hiss (wanted) | bone + air | never masked | 30–40 dBA |

**Pass rule:** with all machinery on and the pins parked, the level at the tragus is within 3 dB of room level. With scratching, it is clearly louder (leap3-D §2 protocol).

### 4.9 Power budget (12 V, certified 5 A adapter)

| Load | Typical | Peak |
|---|---|---|
| 12 S070 coils (≈ 0.35 W each [VERIFY coil]; ≈ 4 energised on average) | 1.4 W | 4.2 W |
| Utility and NO-dump valves (5 NO held closed, about 1 of 3 utility on) | 4.0 W | 6.0 W |
| Pumps P1–P3 (PWM) | 6.0 W | 12 W |
| Steppers ×2 (0.5 A rms) | 7.0 W | 9.0 W |
| Hub servos ×2 at 6 V | 2.0 W | 14 W (stall, current-limited) |
| Logic (ESP32-S3, ADCs, SR, LEDs) | 1.5 W | 2.0 W |
| **Total** | **≈ 22 W** | **≈ 47 W** (adapter 60 W; fuse 5 A) |

### 4.10 Latency budget

| Path | Value | Basis |
|---|---|---|
| Firmware command → valve edge | ≤ 1 ms (1 kHz scheduler; edges timed by esp_timer to 0.1 ms) | EST |
| S070 open / close | 3 / 3 ms | KNOWN datasheet |
| Line acoustic delay 1.4 m | 4 ms | arithmetic |
| Pin starts moving | ≈ 8–12 ms after the edge | EST |
| **Bite: edge → contact (5 mm at 50 mm/s)** | **≈ 110 ms** (calibrated per pin, ±5 ms) | EST [VERIFY Stage B] |
| Force rise after contact | ≤ 20 ms | EST |
| **Lift: edge → force < 0.05 N** | **≈ 20 ms**; hover reached ≈ 40 ms | EST |
| Park from hover (vacuum) | ≤ 120 ms | EST |
| Synchro master → slave | 4–6 ms common to all lines | EST |
| Travel servo command → motion | 20–40 ms (bus at 50 Hz) | EST |
| Egg squeeze → firmware event | ≈ 30 ms (4.4 ms tube + 1 ms sensor + 20 ms debounce); response deliberately delayed 0.4–1.5 s | leap3-C C3 |
| E-stop / hold-to-run → rail dead | < 1 ms | hardware |
| Rail dead → pin force zero | ≤ 30 ms | EST |
| Rail dead → pad retracted 25 mm | ≤ 150 ms | EST |
| Rail dead → synchro slack | ≤ 50 ms | EST |

**Gate timing rule.** Every gate fires early by that pin's measured latency, re-measured at each ARMING (§8.1). A gate window shorter than (bite latency + 60 ms) is not scheduled.

---
## 5. Interfaces

The owner (work package, §11) designs both sides of each interface and changes it only through a revision of this table. Fasteners are M3 into brass heat-set inserts (Ø 4.0 × 5.7 mm holes) unless stated. Printed hair-zone parts are PETG or nylon, sanded and sealed.

### 5.1 Mechanical

| ID | Interface | Geometry / bolt pattern | Datum | Owner |
|---|---|---|---|---|
| M1 | Hub pod ↔ front band and cradle arms | 3 × M3 on a 24 mm triangle, plus one Ø 3 dowel | pod flange face F1 ⟂ hub axis at \|Y\| = 95 mm; dowel = rotation | HALO |
| M2 | Bail ↔ hub | Ø 10 h6 steel stub shaft bonded into the bail leg node (20 mm insertion); 2 × 6800-2RS (10 × 19 × 5) spaced 14 mm, wave-washer preload; capstan sector R 22.5 clamped by an M3 pinch screw on a shaft flat | shaft shoulder = hub axis datum; α = 0 by the zero jig | HALO |
| M3 | Motor cartridge ↔ pod bay (both pods, both bays identical) | cartridge plate 34 × 26 mm, 4 × M2.5 on 28 × 18 mm; accepts STS3032 (adapter A), XL330/XC330 (adapter B) or 2804 gimbal + AS5600 (adapter C) | cartridge face; motor shaft on a pitch circle R 30 mm from the hub axis (capstan centre distance) | HALO |
| M4 | Spring balancer | M3 eye 30 mm above the hub axis on the pod; M3 eye on the sector at 30 mm; zero-length spring (pre-tensioned extension spring + Dyneema) | — | HALO |
| M5 | Bail ↔ carriage | carriage rides the Ø 10 tube on 4 POM V-rollers (groove R 5.2) on Ø 3 pins; the tendon clamps under an M2 plate | — | HALO |
| M6 | Carriage ↔ float | 2 × M3 on 24 mm + Ø 4 dowel; float axis radial through O within 1° | carriage underside | HALO |
| M7 | Float ↔ pad (RCC ring) | **3-ball kinematic mount**: Ø 5 steel balls on the float ring (Ø 110, 120°) into 3 printed V-grooves on the RCC top ring; 3 × N52 Ø 6 × 3 hold ≈ 6 N; pad breakaway ≥ 6 N axial / ≈ 2 N·m | the ball triangle defines the pad frame P | PAD (groove side), HALO (ball side) |
| M8 | Pin cartridge ↔ pin block | Ø 10.0 × 34 mm cartridge in a Ø 10.1 bore; 1 × 8 × 1 O-ring retention; bayonet cap; 18.0 ± 0.1 mm grid | block underside plane | PAD |
| M9 | Nail stick ↔ pin (TM1-P) | Ø 1.0 shaft through the PTFE guide; a piston clip (E-clip groove) is the positive retention; lifted out after a ¼-turn of the bayonet cap | piston top face | PAD |
| M10 | Slave cylinder ↔ deck | 2 × M3 on 16 mm per cylinder; bell-crank pivots MR63 on Ø 3 pins; ball links M2 | deck top | PAD |
| M11 | Helmet plug ↔ halo rear node | 4 × M3 on 50 × 20 mm | node face, 2 × Ø 4 dowels | HALO (node), DRIVE BOX (plug design) |
| M12 | Plug face (both ends) | 64 × 34 mm face; 20 ports on a 2 × 10 grid at 6.0 mm pitch; 6 pogo contacts at 2.54 mm; 2 × Ø 4 × 8 dowels; 2 mm 30A silicone gasket on the helmet side; helmet end 4 × N52 Ø 10 × 3 (12 ± 3 N); box end 2 draw latches (≥ 40 N) | dowel pair | DRIVE BOX |
| M13 | Hanger | 8 mm fibreglass rod, 700 mm, spring clamp (25–60 mm jaw); 3 N magnetic tube clip (Ø 18 sleeve saddle) | — | DRIVE BOX |
| M14 | Box mounting | rear plate 4 × M5 inserts on 200 × 120 mm for the chair-back hook plate; 2 × 40 mm strap slots; 4 sorbothane feet; top handle | box rear face | DRIVE BOX |
| M15 | Twin tee manifold boss | 2 × M3 on 40 mm on the rear node, 12-port tee block footprint 50 × 20 mm | node face | HALO |

### 5.2 Pneumatic

| ID | Line | Tube | Length | End fittings | Pressure range | Owner |
|---|---|---|---|---|---|---|
| A1–A12 | Pin lines | PU 3.0 × 2.0 mm | 1.40 m box plug to helmet plug; + 0.30 m helmet plug to pad manifold; + 12-lumen flat loop 0.12 m to the block | barbs Ø 2.2 (plug, manifold); S070 port per order code [VERIFY]; printed barb into the pin cap | −8 to +27 kPa | DRIVE BOX (to helmet plug), PAD (beyond) |
| A13 | Palm A | PU 3 × 2 | 1.40 + 0.25 m | barb | 0–20 kPa | DRIVE BOX / HALO |
| A14 | Palm B (twin) | PU 3 × 2, blanked port | — | — | 0–16 kPa | — |
| S1–S3 | Synchro A | PU 4 × 2.5 | 1.40 + 0.30 m (**master-to-slave length matched ±10 mm**) | 4 mm push-to-connect at the box; barbs Ø 2.6 at the plug | 0–28 kPa sealed | DRIVE BOX / PAD |
| S4–S6 | Synchro B (twin) | PU 4 × 2.5, blanked ports | — | — | — | — |
| E1–E3 | Egg chambers | PU 3 × 2 | 1.5 m in the controller lead | barb | 0–100 kPa | ELECTRONICS |
| — | Internal box | PU 3 × 2 and 4 × 2.5; printed manifolds with O-ring face seals (2.0 × 1.0 mm O-rings) | — | — | — | DRIVE BOX |

**Port map on the plug (row A / row B):** A1–A10 = pins 1–10. B1–B2 = pins 11–12. B3 = palm A. B4 = palm B (blank). B5–B7 = synchro A. B8–B10 = synchro B (blank).

**Seal spec:** ≤ 0.2 kPa/min decay per synchro line at 25 kPa; pin lines ≤ 1 kPa/min.

### 5.3 Electrical

| ID | Interface | Voltage / current | Connector | Wires |
|---|---|---|---|---|
| E1 | Adapter → box | 12 V DC, 5 A (Mean Well GST60A12-P1J class, UL/CE) | 5.5 × 2.1 mm barrel, panel jack with strain relief | 2 |
| E2 | Actuator rail (internal) | 12 V switched; fuse 5 A at the inlet, 1 A per pump branch, 2 A for the stepper VM, 3 A for the servo buck | Wago / screw blocks inside a printed cover | 18 AWG trunk |
| E3 | Servo bus (to helmet) | 6.0 V buck (3 A, after the rail), TTL half-duplex 1 Mbps | helmet plug pogo 1 (6 V), 2 (GND), 3 (DATA) | 3 |
| E4 | Helmet loop | 3.3 V, 1 mA logic loop through both plugs; gates the rail-enable MOSFET | pogo 4, 5 | 2 |
| E5 | Spare | — | pogo 6 (future shell IMU, leap3-C C2) | 1 |
| E6 | E-stop puck | rail current through the NC contact (≤ 5 A rated, 10 A part) | GX12 4-pin (2 used + 2 sense) | 4 |
| E7 | Hand controller | hold-to-run NO in rail series (≤ 5 A microswitch); egg tubes alongside | GX12 4-pin + 3 tubes | 4 |
| E8 | Hard-squeeze switch PS1 | NC, opens > 40 kPa, in rail series, ≥ 5 A | internal | 2 |
| E9 | Logic supply | 5 V buck from the 12 V input **before** the safety loop → ESP32-S3 5 V pin | — | — |
| E10 | PC | USB-C (the ESP32-S3 native USB), logic-domain only | USB-C | — |

**Wires through the umbilical: 6** (6 V, GND, DATA, LOOP-out, LOOP-return, spare), 26 AWG, ≤ 1.5 A on 6 V (servo stall is current-limited at 1.2 A total).

### 5.4 Control

| Link | Bus / protocol | Rate | Notes |
|---|---|---|---|
| Valve outputs (20 used, 4 reserved for twin; 4th driver footprint) | SPI 10 MHz → 3 × TPIC6B595 (open-drain, 150 mA per channel, outputs disabled by /G tied to the rail-enable) | latched at 1 kHz; edges timed to 0.1 ms | de-energised = safe state for every valve |
| Pressure sensing (22 used, 2 reserved; 4th ADC footprint for twin) | SPI → 3 × MCP3208 12-bit | pins and synchro 1 kHz; others 100 Hz | XGZP6847A 0.5–4.5 V scaled to 3.3 V |
| Synchro master | STEP/DIR from MCPWM/RMT; TMC2209 UART (115 k) for current, stealthChop, StallGuard | step rate ≤ 6.4 kHz | phase = step counter |
| Travel servos | Feetech STS protocol, UART1 1 Mbps half-duplex (74LVC1G125 direction buffer) | sync-write goals 50 Hz; read position/current/temperature 25 Hz | Torque Limit, Protection Current and angle limits set in EEPROM at INIT |
| Pumps | 3 × LEDC PWM 20 kHz → logic-level MOSFETs | PID 1 kHz (rail), 100 Hz (palm, vac) | — |
| PC | USB CDC 921,600 baud, line protocol (§8.7) | telemetry 10 Hz + events | — |
| Storage | microSD (SPI) | session logs | — |
| Watchdog | GPIO toggled at 1 kHz from the core-1 loop → charge pump → rail-enable MOSFET gate | loss of toggling for > 20 ms opens the rail | hardware |

---

## 6. Drive box portability (binding)

**Targets:**
- **300 × 220 × 110 mm, ≤ 2.5 kg** (contents ≈ 1.5 kg + enclosure ≈ 0.8 kg [EST]);
- ≤ 32 dBA at 1 m in operation;
- works in any orientation: no liquid, no gravity-referenced parts, pumps on 3-axis sorbothane;
- all user-facing items on 1.5 m leads.

| Placement | How it sits | Umbilical routing |
|---|---|---|
| **Desk / side table** | flat on 4 sorbothane feet (non-slip), beside the chair | hanger clamped to the desk edge or chair back; clip 100–200 mm above and behind the crown |
| **Chair back** | a printed or aluminium **hook plate** (M14) with two 30 mm-deep J-hooks over the chair-back top rail, plus a 40 mm strap with cam buckle around the chair back; the box hangs vertically against the rear face | hanger clamped to the chair-back top; riser ≈ 0.4 m |
| **Couch back** | flat on the couch-back cushion on its feet, plus a 600 mm non-slip mat strip; strap to a cushion if the couch back is narrow | hanger clamped to the couch frame or box handle; clip behind the head |

**Never tug the helmet:**
- **Riser.** The umbilical rises from the box to the 3 N clip (any route, any slack).
- **Free loop.** Only a **300–350 mm free loop** hangs from the clip to the helmet's rear-node plug.
- **Loose bundle.** Tubes lie loose in a knit sleeve, never tied or spiral-wrapped (bending torque ≤ 0.01 N·m at 60° head yaw; bonded would be 0.18 N·m; leap3-D D3).
- **Head share.** ≈ 20 g.

**Breakaway chain:**
1. The **3 N clip** pops first (stand-up or lean-back).
2. The **helmet plug** releases at **12 ± 3 N**. All pin, palm and synchro lines then open at the helmet face, so the pins vent, the pad retracts and the synchro goes slack. The loop wire breaks and the rail is cut.
3. The cradle form lock (≈ 10 N) is the last fuse. It sheds the helmet up and back, away from the face.

**At the box:**
- The box end is **latched** (≥ 40 N, two draw latches). It is the "single quick-release connector" for packing, not a fuse.
- Pulling it vents everything, as above.

**Leads and controls:**
- The 12 V adapter cord (1.8 m) and USB-C go to the box.
- The e-stop puck and hand controller leads come out of the **front face**, so they reach the lap and armrest whichever way the box sits.
- A status LED ring and a "box master" toggle (logic power only) are on the top face.

---
## 7. Safety architecture

**Principle (safety-requirements §5).** Every S ≥ 3 hazard is bounded first by a **mechanical constant**, second by **hardware electrical** means, and only third by firmware. Firmware is never credited alone (red line 13).

### 7.1 Hardware safety loop

```
 12 V adapter ─ F 5 A ─ E-STOP (NC, latching) ─ HOLD-TO-RUN (NO, palm lever) ─ PS1 hard-squeeze (NC)
            ─ RAIL-ENABLE P-MOSFET (gate held ON only while: watchdog charge-pump output present
                                       AND helmet LOOP continuous through both plugs)
            ─► ACTUATOR RAIL 12 V ─► valve drivers (TPIC6B595 VCC + /G), pumps P1–P3, TMC2209 VM,
                                      6 V servo buck, NO-dump valve coils
 12 V adapter ─ F 1 A ─ 5 V logic buck ─► ESP32-S3, sensors, SD  (never switched by the loop)
 Rail-sense divider → ESP32 (read-only). Nothing in the logic domain can energise the rail.
```

**What de-energises, and the resulting state:**

| Element | De-energised state | Effect at the head | Time |
|---|---|---|---|
| 12 pin valves (S070, NC to rail) | pin ↔ lift manifold | pins vent → force < 0.05 N | ≤ 20 ms |
| LIFT SELECT | lift manifold ↔ atmosphere | no vacuum hold; pins at hover/limp | ≤ 20 ms |
| RAIL DUMP (NO) | rail → atmosphere | no pressure source even if a pin valve sticks open | ≤ 50 ms |
| PALM 3-way + PALM DUMP (NO) + Ø 0.3 float bleed | palm line → atmosphere (3 paths) | **spring retracts the pad ≥ 25 mm** (fail-to-free) | ≤ 150 ms |
| SYNC DUMP 1–3 (NO) | synchro lines → atmosphere | block goes slack (no tangential drive) | ≤ 50 ms |
| SYNC CHARGE (NC) | closed | — | — |
| Pumps P1–P3 | off | no supply | immediate |
| Steppers (TMC2209 VM off) | free | master stops | immediate |
| Travel servos (6 V off) | torque off; gear-held; bail spring-balanced | carriage stays put; no fall | immediate |

**Restart rule.** When the rail returns, firmware goes to ARMING with the pad retracted and the pins parked. It reaches the scalp only through APPROACH: the hold-to-run held for 1 s, a 0.5 s force ramp, and 3 s still. **No resume into contact.**

### 7.2 Force caps

| Cap | Mechanism (constant) | Value | Backup |
|---|---|---|---|
| Normal, per nail | rail relief R1a, independent R1b | 0.96 N / 1.04 N | pump stall 53 kPa = 2.04 N ≤ 2.5 N |
| Normal, total on scalp | palm-float relief R2 (the float holds the pad; pins cannot exceed it) | ≤ 7.2 N single; twin R2 15 kPa → ≤ 11.2 N for both pads | independent R2b 22 kPa (twin 16): ≤ 7.8 N single, ≤ 11.9 N twin at a double fault; without R2b, a stuck R2 plus pump stall (53 kPa) would reach 17.5 N, so R2b is mandatory |
| Tangential, per nail | normal cap × µ ≤ 1.0 + neck yield at ≈ 0.75 N + lean stop | ≤ 1.0 N | — |
| Tangential, pad | synchro relief p₀ + 8 kPa per line | ≤ 2.5 N per line, ≤ 4 N per pad | drag-sensor snag reflex (firmware) |
| Pad / helmet structural contacts | pads ≥ 25 mm wide, closed-cell; dial preload ≈ 4 N per pad | ≤ 5 kPa sustained | — |
| Fault force at the head | KE 0.4 mJ moving group; servo current limit 0.6 A | ≪ 65 N | servo Protection Current |

**Change made by this spec:** the palm circuit carries **two independent reliefs, R2 (20 kPa) and R2b (22 kPa)**. Total load at a double fault is then 22 kPa × 3.14 cm² + 0.9 N = 7.8 N ≤ 12 N.

### 7.3 Hair rules applied

| Rule | How SP1 meets it |
|---|---|
| No gaps 0.04–3 mm within 25 mm of scalp; no changing gaps (H-4.9) | Below 32 mm only the shafts (behind sealed wipers), nails and skid stems exist. The wiper is zero-gap. The block-to-deck gap (≥ 5 mm) is at ≥ 32 mm. Skid stems are static. |
| No rotation within 30 mm unless sealed (red line 1, H-6.1) | Nothing rotates below the deck. Bell cranks and MR63s are under the deck cover at ≥ 45 mm. Hub bearings are sealed at ≥ 60 mm from the canal and outboard of the head. |
| Lift before reversal (H-5.2) | Line ends are crossed in hover (zero force, 5 mm up) or park. Firmware forbids a window containing a velocity reversal. A missed lift (pin sensor still at rail after t_off + 30 ms) → all-lift + rail dump. |
| Lift kinematics (H-5.3) | Lift at v ≥ 0.53 v_peak; land at plough-in ≤ 35° (§4.1) |
| Rigid group, no scissoring (H-5.6) | All pins on one rigid block; spacing never changes |
| Circles (H-5.7) | Pins exit the canopy once per revolution (C19); circle mode is gated by canopy depth ≤ 12 mm and R ≥ 8 mm. Nothing hair-facing orbits below 32 mm except the shafts and nails. |
| Dwell / matting (H-5.5) | Ledger hard counter: ≤ 8 strokes per ±15 mm patch, then a move ≥ 20 mm or a with-grain comb-out |
| With-grain bias (H-5.1) | Grain map from the scan; against-grain only ≤ 25 mm and with lift |
| Snag reflex (H-5.9, H-6.6) | Synchro drag spike > 3× baseline or > 0.8 N → all pins vent within 30 ms, master holds, float retracts 10 mm; never reverse |
| Breakaway (H-4.13) | Neck plastic yield ≈ 0.75 N; pad kinematic mount ≈ 6 N; no tethers |
| Cleanability (H-6.7) | Pad lifts off its magnets tool-free; nail sticks drop out; deck cover snaps off; hair audit per session |

Checklist self-score (H-6.8), carried to Stage B:
- **Items scoring 2:** 1, 2, 3, 4, 5, 6, 9, 10, 12, 13, 14, 15, 17.
- **Item 7 scores 1:** 0.15 N yield is approached only by the 0.12–0.2 N/mm shaft and neck compliance; no design meets it.
- **Item 8 scores 2:** the nail protrudes 32 mm beyond the block.
- **Item 11 scores 1:** the neck yields rather than detaching.
- **Item 16 scores 1:** POM is not ESD-grade; the steel shaft is grounded through the piston clip [VERIFY].
- **Item 18 scores 1:** design basis is 2–8 cm hair; circle mode only ≤ 12 mm canopy.
- **Total ≈ 32/36.**

### 7.4 The 13 red lines, mapped

| # | Red line | SP1 design answer | Verified at |
|---|---|---|---|
| 1 | No exposed rotation within 30 mm of hair; no open slot | §7.3: no rotation below 45 mm; no slots; sealed hubs outboard | Stage B gap probe, Stage C wrap test |
| 2 | Per-element normal force ≤ 2.5 N by a mechanical constant | R1a/R1b reliefs (0.96 N); pump stall 2.04 N | Stage A relief calibration, Stage B load cell |
| 3 | ≤ 12 N total; ≤ 2 N tangential per element | Palm reliefs R2/R2b (≤ 7.8 N); synchro reliefs; neck yield | Stage B: all 12 pins + palm at relief on a load cell ≤ 12 N; drag cap test |
| 4 | NC e-stop in series + hold-to-run | §7.1 | Stage A loop tests |
| 5 | No mains, ≤ 24 V, no lithium | external certified 12 V adapter; no cells anywhere | Stage A visual |
| 6 | Nothing moving anterior to the hairline, within 25 mm of the canal, or above the eyes without a guard | hard stop α ≥ −35° behind the fixed front band (the guard); β ≤ ±60° keeps ≥ 39 mm from the canal; hubs static at ≥ 60 mm | Stage C fence measurement with the halo displaced ±15 mm |
| 7 | No self-locking drive in the force path without a downstream spring cap and spring-return lift | The force path is pins (air) and float (air + spring). The geared servos are in the tangential travel path only; pad lift is a spring on vent. | Stage B power-pull test |
| 8 | Nothing held in contact after power loss, e-stop, watchdog or stall | §7.1: vent + pad retract + per-pin bleed + palm bleed | Stage B/C fault injection |
| 9 | No push-fit-only, PLA or resin tips; proof 3× | POM nails, hooked and filleted necks, piston clip; proof 1.5 N axial, 1.0 N lateral | Stage B per-stick proof |
| 10 | One-handed doff ≤ 3 s; breakaway chin strap only; ≤ 500 g | no chin strap; form lock ≈ 10 N; 352 g; doff §7.6 | Stage C timed doffs |
| 11 | Edges ≥ 1 mm (tips ≥ 0.4) and the tape test | nail rim R 0.4 (loupe vs a 0.8 mm drill shank); all other skin-side edges R ≥ 1 | Stage B tape test |
| 12 | First session only with the checklist, wig test, glasses, ≤ 5 min | Stage D entry gate | Stage D |
| 13 | Firmware never the only barrier for S ≥ 3 | every S ≥ 3 row in §7.5 has an M or E control | Safety Gate |

### 7.5 Hazards (safety-requirements §1) mapped

| H | Hazard | Mechanical / electrical control in SP1 | Firmware layer |
|---|---|---|---|
| H1 | Entanglement | No rotation in the zone; shafts behind wipers; circle-mode exit rule; pad breakaway 6 N | snag reflex; ledger |
| H2 | Strand pulling | omni-nail with no hooks, R 0.4; lift before reversal by hover; neck yield | missed-lift → all-lift |
| H3 | Excess normal force | R1a/R1b, R2/R2b | rail clamp 15.6 kPa |
| H4 | Excess shear | synchro reliefs; µ × capped normal; neck yield | drag-sensor trip |
| H5 | Sharp edges | R ≥ 1 skin-side; tape test | — |
| H6 | Pinch | bail/pod gap ≥ 25 mm or ≤ 4 mm; carriage covered; pad deck cover | — |
| H7 | Motor stall | relief-capped master (cannot stall on load); servo Protection Current + overload cut; fuses | StallGuard / current trip → FAULT |
| H8 | Runaway | hard stops on α, β; the force cap is independent of motion | angle limits in servo EEPROM; one clamp point |
| H9 | Printed part failure | ≥ 4 perimeters; proof 2× (bail node 10 N, cradle 20 N); inspection log | — |
| H10 | Loose fasteners | inserts + threadlocker; torque marks | — |
| H11 | Broken tips | POM nails; proof 3×; red/orange bodies; count sticks per session | — |
| H12 | Abrasion | moving contact only; force caps; finish Ra ≤ 0.8 | ledger ≤ 50 passes/min/spot; dwell ≤ 1 s loaded |
| H13 | Sustained pad pressure | pads ≥ 25 mm, closed-cell, ≤ 5 kPa; skids 0.15 N on ≥ 50 mm² | 20 min session cap |
| H14 | Mains | external certified 12 V adapter only | — |
| H15 | Shorts / overheating | per-branch fuses; sleeved harness; strain relief at every moving wire (2 at hubs) | servo temperature read |
| H16 | Back-EMF | TVS + 470 µF on the rail; flyback diodes on all valve coils (TPIC6B595 internal clamp + external SS14) | — |
| H17 | Lithium | none | — |
| H18 | Eyes / ears | front band is the fixed guard; hubs static; ear fence ≥ 39 mm | soft fences from the scan |
| H19 | Failed e-stop | NC latching e-stop + hold-to-run + egg switch, all in series; watchdog opens the rail | rail sense → PAUSED |
| H20 | Hygiene | removable pad, nail sticks, washable sleeve; IPA-wipeable POM/PETG/silicone; sealed prints | — |
| H21 | Hot parts | servos ≥ 60 mm from the canal, ≤ 0.5 W typical; no other heat on the head | servo temperature trip 50 °C |
| H22 | Noise | §4.8 | — |
| H23 | Head-mounting | 352 g; form lock; no strap; falls away from the face | — |
| H24 | Cannot remove quickly | §7.6 doffing; release = vent + retract | — |
| H25 | Firmware faults | everything above holds with the MCU dead (watchdog opens the rail) | WDT, clamps, timeouts |

### 7.6 Doffing (≤ 3 s, one hand, eyes closed)

1. **Release the palm lever** (hold-to-run). Pins vent in ≤ 20 ms and the pad retracts in ≤ 150 ms.
2. **Grab the front band handle** (0.5–0.8 s).
3. **Tilt up and back.** The cradle slides off the occipital shelf (≈ 10 N) in ≈ 0.5 s.

Total ≈ 1.2–1.8 s [EST]. The umbilical stays plugged in, and the clip carries it.

**Gate:** 10 timed eyes-closed trials on phone video, all ≤ 3 s, and a luggage-scale lift at the band ≤ 20 N.

### 7.7 Failure modes and states

| Failure | Detection | State reached | Bound |
|---|---|---|---|
| Pin valve stuck energised | pin sensor ≠ command for > 30 ms | FAULT: all valves off, RAIL DUMP open, master holds, pad retracts | that pin ≤ 0.96 N until the rail dumps (≤ 50 ms) |
| Pin valve stuck de-energised | no pressure rise on command | pin disabled, logged; play continues with 11 | benign |
| Pin line kinked (pressurised) | blind at the box | per-pin bleed vents it in < 1 s; pad retract on any stop | ≤ 0.96 N, < 1 s |
| Synchro line kinked or leaking | drag sensor offset / re-zero failure | that axis freezes or goes slack; FAULT after 2 failed re-zeros | ≤ 4 N tangential |
| Palm line kinked | S22 pressure with PALM off | float bleed vents within ~2 s; FAULT; user doffs | ≤ 7.8 N total |
| Rail pump stall | S13 below setpoint for > 0.5 s | FAULT; nails weaken (benign) | — |
| Vacuum pump stall | S14 > −4 kPa | circle mode disabled; hover only | — |
| Stepper stall / skipped steps | StallGuard, home check every rest | FAULT → re-home | relief-capped |
| Travel servo stall | Protection Current; position error > 3° for 300 ms | FAULT: pins vent, pad retracts, servo torque off after 1 s | KE 0.4 mJ |
| Power loss | — | everything de-energised (§7.1) | free |
| Helmet plug pulled | loop open → rail cut; helmet ports open | free | 12 ± 3 N pull |
| Box plug pulled | same | free | — |
| Firmware hang | watchdog charge pump stops → rail opens | free | ≤ 20 ms |
| Halo knocked / slipped | registration residual > 2 mm at 3 stations, or a head jerk > 60 rad/s² | PAUSE → re-register | fences move with the halo |
| Bail hits a headrest | servo current spike | stop; reclined mode caps α ≤ 75° | — |
| User falls asleep | hold-to-run released → rail off; 20 min session timer | free | — |

---
## 8. Firmware architecture

**Platform:** ESP32-S3, Arduino-ESP32 core 3.x with FreeRTOS, written in C++. The safety-relevant code is reused from 05-engineering/electronics-firmware.md, ported:
- the single limits table printed at boot;
- one clamp point;
- the settings code (hash) on every log line;
- the BLIND / `bset` / `reveal` experiment machinery;
- the rail-sense → PAUSED rule;
- "no restart without an explicit act".

| Task | Core | Rate | Job |
|---|---|---|---|
| RT loop | 1 | 1 kHz (esp_timer) | sensor scan (pins, synchro), valve edge queue, rail / palm / vac PID, step-rate updates, watchdog toggle, trip checks |
| Bar engine | 0 | per bar (one master cycle, 0.5–4 s), plus 100 Hz | phrase → bar → gate tokens; travel goals; ledger update |
| Servo bus | 0 | 50 Hz write / 25 Hz read | α, β (and α_R) |
| Comms / log | 0 | event-driven, 10 Hz telemetry | serial parser, SD writer |

### 8.1 State machine

```
 BOOT ─► SELFTEST (rail off: sensor zeros, valve-off readback, SD, servo ping skipped) ─► SAFE
 SAFE ── rail present ─► ARMING: dumps close, pumps charge rails, vac to −8, synchro DUMP→CHARGE re-zero,
         servos torque on (limits written), master homes, pins PARK, float retracted, pin latency self-cal
 ARMING ─ ok ─► READY (pad parked at vertex, retracted)
 READY ─ first use ─► SCAN (≈5 min) ─► READY        READY ─ each session ─► REGISTER (15 s)
 READY ─ hold-to-run held 1 s ─► APPROACH: float extends to skid contact (palm ramp 0.5 s), pins land at
         0.10 N (0.5 s ramp), 3 s still ─► PLAY
 PLAY ⇄ REST (P5: pins hover/park, master to centre, synchro re-zero, ≤ 3 s)
 PLAY ─ score end / 'stop' / 20-min cap ─► RETRACT (pins park, float retract, travel to vertex) ─► READY
 any ─ rail lost ─► PAUSED (hardware already vented) ─ rail back ─► ARMING   (never straight to PLAY)
 any ─ trip ─► FAULT (all outputs off, servos torque off after the carriage stops, master off; LED 10 Hz;
         only 'reset' leaves → SAFE)
```

**Trips (each → FAULT):**
- pin command/sensor mismatch;
- rail / palm / vac out of band for 0.5 s;
- synchro drag above the snag threshold three times in 10 s;
- servo error, overload or temperature ≥ 50 °C;
- stepper stall or a home check off by > 2°;
- bus timeout of 5 reads;
- loop-time overrun ×3;
- session > 20 min;
- egg hard-squeeze (the rail opens anyway; firmware latches FAULT to require `reset`).

### 8.2 The three drive modes (firmware view)

- Master phase is the step counters: θ_A = 2π·n_A/N, θ_B = 2π·n_B/N, with N = 3,200 µsteps per revolution.
- The path is z = 7.5·(e^{iθ_A} + e^{iθ_B}) mm, in the S frame.
- Mode parameters are those of §4.3.
- Firmware computes, for every future millisecond, the block position and velocity analytically, so the gate times are exact.

| Mode | Gate rule (per pin, per stroke) |
|---|---|
| PLINE / LINE | Normalised line coordinate s = x/15 along the current heading. **Land** where \|v_t\| ≥ max(1.4·v_descent, 0.3·v_peak), i.e. at s_land ≤ ±0.6 at 1.0 Hz and ±0.85 at 2.0 Hz. **Lift** at \|s\| = 0.85, in the same half-stroke. Both flanks (bidirectional), outbound only, or alternating sets above 1.7 Hz. Hover or park through every end zone. |
| CIRCLE | Window 60–90° of phase centred on the chosen heading. After the window: park (vacuum), then descend again at 50 mm/s so that the landing angle is ≤ 35°. Requires R ≥ 8 mm and canopy ≤ 12 mm. |
| P2 sweep | Master parked at centre. All chosen pins land, then travel moves 60–150 mm with-grain at 40–80 mm/s, then lift. Return is lifted. |

**Virtual hand (pin selection).**
- A lookup table maps heading (5° bins) to a ranked list of 3- and 4-pin rows of the 12-pin grid, ⟂ the heading, with gaps 14–28 mm and stagger ≤ 12 mm (leap2-B L3).
- The active row steps 1 pitch (18 mm) along the heading at most every 8 strokes. In PLINE, the row table is re-indexed as ψ turns.

### 8.3 Per-pin gate timing

For each stroke token (pin k, landing phase φ_L, lift phase φ_U, rail level, onset jitter σ):

```
 t_open(k)  = T(φ_L) − L_bite(k)  + N(0, σ_t)        // σ_t 20–80 ms, redrawn every stroke (scratch-model §4.2)
 t_close(k) = T(φ_U) − L_lift(k)
 reject token if t_close − t_open < L_bite(k) + 60 ms, or if window crosses a velocity reversal or self-crossing
 L_bite(k), L_lift(k) = per-pin calibrated latencies (edge → contact, edge → force < 0.05 N), re-measured at ARMING
   on the parked pad (descent time to the park stop) and corrected online from the box-side flow signature
```

**Rail level per stroke:**
- F_target is drawn from N(F_phrase, σ_F·F_phrase), with σ_F 0.1–0.3, clamped to [0.08, 0.60] N.
- The rail setpoint is F/A. It is slewed during the end zone (≤ 60 ms up; ≤ 3 kPa down per stroke).

**Constant-support gait (leap3-C C1):**
- Σ F_active is kept within ±0.15 N inside a phrase: set A lifts as set B lands.
- The palm setpoint = Σ F_scheduled + 0.45 N + F_spring(x) − m g·n̂(α, β), as feed-forward.

### 8.4 Score format: κ-grammar + fatigue ledger ("SCORE v1")

A score is a JSON-lines file. Line 1 is the header, then phrases; it is streamable over serial as the same JSON. The κ knob is κ = v_drift / v_peak.

```json
{"score":"evening-01","v":1,"seed":2024,"map":"mt-2026-10-05","intensity":1.0,"cap_min":20}
{"ph":1,"prim":"P6_ARRIVE","reg":"VERTEX","mode":"PLINE","f":1.0,"eps":0.025,"F":0.12,"sF":0.0,"sT":0,"pins":"ROW3","win":"FLANKS","drift":null,"D":4}
{"ph":2,"prim":"P1_RAKE","reg":"OCC_U","mode":"PLINE","f":1.4,"eps":0.025,"psi":"GRAIN","F":0.30,"sF":0.20,"sT":40,"pins":"ROW4|ROW3","win":"FLANKS:0.6-0.85","drift":{"to":[60,0],"v":25},"D":9}
{"ph":3,"prim":"P5_REST","D":0.8}
{"ph":4,"prim":"P2_SWEEP","reg":"PAR_L","mode":"PARK","F":0.20,"pins":"ROW3","sweep":{"from":[20,35],"to":[70,45],"v":60},"n":3}
{"ph":5,"prim":"P3_CIRCLE","reg":"VERTEX","mode":"CIRCLE","R":12,"f":0.8,"F":0.25,"win":"ARC:75","drift":{"v":30},"D":5,"needs":"canopy<=12"}
```

**Phrase fields** (leap2-D D1, re-expressed for the puppet line):

| Field | Meaning |
|---|---|
| `prim` | P1 rake, P2 sweep, P2′ bending sweep, P3 travelling circle, P4 spider (alternating single pins, short windows), P5 rest/lift, P6 arrive/build, P7 slow CT trace, N1 hover spiral (drift circles a target at R 15–25), N2 tease→relieve (opt-in) |
| `reg` | region from the head map |
| `mode`, `f`, `eps`, `psi`, `R` | §4.3 |
| `F`, `sF` | phrase force and per-stroke spread |
| `sT` | landing jitter (ms) |
| `pins` | row rule |
| `win` | window rule |
| `drift` / `sweep` | travel |
| `D` | dwell (s) |
| `needs` | precondition checked against the map |

The firmware invariant of leap2-D §1 (no loaded reversal or self-crossing; speed ≥ 0.3 v_peak; heading turn ≤ 90° per window) is checked on every token.

**Fatigue ledger.**
- **Cells:** 15 mm cells on the head map, ≈ 255 cells over 575 cm².
- **Per cell:** stroke count per ±15 mm patch (hard ≤ 8), passes per minute (hard ≤ 50), F_CT (τ 20 s), familiarity h per feature (τ 90 s), satiety minute index.
- **Filter:** each candidate phrase is scored against the ledger before play. It must change ≥ 2 features with h > 0.5; continuous parameters follow pink noise.
- **Session envelope:** novelty is scheduled at minutes 3–6; the band 20–50 mm/s is held to ≤ 40 % of any 60 s.
- **Rejection:** a rejected phrase falls back to P5 lift.

**Attention layer (leap2-D D2, driven by the egg).** STAY / RETURN / BUILD / RELEASE / WANDER behaviours, with a 0.4–1.5 s response lag, p 0.6–0.8, and at most one overt response per 20–30 s. The per-region learner (D3) is **off in SP1 firmware v1**; the hooks and log fields exist.

### 8.5 Squeeze egg

The 3 chambers are FRONT, BACK and TOP; nubs give orientation by feel. Each chamber reads 0–100 kPa, with a 0.3 mm bleed giving τ ≈ 2 s.

| Gesture | Threshold | Response |
|---|---|---|
| Light squeeze any chamber | 5–15 kPa, < 0.6 s | "THERE": 150 ms all-hover acknowledgement after 0.4–1.0 s, stay 6–10 s varying one feature, tag the cell a hit |
| Hold FRONT / BACK / TOP > 1 s | > 5 kPa held | "THAT WAY": drift 20–30 mm/s toward the forehead / occiput / the side the TOP nub faces; overshoot 10–15 mm, then an N1 search spiral; a light squeeze fixes the centre |
| Double squeeze | 2 events < 0.8 s | "NOT THERE": move ≥ 50 mm, mark the cell −1 |
| Hard squeeze | > 40 kPa | PS1 opens the rail (hardware); firmware latches FAULT |

Labels are logged for the D3 learner (SP1 v2 firmware).

### 8.6 Head scan (first use) and registration (each session)

**Scan, ≈ 5 min, ≈ 18 stations at 50 mm spacing** (crown, top, upper parietals, upper occiput):
1. **Shape.** All 12 pins park, then descend together at the scan rail (4 kPa, 0.15 N). Per-pin contact time from the box flow signature × calibrated descent speed gives the heights (±0.2 mm [VERIFY]). A quadric fit gives the local normal (±1°) and curvature.
2. **Canopy depth.** The pin height at contact relative to the skid plane gives canopy depth (±2 mm). This sets the circle-mode permission (C19) and the hover depth.
3. **Grain.** Two lifted-ends 25 mm LINE strokes in each of 8 headings at 0.2 N; drag from the 3 synchro sensors gives a drag rose → grain heading ±15° and strength (leap3-C C4). The field divergence gives the whorl ±5–10 mm.
4. **Fences.** The pad drifts forward at 10 mm/s on the midline. Michael light-squeezes when he feels the front skid at his hairline; repeat for each ear side.
5. **Sensitivity (2 min).** Rakes at 0.15 / 0.30 / 0.45 N at 6 region centres. A squeeze means "too much"; a double squeeze means "too light". This sets the per-region force box.

**Registration, 15 s:** one drag rose near the stored whorl plus 3 profile stations → seating offset (yaw ±1°, fore-aft ±3 mm). Soft fences and ledger cells shift with it.

**Slip watch:** a residual > 2 mm at ≥ 3 consecutive stations → PAUSE + re-register.

### 8.7 Serial command interface (USB CDC, 921,600 baud, newline-terminated)

| Group | Commands |
|---|---|
| State | `help` `status` `limits` `arm` `play` `stop` `rest` `retract` `reset` `zero` (servo zero on the jig) |
| Drive | `mode pline\|line\|circle` `f <Hz>` `eps <ε>` `psi <deg>\|grain` `R <mm>` `hold` (master to centre) |
| Force | `force <N>` `sF <0..0.3>` `sT <ms>` `rail <kPa>` (direct, clamped) `palm auto\|<kPa>` |
| Pins | `pins <mask>` `row auto\|<id>` `win flanks\|out\|alt <s_land> <s_lift>` `park` `hover` |
| Travel | `goto <α> <β> [v]` `drift <dα/s> <dβ/s>` `sweep <α1> <β1> <α2> <β2> <v>` `fence show` |
| Score | `score load <file>` `score play\|pause\|next` `ledger on\|off` `attn on\|off` `seed <n>` `intensity <0.5..1.5>` |
| Scan | `scan` `register` `map save\|load <id>` `grain show` |
| Calibrate | `cal pins` (latency, descent) `cal synchro` (re-zero, viscous model, area ratio) `cal egg` `cal palm` |
| Experiment | `bset <slot> <json-overrides>` `blind <n>` `next` `reveal` `unblind` (as electronics-firmware §5.4) `rate <0-10>` (logs a rating line) |
| Diagnostics (rail on, pad retracted only) | `valve <k> <ms>` `sensors` `pump <n> <duty>` `servo <id> ping\|temp` `twin on\|off` |
| Fault injection (dev build, wig head only) | `inject stuckvalve <k>\|snag\|stall\|hang` |

**Log lines** (CSV, first field is a letter, t in ms):

| Line | Content |
|---|---|
| `H` | 1 Hz health: state, mode, f, ε, F, rail, palm, vac, α, β, servo temperatures, fault, settings code |
| `B` | per bar: phrase id, heading, active pins, windows, rail per stroke, drag vector mean/peak, ledger flags |
| `G` | per gate, optional: pin, t_open, t_close, measured landing, measured lift |
| `P` | pressures at 100 Hz, optional |
| `E` | egg events |
| `F` | faults |
| `C` | full settings behind a code |
| `S` | session marks and ratings |

Logs go to SD and to the PC at once.

---
## 9. Second-pad provisions

**Twin concept (leap3-A L2):**
- Pad B rides the right half-bail at **(−α, −β)**, a point mirror, so the CoM stays within ≈ 7 mm of the vertical and the worst lean falls from 0.24 to 0.03 N·m.
- Pad B's pins share pad A's 12 valves (lockstep).
- Pad B has its own 3 synchro lines from the second master triad, and its own palm line.
- The collision guard holds |β| ≥ 8° per side near the vertex.

### 9.1 Pre-built into SP1 now

| Item | Where | What it is |
|---|---|---|
| Split bail | HALO | two half-bails joined by a bolted nylon **vertex splice** (2 × M3), smooth for the carriage to roll over |
| Right pod pitch bay | HALO | identical to the left: shaft, 2 × 6800, capstan sector and balancer; in single mode the right half-bail is **locked to the left** by the splice, and the bay holds a dummy cartridge |
| β drum | HALO | Ø 20 **double-groove** drum and idlers at both legs, ready for a crossed loop (β_R = −β_L) |
| Servo bus | HALO | daisy-chain socket in the right pod; firmware already supports ID 3 = α_R |
| Plug blocks | DRIVE BOX | 20 ports: palm B and synchro B (3) blanked with printed plugs |
| Master | DRIVE BOX | master plate with **6 cylinder mounts and 6 bell cranks**; triad B cylinders unfitted, ports capped |
| Box channels | ELECTRONICS | outputs 21–24 reserved (PALM B, PALM B dump, synchro B dumps 1–2) plus a 4th TPIC6B595 footprint (synchro B dump 3, spares); sensor channels 23–24 plus a 4th MCP3208 footprint (palm B line, synchro B 1–3); firmware stubs |
| Tee manifold boss | HALO | rear-node mount for a 12-port tee block (M15) |
| Relief documentation | DRIVE BOX | twin settings: R2/R2b → 15/16 kPa per pad (firmware max 3 pins down per pad); pin rail unchanged |

### 9.2 Bought now (in the cost roll-up, §13)

- 1 × STS3032 (α_R).
- **Pad B kit:** 12 nail sticks, 12 pin cartridge parts, 3 slave cylinder diaphragms (cast from the shared kit), skids, struts, PP sheet, kinematic balls and magnets.
- **Carriage B and float B parts:** rollers, guide rods, spring, diaphragm.
- **3 master cylinders** for triad B.
- **Twin plumbing:** 12 brass tees, 24 per-pin restrictors (Ø 0.25, so each pin is metered at its own inlet in twin), 1 cheap 3-way (PALM B), 1 NO dump (palm B), 3 NO dumps (synchro B), 4 sensors (palm B line, synchro B 1–3), 1 × MCP3208 + 1 × TPIC6B595, 4 m PU 4 × 2.5, 2 m PU 3 × 2, 2 m sleeve.
- 2 m Dyneema for the crossed loop.

### 9.3 Install steps (later, ≈ one weekend)

1. Print the pad B block, deck and carriage B (same files, mirrored where marked). Build pad B as pad A (PAD WP procedure).
2. Fit the triad-B master cylinders. Run 3 new synchro lines and the palm B line. Re-sleeve the umbilical (20 tubes) and unblank the 4 plug ports.
3. Fit the 12-port tee block on the rear node. Re-route pin lines A1–A12 through it, to pad A and pad B. Fit the Ø 0.25 per-pin restrictors at both pads' inlets. The box-side sense orifices stay; in twin each flow signature is the sum of two pins, so landing detection becomes per valve, not per pin.
4. Remove the vertex splice, fit end caps on both half-bails, and install the α_R cartridge in the right pod.
5. Re-reeve the β tendon as a crossed loop on the double drum (β_R = −β_L).
6. Set R2/R2b to 15/16 kPa on both palm circuits. Run the Stage B force audit on both pads together (≤ 12 N total at relief).
7. Firmware: `twin on`. Run the zero jig for α_R. Run the collision test at the vertex (|β| ≥ 8°).
8. Stage C mass and CoM checks: ≤ 480 g, coin-free lean test. Then repeat Stage D steps 1–3 before any twin session.

---

## 10. Build staging with go/no-go gates

Every stage uses the real parts; there is no hand wand. A stage passes only when every gate line holds. A failed gate goes back to the owning work package (§11).

### Stage A — drive box on the bench (weeks 1–3)

| Step | Build | Gate (pass line) |
|---|---|---|
| A0 | Power and safety loop on a board: adapter, fuses, e-stop puck, hold-to-run lever, PS1, rail MOSFET, watchdog, loop jumper | e-stop / lever / PS1 / loop open / `hang` each → rail 0 V within 1 ms (scope) and logic stays up; 10 cycles each |
| A1 | Pneumatics: P1 + rail accumulator + reliefs; P2 vac; P3 palm; sensors; 1 S070 and a test pin cartridge on a bench block | R1a opens at 25 ± 1 kPa, R1b 27 ± 1, R2 20 ± 1, R2b 22 ± 1 (5 trials each, against S13); rail PID holds ±0.3 kPa; step 5→12 kPa in ≤ 60 ms; RAIL DUMP to < 1 kPa in ≤ 50 ms on rail-off |
| A2 | **One-line synchro**: one master cylinder on a hand- or stepper-driven linear slide, 1.4 m PU 4 × 2.5, one slave cylinder on a linear slide with a felt pen | slave/master gain 0.98–1.02; stiffness ≥ 0.6 N/mm per line (kitchen scale); stick-slip jump ≤ 0.2 mm; leak ≤ 0.5 kPa/min; re-zero repeatable to ±0.2 mm |
| A3 | Full master (both stages, 3 cylinders) + real slave block on the pad deck, pens on the block, paper under it | **ink traces:** LINE bow ≤ 0.5 mm over 25 mm; circle R 12 roundness ±0.4 mm; 60 s PLINE rosette never retraces a stroke within 2 mm; shrink ≤ 1 mm with 0.5 N drag (50 g on a thread); drift ≤ 1 mm per 60 s between re-zeros; 1.4 Hz and 2.0 Hz |
| A4 | 12 pin valves + manifold + sense orifices + pin lines to a 12-pin test plate (pins of the real design) | each pin: hover holds 5 ± 1 mm, descent 50 ± 10 mm/s, latency calibrated ±5 ms, force at 10 kPa = 0.385 ± 0.03 N on a kitchen scale at 3 extensions; per-pin bleed: trapped 10 kPa < 2 kPa in < 1 s |
| A5 | Box enclosure, all in | box ≤ 32 dBA at 1 m running PLINE + pins cycling (phone SPL, A, slow); box mass ≤ 2.5 kg; runs on its back, side and face (orientation test) |

**Go/no-go A:** all gate lines pass. If A2/A3 fail on stick-slip or stiffness:
1. try Ø 24 cylinders + p₀ 40 kPa (needs a separate charge regulator);
2. else the pad-mounted twin direct-drive Tusi (leap3-B L2) becomes the scrub drive, and the halo mass budget is reopened.

### Stage B — pad with pins on a wig head (weeks 3–5)

Mount: the real carriage + float + pad on a **bench bail segment** (one half-bail clamped in a printed stand at R 210 over a wig head on a load-cell sled).

| Step | Gate |
|---|---|
| B1 Mass | pad ≤ 90 g; moving group ≤ 115 g |
| B2 Force audit | all 12 pins at R1a + palm at R2 on a load cell under a foam dome: total ≤ 12.0 N (expect ≤ 7.8); any single pin ≤ 1.0 N; tangential pad pull at the synchro relief ≤ 4 N |
| B3 Proof | every nail stick: 1.5 N axial, 1.0 N lateral, no set; pad kinematic mount releases at 6 ± 2 N; tape sharpness test on nails and skid domes |
| B4 Fail-to-free | pull power mid-stroke ×10, pull the helmet plug ×10, `hang` ×5: pad retracted ≥ 25 mm in ≤ 150 ms (240 fps), no pin in contact, no strand pulled |
| B5 Hair (hair-interaction §7) | real-hair wig at 3–5 cm and long, plus Kanekalon: 20 min PLINE + 5 min CIRCLE (R 12, canopy ≤ 12 mm wig) + 5 min LINE reversals: **zero wraps, zero gap captures, zero knots**; shed ≤ 2× the combing baseline; tweezer gap probe on every seam; snag yield ≤ 0.3 N with the 15 g / 50 g tether test |
| B6 Contact quality | hover-and-bite ink on moving paper: tapered entry streak (no dot), plough-in ≤ 35° at 1.4 Hz; skid load 0.45 ± 0.15 N through a constant-support phrase (scale under the skids); pad tilt < 2° under a 1.1 N pull at the nail plane (RCC) |
| B7 Forearm | volar forearm, 2 min at 0.15 N then 0.3 N: no erythema beyond 10 min, no abrasion; "nail or pad?" in 8 headings (omni-nail nail-like in ≥ 7) |
| B8 Thermal / noise at the pad | 20 min bench run: nothing on the pad above 30 °C; pad-side SPL with the box out of the room = room level |

**Go/no-go B:** all pass.
- If B5 fails on the block underside stirring hair: still-dome tilting pins (leap2-F L2) go into the PAD WP.
- If B5 fails only in circle mode: circle mode is restricted to canopy ≤ 6 mm or deleted for SP1.

### Stage C — halo with travel (weeks 5–7)

| Step | Gate |
|---|---|
| C1 Fit (Michael, no pad) | the dial cradle seats under the occipital shelf; bun free ≥ 60 mm above the cradle edge; 20 min with no pressure mark beyond 10 min; tip-off force at the front band ≥ 8 N |
| C2 Mass and balance | helmet ≤ 400 g on a kitchen scale; bail stays put ±5° unpowered at α 0/45/90° (spring balance) |
| C3 Lean test | coin bag = moving-group mass at the pad position; moved front / top / back every 2 min for 20 min of TV: lean ≤ 2/10, ink-line slip ≤ 1 mm, slip ≤ 3° (phone inclinometer vs a headband) |
| C4 Travel | drift 20–50 mm/s and sweeps 80 mm/s follow ±1 mm (pen trace on a wig head); hard stops hit before the firmware limits; ear fence ≥ 25 mm and hairline guard verified with the halo displaced ±15 mm |
| C5 Noise | at the tragus with travel running: within 3 dB of room level; **earplugs in, servo on vs off indistinguishable** (bone path) |
| C6 Umbilical | head share ≤ 25 g (kitchen scale at the clip); yaw torque at ±60° ≤ 0.02 N·m (luggage scale, 100 mm lever); clip pops at 3 ± 1 N; helmet plug at 12 ± 3 N; stand-up test ×5 → helmet stays on or sheds up and back |
| C7 Doffing | 10 eyes-closed one-hand trials ≤ 3 s, max ≤ 2.5 s |
| C8 Wig, whole system | 20 min on the wig head, full score, travel on: B5 pass lines again |

**Go/no-go C:** all pass.
- C5 bone-path fail: gimbal + FOC cartridges (M3 adapter C).
- C3 fail: twin conversion is brought forward, or a counter-mass on the β return run (leap3-E).
- C1/C3 slip fail: fit the 12 N magnetic-fuse chin elastic.

### Stage D — human sessions (week 7 on)

**Entry:**
- the safety-requirements §6 checklist is complete and signed;
- B5 and C8 passed;
- safety glasses on;
- e-stop puck in the free hand's reach;
- hold-to-run in hand.

| Step | Content | Stop rules |
|---|---|---|
| D1 | Scalp, 2 min: vertex only, LINE, 0.15 N, f 1.0 Hz, no travel | any pain, tuft pull, heat or loosening → stop; inspect scalp and wig-like hair audit |
| D2 | 5 min: PLINE default, drift on, 0.15–0.30 N | as above |
| D3 | 10 min: full region map, the egg live, the scan run | — |
| D4 | 20 min: score + ledger; feedback form (BRIEF §19 O) | — |
| D5 | Experiment matrix (TEST WP): PLINE vs LINE vs CIRCLE; force 0.15/0.3/0.45; landing jitter 0 vs 40 ms; omni vs directional nail; hover vs park-per-stroke; ledger on/off; blind slots | ≤ 1 variable changed per block |

**Go/no-go D (SP1 hypothesis):**
- **Realism:** "feels like a person's fingernails" ≥ 7/10 on the blind rating.
- **No machine reading:** "machine on my head" ≤ 3/10.
- **Want to repeat:** wants to wear it again tomorrow.
- **Safety:** zero tuft pulls over 5 sessions.

---

## 11. Work packages for the next phase

| WP | Scope | Inputs | Outputs | Owns interfaces |
|---|---|---|---|---|
| **HALO + TRAVEL** | Front band, dial cradle adaptation, temple pads, hub pods (both bays), motor cartridges (adapters A/B/C), capstan and drum, spring balancers, half-bails + splice, carriage, float, tendon routing, rear node, zero jig, hard stops | this spec §3, §4.6–4.8, §5.1; head scan of Michael (tape fit) | hub-pod, bail, carriage and float drawings; zero-length spring calculation; stiffness and proof calculations; assembly procedure; mass ledger by part | M1–M7 (ball side), M11 (node), M15; E3–E5 harness on the halo |
| **PAD** | Pin cartridge (diaphragm, piston, collar, restrictor/duckbill, bleed, guide, wiper, bayonet cap), nail sticks and variants (TM1-P), pin block, deck, slave cylinders + bell cranks, PP parallelogram, skids, RCC struts, pad manifold and flat tube loop, cover; casting moulds | §4.1, §4.4, §7.3; pin-unit.md; tip-interface.md | pad drawings; mould files; per-pin calibration procedure; tip proof procedure; hair checklist self-score; still-dome fallback sketch | M7 (groove side), M8–M10; A-lines beyond the helmet plug |
| **DRIVE BOX** | Master synthesiser (stages, eccentric bushings, Oldham, 6-cylinder master plate), pneumatics (pumps, accumulators, reliefs R1a/b, R2/b, synchro reliefs, dumps, utility valves, manifolds, silencers), plug blocks (both ends), umbilical build, hanger, enclosure and mounts | §4.2–4.5, §5.2, §6 | box layout and drawings; pneumatic schematic (final); relief calibration procedure; umbilical build sheet; portability test | M11 (plug), M12–M14; A1–A14, S1–S6 to the helmet plug |
| **ELECTRONICS + FIRMWARE** | Safety loop, rail MOSFET and watchdog, PCB/perfboard (ESP32-S3, MCP3208 ×3, TPIC6B595 ×3, MOSFETs, bucks, bus buffer, TMC2209 ×2, SD), hand controller (lever + egg casting + PS1), e-stop puck; firmware per §8 | §5.3–5.4, §7.1, §8; electronics-firmware.md (port) | schematic + wiring table; firmware repo `firmware/sp1v2/` (compiles in Arduino-ESP32 3.x); bring-up procedure; limits table; serial reference | E1–E10, all control links, the score format |
| **TEST PROTOCOLS** | Stage A–D procedures and data sheets; safety checklist adapted to SP1 v2; hair bench (hair-interaction §7); feedback form; experiment matrix; blind-trial plans; pre-build cue-card evening (leap2-D §4) | §10, §7; 05-engineering/test-protocols.md (reuse) | test-protocols-v2.md; log templates; pass/fail sheets | gate definitions (§10) |
| **CAD** | OpenSCAD (or Fusion) models for every printed part; assembly model of halo + pad on the design head ellipsoid; interference check at all (α, β) incl. twin vertex; STL export with orientation notes | all WP drawings; this spec's datums | cad/sp1v2/*.scad, stl/, README, CONFLICTS.md | geometric consistency of M1–M15 |
| **BOM** | Live-vendor-verified BOM by WP and by stage; order list by vendor; substitutes; [VERIFY] closures for parts | all WP part lists; §13 | bom-sp1v2.md, Day-0 cart (Stage A parts first) | cost target §13 |

**Sequencing:**
- Day 0: BOM orders the Stage A parts (S070 ×12, pumps, sensors, steppers, ESP32-S3, silicone kit). ELECTRONICS and DRIVE BOX start at once.
- PAD starts with the pin cartridge and the moulds (needed in A4).
- HALO starts after Michael's tape fit.
- CAD runs alongside all of them.

---
## 12. Risks and open items

### 12.1 Top 12 risks, each with the bench test that retires it

| # | Risk | P [EST] | Consequence | Retiring test (stage) | Fallback |
|---|---|---|---|---|---|
| R1 | **Synchro copy fidelity**: stick-slip of cast rolling diaphragms, stiffness, drift, rosette quality | 0.30 | jerky or shrunken strokes; the puppet fails | A2 one-line slide and A3 ink rosettes (pass lines §10) | Ø 24 + p₀ 40 kPa; else pad-mounted twin direct-drive Tusi (leap3-B L2, ≈ 80 g, reopen mass) |
| R2 | **Cast diaphragm life** (synchro and pins): 10⁴ cycles per session | 0.30 | leaks and drift; rebuilds | drill-driven 10⁵-cycle rig per diaphragm type, leak logged every 10⁴ (A2, A4) | commercial rolling diaphragms (≈ $20–40 each, +$150) or nitrile cot bladders as consumables |
| R3 | **Hover collar window** (0.07–0.10 N) drifts with humidity and wear, so pins creep down or never hover | 0.25 | taps or loss of hover | 500-cycle hover test at 30 % and 70 % RH (A4) | vacuum-assisted hover: LIFT SELECT at −2 kPa instead of vent (firmware) |
| R4 | **Head-borne mass** over 400 g (ledgers run low) | 0.35 | neck fatigue; twin over 480 g | weigh at B1 and C2 | the mass ladder of §4.7 |
| R5 | **The hat is felt** leaning (0.24 N·m) or ticking with the scrub | 0.35 | "machine on my head" in the first minute | C3 coin lean test; D2 question "does the hat move?" | bring the twin forward; counter-mass on the β return run |
| R6 | **Hub servo noise by bone conduction** | 0.30 | audible machine at the ear | C5 earplug on/off test | gimbal + FOC cartridge (M3 adapter C) |
| R7 | **Hair stirred or wound** by the moving block underside or the shafts, especially in circle mode | 0.20 | tangles; matting | B5 wig suite (real hair 3–5 cm and long, Kanekalon) | still-dome tilting pins (leap2-F L2); circle mode deleted |
| R8 | **Landing timing**: descent too fast (a tap) or too slow (late); latency scatter > ±10 ms | 0.25 | dabbing, taps, or lost windows | A4 per-pin latency and ink-on-moving-paper streak test (B6) | restrictor resizing; alternating sets as the default |
| R9 | **Plug sealing** at 12 N (20 ports with a soft gasket) | 0.25 | synchro drift; air loss | A3 leak test through the plug; C6 pull tests | barbed hose-per-port on the helmet side with a 20-way strain-relief sleeve, and a separate 12 N magnetic anchor |
| R10 | **Sensation: omni-nail on hover-and-bite reads as "dabby" or "pad-like"** rather than nails | 0.30 | hypothesis fails | pre-build cue-card evening (leap2-D §4, $0); B7 forearm "nail or pad?"; D5 tip A/B | directional mini-nail sticks (D-6); park-per-stroke off; Ø 3 flat |
| R11 | **Palm patting / skid drag** as the constant-support gait fails in practice | 0.20 | rhythmic palm = a machine signature | B6 skid load trace through a phrase | lower the pin count per row; slower palm slew; firmware feed-forward tuning |
| R12 | **Cost and supply**: S070 lead times, STS3032 thin US stock, overrun past $1,200 | 0.30 | delay | BOM WP live check on Day 0; order S070 ×12 and STS3032 ×3 first | Parker X-Valve or Festo MHA1 class; XL330 / XC330 via adapter B |

Also watched: the halo reading as "apparatus" at ≈ 420 mm across (D-stage rating); twin lockstep reading as a machine (twin stage); the cradle pressing on the suboccipital nerves (C1 20-min test).

### 12.2 Every remaining [VERIFY]

| # | Item | Closed by |
|---|---|---|
| V1 | Design-head dimensions (ANSUR-class means) and Michael's tape fit | HALO WP before cradle CAD |
| V2 | S070 order code: 12 V coil, port type (barb Ø for PU 3 × 2), coil power, rated life | BOM WP, SMC catalog |
| V3 | STS3032 mounting pattern, spline, connector, protocol variant, torque-off back-drive, temperature at 0.05 N·m continuous | HALO + ELECTRONICS, bench |
| V4 | Rolling-diaphragm casting (0.4 mm Dragon Skin) holds 34 mm stroke without wrinkling; life ≥ 10⁵ | R2 rig (A2) |
| V5 | Synchro stiffness ≥ 0.6 N/mm per line; leak ≤ 0.5 kPa/min; common lag 4–6 ms | A2/A3 |
| V6 | Descent 50 ± 10 mm/s with a Ø 0.20–0.25 restrictor; force rise ≤ 20 ms; latency scatter ±5 ms | A4 |
| V7 | Hover collar friction 0.07–0.10 N over RH 30–70 % | A4 / R3 |
| V8 | Per-pin bleed Ø 0.15 mm decays 10 kPa → 2 kPa in < 1 s through the restrictor / duckbill topology | A4 |
| V9 | Relief poppets calibrate and repeat ±1 kPa (R1a/b, R2/b, synchro) | A1 |
| V10 | R2b added (§7.2) and the double-fault total ≤ 12 N | B2 |
| V11 | XGZP6847A ranges (0–40, −40–0, 0–100 kPa) and settling at 1 kHz via MCP3208 | A1 |
| V12 | Pump stall pressure (53 kPa class) for the 12 V parts actually bought | A1 |
| V13 | Head scan height accuracy ±0.2 mm from flow time-of-flight; grain ±15° from the synchro drag rose | B (wig), D3 (Michael) |
| V14 | Plug face seal at 12 N with a 30A gasket: ≤ 0.2 kPa/min per synchro port | A3 / C6 |
| V15 | Cradle form-lock override ≈ 10 N and pitch hold ≥ 1 N·m on the chosen bike retention | C1 |
| V16 | Hub servo noise: air ≤ 30 dBA; bone path inaudible | C5 |
| V17 | Mass ledger (pad ≤ 90 g; helmet ≤ 400 g; twin ≤ 480 g) | B1, C2, twin step 8 |
| V18 | Coverage and fence numbers on Michael's head (ellipsoid model is approximate) | C4 + scan |
| V19 | POM nail ESD behaviour; steel shaft grounding path | B5 (dry-air static test) |
| V20 | PS1 hard-squeeze switch: buy (adjustable 0.1–0.8 bar NC) or DIY printed membrane switch, ≥ 5 A contacts | ELECTRONICS, A0 |
| V21 | Box ≤ 32 dBA at 1 m and ≤ 2.5 kg | A5 |
| V22 | Neck stability margin at the 0.96 N cap with the bonded sleeve (k may be 1.5–2.8× higher) | B3 / B6 |
| V23 | Hair-bearing coverage ≈ 90 % (model not area-weighted) | C4 |
| V24 | All prices in §13 | BOM WP |

---

## 13. Cost target and roll-up

**Target: ≤ $1,200** for one-pad SP1 plus the second-pad parts. Excluded: tools, the 3D printer, and the bench test kit (wig heads, load cell, scales, which are listed in the TEST WP). Prices are 2026 US hobby retail at mid-range [EST ±15 %]. The BOM WP verifies them live.

| Group | Main lines | $ |
|---|---|---|
| **Drive box** | 12 × SMC S070 @ $32 (384); 3 utility + 5 NO mini valves (24); pumps 2 × KPM27C + 1 small (18); 22 × XGZP6847A @ $3 (66); relief poppets, restrictors, duckbills, accumulators (26); fittings and manifolds (25); master (2 NEMA 17 pancake 22, 2 × TMC2209 10, eccentric bushings 10, bearings 10, GT2 belt and pulleys 8, Halls 3 = 63); enclosure, foam, sorbothane, hook plate, strap, latches (25) | **631** |
| **Electronics** | ESP32-S3 (15); 3 × MCP3208 + 3 × TPIC6B595 (15); MOSFETs, diodes, TVS, caps, bus buffer (8); 12 V 5 A certified adapter (22); 6 V + 5 V bucks (10); e-stop + puck + GX12 connectors (20); hand controller (lever, DIY PS1, lead) (10); watchdog and rail-MOSFET parts (3); fuses (5); perfboard, headers, JST, 2 × 6-pin magnetic pogo (15); microSD (3); wire and sleeving (10) | **136** |
| **Helmet** | bike helmet for the dial cradle (20); carbon 10 × 8, 2 × 1 m (22); 6800-2RS × 4 + MR63 × 10 + Ø 10 shaft (14); **2 × STS3032 (66)**; Dyneema 1 mm (14); springs (8); foam, sleeve, Al strip (12); magnets (6); POM rod (8) | **170** |
| **Pad** | music wire 1.0 / 0.38, brass tube, PTFE tubes (20); silicone casting kit, shared with the egg and all diaphragms (30); PP sheet, balls, carbon rod, ball links (12); springs (6); 0.5 mm 40A silicone sheet (6) | **74** |
| **Umbilical + hanger** | PU 3 × 2 25 m (16); PU 4 × 2.5 10 m (7); 6-core cable (5); knit sleeve (5); plug gaskets, magnets, latches (10); hanger rod, clamp, magnetic clip (12) | **55** |
| **Printing + consumables** | PETG 2 kg (32); TPU 0.5 kg (14); inserts and fasteners (12); CA, epoxy, UV resin (12) | **70** |
| **Second-pad parts (bought now)** | STS3032 (33); pad B kit (18); carriage B + float B (6); triad-B master cylinder hardware (4); 12 tees + 24 restrictors (10); PALM B + 4 NO dumps (12); 4 sensors (12); MCP3208 + TPIC6B595 (6); sleeve (3) | **104** |
| **Total** | | **≈ $1,240** |

**Closing the 3 % gap, in order:**
1. S070 at a ≤ $30 distributor price (−$24).
2. Reuse parts already bought for the Float-Arm Day-0 cart, if any arrived: e-stop, PETG, Dyneema, magnets, fasteners (−$40 to −$60).
3. Buy pad B's consumables (nail sticks, diaphragms) at twin conversion rather than now (−$15).

Lever 2 alone, or levers 1 + 3 together, brings the total under $1,200.

**If the order exceeds $1,300,** drop to 10 pins (the 4 × 4 minus corners with 2 opposite edge-centre pins removed; −2 valves, −2 sensors, ≈ −$70) and record the loss of 4-nail rows in the experiment matrix.

---

## 14. Change control and next actions

- This file is the **design freeze v2**. Work packages build to it. A deviation goes to a numbered ADDENDUM in 12-sp1v2/, never into this file silently.
- **Immediate next actions (Director):**
  1. Launch the seven WPs of §11, with HALO waiting on Michael's tape fit.
  2. Run the BOM WP's Day-0 order for Stage A parts.
  3. Run the $0 cue-card evening (leap2-D §4) and the $20 coin and bike-helmet evening (leap3-A/D/E) before Stage C hardware is cut.
- **Gates after the WPs land:** BUILD REVIEW, SENSATION GATE and SAFETY GATE (BRIEF §20–22) read the WP package cold, against this file.
