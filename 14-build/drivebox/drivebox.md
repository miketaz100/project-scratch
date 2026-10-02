# SP1 v3 DRIVE BOX: build package

**Project SCRATCH · 14-build/drivebox · DRIVE BOX work package · 2026-10-02 · rev 1**

**Scope (SYSTEM-SPEC-v3 §11):**
- drum module: drums, index, stop plate, flexures, tensioner;
- pneumatics: pumps, accumulators, reliefs, PIN valves, dumps, filters, mufflers, manifolds;
- Apache 2800 case fit-out;
- desk, chair-back and couch-back mounts;
- the umbilical, the box-end latched block and the hanger.

**Owns interfaces:** M16, M17, lines A/B/P, and T1–T4 (§5).

**Binding inputs:**
- DECISION-3;
- SYSTEM-SPEC-v3 (§2.3–2.4, §4.3–4.4, §4.9–4.10, §5.2–5.3, §6, §7.1–7.2);
- safety ruling C1–C8 (C3 is the one that touches this box);
- the safety-requirements red lines;
- leap4-D L1 (tendon puppet) and leap4-E E2;
- redteam-3 §2.

**Companion files**
- parts.md: every part, with live prices.
- CONFLICTS.md: 21 items where the hardware or the market disagrees with the spec.
- cad/: OpenSCAD sources, STLs and the generator; see cad/README.md.

**Tags:** [KNOWN] = a project file or a vendor page cited in parts.md. [EST] = my arithmetic. [VERIFY] = check on the part in hand before you rely on it.

---

## 0. The box in one page

| | Value |
|---|---|
| Case | Harbor Freight **Apache 2800** (SKU 64551, $29.99). Inside 302 × 229 × 135 mm; base ≈ 95 deep, lid ≈ 30 [est] |
| **Loaded mass** | **≈ 3.8 kg (3.6–4.0) [EST], against the 2.8 kg spec.** See §9 and CONFLICTS C1. |
| Layout | The M8P stands on the left end wall. The drum module sits in the middle-right, with the electronics shelf over it. The 250 ml accumulator lies beside the M8P. Both pumps are along the front. The valve rack and the 30 ml accumulator are along the rear. The umbilical block and two vents are on the right end wall. User connectors are at the left rear corner. |
| Drum module | Three 17HS08-1004S pancake steppers, shafts vertical, under a printed deck. Ø 12 SLA drums with two helical grooves each. A floating housing-stop plate on two Ø 4 rods, LM4UU bearings and two springs (ΣT 4.5 N at the W tick). Six flexure seats (three used, three for pad 2); a linear Hall per used seat; a Hall index per drum. The module sits on six rubber isolators. |
| Pneumatics | P1 and P3 are BODENFLO BD-02A-1L, each with a 10 µm filter, followed by: <br>• **rail:** 250 ml PET accumulator → R1a McMaster 4277T51 and R1b Generant VRV 3.5 psi → RAIL DUMP (NO) and S_rail → S070 PIN A; and, through a 25G needle, S070 PIN B → S_A and S_B → lines A and B. <br>• **palm:** 30 ml accumulator → R2 4277T51 and R2b VRV → PALM DUMP (NO), 27G palm bleed → uxcell 3-way PALM → S_palm → line P. <br>• **pad-2 provisions:** capped tees on A and B; capped PALM B port. |
| Umbilical | 3 × SMC TIUB01 PU 1/8 in, 3 tendons in housings, 1 × 4-core 26 AWG, inside 1 in stockinette. Housings are 1.60 m seat to seat. The box end is the SLA plug DB07: O-ring face seals, two M4 thumb screws, a housing slot. A 3 N magnetic clip sits on a gooseneck hanger. |
| Power | Unchanged from §4.10: ≈ 26 W typical, 42 W peak. All heat comes out through two 25 mm baffled vents. |
| Noise target | ≤ 30 dBA at 1 m. Pass line: within 3 dB of the room (CONFLICTS C20). See §8. |
| Parts | ≈ $900–950 for this work package (parts.md). That is ≈ $300 over the spec's §13 share, mostly diverse reliefs, SMC fittings and the real housing price. |
| Hands-on hours | ≈ 34–51 h, including the 1.5× first-timer factor [EST]: S0 rig 6–8, drum module 6–10, pneumatics 8–12, case 6–9, umbilical and hanger 4–6, calibrations 4–6. |

**What a first-timer needs to know first**
1. The box is three sub-assemblies on one plywood **tray**: the drum module, the pneumatics and the electronics. You build and test all of it on the kitchen table, then drop the tray into the case. Nothing is built inside the case.
2. Each sub-assembly has a pass/fail test. Do not move on until it passes:
   - the reliefs and deadheads (§4);
   - the flexure calibration (§6.3);
   - the pre-tension (§6.4);
   - the portability test (§10).
3. Four parts come from a print service, in SLA resin: the three drums and the umbilical block pair. Everything else is PETG on a home printer, or MJF PA12 from the same service if there is no printer (cad/README.md).

---

## 1. Frames and datums

| Frame | Origin | Axes | Used for |
|---|---|---|---|
| **K** (case) | Inside floor of the base, left-front corner | X along the case length (0 = left inner wall, 302 = right). Y from the front, where the latches and handle are (0), to the rear hinge wall (229). Z up from the inside floor. | Layout, holes in the case |
| **D** (drum module) | Deck top surface, deck corner | x toward the umbilical wall (= +X), y = +Y, z up. **D origin = K (105, 40, 44).** | DB02–DB05 |
| **b** (bulkhead) | Right end wall, **outside** surface, at the window centre | u = outward normal (= +X), v = +Y, w = +Z. **b origin = K (302 + wall, 115, 68).** | DB06–DB08 |

**Interface datums**
- **M17 module base plate:** the deck top (D z = 0). Drums sit 1.0 mm above it. Cable rows are at D z 14 (pad 1) and z 22 (pad 2), i.e. K Z 58 and 66.
- **M16 box mounting:** the hook plate on the lid's outside face, bolt pattern 200 × 120. The four sorbothane feet are on the base's outside floor.

---

## 2. Layout of the case interior

### 2.1 Plan view (lid open, looking down; front (latches) at the bottom; 1 px = 0.5 mm)

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 560" width="760" height="560" font-family="Helvetica, Arial, sans-serif" font-size="10">
  <defs>
    <pattern id="hatch" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="6" stroke="#bbb" stroke-width="1"/></pattern>
    <marker id="ar" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#333"/></marker>
  </defs>
  <rect width="760" height="560" fill="#fff"/>
  <text x="40" y="22" font-size="13" font-weight="bold">DRIVE BOX: Apache 2800 interior, plan (frame K, mm). Inside 302 × 229. Front (latches, handle) at the bottom.</text>
  <!-- case inner wall -->
  <rect x="40" y="40" width="604" height="458" fill="#f6f6f6" stroke="#222" stroke-width="2"/>
  <!-- tray -->
  <rect x="60" y="46" width="578" height="446" fill="#fbf5e6" stroke="#b08a3c" stroke-dasharray="6,3"/>
  <text x="62" y="488" fill="#8a6a20">tray: 6 mm Baltic birch X 10–299, Y 3–226 (lifts out as one unit)</text>
  <!-- left panel + M8P -->
  <rect x="46" y="46" width="12" height="446" fill="url(#hatch)" stroke="#8a6a20"/>
  <rect x="78" y="98" width="58" height="340" fill="#e7f3e7" stroke="#2a8a2a" stroke-width="1.5"/>
  <text x="84" y="250" fill="#2a6a2a" font-weight="bold" transform="rotate(-90 84 250)">BTT M8P V2.0 + CB1 (vertical, 170 × 102.7)</text>
  <text x="100" y="250" fill="#2a6a2a" transform="rotate(-90 100 250)">X 19–48, Y 30–200, Z 2–105 (≈ 10 above rim)</text>
  <text x="116" y="250" fill="#2a6a2a" transform="rotate(-90 116 250)">on 6 mm ply panel at X 3–9, 2 × DB18</text>
  <!-- user connectors left wall -->
  <circle cx="40" cy="54" r="5" fill="#2a8a2a"/><text x="48" y="57" font-size="9">DC 24 V jack (Z 20)</text>
  <circle cx="40" cy="70" r="5" fill="#2a8a2a"/><text x="48" y="73" font-size="9">GX12-8 hand ctl (Z 45)</text>
  <circle cx="40" cy="86" r="5" fill="#2a8a2a"/><text x="48" y="89" font-size="9">GX12-4 e-stop (Z 70)</text>
  <circle cx="40" cy="468" r="4" fill="#2a8a2a"/><text x="46" y="482" font-size="9">status LED (Y 15, Z 75)</text>
  <!-- bottle 250 ml -->
  <rect x="144" y="58" width="100" height="350" rx="22" fill="#e8f0fb" stroke="#1f5fbf" stroke-width="1.5"/>
  <rect x="152" y="306" width="84" height="8" fill="none" stroke="#1f5fbf" stroke-dasharray="2,2"/>
  <rect x="152" y="208" width="84" height="8" fill="none" stroke="#1f5fbf" stroke-dasharray="2,2"/>
  <text x="160" y="190" fill="#1f5fbf" font-weight="bold">250 ml ACC</text>
  <text x="160" y="204" fill="#1f5fbf">PET Ø50 × 175</text>
  <text x="160" y="232" fill="#1f5fbf">X 52–102</text>
  <text x="160" y="246" fill="#1f5fbf">Y 45–220</text>
  <text x="160" y="260" fill="#1f5fbf">2 × DB14 saddle</text>
  <text x="160" y="420" fill="#1f5fbf">cap + PM-4 port (front)</text>
  <!-- drum deck -->
  <rect x="250" y="138" width="300" height="280" fill="#fff4ea" stroke="#c06000" stroke-width="1.5"/>
  <text x="256" y="152" fill="#c06000" font-weight="bold">DRUM MODULE: deck DB02, D origin K(105, 40), deck top Z 44</text>
  <!-- legs -->
  <g fill="#ddd" stroke="#888"><rect x="250" y="394" width="20" height="24"/><rect x="250" y="138" width="20" height="24"/><rect x="410" y="394" width="24" height="24"/><rect x="410" y="138" width="24" height="24"/><rect x="526" y="394" width="24" height="24"/><rect x="526" y="138" width="24" height="24"/></g>
  <!-- motors -->
  <g fill="none" stroke="#777" stroke-dasharray="3,2"><rect x="276" y="330" width="84" height="84"/><rect x="276" y="238" width="84" height="84"/><rect x="276" y="146" width="84" height="84"/></g>
  <g fill="#ffe2c4" stroke="#c06000"><circle cx="318" cy="372" r="30"/><circle cx="318" cy="280" r="30"/><circle cx="318" cy="188" r="30"/></g>
  <g fill="#c06000"><circle cx="318" cy="372" r="12"/><circle cx="318" cy="280" r="12"/><circle cx="318" cy="188" r="12"/></g>
  <text x="290" y="404" font-size="9">17HS08 + DB01 drum A (Y 63)</text>
  <text x="290" y="312" font-size="9">drum B (Y 109)</text>
  <text x="290" y="220" font-size="9">drum C (Y 155)</text>
  <g fill="#2a8a2a"><rect x="290" y="368" width="6" height="8"/><rect x="290" y="276" width="6" height="8"/><rect x="290" y="184" width="6" height="8"/></g>
  <text x="256" y="434" font-size="9" fill="#2a6a2a">green: DRV5023 index Hall (R 12)</text>
  <!-- cables drum to FP -->
  <g stroke="#c06000" stroke-width="1.5"><line x1="318" y1="360" x2="478" y2="360"/><line x1="318" y1="268" x2="478" y2="268"/><line x1="318" y1="176" x2="478" y2="176"/></g>
  <!-- rods and posts -->
  <g stroke="#555" stroke-width="2"><line x1="345" y1="408" x2="545" y2="408"/><line x1="345" y1="148" x2="545" y2="148"/></g>
  <g fill="#bbb" stroke="#555"><rect x="365" y="398" width="16" height="20"/><rect x="365" y="138" width="16" height="20"/><rect x="529" y="398" width="16" height="20"/><rect x="529" y="138" width="16" height="20"/></g>
  <g stroke="#2a2a2a" fill="none" stroke-width="1"><polyline points="381,408 386,402 392,414 398,402 404,414 410,402 416,414 422,402 428,414 434,402 440,414 446,408 450,408"/><polyline points="381,148 386,142 392,154 398,142 404,154 410,142 416,154 422,142 428,154 434,142 440,154 446,148 450,148"/></g>
  <text x="372" y="432" font-size="9">springs uxcell 5.5 × 42 on Ø4 rods, LM4UU in the plate</text>
  <!-- bridge and FP -->
  <rect x="438" y="164" width="10" height="228" fill="#e7f3e7" stroke="#2a8a2a"/>
  <rect x="450" y="138" width="16" height="280" fill="#ffd9b3" stroke="#c06000" stroke-width="1.5"/>
  <g fill="#c06000"><rect x="466" y="354" width="12" height="12"/><rect x="466" y="262" width="12" height="12"/><rect x="466" y="170" width="12" height="12"/></g>
  <text x="414" y="132" font-size="9" fill="#c06000">DB03 floating stop plate (X 205–219) + DB04 Hall bridge</text>
  <line x1="450" y1="424" x2="450" y2="440" stroke="#c06000"/><text x="426" y="452" font-size="9" fill="#c06000">W tick: plate rear face at X 205 ±1</text>
  <!-- comb -->
  <rect x="520" y="200" width="20" height="220" fill="none" stroke="#c06000" stroke-dasharray="3,2"/>
  <text x="500" y="196" font-size="9" fill="#c06000">DB05 comb</text>
  <!-- housings to bulkhead -->
  <g stroke="#a04800" stroke-width="2.5" fill="none"><path d="M478,360 C540,360 560,308 610,308"/><path d="M478,268 C540,268 560,268 610,268"/><path d="M478,176 C540,176 560,228 610,228"/></g>
  <text x="556" y="340" font-size="9" fill="#a04800">housings (free, R ≥ 47)</text>
  <!-- e-shelf -->
  <rect x="350" y="158" width="200" height="240" fill="none" stroke="#2a8a2a" stroke-width="1.5" stroke-dasharray="8,4"/>
  <text x="356" y="176" font-size="9" fill="#2a6a2a">E-SHELF at Z 78 (100 × 120, 4 × M3 × 35 standoffs on the deck):</text>
  <text x="356" y="188" font-size="9" fill="#2a6a2a">12 V buck, K1 relay, latch/comparator board, ADS1115 (ELECTRONICS)</text>
  <!-- bulkhead and plug -->
  <rect x="610" y="196" width="34" height="144" fill="#dfe8f7" stroke="#1f5fbf" stroke-width="1.5"/>
  <rect x="644" y="144" width="28" height="248" fill="#c9d8f2" stroke="#1f5fbf" stroke-width="1.5"/>
  <rect x="672" y="144" width="32" height="248" fill="#b6caee" stroke="#1f5fbf" stroke-width="1.5"/>
  <text x="612" y="190" font-size="9" fill="#1f5fbf">DB06 neck</text>
  <text x="646" y="138" font-size="9" fill="#1f5fbf">DB06 head | DB07 plug</text>
  <g fill="#1f5fbf"><circle cx="626" cy="300" r="4"/><circle cx="626" cy="268" r="4"/><circle cx="626" cy="236" r="4"/></g>
  <text x="560" y="250" font-size="9" fill="#1f5fbf">A · B · P</text>
  <line x1="704" y1="268" x2="752" y2="268" stroke="#333" stroke-width="3" marker-end="url(#ar)"/>
  <text x="706" y="258" font-size="9">umbilical</text>
  <text x="648" y="410" font-size="9">GX12-4 loop socket below the</text>
  <text x="648" y="421" font-size="9">block (Y 115, Z 25)</text>
  <!-- vents -->
  <rect x="608" y="388" width="36" height="100" fill="#eee" stroke="#666"/><text x="566" y="500" font-size="9">vent baffle DB17 (Y 30)</text>
  <rect x="608" y="48" width="36" height="100" fill="#eee" stroke="#666"/><text x="560" y="62" font-size="9">vent DB17 (Y 200)</text>
  <!-- pumps front strip -->
  <rect x="264" y="430" width="130" height="56" rx="8" fill="#e8f0fb" stroke="#1f5fbf"/>
  <rect x="404" y="430" width="130" height="56" rx="8" fill="#e8f0fb" stroke="#1f5fbf"/>
  <text x="272" y="462" fill="#1f5fbf" font-weight="bold">P1 BD-02A-1L (rail)</text>
  <text x="412" y="462" fill="#1f5fbf" font-weight="bold">P3 BD-02A-1L (palm)</text>
  <text x="272" y="476" font-size="9" fill="#1f5fbf">2 × DB13 on sorbothane</text>
  <rect x="540" y="438" width="64" height="44" fill="#e8f0fb" stroke="#1f5fbf"/>
  <text x="543" y="456" font-size="9" fill="#1f5fbf">2 × ZFC050</text>
  <text x="543" y="468" font-size="9" fill="#1f5fbf">filters, tees</text>
  <!-- rear band -->
  <rect x="260" y="54" width="130" height="60" rx="14" fill="#e8f0fb" stroke="#1f5fbf"/>
  <text x="268" y="88" fill="#1f5fbf">30 ml ACC (2 × DB13)</text>
  <rect x="400" y="118" width="200" height="8" fill="#777"/>
  <rect x="400" y="54" width="200" height="64" fill="#f0f6ff" stroke="#1f5fbf" stroke-dasharray="4,2"/>
  <text x="404" y="68" font-size="9" fill="#1f5fbf" font-weight="bold">VALVE RACK DB12 (pegboard 100 × 90, vertical)</text>
  <text x="404" y="80" font-size="9" fill="#1f5fbf">S070 PIN A, PIN B · uxcell PALM 3-way · 2 NO dumps</text>
  <text x="404" y="92" font-size="9" fill="#1f5fbf">4 × XGZP6847A · R1a R1b R2 R2b · 3 × PK-4</text>
  <text x="404" y="104" font-size="9" fill="#1f5fbf">25G B-needle · 27G palm bleed · capped tees</text>
  <!-- dims -->
  <text x="40" y="520" font-size="10">X →  0 ······ 50 ······ 100 ······ 150 ······ 200 ······ 250 ······ 302</text>
  <text x="40" y="536" font-size="10">Keep clear: lid foam over the M8P and the E-shelf; 10 mm between the deck and the M8P drivers (Y ≥ 180).</text>
</svg>

### 2.2 Section looking from the front (heights, Z up; base rim 95, lid 30 [est])

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 330" width="760" height="330" font-family="Helvetica, Arial, sans-serif" font-size="10">
  <rect width="760" height="330" fill="#fff"/>
  <text x="40" y="20" font-size="13" font-weight="bold">Front section (frame K): X horizontal (2 px/mm), Z vertical (2 px/mm); floor at y = 300</text>
  <!-- case outline: base 0-95, lid 95-125 -->
  <rect x="40" y="50" width="604" height="250" fill="#f6f6f6" stroke="#222" stroke-width="2"/>
  <line x1="40" y1="110" x2="644" y2="110" stroke="#222" stroke-width="2" stroke-dasharray="10,4"/>
  <text x="648" y="114">base rim Z 95</text><text x="648" y="54">lid top Z 125</text>
  <!-- tray -->
  <rect x="60" y="288" width="578" height="12" fill="#e9d7a9" stroke="#8a6a20"/><text x="64" y="285" font-size="9">tray Z 0–6</text>
  <!-- left panel + M8P -->
  <rect x="46" y="90" width="12" height="210" fill="#e9d7a9" stroke="#8a6a20"/>
  <rect x="78" y="90" width="58" height="206" fill="#e7f3e7" stroke="#2a8a2a"/>
  <text x="82" y="200" fill="#2a6a2a" transform="rotate(-90 82 200)">M8P Z 2–105 (pokes 10 into the lid)</text>
  <!-- bottle -->
  <rect x="144" y="188" width="100" height="100" rx="40" fill="#e8f0fb" stroke="#1f5fbf"/><text x="160" y="240" fill="#1f5fbf">250 ml Z 6–56</text>
  <!-- isolators + legs + deck -->
  <g fill="#555"><rect x="252" y="268" width="16" height="20"/><rect x="414" y="268" width="16" height="20"/><rect x="530" y="268" width="16" height="20"/></g>
  <text x="252" y="282" font-size="8" fill="#fff">iso</text>
  <g fill="#ddd" stroke="#888"><rect x="250" y="220" width="20" height="48"/><rect x="410" y="220" width="24" height="48"/><rect x="526" y="220" width="24" height="48"/></g>
  <rect x="250" y="212" width="300" height="8" fill="#ffd9b3" stroke="#c06000"/>
  <text x="560" y="218" font-size="9" fill="#c06000">deck top Z 44 (D z 0)</text>
  <rect x="276" y="220" width="84" height="43" fill="none" stroke="#777" stroke-dasharray="3,2"/><text x="282" y="246" font-size="9">17HS08 Z 18.5–40</text>
  <rect x="288" y="161" width="60" height="51" fill="#ffe2c4" stroke="#c06000"/><text x="292" y="186" font-size="9">drum Z 45–70.5</text>
  <line x1="348" y1="184" x2="478" y2="184" stroke="#c06000" stroke-width="1.5"/><text x="380" y="180" font-size="9" fill="#c06000">cable row 1 Z 58</text>
  <line x1="348" y1="168" x2="478" y2="168" stroke="#c06000" stroke-width="1" stroke-dasharray="4,2"/><text x="380" y="164" font-size="9" fill="#c06000">row 2 Z 66 (pad 2)</text>
  <rect x="450" y="152" width="16" height="56" fill="#ffd9b3" stroke="#c06000"/><text x="430" y="146" font-size="9" fill="#c06000">plate Z 46–74</text>
  <!-- shelf -->
  <rect x="350" y="138" width="200" height="6" fill="#e7f3e7" stroke="#2a8a2a"/><text x="352" y="132" font-size="9" fill="#2a6a2a">E-shelf Z 78–81; parts ≤ Z 95 (+ lid)</text>
  <!-- pumps (front, behind section) -->
  <rect x="264" y="232" width="130" height="56" fill="none" stroke="#1f5fbf" stroke-dasharray="5,3"/><text x="300" y="300" font-size="8" fill="#1f5fbf">P1/P3 Z 6–34 (front strip)</text>
  <!-- bulkhead -->
  <rect x="610" y="126" width="34" height="78" fill="#dfe8f7" stroke="#1f5fbf"/>
  <rect x="644" y="114" width="28" height="100" fill="#c9d8f2" stroke="#1f5fbf"/>
  <rect x="672" y="114" width="32" height="100" fill="#b6caee" stroke="#1f5fbf"/>
  <text x="610" y="122" font-size="8" fill="#1f5fbf">window Z 48.5–87.5</text>
  <circle cx="626" cy="148" r="3" fill="#1f5fbf"/><text x="676" y="150" font-size="8" fill="#1f5fbf">ports Z 76</text>
  <rect x="610" y="176" width="34" height="16" fill="none" stroke="#a04800"/><text x="676" y="190" font-size="8" fill="#a04800">slot Z 54–62</text>
  <circle cx="648" cy="250" r="7" fill="#2a8a2a"/><text x="660" y="254" font-size="8">GX12-4 Z 25</text>
</svg>

### 2.3 Placement table (frame K, mm)

| Item | X | Y | Z | Fixed by |
|---|---|---|---|---|
| Tray (6 mm ply, corners R 15) | 10–299 | 3–226 | 0–6 | 4 × M5 × 16 through the case floor (sealing washers outside) at (25, 15), (285, 15), (25, 214)\*, (285, 214) |
| Left panel (6 mm ply 223 × 100) + M8P | 3–9 (board X 19–20.6) | 3–226 (board 30–200) | 0–100 (board 2–105) | 2 × DB18 to the tray; M8P on 4 × M3 × 10 standoffs [VERIFY the M8P hole pattern from BTT's SIZE-top.pdf] |
| Drum module (deck DB02) | 105–255 | 40–180 | legs 16–40, deck 40–44 | 6 × M4 rubber isolators to the tray |
| E-shelf (3–6 mm ply 100 × 120) | 158–258 | 50–170 | 78–81 | 4 × M3 × 35 standoffs on the deck at D (60, 52), (60, 98), (145, 52), (145, 98) |
| 250 ml accumulator | 52–102 | 45–220 | 6–56 | 2 × DB14 saddles at Y 61–95 and 120–154, zip ties |
| P1 / P3 | 112–177 / 182–247 | 6–34 | 6–34 | 2 × DB13 each, on 3 mm sorbothane, zip ties |
| ZFC filters, tees | 250–282 | 8–30 | 6–30 | zip ties to the tray |
| 30 ml accumulator | 110–175 | 192–222 | 6–36 | 2 × DB13 |
| Valve rack DB12 | 180–280 | plate 186–190, parts 190–222 | 6–96 | 3 × #6 × 3/8 in wood screws through the flange |
| Bulkhead DB06 + clamp DB08 | 285–316 | 53–177 | 43–93 | 4 × M3 × 25 through the wall |
| GX12-4 (loop) | right wall | 115 | 25 | panel nut |
| Vents 25 mm + DB17 baffles | right wall | 30 and 200 | 50 | 2 × M3 × 10 each |
| User connectors | left wall | 222 (DC), 214 (GX12-8), 206 (GX12-4) | 20 / 45 / 70 | panel nuts |
| Feet (outside) | corners, 20 mm in | — | — | adhesive |
| Hook plate DB09 (outside the lid) | centred on the lid | — | — | 4 × M5 × 16 + fender washers |

\* Move a tray screw if it lands on a floor rib. Mark the holes through the tray onto the case floor.

---

## 3. Pneumatic schematic (final)

```
 CASE AIR (through the front vent baffle foam = inlet muffler)
   │
   ├─► P1 BODENFLO BD-02A-1L (12 V, PWM on FAN0; published max 50 kPa; DEADHEAD ≤ 50 kPa measured, §4)
   │     └─4 mm─► F1 SMC ZFC050-04B (≤ 10 µm) ─► T ─► ACC1 250 ml PET (cap: PM-4 bulkhead union)
   │                                              │      [optional: 27G deadhead bleed to air here if P1 > 50 kPa]
   │                                              └─► MAN1 PK-4 (1-in-4-out, 4 mm)
   │                                                    ├─► R1a McMaster 4277T51, 3 psi = 20.7 kPa (via uxcell 4 mm × 1/8 NPT-F)  → air
   │                                                    ├─► R1b Generant VRV preset 3.5 psi ≈ 24 kPa (other make)                   → air
   │                                                    ├─► RAIL DUMP uxcell NO 12 V (HE3; energised = closed)                      → air
   │                                                    └─► MAN2 PK-4
   │                                                          ├─► S_rail XGZP6847A 0–40 kPa (silicone jumper)          → TH0
   │                                                          ├─► KQ2R23-04A ─1/8─► S070C-6DC-32 PIN A  P│A│R (HE0, NC: off = A↔R)
   │                                                          │                       A ─1/8─► TEE ─► S_A (TH1)
   │                                                          │                                 ├─► TEE (pad-2 port, KQ2P-23 plug)
   │                                                          │                                 └─► DB06 port A ═ DB07 ═ line A (TIUB01) → gallery A (Ø0.15 bleed, PAD)
   │                                                          ├─► KQ2R23-04A ─1/8─► male-Luer→ 25G needle (Ø≈0.26) ─1/8─► S070C-6DC-32 PIN B P│A│R
   │                                                          │                       (HE1 pwm 25 Hz)  A ─1/8─► TEE ─► S_B (TH2)
   │                                                          │                                 ├─► TEE (pad-2 port, plugged)
   │                                                          │                                 └─► DB06 port B ═ DB07 ═ line B → gallery B (Ø0.15 bleed, PAD)
   │                                                          └─► (spare, plugged)
   │
   └─► P3 BODENFLO BD-02A-1L (FAN1 PWM; DEADHEAD ≤ 30 kPa by the fixed bleed B3, §4)
         └─4 mm─► F2 ZFC050-04B ─► T ─► ACC2 30 ml HDPE
                                   └─► MAN3 PK-4
                                         ├─► R2  4277T51 20.7 kPa → air
                                         ├─► R2b Generant VRV ≈ 24 kPa → air
                                         ├─► PALM DUMP uxcell NO (HB) → air
                                         └─► TEE ─┬─► B3 palm bleed 27G (Ø≈0.21) → air  (also the P3 deadhead limiter)
                                                  ├─► PALM B port (provision, plugged)
                                                  └─► uxcell 3-way PALM (HE2; off = A↔exhaust) A ─► TEE ─► S_palm (TH3)
                                                                                                    └─► DB06 port P ═ DB07 ═ line P (TIUB01) → QEV → Airpel (HALO)
 All exhausts (S070 R ports, 3-way exhaust, dumps, reliefs, bleeds) vent into the case; the case breathes through two baffled vents.
```

**How it meets C3 (ruling) and §7.1**

| Requirement | How it is met here |
|---|---|
| Accumulator on the **rail side** of both PIN valves | ACC1 sits upstream of MAN1/MAN2. Only line + gallery air (≈ 8 ml) leaves on a vent. |
| PIN valves NC to the rail, venting when de-energised | S070C: P blocked and A ↔ R when off. With no coil power, every line vents. |
| Line B servo downstream of R1a/R1b | The 25G needle and the PIN B valve take rail pressure that R1a/R1b have already capped. |
| Rail-loss vent | RAIL DUMP and PALM DUMP are normally open, so they open when ACT-12 drops (≤ 50 ms) even if a PIN valve sticks. |
| Fail-to-free on the palm | PALM 3-way vents, PALM DUMP opens, the Ø 0.2 bleed is always open, the Airpel leaks, and the QEV at the float dumps (HALO). |

**Tube and fitting rules (a first-timer's checklist)**
- **In-box tube sizes:**
  - 4 × 2.5 mm PU (TU0425) from the pumps to the manifolds;
  - 1/8 in × 2.03 mm PU (TIUB01) from each reducer through the S070 barbs to DB06;
  - silicone 2 × 4 mm only as ≤ 40 mm jumpers onto sensor nozzles and the NO-valve and 3-way barbs.
- **Cutting:** cut PU square with a tube cutter or a fresh razor blade. Push into a push-fit until it stops (≈ 12 mm); a tug must not pull it out. To release a tube, press the collet ring and pull.
- **Over barbs:** push PU or silicone fully over the barb, past the last ridge. On the S070 barbs, warm the tube end in hot water first.
- **Needles to the next tube:** the needle hub (female Luer) screws onto a male-Luer-to-3/32 in barb. The cannula's open end goes **8 mm into the next PU tube**, sealed with a 2 mm band of 5-minute epoxy at the tube mouth and a 15 mm heat-shrink sleeve. Bleed needles to air are left open.
- **Leak test before any calibration:**
  - pin lines: ≤ 1 kPa/min decay with the gallery bleed plugged (§5.2);
  - palm line: ≤ 2 kPa/min.
  
  To find a leak, brush the joints with soapy water at 15 kPa: bubbles show it.

---

## 4. Relief setting and deadhead procedure (Stage A1)

**What you are proving.** Three separate mechanical barriers cap each rail. Firmware cannot change any of them:

| Barrier | Rail | Palm |
|---|---|---|
| Relief "a" | R1a 20.7 kPa | R2 20.7 kPa |
| Relief "b" (other make) | R1b ≈ 24 kPa | R2b ≈ 24 kPa |
| Pump deadhead | P1 ≤ 50 kPa | P3 ≤ 30 kPa |

These numbers become red line 2 (≤ 2.5 N per nail) and red line 3 (≤ 12 N total) in §7.2.

**You need:**
- the M8P running Klipper with S_rail and S_palm configured (ELECTRONICS bring-up), **or**, for the deadhead step only, the 0–15 psi dial gauge on a 4 mm tee;
- pinch clamps or KQ2P plugs to block a relief;
- a notebook or the `pump`/`sensors` console commands (§8.6 of the spec).

Wear safety glasses. These pressures cannot hurt you, but a tube that pops off can flick.

**A1-0 Zero.** With both pumps off and all dumps open, read S_rail and S_palm. Each must read 0 ± 0.3 kPa. Record the offsets.

**A1-1 Relief R1a alone** (do this five times):
1. Cap R1b and the RAIL DUMP outlet. For R1b, unscrew it and fit a 1/8 NPT plug into the adapter; for the dump, energise it closed. Close both PIN valves (de-energised; their P ports are blocked).
2. Run P1 with `pump 1 <duty>` stepping 20 → 40 → 60 → 100 % duty, 5 s at each step.
3. Record:
   - the **plateau pressure at 100 %**, which is the relief's full-flow pressure;
   - the **pressure 2 s after P1 stops**, which is the reseat pressure.
4. **Pass:** plateau **20.7 ± 1.5 kPa** each time; reseat ≥ 17 kPa (the relief reseats and the rail holds).
5. **If it fails:** a plateau well under 19 kPa means a leak upstream; soap-test it. Over 22.2 kPa means a faulty relief; replace it. McMaster's own figure is "fully open at about 10 % over the set pressure".

**A1-2 Relief R1b alone.** Swap the caps: R1a plugged, R1b fitted. Repeat. **Pass: 24 ± 1.5 kPa** (Generant preset 3.5 psi).

**A1-3 Both reliefs together.** Uncap both. The plateau must be **≤ 21.5 kPa** (R1a governs).

**A1-4 P1 deadhead** (this is the third barrier, so measure it, don't assume it):
1. Plug R1a, R1b and the dump, so that nothing on the rail can vent.
2. Watch the **dial gauge**; it is independent of the electronics.
3. Run P1 at **100 % for no more than 10 s**.
4. Record the highest reading.
5. **Pass: ≤ 50 kPa (7.25 psi).** At 50 kPa a bottomed nail sees 1.93 N, under red line 2's 2.5 N.
6. **If it fails:**
   - fit a **27G blunt needle to air** on the rail tee (the "deadhead bleed") and repeat;
   - still high: change to 25G;
   - re-run A1-1 afterwards. A bleed lowers the relief plateau slightly; that is fine as long as it stays ≥ 19 kPa.
   
   The bleed is a fixed hole behind the 10 µm filter, so it is a mechanical constant (CONFLICTS C9).
7. Unplug everything.

**A1-5 Palm side.** Repeat A1-1 to A1-3 with R2 and R2b, with the PALM 3-way off (its P port blocked).

**A1-6 P3 deadhead:**
1. Plug R2, R2b and the PALM DUMP. **Leave the 27G palm bleed open**; it is part of the design.
2. P3 at 100 % for no more than 10 s.
3. **Pass: ≤ 30 kPa.**
4. **If it fails:** add a second 27G bleed or change to 25G until it passes. Then check that P3 at 100 % can still hold **20 kPa with the bleed(s) open**. That is the top of the palm range (8–20 kPa); if it cannot, the bleed is too big.
5. Record the needle gauges used in the build log.

**A1-7 Line B at 100 % servo** (ruling C3; with PAD at A2):
1. Rail at the R1a plateau, PIN B PWM 100 %.
2. The per-nail force measured at the gallery tee must be **≤ 1.04 N**.

**A1-8 Rail PID:**
1. Set 2, 8 and 13 kPa in turn.
2. **Pass:** each holds ±0.5 kPa for 60 s with both PIN valves open into plugged galleries.

**Log** every number in the A1 sheet (TEST PROTOCOLS). **Repeat A1-1, A1-4 and A1-6:**
- after any pneumatic change;
- every 25 sessions;
- whenever a reading drifts more than 1 kPa from its logged value.

---

## 5. Drum module

### 5.1 Parts and what they do

| Ref | Part | Material, source | Function and key numbers |
|---|---|---|---|
| DB01 ×3 | Drum | SLA (JLC3DP 9600) | Ø 12 pitch (cable centre R 6.0); groove Ø 0.5, pitch 1.0 mm, 5 turns × 2 grooves. rotation_distance = 37.70 mm, so 1/16 step = 11.8 µm. Groove 1 (pad 1) at drum z 10.5–15.5; groove 2 (pad 2) at z 18.5–23.5. M3 grub on the D-flat via a trapped M3 nut. #2 crimp-tube anchor pocket at the start of each groove. Index magnet at R 12 under the Ø 30 flange. |
| DB02 | Deck | PETG, 4 perimeters, 40 % gyroid (or MJF) | 150 × 140 × 4 plate on six 24 mm legs: three motors hang underneath, two rod posts each end. Index Hall pockets at R 12, angle 180°. Working-point ticks at D x 94 / 100 / 106 (W−6 / W / W+6). Four shelf-standoff holes. |
| DB03 | Floating stop plate | PETG (or MJF PA12) | Rides two LM4UU on Ø 4 rods at D z 16. Six seat tongues (2.5 × 6 × 14 mm cantilevers, **≈ 17 N/mm PETG, ≈ 14 N/mm PA12** [EST]). Ø 2.5 ferrule bores 5 deep (DB03b: Ø 5.2 for SP41 end caps). Ø 1.0 cable holes with 0.8 mm release slots. Magnet bosses 5 mm toward the tongue root. |
| DB04 | Hall bridge | PETG | Carries three DRV5053s (plus three pad-2 pockets) facing the tongue magnets. Bolted behind the plate with 4 × M3 × 12 into inserts. Spacer washers set the sensor gap: **2.5 mm for DRV5053RA**, ≈ 6.5 mm (M3 × 16 + spacers) for VA. |
| DB05 | Comb ("three-ferrule hook block") | PETG | Holds the three housings 30 mm in front of the seats, so all three ferrules come out or go in together (T3). |
| — | Rods, LM4UU, springs | bought | 2 × Ø 4 × 100. Two uxcell 0.5 × 5.5 × 42 springs (≈ 0.3 N/mm [VERIFY]) between the rear posts and the plate bosses: **4.5 N total at the W tick** (7.5 mm compression each); ±6 mm travel. |
| — | Motors | 17HS08-1004S | Face up, bolted to the deck underside with 4 × M3 × 8 (blue thread-locker). Connector faces +x (the open side under the deck). |
| — | Isolators | M4 rubber 10 × 10, ×6 | The whole module floats as one rigid unit, so the cable path from drum to seat is not affected by isolator compliance. |

### 5.2 Tendon schematic (final)

```
 BOX (frame D)                                                                          UMBILICAL                         PAD (PAD WP)
 17HS08 (A, B, C: Klipper manual_stepper cable_a/b/c, GCODE_AXIS A/B/C, VREF ≤ 0.19 A)
   └ DB01 drum Ø12 ─ groove 1: #2 crimp in anchor pocket, 1.5 turns wrapped at centre (1.03–1.97 over travel)
        │  cable leaves tangent at y = drum y + 6, z 14, heading +x (66 mm free run, fleet ≤ 0.9°)
        ▼
   DB04 bridge hole Ø3 (sensor DRV5053 faces the tongue magnet, gap 2.5 mm)
   DB03 tongue: cable hole Ø1.0 → ferrule bore Ø2.5 (housing end bears here; ≈ 17 N/mm; Hall reads T_i ± 0.1–0.2 N)
        │  plate floats on LM4UU: Σ T_i = spring force = 4.5 N at the W tick (common mode absorbed; Σ e_i = 0)
        ▼
   housing (A: 1.35/0.74 coil + 3/32 brass ferrules | B: SP41 + end caps), free S-bend R ≥ 47 → DB05 comb
        │                                                                    ═══ through DB06/DB07 slot (free) ═══╗
        ▼                                                                                                          ║ 1.60 m seat to seat
   umbilical sleeve → 3 N clip → ≥ 450 mm loop → right hub bore (ear axis) → bail clip track → carriage → 150 loop ╝
                                                                     → deck stop (barrel adjuster, R 48 at 90/210/330°) → 2 N/mm spring
                                                                     → Ø1.6 brass ferrule → yoke post R 30 → 2.0 N magnetic coupling → block
 Pad-2 provision: groove 2 → row-2 seat (z 22) on the same tongue line; Hall pockets present; nothing installed.
```

**Pulls and caps (red lines 3, 7 and 13):**
- **Tangential cap:** the 2.0 N magnetic coupling at the pad (a constant).
- **Backup cap:** the stepper current.
  - With the live 16 N·cm motor, VREF must give **≤ 0.19 A rms**, i.e. ≤ 5 N of cable pull. The spec's 0.35 A would allow ≈ 9 N (CONFLICTS C5).
  - Measure the cable pull at stall with a luggage scale on the cable at A0.
- **Motors unpowered:** the drums back-drive, so nothing in the box holds force (red line 7).

### 5.3 Spring and tensioner numbers [EST]

- **Common mode.** All three housings bear on one plate, so ΣT = F_spring. A 1 N pad load changes the individual T_i by ≤ ±0.67 N and leaves ΣT unchanged. The bail and head-turn common mode (≤ 0.5 mm) moves the plate by ≤ 0.5 mm, which changes ΣT by ≤ 0.3 N (≤ 0.1 N per cable).
- **Travel:** ±6 mm on the deck ticks (ΣT 0.9–8.1 N at the ends). Operation stays within ±1.5 mm of W after trim (ΣT 3.6–5.4 N).
- **Plate friction** (two LM4UU) ≈ 0.05 N, small against the 0.67 N/N differential signal.
- **Flexure deflection** at 1.5 N:
  - tip 0.088 mm;
  - at the magnet 0.043 mm, i.e. 2.9 µm per 0.1 N.
  
  At a 2.5 mm gap from a 3 × 2 N52, the DRV5053RA sees ≈ 1.2 mV per 0.1 N, ≈ 20 ADS1115 counts at ±2.048 V. **Marginal against sensor noise; bench it first** (CONFLICTS C7).
- **Block stiffness including the flexure:** ≈ 1.82 N/mm (spec 1.9; CONFLICTS C6).

---

## 6. Tendons: routing, terminations, pre-tension and creep

### 6.1 Cut list (one pad; 1.60 m housings)

| Item | Length | Note |
|---|---|---|
| Housing ×3 | **1.600 m ± 2 mm**, seat end to deck-stop end | Measure all three together, taped side by side, and cut in one go: equal lengths matter more than the absolute length. Option A: Dremel cut-off wheel, then square and deburr the end on 400 grit and open the bore with a 0.8 mm drill bit turned by hand. Option B: housing cutter. |
| Cable ×3 | **1.90 m** each (trim later) | 1.60 housing + 0.057 drum wrap + 0.075 drum-to-seat + ≈ 0.06 pad side [PAD] + crimp tails |
| Ferrules (option A) | 8 mm of K&S 8126 per housing end, ×6 | Cut with a tube cutter or razor saw; deburr inside. |

### 6.2 Terminations

**T1-a. Box end of the housing (option A).**
1. Scuff 8 mm of the coil end with 400 grit.
2. Coat it thinly with slow epoxy.
3. Slide the 8 mm brass ferrule on so it is **flush with the coil end**. Wipe any epoxy off the end face.
4. Push a 0.4 mm wire through the bore while the epoxy cures, so the bore stays open.
5. **Good:** the end face is flat and square, with no epoxy bead.

**T1-b. Option B.** Press a Shimano/Jagwire 4 mm end cap onto each end.

**T1-c. Drum end of the cable.** Done in the box, after threading; §11 step D7.
1. Slide on one #2 crimp tube, leaving 4 mm of tail.
2. Crimp with the Beadalon Standard Crimper: first the back (oval) notch, then fold in the front notch.
3. **Proof every crimp at 30 N.** Hang a 3.1 kg load (a 3 L water bottle in a bag) on the cable for 10 s; the crimp must not move.
4. Trim the tail to 1.5 mm.
5. **Good:** the tube is folded into a C shape and the wire does not slide under a hard fingernail pull.

**T1-d. Pad end.** PAD specifies the Ø 1.6 brass ferrule at the series spring. Proof it the same way (30 N).

### 6.3 Flexure calibration (once per plate, and again at 50 sessions)

**Jig**
- A 623ZZ bearing on an M3 bolt, clamped to the deck's +x edge (a small C-clamp), at cable height.
- A 100 mm stub of the same housing in the seat.
- The cable runs from the drum, through the stub, over the bearing, down to a zip bag.

**Procedure**
1. Power the M8P (logic only is enough for the ADS1115) and hold the drum by hand.
2. Add US nickels (5.000 g each) to the bag: 0, 10, 20, 30, 40, 50 nickels = 0, 0.49, 0.98, 1.47, 1.96, 2.45 N.
3. Record the reading (`tensions`) 3 times at each step, then come back down the same steps.
4. **Pass:**
   - a straight line (R² ≥ 0.995);
   - up/down hysteresis ≤ 0.1 N;
   - noise ≤ 0.1 N rms at 280 Hz (V-T5).
5. Store the slope and offset per channel.
6. **If it fails:**
   - **noise too high:** close the gap one washer at a time (RA variant), or print DB03 with a 2.0 mm tongue (CONFLICTS C7);
   - **hysteresis:** check the LM4UU for binding and that the bridge screws are tight.

### 6.4 Pre-tension and trim (after the pad is built; A3)

1. **Home.** ARMING homes all three drums on their index (drums unpowered before this).
2. **Common mode.** Turn the three pad barrel adjusters **equally**, half a turn at a time, until the plate's rear boss face sits on the **W tick** (D x 100) ± 1 mm. ΣT is now ≈ 4.5 N.
3. **Differential.** Read `tensions`. Adjust the adjusters in pairs (tighten one, loosen another by the same amount) until each cable reads **1.5 ± 0.1 N** with the plate still on W ± 1.
4. **Centre.** Run the ink rosette (TEST/PAD). If the block centre is off by more than 0.3 mm, enter per-cable length offsets in firmware (`cal drums`); do not chase it with the adjusters.
5. **Log** the three tensions, the plate position, and the adjuster positions (count the turns from fully in).

### 6.5 Creep re-check

Three things settle in this tendon system:
- the nylon-coated cable under the crimps;
- the housing liner under compression;
- the PETG tongues.

All three show up as the plate drifting backward (−x) and the tensions falling.

| When | Check | Act if |
|---|---|---|
| After 1 h of running, then after a 24 h rest | plate position, three tensions | plate off W by > 1.5 mm, or any tension outside 1.5 ± 0.2 N → redo §6.4 steps 2–3 |
| After sessions 1, 2, 3 | same | same |
| Every 10 sessions | same + look at each crimp and the first 50 mm of cable at the drum with a 10× loupe | any broken strand, or a crimp that has moved → replace that cable (§4.4: also replace at 50 sessions) |
| Every 50 sessions | flexure calibration (§6.3) | slope changed > 5 % → re-store it |

Expect the first-week creep to take up 1–3 mm of common mode [EST]; the plate's ±6 mm travel covers it.

---

## 7. Umbilical build sheet (Stage B)

**Lengths** (CONFLICTS C4: the 1.6 m housing limits the riser to ≈ 0.47 m):

| Segment | Length | Owner |
|---|---|---|
| In-box housing run (seat → DB07 rear face) | 0.13 m | DRIVE BOX |
| **Sleeved umbilical** L_u (DB07 → right-hub clamp): riser ≤ 0.47 + free loop ≥ 0.45 | **0.92 m** | DRIVE BOX |
| Head side (hub bore → bail clip track → carriage → 150 mm loop → deck stops) | 0.55 m [HALO to confirm] | HALO |
| **Housing total** | **1.60 m** | — |

**Cut list (one pad)**

| Line | Cut | Box end | Head end |
|---|---|---|---|
| PIN A tube (TIUB01) | 1.75 m (trim at the pad) | KQ2H23-M5A in DB07 port A (v −16) | PAD gallery A barb (continuous; the 0.15 m on-pad jumper is this tube) |
| PIN B tube | 1.75 m | DB07 port B (v 0) | gallery B |
| PALM tube | 1.60 m | DB07 port P (v +16) | QEV on the float (HALO) |
| Housings ×3 | 1.600 m | DB03 seats via the DB07 slot | deck stops A (90°), B (210°), C (330°) |
| 4-core 26 AWG | 1.10 m | GX12-4 cable plug: pin 1 loop out, pin 2 loop return, pins 3–4 spare (insulate) | 2-pin magnetic pogo at the right hub (ELECTRONICS/HALO) |
| Stockinette 1 in | 0.95 m | over everything, from 20 mm behind DB07 | to 10 mm short of the hub clamp |

**Build order**
1. **Mark.** Lay the three housings, three tubes and the cable side by side on the table. Mark each with coloured tape bands at both ends, matching the port colours on the box: A red, B blue, P white, tendons A/B/C = 1/2/3 bands.
2. **Housings through the plug.** Pass the housings through the **DB07 slot** (ferrules pass easily), then through the DB06 slot when the plug is offered up.
3. **Tubes into the plug.** Push the three tubes into the DB07 KQ2H23 fittings, already screwed into the M5 holes you tapped in DB07. Tug-test each one.
4. **Strain relief.** Fit a Ø 12 P-clip (M3 × 8 into the two tapped holes at the bottom rear of DB07) around the **tubes + cable only, not the housings**. The housings must slide.
5. **Sleeve.** Pull the stockinette over the bundle. Secure each end with a 20 mm band of heat-shrink. **Never tie or tape the bundle along its length.** It must stay loose, so the head can turn (≤ 0.01 N·m at 60° yaw).
6. **Clip.** Clamp **DB16a + DB16b** around the sleeve at **0.47 m from DB07**: 4 × M3 × 20, nuts in DB16b, snug but not crushing. Check that a tube slides when you pull it inside the clip.
7. **Hanger.** Fit the gooseneck's C-clamp on the chair-back top or the desk edge. Screw **DB15** onto its 1/4-20 tip; the 1/4-20 nut is glued in DB15 with CA. Press a Ø 6 × 3 N52 into DB15's pocket with a dot of CA, flush. Glue an M6 steel washer into DB16a's nose pocket.
8. **Set the clip to 3 ± 1 N.** Seat the clip on the hanger. Hook a luggage scale (or the kitchen-scale pull method) on the sleeve 50 mm from the clip and pull **along the umbilical, toward the head**. Add layers of electrical tape on the magnet face until the clip releases at 2–4 N, five times out of five.
9. **Head end.** HALO takes it from here: hub bore, pogo lanyard, deck stops, QEV.

**Gate C6 (with HALO):**
- the clip pops at 3 ± 1 N;
- the lanyard parts before any tube is taut;
- yaw torque at ±60° ≤ 0.02 N·m;
- stand-up test ×5.

**Box end (packing and unpacking: T3, §6)**

*Unpack* (≈ 3 min):
1. Lever released, box off.
2. Open the lid.
3. Turn each drum by hand to pay out ≈ 1.5 turns, and lift its crimp out of the anchor pocket.
4. Slide the DB05 comb toward the wall, so the three ferrules leave their bores.
5. Lift the cables up out of the 0.8 mm release slots.
6. Undo the two M4 thumb screws.
7. Unplug the GX12.
8. The umbilical, with DB07 and the housings, comes away.

*Repack:* the same in reverse, then:
- **ARMING** re-homes the drums;
- **check the plate is on W ±1.5 mm**; if not, trim (§6.4 step 2–3).

---

## 8. Noise mitigation (§4.9 budget ≤ 30 dBA at 1 m)

| Source | Measure | Where |
|---|---|---|
| Steppers (step ripple, ≈ 700 Hz) | stealthChop; VREF ≤ 0.19 A (also the safety cap); the whole module on six rubber isolators; the deck is not screwed to anything rigid | §5.1 |
| Stepper ripple into the tendons | 2 N/mm series springs at the pad (PAD); leap4-D: +6 dB vs the air puppet | — |
| Pumps | 10–20 % duty; **3 mm sorbothane under each DB13 saddle**; soft 4 mm PU (not rigid) for the first 100 mm; inlets inside the front vent-baffle foam (inlet muffler) | §2.3 |
| Valve clicks | S070s switch only on the rim; the rack sits on a 3 mm sorbothane strip under its flange | — |
| Exhaust hiss | all exhausts vent inside the case, which acts as the muffler; the vents are baffled | §3 |
| Case drumming | line the lid and the two long walls with **3 mm closed-cell EVA** (contact cement); sorbothane hemisphere feet; latches closed | §11 phase C |
| Cable creak | greased housings: one drop of light silicone or PTFE oil per housing before threading [V-T3] | §6 |
| Placement | box 0.7–1.2 m from the ear; on a chair back it is behind the seat back, which helps | §9 |

**Test (A5):**
1. Phone SPL app, A-weighted, slow, at 1 m, box closed.
2. Record (a) the room, and (b) PLINE at 1.4 Hz with P1 cycling.
3. **Pass:** (b) − (a) ≤ 3 dB, and the earplug A/B (leap4-D) is indistinguishable.
4. **If it fails:**
   - if the pumps dominate, add a second sorbothane layer and check that no tube touches the wall;
   - if the steppers dominate, check that no isolator is shorted by a screw or wire and reduce the step rate ripple (interpolation on).

---

## 9. Mass ledger and mounts

### 9.1 Mass ledger [EST; weigh at A5]

| Item | kg |
|---|---|
| Apache 2800 case, foam removed (HF 3.96 lb shipping; a user report says "5 pound") | 1.60 |
| 3 × 17HS08-1004S (0.14 each) | 0.42 |
| Drum module printed parts, rods, bearings, springs, isolators, screws | 0.20 |
| M8P V2.0 + CB1 + 3 TMC2209 | 0.17 |
| Pneumatics (2 pumps 0.12, valves 0.07, reliefs 0.04, sensors, filters 0.03, ≈ 25 fittings 0.10, tubing, bottles) | 0.37 |
| Tray + left panel (6 mm ply, lightened) + brackets + E-shelf | 0.33 |
| Electronics smalls and wiring (ELECTRONICS) | 0.22 |
| Bulkhead DB06 + clamp DB08 (the plug DB07, 0.09, travels with the umbilical) | 0.14 |
| Hook plate + 2 hooks + M5 hardware (always fitted) | 0.16 |
| Valve rack, saddles, baffles | 0.08 |
| Panel connectors, vents, EVA lining, feet, fasteners | 0.12 |
| **Total** | **≈ 3.8 kg (3.6–4.0)** |

**Against §6 (≤ 2.8 kg): it fails** (CONFLICTS C1).

**Trims if wanted:**

| Trim | Saves |
|---|---|
| Tray-less build | −0.19 kg |
| Hook plate off when the box lives on the desk | −0.16 kg |
| PETG pocketed bulkhead | −0.06 kg |

**Real fix:** the R9 ply box (−0.8 kg).

**Recommendation:** relax §6 to ≤ 4.0 kg.

### 9.2 Mounts (M16)

| Placement | How | Umbilical routing |
|---|---|---|
| **Chair back** (default) | DB09 hook plate on the lid. DB10 (30 mm throat) or DB11 (55 mm throat) J-hooks over the chair's top rail, hooks at the hinge-side top. A 1.5 in cam strap around the chair back through the two plate slots. The box hangs vertically, right end (umbilical) toward the user's right. | Gooseneck clamped to the chair-back top rail; DB15 clip 100–200 mm from the right ear; riser ≤ 0.47 m (C4). |
| **Desk / side table** | Flat on the four sorbothane feet; lid closed. Hooks stay on: they face down-and-away when lying flat on the base. | Gooseneck clamped to the desk edge. **The box must be within ≈ 0.45 m of the clip point** (C4). |
| **Couch back** | Flat on the cushion-back on its feet, with a 600 mm non-slip mat strip (rug gripper). Strap it to the couch frame with the cam strap if the top is narrow. | Gooseneck on the couch frame or the case handle (handle mount: clamp on the handle bar). |

---

## 10. Portability test (A5 gate; V-B1)

Run it with the full box closed and the umbilical attached to the bench pad.

| # | Test | Method | Pass |
|---|---|---|---|
| P1 | Mass | Luggage scale on the handle | **≤ 4.0 kg** (proposed, C1); report against 2.8 |
| P2 | Orientation | 5 min PLINE + group switching with the box (a) flat, (b) on its back (lid down), (c) on its right end, (d) on its face, (e) hanging from the chair hooks | No rattles; tensions within ±0.2 N of the flat run; no rail PID alarm; the plate stays within W ± 1.5 mm; nothing shifted when the lid is opened |
| P3 | Noise | §8 | ≤ +3 dB over the room; earplug A/B passes |
| P4 | Heat | 1 h, PLINE 50 % / REST 50 %, box closed; kitchen probe thermometer in the case through a vent, plus the M8P MCU temperature | ≤ +20 K over the room inside the case; MCU ≤ 60 °C |
| P5 | Carry | Carry by the handle up and down stairs, set it down hard on a carpet (≈ 5 cm drop), then ARMING | Index error ≤ 0.3 mm on all drums; no tube unseated (leak-down ≤ 1 kPa/min) |
| P6 | Chair hang | 20 min of TV with the box hanging, pad parked | Hooks undeformed (check the throat with calipers: ≤ 0.5 mm change); lid hinge and latches fine |
| P7 | Pack and unpack | §7 box end, timed, twice | ≤ 5 min each; W within ±1.5 mm after repack, without re-trim |
| P8 | Breakaway at the box | Pull the umbilical sideways at the plug with 40 N (luggage scale) | DB07 does not move and seals hold (no decay) |

---

## 11. Assembly steps for a first-timer

**Before you start**

*Tools:* metric hex keys (1.5, 2, 2.5, 3), Phillips #1/#2, flush cutters, needle-nose pliers, calipers, the crimper, M3/M5 taps and tap wrench, a soldering iron with heat-set-insert tip (or a plain conical tip at 220 °C), a cordless drill with bits 2.5/3.4/4.2/4.5/5.5 mm, a step bit, a 25 mm hole saw, a coping saw or jigsaw, files, 5-minute and slow epoxy, CA, blue thread-locker.

*Print orientation* is in cad/README.md. Clean every print: remove brims and drill out every hole to its nominal size (Ø 3.4 holes with a 3.4 mm bit by hand).

*Insert rule:*
1. Set the iron to 220 °C for PETG.
2. Rest the insert on the hole and let it sink under its own weight plus light pressure, until it is 0.2 mm below flush.
3. Lift the iron straight up. Don't wiggle.

### Phase S0: drum rig (also the bench start of the module)

| Step | Do | Good looks like | If not |
|---|---|---|---|
| S0.1 | Print DB02 deck (top face down, no supports) and order DB01 ×4 in SLA | flat deck; drums with crisp grooves | deck warped > 0.5 mm → reprint at 85 °C bed with a brim |
| S0.2 | Bolt the three motors under the deck: connector toward +x, 4 × **M3 × 8** SHCS each, blue thread-locker | motor faces flush to the deck underside; shaft stands 16 mm above the deck top | shaft rubs the Ø 22.6 hole → file the hole |
| S0.3 | Push a DRV5023 into each index pocket, flat face up, legs along the channel. Glue with a dot of CA. Solder 3 thin wires (30 AWG) and route them along the channel and down the edge. | sensor top flush or 0.1 mm below the deck | proud → deepen the pocket with a file |
| S0.4 | Drum prep: CA one index magnet into each drum's flange pocket, **same pole down on all three** (mark the magnet with a marker first, using one of the spare magnets). Drop an M3 nut into the slot from the bottom; start an **M3 × 6 grub** from the outside. | magnet flush; nut captured | — |
| S0.5 | Slide each drum on its shaft, flat to the grub, drum bottom **1.0 mm above the deck** (use a 1 mm shim, e.g. two stacked credit cards, then remove it). Tighten the grub firmly. | the drum turns freely with the motor unpowered; no wobble visible against a pen tip | wobble → the bore isn't on the flat; loosen, re-seat |
| S0.6 | Ink rig per leap4-D (e) / TEST PROTOCOLS: the cables from §6 go straight to the pen plate | — | — |

### Phase A1–A2: pneumatics on the tray

| Step | Do | Good looks like | If not |
|---|---|---|---|
| A.1 | Cut the tray: 289 × 223 mm from 6 mm ply, corners R 15 (trace a soda can). Drill the 4 case-floor holes Ø 5.5 later (phase C). Lay out the zones from §2.3 in pencil. | tray drops into the case with ≈ 1–3 mm all round | tight → plane or sand the edges |
| A.2 | Print and fit 2 × DB14 (bottle) and 4 × DB13 (pumps, 30 ml). Cut 3 mm sorbothane pads to each footprint. Screw down with **#6 × 3/8 in** pan-head wood screws. | — | — |
| A.3 | Accumulator caps: drill each cap Ø 8 (or to suit the PM-4 bulkhead thread [VERIFY]). Fit the bulkhead union with its nut inside the cap and a thin smear of silicone. | the cap still screws on; no leak at 25 kPa (soapy water) | leaks → add an O-ring under the nut |
| A.4 | Valve rack: print DB12. Mount the valves, sensors, reliefs and manifolds on it with 2.5 mm zip ties through the 10 mm-grid holes, in the order of the schematic: **rail side left, palm side right**. Label every valve with tape. | nothing can move when you shake the rack | — |
| A.5 | Plumb exactly as §3 (tube rules). Tag both ends of every tube. | — | — |
| A.6 | Leak test, then **§4 in full**. Do not continue until A1-1 to A1-8 pass. | log sheet complete | see §4 |

### Phase A3: drum module complete

| Step | Do | Good looks like | If not |
|---|---|---|---|
| D.1 | Print DB03 (lying on its −x face) and DB04. Fit 4 heat-set **M3 × 5.7** inserts in DB03's rear face. Press the LM4UUs into the bosses with a vise and a socket (a drop of CA on the outside). | bearings flush; the plate slides on a test rod with no drag | tight → ream the boss to 8.1 with sandpaper on a dowel |
| D.2 | CA a magnet into each **row-1** tongue boss; all the same pole toward −x. (Row 2 stays empty.) | magnet flush | — |
| D.3 | Rods: push one rod through a rear post, slide on a spring, then the plate's bearing, then into the front post. Repeat for the other rod. A drop of light oil on the rods. | the plate slides ±6 mm smoothly, and the springs push it to +x when released | binding → check the posts are square; open the rod holes with a 4.0 mm bit if a rod won't go in |
| D.4 | DB04: push three DRV5053s (RA first) into the row-1 pockets, flat face toward +x. Leads go down the lead channels. Solder 3 × 30 AWG each. Bolt to DB03 with **4 × M3 × 12** and **two 0.5 mm M3 washers** under each (1 mm gap). | sensor faces 2.5 mm from the magnets (check with a 2.5 mm drill shank as a feeler) | adjust with washers |
| D.5 | Isolators: 6 × M4 rubber isolators. From the deck top, **M4 × 35** SHCS down through each leg into the isolator. From under the tray, **M4 × 12** countersunk (countersink the ply 1 mm) into the isolator's lower end. | the module rocks slightly when pushed, and springs back | — |
| D.6 | Flexure calibration, §6.3 | pass lines in §6.3 | see §6.3 |
| D.7 | Thread each cable from the pad side: pad end → deck stop → housing → **seat bore** → tongue hole → bridge hole → drum. Wrap **1.5 turns** into groove 1, winding so that the drum turning *toward +x at the cable tangent* pays out. Crimp the drum end (§6.2), and drop the crimp into the anchor pocket. Clip the comb onto the three housings 30 mm in front of the seats. | the cable lies in the groove without crossing itself; the housing ferrules sit fully home in their bores | the cable rides out of the groove → the fleet angle is wrong; check the drum height (S0.5) |
| D.8 | Pre-tension and trim, §6.4 | — | — |

### Phase C (A5): the case

| Step | Do | Good looks like | If not |
|---|---|---|---|
| C.1 | Empty the case: remove all the pick-and-pull foam. **Keep two blocks** for the vent baffles. Remove the lid foam above where the M8P will stand. | — | — |
| C.2 | **Wall window (right end).** Tape the outside. Mark a 73 × 39 mm rectangle centred at Y 115, Z 68 (from the inside floor), on a flat patch [VERIFY ribs]. Drill 6 mm holes in the four corners, then cut between them with a coping saw or jigsaw. File to the line. | DB06's neck slides in with ≤ 0.5 mm play | over-cut → bed DB06 in silicone; the clamp still holds |
| C.3 | DB06 + DB08: tap DB06's three M5 holes and DB07's three M5 holes (M5 tap, straight, a drop of oil; back the tap off every half turn). Screw in the 6 × KQ2H23-M5A, gasket faces snug. Press the two Ø 3 × 12 dowels into DB06 (vise). Slide two M4 nuts into DB06's top slots. Fit DB06 from outside with a bead of silicone under the head, DB08 inside, **4 × M3 × 25** + nyloc. | head flat on the wall; no gap | — |
| C.4 | Right wall: drill **Ø 12.2** for the GX12-4 at Y 115, Z 25 (step bit). Drill two **25 mm** vents (hole saw) at Y 30 and Y 200, Z 50. Fit the DB17 baffles inside with 2 × M3 × 10 each, filled loosely with case foam. | — | — |
| C.5 | Left wall: DC jack hole (Ø per the jack, ≈ 11–12 mm), GX12-8 and GX12-4 holes **Ø 12.2**, at Y 222 / 214 / 206 and Z 20 / 45 / 70. Status LED Ø 5 or 8 at Y 15, Z 75. (ELECTRONICS fits the connectors.) | — | — |
| C.6 | Lining: cut 3 mm EVA for the lid and the two long walls (not the ends). Glue with contact cement. | — | — |
| C.7 | Lid hook plate: put DB09 on the lid's outside, centred, hinge side as "up". Mark and drill 4 × Ø 5.5. **M5 × 16** pan head from outside, fender washer + nyloc inside. Bolt the J-hooks (DB10 or DB11) with **M5 × 12** into the hex-pocket nuts. | the lid still closes and seals; no screw touches anything in the base | a nut fouls → shorten the screw |
| C.8 | Feet: four sorbothane hemispheres on the base's outside floor, 20 mm in from the corners. | — | — |
| C.9 | Tray in: lower the complete tray (drum module, pneumatics, rack, E-shelf, left panel). Mark the 4 tray holes onto the case floor, take the tray out, drill Ø 5.5, then refit with **M5 × 16** + rubber sealing washers outside + nuts inside. | tray solid; no rocking | — |
| C.10 | Connect DB06's inner fittings to lines A, B and P from the rack (1/8 in tubes, labelled). | — | — |
| C.11 | Portability test, §10. | all of P1–P8 | — |

### Phase B: umbilical and hanger
§7, in order.

---

## 12. Printed parts summary (details in cad/README.md)

| Part | Qty | Material | Who prints | Notes |
|---|---|---|---|---|
| DB01 drum | 3 (+1) | SLA 9600 / JLC Black | **print service OK** | the grooves need SLA resolution |
| DB02 deck | 1 | PETG / PA12 | print service OK (MJF ≈ $25–30) | flat, simple |
| DB03 floating plate (or DB03b) | 1 | PETG / PA12 | **needs iteration, home printer recommended** | the tongue stiffness and sensor gap may need 1–2 tries (C7) |
| DB04 Hall bridge | 1 | PETG | needs iteration, home printer recommended | — |
| DB05 comb (or DB05b) | 1 | PETG | print service OK | — |
| DB06 bulkhead, DB07 plug | 1 + 1 | **SLA** (airtight) | **print service OK** | tap M5/M3 after printing |
| DB08 clamp | 1 | PETG | print service OK | adjust WALL_T first (C19) |
| DB09 hook plate, DB10/DB11 hooks | 1 + 2 | PETG, 5 perimeters for the hooks | print service OK | the hooks carry 20 N each |
| DB12 pegboard, DB13 ×4, DB14 ×2, DB17 ×2, DB18 ×2 | — | PETG | print service OK | — |
| DB15 seat, DB16a/b clip | 1 + 1 + 1 | PETG | needs iteration (3 N setting), home printer recommended | — |

---

## 13. Open items this package closes, and the ones it adds

**Closed or made ready to close**
- V9 / V12: procedure §4.
- V-T5 / V-T6: procedures §6.3 and §5.
- V-B1: procedure §10.
- V-T4: inspection §6.5.
- V2: S070C price re-confirmed at $35.00.

**Added or still open:**
- CONFLICTS C1–C21. **The four to decide now:**
  1. **C1:** box mass ≈ 3.8 kg.
  2. **C3:** the housing source.
  3. **C5:** VREF ≤ 0.19 A for 5 N.
  4. **C8:** the Generant quote for the diverse reliefs.
- [VERIFY] on the hardware in hand:
  - Apache base/lid split and wall thickness;
  - M8P hole pattern;
  - 4277T51 thread;
  - PM-4 bulkhead thread;
  - pump prices;
  - uxcell spring rate;
  - DRV5053 noise.
