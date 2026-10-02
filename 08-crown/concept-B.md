# CROWN CONCEPT B — "TRIPOD CAP"
(Concept team B. Seed: the smallest possible structure, three legs on three pads, hand module's elbow carrier as the hub. Written to CROWN-BRIEF.md; numbers reference DESIGN-FREEZE.md, ADDENDUM-1, mechanical.md §2/§5.3/§6–9/§11–12, safety-requirements.md §2.2/§3.1/§3.9/§7, hair-interaction.md §1.3/§1.5/§6, judge-2 §0, redteam-2 §1–3/§5–6/§8.)

**In one sentence.** The 270 mm 2020 elbow-carrier beam, drop legs, yaw plates, spine, post, hinge, springs, magnet, VESA adapter, ballast and monitor arm are all deleted; the servo cradle (P13) and idler housing (P15) are instead bolted to two printed NODES joined by a 10 mm carbon tube 68 mm behind the elbow axis, and three carbon-tube legs with Ø 45 mm TPU pads carry that hub on the skull in a 140 mm triangle around the scratch patch, retained by a light elastic Y-strap under the chin on a magnetic breakaway buckle. The hand, yoke, rail, float, wrist and all firmware are untouched.

**Headline numbers.** Head-borne mass 442 g bare float (W1), 472 g with the +30 g slug; the +60 g slug is barred on the head until the lightening list in §4 is applied (target 395 g). Pads: 3 × Ø 45 mm, 2.7–3.9 kPa. Stability margin against the worst stroke reaction: 1.5× with the strap at 2.5 N per side, 0.8× without it (so the strap is required). Coverage: crown and upper occiput, repositionable by lift-and-reseat. Cost delta vs the hand module alone: +$38; vs the monitor-arm stand: −$120 to −$150.

**Discrepancy flagged first.** The brief says the hand module is "≈ 150–200 g". mechanical.md §3.1 itemises the parts on the elbow axis (servo + cradle 41, idler 33, cheeks 30, crossbar 45, mast/rail/stops 64, shroud 15, float 92, guards 16, cables 10) at **346 g**. All mass figures below use that, trimmed to 325 g by two cuts in §4; every one of those parts must be on the head in any crown concept.

---

## 1. Geometry

### 1.1 What changes in the module interface
- **Elbow carrier beam (270 mm 2020, 130 g) → carbon hub tube.** A 10 × 8 mm pultruded carbon tube, 250 mm long, parallel to the elbow axis at (X −68, Z +84): 68 mm behind the axis, level with it. Everything that swings stays ≥ 20 mm clear (palm rear corner X −31 at ±28°, mech §2 check a; mast top X −48 at Z 160). The scalp under it is at Z −27, so the tube is 100 mm above skin, outside even the 60–90 mm zone for 5–8 cm hair.
- **Drop legs P11/P12 → nodes N-S and N-I.** Printed PETG blocks that (a) take P13's 4 × M3 foot pattern (copied from P11's flange, so P13/P17 bolt on unchanged; the idler side takes P15 on its 2 × M3 slots as P12 did), (b) clamp the hub tube in a slit Ø 10.2 bore with one M3, (c) carry a Ø 8.2 socket and M3 thumbscrew for a side leg. Servo stays at Y −101 to −127, horn +Y; idler at Y +101 to +111; cheeks at |Y| 93–98. **Nothing in the yoke, rail, float, wrist or hand changes.**
- **Coaxiality.** Nodes are set on the tube with the zero pin through cheek A and P13, the shoulder screw in P15, and the yoke swinging free before the clamps are tightened (P15's slots give ±1.5 mm).

### 1.2 Pads and legs
| Pad | Centre (X, Y) | Scalp Z on the R 90 sphere (centre 0, 0, −86) | Leg route |
|---|---|---|---|
| P-S (servo side) | (+45, −70) | −52 | 8 × 6 mm carbon tube from node N-S at (+20, −108, +50), straight down outside the cheek to Z 0, then a printed bend inboard-forward to the pad stem |
| P-I (idler side) | (+45, +70) | −52 | mirror of P-S |
| P-R (rear) | (−80, 0) | −45 | 10 × 8 mm carbon tube straight down from a clamp at the hub tube's mid-length (X −72, Z 84) to the pad stem; 125 mm long |

Triangle: 140 mm between the side pads, 143 mm from each side pad to the rear pad; centroid at (+3, 0). The nail patch (chord ±19 mm in X, nails at Y ±24) and the whole-cap centre of mass (§4: X +9) sit inside the triangle with ≥ 36 mm to every edge.

The sphere exaggerates the drop at 80 mm radius; a real crown is flatter. Each leg therefore has **±12 mm of length adjustment** (tube in socket, M3 thumbscrew) and is set with the existing apex height gauge P43 so that the elbow axis is 80 mm above the target point (H = 80, e = L_max − 80).

**Pad.** Ø 45 mm TPU 95A dome shell, 2.5 mm wall, 12 mm tall, rim R 8, face printed down and ironed (hair–TPU µ 0.4–0.8 per hair-interaction §1.5, taken as 0.4 design / 0.3 worst), bonded to a PETG stem drafting from Ø 12 at the tube socket to Ø 18 at the dome over 30 mm. **No joint within 30 mm of the pad face**: the pad is rigid and the ±5° of local mismatch is taken by the dome's own compliance (≈ 3 N/mm). There is no rotation anywhere in the structure.

**Hair canopy.** The pads sit on the pile (5–20 mm for 2–8 cm hair) and press it flat; they are stationary, so TPU's high friction holds rather than grabs (nothing slides through hair). The side legs' inboard runs cross the canopy at ≥ 35° to the scalp tangent, so the only canopy contact is the pad. Every leg surface is a closed tube or drafted solid; the only gaps are the clamped tube sockets ≥ 60 mm above skin (no changing gap). Side-leg vertical run (|Y| ≥ 106) to the swinging cheek (|Y| ≤ 98): 8 mm at Z 0–50, ≥ 36 mm above the scalp there (> 3 mm rule, smooth on smooth). Inboard run to the swung palm end (Y −88, Z ≥ 31): 58 mm. Knuckle plate and paddles (|Y| ≤ 45) to the inboard runs (|Y| ≥ 70): ≥ 25 mm.

### 1.3 Side view (XZ), Y = 0 section, 1 px = 1 mm
<svg viewBox="0 0 420 320" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="9">
  <!-- frame: x = X + 190, y = 196 - Z -->
  <path d="M 70 290 A 90 90 0 0 1 310 290" fill="none" stroke="#999" stroke-width="1.5"/>
  <text x="300" y="300" fill="#999">scalp R 90 (apex Z +4)</text>
  <line x1="190" y1="60" x2="190" y2="300" stroke="#ccc" stroke-dasharray="3 3"/>
  <text x="193" y="70" fill="#999">X 0</text>
  <!-- elbow axis -->
  <circle cx="190" cy="112" r="4" fill="none" stroke="#000"/>
  <text x="197" y="108">elbow axis Z +84</text>
  <!-- hub tube -->
  <circle cx="122" cy="112" r="5" fill="#333"/>
  <text x="60" y="100">hub tube Ø10 CF, X −68</text>
  <!-- node outline -->
  <rect x="118" y="100" width="92" height="40" fill="none" stroke="#555" stroke-dasharray="2 2"/>
  <text x="120" y="150" fill="#555">node (cradle flange + tube clamp)</text>
  <!-- cheek / yoke -->
  <path d="M 190 92 L 247 92 L 247 132 L 190 132 Z" fill="none" stroke="#06c"/>
  <!-- crossbar + mast -->
  <rect x="235" y="100" width="12" height="16" fill="#06c"/>
  <rect x="230" y="28" width="5" height="90" fill="#06c"/>
  <text x="238" y="35" fill="#06c">mast + MGN9 rail</text>
  <!-- palm -->
  <rect x="164" y="130" width="52" height="28" fill="none" stroke="#06c"/>
  <text x="166" y="170" fill="#06c">palm</text>
  <!-- knuckle plate and nails -->
  <path d="M 158 158 Q 190 152 222 158" fill="none" stroke="#06c" stroke-width="2"/>
  <line x1="190" y1="158" x2="190" y2="196" stroke="#06c" stroke-width="2"/>
  <text x="194" y="192" fill="#06c">nail, Z 0</text>
  <!-- rear leg -->
  <line x1="118" y1="112" x2="110" y2="241" stroke="#000" stroke-width="3"/>
  <ellipse cx="110" cy="243" rx="22" ry="6" fill="#c60"/>
  <text x="40" y="262" fill="#c60">P-R pad (−80, 0), Z −45</text>
  <!-- side leg (profile, one shown) -->
  <line x1="210" y1="146" x2="210" y2="196" stroke="#000" stroke-width="3"/>
  <line x1="210" y1="196" x2="235" y2="248" stroke="#000" stroke-width="3"/>
  <ellipse cx="235" cy="250" rx="22" ry="6" fill="#c60"/>
  <text x="248" y="262" fill="#c60">P-S / P-I pads (+45, ±70), Z −52</text>
  <!-- dimensions -->
  <line x1="122" y1="60" x2="190" y2="60" stroke="#900"/>
  <text x="140" y="56" fill="#900">68</text>
  <line x1="110" y1="275" x2="235" y2="275" stroke="#900"/>
  <text x="160" y="286" fill="#900">125 (rear pad to front-pad line)</text>
  <line x1="380" y1="112" x2="380" y2="196" stroke="#900"/>
  <text x="383" y="158" fill="#900">84</text>
  <line x1="400" y1="112" x2="400" y2="243" stroke="#900"/>
  <text x="403" y="200" fill="#900">~130 to pads</text>
  <!-- strap -->
  <path d="M 240 252 Q 290 300 300 318" fill="none" stroke="#393" stroke-dasharray="4 2"/>
  <path d="M 112 246 Q 170 300 300 318" fill="none" stroke="#393" stroke-dasharray="4 2"/>
  <text x="250" y="312" fill="#393">Y-strap to chin</text>
</svg>

### 1.4 Front view (YZ), looking along −X from the front, 1 px = 1 mm
<svg viewBox="0 0 420 300" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="9">
  <!-- frame: x = Y + 210, y = 180 - Z -->
  <path d="M 110 280 A 100 110 0 0 1 310 280" fill="none" stroke="#999" stroke-width="1.5"/>
  <text x="300" y="292" fill="#999">head (≈150 wide)</text>
  <!-- hub tube behind -->
  <line x1="80" y1="96" x2="325" y2="96" stroke="#333" stroke-width="6"/>
  <text x="300" y="88" fill="#333">hub tube</text>
  <!-- servo -->
  <rect x="83" y="72" width="26" height="34" fill="#444"/>
  <text x="40" y="70" fill="#444">XL330 Y −127…−101</text>
  <!-- idler -->
  <rect x="311" y="86" width="10" height="20" fill="#444"/>
  <text x="300" y="120" fill="#444">idler</text>
  <!-- nodes -->
  <rect x="78" y="60" width="38" height="60" fill="none" stroke="#555" stroke-dasharray="2 2"/>
  <rect x="304" y="60" width="30" height="60" fill="none" stroke="#555" stroke-dasharray="2 2"/>
  <!-- cheeks -->
  <rect x="112" y="76" width="5" height="40" fill="#06c"/>
  <rect x="303" y="76" width="5" height="40" fill="#06c"/>
  <!-- crossbar -->
  <rect x="112" y="84" width="196" height="16" fill="none" stroke="#06c"/>
  <!-- palm -->
  <rect x="122" y="114" width="169" height="28" fill="none" stroke="#06c"/>
  <text x="180" y="110" fill="#06c">palm Y −88…+81</text>
  <!-- knuckle plate -->
  <path d="M 165 146 Q 210 138 255 146" fill="none" stroke="#06c" stroke-width="2"/>
  <!-- nails -->
  <line x1="186" y1="146" x2="186" y2="184" stroke="#06c" stroke-width="2"/>
  <line x1="210" y1="146" x2="210" y2="180" stroke="#06c" stroke-width="2"/>
  <line x1="234" y1="146" x2="234" y2="184" stroke="#06c" stroke-width="2"/>
  <text x="170" y="196" fill="#06c">nails Y −24, 0, +24</text>
  <!-- side legs -->
  <line x1="102" y1="120" x2="102" y2="180" stroke="#000" stroke-width="3"/>
  <line x1="102" y1="180" x2="140" y2="232" stroke="#000" stroke-width="3"/>
  <line x1="318" y1="120" x2="318" y2="180" stroke="#000" stroke-width="3"/>
  <line x1="318" y1="180" x2="280" y2="232" stroke="#000" stroke-width="3"/>
  <ellipse cx="140" cy="234" rx="22" ry="7" fill="#c60"/>
  <ellipse cx="280" cy="234" rx="22" ry="7" fill="#c60"/>
  <text x="60" y="252" fill="#c60">pads Ø45 at Y ±70, Z −52</text>
  <!-- rear pad hidden -->
  <ellipse cx="210" cy="225" rx="22" ry="7" fill="none" stroke="#c60" stroke-dasharray="3 2"/>
  <text x="222" y="222" fill="#c60">P-R (hidden)</text>
  <!-- dims -->
  <line x1="102" y1="40" x2="318" y2="40" stroke="#900"/>
  <text x="180" y="36" fill="#900">216 (leg verticals, |Y| 108)</text>
  <line x1="140" y1="262" x2="280" y2="262" stroke="#900"/>
  <text x="195" y="274" fill="#900">140</text>
  <line x1="380" y1="96" x2="380" y2="184" stroke="#900"/>
  <text x="383" y="140" fill="#900">84</text>
  <!-- ear canal marker -->
  <circle cx="135" cy="300" r="3" fill="none" stroke="#393"/>
  <text x="60" y="296" fill="#393">ear canal ≈ Z −120</text>
  <!-- strap -->
  <path d="M 140 240 Q 120 290 150 298" fill="none" stroke="#393" stroke-dasharray="4 2"/>
  <path d="M 280 240 Q 300 290 270 298" fill="none" stroke="#393" stroke-dasharray="4 2"/>
</svg>

**Module position** is unchanged from the freeze: elbow axis at Z +84 above the scalp apex, nails at Z 0, L_max = 84 mm, swept envelope within R 91 of the axis. The lowest fixed structure above the scalp patch is the node underside at Z +50; the lowest moving part is the nail. Nothing fixed is above the hand within its swept volume (the hub is behind it), so the arm's upward sweep has no ceiling to hit.

---

## 2. Force reference

**Nail force is the floating dead weight, not the seating.** The hand hangs on the MGN9 float (mech §6), which is free between its up-stop and down-stop. Wherever the cap seats, the carriage simply rides to a different point on the rail; the normal force on the scalp is W = 0.88 / 1.18 / 1.47 N (W1/W2/W3) shared 0.8 : 1.0 : 1.2 by the leaves, ± the 0.03 N float stiction (mech §6.8), independent of the structure's position as long as the carriage is off both stops. Seating variation of ±3–5 mm (hair pile, pad settling, a different spot on the head) is 3–5 mm of carriage position, nothing else. This is exactly Judge 2's F1 argument in reverse: the head-worn designs that lost used the strap as the force reference (k × depth); here the strap carries no force path to the nails at all, only the dead weight does.

**Float travel required.** With e = 4 mm the carriage has 24 mm of up-travel and 4 mm of down-travel to the free-tip position (mech §6.3). Demands on it, summed in the worst direction:

| Source | Travel |
|---|---|
| Stroke arc rise (4.1 mm arm arc + 3.6 mm sphere drop at ±18°, RT2 §1) | 7.7 mm |
| Seating variation (pads on pile, reseat scatter) | ±5 mm |
| Pad settling into hair over 20 min (§9 risk 2) | 0–3 mm (cap sinks, carriage rises) |
| Head-shape mismatch under the patch (R 75–110 vs R 90) | ±2 mm |
| Breathing / posture drift | **0** — the cap moves with the head |
| Total up-travel needed | ≤ 18 mm against 24 mm available |

The breathing row is the structural advantage over the stand: mech §10.1 budgets 5–15 mm of drift at the face cradle for the stand's float; the cap's float never sees it. Legs set 5 mm short: the free tip is 9 mm into the sphere, the carriage floats with 19 mm spare. Legs 5 mm long: e = −1 mm, nails touch only through leaf travel, obvious and fixed with the gauge. The D10 failure (carriage on the up-stop, 9 N) needs the cap to sink 24 mm relative to the patch: impossible on a 5–20 mm pile already pressed flat, and a head rise lifts the cap with it. **The up-stop is unreachable in normal use; D10 is retired by geometry.**

**Head tilt.** Tilt the head and cap by φ fore-aft: the dead weight's component along the rail is W cos φ; W sin φ is carried by the carriage against the rail, never by the scalp. Nail force = W cos φ: −1.5 % at 10°, −6 % at 20°, −13 % at 30°. Sideways tilt is the same cosine with W sin φ as a side load on the block (rated in tens of newtons; the leaves are stiff in Y); the added rail friction is 0.005 N at 20°. **Tilt limit: 20° of the pad plane from level in any direction** (force within −6 %; the strap-free tip-over margin in §3 is 17.5°, so beyond 15° the strap is doing the holding). Practice: crown = head level ±10°; upper occiput = lean forward 40–60° over a desk or face cradle, seat the cap with its pad plane level (a 10 mm bubble level is glued to the hub clamp).

---

## 3. Stability on the skull

**Loads trying to move the cap**
- Servo reaction torque, 0.1 N·m peak at 1–3 Hz, about Y (the elbow axis), applied to the hub. It peaks at the stroke ends (acceleration) where the nails are lifted.
- Hand drag, ≤ 1.2 N by the firmware current limit (freeze §1.10), 1.5 N bounding, along ±X at the scalp. Reacted through the rail and yoke at the elbow axis, Z +84, i.e. 134 mm above the pad plane (Z ≈ −50). Moment on the cap about Y: 1.5 × 0.134 = **0.20 N·m**. Peaks at mid-stroke (peak velocity) where the servo torque is near zero: the two are in quadrature, so the bound is 0.20 + a fraction of 0.10, taken as **0.25 N·m**.
- Arm gravity shift: the arm's ≈ 250 g (hand, float, mast, rail, crossbar) moves its CoM ≈ ±15 mm in X over ±25°: ±0.037 N·m at the stroke frequency. Included in the 0.25.
- Cap inertia on a head jerk: 0.44 kg × 2.25 m/s² (20 mm at 0.3 m/s) = 1.0 N, once.

**Holding moments from gravity alone (no strap).** Cap 442 g = 4.34 N, CoM at X +9 (§4). Pad loads: rear 0.288 × 4.34 = 1.25 N; each front pad 1.55 N. Pitch nose-down (front pads load, rear pad unloads) is resisted until the rear pad lifts: 1.25 N × 0.125 m = **0.156 N·m**. Pitch nose-up: 3.1 N × 0.125 = 0.39 N·m. Sliding in X: µ × 4.34 = 1.3 N (µ 0.3) to 2.2 N (µ 0.5). Against 0.25 N·m and 1.5 N: **margin 0.6× in pitch and 0.9× in sliding at µ 0.3 — fails. A loose cap rocks on its rear pad at every stroke. The strap is not optional.**

**Y-strap.** Per side, a 20 mm elastic runs from a loop boss on the side-pad stem (30 mm above the pad face, X +45, Z −20) down in front of the ear to the chin, where a magnetic buckle joins the sides; a second strand runs from the chin back and up to a boss on the rear leg 30 mm above its pad. Tension **T = 2.5 N per side** (≈ 250 gf; a snug bicycle-helmet strap is 5–10 N). The front strands add ≈ 2.3 N to each front pad, the rear strands at ≈ 45° add ≈ 1.8 N to the rear pad: rear 3.0 N, fronts 3.9 N each, total 10.8 N.

| Disturbance | Bound | Holding capacity with strap | Margin |
|---|---|---|---|
| Pitch nose-down (rear pad lift) | 0.25 N·m | 3.0 N × 0.125 m = 0.38 N·m | **1.5×** |
| Pitch nose-up (front pads lift) | 0.25 N·m | 7.8 N × 0.125 m = 0.98 N·m | 3.9× |
| Slide in X (drag) | 1.5 N | µ 0.3 × 10.8 N = 3.2 N (µ 0.4: 4.3 N) | 2.2× (2.9×) |
| Yaw about Z (one nail on bare skin, 0.4 N × 24 mm) | 0.01 N·m | 3 pads × 0.3 × 3.6 N × 0.07 m = 0.23 N·m | 23× |
| Head jerk, cap inertia | 1.0 N | 3.2 N | 3.2× |
| Roll about X (side pads at ±70, arm gravity ±0.02 N·m) | 0.02 N·m | 3.9 N × 0.07 = 0.27 N·m | 13× |

**Breakaway (red line 10).** Two independent releases: (1) a Fidlock-type magnetic buckle (20 mm V-buckle class): one finger slides it sideways, < 1 s, eyes closed; (2) the strap is elastic (≈ 0.02 N/mm, 120 mm stretch at 2.5 N), so pulling the cap straight up stretches it off the chin at ≈ 6 N without touching the buckle, well under the safety doc's < 20 N. The front strand leaves the stem at X +45; the ear canal is at X ≈ 0, Z −120, so the strand passes ≥ 35 mm in front of the tragus.

**Jaw motion.** Talking and swallowing move the chin point 2–5 mm: ΔT = 0.04–0.10 N (±4 %), pad loads change < 0.1 N, the pad stack (TPU ≈ 3 N/mm on pile ≈ 1 N/mm) moves 0.03–0.1 mm. The cap does not measurably move, and a full millimetre would leave the float 23 mm to spare (§2). A webbing strap (> 1 N/mm) would turn every swallow into a 2–5 N tug, one reason the head-worn tournament entries drifted; the elastic is what makes jaw motion a non-event.

---

## 4. Mass budget

**Module as engineered (mech §3.1), with two cuts**

| Part | g | Note |
|---|---|---|
| XL330 + cradle P13 + strap P14 + screws | 41 | reused |
| Idler: 625-2RS, housing P15, shoulder screw, horn disc P16 | 33 | reused |
| Yoke cheeks P19/P20 | 30 | reused |
| Crossbar + mast P21 | 45 | reused |
| MGN9 rail, stops, thumbscrews, scale, cleat | 64 → **48** | **cut 1: rail 100 → 70 mm** (−11 g; 28 mm travel + 29 mm block + 2 stops = 61 mm needed), scale strip and trim cleat left off (−5 g; e is set by the gauge) |
| Rail shroud P22 | 15 → **10** | cut 2: 1.2 mm walls, 3 perimeters; still closed-bottom |
| Float: carriage, riser, wrist, palm, leaves, paddles, tips | 92 | W1 90.1 g + tether etc. |
| Guard caps P17/P18 | 16 | reused |
| DXL cable on the head (0.4 m) and clips | 10 | |
| **Module subtotal** | **325** | |

**Structure (new)**

| Part | g |
|---|---|
| Hub tube, 10 × 8 mm pultruded CF, 250 mm (28 mm² × 1.55 g/cm³) | 11 |
| Node N-S (PETG, 48 × 36 × 60, 4 perimeters, 30 %) | 14 |
| Node N-I | 12 |
| Rear-leg clamp on the hub tube | 6 |
| Side legs: 8 × 6 CF tube 150 mm (5 g) + printed bend/stem (4 g) + adjuster thumbscrew (3 g), × 2 | 24 |
| Rear leg: 10 × 8 CF tube 125 mm (5.5 g) + stem (4 g) + thumbscrew (3 g) | 12 |
| Pads, TPU 95A Ø 45 dome, × 3 | 18 |
| Y-strap: 20 mm elastic 2 × 450 mm + 2 × 200 mm, magnetic buckle, 3 loop bosses | 20 |
| Bubble level, fasteners, adhesive | 6 |
| **Structure subtotal** | **123** |

**Head-borne total: 448 g at W1 (call it 442–450 g); 478 g with the +30 g slug; 508 g with +60 g.** Red line 10 is 500 g, so **W3 is not allowed on the head as built**; W1 and W2 are. Lightening list: crossbar box beam → 10 × 8 CF tube with printed ends (−22 g), cheeks 4 mm at 20 % infill (−8 g), MGN7 rail and block (−12 g, mech §6.5 fallback), nodes at 20 % infill (−6 g), TPU 85A pads at 2 mm (−5 g): **−53 g → 395 g bare, 455 g with W3.** Below 350 g needs a lighter hand (60 g of the 92 g float), which the brief forbids. I report 442 g and claim ≤ 400 g after the list.

**Centre of mass** (module parts at their mech §2 positions): **X +9, Y −2, Z +64 mm**, 114 mm above the pad plane. Load share at rest: rear 29 %, each side 35.5 % (servo side 2 % heavier). The tall CoM is the concept's structural weakness: strap-free tip-over is atan(36/114) = 17.5° forward, 21° diagonally rearward; the strap holds the cap to the 20° limit of §2 and beyond, but the number should be remembered when Michael nods.

**Comfort.** With the strap: 3.9 N per front pad, 3.0 N rear. A Ø 45 dome on flattened pile gives a contact patch ≈ Ø 36 mm = 10 cm²: **3.9 kPa front, 3.0 kPa rear**, under the 5 kPa / 37 mmHg sustained limit (safety §2.2) by 22 %. A Ø 25 mm patch would be 8 kPa, so the face must conform (TPU 95A, 2.5 mm wall) and the 20-min wear test (§9) checks for blanching. Reposition every 20 min regardless. Chin: 5 N over a 20 × 60 mm cup = 4 kPa.

---

## 5. Coverage and repositioning

**Reach.** Any patch that faces up within 20° in the current posture and has hair-covered scalp under all three pads (≥ 25 mm behind the hairline, ≥ 25 mm above the ear canals, ≥ 20 mm above the nuchal hairline). Seated upright that is a zone ≈ 80 mm (X) × 50 mm (Y) around the vertex. Leaning forward 40–60° the same cap reseats on the **upper occiput**; the rear pad then sits 80 mm below the target toward the nape, which limits occipital targets to ≥ 60 mm above the inion. **Lower occiput, nape, temples: no** (a pad would be on bare neck or over an ear).

**Region change = lift and reseat by hand**, servo off: release the buckle (or lift against the elastic), raise 40 mm, move, set down, re-click: 5–8 s. Direction change: the triangle turned 90° puts the rear pad over an ear, **not allowed**, so CROSS aims use the 45° reseat (rear pad on the parietal boss, 60 mm above the ear): 0° and ±45° aims, which is what the stand's Stage 1 offered by tape marks (ADD-1 ruling 8). Detents: none mechanical; the pads seat in the hair they flattened last time, and three pencil dots on the pad rims mark the aim.

**Back of the head leaning forward over a desk:** yes, the upper occiput, forehead on folded arms or the SEAT face cradle (mech §10.1), head flexed 40°, hub tube toward the nape, cable leaving downward. The face cradle stays in the BOM; the isolation baseboard (§10.2) goes, since nothing couples to the desk.

---

## 6. Safety

**Donning / doffing.** Don: hold the hub tube in one hand, lower until three pads touch, swing the strap under the chin, click the magnetic buckle (it self-finds): 5 s, one hand. Doff: thumb slides the buckle sideways (< 1 s) and the same hand lifts the hub 50 mm; the nails leave the scalp with the cap because the hand is captive on the rail: **≤ 3 s, one hand, eyes closed** (safety §3.9, red line 10). Fastest exit of all: grab anything and lift — the elastic stretches off the chin at ≈ 6 N. The cap, lifted, weighs 0.45 kg: trivial.

**Power loss, e-stop, watchdog, stall.** The actuator rail (freeze §1.10) is unchanged: E-STOP (NC) → HOLD-TO-RUN → XL330 VIN. Opening it torques the servo off. There is no electromagnet and no spring lift on the cap, so the de-energised state is **limp**: the arm stops where it is (the XL330's unpowered back-drive torque, 0.02–0.05 N·m, roughly equals the top-heavy arm's gravity moment, mech §5.3 and RT2 §6, so it neither falls nor lifts), and the nails rest at the dead weight W ≤ 1.5 N, or are already lifted if the stroke was beyond ±18°.

Argument against red line 8 and RT2 §8. The red line allows "lifted-off **or limp**". RT2 ruled LIFTED for the monitor-arm crown configuration on three grounds:
1. *"The reflexive exit moves the head into a limp hand."* On the stand, lifting the forehead off the pad extends the neck and drives the crown 15–25 mm into a desk-fixed hand (RT2 §5). On the cap the hand is referenced to the head: neck extension carries the hand with the scalp; the only relative motion is the float's inertia lag (2–3 mm, 0.2–0.9 N transient) against 24 mm of up-travel. **The flinch-into-the-hand mechanism does not exist here**, the strongest safety argument for the concept.
2. *"A stopped stroke leaves a trapped strand loaded."* True here too: ≤ µW ≈ 0.3–0.65 N on a strand (RT2 H1) until the user lifts the cap, 1–3 s, against H-5.9's 100 ms. Firmware snag reflex and hold-to-run are unchanged. Residual: one plucked hair in that window on a power loss during a snag; I rate it S1 and accept it for SP1. If the Safety Gate does not, the fallback is RT2 §8's latch on the float carriage (20 mm electromagnet, 30 g, holding the carriage down against a 2.5 N spring that lifts it to the up-stop on rail loss): +45 g on the head (487 g bare, W2 only) and 1.1 W of heat 60 mm above the scalp. A gate decision, not a default.
3. *"The limp state is indeterminate."* Here the hand is already on the head at W, or lifted beyond ±18°; a few degrees of arm drift changes nothing. Determinate: force ≤ W at all times after a fault, for as long as it takes the user to lift 0.45 kg.

**Flinch / head jerk ±20 mm at 0.3 m/s (RT2 §3).** The cap follows the head by pad friction and strap (3.2 N available against 1.0 N inertial). The float decouples the hand (0.9 N to accelerate 100–150 g over 5 mm, within 24 mm of travel); nothing rigid is in the path in any direction, because the structure the hand could hit moves with the head. Sideways jerk: as on the stand (leaves stiff in Y, 2 N wrist breakaway), no worse.

**E-stop and hold-to-run** stay on the desk box (P37–P40, unchanged); the button is in the free hand, the other hand is the lift, as for the stand.

**Ears and eyes.** Lowest moving part: the nails, ≥ 100 mm from either ear canal (≈ 120 mm below the crown plane, mech §10.3). Side-leg verticals end at Z 0, 70 mm above and 108 mm lateral to the canals; the pads at Z −52 are 68 mm above them. Nothing moving is anterior to the hairline (the static front pads at X +45 are ≥ 55 mm behind it); nothing is above the eyes. On the occiput seat the arm swings over the nape, ≥ 25 mm from the ears.

**Cable.** The single DXL cable (Ø 3 mm) leaves the servo downward with its 60 mm service loop, clips to N-S, runs along the hub tube to the rear-leg clamp and leaves at the tube's rear, down the back with 300 mm of slack to a collar clip, then to the desk box. It never crosses the float, never comes within 30 mm of the scalp, never passes an ear; its pull is < 0.1 N rearward, and a yank drags the cap backward against the front strands, never toward the face.

---

## 7. Noise

The path is servo → cradle → node → leg → pad → skull: bone conduction, which the stand did not have. Three things keep it under the 60 dBA target:
1. **Pad isolation.** Three TPU 95A domes at ≈ 3 N/mm each on flattened pile (≈ 1 N/mm) give a cap-on-head stack stiffness of about 2.2 N/mm per pad, 6.7 N/mm total, under 0.45 kg: f_n ≈ (1/2π)√(6700/0.45) ≈ **19 Hz**. XL330 gear noise is 200–2000 Hz, so the transmissibility is ≈ (19/f)², −20 dB at 200 Hz and −40 dB at 2 kHz on paper; call it −15 dB in practice because the strap shorts part of the path.
2. **Cradle isolation.** Mount P13 to the node through four TPU 85A grommets (Ø 8 × 4 mm, M3 through) instead of hard on the flange: a second stage at ≈ 60 Hz for the 41 g cradle mass; costs 2 g and 0.3 mm of servo compliance, which the yoke alignment absorbs (the idler side stays hard so the axis is defined).
3. **Airborne path.** The XL330 at Y −115 is ≈ 200 mm from the near ear canal; at 45–50 dBA at 0.3 m it is ≈ 50–53 dBA at the ear, inside the target.

What cannot be removed: the 1–3 Hz stroke reaction is felt as a gentle rocking of the cap, the rhythm of the stroke; the sensation gate must say whether it helps or kills the illusion. Bench test in §9 risk 4.

---

## 8. Build

**Printed parts (new).** PETG unless stated, 0.2 mm layers.

| # | Part | Qty | Size (mm) | Features |
|---|---|---|---|---|
| C1 | Node N-S | 1 | 48 × 36 × 60 | Ø 10.2 slit bore + M3 clamp for the hub tube; cradle flange copying P11's 4 × M3 foot pattern (inserts); 4 TPU grommet seats; Ø 8.2 × 25 leg socket with M3 thumbscrew insert; cable clip boss |
| C2 | Node N-I | 1 | 40 × 36 × 60 | mirror; P15's 2 × M3 slot pattern (hard-mounted); Ø 8.2 leg socket |
| C3 | Rear-leg clamp | 1 | 24 × 20 × 30 | Ø 10.2 slit clamp on the hub tube, Ø 10.2 × 20 vertical socket + thumbscrew; bubble-level seat; cable exit saddle |
| C4 | Side-leg bend and stem | 2 (mirrored) | 60 × 40 × 55 | Ø 8.2 socket at the top, 35° bend, stem drafting Ø 12 → 18 over 30 mm, strap loop boss 30 mm above the pad face, 1 mm fillets everywhere |
| C5 | Rear stem | 1 | Ø 18 × 45 | Ø 10.2 socket, same drafted stem and loop boss |
| C6 | Pad | 3 | Ø 45 × 12 | TPU 95A dome shell 2.5 mm, rim R 8, face printed down and ironed, stem pocket Ø 18 × 5 |
| C7 | Chin cup | 1 | 60 × 25 × 3 | TPU 95A, two strap slots |
| C8 | Cable clips | 3 | 12 × 10 × 8 | P36 geometry, re-cut for a Ø 10 tube snap |

**Bought (new).** 10 × 8 mm pultruded CF tube 500 mm, $9; 8 × 6 mm CF tube 500 mm, $7; 20 mm elastic webbing 2 m, $4; magnetic breakaway buckle 20 mm (Fidlock V-buckle or equivalent helmet magnetic buckle), $8–14; 4 × M3 × 16 knurled thumbscrews, $3; TPU grommets (print, TPU on hand); epoxy (have). **Total new parts ≈ $38.**

**Deleted vs the stand (bom.md §2 and mech §12):** monitor arm $36, 2020 extrusion and bracket kit ≈ $30, ballast plates $54 (SendCutSend) or $45, hinge springs $16, electromagnet + keeper ≈ $10, 623ZZ pulleys/bearings and cord ≈ $8, M6 hinge pin set ≈ $3, isolation feet and baseboard ≈ $20, P1–P12 and P41–P45 prints ≈ 0.35 kg PETG ≈ $8. **≈ $160–185 deleted.** Net vs the stand: **−$120 to −$150**. Cost delta vs the hand module alone: +$38 (the module's own parts, including the rail now shortened, are the same money).

**Servo mounting (Director's verified XL330-M288-T facts, bom-verified.md §11).** The XL330 has **no side mounting holes**; it has 4 × Ø 1.6 holes on a 16 × 30 mm pattern on the horn-end face and on the back face, the output axis is 9.5 mm from the horn-end face, and the horn is Ø 16 with M2 × 6 screws on a Ø 12 PCD. Connectors are on the 23 × 34 mm side faces. Consequence: P13's "2 × M2 into the servo's side holes" (mech §5.3) does not exist; **P13 is re-cut so the servo is screwed through its back face**, 4 × M2 × 6 thread-forming into the Ø 1.6 holes on the 16 × 30 pattern, with side-wall cut-outs for the connectors and the strap P14 kept as a backup. The pocket is referenced to the output axis at 9.5 mm (not 10) from the horn face, moving the pocket floor 0.5 mm. P16's pattern is 4 × M2 on Ø 12 PCD. None of this touches the node interface. **Supply:** the XL330 is on a two-month back-order at robotis.us; ROBOTIS Korea ships by DHL in about a week, so order there first or the servo gates the build.

**Hours.** Modelling the nodes and stems in gen_frame_stl.py (reusing `xl330_pocket`, the `_drop_leg` foot flange and `ins_z`): 3 h. Printing ≈ 7 h unattended. Tubes, bonding, assembly, node alignment with the zero pin: 2 h. Fit on the foam head, leg setting with P43, strap trimming: 1 h. **≈ 6 h hands-on**, against ≈ 10 h for the stand's adapter, hinge, springs, magnet and ballast (mech §13, P1–P12).

**Reusable from cad/frame/stl:** p13 (after the back-face re-cut), p14–p20, p21/p22 (shortened for the 70 mm rail, one line), p23, p24, p26, p28–p35, p36 (re-cut), p37–p40, p43, p46–p48. **Deleted:** p01–p12, p25, p27, p41, p42, p44, p45. cad/tips unchanged.

---

## 9. Top five risks and the bench tests that retire them

| # | Risk | Why it is credible | Bench test (mannequin head with a 5–8 cm wig, servo running) | Pass |
|---|---|---|---|---|
| 1 | **The cap rocks or creeps under stroke reaction** (rear pad lifting, sliding in X), the hand walks off the patch | §3: without the strap the pitch margin is 0.6×; with it 1.5×, on an assumed µ 0.3 and a 134 mm lever | Drag test: fish scale on the centre paddle's seam sleeve (P46) to 1.5 N in ±X with the strap at 2.5 N per side: no pad lifts, no slip. Then PERIODIC at 3 Hz, W2, 5 min, a laser pointer on the hub projecting on a wall at 2 m: drift < 1 mm on the head (< 2 mm on the wall per mm) | ≤ 1 mm creep in 5 min; no visible rock on 240 fps video |
| 2 | **Pads settle into the hair pile** over 20 min; the cap sinks, engagement grows, and on long hair the knuckle plate reaches the pile (RT2 §5's silent force loss in reverse) | pile 5–20 mm compresses under 3–4 N | 20-min run, carriage scale reading every 2 min against the apex gauge | sink ≤ 3 mm; knuckle plate ≥ 10 mm above the flattened pile |
| 3 | **Mass over 500 g with slugs** (printed masses scatter ±10 %; the 346 g module figure is itself a design estimate) | §4 lands at 442 g bare, 508 g with W3 | Kitchen scale on the assembled cap at each slug setting before the first human session; the allowed slug set is 500 g minus the measured bare mass | bare ≤ 450 g; W2 allowed; W3 only after the §4 lightening list |
| 4 | **Bone-conducted servo noise and the felt rocking destroy the fingernail illusion** (Judge 1's lens; the stand had no bone path) | §7 isolation is an estimate; the strap bypasses the pads | Contact microphone inside the mannequin skull, PERIODIC 2 Hz, cap vs module-on-stand; then Michael's 1-min wear with nails lifted and the servo running | ≤ 60 dBA-equivalent; rhythm rated "not intrusive" or better |
| 5 | **Tilt and head-shape mismatch**: force ∝ cos φ and the pad triangle on a non-spherical head leaves one pad light, so the cap rocks on two pads | the sphere model exaggerates the drop at r = 80; real heads are flatter and asymmetric | Tilt test: mannequin on a tilting board at 0°, ±10°, ±20° fore-aft and sideways, scale under a scalp patch reading nail force at W2; three-pad load check with 1 mm shim paper under each pad | force within −6 % at 20°; every pad loaded ≥ 0.8 N at rest after leg adjustment |

Also carried: leg hair-safety (wig entanglement test, hair-interaction §7.3, with the legs on); node coaxiality (free-swing with the zero pin); chin-strap comfort over 20 min (servo off); the buckle's breakaway (≤ 20 N straight, ≤ 3 N sideways).

---

## 10. Verdict

For SP1 as a sensation experiment the Tripod Cap beats the monitor-arm stand on what was wrong with the stand: $120–150 cheaper, no desk clamp, ballast or 1.1 kg frame, head-worn in form so the Stage-1 answer transfers to the product, and a force reference as good as the stand's, arguably better, because the float no longer absorbs breathing drift and the D10 up-stop case cannot happen. It also removes the red team's worst crown finding, the flinch into a desk-fixed hand. The price is real: 442 g on the head, a 5 N chin strap, servo noise by bone conduction, a tall centre of mass that is only a structure with the strap on, no 100 ms fail-safe lift (limp at W, §6), and a user feeling an apparatus on his head while being asked whether it feels like fingernails. I would choose the stand after all if the Safety Gate rejects "limp" and the +45 g latch pushes the mass past 500 g with the slugs the experiment needs; if the bone-conduction test puts a tonal whine in Michael's skull that the sensation gate cannot ignore; or if the pads cannot be made comfortable for 20 min on his hair. Build the cap first and keep the stand's drawings: every part on the cap is the stand's module, so the stand is a 10-hour fallback, not a redesign.
