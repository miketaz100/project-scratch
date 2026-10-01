# SP1 ELECTRONICS & FIRMWARE — wiring, safety loop, control spec, pattern engine, bring-up

**Owner:** Electronics & Firmware Lead · **Builds to:** `05-engineering/DESIGN-FREEZE.md` §1 items 9–10, §2, §3 · **Governed by:** `01-foundations/safety-requirements.md` §3–4, red lines 4, 7, 8, 13 · **Source:** `05-engineering/firmware/sp1_scratch/sp1_scratch.ino` (+ `firmware/README.md`) · **Date:** 2026-10-01

Legend: **[SRC]** verified against a cited page · **[EST]** engineering estimate · **[VERIFY]** could not be verified from documentation; a bench test in §6 decides it.

**Deviations from the freeze (flagged, not silently made):**
1. A **rail-sense input** (10 k/10 k divider from the actuator rail to A2) is added so the firmware *knows* the rail state. It is read-only: the hold-to-run and e-stop remain hardware (safety §3.10 "the MCU may read it but must not be what implements it").
2. **Status Return Level stays 2** (every write acknowledged) rather than 1, because Dynamixel2Arduino waits for a status packet on writes; level 1 would make every write look like a timeout and defeat error detection.
3. **Current Limit (EEPROM 38) = 450 mA** is set as a second, firmware-independent ceiling above the 300 mA Goal Current; freeze §1.10 only names the goal-current cap.
4. The sketch is 533 lines against the "~500" target, because the Test Lead's §Q.3 hooks (1 Hz telemetry, `goto`/`gotoraw`/`hang`, BLIND presets, settings code) were added.

---

## 1. Wiring architecture

### 1.1 Rail topology (one sentence)
One certified 5 V brick feeds **one series safety loop** — fuse → NC e-stop → NO hold-to-run — and only after that loop does the 5 V split into (a) the OpenRB-150 **Terminal VIN** (which is the DYNAMIXEL bus supply when the jumper is on `VIN(DXL)`) and (b) the **holding electromagnet**. The OpenRB-150 **logic runs from USB-C**, on the laptop side of the loop, so opening the loop kills the servo and drops the magnet while the MCU keeps logging. Nothing on the laptop side can energise anything on the rail side (see §1.5).

### 1.2 Schematic

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 560" width="960" height="560" font-family="Helvetica, Arial, sans-serif" font-size="12">
  <defs><marker id="ar" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#333"/></marker></defs>
  <rect x="0" y="0" width="960" height="560" fill="#fff"/>
  <text x="12" y="20" font-size="14" font-weight="bold">SP1 actuator rail (hardware safety loop) and control wiring</text>
  <!-- rail band -->
  <rect x="12" y="40" width="936" height="190" fill="#fff4f4" stroke="#c33" stroke-dasharray="4 3"/>
  <text x="20" y="56" fill="#c33" font-weight="bold">ACTUATOR RAIL — everything inside this box is dead when the loop is open</text>
  <!-- adapter -->
  <rect x="24" y="90" width="110" height="60" fill="#fff" stroke="#333"/>
  <text x="79" y="112" text-anchor="middle">5 V 4 A brick</text><text x="79" y="128" text-anchor="middle" font-size="10">Adafruit 1466, UL</text><text x="79" y="142" text-anchor="middle" font-size="10">5.5×2.1 centre +</text>
  <!-- jack adapter + fuse -->
  <rect x="160" y="100" width="70" height="40" fill="#fff" stroke="#333"/><text x="195" y="117" text-anchor="middle" font-size="10">jack→screw</text><text x="195" y="131" text-anchor="middle" font-size="10">adapter</text>
  <rect x="255" y="100" width="70" height="40" fill="#fff" stroke="#333"/><text x="290" y="117" text-anchor="middle">FUSE</text><text x="290" y="131" text-anchor="middle" font-size="10">1 A fast 5×20</text>
  <!-- e-stop -->
  <rect x="350" y="90" width="90" height="60" fill="#fff" stroke="#c33" stroke-width="2"/><text x="395" y="112" text-anchor="middle" font-weight="bold">E-STOP</text><text x="395" y="127" text-anchor="middle" font-size="10">22 mm mushroom</text><text x="395" y="141" text-anchor="middle" font-size="10">NC, latching, boxed</text>
  <!-- hold to run -->
  <rect x="465" y="90" width="100" height="60" fill="#fff" stroke="#c33" stroke-width="2"/><text x="515" y="112" text-anchor="middle" font-weight="bold">HOLD-TO-RUN</text><text x="515" y="127" text-anchor="middle" font-size="10">NO momentary, handheld</text><text x="515" y="141" text-anchor="middle" font-size="10">1.5 m lead</text>
  <!-- split node -->
  <circle cx="600" cy="120" r="4" fill="#333"/>
  <!-- OpenRB VIN -->
  <rect x="650" y="70" width="130" height="50" fill="#fff" stroke="#333"/><text x="715" y="90" text-anchor="middle">OpenRB-150</text><text x="715" y="105" text-anchor="middle" font-size="10">Terminal VIN (+ / −)</text>
  <text x="790" y="78" font-size="9">470 µF + SMAJ5.0A</text><text x="790" y="90" font-size="9">at the terminal</text>
  <!-- magnet -->
  <rect x="650" y="150" width="130" height="60" fill="#fff" stroke="#333"/><text x="715" y="170" text-anchor="middle">ELECTROMAGNET</text><text x="715" y="185" text-anchor="middle" font-size="10">P20/15 5 V 0.22 A 25 N</text><text x="715" y="199" text-anchor="middle" font-size="10">1N5819 flyback ↑ across coil</text>
  <!-- servo -->
  <rect x="820" y="100" width="118" height="60" fill="#fff" stroke="#333"/><text x="879" y="120" text-anchor="middle">XL330-M288-T</text><text x="879" y="135" text-anchor="middle" font-size="10">ID 1 elbow (ID 2 yaw, St.3)</text><text x="879" y="149" text-anchor="middle" font-size="10">DXL port, FET-switched</text>
  <!-- wires rail -->
  <line x1="134" y1="120" x2="160" y2="120" stroke="#c33" stroke-width="2"/>
  <line x1="230" y1="120" x2="255" y2="120" stroke="#c33" stroke-width="2"/>
  <line x1="325" y1="120" x2="350" y2="120" stroke="#c33" stroke-width="2"/>
  <line x1="440" y1="120" x2="465" y2="120" stroke="#c33" stroke-width="2"/>
  <line x1="565" y1="120" x2="600" y2="120" stroke="#c33" stroke-width="2"/>
  <line x1="600" y1="120" x2="600" y2="95" stroke="#c33" stroke-width="2"/><line x1="600" y1="95" x2="650" y2="95" stroke="#c33" stroke-width="2" marker-end="url(#ar)"/>
  <line x1="600" y1="120" x2="600" y2="180" stroke="#c33" stroke-width="2"/><line x1="600" y1="180" x2="650" y2="180" stroke="#c33" stroke-width="2" marker-end="url(#ar)"/>
  <line x1="780" y1="95" x2="800" y2="95" stroke="#333" stroke-width="2"/><line x1="800" y1="95" x2="800" y2="130" stroke="#333" stroke-width="2"/><line x1="800" y1="130" x2="820" y2="130" stroke="#333" stroke-width="2" marker-end="url(#ar)"/>
  <text x="790" y="170" font-size="9">3-pin TTL cable</text><text x="790" y="181" font-size="9">(GND, VDD, DATA)</text>
  <text x="90" y="170" font-size="10">22 AWG silicone, red/black, the whole rail; return (−) runs straight from the brick to the OpenRB terminal − and the magnet −</text>
  <text x="90" y="186" font-size="10">Rail-sense tap: 10 k from the split node to A2, 10 k from A2 to GND, 100 nF to GND (read-only, 2.5 V when live)</text>
  <line x1="600" y1="120" x2="600" y2="222" stroke="#888" stroke-width="1" stroke-dasharray="3 2"/><text x="606" y="225" font-size="9" fill="#555">→ A2 via divider</text>
  <!-- logic side -->
  <rect x="12" y="250" width="936" height="296" fill="#f3f7ff" stroke="#36c" stroke-dasharray="4 3"/>
  <text x="20" y="266" fill="#36c" font-weight="bold">LOGIC — powered from USB-C; stays alive when the rail is open; cannot energise the rail</text>
  <rect x="24" y="290" width="120" height="50" fill="#fff" stroke="#333"/><text x="84" y="310" text-anchor="middle">Laptop / USB</text><text x="84" y="325" text-anchor="middle" font-size="10">charger 5 V (500 mA fuse on board)</text>
  <rect x="250" y="280" width="300" height="250" fill="#fff" stroke="#333" stroke-width="1.5"/>
  <text x="400" y="300" text-anchor="middle" font-weight="bold">OpenRB-150 (SAMD21G18A)</text>
  <text x="400" y="315" text-anchor="middle" font-size="10">jumper = VIN(DXL) · DXL power FET on pin 31 (off at boot)</text>
  <text x="262" y="340" font-size="11">A0  ← SPEED pot wiper</text>
  <text x="262" y="358" font-size="11">A1  ← VARIATION pot wiper</text>
  <text x="262" y="376" font-size="11">A2  ← rail sense (divider)</text>
  <text x="262" y="394" font-size="11">D4  ← PERIODIC/HUMAN toggle (INPUT_PULLUP, closed = PERIODIC)</text>
  <text x="262" y="412" font-size="11">D5  → status LED (330 Ω) ; LED_BUILTIN (pin 32) mirrors</text>
  <text x="262" y="430" font-size="11">D2, D3, 3V3, GND → HX711 header (reserved, Stage 3)</text>
  <text x="262" y="448" font-size="11">3V3 → pot ends (+) ; GND → pot ends (−), toggle, LED, divider</text>
  <text x="262" y="466" font-size="11">Serial1 (DXL port 1) → XL330 TTL bus, 1 Mbps</text>
  <text x="262" y="484" font-size="11">USB-C → Serial (115200): commands, 1 Hz telemetry, stroke log</text>
  <text x="262" y="508" font-size="10" fill="#555">GND: logic GND and rail − are the same net at the OpenRB terminal (star point); no second return path.</text>
  <line x1="144" y1="315" x2="250" y2="315" stroke="#36c" stroke-width="2" marker-end="url(#ar)"/><text x="160" y="308" font-size="10">USB-C</text>
  <!-- pots -->
  <rect x="600" y="290" width="150" height="70" fill="#fff" stroke="#333"/><text x="675" y="310" text-anchor="middle">SPEED pot 10 kΩ</text><text x="675" y="325" text-anchor="middle" font-size="10">3V3 — wiper A0 — GND</text><text x="675" y="340" text-anchor="middle" font-size="10">tape marks 0 / 50 / 100 %</text>
  <rect x="600" y="370" width="150" height="70" fill="#fff" stroke="#333"/><text x="675" y="390" text-anchor="middle">VARIATION pot 10 kΩ</text><text x="675" y="405" text-anchor="middle" font-size="10">3V3 — wiper A1 — GND</text><text x="675" y="420" text-anchor="middle" font-size="10">tape marks 0 / 50 / 100 %</text>
  <rect x="600" y="450" width="150" height="40" fill="#fff" stroke="#333"/><text x="675" y="467" text-anchor="middle">PERIODIC/HUMAN toggle</text><text x="675" y="481" text-anchor="middle" font-size="10">SPST: D4 — GND</text>
  <rect x="780" y="290" width="150" height="40" fill="#fff" stroke="#333"/><text x="855" y="307" text-anchor="middle">Status LED</text><text x="855" y="321" text-anchor="middle" font-size="10">D5 — 330 Ω — LED — GND</text>
  <rect x="780" y="350" width="150" height="50" fill="#fff" stroke="#333" stroke-dasharray="3 2"/><text x="855" y="370" text-anchor="middle">HX711 + bar cell</text><text x="855" y="385" text-anchor="middle" font-size="10">reserved: D2 DT, D3 SCK</text>
  <line x1="550" y1="325" x2="600" y2="325" stroke="#36c" stroke-width="1.5"/><line x1="550" y1="405" x2="600" y2="405" stroke="#36c" stroke-width="1.5"/><line x1="550" y1="470" x2="600" y2="470" stroke="#36c" stroke-width="1.5"/>
  <line x1="550" y1="310" x2="780" y2="310" stroke="#36c" stroke-width="1.5" stroke-dasharray="6 3"/>
  <text x="20" y="540" font-size="10" fill="#555">Red = rail (switched 5 V). Blue = logic. The only link between the two domains is the DXL cable's GND/DATA and the rail-sense divider; the DXL VDD pin is fed from Terminal VIN through the on-board FET, never from USB (jumper VIN(DXL), bench test B3).</text>
</svg>

### 1.3 Connection table (every wire)

| # | From | To | Wire / gauge | Connector / termination | Notes |
|---|---|---|---|---|---|
| 1 | Adapter 5.5×2.1 plug (+ centre) | Jack-to-screw adapter | adapter cord | barrel 5.5/2.1 → screw terminals | Polarity: centre positive [SRC Adafruit 1466]. Meter before first power-up (§6 B1). |
| 2 | Jack adapter **+** | Fuse holder in | 22 AWG red silicone | screw / inline holder | 1 A fast-blow 5×20 (F1AL250V); spare in the kit (§Q.4). |
| 3 | Fuse holder out | E-stop NC terminal 1 | 22 AWG red | ring/fork crimp on the e-stop block | Boxed e-stop on the desk, weighted base. |
| 4 | E-stop NC terminal 2 | Hold-to-run cable **+** | 22 AWG red | crimp at e-stop; 1.5 m 2-core 22 AWG cable to the handle | Second NC contact of the e-stop left unused (spare). |
| 5 | Hold-to-run microswitch COM | — | inside handle | 4.8 mm spade on the arcade microswitch | Strain relief: cable through a printed gland + internal zip-tie anchor. |
| 6 | Hold-to-run microswitch **NO** | Rail split node (3-way Wago / screw block at the module) | 22 AWG red (return leg of the 1.5 m cable) | 221-413 lever block or screw terminal | This node is the **ACTUATOR RAIL +**. |
| 7 | Rail node + | OpenRB-150 Terminal VIN **+** | 22 AWG red | removable terminal block (supplied) | 470 µF 10 V electrolytic + SMAJ5.0A TVS across + / − at the terminal. Jumper on **VIN(DXL)**. |
| 8 | Rail node + | Electromagnet lead 1 (+) | 22 AWG red (magnet's own 270 mm leads spliced, heat-shrink) | solder + heat-shrink | 1N5819 Schottky across the coil: **cathode (band) to +**, anode to −. |
| 9 | Rail node + | 10 kΩ → A2 | 26 AWG | pot/divider on a small perfboard | 10 kΩ A2 → GND, 100 nF A2 → GND. Read-only sense. |
| 10 | Jack adapter **−** | OpenRB-150 Terminal VIN **−** | 22 AWG black | terminal block | Star ground point. |
| 11 | OpenRB-150 Terminal **−** | Electromagnet lead 2 (−) | 22 AWG black | solder + heat-shrink | |
| 12 | OpenRB-150 DXL port 1 | XL330 ID 1 (either X3P socket) | Robotis 3-pin TTL cable (X3P/JST-EH, supplied with the servo) | JST-EH 3-pin | Service loop at the elbow bracket; sleeved. Daisy-chain port on the servo → ID 2 in Stage 3. |
| 13 | SPEED pot ends | 3V3 / GND | 26 AWG | Dupont to the OpenRB headers | Wiper → **A0**. |
| 14 | VARIATION pot ends | 3V3 / GND | 26 AWG | Dupont | Wiper → **A1**. |
| 15 | Toggle PERIODIC/HUMAN | **D4** / GND | 26 AWG | Dupont | INPUT_PULLUP; closed (to GND) = PERIODIC. |
| 16 | Status LED anode | **D5** via 330 Ω; cathode → GND | 26 AWG | Dupont | LED_BUILTIN (pin 32) mirrors it. |
| 17 | HX711 header | **D2** (DT), **D3** (SCK), 3V3, GND | 26 AWG | 4-pin header, unpopulated | Stage 3 load cell (40×12 mm bar cell slot in the wrist). |
| 18 | Laptop / USB charger | OpenRB-150 USB-C | USB-C cable | USB-C | Logic power + serial. Board USB input fused 500 mA [SRC]. |

Every wire that crosses a moving joint (12 only: the DXL cable from the module frame to the elbow servo; the servo moves with the frame on the fail-safe hinge) gets a 60 mm service loop, braided sleeving, and a zip-tie anchor at both ends. No bare terminals anywhere on the rail; the Wago block sits inside a printed cover on the module frame.

### 1.4 Parts (electrical) with sources

| Part | Spec | Source |
|---|---|---|
| 5 V 4 A adapter | Adafruit 1466, 5 V 4 A, UL-listed, 100–240 V in, 5.5×2.1 mm centre-positive, 20 W | [SRC] <https://www.adafruit.com/product/1466> (also [Jameco](https://www.jameco.com/z/1466-Adafruit-Industries-5V-4A-4000Ma-Switching-Power-Supply-UL-Listed_2505471.html)) |
| Jack → screw adapter | 5.5×2.1 mm female DC jack to 2-pin screw terminal | generic (Amazon/Adafruit 368) |
| Fuse | 5×20 mm glass, **1 A fast** (F1AL250V) + inline screw-type holder 18 AWG | [uxcell inline holder](https://www.amazon.com/uxcell-Inline-Screw-Holder-Gauge/dp/B07SM5KYZ7) |
| E-stop | 22 mm NC mushroom, latching (push-lock, twist-release), 10 A/600 V, **boxed** for desk use | [TWTADE YW1B-V4E02R boxed](https://www.amazon.com/TWTADE-Mushroom-Emergency-Warranty-YW1B-V4E02R-BOX/dp/B07NNZB41H) (component-landscape §6.3); panel-mount alternative [APIELE 1NC LA139A-ES542](https://www.amazon.com/APIELE-Emergency-Stop-Button-Switch/dp/B0F2F8TYMY) |
| Hold-to-run button | **uxcell 30 mm momentary arcade push button**, N.O. microswitch, 3 A/250 V, snap-in | [SRC] <https://www.amazon.com/uxcell-Mounting-Momentary-Button-Switch/dp/B08HH78XMH> |
| Hold-to-run housing | printed PETG handle Ø 36 × 110 mm, two halves, M3 screws; the button face sits **3 mm below a 36 mm rim** (thumb well); cable gland boss + internal zip-tie anchor; 1.5 m 2-core 22 AWG cable | CAD agent: `cad/handheld_button.scad` (spec here) |
| Hold-to-run, bought alternative | Philmore 30-825 hand-held momentary N.O. SPST push-to-talk switch, 3 A/125 V, die-cast body; extend its cord to 1.5 m | [Amazon B00T6RCGNC](https://www.amazon.com/Hand-Held-Button-Switch-30-825/dp/B00T6RCGNC), [Vetco](https://vetco.net/products/philmore-30-825-spst-push-button-switch-momentary-n-o-3a-125vac-handheld-with-red-actuator) |
| Holding electromagnet | **Adafruit 3872, P20/15**: 5 V DC, 0.22 A, 2.5 kg (25 N) holding, Ø 20 × 15 mm, M3 rear thread, 270 mm leads | [SRC] <https://www.adafruit.com/product/3872> (freeze §1.3 asks ≥ 25 N, 20–25 mm: exact match; P25/20 5 kg [3873](https://www.adafruit.com/product/3873) is the fallback if the spring is uprated) |
| Flyback diode | 1N5819 Schottky, 40 V 1 A | any distributor |
| Bulk / TVS at the terminal | 470 µF 10 V electrolytic; SMAJ5.0A TVS | any distributor (safety §4.2) |
| Controller | OpenRB-150, SAMD21G18A, 4 DXL TTL ports, FET-switched DXL power, USB-C | [SRC] <https://emanual.robotis.com/docs/en/parts/controller/openrb-150/> |
| Servo | XL330-M288-T, 5 V, 0.52 N·m stall at 1.47 A, 18 g, 4096 ticks/rev, protocol 2.0 | [SRC] <https://emanual.robotis.com/docs/en/dxl/x/xl330-m288/> |
| Pots, toggle, LED, divider | 2 × 10 kΩ linear pots with knobs; SPST toggle; 5 mm LED + 330 Ω; 2 × 10 kΩ + 100 nF | kit |
| Wire | 22 AWG silicone (rail), 26 AWG (signals), heat-shrink, braided sleeve, Wago 221-413, Dupont kit | kit |

### 1.5 Power facts verified from the ROBOTIS e-manual, and the one thing it does not say

Verified [SRC: [OpenRB-150 e-manual](https://emanual.robotis.com/docs/en/parts/controller/openrb-150/), [docs.robotis.com mirror](https://docs.robotis.com/docs/parts/controller/openrb-150/), [emanual source](https://raw.githubusercontent.com/ROBOTIS-GIT/emanual/master/docs/en/parts/controller/openrb-150.md)]:
- Three power inputs: **USB-C 5 V**, **VIN pin 3.7–12.6 V**, **Terminal block / XT60 3.7–12.6 V**. A jumper selects the DYNAMIXEL supply: *"To supply power to the OpenRB-150 controller via the Terminal VIN, set the jumper to `VIN(DXL)` side"*; the other position is `USB(5V)`.
- *"Power to the DYNAMIXEL ports is controlled by the FET on the bottom of the microcontroller … by default the FET is turned off whenever the OpenRB-150 is powered on."* Pin `BDPIN_DXL_PWR_EN` (31). The DXL RED LED lights when the FET is on. **Dynamixel2Arduino raises this pin in `begin()` on the OpenRB-150** [SRC: [port_handler.cpp](https://raw.githubusercontent.com/ROBOTIS-GIT/Dynamixel2Arduino/master/src/utility/port_handler.cpp), `#elif defined(ARDUINO_OpenRB)`], so the bus is only powered once firmware is running — a reset (including a watchdog reset) drops it.
- *"The current from the USB port is limited to 500mA with the built-in fuse"*; *"DC CURRENT FOR DYNAMIXEL PORTs: 3,000 mA"*; *"USB port is not a suitable power source for dynamic motor operation."* The Korean page adds that Dynamixels *can* be driven from USB with a limited count — i.e. in the `USB(5V)` jumper position the bus is fed from USB. **That position is forbidden for SP1** (it would put the servo on the laptop side of the safety loop: Red Team 2 §6 "USB back-feed").
- *"Resetting the microcontroller will also reset the power of any connected DYNAMIXELs."*

**[VERIFY] — not stated in the manual:** whether, with the jumper on `VIN(DXL)` and Terminal VIN at 0 V, the MCU keeps running from USB-C. The MKR-style design (ORed USB/VIN into the 3.3 V regulator) makes this likely, the schematic is only available as a download (<https://www.robotis.com/service/download.php?no=2117>, check it at build), and the ROBOTIS forum threads on exactly this question ([4971](https://forum.robotis.com/t/about-powering-dynamixel-through-openrb150/4971), [8233](https://forum.robotis.com/t/openrb-150-power-supply-issue-inquiry/8233)) were unreachable from here. Bench test **B2** settles it. Both outcomes are safe:
- *Outcome A (expected):* MCU alive on USB, DXL port 0 V with the rail open → full logging of the event; firmware sees `rail=0`, goes PAUSED, re-initialises when the rail returns.
- *Outcome B:* MCU resets with the rail → bus FET off at boot, servo limp, firmware restarts in INIT and waits for the rail; the host terminal keeps the log printed up to the event (1 Hz `H,` lines and per-stroke `S,` lines). Nothing is lost that safety depends on; only the post-event fault line.
- Either way, **B3 is a hard gate:** rail open + USB connected → DXL port VDD pin meters 0 V and the servo LED stays dark. If it reads 5 V the jumper is wrong; the rig is not used until it reads 0 V.

### 1.6 Fusing, polarity, strain relief, back-feed
- **Fuse 1 A fast** on the rail. Normal rail current: servo ≤ 0.30 A (goal current) + magnet 0.22 A + board ≈ 0.05 A ≈ **0.6 A** → 1 A ≈ 1.5–1.7× running (safety §2.8). A servo that has lost its current limits stalls at 1.47 A [SRC] → fuse opens; the brick's own OCP (≈ 4 A) is the absolute ceiling. If the fuse nuisance-trips during bring-up at 450 mA goal current, 1.25 A fast is the only permitted step up; note it on the diagram.
- **Polarity:** 5.5×2.1 centre-positive brick → keyed barrel adapter → red/black convention → terminal block marked + / −. No series diode (it would drop the 5.0 V bus toward the XL330's 3.7 V floor under load); the SMAJ5.0A TVS clamps reversed or spiked input and a metered polarity check is bench test B1. XL330 operating range 3.7–6.0 V [SRC].
- **Strain relief:** brick cord zip-tied to the desk edge; e-stop box screwed to a steel plate; the 1.5 m hold-to-run cable has a gland at the handle and a zip-tie anchor at the module; the DXL cable has a service loop at the hinge; nothing hangs from a solder joint.
- **Why the magnet must not back-feed, and must not be fed from anywhere else:** the fail-safe lift (freeze §1.3) is credited only because the magnet dies *with* the servo. (i) It therefore hangs on the rail after the hold-to-run contact — never on a GPIO, a MOSFET from USB 5 V, or its own supply; a magnet with any other path would hold the frame down with the nails in the hair while the servo is dead (red line 8). (ii) The coil stores ½·L·I² ≈ a few mJ [EST]; when the loop opens that energy would otherwise spike the open contact to tens of volts (contact arcing, and a transient on the OpenRB VIN and the DXL bus — H16). The 1N5819 across the coil recirculates it; drop-out takes a few ms longer, which is irrelevant against the spring's lift time. (iii) The 470 µF at the terminal holds up the rail for ≈ 2.35 mC / 0.6 A ≈ 4 ms — negligible, and the magnet releases below ~50 % of rated voltage anyway.

---

## 2. Controller / driver requirements, and the budget stack

**Requirements the controller–driver pair must meet (from safety §4 and the freeze):** (1) a serial servo with current-based position control and a *servo-side* current limit, readable present current, software-settable position limits, and a bus watchdog; (2) a controller whose servo-bus supply is physically separate from its logic supply and is switchable from firmware (default off); (3) a hardware watchdog on the MCU; (4) ≥ 2 analog inputs, ≥ 2 digital I/O, USB serial; (5) ≥ 50 Hz read/write loop on the bus (1 Mbps); (6) no lithium, ≤ 24 V, certified brick. Stack A (OpenRB-150 + XL330-M288-T) meets all six: XL330 registers Current Limit (38), Goal Current (102), Present Current (126, 1 mA/LSB), Min/Max Position Limit (52/48), Bus Watchdog (98, 20 ms/LSB) [SRC]; OpenRB-150 FET-switched DXL power, SAMD21 WDT, 7 ADC pins, USB-C CDC [SRC].

**Stack B — ESP32 + Waveshare "Servo Driver with ESP32" + Feetech STS3215 (component-landscape §9):** same rail topology, with these changes:
- Rail voltage **7.4 V** (STS3215-7.4 V variant) or 12 V: Mean Well GST60A12 brick + a 7.4 V UBEC *after* the hold-to-run, or the 7.4 V STS3215 on a 7.5 V brick. The magnet becomes a 12 V P20/15 (Adafruit lists 12 V variants) on the same rail; fuse 2 A; 20 AWG rail wire.
- The Waveshare board's barrel jack is the servo rail input; its ESP32 logic is fed from the same jack through an on-board regulator, so **logic dies with the rail** (Outcome B above) unless the ESP32 is powered from USB — check the board's power path; if logic cannot be kept alive separately, accept Outcome-B behaviour and log on the host.
- STS3215 has no Bus Watchdog register: comm loss leaves the servo holding its last goal under its torque limit; the firmware watchdog → ESP32 reset → the Waveshare board's servo-power path is *not* FET-gated by default, so the servo stays powered through a reset. The hardware loop therefore carries more of the burden; add an INA219 rail watchdog (trip 1.2 A / 200 ms) or a logic-driven MOSFET on the servo rail.
- Torque limit register (Feetech "Torque Limit" / "Protection current", 6.5 mA/LSB present-current scale) replaces Goal Current; stall torque 2.7 A at 12 V means the current limit must be set *much* lower in proportion (~0.1 N·m → ~300 mA at 7.4 V [EST]); re-derive on the bench.
- Position units 4096/rev are the same; profile velocity/acceleration registers exist but with Feetech units (steps/s); the pattern engine's `tipSpeedToVelLsb()` is the only function to re-scale.
- ESP32's hardware WDT and ADC (12-bit, 3.3 V) map directly; the ESP32 ADC is non-linear near the rails, so pot end-points are tape marks at 5 %/95 %.

---

## 3. Safety architecture — what electronics/firmware mitigates, and how

The hardware loop (§1) is **primary**; the servo's own registers are the **electrical second layer**; the sketch is **third**, never credited alone (red line 13). Hazard numbers are from safety-requirements §1.

| Hazard | Primary (hardware) | Electrical second layer (servo registers, set by firmware at INIT, EEPROM items persist) | Firmware third layer (sp1_scratch.ino) |
|---|---|---|---|
| H3 excessive normal force | mechanical: dead weight + leaf stops (MECH) | — (normal force is not a servo quantity) | — |
| H4 excessive tangential force; red line 3 | 2.0 N magnetic wrist breakaway (MECH) | **Goal Current 300 mA ≈ 1.26 N at 84 mm; Current Limit 450 mA ≈ 1.9 N** (§4.3) | stall trip 270 mA / 250 ms → FAULT; `cur` command clamped ≤ 450 |
| H7 motor stall / overheating | 1 A fuse; XL330 Shutdown on overload/overheat (bits 5, 2) [SRC] | Current Limit 450 mA bounds dissipation to ≈ 0.7 W [EST]; Shutdown 0x34 default | stall trip < 300 ms (safety §4.6); Hardware Error Status polled 5 Hz → FAULT; re-arm by `reset` |
| H8 runaway actuation | e-stop / hold-to-run cut the rail; mechanical stops at the hinge and rail | **Min/Max Position Limit ±28° in EEPROM** — the servo refuses goals outside (bench test B6 `gotoraw`); Profile Velocity written per stroke, never above 180 LSB | all goals clamped to ±25° in one function (`setGoal`), bounded speeds, 3 ramp strokes, MCU WDT 1 s → reset → DXL FET off |
| H12 abrasion / dwell | — | — | no dwell on skin: pauses go to +25° (lifted by geometry); end-dwell ≤ 300 ms; 20-min session limit |
| H14 mains | certified external brick, nothing above 5 V on the rig | — | — |
| H15 low-voltage shorts | 1 A fuse, 22 AWG, sleeving, no bare terminals | servo OCP/OTP | — |
| H16 back-EMF / inductive kick | 1N5819 on the magnet; 470 µF + SMAJ5.0A at the terminal; separate USB logic supply | — | — |
| H17 lithium | none in SP1 | — | — |
| H19 no / failed emergency shutoff; red line 4 | NC e-stop in series with the rail, in reach; hold-to-run in the free hand; logic on USB stays up | Bus Watchdog 100 ms stops the servo if the MCU dies [SRC] | firmware reads the rail (A2) and mirrors it as PAUSED; never implements the stop |
| H21 hot motor near scalp | servo ≥ 75 mm from the scalp (MECH) | current limits keep dissipation low; Shutdown on overheat | Present Temperature readable (`status` prints it on request in a later rev) |
| H24 cannot remove quickly; red line 8 | release the button → rail dead → magnet drops → spring lifts ≥ 25 mm | servo unpowered → limp (XL330 back-drive torque small [EST]) | on FAULT: torque off + bus FET off; restart only via `reset` |
| H25 firmware faults; red line 13 | the rail loop does not depend on any of this | Bus Watchdog (servo-side), EEPROM limits (servo-side) | MCU WDT, one limits table printed at boot, single clamp point, motion timeout, comm-loss trip |
| Red line 7 (non-back-drivable servo) | spring-return lift on the hinge; leaf cap downstream (MECH) | — | torque off on every stop/fault so the arm is at least limp |

What firmware **cannot** do and does not claim: bound the normal force (that is the dead weight and leaf stops), lift the hand on comm loss (the Bus Watchdog *stops* the servo, it does not torque it off — the hardware rail lifts), or stop a latched hold-to-run (see §7, flag 4).

---

## 4. Control logic specification

### 4.1 State machine

```
            rail present, servo configured, zero sane, torque on at +25°
  INIT ───────────────────────────────────────────────────────────────▶ LIFTED_IDLE
   ▲  (no rail: wait, print every 2 s)                                     │ 1 s hold, run latch set
   │                                                                       ▼
   │  rail returns (servo was unpowered → re-write RAM registers)       RUNNING ──── stroke engine (§5)
   │◀──────────────────────── PAUSED ◀──── rail lost (button released / e-stop) ──┘
   │                                                                       │ 'stop' / 20-min limit: finish at +25°, torque off
   │                                                                       ▼
   │                                                               LIFTED_IDLE (torque off)
   │
   └──────── 'reset' ◀──── FAULT ◀── comm loss | over-current/stall | hardware error | motion timeout | zero out of range | config
                            (torque off + DXL power FET LOW; LED rapid flash; nothing restarts without 'reset')
```
- **INIT:** waits for the rail (A2 > ~1.3 V). Then `dxl.begin(1 Mbps)` (raises the DXL FET), ping ID 1 (falls back to 57600 and migrates a factory servo to 1 Mbps), model check (1200 = XL330-M288), torque off, EEPROM table written **only where it differs**, RAM registers, zero-sanity check (free-hanging hand within ±40° of zero, else FAULT `zero_out_of_range`), goal +25° at 60 mm/s, torque on, **Bus Watchdog armed last**.
- **LIFTED_IDLE:** torque on at +25° (lifted by geometry, 19.9 mm gap). After 1 s, if the run latch is set (default: the hold-to-run press *is* the start action; `stop` clears it, `run` sets it) → RUNNING. `goto`/`gotoraw`/`zero` are only accepted here.
- **RUNNING:** §5. Every 20 ms: read Present Position and Present Current (this feeds the Bus Watchdog), Hardware Error Status every 200 ms, trips, stroke engine, 1 Hz telemetry.
- **PAUSED:** rail is off; the servo and magnet are already dead by hardware; firmware waits and re-enters INIT when the rail returns (the servo rebooted, so RAM registers — goal current, profiles, watchdog, torque — are re-written).
- **FAULT:** torque off (best effort), `BDPIN_DXL_PWR_EN` LOW, LED 10 Hz, telemetry keeps printing the fault code; only `reset` leaves (→ INIT).

### 4.2 XL330-M288-T register settings (all [SRC: e-manual control table])

| Register (addr) | Value | Unit / meaning | Why |
|---|---|---|---|
| Operating Mode (11) | **5** current-based position | — | position goals with a hard current (torque) ceiling; "Goal Current(102) can be used to set a limit to current in Current-based Position Control Mode" [SRC] |
| Baud Rate (8) | 3 (1 Mbps) | — | 50 Hz loop with three reads per tick; migrated from factory 57600 by firmware |
| Return Delay Time (9) | **0** | 2 µs/LSB (default 250 = 500 µs) | fastest turnaround |
| Status Return Level (68) | **2** | all instructions answered | every write is acknowledged → every write is verifiable (deviation 2) |
| Homing Offset (20) | set by `zero` | ticks; Present = Actual + Offset [SRC] | puts the hanging-vertical hand at 2048 |
| Min Position Limit (52) | **1729** (= 2048 − 28°·11.378) | 0.088°/LSB | −28° absolute; the servo refuses goals below |
| Max Position Limit (48) | **2367** | | +28° absolute |
| Current Limit (38) | **450** | mA (default 1750) | EEPROM ceiling ≈ 1.9 N tangential; Goal Current cannot exceed it |
| Shutdown (63) | 0x34 (default) | overload, electrical shock, overheating | factory default kept explicitly |
| Goal Current (102) | **300** (RAM, `cur` command, 100–450) | mA | ≈ 1.26 N at 84 mm by the linear curve (§4.3) |
| Profile Acceleration (108) | 20–60 per stroke | 214.577 rev/min²/LSB = 21.46 °/s² | 0.63–1.9 m/s² at the tip |
| Profile Velocity (112) | per stroke, **cap 180** | 0.229 rpm/LSB | 25 / 50 / 75 LSB ≈ 50 / 100 / 150 mm/s; 180 LSB = 41.2 rpm = 0.36 m/s < 0.4 m/s cap |
| Goal Position (116) | per stroke, clamped ±25° (±284 ticks) | ticks | one clamp point: `setGoal()` |
| Bus Watchdog (98) | **5** = 100 ms, armed after torque on; cleared with 0 at every INIT | 20 ms/LSB | "If the measured communication interval is larger than the set value … the DYNAMIXEL will stop"; goal registers become read-only and the register reads −1 until cleared with 0 [SRC] |
| Present Position (132) / Present Current (126) / Hardware Error Status (70) | read 50 Hz / 50 Hz / 5 Hz | ticks / mA (signed) / bits 0,2,3,4,5 | telemetry, stall trip, fault trip |

**Zero calibration (`zero`):** rail on, not running. Firmware writes Homing Offset = 0, reads the raw Present Position with the **hand hanging freely vertical** (torque off, module latched down, nails ≥ 25 mm above the sphere so nothing touches), writes Homing Offset = 2048 − raw, re-reads and expects 0.0° ± 0.5°. The offset lives in the servo's EEPROM, so it survives reflashes and power cycles; redo it after any hand/arm re-mount. `+` is the stroke direction that lifts toward +25° park (horn facing +Y, right-hand rule about +Y): check on the bench that `goto 25` raises the nails on the *same* side every time and swap the sign convention in `degToTicks()` if the build has the horn mirrored.

### 4.3 Goal current from 1.2 N at 84 mm (the math)

- Datasheet points [SRC: [XL330-M288 specifications](https://emanual.robotis.com/docs/en/dxl/x/xl330-m288/)]: stall torque **0.52 N·m at 5.0 V, 1.47 A, quoted as 0.354 N·m/A**; 0.42 N·m at 3.7 V / 1.11 A (0.378 N·m/A); 0.60 N·m at 6.0 V / 1.74 A (0.345 N·m/A). The performance graph is linear in current to a good approximation; the torque constant at 5 V is K_t ≈ 0.354 N·m/A.
- Required torque: τ = F · r = 1.2 N × 0.084 m = **0.1008 N·m**.
- Linear estimate: I = τ / K_t = 0.1008 / 0.354 = **0.285 A → Goal Current = 300 mA** (→ 1.26 N on the same line).
- Ceiling: Current Limit 450 mA → 0.159 N·m → **1.90 N** at the tip, inside the 2.0 N wrist breakaway and red line 3.
- Expected running current: three nails × ~0.1 N drag × 0.084 m = 0.025 N·m → ~70 mA, plus inertia (hand ≈ 30 g at 84 mm, J ≈ 2.1×10⁻⁴ kg·m², α ≤ 22 rad/s² → 0.005 N·m → 13 mA) plus gear friction → **≈ 150 mA typical** [EST]; the 270 mA stall trip is ~1.8× that.
- Caveat and calibration: the linear curve passes through the origin, but the real gearbox needs a no-load current (not quoted for the XL330; 50–100 mA [EST]) before torque appears, so the *actual* stall force at 300 mA will be lower, roughly 0.85–1.1 N. Bench test **B7** blocks the arm against a kitchen/spring scale and adjusts `cur` until the stalled push reads **1.2 ± 0.2 N**; the result replaces `goalCurrentMa` in the config block. Current is a secondary layer; the 2.0 N wrist breakaway is the constant that bounds the worst case (safety §3.2).

### 4.4 Velocity, acceleration, timing
- ω = v / L. For v = 50, 100, 150 mm/s at L = 84 mm: 0.595, 1.19, 1.79 rad/s = 5.7, 11.4, 17.0 rpm = **25, 50, 75 LSB**. Cap 180 LSB (0.36 m/s).
- Acceleration 20–60 LSB (430–1290 °/s²) → 0.63–1.9 m/s² at the tip (< 2 m/s², team-G/H-5.4); the servo's trapezoidal profile does the shaping; shorter strokes become triangular automatically (Moving Status bits 4–5 [SRC]).
- Stroke timeout = 2 × (distance / velocity) + 600 ms; three consecutive timeouts → FAULT `motion_timeout`.

### 4.5 What the servo does on communication loss
With Bus Watchdog = 100 ms: the XL330 **stops** (holds its position under the current limit; goal registers become read-only; register 98 reads −1) [SRC]. It does **not** torque off by itself. Consequences: (a) if the MCU hung, the SAMD21 WDT resets it within 1 s → the DXL FET is off at boot → the bus is unpowered → the servo goes limp; (b) if the MCU is dead (USB pulled, Outcome B), the servo stays stopped under ≤ 300 mA until the operator releases the hold-to-run — the normal way to end anything (test-protocols §M); (c) the hand's normal force never came from the servo in the first place (dead weight), so a stopped servo is a resting hand at W, exactly the "H-5.9 stop with a loaded strand" Red Team 2 §6 named — which is why the lift is on the rail, not in the servo. On the firmware side, 5 consecutive failed reads (100 ms) → FAULT `comm_loss` → torque off + FET off.

---

## 5. Pattern engine (freeze §2) — specification, pseudocode, parameters

### 5.1 Parameters (defaults in the config block; all settable over serial)

| Symbol | Default | Freeze §2 | Serial |
|---|---|---|---|
| amplitude band (half-amplitude) | 12–25° | 12–25° (chord 33–68 mm, contact ≤ 36 mm) | `amp <min> <max>` |
| peak tip speed band | 50–150 mm/s × SPEED | 50–150 mm/s, SPEED pot scales | `speed <min> <max>` |
| SPEED pot | 0 / 50 / 100 % → ×0.5 / ×1.0 / ×1.5 (S1/S2/S3) | | `spd <%>` / `spd auto` |
| per-stroke jitter | ±25 % amp, ±25 % speed, × VARIATION | ±25 % | `jitter <%>` |
| direction asymmetry | up to 15 % × VARIATION | "randomized asymmetry" | `asym <%>` |
| end dwell | 0–300 ms × VARIATION | 0–300 ms | `dwell <ms>` |
| pause | every 4–10 strokes, 0.5–3 s at +25°, p = 1.0 | every 4–10 strokes, 0.5–3 s lifted | `pausen`, `pausems`, `pause <p>` |
| episode | every 5–20 s new sub-bands; p = 0.2 × VARIATION one slow long stroke (25°, 40 mm/s) | every 5–20 s | `episode <min> <max>`, `slow <p>` |
| VARIATION pot | 0–100 % scales all jitter, dwell, asymmetry, slow-stroke chance; at < 5 % bands collapse to their centres | 0–100 % | `var <%>` / `var auto` |
| PERIODIC | 18°, 100 mm/s × SPEED, no pauses/dwell/episodes | fixed 18°, fixed speed, no pauses | toggle, `mode`, `periodic <deg> <mm/s>` |
| strokes/s | emergent: 2·amp/ω + dwell → ≈ 1–3 /s | 1–3 /s | — |
| RNG seed | 0x5EEDC0DE | — | `seed <n>` (reproducible sessions) |

### 5.2 Pseudocode

```
every 20 ms tick (RUNNING):
  read PresentPosition, PresentCurrent (feeds Bus Watchdog); HardwareError every 10th tick
  trips: hwError → FAULT ; |I| ≥ 0.9·Igoal and |Δθ| < 0.3° for ≥ 250 ms → FAULT ; 5 failed reads → FAULT
  if session > 20 min → stop (finish at +25°, torque off)
  phase MOVING : if |θ − goal| < 1.5° → endStroke() ; elif t > timeout → count, endStroke() (3 in a row → FAULT)
  phase DWELL / PAUSE : if t ≥ phaseEnd → beginStroke()

beginStroke():
  if PERIODIC: amp = 18°, tip = 100 mm/s × S, acc = 40
  else (HUMAN):
    if t > episodeEnd: newEpisode()        # sub-bands [epAmp], [epSpd] ⊂ bands; width 30–100 %; maybe one slow stroke
    if slowStrokePending: amp = 25°, tip = 40 × S, acc = 20
    else: amp = U(epAmp) · (1 + U(−.25,.25)·V) ; tip = U(epSpd) · (1 + U(−.25,.25)·V) · S · (1 ± 0.15·V·U(0,1)) ; acc = U(20,60)
    dwell = U(0, 300 ms) · V
  first 3 strokes of a run: tip × 0.5 / 0.7 / 0.9     # soft start
  clamp amp ∈ [5°, 25°], tip ∈ [20, 360] mm/s ; vel = ω(tip)/0.229 rpm, ≤ 180
  write ProfileAccel, ProfileVelocity, GoalPosition(dir·amp) ; dir = −dir

endStroke():
  n++ ; if settings code changed → print "C," line ; print "S," line
  if HUMAN and --strokesToPause == 0: strokesToPause = U(4,10); with p=pause_prob → goal +25°, PAUSE U(0.5,3 s)+0.4 s
  else DWELL(dwell)
```

### 5.3 Startup, shutdown, fault behaviours
- **Startup** (freeze §2): rail on → INIT configures → torque on at **+25°**, **1 s hold** in LIFTED_IDLE → RUNNING with the 50/70/90 % ramp over the first three strokes (safety §4.7 soft-start ≥ 500 ms is met by the 1 s hold plus the ramp).
- **Shutdown** (`stop`, 20-min limit): the current stroke is abandoned for a goal of +25° at 80 mm/s, then torque off 1.5 s later ("finish stroke at +25°, torque off"). `run` after a stop re-enters INIT (fresh register check) and then the 1 s lifted hold.
- **Rail loss** (button released, e-stop): hardware has already removed servo power and dropped the magnet; the firmware mirrors this as PAUSED within one tick and re-initialises when the rail returns. Resuming through INIT → LIFTED_IDLE (1 s at +25°) → RUNNING with the ramp means **no stroke ever starts in contact**. Red Team 2 §6 asked for an explicit re-arm after a dead-man release; here the hold-to-run press is itself the explicit action and the 1 s lifted hold is the guard; set `AUTO_RUN_ON_RAIL = false` to require a serial `run` instead.
- **Fault** (comm loss, over-current/stall, hardware error, motion timeout, zero out of range, config): torque off (best effort), DXL FET LOW, LED 10 Hz, telemetry shows the fault name; only `reset` clears it. The hardware rail is what lifts the hand (freeze §2: "Fault … torque off (hardware rail handles the lift)").

### 5.4 Serial command interface (USB, 115200 8N1, newline-terminated)

| Command | Effect |
|---|---|
| `help`, `status`, `limits` | help; one-line status + full `C,` settings line; the limits table (also printed at boot) |
| `run`, `stop`, `reset` | set run latch / finish at +25° and torque off / leave FAULT → INIT |
| `zero` | zero calibration (rail on, not running, hand hanging) → Homing Offset in the servo |
| `goto <deg>` | LIFTED_IDLE only; clamps to ±28°; limit test (§Q.3 "go to +28°") |
| `gotoraw <deg>` | LIFTED_IDLE only; sends the unclamped goal; the servo must **refuse** anything beyond ±28° (prints ACCEPTED/REFUSED) |
| `hang` | stops the main loop → MCU watchdog reset in ≈ 1 s → DXL FET off → servo limp (§Q.3 watchdog test) |
| `mode human|periodic|auto` | override the toggle / return to it |
| `spd <0-100>|auto`, `var <0-100>|auto` | override the SPEED / VARIATION pots / return to them |
| `amp a b`, `speed a b`, `jitter %`, `asym %`, `dwell ms`, `pause p`, `pausen a b`, `pausems a b`, `episode a b`, `slow p`, `periodic deg mm/s` | pattern parameters (§5.1), all clamped inside the limits table |
| `cur <mA>` | goal current, clamped 100–450 (Current Limit); written immediately when the servo is up |
| `seed <n>` | reseed the xorshift32 RNG (same seed + same settings code = same stroke sequence) |
| `log on|off` | per-stroke lines on/off (telemetry and state lines always print) |
| `bset <slot 1-8> per|hum|auto <spd%|-1> <var%|-1>` | define a BLIND condition slot (−1 = leave that level to the pot) |
| `blind <n>` | shuffle slots 1..n (seeded), apply the first **without printing which**; mode shows `BLD`, S/V show −1 or 0 in logs |
| `next` | advance to the next hidden slot (between trials) |
| `reveal` | print `R,trial i = slot k MODE Sx Vy` for every trial |
| `unblind` | clear overrides, back to pots/toggle |

**Log lines** (all comma-separated, first field is a letter, `t` = ms since boot):
- `H,t,state,mode,spd%,var%,strokes,pos_deg,mA,fault,code` — **1 Hz, always** (§Q.3 echo of SPEED %, VARIATION %, MODE, stroke count, elbow position, fault code).
- `S,t,n,amp_deg,vel_lsb,tip_mm_s,dwell_ms,cur_peak_mA,cur_mean_mA,pos_end_deg,code` — one per stroke: timestamp, amplitude, speed, present current (peak and mean over the stroke), and the **settings code**.
- `C,t,code,amp…,spd…,jit,asym,dwell,pause,ep,slow,per,seed` — the full settings behind a code; printed at boot and whenever the code changes, so a log file is self-describing.
- `E,t,ampMin,ampMax,spdMin,spdMax[,slow]` episode; `Z,t,ms` pause; `T,stroke timeout`; `STATE …`; `R,…` reveal.
- **Settings code** = `MODE-S<spd%>-V<var%>-C<goal mA>#<hash>` e.g. `HUM-S50-V100-C300#3f1a`; the 16-bit hash covers every pattern parameter, goal current and seed. The Test Lead's notation (`HUM S2 V100`) maps directly: S1/S2/S3 = S0/S50/S100, V0/V50/V100 = V0/V50/V100. In BLIND the mode prints as `BLD` and hidden levels as 0/−1 until `reveal`.

---

## 6. Bring-up procedure and bench tests (pass criteria)

Equipment: multimeter, kitchen scale (1 g) or 0–5 N spring scale, a stopwatch/phone, the servo on the bench **without the hand** for B4–B6, with the hand for B7–B9.

| # | Step / test | Procedure | Pass |
|---|---|---|---|
| B0 | Toolchain | Arduino IDE 2.x; Boards Manager URL `https://raw.githubusercontent.com/ROBOTIS-GIT/OpenRB-150/master/package_openrb_index.json` → board "OpenRB-150"; Library Manager → Dynamixel2Arduino (0.7.x). Jumper on **VIN(DXL)**. Upload `sp1_scratch.ino` with **nothing on the rail**. | Boot banner `PROJECT SCRATCH SP1 SP1-fw-0.2` and the limits table print; `H,` lines at 1 Hz; `INIT: waiting for actuator rail`. |
| B1 | Polarity & rail | Brick → adapter → fuse → e-stop → button → terminal, **servo not yet plugged**. Meter the terminal: + is centre-positive 5.0 ± 0.25 V only while the button is held; 0 V with the button released; 0 V with the e-stop pressed regardless of the button. | all three readings; fuse value written on the diagram and the kit label. |
| B2 | Logic survives rail loss **[VERIFY]** | USB connected, button held (rail live), then release. Watch the serial monitor. | Outcome A: `H,` lines continue, state → PAUSED. Outcome B: board resets and re-prints the banner. Record which; both pass, B is noted in the session log template. |
| B3 | **No USB back-feed to the bus (hard gate)** | Rail open (button released), USB connected, firmware running. Meter the DXL port VDD pin against GND; plug the servo in. | **0.0 V**; servo LED dark; `INIT` keeps waiting. Any voltage → stop, fix the jumper, repeat. |
| B4 | Servo ID / baud | Plug the XL330 (factory ID 1, 57600). Hold the button. | Serial: `servo found at 57600, migrating to 1 Mbps` (first time only), then `STATE LIFTED_IDLE` and the horn moves to +25°. Alternative: Dynamixel Wizard 2.0 to set ID 1 / 1 Mbps beforehand. ID 2 (yaw) is set the same way in Stage 3, one servo on the bus at a time. |
| B5 | Zero calibration | Mount the arm + hand, module latched down, nails in free air. `stop`, release/hold the button, `zero`. Then `goto 0`, `goto 25`, `goto -25`. | `zero OK … now 0.0 deg`; the hand hangs vertical at `goto 0` (plumb line ± 1°); `goto 25` lifts toward the park side; both directions symmetric. |
| B6 | Position limits (K 2.13 / L 4.1) | `goto 28`, `goto -28` (hand held lightly), then `gotoraw 40` and `gotoraw -40`. | Hand reaches ±28° and no further; `gotoraw` prints **REFUSED** and the horn does not move; `H,` position never exceeds ±28.5°. |
| B7 | Goal-current calibration (over-current test) | `run`; while running, block the arm with a finger/spring scale at the nail tips. Then at `goto 0`, push the horn via the scale until it stalls. | Running: FAULT `over_current` within **≤ 300 ms** of blocking (stopwatch/video); LED rapid flash; `reset` required. Stalled push on the scale = **1.2 ± 0.2 N**; otherwise adjust `cur` and record the final value in the config block. |
| B8 | E-stop (K 3.5) | Running; press the e-stop. Twist to release. | Rail 0 V, servo limp, magnet drops, frame lifts ≥ 25 mm; firmware → PAUSED; on release *nothing moves* until the button is held, then INIT → 1 s at +25° → strokes. |
| B9 | Hold-to-run release | Running; release the thumb ×10. | Every time: servo limp + lift within the spring's time; resume only through the 1 s lifted hold; no stroke starts in contact (video). |
| B10 | Watchdog (K 4.3) | (a) `hang` while running; (b) unplug USB while running (rail live). | (a) reset in ≈ 1 s, banner reprints, DXL LED off, servo limp (hand liftable by hand) ≤ 1 s. (b) servo **stops** within 100 ms (Bus Watchdog) and holds under ≤ 300 mA; releasing the button lifts it; re-plugging USB → INIT clears the watchdog (`BUS_WATCHDOG` 0) and resumes only via the lifted hold. |
| B11 | Runaway / garbage input (K 4.6) | Type garbage, `amp 90 200`, `speed 5 9999`, `cur 9999`, wiggle pots, flip the toggle mid-stroke. | All values clamp (`status` shows the clamped numbers); position stays inside ±25° nominal, ±28° absolute; tip speed ≤ 0.36 m/s; mode changes take effect at the next stroke. |
| B12 | Telemetry & reproducibility | `seed 42`, `status`, run 30 s, `stop`; repeat. | Identical `S,` amplitude/speed sequences for the same seed and code; `H,` lines every 1.0 s; the `C,` line appears whenever a parameter changes. |
| B13 | BLIND | `bset 1 per -1 -1`, `bset 2 hum -1 0`, `bset 3 hum -1 50`, `bset 4 hum -1 100`, `blind 4`, run/`next` ×3, `reveal`. | Mode prints `BLD` throughout; `reveal` lists a permutation of the four slots; the pot echo shows −1 while blind. |
| B14 | 30-min soak (L7) | Per test-protocols L7, hold-to-run taped **for this bench test only**. | Zero faults, zero resets; XL330 case ≤ 48 °C; stroke count 1–3/s consistent with the log. |

---

## 7. Test Lead §Q compliance (test-protocols.md §Q.3–4)

| Requirement | Status | Where |
|---|---|---|
| 1 Hz serial echo of SPEED %, VARIATION %, MODE, stroke count, elbow position, fault code | **Met** | `H,` line, `telemetry()` |
| SPEED pot active in PERIODIC | **Met** — PERIODIC speed = 100 mm/s × (0.5 + pot) | `beginStroke()` |
| Serial "go to +28°", "hang", limits at boot | **Met** | `goto`, `gotoraw`, `hang`, `printLimits()` in `setup()` |
| BLIND: picks PER/HUM at random, reveals on request; randomized condition order hidden until the session ends | **Met for firmware-settable conditions** (mode, SPEED %, VARIATION %) via `bset`/`blind`/`next`/`reveal`. **Cannot be met for tips, weights, engagement or direction** — those are physical swaps Michael makes himself; blinding them needs the tip-code box procedure (§N "Blinding mechanics") or a helper. The firmware can print a hidden tip order at `reveal`, but it cannot stop the operator from seeing the tip he seats. | §5.4 |
| Hold-to-run lead ≥ 1.5 m | **Met** — 1.5 m 2-core 22 AWG | §1.3 row 4 |
| Button "cannot be latched" | **Partly met.** Momentary microswitch (no latching variant exists for this part), thumb well recessed 3 mm below a 36 mm rim so no flat object, tape or rubber band across the handle can hold it; firmware ends any run at 20 min; §M's "never taped, tied, latched, wedged" rule stands. **Flag:** no cheap handheld switch is proof against a deliberately inserted wedge; a true enabling (3-position) pendant is the industrial answer and is out of SP1's budget. | §1.4 |
| Fuse value on the wiring diagram, spare in the kit | **Met** — 1 A fast, on the schematic and in BOM notes | §1.2, §1.6 |
| Per-stroke log line carries the settings code | **Met** | `S,…,code` + `C,` lines |
| E-stop on a weighted base | **Met** (boxed e-stop on a steel plate) | §1.4 |
| Tape marks on both pots at 0/50/100 % | procedural, noted | §1.2 |

---

## 8. Sources
- OpenRB-150 e-manual: <https://emanual.robotis.com/docs/en/parts/controller/openrb-150/> ; mirror <https://docs.robotis.com/docs/parts/controller/openrb-150/> ; source <https://raw.githubusercontent.com/ROBOTIS-GIT/emanual/master/docs/en/parts/controller/openrb-150.md> ; board package <https://github.com/ROBOTIS-GIT/OpenRB-150> (`variants/OpenRB-150/variant.h`: A0–A6 = 15–21, LED_BUILTIN 32, BDPIN_DXL_PWR_EN 31, Serial1 = DXL port; `boards.txt`: `ARDUINO_OpenRB`, `__SAMD21G18A__`).
- XL330-M288-T e-manual (specs, control table, Bus Watchdog, Goal Current, Homing Offset): <https://emanual.robotis.com/docs/en/dxl/x/xl330-m288/> ; mirror <https://docs.robotis.com/docs/dxl/model_reference/x_series/xl_series/xl330-m288/>.
- Dynamixel2Arduino: <https://github.com/ROBOTIS-GIT/Dynamixel2Arduino> — `src/Dynamixel2Arduino.h` (API: `begin`, `setPortProtocolVersion`, `ping`, `setBaudrate`, `torqueOn/Off`, `setOperatingMode`, `setGoalPosition/Current`, `readControlTableItem`, `writeControlTableItem`, enums `OP_CURRENT_BASED_POSITION`, `UNIT_*`), `src/utility/master.h` (`getLastLibErrCode`, `getLastStatusPacketError`, `reboot`), `src/utility/port_handler.cpp` (DXL power FET on OpenRB), `examples/basic/position_mode/position_mode.ino` (`#elif defined(ARDUINO_OpenRB)`: `Serial1`, `DXL_DIR_PIN = -1`).
- SAMD21 watchdog sequence: Adafruit_SleepyDog `utility/WatchdogSAMD.cpp` <https://github.com/adafruit/Adafruit_SleepyDog>.
- Parts: Adafruit 1466 brick; Adafruit 3872 P20/15 electromagnet (5 V, 0.22 A, 2.5 kg) and 3873 P25/20; uxcell 30 mm arcade button B08HH78XMH; Philmore 30-825 B00T6RCGNC; TWTADE boxed e-stop B07NNZB41H; APIELE 1NC B0F2F8TYMY; uxcell inline fuse holder B07SM5KYZ7 (URLs in §1.4).
- Project: `01-foundations/safety-requirements.md`, `01-foundations/component-landscape.md` §6/§9, `01-foundations/scratch-model.md` §3–4, `04-redteam/redteam-2-mechanical.md` §6, `02-mechanisms/team-B.md` §2f, `02-mechanisms/team-G.md` §2c/§2f, `05-engineering/test-protocols.md` §K, §L, §Q.
