# SP1 v3 — ELECTRONICS + FIRMWARE (work package §11)

**Project SCRATCH · 14-build/electronics · 2026-10-02 · builder: Michael (careful first-timer)**
**Builds to:** 12-sp1v2/SYSTEM-SPEC-v3.md §4.5, §4.10–4.11, §5.4–5.5, §7.1, §7.8, §8 · safety-ruling C1–C8 · the 13 red lines.
**Files:** `firmware/printer.cfg` (Klipper), `firmware/sp1v3/` (host Python package), `firmware/pico/main.py` (tension front-end), `firmware/systemd/` (services), `firmware/tests/` (pytest), `CONFLICTS.md`, `parts.md`.
**Tags:** [KNOWN] = checked in a cited document today · [EST] = my arithmetic · [VERIFY] = a named bench step closes it.

> **Read CONFLICTS.md E-C1 first.** The spec's tendon geometry (deck stops R 48, yoke posts R 30) cannot hold the block with positive cable tension beyond ≈ 9 mm in three directions, so the block can never reach the rim there. The firmware checks this at boot and refuses to run until PAD/DRIVE BOX choose a geometry that passes (two passing options are given). Everything else in this package is independent of that choice: the geometry is a config value.

---

## 1. The design in one page

**Hardware safety loop (firmware cannot override it).** One 24 V adapter. The M8P logic and the CB1 are always powered. Everything that moves or pushes air — the three drum drivers (via the M8P's separate **Motor Power** input), and every valve and pump (via a 12 V buck) — hangs on **ACT-24**, which exists only while force-guided relay **K1** is closed. K1's coil current flows through a series chain: **e-stop pole 1 → hold-to-run lever → helmet loop (magnetic lanyard + head-present switch) → Q_LATCH → Q_WD**. K1's two NO contacts in series feed ACT-24 through **e-stop pole 2**. K1's first NC contact dumps ACT-24 into a 4.7 Ω bleeder the moment K1 drops; its second NC contact tells the M8P that K1 really released (weld check). **Q_LATCH** is held on by a 74HC74 flip-flop that any of eight open-collector "trip" inputs sets — six LM393 window comparators on the three cable tensions (slack or over-tension), **M8P_OK** low (host fault, Klipper shutdown, boot) and **PICO_OK** low (reflexd trip or dead) — and that only releasing the lever clears. **Q_WD** is held on by a diode charge pump fed by a 1 kHz square wave from the M8P; if Klipper, the host or the MCU stops, the square wave stops and K1 drops within ≈ 45 ms.

**Firmware.** Klipper on the M8P (MCU) and CB1 (host) drives the three drums as G-code axes A/B/C (`MANUAL_STEPPER … GCODE_AXIS`) with `kinematics: none`, switches the valves with `pwm_tool` (motion-synchronised, MCU watchdog), and runs the two pumps as `heater_generic` PID loops on pressure. On the CB1, `scorer.py` (state machine, modes, simple variation, the C5 path checker, dish-aware inverse kinematics, dead-band and spring compensation, logging, console) streams 5 ms G1 segments and keeps ≤ 0.5 s queued; `reflexd` reads the three tensions from a $4 Pico at 500 frames/s and trips the latch through the Pico; `scratchctl` is the console.

**Tests run here (2026-10-02, Python 3.14, macOS):** **118 passed** — IK 24, path checker 83 (incl. every planner mode × 3 seeds × 3 speeds), reflex criterion 6, scorer state machine/streaming against a Klipper simulator 5. See §8.7.

---

## 2. Schematic

Colours: red = 24 V unswitched, orange = ACT-24 (switched rail), brown = ACT-12, green = logic (3.3/5 V, always on), blue = signals into the M8P, grey dashed = inside the M8P.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 1010" width="1200" height="1010" font-family="Helvetica, Arial, sans-serif" font-size="11">
  <defs>
    <marker id="a" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#333"/></marker>
  </defs>
  <rect width="1200" height="1010" fill="#fff"/>
  <text x="12" y="20" font-size="15" font-weight="bold">SP1 v3 drive box: hardware safety loop, power, and safety logic (ELECTRONICS WP, 2026-10-02)</text>

  <!-- ===== POWER ENTRY ===== -->
  <rect x="12" y="40" width="120" height="54" fill="#fff" stroke="#333"/>
  <text x="22" y="58" font-weight="bold">24 V adapter</text>
  <text x="22" y="72">Mean Well GST60A24</text>
  <text x="22" y="86">J1 2.1 mm, centre +</text>
  <rect x="150" y="52" width="74" height="30" fill="#fff" stroke="#333"/>
  <text x="158" y="71">F1 T3.15A</text>
  <line x1="132" y1="67" x2="150" y2="67" stroke="#c00" stroke-width="2.5"/>
  <line x1="224" y1="67" x2="262" y2="67" stroke="#c00" stroke-width="2.5"/>
  <circle cx="262" cy="67" r="4" fill="#c00"/>
  <text x="240" y="58" fill="#c00" font-weight="bold">+24V_IN</text>
  <text x="232" y="100" font-size="10">SMAJ26A + 470 µF</text>
  <!-- to M8P VIN -->
  <line x1="262" y1="67" x2="860" y2="67" stroke="#c00" stroke-width="2.5" marker-end="url(#a)"/>
  <text x="560" y="60" fill="#c00">unswitched: M8P POWER (VIN) terminal = MCU + CB1 + 5 V/3.3 V logic (never switched)</text>

  <!-- ===== COIL CHAIN (y=190) ===== -->
  <text x="290" y="150" font-weight="bold" font-size="13">K1 COIL CHAIN (≈ 15 mA at 24 V): every element is a series opening</text>
  <line x1="262" y1="67" x2="262" y2="190" stroke="#c00" stroke-width="2.5"/>
  <rect x="280" y="165" width="96" height="50" fill="#fff" stroke="#c00" stroke-width="2"/>
  <text x="290" y="183" font-weight="bold">E-STOP NC1</text>
  <text x="290" y="197">puck, J2 pins 1-2</text>
  <text x="290" y="209">latching 2NC</text>
  <line x1="262" y1="190" x2="280" y2="190" stroke="#c00" stroke-width="2.5"/>
  <line x1="376" y1="190" x2="410" y2="190" stroke="#c00" stroke-width="2.5"/>
  <circle cx="400" cy="190" r="3.5" fill="#c00"/><text x="392" y="182">N1</text>
  <rect x="410" y="165" width="100" height="50" fill="#fff" stroke="#c00" stroke-width="2"/>
  <text x="420" y="183" font-weight="bold">HOLD-TO-RUN</text>
  <text x="420" y="197">lever NO, J3 1-2</text>
  <text x="420" y="209">(Stage D: armrest)</text>
  <line x1="510" y1="190" x2="545" y2="190" stroke="#c00" stroke-width="2.5"/>
  <circle cx="535" cy="190" r="3.5" fill="#c00"/><text x="527" y="182">N2</text>
  <rect x="545" y="160" width="150" height="60" fill="#fff" stroke="#c00" stroke-width="2"/>
  <text x="553" y="177" font-weight="bold">HELMET LOOP</text>
  <text x="553" y="191">J4 → umbilical 26 AWG →</text>
  <text x="553" y="203">magnetic pogo lanyard →</text>
  <text x="553" y="215">head-present switch → back</text>
  <line x1="695" y1="190" x2="725" y2="190" stroke="#c00" stroke-width="2.5"/>
  <circle cx="715" cy="190" r="3.5" fill="#c00"/><text x="707" y="182">N3</text>
  <rect x="725" y="165" width="92" height="50" fill="#fff8f0" stroke="#333" stroke-width="2"/>
  <text x="733" y="183" font-weight="bold">K1 COIL</text>
  <text x="733" y="197">SFS2-DC24V</text>
  <text x="733" y="209">diode + 18 V Z</text>
  <line x1="817" y1="190" x2="845" y2="190" stroke="#333" stroke-width="2"/>
  <rect x="845" y="168" width="78" height="44" fill="#fff" stroke="#333"/>
  <text x="852" y="185" font-weight="bold">Q_LATCH</text>
  <text x="852" y="199">2N7000</text>
  <line x1="923" y1="190" x2="948" y2="190" stroke="#333" stroke-width="2"/>
  <rect x="948" y="168" width="78" height="44" fill="#fff" stroke="#333"/>
  <text x="956" y="185" font-weight="bold">Q_WD</text>
  <text x="956" y="199">2N7000</text>
  <line x1="1026" y1="190" x2="1060" y2="190" stroke="#333" stroke-width="2"/>
  <text x="1064" y="194">GND</text>
  <line x1="884" y1="212" x2="884" y2="268" stroke="#2a8a2a" stroke-width="1.5" stroke-dasharray="5 3"/>
  <text x="890" y="262" fill="#2a8a2a">gate ← /Q (latch)</text>
  <line x1="987" y1="212" x2="987" y2="240" stroke="#2a8a2a" stroke-width="1.5" stroke-dasharray="5 3"/>
  <text x="993" y="236" fill="#2a8a2a">gate ← charge pump</text>

  <!-- ===== CONTACT CHAIN (y=320) ===== -->
  <text x="290" y="293" font-weight="bold" font-size="13">RAIL PATH: e-stop pole 2 + two K1 NO contacts in series</text>
  <line x1="262" y1="190" x2="262" y2="320" stroke="#c00" stroke-width="2.5"/>
  <rect x="280" y="296" width="96" height="48" fill="#fff" stroke="#c00" stroke-width="2"/>
  <text x="290" y="314" font-weight="bold">E-STOP NC2</text>
  <text x="290" y="328">J2 pins 3-4</text>
  <text x="290" y="340">20 AWG</text>
  <line x1="262" y1="320" x2="280" y2="320" stroke="#c00" stroke-width="2.5"/>
  <line x1="376" y1="320" x2="410" y2="320" stroke="#c00" stroke-width="2.5"/>
  <rect x="410" y="300" width="64" height="40" fill="#fff8f0" stroke="#333"/>
  <text x="418" y="318" font-weight="bold">K1 NO-a</text><text x="418" y="332">13-14</text>
  <line x1="474" y1="320" x2="494" y2="320" stroke="#c00" stroke-width="2.5"/>
  <rect x="494" y="300" width="64" height="40" fill="#fff8f0" stroke="#333"/>
  <text x="502" y="318" font-weight="bold">K1 NO-b</text><text x="502" y="332">23-24</text>
  <line x1="558" y1="320" x2="600" y2="320" stroke="#e07000" stroke-width="3"/>
  <circle cx="600" cy="320" r="4" fill="#e07000"/>
  <text x="575" y="312" fill="#e07000" font-weight="bold">ACT-24</text>
  <line x1="600" y1="320" x2="860" y2="320" stroke="#e07000" stroke-width="3" marker-end="url(#a)"/>
  <text x="640" y="312" fill="#e07000">→ M8P MOTOR POWER (HV) terminal: drivers 1-3 (jumper HV)</text>
  <text x="640" y="336" font-size="10">SMAJ26A + 470 µF 35 V at the terminal</text>
  <!-- buck -->
  <line x1="600" y1="320" x2="600" y2="380" stroke="#e07000" stroke-width="3"/>
  <rect x="560" y="380" width="90" height="40" fill="#fff" stroke="#333"/>
  <text x="568" y="398" font-weight="bold">BUCK 12 V</text><text x="568" y="412">XL4015 5 A</text>
  <line x1="650" y1="400" x2="700" y2="400" stroke="#8a5a00" stroke-width="3"/>
  <text x="656" y="392" fill="#8a5a00" font-weight="bold">ACT-12</text>
  <rect x="700" y="372" width="178" height="58" fill="#fff" stroke="#8a5a00"/>
  <text x="708" y="388">+ of: PIN A, PIN B, PALM,</text>
  <text x="708" y="401">RAIL DUMP, PALM DUMP, P1, P3</text>
  <text x="708" y="414">SS14 across every coil/motor</text>
  <text x="708" y="426">− side → M8P low-side outputs</text>
  <line x1="878" y1="400" x2="905" y2="400" stroke="#1f5fbf" stroke-width="2" marker-end="url(#a)"/>
  <!-- bleeder and NC aux -->
  <line x1="530" y1="320" x2="530" y2="460" stroke="#e07000" stroke-width="2"/>
  <rect x="490" y="460" width="80" height="34" fill="#fff8f0" stroke="#333"/>
  <text x="498" y="475" font-weight="bold">K1 NC-a</text><text x="498" y="488">31-32</text>
  <line x1="530" y1="494" x2="530" y2="512" stroke="#333" stroke-width="2"/>
  <rect x="500" y="512" width="60" height="26" fill="#fff" stroke="#333"/>
  <text x="506" y="529">4.7 Ω 5 W</text>
  <text x="440" y="560">bleeder → GND (closes only when K1 is released)</text>
  <rect x="330" y="460" width="80" height="34" fill="#fff8f0" stroke="#333"/>
  <text x="338" y="475" font-weight="bold">K1 NC-b</text><text x="338" y="488">41-42</text>
  <text x="240" y="512" fill="#1f5fbf">PF0 (M5-STOP) ↔ GND: "k1_nc"</text>
  <!-- rail sense -->
  <line x1="640" y1="320" x2="640" y2="470" stroke="#e07000" stroke-width="1.5"/>
  <rect x="610" y="470" width="80" height="30" fill="#fff" stroke="#1f5fbf"/>
  <text x="617" y="489">O4 PC817 → PF1</text>
  <text x="600" y="514" fill="#1f5fbf">"rail_sense"</text>

  <!-- ===== optos on N1 N2 N3 ===== -->
  <line x1="400" y1="190" x2="400" y2="240" stroke="#c00" stroke-width="1.2"/>
  <rect x="356" y="240" width="88" height="24" fill="#fff" stroke="#1f5fbf"/><text x="362" y="256">O1 → PD14 estop</text>
  <line x1="535" y1="190" x2="535" y2="240" stroke="#c00" stroke-width="1.2"/>
  <rect x="470" y="240" width="130" height="24" fill="#fff" stroke="#1f5fbf"/><text x="476" y="256">O2a → PD12, O2b → /CLR</text>
  <line x1="715" y1="190" x2="715" y2="240" stroke="#c00" stroke-width="1.2"/>
  <rect x="672" y="240" width="90" height="24" fill="#fff" stroke="#1f5fbf"/><text x="678" y="256">O3 → PC11 loop</text>

  <!-- ===== M8P box ===== -->
  <rect x="905" y="300" width="285" height="350" fill="#f4f8ff" stroke="#555" stroke-dasharray="6 3"/>
  <text x="915" y="318" font-weight="bold" font-size="13">BTT MANTA M8P V2.0 + CB1</text>
  <text x="915" y="336">Motor1/2/3 → drums A/B/C (TMC2209 standalone,</text>
  <text x="915" y="349">  1/16 µstep, VREF 0.35 V = 0.35 A peak)</text>
  <text x="915" y="366">HE0 PA0 PIN A · HE1 PA1 PIN B (25 Hz)</text>
  <text x="915" y="379">HE2 PA3 PALM 3-way · HE3 PA5 pump P1</text>
  <text x="915" y="392">FAN0 PF7 RAIL DUMP · FAN1 PF9 PALM DUMP</text>
  <text x="915" y="405">FAN3 PF8 pump P3 · FAN2 PF6 WATCHDOG 1 kHz</text>
  <text x="915" y="418">FAN4 PA4, HB PF5: pad-2 reserve</text>
  <text x="915" y="435">TH0 PB0 S_rail · TH1 PC5 S_A · TH2 PC4 S_B</text>
  <text x="915" y="448">TH3 PA7 S_palm · TB PB1 MODE ladder</text>
  <text x="915" y="461">FWS PC0 SPEED · PF10 INTENSITY</text>
  <text x="915" y="478">STOP PF4/PF3/PF2 drum index Halls</text>
  <text x="915" y="491">PF1 rail_sense · PF0 k1_nc · PC15 MOVED</text>
  <text x="915" y="504">PD13 latch_q · PD12 lever · PD14 estop</text>
  <text x="915" y="517">PC11 loop · PE9 → M8P_OK · PC12 → chime</text>
  <text x="915" y="530">PD15 NeoPixel ring</text>
  <text x="915" y="550" font-weight="bold">CB1 (Linux): Klipper host, scorer.py,</text>
  <text x="915" y="563" font-weight="bold">reflexd, scratchctl; USB → Pico</text>
  <text x="915" y="584" fill="#c00">HE "+" pins = VBB (24 V, unswitched):</text>
  <text x="915" y="597" fill="#c00">NEVER connect a load there (tape over).</text>
  <text x="915" y="614" fill="#c00">VFAN jumpers FAN0/1/3/4 = VIN (24 V);</text>
  <text x="915" y="627" fill="#c00">FAN2 = 12 V. Driver jumpers 1-3 = HV.</text>

  <!-- ===== SAFETY LOGIC (bottom) ===== -->
  <rect x="12" y="590" width="880" height="405" fill="#f3fbf3" stroke="#2a8a2a"/>
  <text x="22" y="610" font-weight="bold" font-size="13" fill="#2a8a2a">SAFETY BOARD (perfboard, logic domain: 5 V from the M8P servo header, 3.3 V from the Pico)</text>
  <!-- halls -->
  <rect x="24" y="625" width="150" height="74" fill="#fff" stroke="#333"/>
  <text x="32" y="641" font-weight="bold">3 tension Halls</text>
  <text x="32" y="655">DRV5053EA on flexures</text>
  <text x="32" y="669">VCC = Pico 3V3(OUT)</text>
  <text x="32" y="683">1 k + 100 nF each</text>
  <text x="32" y="695" font-size="10">tension ↑ ⇒ volts ↑</text>
  <line x1="174" y1="650" x2="230" y2="650" stroke="#333" stroke-width="1.5" marker-end="url(#a)"/>
  <line x1="174" y1="680" x2="230" y2="760" stroke="#333" stroke-width="1.5" marker-end="url(#a)"/>
  <rect x="230" y="625" width="140" height="56" fill="#fff" stroke="#333"/>
  <text x="238" y="641" font-weight="bold">Pico (RP2040)</text>
  <text x="238" y="655">GP26-28 ADC, 500 fr/s USB</text>
  <text x="238" y="669">GP15 → PICO_OK (47 k ↓)</text>
  
  <text x="378" y="645" fill="#2a8a2a" font-size="10">USB ↔ CB1 reflexd</text><text x="378" y="658" fill="#2a8a2a" font-size="10">('H' heartbeat, 'X' trip)</text>
  <!-- comparators -->
  <rect x="230" y="720" width="160" height="96" fill="#fff" stroke="#333"/>
  <text x="238" y="737" font-weight="bold">LM393 ×3: windows</text>
  <text x="238" y="751">per cable: V &lt; V(0.2 N) slack</text>
  <text x="238" y="765">          V &gt; V(3.6 N) over</text>
  <text x="238" y="779">thresholds: 3296 trimpots</text>
  <text x="238" y="793">from Pico 3V3 (ratiometric)</text>
  <text x="238" y="808">6 open-collector outputs</text>
  <rect x="230" y="830" width="160" height="66" fill="#fff" stroke="#333"/>
  <text x="238" y="847" font-weight="bold">LM393 #4: OK lines</text>
  <text x="238" y="861">M8P_OK (PE9) &lt; 1.0 V ⇒ trip</text>
  <text x="238" y="875">PICO_OK (GP15) &lt; 1.0 V ⇒ trip</text>
  <text x="238" y="889">100 k pull-downs: absent = trip</text>
  <!-- trip bus -->
  <line x1="390" y1="768" x2="440" y2="768" stroke="#c00" stroke-width="2"/>
  <line x1="390" y1="862" x2="440" y2="862" stroke="#c00" stroke-width="2"/>
  <line x1="440" y1="768" x2="440" y2="862" stroke="#c00" stroke-width="2"/>
  <line x1="440" y1="815" x2="500" y2="815" stroke="#c00" stroke-width="2" marker-end="url(#a)"/>
  <text x="446" y="806" fill="#c00" font-weight="bold">TRIP_N</text>
  <text x="446" y="848" font-size="10">4.7 k to 5 V</text><text x="446" y="860" font-size="10">+ 1 nF</text>
  <!-- latch -->
  <rect x="500" y="760" width="150" height="110" fill="#fff" stroke="#333" stroke-width="2"/>
  <text x="510" y="778" font-weight="bold">74HC74 (½), 5 V</text>
  <text x="510" y="796">/PRE ← TRIP_N (set = trip)</text>
  <text x="510" y="812">/CLR ← O2b: low while the</text>
  <text x="510" y="825">  lever is released (reset)</text>
  <text x="510" y="843">/Q → Q_LATCH gate (100 Ω)</text>
  <text x="510" y="858">Q → O5 PC817 → PD13</text>
  <text x="660" y="780" font-size="10">power-up: OK lines low ⇒ tripped</text>
  <text x="660" y="794" font-size="10">re-arm: trip cleared AND lever</text>
  <text x="660" y="808" font-size="10">released, then pressed again</text>
  <!-- charge pump -->
  <rect x="660" y="840" width="220" height="140" fill="#fff" stroke="#333" stroke-width="2"/>
  <text x="668" y="858" font-weight="bold">WATCHDOG CHARGE PUMP</text>
  <text x="668" y="874">FAN2 (PF6) 1 kHz 50 % hardware PWM,</text>
  <text x="668" y="887">2.2 k from FAN2+ (12 V) to FAN2−</text>
  <text x="668" y="900">FAN2− → C1 1 µF → node X</text>
  <text x="668" y="913">D2 1N4148 GND→X, D1 1N4148 X→OUT</text>
  <text x="668" y="926">C2 1 µF + R 18 k OUT→GND (τ 18 ms)</text>
  <text x="668" y="939">OUT ≈ 9.5 V → 1 k → Q_WD gate</text>
  <text x="668" y="952">square wave stops (any level) ⇒</text>
  <text x="668" y="965">gate &lt; 0.8 V in ≤ 45 ms ⇒ K1 drops</text>
  <line x1="770" y1="840" x2="770" y2="250" stroke="#2a8a2a" stroke-width="1.5" stroke-dasharray="5 3"/>
  <line x1="770" y1="250" x2="987" y2="250" stroke="#2a8a2a" stroke-width="1.5" stroke-dasharray="5 3"/>
  <line x1="575" y1="760" x2="575" y2="272" stroke="#2a8a2a" stroke-width="1.5" stroke-dasharray="5 3"/>
  <line x1="575" y1="272" x2="884" y2="272" stroke="#2a8a2a" stroke-width="1.5" stroke-dasharray="5 3"/>
  <text x="24" y="925" font-size="11">Hand controller (J3 GX16-8): lever (24 V coil chain), SPEED/INTENSITY 10 k pots (3.3 V), MODE 1P4T ladder</text>
  <text x="24" y="940" font-size="11">  (1 k / 3.3 k / 10 k / 33 k → TB), MOVED button (PC15). ADC lines: 1 k series + BAT54S clamp at the box.</text>
  <text x="24" y="960" font-size="11">Drum index: A3144 Halls on M1/M2/M3-STOP (+5 V, GND, signal). Pressure sensors XGZP6847A 3.3 V on TH0-3.</text>
  <text x="24" y="980" font-size="11" fill="#555">Nothing on the safety board or in the logic domain can supply ACT-24 or ACT-12. Loads have no + until K1 closes.</text>
</svg>

---

## 3. The safety loop, element by element

| # | Element | Opens the rail when | How it can fail | What catches that failure | Credited as |
|---|---|---|---|---|---|
| 1 | **E-stop** 2NC latching (pole 1 in the coil chain, pole 2 in the rail path) | pressed | one pole welds | the other pole still opens; O1 shows pole 1 state; A0 test every 10 cycles | hardware (red line 4) |
| 2 | **Hold-to-run lever** NO | released | contact sticks closed | head-present switch still opens on doff; 20-min cap; user can e-stop | hardware |
| 3 | **Helmet loop**: magnetic pogo lanyard + head-present microswitch | lanyard pulled off, helmet off the head | pogo pins bridged by sweat/debris | lanyard pull test every session (B6 checklist); head switch in series | hardware |
| 4 | **K1** Panasonic SFS2 force-guided, 2 NO in series + 2 NC | coil de-energised by any of 1–3, 5, 6 | one NO contact welds | second NO in series; NC-b cannot close (force-guided) → k1_nc input open with coil off → scorer refuses to arm; rail up with lever released > 150 ms → FAULT "press the E-STOP" (pole 2 still cuts) | hardware + firmware check |
| 5 | **Q_LATCH** (74HC74 + 2N7000), set by 6 comparators, M8P_OK, PICO_OK; cleared only by lever release | any trip | MOSFET fails short | latch tripping still logged (O5 → latch_q) but rail stays up → scorer sees latch_q with rail_sense high → FAULT → M8P vents outputs and disables drums; **A0/A4 proof test**: every ARMING the reflex path is exercised at A4 and every 10 sessions (`inject snag`) | hardware (backed by firmware detection) |
| 6 | **Q_WD** charge pump | the 1 kHz square wave stops (Klipper shutdown, klippy dead > 1 s, scorer heartbeat lost > 1 s → M112, MCU hang → IWDG reset) | MOSFET short | logged nowhere directly → **A0 proof test** (`SET_PIN PIN=watchdog VALUE=0` must drop the rail) repeated at every Stage gate | hardware |
| 7 | **Bleeder** via K1 NC-a | K1 releases | resistor open | rail decays more slowly (loads still discharge it); A0 timing test catches it | — |
| 8 | **pwm_tool `maximum_mcu_duration`** on every valve/dump | klippy stops refreshing for 2 s | — | MCU shutdown → all outputs to shutdown value | firmware (not credited) |
| 9 | **Heater max_temp 28 kPa** on rail and palm | pressure > 28 kPa or a sensor unplugged | — | MCU-side range check → Klipper shutdown | firmware (the reliefs are the credited cap) |

**Restart rule (SPEC §7.1):** when the rail returns the scorer goes to ARMING (dumps closed, lines vented, drums homed with the pad retracted, tension trim checked) and reaches the scalp only through APPROACH (lever held 1 s, palm on, lines at 0.10 N, 3 ramp strokes). There is no resume into contact.

**Why the helmet loop carries coil current (CONFLICTS E-C7):** a passive switch in series with the coil cannot fail closed by itself; a 3.3 V logic loop would need a transistor that can.

---

## 4. Resource map and wiring table (every wire)

### 4.1 Board settings before first power

| Setting | Where | Value | Why |
|---|---|---|---|
| Driver supply jumpers | 3-pin "HV · VM · VBB" header beside each driver socket | Motors 1, 2, 3: jumper on **HV–VM**. Motors 4–8: **no jumper, no driver** | drivers take power from the Motor Power (HV) terminal = ACT-24 (V-E1) |
| Driver mode jumpers | under each driver socket | **no UART jumper**; MS1 + MS2 jumpers fitted (TMC2209 standalone 1/16 with 256 interpolation) [VERIFY against the TMC2209 V1.3 sheet: MS2,MS1 = 1,1 → 1/16] | standalone = VREF is a hardware current cap; no UART = Klipper does not fault when motor power is cut |
| VFAN jumpers | VF0–VF4 blocks bottom-left | **FAN0, FAN1, FAN3, FAN4: VIN (24 V)**; **FAN2: 12 V** | E-C12: on-board flyback diodes go to VFAN; FAN2 feeds the charge pump |
| Thermistor PT1000 jumpers | near TH0–TH3 | **not fitted** (4.7 k pull-ups only) | pressure sensors read as voltage |
| VUSB jumper | centre of board | **not fitted** | board is powered from VIN, not USB |
| CB1 | BTB connector | seated per the M8P manual's orientation photo, heatsink on | — |
| TMC2209 VREF | trimmer on each driver | **0.35 V** (I_peak = VREF on BTT TMC2209 V1.3: I_RMS = VREF/√2) — set in §9.6 | SPEC §4.4 (see E-C6) |

### 4.2 Wiring table

Gauge: 18 AWG for +24V_IN/ACT-24 trunk, 20 AWG for ACT-12 trunk and e-stop pole 2, 22 AWG for single loads, 24–26 AWG for signals. Colour code: **red** +24V_IN, **orange** ACT-24, **yellow** ACT-12, **black** GND, **white/blue** signals, **green** 3.3 V/5 V logic.

| W | From | To | Wire | Termination | Notes |
|---|---|---|---|---|---|
| W1 | J1 DC jack centre (+) | F1 fuse holder in | 18 AWG red | solder + heat-shrink | meter polarity before first power (§9.1) |
| W2 | F1 out | TB1 terminal "+24V_IN" (safety board) | 18 AWG red | ferrule in screw terminal | SMAJ26A + 470 µF across +24V_IN/GND on the board |
| W3 | J1 sleeve (−) | TB1 "GND" (star point) | 18 AWG black | ferrule | the one ground star; everything returns here |
| W4 | TB1 +24V_IN | M8P **POWER +** (VIN) | 18 AWG red | ferrule | logic supply, never switched |
| W5 | TB1 GND | M8P **POWER −** | 18 AWG black | ferrule | |
| W6 | TB1 +24V_IN | J2-1 (e-stop pole 1 in) | 22 AWG red | GX12 solder cup | |
| W7 | J2-2 (pole 1 out) | TB2 "N1" | 22 AWG red | | O1 LED (10 k) from N1 to GND |
| W8 | N1 | J3-1 (lever in) | 22 AWG red | GX16 solder cup | |
| W9 | J3-2 (lever out) | TB2 "N2" | 22 AWG red | | O2a + O2b LEDs in series via 4.7 k to GND |
| W10 | N2 | J4-1 (helmet loop out) | 22 AWG red | GX12 | through the umbilical's loop pair |
| W11 | J4-2 (loop return) | TB2 "N3" | 22 AWG red | | O3 LED (10 k) to GND |
| W12 | N3 | K1 coil A1 (+) | 22 AWG red | PCB | 1N4007 + 1N4746A (18 V) in series across the coil, diode cathode to A1 |
| W13 | K1 coil A2 (−) | Q_LATCH drain | PCB trace | | Q_LATCH source → Q_WD drain; Q_WD source → GND |
| W14 | TB1 +24V_IN | J2-3 (e-stop pole 2 in) | 20 AWG red | GX12 | carries rail current (≤ 2.5 A) |
| W15 | J2-4 (pole 2 out) | K1 NO-a pin 13 | 20 AWG red | PCB | |
| W16 | K1 NO-a 14 | K1 NO-b 23 | PCB trace ≥ 2 mm | | contacts in series |
| W17 | K1 NO-b 24 | TB3 "ACT-24" | 18 AWG orange | | SMAJ26A + 470 µF 35 V at TB3 |
| W18 | TB3 ACT-24 | M8P **Motor Power +** (HV) | 18 AWG orange | ferrule | |
| W19 | TB1 GND | M8P **Motor Power −** | 18 AWG black | ferrule | |
| W20 | TB3 ACT-24 | buck IN+ | 20 AWG orange | screw | buck IN− to GND star |
| W21 | buck OUT+ | Wago bus "ACT-12" (5-way) | 20 AWG yellow | lever nut | set the buck to 12.0 V with no load first (§9.6) |
| W22 | TB3 ACT-24 | K1 NC-a 31 | PCB | | NC-a 32 → 4.7 Ω 5 W → GND |
| W23 | K1 NC-b 41 | M8P **M5-STOP signal (PF0)** | 24 AWG white | Dupont/XH | NC-b 42 → M5-STOP GND pin |
| W24 | TB3 ACT-24 | O4 LED anode via 10 k | PCB | | O4 collector → M4-STOP signal (PF1), emitter → GND |
| W25 | O1 collector / emitter | PS-ON header PD14 / GND | 24 AWG white | | |
| W26 | O2a collector / emitter | Probe header PD12 / GND | 24 AWG white | | |
| W27 | O2b collector → 5 V; emitter → /CLR (pin 1) with 10 k to GND | — | PCB | | emitter-follower: lever held ⇒ /CLR high |
| W28 | O3 collector / emitter | SPI header PC11 / GND | 24 AWG white | | |
| W29 | 74HC74 Q (pin 5) → 1 k → O5 LED | O5 collector → Probe header PD13 | 24 AWG white | | latch state |
| W30 | 74HC74 /Q (pin 6) | Q_LATCH gate via 100 Ω; 100 k gate → GND | PCB | | |
| W31 | M8P servo header (+5 V, GND, PE9) | safety board 5 V, GND, M8P_OK | 3-wire 24 AWG | servo plug | M8P_OK with 100 k pull-down on the board |
| W32 | M8P FAN2 + and − | charge-pump input (2.2 k from + to −; − to C1) | 24 AWG | XH | FAN2 VFAN jumper = 12 V |
| W33 | charge-pump OUT | Q_WD gate via 1 k | PCB | | 18 k + 1 µF to GND at OUT |
| W34 | Pico 3V3(OUT), GND | Hall VCC/GND (×3), comparator reference trimpots | 26 AWG green/black | | ratiometric |
| W35 | Hall A/B/C outputs | 1 k → Pico GP26/27/28 **and** LM393 inputs; 100 nF to GND at the board | 26 AWG shielded 3-core per Hall | JST-XH 3-pin | Halls sit on the drum-module flexures (DRIVE BOX) |
| W36 | Pico GP15 | LM393 #4 IN+ (PICO_OK), 47 k to GND | PCB | | |
| W37 | Pico micro-USB | M8P USB-A port (CB1) | USB cable 0.3 m | | |
| W38 | ACT-12 bus | + of PIN A, PIN B, PALM, RAIL DUMP, PALM DUMP valves; P1, P3 pumps | 22 AWG yellow | Wago | SS14 across each coil/motor, band (cathode) to + |
| W39 | PIN A − | **HE0 second pin (drain)** | 22 AWG black | KF128 screw | never the HE0 "+" pin (VBB) |
| W40 | PIN B − | HE1 drain | 22 AWG black | | |
| W41 | PALM 3-way − | HE2 drain | 22 AWG black | | |
| W42 | P1 rail pump − | HE3 drain | 22 AWG black | | 100 nF across the pump too |
| W43 | RAIL DUMP − | FAN0 − | 22 AWG black | PH2.54 2-pin | FAN0 "+" unused |
| W44 | PALM DUMP − | FAN1 − | 22 AWG black | | |
| W45 | P3 palm pump − | FAN3 − | 22 AWG black | | pump ≤ 0.8 A |
| W46 | S_rail, S_A, S_B, S_palm outputs | TH0 (PB0), TH1 (PC5), TH2 (PC4), TH3 (PA7) signal pins | 26 AWG | XH 2-pin | TH GND pin = sensor GND |
| W47 | SPI header 3.3 V | pressure-sensor VCC (×4, 3 mA each) and hand-controller 3V3 (J3-3) | 26 AWG green | | M8P 3.3 V = the ADC reference |
| W48 | J3-5 SPEED wiper | 1 k → FWS PC0, BAT54S clamp | 26 AWG | | |
| W49 | J3-6 INTENSITY wiper | 1 k → FWS PF10, BAT54S clamp | 26 AWG | | |
| W50 | J3-7 MODE ladder | TB thermistor input (PB1) signal | 26 AWG | XH 2-pin | on-board 4.7 k pull-up does the divider |
| W51 | J3-8 MOVED | M6-STOP signal (PC15) | 26 AWG | | button to J3-4 GND |
| W52 | J3-4 GND | M8P GND (any header GND) | 24 AWG black | | |
| W53 | Drum index Halls A/B/C (+5 V, GND, OUT) | M1/M2/M3-STOP (+5 V, G, PF4/PF3/PF2) | 26 AWG 3-core | XH 3-pin | A3144 open-collector; MCU pull-up |
| W54 | Drum steppers A/B/C | Motor1/2/3 (2B 2A 1A 1B) | stepper cable | XH 4-pin | swap one coil pair to reverse if needed (or flip dir_pin) |
| W55 | NeoPixel ring (5 V, GND, DIN) | RGB header (+5 V, GND, PD15) | 26 AWG | | 330 Ω in DIN at the ring |
| W56 | Buzzer 5 V + | safety-board 5 V; buzzer − → 2N7000 drain; gate ← PC12 via 1 k (SPI header) | 26 AWG | | |

**Strain relief:** every cable leaving the case passes a panel connector (J1–J4); inside, every bundle is tied to an adhesive tie-mount within 50 mm of its terminal. No bare terminal is exposed: the safety board sits under a 2 mm acrylic or printed cover.

---

## 5. Connector pinouts

| Connector | Type | Pin 1 | Pin 2 | Pin 3 | Pin 4 | Pin 5 | Pin 6 | Pin 7 | Pin 8 |
|---|---|---|---|---|---|---|---|---|---|
| **J1** power | 5.5 × 2.1 panel jack | centre = +24 V | sleeve = GND | | | | | | |
| **J2** e-stop puck | GX12-4 (box: female) | +24V_IN → NC1 | NC1 → N1 | +24V_IN → NC2 | NC2 → K1 NO-a | | | | |
| **J3** hand controller | GX16-8 (box: female) | N1 (24 V) → lever | lever → N2 | +3.3 V | GND | SPEED wiper | INTENSITY wiper | MODE ladder | MOVED (to GND) |
| **J4** helmet loop | GX12-4 (box: female) | N2 → loop out | loop return → N3 | spare | spare | | | | |
| **Hand controller inside** | — | lever COM ← pin 1, lever NO → pin 2 (Omron V-15G2: COM + NO tabs) | | pots: CW end → pin 3 | pots: CCW end, button, ladder common → pin 4 | | | ladder: 1 k / 3.3 k / 10 k / 33 k from the rotary positions PLINE/LINE/CIRCLE/MIX to pin 7 (rotary common to pin 4) | button NO → pin 8 |
| **Umbilical loop pair** | 2 of the 4 cores | J4-1 → pogo pin 1 → head switch COM | head switch NO → pogo pin 2 → J4-2 | | | | | | |
| **Pico** | — | GP26 ← Hall A | GP27 ← Hall B | GP28 ← Hall C | GP15 → PICO_OK | 3V3(OUT) → Halls + refs | GND | GP25 = on-board LED | (GP4/GP5 reserved: pad-2 ADS1115) |

**Keying rule:** 24 V lives only on J3 pins 1–2 at one end of the GX16 face; a pin-bent short to pins 5–7 is clamped by the 1 k + BAT54S on each ADC line (and TB has the board's own protection).

---

## 6. Safety-loop timing analysis

Capacitance on ACT-24 [EST]: 470 µF (added) + 3 × 100 µF (driver sockets 1–3 on HV, M8P schematic) + ≤ 560 µF (HV input bulk, not legible in the schematic) + ≈ 220 µF (buck input) ≈ **1.55 mF**. Bleeder 4.7 Ω → τ = 7.3 ms. ACT-12: buck output ≈ 220 µF into ≈ 20 Ω of coils → τ ≈ 4.4 ms.

| Step | Typical | Worst | Basis |
|---|---|---|---|
| Trigger → K1 coil current stops: e-stop / lever / loop (contact opens) | < 0.1 ms | 1 ms (bounce) | mechanical |
| … comparator trip (Hall RC 0.1 ms + LM393 + 74HC74 + 2N7000) | 0.2 ms | 0.3 ms | datasheets [EST] |
| … reflexd trip (frame 2 ms + 2-frame rule 2 ms + USB 1 ms + compute + 'X' 1 ms + Pico loop 2 ms) | 5 ms | 9 ms | [EST] — C4 A4 test: ≤ 50 ms |
| … watchdog: square wave stops → gate < 0.8 V (τ 18 ms, from 9.5 V) | 28 ms | 45 ms | [EST]; + 1.0 s (klippy loss, `maximum_mcu_duration`) or + 0.5 s (MCU hang, STM32 IWDG 410–512 ms) or + 1.25 s (scorer hang → heartbeat → M112) before the wave stops |
| K1 release (NO contacts open), diode + 18 V Zener clamp | ≈ 5 ms | **20 ms** | Panasonic SF datasheet: release time max 20 ms [KNOWN] |
| NC-a closes → ACT-24 24 → 13 V (buck drops out) | 4.5 ms | 6 ms | 0.61 τ |
| ACT-24 → < 4 V (TMC2209 under-voltage; drums limp) | 13 ms | 16 ms | 1.8 τ |
| ACT-12 → valve/pump drop-out (≈ 35 % of 12 V) | 5 ms | 8 ms | ≈ 1.1 τ_12 |
| **Trigger → rail dead (ACT-24 < 4 V)** | **≈ 18 ms** | **≈ 35 ms** | sum |
| **Trigger → valves de-energised** | **≈ 15 ms** | **≈ 31 ms** | sum |
| Valve de-energised → gallery < 0.05 N | ≤ 100 ms | 100 ms | ruling C3 [VERIFY A2] |
| **Trigger → nails vented** | ≈ 115 ms | **≈ 131 ms** | |
| PALM de-energised → pad retracted 25 mm (QEV) | ≤ 150 ms | 150 ms | SPEC §4.11 [VERIFY B4] |
| **Trigger → pad retracted** | ≈ 165 ms | **≈ 181 ms** | |

Against SPEC §4.11: "rail dead < 5 ms" is not achievable with a force-guided relay (CONFLICTS E-C3); everything downstream of it holds. The A0 gate measures it: **each element opens ACT-24 (< 4 V) within 35 ms, 10 cycles each, logic stays up.**

---

## 7. Limits table (hardware + firmware), printed at boot by `limits`

| Quantity | Hardware limit (credited) | Firmware limit (not credited) | Where set |
|---|---|---|---|
| Drum motor current | VREF 0.35 V → 0.35 A peak (≈ 7.6 N at the drum, E-C6) | — | trimmer, §9.6 |
| Tangential force on the block | 2.0 N magnetic coupling (PAD) | reflexd residual 0.8 N / 0.5 N opposing 60 ms | `reflexd.py` |
| Cable tension window | LM393: < 0.2 N or > 3.6 N → latch | same in reflexd (2 frames) | trimpots, §9.9 |
| Cable speed | — | 250 mm/s (`LIMIT_VELOCITY`), position ±25 mm | `printer.cfg`, `scorer.py` |
| Block offset |d| | dish rim top 17.0 mm, yoke cage ±18 | 16.5 mm (P1) | `limits.py` |
| Path speed / contact accel | — | 200 mm/s; 2 m/s² in contact | `limits.py` |
| No-reversal radius | dish geometry (lift ≥ 5 mm outside 13.7) | 13.7 mm, heading ≤ 30°/50 ms, cusp < 10 mm/s | `checker.py` |
| Landing speed | — | ≥ 0.3 v_peak in 8.5–12.2 mm | `checker.py` |
| Frequency | — | PLINE 0.6–2.0 Hz, CIRCLE 0.6–1.5 Hz | `limits.py` |
| Circle | — | R 9–12.5, R+e ≥ 14.5, R−e ≤ 8.5, offset 15–40°/rev | `limits.py`, `checker.py` |
| Nail force | R1a 20.7 kPa = 0.80 N; R1b ≈ 24 kPa (DRIVE BOX) | rail ≤ 15.6 kPa = 0.60 N; Stage B 0.20–0.45 N | `limits.py` |
| Constant support | palm reliefs (DRIVE BOX) | Σ F_pins + 0.45 N ≤ F_float; palm ≤ 20 kPa | `checker.py` P9 |
| Rail / palm sensor range | — | Klipper `max_temp` 28 kPa → MCU shutdown | `printer.cfg` |
| Valve command freshness | — | `maximum_mcu_duration` 2.0 s on every valve, 1.0 s on the watchdog | `printer.cfg` |
| Host liveness | watchdog charge pump | heartbeat 0.25 s, M112 after 1.0 s; reflexd heartbeat 50 ms, Pico drops OK at 250 ms | `printer.cfg`, `pico/main.py` |
| Session | — | 20 min; station dwell 90 s (placeholder, set at B5) | `limits.py` |
| Fuse | T3.15 A on +24V_IN | — | F1 |

---

## 8. Firmware

### 8.1 Structure (`firmware/`)

| File | Lines | What it does |
|---|---|---|
| `printer.cfg` | — | Klipper: 3 manual steppers (drums), 5 valve/dump `pwm_tool`s, watchdog `pwm_tool` (hardware PWM 1 kHz), 2 pump `heater_generic`s with kPa tables, 2 line sensors, 2 knobs, 11 `gcode_button`s (loop states, MOVED, MODE ladder), NeoPixel, host-heartbeat `delayed_gcode` → M112, homing macro |
| `sp1v3/limits.py` | 150 | the one limits table and clamp point; settings code; force arithmetic |
| `sp1v3/ik.py` | 420 | dish model (rise, tilt), `TendonIK` (IK, FK, Jacobian, conditioning, statics, workspace **audit**), `CableComp` (dead band + spring feed-forward) |
| `sp1v3/paths.py` | 210 | `line` (PLINE/LINE/CHORD), `circle` (offset + precession), `dpath`, `rim_arc` connectors, `park`; every token starts and ends at rest on the rim |
| `sp1v3/checker.py` | 210 | rules P1–P12 (C5 and §8.3) |
| `sp1v3/variation.py` | 100 | §8.4 draws (chords, period, heading kicks, pauses, force phrases, group patterns, MIX phrases, no-repeat) |
| `sp1v3/planner.py` | 265 | mode → checked token stream; force/palm bookkeeping (constant support) |
| `sp1v3/forcemodel.py` | 50 | rim reaction + PTFE + scalp drag model shared by feed-forward and reflexd |
| `sp1v3/scorer.py` | 930 | state machine §8.1, streamer, controls, supervision, console server, CSV logs |
| `sp1v3/reflexd.py` | 270 | snag criterion, planned-path buffer, Pico link |
| `sp1v3/scratchctl.py` | 80 | console client |
| `sp1v3/klipper.py` | 230 | API-socket client + simulator |
| `sp1v3/benchtest.py` | 70 | S0/A0 streaming test |
| `pico/main.py` | 60 | MicroPython tension front-end + PICO_OK |
| `systemd/*.service` | — | `sp1-reflexd`, `sp1-scorer` |
| `tests/` | — | pytest (§8.7) |

### 8.2 Kinematics and streaming — what Klipper actually does (checked in the docs and source, 2026-10-02)

* **GCODE_AXIS exists and behaves as the spec assumed:** `MANUAL_STEPPER STEPPER=config_name GCODE_AXIS=[A-Z] [LIMIT_VELOCITY=…] [LIMIT_ACCEL=…] [INSTANTANEOUS_CORNER_VELOCITY=…]` — "configures the stepper motor as an extra axis on G1 move commands … The resulting moves will occur synchronously with the associated toolhead xyz movements" (Klipper G-Codes reference). While registered, `MANUAL_STEPPER … MOVE` is refused, so homing first unregisters (`GCODE_AXIS=`), homes with `STOP_ON_ENDSTOP=home`, then re-registers.
* **With `kinematics: none` every move is extra-axis-only** (`toolhead.py`, `Move.__init__`): duration = max |Δaxis| / speed; junction blending is skipped (`calc_junction` returns for non-kinematic moves), so every segment starts and ends at zero speed **with the per-axis acceleration**. Hence `accel: 0` on the steppers and `LIMIT_ACCEL=100000000` at registration: each 5 ms segment then runs at constant speed and the stop-start at the boundary lasts ≈ 1 µs. The host writes `F = 60 · max|Δl| / Δt`. `INSTANTANEOUS_CORNER_VELOCITY` is irrelevant here (E-C4).
* **SET_PIN timing:** `SET_PIN` on `output_pin` and `pwm_tool` is queued with `register_lookahead_callback`, i.e. it executes at the print time between the surrounding G1 moves. `output_pin` enforces ≥ 100 ms between updates on one pin (`MIN_SCHEDULE_TIME = 0.100`, mcu.py); `pwm_tool` does not. `maximum_mcu_duration` (≤ 3.0 s, `MAX_NOMINAL_DURATION`) exists only on `pwm_tool`, needs value = shutdown value, and the host re-sends the value automatically while it is non-default (pwm_tool.py `_gen_intermediate_updates`).
* **Queue depth:** `BUFFER_TIME_HIGH = 1.0` s; the API's `gcode/script` returns when the script is processed (for G1: queued) and blocks when > 1 s is buffered. The scorer keeps ≤ 0.5 s queued by its own clock (start ≈ 0.25 s after an idle queue, `BUFFER_TIME_START`), so knob/mode changes act at the next token boundary.
* **API server:** JSON + 0x03 framing on the Unix socket given to klippy with `-a` (`/home/biqu/printer_data/comms/klippy.sock` on the CB1 image [VERIFY in `~/printer_data/systemd/klipper.env`]); `objects/subscribe` for button/sensor/knob states; `emergency_stop`; `gcode/firmware_restart`. Moonraker (pre-installed on the CB1 Klipper image) is used only for the Mainsail web console; the scorer does not need it.
* **IK** (`ik.py`): l_i = |A_i − (c(d) + R(axis, t(d))·q_i)| − l_i(0), with c(d) = (d, z(|d|)), the tilt axis d̂ × ẑ (leading side rises), z and t from the dish table. FK by Gauss–Newton (round trip < 1e-6 mm). Dead band: ± b_i/2 on every reversal of dl_i/dt, spread over 3 mm of path. Spring feed-forward: l_cmd −= ΔT_i / k_i with ΔT from the modelled rim reaction and drag (minimum-norm statics). Cost ≈ 7 µs per sample on a Mac, ≈ 50 µs expected on the CB1 → < 2 % CPU at 200 samples/s.
* **Geometry audit** (`TendonIK.audit`, run at every boot): predicted tensions over |d| ≤ 16.5 with and without the rim reaction must stay in 0.3–3.3 N and the positive-tension reach must be ≥ 16.5 mm. The spec geometry fails (E-C1).

### 8.3 State machine (SPEC §8.1, as built)

`BOOT → SELFTEST` (Klipper ready; rail off; K1 NC closed; geometry audit; outputs safe; watchdog PWM on; heartbeat on; M8P_OK high) `→ SAFE`. Lever held + rail up (with the NC proof seen) `→ ARMING` (dumps closed, lines vented, palm pre-charged with the PALM valve off, drums homed, tension trim, park on the rim) `→ READY`. Lever held 1 s `→ APPROACH` (PALM on, 0.6 s, rail to 0.10 N, 3 ramp strokes) `→ PLAY ⇄ REST`. Dwell timer spent `→ STATION_WAIT` (pins vented, chime) `→ MOVED → APPROACH`. `stop`/20-min cap `→ RETRACT` (vent, PALM off, centre, index window check ±0.3 mm, park) `→ READY`. Rail lost `→ PAUSED` (stream stops; resume only through ARMING). Any trip `→ FAULT` (M8P_OK low → latch, all outputs off, M84; leave only by lever release + `reset`, which re-runs SELFTEST).

Trips: reflexd silent > 0.5 s; latch tripped; K1 NC closed with rail up or open with rail off; rail up with lever/e-stop open > 150 ms (weld); PIN A line pressurised while commanded off > 0.5 s; path checker rejects 3 plans in a row; stream discontinuity; index error; Klipper shutdown/error; klippy socket lost (the scorer exits and systemd restarts it into SELFTEST).

### 8.4 Path checker (C5) — rules and tests

P1 |d| ≤ 16.5 · P2 v ≤ 200 mm/s · P3 a ≤ 2 m/s² in contact · P4 no reversal / heading change > 30° per 50 ms inside 13.7 · P5 no cusp/stop inside 13.7 · P6 landing ≥ 0.3 v_peak · P7 circle R+e ≥ 14.5, R−e ≤ 8.5, offset 15–40°/rev · P8 valve changes only on the rim · P9 force ceiling and constant support · P10 tokens start/end at rest on the rim · P11 sampling ≤ 5 ms · P12 tokens join. Every rule has at least one deliberately bad token in `tests/test_checker.py`, and every planner mode is run for 60 s × 3 seeds × 3 speeds with zero violations.

### 8.5 Snag reflex (C4) — three layers as built

| Layer | Mechanism | Threshold | Action |
|---|---|---|---|
| M | nail breakaway (PAD) / 2.0 N coupling (PAD) | 0.12–0.25 N / 2.0 N | nail drops / yoke parts → tensions collapse → E layer |
| E | LM393 windows on each Hall | < 0.2 N or > 3.6 N | latch → rail dead (≤ 35 ms) |
| F | reflexd: F_meas = −Σ T_i u_i(d) at the planned d(t); residual = F_meas − model − learned bias | > 0.8 N for 2 frames, or > 0.5 N opposing the motion for 60 ms, or tension pattern | 'X' → Pico → PICO_OK low 50 ms → latch |

The learned bias (median of the along-motion residual, clamped ±0.4 N) only learns samples within 0.25 N of zero, so a snag step is never absorbed (unit test: 0.6 N opposing trips at 60 ms; 1.2 N trips in 4 ms; 0.6 N lateral does not trip).

### 8.6 Console and logs

`python3 -m sp1v3.scratchctl` on the CB1, or from the PC with `--host <CB1 IP>` (the service binds 0.0.0.0:7700; nothing sent can energise the rail). Commands per SPEC §8.6: `status limits play rest stop retract reset | mode f amp dpsi psi R e chord dpath park | force sF groups bratio palm | vary seed dwell | cal drums|deadband|rim|lines | bset blind reveal rate | valve pump sensors tensions | inject` (inject only with `"wig_mode": true` in `~/sp1v3/config.json`). Logs: `~/sp1v3/logs/sp1-YYYYmmdd-HHMMSS.csv`, letters H (1 Hz health), B (per token), E (events), F (faults), C (settings + code), S (ratings), T (tensions, optional); every line carries the 6-hex settings code.

### 8.7 Test results (run 2026-10-02)

```
$ python3 -m pytest -q tests          (Python 3.14.0, pytest 8, macOS)
test_ik.py          24 passed   dish profile, centring, Jacobian, 3-fold + mirror symmetry, hand-calculated
                                 rise and tilt cases, FK round trip < 1e-6 mm over |d| <= 16.5, continuity,
                                 conditioning, statics, dead band, spring feed-forward, cable speed,
                                 tendon audit (spec geometry FAILS as documented; two alternatives pass)
test_checker.py     83 passed   36 good lines, 24 good circles, D-path, connectors; bad tokens for P1-P12;
                                 planner output for 5 modes x 3 seeds x 3 speeds: zero violations
test_reflex.py       6 passed
test_scorer_sim.py   5 passed   lever -> ARMING -> READY -> PLAY -> release -> PAUSED; latch trip -> FAULT
                                 -> reset; clamp; streamed G1 timing = plan within 1 %; discontinuity refused
118 passed in 7.0 s
```

To repeat on any machine: `cd firmware && python3 -m pip install pytest && python3 -m pytest -q tests`.

---

## 9. Bring-up procedure (first-timer, step by step)

**Rules for every step.** Work with the adapter unplugged unless the step says "power on". Before each first power-on, measure resistance between +24V_IN and GND with the meter on Ω: it must read > 1 kΩ (the capacitors charge, so it climbs). If any step's "good" is not what you see, stop and use the "if not" line; do not skip ahead. Keep a notebook: date, step, reading.

### 9.1 S0 — the CB1 and Klipper (≈ 2 h)

1. **Write the CB1 image.** On the Mac, download the newest "Klipper" CB1 image from github.com/bigtreetech/CB1/releases (file name like `CB1_Debian12_Klipper_kernel6.6_*.img.xz`) [VERIFY exact name on the day]. Install Raspberry Pi Imager → "Choose OS" → "Use custom" → pick the file → "Choose storage" → the microSD → Write. *Good:* "Write successful". *If not:* try balenaEtcher; try another card.
2. **Wi-Fi.** Re-insert the card in the Mac: a drive named **BOOT** appears. Open `system.cfg` in TextEdit (plain text). Remove the `#` in front of `WIFI_SSID="…"` and `WIFI_PASSWD="…"`, type your network name and password between the quotes; optionally set `hostname="sp1-box"`. Save, eject.
3. **Seat the CB1 on the M8P** (power off): the M8P manual's "M8P+CB1" photo shows the orientation; press evenly until both BTB connectors click. Fit the CB1 heatsink. Insert the microSD in the CB1's card slot (the **SOC-Card** slot on the M8P V2).
4. **Bench power, logic only.** Screw the adapter's leads (via J1/F1 or temporarily straight) to the M8P **POWER** terminal only (+ to +). Nothing on Motor Power, no drivers, no loads. Power on. *Good:* the M8P power LED lights; after ≈ 1–2 min the CB1 joins Wi-Fi (check the router's device list for `sp1-box` or `BIGTREETECH-CB1`). *If not:* re-check `system.cfg` quotes; plug an Ethernet cable into the M8P's LAN port.
5. **Log in.** Mac Terminal: `ssh biqu@sp1-box.local` (or `ssh biqu@<IP>`), password `biqu`. Then `passwd` and set your own password. *Good:* a `biqu@…$` prompt.
6. **Klipper is pre-installed** on the Klipper image: `systemctl status klipper moonraker` shows both "active". Open `http://sp1-box.local` in a browser: Mainsail appears and says the MCU is not connected yet. That is expected.

### 9.2 S0 — compile and flash the M8P firmware (≈ 45 min)

1. On the CB1: `cd ~/klipper && make menuconfig`. Set exactly (BTT's own config header): **Enable extra low-level configuration options** [*]; **Micro-controller: STMicroelectronics STM32**; **Processor model: STM32H723**; **Bootloader offset: 128KiB bootloader**; **Clock Reference: 25 MHz crystal**; **Communication interface: USB (on PA11/PA12)**. Press Q, then Y to save.
2. `make clean && make`. *Good:* ends with `Creating hex file out/klipper.bin`.
3. **Flash, method A (SD card):** copy `out/klipper.bin` to the Mac (`scp biqu@sp1-box.local:klipper/out/klipper.bin .`), rename it **`firmware.bin`**, put it alone on a FAT32 microSD, insert it in the M8P's **MCU-Card** slot, power-cycle, wait 30 s. *Good:* the file on the card is now named `FIRMWARE.CUR`. **Method B (DFU):** hold the M8P **BOOT** button, press and release **RESET**, release BOOT; on the CB1 `lsusb` shows `0483:df11`; run `make flash FLASH_DEVICE=0483:df11`. *Good:* "File downloaded successfully". *If neither works:* BTT's bootloader may be missing — flash `M8P_V2_H723_bootloader.bin` with `sudo dfu-util -d ,0483:df11 -R -a 0 -s 0x8000000:leave -D M8P_V2_H723_bootloader.bin` (BTT Firmware README), then method A.
4. `ls /dev/serial/by-id/` → a line `usb-Klipper_stm32h723xx_…-if00`. Copy it.

### 9.3 S0 — install the SP1 files

1. From the Mac: `scp -r 14-build/electronics/firmware biqu@sp1-box.local:~/sp1v3-src`.
2. On the CB1: `cp ~/sp1v3-src/printer.cfg ~/printer_data/config/printer.cfg`, then `nano ~/printer_data/config/printer.cfg` and paste the serial line from 9.2-4 into `[mcu] serial:`. Ctrl-O, Enter, Ctrl-X.
3. Check the API socket path: `cat ~/printer_data/systemd/klipper.env` — the `-a` argument should be `/home/biqu/printer_data/comms/klippy.sock`. If it differs, use that path in `systemd/sp1-scorer.service`.
4. In Mainsail, press **FIRMWARE RESTART**. *Good:* state "Ready"; the console lists no errors. *If "Option … is not valid":* your Klipper is older than the GCODE_AXIS feature — run `cd ~/klipper && git pull && sudo systemctl restart klipper` and re-flash (9.2). *If an ADC "out of range" shutdown:* a sensor input is open — that is normal before the sensors are wired; temporarily comment out the sensor/heater sections until A1.
5. Unit tests on the CB1 (optional, proves the Python): `cd ~/sp1v3-src && python3 -m pip install --user pytest && python3 -m pytest -q tests` → `118 passed`.

### 9.4 S0 — V-K1 streaming test (no safety board yet; bench only, no pad)

At S0 the drivers get their motor power straight from the adapter **through the e-stop puck** (pole 2) — never a bare wire — because the safety board comes in Cart A.

1. Power off. Fit three TMC2209s in Motor1–3 (match the driver's EN/GND/VM pin labels to the socket silkscreen — a driver inserted backwards is destroyed at power-on; BTT's manual photo shows the orientation), MS1+MS2 jumpers, **no UART jumper**, driver-supply jumpers on **HV**. Connect steppers to Motor1–3. Wire adapter + → e-stop pole 2 → Motor Power +; adapter − → Motor Power −.
2. **Set VREF before connecting motors** (§9.6 step 3), then connect them.
3. Wire a 5 mm LED + 2.2 k resistor from the HE0 "+" pin (VBB, only allowed here as a test source) to the HE0 drain pin: the LED lights when `pin_a` = 1. (Remove this LED before any 12 V load is wired, E-C12.)
4. Power on, e-stop released. In Mainsail console: `SP1_HOME_DRUMS` will fail without index Halls — instead register the axes by hand: `MANUAL_STEPPER STEPPER=cable_a ENABLE=1`, same for b and c, then `MANUAL_STEPPER STEPPER=cable_a GCODE_AXIS=A LIMIT_VELOCITY=250 LIMIT_ACCEL=100000000` (and B, C). `G1 A5 F300` → drum A turns ≈ 48° and stops. *If it buzzes but does not turn:* a coil pair is swapped — swap the two middle wires of that motor plug.
5. On the CB1: `cd ~/sp1v3-src && python3 -m sp1v3.benchtest stream --strokes 500`. Film the drum (a paper flag on the shaft) and the LED at 240 fps for a few seconds.
6. *Pass (V-K1, V-K2):* prints `stalls 0` and `PASS`; planned and wall times agree (wall = planned + ≈ 0.8 s of start/stop); the LED edge coincides with the flag's turnaround within ±1 frame (± 4 ms) over the filmed strokes; no stutter audible. *If stalls > 0:* the CB1 is too slow or busy — close Mainsail tabs, check `top`; if it persists, record and use fallback 1 (SPEC §8.2).

### 9.5 Cart A — build the safety board (≈ 6–8 h)

Build on a 7 × 9 cm perfboard following §2 and the wiring table, in this order, testing as you go:

1. **Power section:** TB1 (+24V_IN, GND), SMAJ26A (band to +), 470 µF (stripe to GND), TB3 (ACT-24) with its SMAJ26A + 470 µF, 4.7 Ω 5 W bleeder footprint. *Check:* Ω between +24V_IN and GND climbs > 1 kΩ.
2. **K1:** solder the SFS2-DC24V (pins only fit one way). Coil clamp: 1N4007 + 1N4746A in series across A1/A2 (1N4007 band toward A1, Zener band toward A2 — together they conduct only in the reverse direction above ≈ 19 V). Contacts: NO-a/NO-b in series; NC-a to the bleeder; NC-b to a 2-pin header for PF0.
3. **Q_LATCH, Q_WD:** two 2N7000 in series in the coil's low side (flat face toward you: S-G-D left to right — check the datasheet print), 100 k gate-to-source on each.
4. **Optos O1–O5:** PC817 in DIP sockets; dot = pin 1 = LED anode.
5. **Latch:** 74HC74 in a socket; pin 14 = 5 V, pin 7 = GND, 100 nF across them; tie the unused half's /PRE, /CLR, D, CLK (pins 10, 13, 12, 11) to 5 V; first half's D (2) and CLK (3) to GND.
6. **Comparators:** 4 × LM393 in sockets, 100 nF each; 8 trimpots for the six window thresholds + one 1.0 V reference (10 k/3.3 k divider from 3.3 V is fine).
7. **Charge pump** as §2 (C1 1 µF film, D1/D2 1N4148, C2 1 µF, 18 k, 1 k to Q_WD gate).

### 9.6 A0 — first power with the safety board, then the dead-rail test (≈ 3 h)

1. **No loads yet.** Wire J1–J4, the safety board, the M8P POWER and Motor Power, and a **12 V test lamp** (or 1 k + LED) on the ACT-12 bus instead of valves.
2. **Buck setting:** before connecting it to ACT-24, feed the buck from a 24 V source (hold the lever with the loop jumpered, or a separate test), and turn its trimmer until the output reads **12.0 V** with no load.
3. **VREF:** lever held (rail up), meter between each driver's trimmer wiper and GND; turn with the ceramic screwdriver to **0.35 V**. *If you cannot reach it:* the driver is not powered — check the HV jumper.
4. **Loop tests (gate A0):** with the logic analyser on PD12 (lever), PD14 (e-stop), PC11 (loop), PF1 (rail), PD13 (latch), PF0 (K1 NC) and ACT-12 through a 47 k/10 k divider, do each 10 times: release lever; press e-stop; pull the lanyard; open the head switch; `SET_PIN PIN=m8p_ok VALUE=0`; unplug the Pico; short one Hall output to GND (slack) with a 1 k; `SET_PIN PIN=watchdog VALUE=0`. *Good:* PF1 shows the rail gone (< 4 V) within **35 ms** of the trigger edge every time; the M8P and CB1 stay up; after each latch trip the rail returns only after the lever is released and pressed again. *If not:* the element that did not open the rail is miswired — fix before anything else.
5. **Weld check:** power off, bridge K1 NO-a with a clip lead, power on: `status` must say FAULT "K1 NC open with the rail off" or refuse to arm. Remove the bridge.
6. **Host watchdog:** with the scorer running (§9.7), `sudo systemctl kill -s STOP sp1-scorer` (freezes it). *Good:* rail gone within ≈ 1.3 s; Mainsail shows "Shutdown". `sudo systemctl kill -s CONT sp1-scorer`, then `FIRMWARE_RESTART` and `reset`.
7. **Dead-rail output test (hard gate, E-C12):** lever **released**. In the console: `SET_PIN PIN=pin_a VALUE=1`, same for `pin_b`, `palm`, `rail_dump`, `palm_dump`, `SET_HEATER_TEMPERATURE HEATER=rail TARGET=10`, same for palm. Meter every load's + and − terminals to GND: **all must read 0 V**; no click. Then `SP1_ALL_OFF`. *If any load reads 12 or 24 V:* it is wired to a "+" pin or a VFAN jumper is on 5 V — fix before connecting real valves.

### 9.7 Install the services and the Pico (≈ 1 h)

1. **Pico:** hold BOOTSEL, plug the Pico into the Mac → drive RPI-RP2 → drag the MicroPython UF2 for "Raspberry Pi Pico" (micropython.org/download/RPI_PICO) onto it. Install Thonny, open `firmware/pico/main.py`, File → Save as → Raspberry Pi Pico → `main.py`. Unplug, plug it into the M8P's USB port. On the CB1 `ls /dev/serial/by-id/` → `usb-MicroPython_Board_in_FS_mode_…-if00`; paste into `systemd/sp1-reflexd.service`.
2. `sudo cp ~/sp1v3-src/systemd/*.service /etc/systemd/system/ && sudo systemctl daemon-reload && sudo systemctl enable --now sp1-reflexd sp1-scorer`.
3. `python3 -m sp1v3.scratchctl status` → `state SAFE`, `reflexd ok`. The Pico's LED is on. *If FAULT "tendon geometry audit failed":* expected until E-C1 is settled; for bench work with the spec geometry set `"geometry_audit": "warn"` in `~/sp1v3/config.json` (never for a head session).

### 9.8 A1 — pressure sensors and pumps

1. Connect the four sensors (3.3 V versions!) and a reference digital manometer on a tee. `sensors` in the console prints kPa. At 0 and ≈ 10 and ≈ 20 kPa the reading must match the manometer within ±0.3 kPa; if not, edit the `[adc_temperature xgzp_40k_33]` points (voltage = what the sensor outputs at that pressure) and FIRMWARE_RESTART.
2. Pump PID: `pump 1 8` (rail to 8 kPa). Watch the rail graph in Mainsail: *good* = settles within ±0.5 kPa in < 3 s with no sustained oscillation. If it oscillates, halve `pid_Kp`; if it is sluggish, raise `pid_Ki`. Record final gains.

### 9.9 A3 — drums, index, tensions, comparators

1. **Direction:** pad retracted, `G1 A2 F300` must pay cable A out (block moves away from stop A). If not, add or remove `!` on that stepper's `dir_pin`.
2. **Index:** `QUERY_ENDSTOPS` with each drum's magnet facing its Hall → `manual_stepper cable_a: TRIGGERED`. Adjust the Hall gap (1–2 mm) until it triggers reliably and not 1 mm away. Run `cal drums` → "index check PASS".
3. **Tension calibration:** drums held (rail up, block centred), hang 0, 100, 200, 300 g at the pad end of each cable; note `tensions` raw counts (temporarily set `tension_cal` to `[[0, 1], …]`); fit zero and N/count (0.981 N per 100 g); write `tension_cal` in `~/sp1v3/config.json`; restart reflexd. *If a tension falls when you add weight:* flip that Hall's magnet.
4. **Comparator thresholds:** compute each channel's voltage at 0.2 N and 3.6 N (V = 3.3 × counts/65535) and set the trimpots with the meter on the LM393 reference pins. Check: lifting a cable's weight off (slack) trips the latch; 400 g hung trips it.
5. **Trim and dead band:** barrel adjusters to the chosen pretension ± 0.1 N (E-C1: 2.0 N in the passing geometry); dead band per cable by the ink-rosette method (SPEC §8.2) → `deadband_mm`.

### 9.10 A4 — reflex on the wig tether

`inject snag` then pull the tether: the latch must trip with the strand tension ≤ the C4 limit, trip ≤ 50 ms after onset (240 fps). Then 20 min each of PLINE, D-paths, CIRCLE without the tether: **zero false trips** (`grep ',F,' ~/sp1v3/logs/*.csv`). If false trips appear, raise `opp_n` in 0.1 N steps, never above 0.8 N, and log the change.

### 9.11 Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Rail never comes up when the lever is held | e-stop latched; loop open; latch tripped (Pico not running, scorer not in SAFE) | `status` shows which sense input is off; twist the e-stop; check the lanyard; start reflexd |
| Rail drops every few seconds | watchdog pump marginal; heartbeat late | scope the Q_WD gate (should be ≥ 8 V steady); check CB1 load |
| Klipper "MCU 'mcu' shutdown: Missed scheduling of next pin event" | host overloaded | fewer browser tabs; keep the queue at 0.5 s |
| `Timer too close` | same | same |
| Drum stutters every segment | `accel` not 0 or LIMIT_ACCEL missing | check `printer.cfg` and the homing macro |
| Valve stays on with the rail off | load wired to "+" pin, or VFAN on 5 V | §9.6 step 7 |
| Pressure reads 48 kPa and Klipper shuts down | sensor unplugged | reconnect; this shutdown is intended |

---

## 10. Pad-2 provisions (SPEC §9) in this package

FAN4 (PA4) = PALM B valve; HB (PF5) = PALM B dump with BED IN fed from ACT-12 at install; S_palm B on an ADS1115 at the Pico's GP4/GP5; J4 pins 3–4 spare for a second head switch; `twin` stub not yet in the scorer (planned with the pad-2 install, ≈ 2 h).

---

## 11. Sources (checked 2026-10-02)

* Klipper G-Codes (`MANUAL_STEPPER … GCODE_AXIS`, `SET_PIN`, `SET_KINEMATIC_POSITION`): https://www.klipper3d.org/G-Codes.html — raw: https://github.com/Klipper3d/klipper/blob/master/docs/G-Codes.md
* Klipper Config Reference (`[manual_stepper]`, `[pwm_tool]` incl. `maximum_mcu_duration`, `[output_pin]`, `[gcode_button]` analog_range, `[heater_generic]`, `[adc_temperature]`, `[verify_heater]`, None kinematics, `[delayed_gcode]`, `[idle_timeout]`): https://www.klipper3d.org/Config_Reference.html
* Klipper API Server (socket framing, `gcode/script`, `objects/subscribe`, `emergency_stop`, `gcode/firmware_restart`): https://www.klipper3d.org/API_Server.html
* Klipper source, master: `klippy/toolhead.py` (Move, BUFFER_TIME_HIGH 1.0), `klippy/extras/manual_stepper.py`, `klippy/extras/output_pin.py`, `klippy/extras/pwm_tool.py`, `klippy/mcu.py` (MIN_SCHEDULE_TIME 0.100, MAX_NOMINAL_DURATION 3.0), `klippy/extras/buttons.py`, `src/stm32/hard_pwm.c` (PF6 = TIM16), `src/stm32/watchdog.c` (IWDG ≈ 410–512 ms): https://github.com/Klipper3d/klipper
* BTT Manta M8P V2.0: user manual, pin-out PNG, schematic PDF, `generic-bigtreetech-manta-m8p-V2_0.cfg`, bootloader README: https://github.com/bigtreetech/Manta-M8P/tree/master/V2.0 ; wiki https://global.bttwiki.com/M8P-V2_0.html
* BTT CB1: https://global.bttwiki.com/CB1.html ; readme (images, `system.cfg`, overlays incl. `i2c0`): https://github.com/bigtreetech/CB1 ; CB1 user manual (GPIO numbering) in the same repo; independent I²C notes: https://www.learningtopi.com/sbc/cb1/bigtreetech-cb1/
* BTT TMC2209 VREF (I_RMS = VREF/√2 for 0.11 Ω sense): https://global.bttwiki.com/TMC2209.html
* Panasonic SF/SFS safety relay datasheet (2 Form A 2 Form B, release time max 20 ms, 360 mW): https://datasheet.octopart.com/SFS2-DC12V-Panasonic-datasheet-145014476.pdf
* CFSensor XGZP6847A datasheet (3.3 V option 0.2–2.7 V): https://cfsensor.com/wp-content/uploads/2022/11/XGZP6847A-Pressure-Sensor-V2.7.pdf
* Prices: see parts.md (each line linked).
