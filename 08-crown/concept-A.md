# CONCEPT A — THE RING CROWN

**Project SCRATCH · 08-crown · 2026-10-01 · Crown concept team A.** Builds to 08-crown/CROWN-BRIEF.md and the director's chin-strap note. Inherits DESIGN-FREEZE.md + ADDENDUM-1 (D1–D13, rulings 1–8), mechanical.md ("mech §x"), safety-requirements.md ("safety", red lines RL-n), hair-interaction.md ("H-x.y"), judge-2 §0 (F1/F3/F5), redteam-2 ("RT2 §x"). Numbers I chose are marked **[CHOICE]**; estimates without a source **[EST]**; items to check on the bench **[TEST]**. Director's verified XL330 facts (bom-verified.md §11) are applied in §8.

**One sentence.** A 15.9 × 1.6 mm aluminium hoop (inner 212 × 172 mm, ratchet-adjustable) rests on the skull just above the hairline through four TPU-and-foam feet; a carbon-tube portal clamped to the hoop's straight sides carries the hand module's elbow axis 130 mm above it at Z +84; the hand floats inside on its own dead weight, so the hoop's seating does not set the nail force; a 1.5 N elastic chin strap with a 12 N magnetic fuse retains the crown; a spring lift on the float, held down by a micro electromagnet on the actuator rail, lifts the nails 25 mm on any loss of power.

**Headline numbers.** On-head mass 429 g at W1 (0.9 N), 459 g at W2 (1.2 N), 489 g at W3 (only after weighing: RL-10 margin 11 g). The brief's "module ≈ 150–200 g" is not what mech §3.1 adds up to: servo + idler + yoke + rail + float + guards are 346 g in that ledger, 253 g after the trims in §4. The 350 g target is not reachable with this hand module; 430–460 g is.

---

## 1. Geometry

### 1.1 Layout in words

Frame as frozen (D9): Z up, X stroke, Y pitch, origin at the centre nail edge at mid-stroke; scalp sphere R 90 mm centred (0, 0, −86), apex Z +4; elbow axis at Z +84 (H = 80). The crown adds:

- **Hoop.** Aluminium flat bar 15.9 × 1.6 mm (5/8 × 1/16 in), bent on a plywood form to a stadium-ellipse: straight parallel sides at Y ±86 from X −70 to +10, elliptical front (semi-axis 96 in X) and rear (36); inner perimeter 646 mm, bounding box 212 × 172 mm, band plane **Z −46** (50 mm below the apex), band Z −54 to −38. The form is cut to Michael's hat-line circumference + 50 mm (pads stand 8 mm in); the rear ratchet gives −24 mm of perimeter. Heat-shrink sleeved (RL-11), 49 g.
- **Four feet** (§1.4): forehead F, parietal L/R, upper-occiput O, faces tilted to the local skull slope (normal ≈ 60° from vertical [EST]).
- **Portal.** Two carbon tubes 10 × 8 mm (uprights, 140 mm) rising from the hoop's straight sides at X −30, Y ±100, joined by a 200 mm carbon cross tube at (X −30, Z +105) through two printed nodes: C1 (−Y) carries a plate screwed to the XL330's back face so the output axis sits at (0, 84), horn facing +Y; C2 (+Y) carries the 625-2RS idler bearing at Y +95 to +100. The portal is one rigid, jig-bonded gauge: servo-to-idler coaxiality never changes when it is moved.
- **Portal feet.** Each upright ends in a printed plug (C4) sliding inside the tube (telescoping, 1 mm marks, M3 thumbscrew) with a 36-tooth radial serration mating a hoop clamp (C5) locked by an M4 thumbscrew: pitch detents every 10° about Y, slide anywhere on the straight sides.
- **Hand module.** As engineered, with: cheeks at |Y| 88–92 (4 mm PETG), crossbar 176 mm (carbon tube + printed lugs replacing the P21 box beam), MGN7 100 mm rail (D7 fallback, −16 g; float re-trimmed to 90 g, W1 unchanged), down-stop at **E6** (L_max 86), 30 mm between stops. Servo body Y −98 to −121, horn −98 to −95, disc −95 to −92; idler +95 to +100.

### 1.2 Side view (XZ), ψ = 0°, head upright, nails in contact

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 430" width="520" font-family="sans-serif" font-size="7">
<g transform="translate(170,200) scale(1,-1)" stroke="#333" fill="none" stroke-width="1">
<!-- head -->
<path d="M -100,-215 L -98,-70 C -98,-20 -60,4 0,4 C 60,4 98,-20 98,-70 L 106,-118 L 100,-140 L 108,-168 L 92,-200 L 78,-226 L -60,-226 L -100,-215 Z" stroke="#555" stroke-width="1.2"/>
<circle cx="0" cy="-86" r="90" stroke="#999" stroke-dasharray="3,2"/>
<circle cx="0" cy="-86" r="120" stroke="#c66" stroke-dasharray="2,3" stroke-width="0.6"/>
<ellipse cx="90" cy="-118" rx="6" ry="3" stroke="#555"/>
<!-- hoop band (sides seen edge-on) -->
<rect x="-107.6" y="-54" width="215.2" height="16" fill="#dde" stroke="#669" opacity="0.8"/>
<!-- pads F and O -->
<rect x="96" y="-68" width="10" height="45" fill="#cfc" stroke="#393"/>
<rect x="-106" y="-68" width="10" height="45" fill="#cfc" stroke="#393"/>
<!-- portal clamp + foot plug + upright -->
<rect x="-40" y="-56" width="20" height="30" rx="3" fill="#fde" stroke="#936"/>
<circle cx="-30" cy="-30" r="5" fill="#fff" stroke="#936"/>
<rect x="-35" y="-25" width="10" height="125" fill="#eee" stroke="#333"/>
<rect x="-38" y="96" width="50" height="16" rx="3" fill="#fde" stroke="#936"/>
<circle cx="-30" cy="105" r="5" fill="#fff" stroke="#333"/>
<!-- servo (behind yoke) and axis -->
<rect x="-10" y="74" width="20" height="34" fill="#ffd" stroke="#996"/>
<line x1="-6" y1="84" x2="6" y2="84"/><line x1="0" y1="78" x2="0" y2="90"/>
<circle cx="0" cy="84" r="91" stroke="#c66" stroke-dasharray="4,2" stroke-width="0.6"/>
<!-- yoke cheek, crossbar, mast, rail, carriage -->
<rect x="-12" y="64" width="69" height="40" rx="4" stroke="#333"/>
<circle cx="51" cy="88" r="5" fill="#eee"/>
<rect x="40" y="64" width="5" height="110" fill="#ddd"/>
<rect x="33.5" y="68" width="6.5" height="100" fill="#bbb"/>
<rect x="30" y="79" width="10" height="29" fill="#888"/>
<rect x="0" y="77" width="30" height="4" fill="#888"/>
<rect x="-22" y="74" width="44" height="5" fill="#aaa"/>
<rect x="-4" y="79" width="8" height="34" fill="#aaa"/>
<!-- lift latch on mast -->
<rect x="45" y="60" width="10" height="10" fill="#fcc" stroke="#933"/>
<line x1="45" y1="70" x2="30" y2="76" stroke="#933"/>
<!-- hand: palm, knuckle plate, paddles, tips on scalp -->
<rect x="-26" y="42" width="52" height="32" rx="2" fill="#eef" stroke="#336"/>
<path d="M -32,37 Q 0,45 32,37" stroke="#336" stroke-width="1.5"/>
<path d="M -14,38 L -2,38 L -5,4 L -11,4 Z M -6,40 L 6,40 L 3,4 L -3,4 Z M 2,38 L 14,38 L 11,4 L 5,4 Z" fill="#dde" stroke="#336"/>
<!-- dimension lines -->
<line x1="70" y1="4" x2="70" y2="84" stroke="#06c"/><line x1="66" y1="4" x2="74" y2="4" stroke="#06c"/><line x1="66" y1="84" x2="74" y2="84" stroke="#06c"/>
<line x1="-60" y1="-46" x2="-60" y2="84" stroke="#06c"/><line x1="-64" y1="-46" x2="-56" y2="-46" stroke="#06c"/><line x1="-64" y1="84" x2="-56" y2="84" stroke="#06c"/>
<line x1="-106" y1="-80" x2="106" y2="-80" stroke="#06c"/><line x1="-106" y1="-84" x2="-106" y2="-76" stroke="#06c"/><line x1="106" y1="-84" x2="106" y2="-76" stroke="#06c"/>
<line x1="120" y1="-68" x2="120" y2="-118" stroke="#06c"/><line x1="116" y1="-68" x2="124" y2="-68" stroke="#06c"/><line x1="116" y1="-118" x2="124" y2="-118" stroke="#06c"/>
<line x1="98" y1="-55" x2="112" y2="-55" stroke="#c33" stroke-width="1.5"/>
</g>
<g fill="#06c">
<text x="246" y="158">H = 80</text>
<text x="80" y="185">130 to axis</text>
<text x="128" y="276">hoop inner 212 (X)</text>
<text x="296" y="296">50 ≥ 25</text>
<text x="176" y="112">elbow axis Z +84</text>
<text x="100" y="86">cross tube X −30, Z +105</text>
<text x="118" y="236">pivot Z −30, 10° detents</text>
<text x="20" y="260">clamp X −30</text>
<text x="282" y="248">pad F 45×35×12</text>
<text x="24" y="248">pad O</text>
<text x="222" y="22">swept R 91 (dashed red)</text>
<text x="222" y="32">hair zone R 120 (dotted red)</text>
<text x="92" y="300">scalp sphere R 90, centre Z −86</text>
<text x="282" y="258" fill="#c33">hairline Z ≈ −55</text>
<text x="190" y="80">servo Z 74–108 (behind)</text>
<text x="246" y="58">mast / MGN7 rail</text>
<text x="190" y="140">latch</text>
<text x="200" y="174">E6: nails at Z +4</text>
</g>
</svg>

Side-view reads: the upright stands 130 mm above the band plane; the hoop's front is 106 mm ahead of the nails and 50 mm above the eye (RL-6: the leading tip at +25° is ≥ 60 mm behind the hairline at the most forward setting of §5); the cross tube is 7 mm clear of the palm's rear-top corner at θ = +28° on the up-stop (X −18, Z 105; mech §2 check a) and 13 mm above the cheeks **[TEST on the CAD solids]**; servo, bearing, cheeks and tube are above Z +60, ≥ 115 mm above the scalp at |Y| ≥ 88, outside the 30 mm hair zone (H-6.1). Inside it: tips, paddles, boot and knuckle plate as before, plus the **static** hoop, feet and clamps.

### 1.3 Front view (YZ)

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 430" width="520" font-family="sans-serif" font-size="7">
<g transform="translate(170,200) scale(1,-1)" stroke="#333" fill="none" stroke-width="1">
<path d="M -80,-200 L -79,-70 C -79,-20 -50,4 0,4 C 50,4 79,-20 79,-70 L 80,-200 C 60,-226 -60,-226 -80,-200 Z" stroke="#555" stroke-width="1.2"/>
<ellipse cx="-84" cy="-118" rx="9" ry="17" stroke="#555"/><ellipse cx="84" cy="-118" rx="9" ry="17" stroke="#555"/>
<circle cx="0" cy="-86" r="90" stroke="#999" stroke-dasharray="3,2"/>
<circle cx="0" cy="-86" r="120" stroke="#c66" stroke-dasharray="2,3" stroke-width="0.6"/>
<!-- hoop front section, side pads, front pad face-on -->
<rect x="-87.6" y="-54" width="175.2" height="16" fill="#dde" stroke="#669"/>
<rect x="-86" y="-68" width="10" height="45" fill="#cfc" stroke="#393"/><rect x="76" y="-68" width="10" height="45" fill="#cfc" stroke="#393"/>
<rect x="-17.5" y="-68" width="35" height="45" fill="none" stroke="#393" stroke-dasharray="2,2"/>
<!-- chin strap and fuse -->
<line x1="-88" y1="-46" x2="-8" y2="-226" stroke="#936" stroke-width="1.5"/><line x1="88" y1="-46" x2="8" y2="-226" stroke="#936" stroke-width="1.5"/>
<rect x="-9" y="-232" width="18" height="8" fill="#fde" stroke="#936"/>
<!-- portal -->
<rect x="-105" y="-25" width="10" height="125" fill="#eee"/><rect x="95" y="-25" width="10" height="125" fill="#eee"/>
<rect x="-110" y="100" width="220" height="10" rx="3" fill="#eee"/>
<rect x="-104" y="-56" width="12" height="30" rx="3" fill="#fde" stroke="#936"/><rect x="92" y="-56" width="12" height="30" rx="3" fill="#fde" stroke="#936"/>
<!-- servo side: back plate, body, horn, disc, cheek A; idler side -->
<rect x="-124" y="70" width="3" height="42" fill="#fde" stroke="#936"/>
<rect x="-121" y="74" width="23" height="34" fill="#ffd" stroke="#996"/>
<rect x="-98" y="76" width="3" height="16" fill="#996"/><rect x="-95" y="72" width="3" height="24" fill="#ccc"/>
<rect x="-92" y="64" width="4" height="40" fill="#ddd"/><rect x="88" y="64" width="4" height="40" fill="#ddd"/>
<rect x="95" y="76" width="5" height="16" fill="#ccc" stroke="#333"/><rect x="92" y="96" width="14" height="10" fill="#fde" stroke="#936"/>
<!-- guard caps -->
<path d="M -125,74 L -125,62 Q -110,58 -95,62 L -95,74" fill="#eef" stroke="#336"/><path d="M 95,74 L 95,62 Q 103,58 110,62 L 110,74" fill="#eef" stroke="#336"/>
<!-- yoke crossbar tube, mast, rail, carriage, seat, post -->
<rect x="-88" y="83" width="176" height="10" rx="5" fill="#eee"/>
<rect x="-12" y="64" width="24" height="110" fill="#ddd"/><rect x="-4.5" y="68" width="9" height="100" fill="#bbb"/>
<rect x="-22" y="74" width="44" height="5" fill="#aaa"/><rect x="-4" y="79" width="8" height="34" fill="#aaa"/>
<!-- hand -->
<rect x="-88" y="42" width="169" height="32" rx="2" fill="#eef" stroke="#336"/>
<path d="M -45,37 Q 0,45 45,37" stroke="#336" stroke-width="1.5"/>
<path d="M -32,37 L -16,37 L -20,1 L -28,1 Z M -8,38 L 8,38 L 4,4 L -4,4 Z M 16,37 L 32,37 L 28,1 L 20,1 Z" fill="#dde" stroke="#336"/>
<!-- dims -->
<line x1="-86" y1="-80" x2="86" y2="-80" stroke="#06c"/><line x1="-86" y1="-84" x2="-86" y2="-76" stroke="#06c"/><line x1="86" y1="-84" x2="86" y2="-76" stroke="#06c"/>
<line x1="-24" y1="-10" x2="24" y2="-10" stroke="#06c"/><line x1="-24" y1="-14" x2="-24" y2="-6" stroke="#06c"/><line x1="24" y1="-14" x2="24" y2="-6" stroke="#06c"/>
<line x1="130" y1="-68" x2="130" y2="-101" stroke="#06c"/><line x1="126" y1="-68" x2="134" y2="-68" stroke="#06c"/><line x1="126" y1="-101" x2="134" y2="-101" stroke="#06c"/>
</g>
<g fill="#06c">
<text x="124" y="276">hoop inner 172 (Y)</text>
<text x="138" y="222">pitch 24, nails L C R</text>
<text x="305" y="286">≥ 33 to ear</text>
<text x="4" y="112">servo back face Y −121</text>
<text x="4" y="122">plate C1 (4 × M2, 16 × 30)</text>
<text x="262" y="112">idler Y +95…+100</text>
<text x="262" y="122">cheek B Y +88…+92</text>
<text x="100" y="90">cross tube Y ±110, Z +105</text>
<text x="4" y="236">clamp C5 / plug C4</text>
<text x="262" y="236">pads L/R 45×35</text>
<text x="128" y="250">pad F (face-on, dashed)</text>
<text x="112" y="404">strap 1.5 N/side, fuse 12 N</text>
<text x="4" y="150">guard caps G2 / G3</text>
<text x="222" y="22">palm Y −88…+81</text>
<text x="222" y="32">uprights Y ±100 (carbon 10×8)</text>
</g>
</svg>

### 1.4 Where the structure touches the head

| Pad | Location | Surface | Size (contact × thickness) | Stack |
|---|---|---|---|---|
| F | forehead, 15–20 mm below the frontal hairline, centred on the mid-line, ≈ 45 mm above the brows | bare skin | 45 (Y) × 35 (Z) × 12 mm | PETG backing plate 3 mm on the hoop's inner face → TPU 85A block 12 mm, 20 % gyroid, face printed at the skull slope → 3 mm closed-cell PE foam (wipeable), self-adhesive |
| L, R | parietal bosses, ≥ 60 mm above the ear canals | hair | 45 (X) × 35 (Z) × 12 mm | same |
| O | upper occiput, ≥ 30 mm above the nuchal line, on the mid-line | hair | 45 × 35 × 12 mm | same |

Hoop stand-off from the skull 8 mm at the pads (10 mm compressed), 8–15 mm elsewhere: a static, sleeved, R ≥ 1 mm surface sitting in the hair like a hat band. Nothing on the crown rotates within 30 mm of the scalp: the pitch pivots are **clamped** joints with their serrations inside a closed, drafted housing with a 0.5 mm lip (no 40 µm–3 mm gap, H-4.9); the ratchet rack faces outward inside a closed sleeve over a smooth lapped overlap. Static gaps hoop-to-skull are ≥ 8 mm (not changing gaps). The hand's own clearances are mech §8.7's, unchanged.

**Module position.** Elbow axis (0, 0, +84) as frozen at ψ = 0; the portal plane at X −30 puts the uprights 30 mm behind the axis, node tops 21 mm above it. Nothing on the crown enters the swept envelope (R 91 about the axis): the cross tube is 36 mm from the axis, the uprights at |Y| 95–105 are 3 mm outboard of the cheeks, the clamps 110 mm below.

---

## 2. Force reference

**Claim.** Nail force = floating dead weight W (0.88 / 1.18 / 1.47 N for W1 / W2 / W3, shared 0.8 : 1.0 : 1.2 by the leaf rates, mech §8.3) for any crown seating between −28 mm (crown low) and +5 mm (crown high), independent of hoop tension, pad creep, jaw motion or strap tension, because none of those loads reaches the hand: the carriage rolls on the rail with 0.01–0.03 N of friction (mech §6.8), and the only force along the rail is gravity on the float.

**Seating variation.** Setting: E6 (down-stop at L_max = 86 mm) and the uprights telescoped so the apex sits at **H = 78 mm** (2 mm below the frozen 80, biasing the float toward mid-travel) **[CHOICE]**. At mid-stroke the leaves take δ = W/Σk = 1.96 / 2.62 / 3.27 mm (W1/W2/W3, Σk = 0.45 N/mm), so the carriage floats (6 + 2) − δ = **5.4 mm above its down-stop at W2** (6.0 at W1, 4.7 at W3). A crown seated high by s drops the carriage by s at force W until s = 5.4 mm; beyond that the nails lose contact (the safe direction, and the pointer shows it). A crown seated low raises the carriage, with 24.6 mm to the up-stop. The brief's ±3–5 mm is absorbed at exactly W (± the 0.05 N friction step at reversals); the tolerance is asymmetric, **−24.6 / +5.4 mm**. A larger E would widen the high side, but lift-off is geometric: each millimetre of E costs a millimetre of trailing-nail clearance at ±25° (mech §9.1: 5.7 mm at E4, 3.7 at E6, 1.7 at E8). E6 keeps every nail ≥ 3.7 mm clear at ±25° (7.1 at ±28°) with a 48 mm chord (half-angle 15.4°, outer nails to 20.6°), so HUMAN-mode strokes below ±21° reverse in contact on the trailing nail: the firmware's minimum amplitude on the crown becomes 21° **[CHOICE, flag to ELEC]**, band 21–25°, chord 55–68 mm. (The stand at E4 has the same issue below 13°.)

**Float travel required.** Seating ±5 mm + breathing and pad creep over 20 min 2–3 mm [EST] + stroke-profile float motion ≤ 2 mm (mech §6.9) + jaw/strap excursion ≤ 0.2 mm (§3.4) ≈ **8 mm**, against 30 mm available. The pointer must read 3–8 mm with the head upright at mid-stroke; this reading replaces the apex gauge as the session H check.

**Head tilt φ (any axis).** Force along the rail = W cos φ; W sin φ perpendicular to the rail goes into the yoke through the MGN7C block (side-load rating ≫ 10 N; added rolling friction ≤ 0.02 N). Per nail 0.87 W/3 at 30°, 0.71 W/3 at 45°. **Tilt limit ±30° working** (force −13 %, stability margin ≥ 1.1 at µ 0.3, §3), ±20° recommended for 20-minute sessions (−6 %, margin ≥ 1.4, neck +0.26 N·m). Beyond 30° the crown is re-aimed with the pitch detent (§5), not the neck: the 25° occiput detent with the head leaned 25° forward restores the full W. The 0.8 : 1.0 : 1.2 leaf shares are unchanged by tilt (all three leaves see the same δ).

**What the pads cannot do to the force.** Hoop tension and the crown's weight are reacted at the pads and in the hoop; the hand hangs on the rail and feels only its own weight. This is judge-2 F1 resolved for a head-worn frame: the strap is not the force reference.

---

## 3. Stability

### 3.1 Disturbances (about the sphere centre C = (0, 0, −86))

On a sphere every pad normal passes through C, so pad normal forces give **no** moment about C; every moment about C is pad friction (the real head's non-sphericity helps and is not credited). Moments:

- Drag ≤ 1.5 N at the nails (realistic µW ≈ 0.8 N at W2), lever R = 90 mm → **0.135 N·m** about Y, in phase with velocity.
- Servo reaction = arm inertia torque: I_arm ≈ 0.19 × 0.08² + 0.06 × 0.05² = 1.4 × 10⁻³ kg·m², ±25° at 2 Hz → α = 69 rad/s², τ = **0.094 N·m** (0.024 at 1 Hz, 0.21 at 3 Hz where the amplitude is smaller), in phase with acceleration, 90° from the drag.
- Vector peak √(0.135² + 0.1²) = **0.17 N·m**; arithmetic worst case 0.235 N·m. Yaw and roll disturbances (nail-to-nail drag differences, the 13 g servo/idler asymmetry) ≤ 0.013 N·m each.
- Translation: the 1.5 N drag is also reacted as a force; the lift latch (§6) adds a 2.5 N, 0.1 s downward impulse (safe direction).

### 3.2 Holding moment

Pad normal loads: ratchet preload **P = 3.0 N per pad [CHOICE]** (hoop tension ≈ P/√2 ≈ 2.1 N, the level of a loosely snugged hard-hat band) plus gravity ≈ 3.5 N over four feet on 60° slopes ≈ 1.5 N per pad → N ≈ 4.5 N per pad, ΣN ≈ 18 N. Capacity M_hold = µ ΣN R:

| µ (foam on hair / skin) | ΣN | M_hold | margin vs 0.17 N·m | vs 0.235 N·m | tangential capacity vs 1.5 N drag + 1.9 N (moment) |
|---|---|---|---|---|---|
| 0.3 (sweaty hair, design) | 18 N | 0.49 N·m | 2.9 | 2.1 | 5.4 N vs 3.4 N → 1.6 |
| 0.5 (dry hair / skin, typical) | 18 N | 0.81 N·m | 4.8 | 3.4 | 9.0 N vs 3.4 N → 2.6 |
| gravity only, no ratchet (ΣN ≈ 6 N) | 6 N | 0.16 / 0.27 N·m | 0.95 / 1.6 | — | **insufficient at µ 0.3: the ratchet snug is required** |

Drag shifts normal load between front and rear pads by ≈ 0.9 N; all pads stay loaded (4.5 ± 0.9 N). **With head tilt:** the crown's gravity moment about C is m g h sin φ, h = 122 mm (§4): 0.18 N·m at 20°, 0.27 at 30°, 0.38 at 45°. Demand at 30° ≈ 0.27 + 0.17 = 0.44 N·m against 0.49 (µ 0.3) → margin 1.1; at µ 0.5 the limit is above 45°. Hence the ±30° rule. **Headline margin: 2.9 upright at µ 0.3 (4.8 at 0.5); 1.1 at 30° tilt and µ 0.3.** Pad shear compliance (≈ 1 N/mm per block [EST]) lets the crown rotate ≈ 0.08° at the stroke frequency: 0.1 mm of hand motion, absorbed by the float.

### 3.3 Retaining band: needed, and what for

A loose band **is needed**, but not for the moment: the strap's moment arm about C is 2.9 N·mm per newton per side (anchors at (−10, ±88, −46), chin at (50, 0, −226)), so even 5 N of strap gives 0.03 N·m, a tenth of the friction hold. Its jobs are (a) lift-off and slide-off retention when friction is lost (sweat, a 1 g head jerk: 0.46 kg × 10 m/s² = 4.6 N against 5.4 N of friction at µ 0.3, marginal without a strap), (b) keeping the crown on if the ratchet is bumped open, (c) holding the 4.5 N crown at any head angle until the user removes it. **Spec [CHOICE]:** 15 mm elastic webbing, ≈ 0.1 N/mm, set to **1.5 N per side**, anchored at the parietal pad stations, routed ≥ 15 mm forward of the tragus, never over the pinna; closed by a printed **magnetic fuse** (two Ø 10 × 3 mm N35 discs in keyed cups, release **12 ± 3 N [TEST]**, < 20 N per safety §3 and RL-10); a side-release buckle on one leg sets length. The fuse opens before the crown can be pulled onto the face or the neck loaded; 60 mm of stretch (6 N) precede it, so a snag has to be a real pull.

### 3.4 Jaw motion, talking, swallowing

Jaw excursion 2–5 mm lengthens the strap ≤ 5 mm → ΔT ≤ 0.5 N per side, i.e. ≤ 0.3 N forward and ≤ 0.9 N downward on the crown against 5.4 N of friction capacity: no sliding, only pad compliance, 0.9 N / (4 × 2 N/mm) ≈ **0.1 mm**, recovering with the jaw. Forehead skin motion under pad F (eyebrow raise, 2–4 mm) shears the foam by ≤ 1 mm and moves the hoop ≤ 0.3 mm. All of it is one to two orders below the float's +5.4 / −24.6 mm tolerance; the nail force stays W. Comfort: 1.5 N per side is less than a bicycle-helmet strap, +0.5 N at full gape.

---

## 4. Mass, centre of mass, pad loads, comfort

Ledger (printed masses estimated from mech §11 densities and infills, ±10 % [EST]; weigh every part, TP L1 style):

| Item | g | Notes |
|---|---|---|
| Float, bare (MGN7C block + 6 g trim washers, hand, wrist) | 90 | mech §6.5 ledger, W1 = 0.88 N |
| XL330-M288-T + 60 mm cable loop | 23 | 18 g servo |
| C1 cradle node + servo back-plate | 12 | PETG |
| C2 idler node + 625-2RS + Ø 5 × 30 shoulder screw | 18 | shoulder 30 mm (absorbs ±4 mm of Y spacing) |
| Yoke cheeks A/B, 4 mm, narrowed | 16 | P19/P20 regenerated |
| Yoke crossbar: carbon 10 × 8 × 180 + 2 lugs | 12 | replaces the 45 g P21 beam; mast clamps to the tube |
| Mast + MGN7 100 mm rail + stops + thumbscrews | 44 | rail 22 g |
| Rail shroud G4, guard caps G2/G3, horn disc + M2 | 25 | |
| Lift latch: micro magnet, finger, spring, bracket | 13 | §6 |
| **Hand module subtotal** | **253** | (mech §3.1 ledger for the same parts: 346 g) |
| Uprights 2 × carbon 10 × 8 × 140 | 13 | |
| Foot plugs C4 × 2, hoop clamps C5 × 2, M4/M3 thumbscrews | 30 | |
| Cross tube carbon 10 × 8 × 200 | 9 | |
| Hoop Al 15.9 × 1.6 × 660 + heat-shrink | 49 | printed-PETG alternative 6 × 14 mm: 70 g |
| Rear ratchet C8/C9 | 12 | |
| Pads × 4 (TPU block, foam, plate, 2 × M3) | 32 | |
| Chin strap, anchors, magnetic fuse | 14 | |
| On-head 5-core cable + exit boot | 9 | |
| Fasteners, cable clips, misc | 8 | |
| **Crown structure subtotal** | **176** | |
| **Total on head, W1** | **429** | |
| + 30 g slug (W2) | 459 | default sensation setting |
| + 60 g (W3) | 489 | allowed only after the scale confirms ≤ 495 g **[TEST]** |

**Centre of mass:** W1 at (X +2, Y −6, Z +32); W2 at (+2, −5, +36), 122 mm above C and 82 mm above the band plane. The moving arm (yoke, crossbar, mast, rail, float, latch; 213 g) has its CoM 8 mm below the elbow axis: a weak pendulum, so with torque off it stays put (back-drive 0.02–0.05 N·m ≫ gravity 0.006 N·m at 25°, RT2 §6): a determinate limp state.

**Pad load sharing.** With the hand on the scalp the pads carry 459 − 120 = 339 g = 3.3 N (the float's weight goes through the nails); lifted, 4.5 N. The CoM offsets shift the shares by < 6 %: 0.8–0.9 N vertical per pad, 1.6–1.8 N normal on the 60° slopes, plus 3 N preload → **4.5–5 N per pad**, 5.5 N on the rear pad under full drag. Pressure 4.5 N / 1575 mm² = **2.9 kPa** mean, 3.5 kPa peak, 4.9 kPa if the TPU face conforms over only 70 % [EST]; limit 5 kPa (hard-hat sweatbands run at 3–6). Set the ratchet so pad F reads 3 N on a kitchen scale slid between pad and forehead. Neck: +0.26 N·m at 20° tilt against the head's own ≈ 0.45 N·m, the reason for the 20° recommendation. Topple: CoM 82 mm above a 212 × 172 mm foot pattern, tip angle > 45°; friction, not toppling, is the limit.

---

## 5. Coverage and repositioning

The hand is fixed to the head, so "coverage" is where the portal can put it while the rail still aims at C (the lift-off geometry needs a radial rail). Pitch ψ about the foot pivots (Z −30) with the telescoping uprights; the lookup card:

| ψ (detent) | upright pivot-to-axis L | clamp position on the hoop X_c | nail contact, arc behind (+) / ahead (−) of the vertex | scalp reached incl. ±24 mm chord |
|---|---|---|---|---|
| −10° (front) | 118 mm | −21 | −16 mm | −40 to +8 mm |
| 0° | 114 | −30 | 0 | ±24 |
| +10° | 108 | −40 | +16 | −8 to +40 |
| +20° | 100 | −52 | +31 | +7 to +55 |
| +25° (rear) | 94 | −59 | +39 | +15 to +63 |

Plus **sliding** the portal along the straight sides (X −70 to +10) at any ψ: at 0° the hand centre moves X −40 to +40, so the reachable crown is a cap of ≈ **±64 mm of arc around the vertex** (±40° on R 90); at +25° with the clamps at −70 the contact reaches ≈ 75 mm behind the vertex (47°), 21 mm above the band plane: **crown + upper occiput**. Forward of −10° is blocked by the hoop's front and by RL-6 (the most forward stroke end is ≥ 60 mm behind a hairline 100–110 mm of arc from the vertex). **Not reachable: lower occiput, inion, nape** — the hoop sits there, and the convex-sphere lift-off does not hold on the nuchal ridges (RT2 §3). Leaning forward does not extend reach (the hand moves with the head); it only restores the gravity reference at the rear detents. Stroke direction: the base portal spans ear-to-ear, stroke along the head's X; a **second portal with 236 mm foot spacing** (same nodes, longer tube, +40 g, +$10) spans front-to-back for the across-the-head stroke, its detents rolling the hand ±20° toward the parietals; not in the base build.

**How a change is made.** Release hold-to-run (float lifts), loosen the two M4 clamp thumbscrews, slide/pitch the portal to the card values (10 mm marks on the hoop, 1 mm marks on the plugs), re-tighten, read the float pointer at mid-stroke (3–8 mm) and trim the telescoping feet by the difference: 30–60 s, crown on (mirror) or off. No lift-and-reseat of the crown; the serration gives positive detents, the M4 clamp at ≈ 1 N·m holds > 20 N along the hoop.

---

## 6. Safety

**Donning / doffing, one hand, ≤ 3 s.** The cross tube is the handle. Don: lower onto the head from the front, forehead pad first; the hoop seats on the four feet by gravity (its contact perimeter is smaller than the head's maximum circumference, so it stops on the dome and cannot slide over the ears); the ratchet keeps its setting; click the self-locating fuse: ≈ 6 s. Doff: release hold-to-run (nails lift 25 mm), then pull the fuse tab or simply lift the handle (6 N at 60 mm of elastic, fuse at 12 N): **1–2 s, eyes closed [TEST, 10 trials]**. With the float lifted the nails leave the hair vertically before the crown moves (H-6.4).

**Power loss, e-stop, hold-to-run, watchdog, stall.** The actuator rail is unchanged (5 V → NC e-stop → hold-to-run → VIN and the lift magnet in parallel); the fail-safe moves from the frame hinge (gone) to the float: a **lift finger** pivoted on the mast under the carriage's riser foot, pulled up by a 2.5 N extension spring (W3 + 1 N), parked clear of the carriage by a **5 V micro holding electromagnet** (Ø 10–12 mm, ≥ 5 N, ≈ 7 g, 0.1–0.15 A, PTFE-taped) on a steel tab at the finger's 2:1 lever end (1.25 N to hold, 4× margin). Rail dead → finger swings up → carriage to the up-stop (≥ 24.6 mm) in < 100 ms [TEST at 240 fps]; the spring's travel ends on the up-stop so it can never add scalp force (RT2 §11); reset by pressing the finger down with the rail live. 13 g on the arm.

Why not "limp at W, the user lifts the whole thing off" (the brief's question against RL-8 and RT2 §8): of the two reasons that forced LIFTED on the stand, (1) the reflexive exit that drives the head *into* a limp hand is **not applicable** — the hand rides with the head; (2) a stopped stroke leaving a trapped strand loaded (H-5.9) **still applies**, and worse, the user's own lift-off would then pull a hooked strand with an unbounded hand force. RL-8's letter would be met by limp; RT2's ruling and H-5.9 only by lifting, which costs 13 g and $8, so I keep LIFTED. The limp state is at least determinate (§4). The lift's 2.5 N exceeds the 0.36 N pluck floor, as the stand's 13 N lift did; the W tip's radiused symmetric edge (H-4.1–4.4), not the lift force, keeps strands from hooking.

**Snag reflex.** As frozen: the hold-to-run release drops the rail; the mechanical layers (leaf torsion ≈ 0.1 N/mm tangential, wrist tip-release at 2.0 N, lift) are the hand's own, unchanged.

**Flinch / head jerk ±20 mm at 0.3 m/s.** The crown moves with the head: relative hand-scalp motion is only pad slip under the crown's inertia (4.6 N at 1 g against 5.4–9 N of friction: ≤ 1–2 mm at µ 0.3, none at 0.5) plus the float's own inertia, W(1 + a/g): 2 W at 1 g (0.8 N per nail at W2, 1.0 at W3), 3 W at a 2 g sneeze (1.5 N per nail at W3), under the 2.5 N RL-2 cap. RT2 §3's rigid stage (float, leaf, then a monitor arm at 10–20 N) **does not exist**: no fixed structure for the head to rise into, and no aim error reaches the temple, ear or forehead (RT2 §8's open RL-6 "no aim limit" closes by geometry: the hand's lowest reach is ≥ 60 mm behind the hairline and ≥ 110 mm above the ear canals at every detent).

**25 mm from eyes and ears.** Pad F's lower edge is 50 mm above the eye; the strap passes ≥ 15 mm forward of the tragus (static, not an element); side pads ≥ 60 mm above the ear canals; the yoke's lowest moving point (cheek corner, Z 60) is ≥ 115 mm above the scalp at the ear line. The CROSS-aim rule (idler side forward, mech §10) carries over to the second portal.

**Cable.** One 5-conductor 26 AWG lead (DXL data, VIN, GND, magnet ±): servo (connectors on the 23 × 34 side faces, exit toward −X) → clipped down the −Y upright → along the hoop's outer face → a 6 mm TPU boot at the occipital pad pointing down → 1.2 m to the OpenRB-150 on the desk, with a 150 mm PTFE-sleeved stiff section at the nape so no loop forms in nape hair (H-6.1: a static cable over the collar is not a wind-up path); the boot's strain relief takes a 20 N tug without moving the crown. Hold-to-run stays handheld, e-stop on the desk.

---

## 7. Noise and vibration

Path: XL330 gear train (hundreds of Hz to ~2 kHz) → C1 node → carbon upright → hoop → four pads → skull, by bone conduction and by shaking the forehead skin. The servo stays in the yoke (brief), so mitigation is isolation, damping and distance:

1. **Pads as isolators.** The 12 mm TPU 85A gyroid blocks, ≈ 3 N/mm each [EST] under 0.46 kg → f_n ≈ 25 Hz, isolation above ≈ 36 Hz, roughly −20 dB at 100 Hz; the 1–3 Hz stroke reaction is quasi-static and the pads' shear compliance there is small (§3.2). Foam alone is too stiff, TPU alone too lively: 12 mm TPU under 3 mm foam.
2. **Servo mount.** The back-face M2 screws pass through 1 mm TPU 95A grommets with a 1 mm TPU gasket under the servo, torqued to 0.1 N·m: −6 to −10 dB in the structure path [EST].
3. **Hoop damping.** An aluminium band rings; a 0.5 mm butyl strip under the heat-shrink (+5 g, optional) kills it; the PETG hoop alternative is self-damped.
4. **Distance.** The servo is ≈ 110 mm from the nearer ear canal (300 mm on the stand): RT2 §7's 45–55 dBA becomes ≈ 55–65 dBA at the ear [EST], hair-clipper territory; the SPEED pot is the lever, gear noise falls steeply with speed.

Honestly: the crown is intrinsically noisier at the ear than the stand, and bone-conducted buzz through the forehead pad is a plausible illusion-breaker that no calculation settles. **[TEST]** phone accelerometer inside the mannequin under pad F, servo at 2 Hz ±25° and W2, rigid pads vs TPU stack (≥ 15 dB reduction at 200–2000 Hz), then Michael's unpowered-vs-powered 5-minute rating ("servo intrusive?" ≤ 2/7 passes).

---

## 8. Build

**Director's XL330 facts applied (bom-verified.md §11).** No side mounting holes (mech §5.3's two M2 side screws are deleted); the servo mounts through its **back-face 4 × Ø 1.6 holes on a 16 × 30 mm pattern** with M2 × 6 screws into C1's plate (counterbored, TPU gasket between); output axis 9.5 mm from the horn-end face, so C1 sets the axis 9.5 mm above the servo's lower end (body Z 74.5–108.5, axis 84.0; the mech lead's "10 mm [VERIFY]" becomes 9.5); horn Ø 16, PCD Ø 12, M2 × 6: P16 is regenerated with 4 × Ø 2.2 on PCD 12; connectors on the 23 × 34 side faces, cable exit toward −X (C1 leaves that face open). **Supply:** the XL330 is on 2-month back-order at robotis.us; order from ROBOTIS Korea (DHL) or the build waits on the servo. The crown adds no second servo.

**Printed parts (PETG, 0.2 mm layers, 4 perimeters / 40 % unless noted).**

| # | Part | Qty | Mat. | Size (mm) | Notes |
|---|---|---|---|---|---|
| C1 | Cradle node (−Y): tube sockets (Ø 10.2, M3 set screws), 30 mm forward arm, servo back-plate 24 × 38 × 3 with 4 × Ø 2.2 on 16 × 30, gasket recess | 1 | PETG | 60 × 32 × 40 | replaces P11/P13/P14 |
| C2 | Idler node (+Y): sockets, forward arm, Ø 16.0 × 5 bearing bore, ±1.5 mm X/Z slots | 1 | PETG | 55 × 20 × 36 | replaces P12/P15; 60 % |
| C3 | Yoke crossbar lugs (Ø 10 clamp, 2 × M3 to the cheeks) + mast clamp | 2 + 1 | PETG | 20 × 16 × 16 / 24 × 20 × 20 | replaces P21 |
| C4 | Foot plug: 8 × 8 × 40 telescoping stem with 1 mm marks, Ø 24 36-tooth serration, M4 bore | 2 | PETG | 24 × 24 × 55 | 100 % |
| C5 | Hoop clamp: saddle on the 15.9 × 1.6 band, mating serration in a closed lip housing, M4 thumbscrew + nyloc | 2 | PETG | 30 × 24 × 30 | 60 % |
| C6 | Pad backing plate, 2 × Ø 3.4 | 4 | PETG | 45 × 35 × 3 | |
| C7 | Pad block, face at the 60° slope, 20 % gyroid, + 3 mm foam skin | 4 | TPU 85A | 45 × 35 × 12 | |
| C8 | Ratchet sleeve, 40 mm rack (1.5 mm pitch) outward, closed | 1 | PETG | 60 × 22 × 12 | left band end |
| C9 | Pawl carrier, release tab, living-hinge pawl | 1 | PETG | 40 × 22 × 12 | right band end |
| C10 | Strap anchor, 15 mm slot | 2 | PETG | 20 × 12 × 8 | L/R pad stations |
| C11 | Magnetic fuse halves, keyed cone, Ø 10 × 3 pocket | 2 | PETG | Ø 18 × 8 | 12 ± 3 N [TEST] |
| C12 | Lift finger (Ø 12 × 1 steel keeper), spring post, magnet bracket | 1 set | PETG | 30 × 8 × 4 + 20 × 14 × 14 | on the mast |
| C13 | Cable exit boot + 6 clip loops | 1 + 6 | TPU | Ø 12 × 20 | |
| P16r | Horn disc, PCD 12 | 1 | PETG | Ø 24 × 3 | regenerated |
| P19r/P20r | Yoke cheeks, 4 mm, inner faces at |Y| 88 | 2 | PETG | 69 × 4 × 40 | regenerated |

**Reused unchanged from cad/frame/stl:** P17, P18 (guard caps, re-mounted to C1/C2), P22–P29, P30–P35, P43, P46, P47, and the tip lead's T1–T4 and tips. **Dropped:** P1–P15, P21, P36–P42, P44, P45 (24 of 48 designs: everything that belonged to the arm, hinge, frame and cradle). gen_frame_stl.py regenerates the yoke, mast and float parts with the parameters above; C1–C13 are new OpenSCAD (≈ 4 h of CAD).

**Bought parts, delta.** Added: aluminium flat bar 15.9 × 1.6 × 915 mm ($6); carbon tube 10 × 8 × 500 mm ($9); TPU 85A 250 g ($14); closed-cell PE foam 3 mm ($6); 15 mm elastic webbing + side-release ($5); N35 Ø 10 × 3 magnets ×4 ($5); 5 V micro holding electromagnet ($7); 2.5 N extension spring (BOM assortment); 5-core 26 AWG cable 2 m ($6); M4/M3 thumbscrews ($5); 25 mm heat-shrink ($4); MGN7 100 mm rail + MGN7C block ($10, replaces the $12 MGN9 kit): **≈ $77.** Removed from the stand build (bom.md §2): monitor arm $36, ballast ≈ $40, 2020 extrusion and brackets ≈ $40, Adafruit 3872 magnet $8, hinge springs/cords/pulleys ≈ $18, M6 pin and VESA hardware ≈ $8, face cradle, cushion and isolation feet ≈ $55: **≈ $205.** Net **≈ −$130 versus the stand rig**; versus the hand module alone the crown is **≈ +$77** (+$10 and 40 g for the second portal).

**Build hours.** Plywood form and hoop bending 1.5 h; ratchet ends and heat-shrink 0.5 h; printing ≈ 9 h unattended (≈ 230 g PETG, 45 g TPU); portal bonding in a jig (nodes on tubes against two blocks on a flat board, CA then epoxy fillets, coaxial to 0.3 mm) 1 h; pads, strap, fuse 1 h; hand onto the portal and alignment 1.5 h; §9 bench tests ≈ 4 h. **Crown-specific hands-on ≈ 10 h** against ≈ 7–8 h of adapter/hinge/frame/cradle work in mech §13 (the hand module's 8–10 h is common): cheaper in cash, two hours longer, no desk-clamp site preparation.

---

## 9. Top five risks and the bench test that retires each

| # | Risk | Why it is credible | Bench test (mannequin head with a 5–8 cm wig, servo running) | Pass |
|---|---|---|---|---|
| 1 | **Crown creeps or twists under servo reaction and drag at low µ** (sweat, fine hair); the stroke walks off target | margin 1.1 at 30° tilt and µ 0.3; µ on real hair unmeasured | Drag test: 20 min at 2–3 Hz ±25°, W2, B45-12 tip on a dry then misted wig, ratchet at 2 and 3 N per pad, dial indicator on the hoop; tilt test at 20° and 30° | drift ≤ 2 mm, rotation ≤ 1° at every condition; else P = 4 N (3.9 kPa) or a fifth (vertex) pad |
| 2 | **Over 500 g, or uncomfortable at 20 min** (forehead pad, neck) | ledger ±10 %; 459 g at W2 is 41 g under the line | Weigh at W1/W2/W3; wear unpowered 20 min upright + 10 min at 20°; FSR under pad F | ≤ 495 g at the W used; pad F ≤ 5 kPa; no mark 5 min after; comfort ≥ 5/7 |
| 3 | **Seating outside the float's +5.4 mm high-side tolerance**, or H unrepeatable session to session | the high-side margin is small by design (§2) | Shim the mannequin pads −5…+5 mm; pointer at mid-stroke; nail force on a 0.01 N scale at 0°, 20°, 30° tilt | pointer 1–10 mm and force = W cos φ ± 0.05 N at every shim; five donnings repeat the pointer ± 2 mm |
| 4 | **Noise and buzz through the pads break the illusion** | servo 110 mm from the ear, structure path through four pads | §7 accelerometer A/B (rigid vs TPU stack), then Michael's 5-minute rating | ≥ 15 dB isolation at 200–2000 Hz; "servo intrusive" ≤ 2/7; else lower SPEED and add butyl, or the stand |
| 5 | **Lift latch fails** (residual magnetism, spring weak at W3, finger fouls the riser) or **doffing > 3 s** | new mechanism; 2.5 N spring vs 1.47 N W3 is 1.7× | 20 rail-drops per W at 0°, ±25°, mid-stroke, 240 fps; float-jam at the up-stop (ADD-1 D10); 10 eyes-closed doffs; fuse pull ×10 | ≥ 24 mm in ≤ 100 ms every time; doff ≤ 3 s in 10/10; fuse 9–15 N |

Also carried: the hair checklist re-score on the built crown (the hand's 29/36 stands; the crown adds static parts only), the RL-6 hairline check at the −10° detent on Michael, and the yoke free-swing check (mech §13 step 9) after portal bonding.

---

## 10. Verdict

The ring crown is the better **product prototype** and, by the numbers here, a credible **SP1 rig**: the dead-weight force reference survives intact (strap and hoop never touch the force path), it removes the two hazards the red team could not close on the stand (head rising into a rigid arm, and an aim that could reach the temple), it is hands-free and ≈ $130 cheaper, and the hand module changes only by a narrower yoke, a lighter rail and a float-mounted lift. What it costs is real: 430–460 g on the head (the 350 g target is unreachable with this hand module; W3 sits 11 g under the red line), a servo 110 mm from the ear with a bone-conduction path the stand lacks, coverage limited to the crown and upper occiput (no nape, no inion: the hoop is in the way), a ±30° tilt rule, and a Stage-2 matrix whose reference frame is a hat that creeps rather than a desk that does not. I would choose the stand after all if any of three bench results comes back wrong — creep > 2 mm in the drag/tilt test (risk 1), "servo intrusive" above 2/7 (risk 4), a forehead-pad complaint at 20 minutes (risk 2) — or if the sensation gate needs W3 or the occiput/nape lanes, which only the stand gives. Those tests cost the hoop, pads and portal (≈ $77 and a weekend) and run on the mannequin before the hand is finished; run them first and let them, not the brief, pick the rig.
