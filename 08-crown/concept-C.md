# CROWN CONCEPT C — "TWIN-RAIL ARCH HALO" (resting crown, sagittal arch carriage)

Team C, 2026-10-01. Seed: the arch halo (a sagittal arch over the head, forehead and occiput pads, the elbow carrier as a carriage sliding along the arch with detents, breakaway chin strap). Written to CROWN-BRIEF.md; references DESIGN-FREEZE.md (DF), DESIGN-FREEZE-ADDENDUM-1.md (ADD-1), mechanical.md (MECH), safety-requirements.md (SR), hair-interaction.md (HI), judge-2-engineering.md (J2), redteam-2-mechanical.md (RT2). Frame: DF §0 with ADD-1 D9 (scalp sphere R 90 mm, centre C = (0, 0, −86), apex Z +4, elbow axis Z +84 = R 170 from C). +X = anterior (toward the forehead), +Y = left, Z up. The polar angle φ about the Y-axis through C is positive toward the forehead; the carriage position on the arch is φ_c.

## 0. The one geometric fact that shapes this concept

A single sagittal arch of R 110–120 mm at Y = 0 cannot carry this hand module. Everything on the swinging arm lies within R 91 mm of the elbow axis (MECH §2 check c) and the palm occupies Y −88 to +81, Z 38–66, so an arch at Y = 0 passes either through the palm (R 110–120 from C is Z 24–34 above the apex) or above the mast's sweep at R ≥ 170 + 91 + 10 = 271 mm, 185 mm above the crown: ~240 g of 2020 or ~90 g of flat bar plus 180 mm uprights, with the centre of mass 150 mm above the head.

So the seed's arch is split into **two sagittal rails in the planes Y = ±116 mm**, outboard of the yoke cheeks (|Y| 93–98), servo (Y −101 to −127) and idler (Y +101 to +111). Each is a printed C-channel arc of **R 120 inner / R 140 outer about C** (the seed's radius), φ −60° to +45°, slot on top. A shoe runs inside each channel; a 4 mm leg rises through the slot *behind* the servo (X −28 to −24) to the elbow axis at R 170; an Ø 8 mm aluminium tube ties the two legs behind the hand's sweep. Because the rails are concentric with the scalp sphere, the elbow axis stays at R 170 (H = 80) and the float rail stays normal to the local scalp at every position: sliding the carriage re-aims the module for free. Forehead, occiput and two sprung temple pads hold the ring; an elastic magnetic chin strap retains it. Servo and idler stay where MECH §5 put them (narrowing by 6 mm would close the 5 mm palm-to-cheek gap of MECH §2 check d).

The second, lateral (ear-to-ear) arch is rejected (§5).

## 1. Geometry

### 1.1 Side view (XZ, looking from +Y; carriage at the crown detent φ_c = 0)

<svg viewBox="-200 -230 420 330" xmlns="http://www.w3.org/2000/svg" width="640" font-family="sans-serif" font-size="7">
  <g transform="scale(1,-1)">
    <!-- scalp sphere R90 about C(0,-86) -->
    <circle cx="0" cy="-86" r="90" fill="#f3e9dc" stroke="#999" stroke-width="0.8"/>
    <!-- face / neck hint -->
    <path d="M 86,-112 L 92,-150 L 70,-200 L 40,-230 L -60,-230 L -80,-176" fill="none" stroke="#bbb" stroke-width="0.6"/>
    <!-- ear canal marker -->
    <circle cx="-10" cy="-86" r="3" fill="none" stroke="#c66" stroke-width="0.6"/>
    <!-- rails R120-140, phi -60..+45 -->
    <path d="M -121.2,-16 A 140,140 0 0 1 99,13 L 85,-1.1 A 120,120 0 0 0 -103.9,-26 Z" fill="#cfe3ff" stroke="#246" stroke-width="0.8"/>
    <!-- detent holes at 15 deg -->
    <g fill="#246">
      <circle cx="65" cy="26.6" r="1.5"/><circle cx="33.6" cy="39.5" r="1.5"/><circle cx="0" cy="44" r="1.5"/>
      <circle cx="-33.6" cy="39.5" r="1.5"/><circle cx="-65" cy="26.6" r="1.5"/><circle cx="-91.9" cy="5.9" r="1.5"/>
    </g>
    <!-- shoe + leg + cradle (carriage, servo side) -->
    <rect x="-20" y="22" width="40" height="18" fill="#9bc" stroke="#246" stroke-width="0.6"/>
    <rect x="-28" y="40" width="4" height="68" fill="#9bc" stroke="#246" stroke-width="0.6"/>
    <rect x="-24" y="74" width="24" height="34" fill="#9bc" stroke="#246" stroke-width="0.6"/>
    <!-- cross tube at local -24 deg, R146 -->
    <circle cx="-59.4" cy="47.4" r="4" fill="#ddd" stroke="#246" stroke-width="0.6"/>
    <!-- elbow axis -->
    <circle cx="0" cy="84" r="2" fill="#000"/>
    <!-- yoke cheek, crossbar, mast -->
    <path d="M 0,64 L 57,64 L 57,104 L 0,104 Z" fill="none" stroke="#555" stroke-width="0.6" stroke-dasharray="2,1"/>
    <rect x="45" y="80" width="12" height="16" fill="#ccc" stroke="#555" stroke-width="0.6"/>
    <rect x="40" y="64" width="5" height="111" fill="#ccc" stroke="#555" stroke-width="0.6"/>
    <!-- float carriage, palm, knuckle plate, nails -->
    <rect x="30" y="74" width="10" height="29" fill="#aaa" stroke="#555" stroke-width="0.6"/>
    <rect x="-26" y="38" width="52" height="28" fill="#eee" stroke="#555" stroke-width="0.6"/>
    <path d="M -32,37.5 Q 0,34 32,37.5" fill="none" stroke="#555" stroke-width="1.2"/>
    <line x1="0" y1="34" x2="0" y2="0" stroke="#000" stroke-width="1"/>
    <!-- sweep R91 -->
    <circle cx="0" cy="84" r="91" fill="none" stroke="#c99" stroke-width="0.4" stroke-dasharray="3,2"/>
    <!-- pads -->
    <path d="M 86,-32 A 90,90 0 0 0 65,-22" fill="none" stroke="#e8a" stroke-width="8"/>
    <path d="M -89,-30 A 90,90 0 0 0 -70,-22" fill="none" stroke="#e8a" stroke-width="8"/>
    <!-- bridges -->
    <path d="M 99,13 L 94,-40 M -121.2,-16 L -102,-40" stroke="#246" stroke-width="2" fill="none"/>
    <!-- chin strap -->
    <path d="M 25,45 L 70,-180" stroke="#484" stroke-width="1.5" fill="none" stroke-dasharray="4,2"/>
    <!-- dimensions -->
    <line x1="0" y1="-86" x2="0" y2="-200" stroke="#000" stroke-width="0.3" stroke-dasharray="1,1"/>
    <line x1="-150" y1="84" x2="-30" y2="84" stroke="#000" stroke-width="0.3"/>
    <line x1="-150" y1="4" x2="-30" y2="4" stroke="#000" stroke-width="0.3"/>
    <line x1="-150" y1="-86" x2="-30" y2="-86" stroke="#000" stroke-width="0.3"/>
    <line x1="-145" y1="84" x2="-145" y2="4" stroke="#000" stroke-width="0.4"/>
    <line x1="-150" y1="4" x2="-150" y2="-86" stroke="#000" stroke-width="0.4"/>
    <line x1="120" y1="-86" x2="120" y2="44" stroke="#000" stroke-width="0.4"/>
    <line x1="140" y1="-86" x2="140" y2="84" stroke="#000" stroke-width="0.4"/>
  </g>
  <g>
    <text x="-190" y="-40" font-size="7">H = 80 (axis to apex)</text>
    <text x="-190" y="40" font-size="7">R = 90 (apex to C)</text>
    <text x="100" y="-20" font-size="7">rail R 120–140</text>
    <text x="145" y="-5" font-size="7">axis R 170</text>
    <text x="-70" y="-55" font-size="7">cross-tube Ø8 at R146, −24°</text>
    <text x="60" y="35" font-size="7">forehead pad φ+68°</text>
    <text x="-190" y="35" font-size="7">occiput pad φ−65°</text>
    <text x="-100" y="140" font-size="7">+X forward →   rails: φ −60° … +45°, detents every 15° from −45° to +30°</text>
    <text x="30" y="110" font-size="7" fill="#484">chin strap (elastic, magnetic)</text>
    <text x="-20" y="95" font-size="7" fill="#c66">ear canal</text>
    <text x="-5" y="-115" font-size="7">R91 sweep</text>
  </g>
</svg>

### 1.2 Front view (YZ, looking from +X; carriage at φ_c = 0, arm at θ = 0)

<svg viewBox="-200 -200 400 300" xmlns="http://www.w3.org/2000/svg" width="640" font-family="sans-serif" font-size="7">
  <g transform="scale(1,-1)">
    <!-- head: sphere R90 about C -->
    <circle cx="0" cy="-86" r="90" fill="#f3e9dc" stroke="#999" stroke-width="0.8"/>
    <!-- ears -->
    <ellipse cx="-88" cy="-86" rx="6" ry="18" fill="none" stroke="#c66" stroke-width="0.6"/>
    <ellipse cx="88" cy="-86" rx="6" ry="18" fill="none" stroke="#c66" stroke-width="0.6"/>
    <!-- rails (channels) at |Y| 108-124, R120-140 -> Z 34-54 -->
    <rect x="-124" y="34" width="16" height="20" fill="#cfe3ff" stroke="#246" stroke-width="0.8"/>
    <rect x="108" y="34" width="16" height="20" fill="#cfe3ff" stroke="#246" stroke-width="0.8"/>
    <!-- top slots -->
    <rect x="-122" y="52" width="12" height="2" fill="#fff" stroke="none"/>
    <rect x="110" y="52" width="12" height="2" fill="#fff" stroke="none"/>
    <!-- legs (4 mm plates, behind servo) -->
    <rect x="-118" y="40" width="4" height="68" fill="#9bc" stroke="#246" stroke-width="0.6"/>
    <rect x="114" y="40" width="4" height="68" fill="#9bc" stroke="#246" stroke-width="0.6"/>
    <!-- servo cradle and body Y -101..-127, Z 74..108 -->
    <rect x="-127" y="74" width="26" height="34" fill="#9bc" stroke="#246" stroke-width="0.6"/>
    <!-- idler housing +101..+111 -->
    <rect x="101" y="70" width="10" height="28" fill="#9bc" stroke="#246" stroke-width="0.6"/>
    <!-- cross tube projected (behind) -->
    <rect x="-124" y="43" width="248" height="8" fill="none" stroke="#246" stroke-width="0.5" stroke-dasharray="2,1"/>
    <!-- yoke cheeks |Y| 93-98 -->
    <rect x="-98" y="64" width="5" height="40" fill="#ccc" stroke="#555" stroke-width="0.6"/>
    <rect x="93" y="64" width="5" height="40" fill="#ccc" stroke="#555" stroke-width="0.6"/>
    <!-- crossbar Y -98..98, Z 80-96 -->
    <rect x="-98" y="80" width="196" height="16" fill="#ddd" stroke="#555" stroke-width="0.6"/>
    <!-- mast + rail -->
    <rect x="-12" y="64" width="24" height="111" fill="#ccc" stroke="#555" stroke-width="0.6"/>
    <!-- palm Y -88..81, Z 38..66 -->
    <rect x="-88" y="38" width="169" height="28" fill="#eee" stroke="#555" stroke-width="0.6"/>
    <!-- knuckle plate and nails at Y -24,0,24 -->
    <path d="M -45,33.9 Q 0,37.5 45,33.9" fill="none" stroke="#555" stroke-width="1.2"/>
    <line x1="-24" y1="34" x2="-24" y2="-3.6" stroke="#000" stroke-width="1"/>
    <line x1="0" y1="34" x2="0" y2="0" stroke="#000" stroke-width="1"/>
    <line x1="24" y1="34" x2="24" y2="-3.6" stroke="#000" stroke-width="1"/>
    <!-- elbow axis line -->
    <line x1="-130" y1="84" x2="130" y2="84" stroke="#000" stroke-width="0.3" stroke-dasharray="1,1"/>
    <!-- temple pads at Y ±78, Z -30, on sprung arms from the rails -->
    <path d="M -108,40 L -92,-20" stroke="#246" stroke-width="2" fill="none"/>
    <path d="M 108,40 L 92,-20" stroke="#246" stroke-width="2" fill="none"/>
    <rect x="-86" y="-45" width="8" height="30" fill="#e8a" stroke="none"/>
    <rect x="78" y="-45" width="8" height="30" fill="#e8a" stroke="none"/>
    <!-- chin strap -->
    <path d="M -116,34 L -40,-190 L 40,-190 L 116,34" stroke="#484" stroke-width="1.5" fill="none" stroke-dasharray="4,2"/>
    <!-- dims -->
    <line x1="-124" y1="140" x2="124" y2="140" stroke="#000" stroke-width="0.4"/>
    <line x1="-90" y1="-110" x2="90" y2="-110" stroke="#000" stroke-width="0.4"/>
  </g>
  <g>
    <text x="-30" y="-150" font-size="7">halo width 248</text>
    <text x="-50" y="118" font-size="7">head 180 (sphere); real ≈ 150–160</text>
    <text x="-190" y="-70" font-size="7">servo Y −101…−127</text>
    <text x="125" y="-70" font-size="7">idler +101…+111</text>
    <text x="-190" y="-40" font-size="7">rail channel |Y| 108–124</text>
    <text x="-190" y="40" font-size="7">temple pad Y ±78, Z −30</text>
    <text x="-190" y="92" font-size="7" fill="#c66">ears |Y| 82–94, Z −68…−104</text>
    <text x="40" y="100" font-size="7" fill="#484">strap ≥ 35 mm ahead of the tragus</text>
  </g>
</svg>

### 1.3 Where it touches the head

| Pad | Location (on the R 90 sphere) | Size | Material | Nominal normal load |
|---|---|---|---|---|
| FH forehead | φ +68°, Y 0; centre at (X 83, Z −52); bottom edge 20 mm above the brow | 70 × 40 × 8 mm | closed-cell EVA 35 Shore A on a 2 mm TPU 85A isolator plate, cotton sleeve, hook-and-loop | 5.5 N (3 N clip preload + weight and strap share) |
| OC occiput | φ −65°, Y 0; centre at (X −82, Z −48), 25 mm above the inion | 70 × 40 × 8 mm | same | 5.5 N (up to 9.5 N at the −45° detent) |
| TL/TR temples | (X −5, Y ±78, Z −30), on the parietal eminences, 56 mm from the ear canal | 45 × 30 × 8 mm | same, on sprung printed arms (3 shim positions) | 2 N each |

Pad pressure: FH/OC 5.5 N / 28 cm² = 2.0 kPa (3.4 kPa worst case), temples 1.5 kPa; all under the 5 kPa comfort limit. The two bridges are open frames (two 6 × 10 mm struts each) converging from the rail ends to the pad carriers; nothing but the four pads and the strap touches the head. The forehead pad carrier sits on a printed 2 mm PETG leaf (k ≈ 0.7 N/mm) with an M4 thumbscrew: the halo is a sagittal spring clip with 2–4 N of fore-aft preload, set per head length (180–200 mm).

### 1.4 Hair canopy clearance

Everything that moves relative to the head is the hand module (unchanged from MECH §5.5 and §8: nothing within 30 mm of the scalp but tips, paddles, boot and knuckle plate) or the carriage in its channel. The channels sit at |Y| 108–124, Z −26 to +54: 30–45 mm outboard of a real head's side and ≥ 23 mm above the ear. The sliding interface (shoe in channel, 0.3 mm clearances) is enclosed on the inner, lower and outer faces; the only opening is the 12 mm top slot, facing away from the head, through which the 4 mm leg passes with 4 mm clear each side (≥ 3 mm, DF §1.4). Channel ends are closed and the shoe stays ≥ 10 mm from them at the end detents, so RT2 §2's closing V does not occur; the carriage moves only by hand with the servo off. The cross-tube passes 40 mm above the scalp behind the hand, smooth and non-rotating. Tolerated hair: ≤ 5 cm free, longer clipped up off the sides (HI §1.9); the wig-head test (§9 R3) decides.

### 1.5 Module position and what changes in the module

Elbow axis at R 170 from C at every carriage position (H = 80 mm), float rail radial, stroke ±25°, all firmware constants unchanged. Module changes: (a) the P13 cradle and P15 idler housing geometries (pocket, ±32° bumper lugs, zero-pin bore, alignment slots) are absorbed into the carriage prints C1/C2, whose undersides replace the guard caps P17/P18; (b) P1–P12 and P14 (adapter, hinge, magnet, springs, frame, carrier beam, drop legs, yaw plates) are deleted; (c) MGN9 rail shortened to 70 mm (−11 g); (d) default down-stop E8 (§2.2); (e) yoke cheeks 4 mm, P21 walls 1.6 mm (−13 g). Radial trim ±6 mm (three cradle bolt positions on the leg) corrects head-shape error between detents.

## 2. Force reference

### 2.1 Nail force = dead weight, whatever the seating

The hand hangs from the MGN9 float, a 1-DoF bearing along the local scalp normal. Between its stops the only normal force that can reach the nails is the floating weight W (90–190 g, 0.88–1.86 N) less rolling friction ≤ 0.03 N (MECH §6.8), shared 0.8 / 1.0 / 1.2 by the leaves. The halo's seating enters only as the down-stop's position relative to the scalp, i.e. the geometric engagement E. A ±3–5 mm seating change (pad compression, pile, head shape between detents) changes E, not W: while the sphere is more than δ = W/Σk (2–3.3 mm) above the free tip and the float is off its up-stop, N = W cos φ_eff (§2.3). Leaf preload spread (±0.1 N between nails) rides on W as in every architecture.

### 2.2 Float travel required and the default engagement

Budget along the rail, from the down-stop upward: head-shape and seating error ±5 mm; stroke arc profile 7.7 mm peak-to-peak (RT2 §1), of which the leaves take part; jaw-motion crown displacement ≤ 0.5 mm (§3.4); flinch reserve ≥ 15 mm (RT2 §3). The engineered float gives 24 + E mm between stops (MECH §6.3). **Default E8** here (down-stop at L_max = 88 mm): the float sits 8 − δ ≈ 5–6 mm above the down-stop at mid-stroke, with 24 mm of up-travel in reserve, and a −5 mm seating error still leaves E3 (dead-weight plateau ≈ 10 mm around the apex per MECH §9.3; the force is still capped at W because the leaves alone give ≤ 0.9 N). A +5 mm error gives E13: plateau the whole chord. The E column of the experiment matrix therefore reads E8 nominal, set with the apex gauge P43 at each detent (the gauge rings at 80–88 become 84–92).

### 2.3 Tilt

The float rail is radial at the carriage's φ_c; gravity is vertical. With the head pitched forward by α (chin down), the effective inclination of the rail from vertical is φ_eff = φ_c + α (forward positive):

| φ_eff | 0° | 15° | 30° | 45° | 60° |
|---|---|---|---|---|---|
| N/W = cos φ_eff | 1.00 | 0.97 | 0.87 | 0.71 | 0.50 |
| W1 90 g → N (N) | 0.88 | 0.85 | 0.76 | 0.62 | 0.44 |
| W2 120 g → N | 1.18 | 1.14 | 1.02 | 0.83 | 0.59 |
| W3 150 g → N | 1.47 | 1.42 | 1.27 | 1.04 | 0.74 |
| 190 g (max slugs) → N | 1.86 | 1.80 | 1.61 | 1.32 | 0.93 |
| tangential W sin φ_eff on the rail block (190 g) | 0 | 0.48 | 0.93 | 1.32 | 1.61 |

The tangential component W sin φ_eff is carried by the MGN9 block (rated hundreds of newtons) into the yoke and halo; it never reaches the nails, which are rigid to the carriage in X and Y and see only friction µN during the stroke. Head roll β likewise loads the block sideways, not the nails. **Tilt limit: |φ_eff| ≤ 45°, |β| ≤ 20°.** At 45° the force is 0.71 W, the block side load 1.3 N, the wrist breakaway shifts to 1.7–2.2 N (the hand's weight component at 35 mm below the seat adds ±0.015 N·m to MECH §7.2's seat moment) and the halo margin (§3) stays ≥ 1.3. Beyond 60° the force halves and the halo's gravity load along the skull exceeds the clip preload: out of bounds, enforced by posture (face cradle ≤ 45°), not firmware. **Usable arc:** the full 0.6–1.5 N window needs 1.86 cos φ_eff ≥ 1.5 N, |φ_eff| ≤ 36°; the W1–W2 window holds to 50°. The way to use the back detents is to lean forward: at −45° with α = 30–45° the rail is within 15° of vertical and N = W. If a trim is wanted, the MECH §6.7 beading cord hooked *below* the riser adds a bounded 0.3 N at 0.003 N/mm; the cap becomes W + 0.35 N ≤ 2.2 N, still a mechanical constant (SR red line 2).

### 2.4 Force variation inside the stroke

Unchanged from DF §1.5 / MECH §6.9: N = W cos θ / (1 ∓ µ sin θ) along the arc, 0.84–1.16 W at ±13°; the float sits on its down-stop beyond ±7–15° and force tapers to zero by ±25° (lift-off by geometry at both ends). Inertia of the float following the arc adds ≈ 3 % at 2 Hz. A head jerk toward the hand at 5 m/s² adds m_float × a = 0.45–0.95 N for 20–40 ms (per nail 0.15–0.3 N), then the leaves soften it; no element exceeds 1.0 N.

## 3. Stability on the skull

### 3.1 Disturbances

| Source | Magnitude | Axis | Lever to C | Moment |
|---|---|---|---|---|
| Hand drag at the nails, normal operation (3 × 0.3 N) | 0.9 N along X | pitch (about Y) | reaction enters the halo at the elbow axis, R 170 | 0.15 N·m |
| Hand drag at the firmware stall limit (DF §1.10 ≈ 1.2 N; take 1.5 N) | 1.5 N | pitch | R 170 | 0.26 N·m |
| XL330 reaction torque accelerating the yoke (≈ 0.2 kg at 60 mm, ±25° at 2–3 Hz) | ≤ 0.1 N·m peak, 1–3 Hz | pitch | — | 0.10 N·m |
| **Dynamic total** | | pitch | | **0.25 N·m normal, 0.35 N·m stall** |
| Static: module CoM (322 g at R 163) rotated to φ_c | at −45°: X_cm = −80 mm | pitch | | **0.37 N·m** (0.14 at ±15°, 0.27 at +30°) |
| Drag at the outer nails (±24 mm) | 1.5 N × 0.024 | yaw (about Z) | | 0.04 N·m |
| Servo-vs-idler mass asymmetry (≈ 20 g at 110 mm) | | roll (about X) | | 0.02 N·m |

Pitch is the axis that matters: it is the "hat rotates off backward" mode, the servo torque and the drag both excite it, and the module's own weight adds to it at the rear detents.

### 3.2 Holding moment from pad friction

Pads press along the sphere normal, so their normal forces produce no moment about C; only their friction does: M_hold = µ Σ N_i r_i with r the distance of each pad from the pitch axis (FH, OC: 90 mm; temples: 62 mm). Nominal loads: FH 5.5 N, OC 5.5 N (3 N clip preload each plus the share of the 4.7 N weight and the strap's pull-down), temples 2 N each from their sprung arms.

Σ N r = 2 × 5.5 × 0.090 + 2 × 2.0 × 0.062 = 1.24 N·m per unit µ → **M_hold = 0.37 N·m at µ = 0.3 (hair under the pads), 0.62 N·m at µ = 0.5 (forehead skin).** The pads are also a torsional spring (≈ 1 kN/m shear each at r ≈ 80 mm → ≈ 30 N·m/rad; halo inertia ≈ 0.01 kg·m² → ≈ 9 Hz resonance, foam-damped, above the stroke), so the 0.1 N·m servo torque rocks the halo ≈ 0.2°, 0.5 mm at the elbow axis, which the float absorbs.

### 3.3 Margins and whether a strap is needed

| Case | Disturbance | Hold (µ 0.3 / 0.5) | + strap preload moment 0.25 N·m | Margin without / with strap (µ 0.3) |
|---|---|---|---|---|
| Crown detents (0, ±15°), normal drag | 0.25 + 0.14 = 0.39 | 0.37 / 0.62 | 0.62 / 0.87 | 0.95 / **1.6** |
| Crown detents, stall peak | 0.35 + 0.14 = 0.49 | 0.37 / 0.62 | 0.62 / 0.87 | 0.76 / **1.3** |
| −45° detent, head upright, stall | 0.35 + 0.37 = 0.72 | 0.37 / 0.62 | 0.62 / 0.87 | 0.5 / **0.86** |
| −45° detent, leaning forward 30° (static moment falls to 0.13) | 0.35 + 0.13 = 0.48 | 0.37 / 0.62 | 0.62 / 0.87 | 0.77 / **1.3** |
| +30° detent, upright, stall | 0.35 + 0.27 = 0.62 | 0.37 / 0.62 | 0.62 / 0.87 | 0.6 / **1.0** |

Conclusion: **a retaining strap is needed** (no-strap is marginal at the stall peak even at the crown; the rear detents fail without it), and the rear detents are used leaning forward, where they also have full force (§2.3). µ 0.3 is the all-pads-on-hair pessimum; with the forehead pad on skin (µ ≈ 0.5) every "with strap" margin is ≥ 1.4. A slip is benign: the halo rotates a few millimetres, the float absorbs the engagement change, the stroke continues at W and the user re-seats by hand; that is why 1.3 at the stall peak is accepted. Bench test §9 R2.

### 3.4 The chin strap

**Tension.** Strap preload moment needed: 0.25 N·m from §3.3. The anchors are on the rails at φ_a = +12° (X +25, R 128, 35 mm ahead of the tragus); the strap runs down in front of the ear to under the chin. For a pitch rotation ρ of the halo the anchor moves ρ × (−128, 25) mm and the strap (direction (0.21, −0.98) from anchor to chin) lengthens by 50 ρ mm: the moment arm of the strap tension about C is 50 mm, so **2.5 N per side (5 N total) gives the 0.25 N·m** and adds ≈ 4 N of pull-down shared by the four pads (included in §3.2's loads). 2.5 N per side is a quarter of a bicycle-helmet strap and below the "jaw comfortable" threshold of ≈ 5 N; the user feels it as a light elastic.

**Breakaway and release (SR red line 10, §3.9).** 20 × 1.5 mm knitted elastic, k ≈ 0.15 N/mm per side, joined under the chin by a printed magnetic buckle (2 × N42 Ø 10 × 3 mm on 1 mm steel keepers, pull-apart 8–12 N measured, thumb-slide release < 3 N). Two one-handed ways off: slide the buckle (≈ 1 s), or lift the halo by its front handle so the elastic stretches 40 mm over the chin at ≈ 6 N and slips off (≈ 1.5 s, timed in §9 R2). A snag pulls the buckle apart at ≤ 12 N: no non-breakaway path exists.

**Jaw motion.** Talking and swallowing move the chin 2–5 mm, lengthening the strap by the same: tension rises 0.3–0.75 N per side, 0.6–1.5 N more pull-down on a pad set of ≈ 8 N/mm combined stiffness, so the halo moves ≤ 0.2 mm at 1–3 Hz. The float sits 5–6 mm off its down-stop at E8 with 24 mm of up-travel; a 0.2 mm (or even a 5 mm) halo motion moves the carriage and changes the nail force by nothing, because the dead weight does not know where the down-stop is. Only halo motion beyond 24 mm toward the scalp or 5–6 mm away from it changes the force, and the strap can produce neither.

**Routing.** From the anchors at X +25 the straps pass 35 mm in front of the tragus, never over the ear; the buckle sits 25 mm behind the chin point, off the throat.

## 4. Mass budget

| Group | Item | g |
|---|---|---|
| Hand module (engineered, MECH §3.1 / §6.5, lightened per §1.5) | XL330 | 18 |
| | float W1 (MGN9C block, riser, seat, palm, leaves, paddles, tips) | 90 |
| | yoke cheeks A/B (4 mm) | 20 |
| | crossbar + mast P21 (1.6 mm walls) | 32 |
| | MGN9 rail 70 mm | 27 |
| | down/up stops, scale, cleat, thumbscrews | 10 |
| | rail shroud G4 | 10 |
| | idler 625-2RS, shoulder screw, nut; horn disc + M2 screws | 12 |
| | fasteners, zero pin | 8 |
| | DXL cable on the head (0.4 m) + clips | 6 |
| | **module subtotal** | **233** |
| Carriage | C1 servo-side carriage (shoe, leg, cradle, guard shell, tube boss) | 28 |
| | C2 idler-side carriage (shoe, leg, idler housing, guard shell, tube boss) | 22 |
| | cross-tube Ø 8 × 1 × 260 mm aluminium, 2 × M3 cross-pins | 17 |
| | detent latch, Ø 3 steel pin, rubber band | 5 |
| | **carriage subtotal** | **72** |
| Halo | rail channels R1, R2 (240 mm arcs, 1.2–1.6 mm walls) | 52 |
| | front bridge B1 with clip leaf, forehead pad carrier, handle | 22 |
| | rear bridge B2 with occiput pad carrier, cable anchor | 18 |
| | temple arms T1, T2 (sprung) | 14 |
| | 4 pads (EVA + TPU plate + sleeve) | 13 |
| | elastic strap + magnetic buckle | 14 |
| | fasteners, shims | 8 |
| | **halo subtotal** | **141** |
| **Total on the head, W1** | | **446 g** |
| with +30 g slug (W2) | | 476 g |
| with +60 g slug (W3) | | 506 g |

Honesty note: the brief's "module ≈ 150–200 g" is not what the engineered module weighs: 346 g in MECH §3.1 with cradle, idler housing and guards, 305 g here after lightening and merging those into the carriages. The structure replacing arm, adapter, hinge, frame and carrier beam is 141 g. **The 500 g line is met at W1 and W2; W3 sits on it**, so W3 is reached with the 0.3 N trim cord (§2.3, 0 g) rather than the +60 g slug, and the halo is weighed before every W3 session. If the sensation gate needs 1.5 N routinely and the as-built halo exceeds 440 g, the mass rule takes ≈ 60 g of force range: risk R1.

**Centre of mass.** Module 305 g at R ≈ 163 mm from C (float and hand at R ≈ 120, servo, yoke, rail and carriage at R ≈ 180); halo 141 g at R ≈ 118. Combined R_cm = 149 mm, 59 mm above the apex at the crown detent, on the mid-sagittal plane within ±3 mm (the cross-tube bosses are shaped to balance the 20 g servo-side excess). At −45° the combined CoM moves to X −80 (the 0.37 N·m static moment of §3.1); at +30°, X +58.

**Load sharing and comfort.** Crown detent, upright: weight 4.4 N plus strap pull-down 4 N. The forehead and occiput surfaces are inclined 65–68°, so each unit of pad normal carries cos 66° + µ sin 66° ≈ 0.4–0.7 of vertical load; with the temple pads taking ≈ 30 %, FH ≈ OC ≈ 5.5 N (including the 3 N clip), TL ≈ TR ≈ 2 N. At −45° the static moment shifts ≈ 4 N from FH to OC (9.5 N, 3.4 kPa). 2.0–3.4 kPa on 8 mm EVA is a snug cycling helmet; the 2.5 N strap is lighter than any helmet; the 20-minute wear test on Michael (§9) finds hot spots, equalised with 3 mm shims. Nothing rests on the crown, the ears or the superficial temporal artery.

## 5. Coverage

**Reach.** Six detents at 15° pitch, φ_c = +30°, +15°, 0°, −15°, −30°, −45° (Ø 3.2 mm holes in the channels' outer walls at R 130; a printed latch lever on the servo-side leg drops a Ø 3 mm steel pin through the leg into the hole, held by a rubber band; the idler side follows through the cross-tube). On the scalp that is the arc from 47 mm in front of the vertex to 71 mm behind it, and with the hand's own ±18 mm contact chord the nails cover **+65 mm to −89 mm of sagittal arc from the vertex: the whole crown and the upper occiput**, stopping 35 mm behind the hairline (the knuckle plate's front edge at the +30° detent is 30 mm behind it: SR red line 6) and 30 mm above the inion. The rails run 15° beyond the end detents so the 40 mm shoe stays inside the channel.

**Direction.** The stroke is sagittal (fore–aft) at every detent; the yaw joint of DF §1.4 is gone with the frame. 45°/90° directions, if the sensation gate wants them, come from an indexed 0/45/90° plate between the leg and the cradle (Stage 3, 15 g) or, for 90°, from the lateral arch rejected below. For SP1 the matrix keeps direction = sagittal, with-grain over the crown toward the back (HI H-5.1): the bidirectional rake is the frozen primitive anyway.

**Repositioning.** Release the hold-to-run button (servo off, nails resting at W), lift the latch with the other hand, slide the carriage to the next detent, let the latch drop, press the button. Nothing is lifted off the head; the float keeps the nails on the scalp during the slide at W, so the move itself is a slow with-grain stroke (push the carriage backward, never forward, when hair is long). 5 s per move.

**Back of the head leaning forward: yes.** At the −45° detent with the head pitched forward 30–45° in the face cradle, φ_eff is −15° to 0°, the force is 0.97–1.0 W and the stability margin is 1.3 (§3.3). The occiput pad is 25 mm above the inion, so the module never reaches the nape, the nuchal ridges or bare neck skin (RT2 §3's 2 mm-contact-length hazard); the lower occiput stays out of scope for SP1.

**Second, lateral (ear-to-ear) arch: rejected.** (1) The module is 254 mm wide across Y; carried to the parietal side at a 50° tilt about X, its down-slope end (servo or idler, 110–127 mm from centre) drops 85–95 mm below the elbow axis and lands within 20 mm of the ear: SR red line 6. (2) A lateral rail pair crosses the sagittal channels at the crown and adds 60–80 g on a budget already at the line at W3. (3) The parietal lanes are not in the frozen matrix. Lateral stabilisation comes from the two temple pads instead (§1.3).

## 6. Safety

**Donning/doffing.** Spread the clip 4 mm by the forehead handle, drop the halo on from the front with the OC pad finding the occiput, let the forehead pad close, snap the buckle: 5 s two-handed to don. Doff one-handed: lift the front handle up and back; the elastic strap slips over the chin and the halo comes off, ≤ 2 s (the hold-to-run button is in the other hand and has already been released, so the servo is off). Measured in §9 R2. Nails leave the scalp after 5–6 mm of lift (the float sits that far above its down-stop), i.e. in the first 0.2 s.

**Power loss, e-stop, watchdog, stall: limp at W.** Losing the actuator rail (e-stop, hold-to-run, brown-out < 4.0 V per ADD-1 ruling 7, comm loss) torques the XL330 off; the yoke is free and the hand stays where it stopped, pressed at W cos φ_eff ≤ 1.5 N, 0.5 N per nail, on a free float. SR red line 8 allows "lifted-off or limp"; this is limp. RT2 §8 ruled "lifted" for the monitor-arm *because* the hand was referenced to the desk: the reflexive exit (neck extension) drove the crown into a limp hand on a rigid arm (RT2 §5), a stopped stroke left a trapped strand loaded, and the limp state was indeterminate. Here the first argument inverts: the hand is referenced to the head. No head motion, flinch or exit can raise the force, because the only ground path is the halo, which moves with the head; raising it needs the float driven 24 mm to its up-stop, i.e. the halo pushed 24 mm into the skull against four pads and the clip, which a head cannot do to a hat. A snagged strand is held at ≤ µW ≈ 0.3–0.5 N until the halo is lifted, a resting finger's load, under the 0.36 N pluck floor for most of the W range. The state is determinate: W, on the scale. Residual: with the servo off the arm does not park; the firmware still parks at +25° on any fault that leaves the servo powered (DF §2). If the SAFETY gate wants a mechanical lift on rail loss, the cheap option here is a park bias: a 0.5 mm elastic from yoke cheek to carriage leg pulling the arm toward +25° with ≈ 0.05 N·m (0.6 N tangential-equivalent), enough to swing the hand to the lifted end against µW at W ≤ 1.2 N; 2 g, 1 h, and the goal-current limit becomes asymmetric by +0.6 N in the lifting direction. Baseline: limp-at-W plus manual lift; the bias is the gate's option.

**Flinch and head jerk ±20 mm.** The halo follows the head through the pads; the only relative motion is the halo's inertial lag, F/k = m a / k ≈ 0.45 kg × 5 m/s² / 8 kN/m ≈ 0.3 mm, and the float's own inertia (§2.4: ≤ 0.95 N for 20–40 ms, ≤ 0.3 N per nail). RT2 §3's "rigid stage after 16 mm" does not exist: there is no rigid ground. A sneeze or sit-up moves the hand with the head.

**E-stop, hold-to-run, snag reflex.** Unchanged: 5 V brick → NC 22 mm e-stop on the desk → handheld hold-to-run → OpenRB-150 VIN; firmware watchdog, ±28° limits, goal-current ≈ 1.2 N tangential-equivalent, lift-never-reverse on current rise (HI H-5.9). The hold-to-run button's own cable and the servo cable both run to the desk.

**Ears and eyes.** Nearest moving part to the ear canal: the rail-channel shoe at 114 mm; temple pads (static) at 56 mm; strap 35 mm ahead of the tragus. Nothing moves above the eyes: the forehead pad and bridge struts are static and stop 20 mm above the brow; the module's front-most point at the +30° detent (the crossbar) is 95 mm above the brow line and behind the hairline. The front bridge is a fixed guard between the module and the eyes in the sense of SR red line 6.

**Cable routing.** The X3P servo lead leaves the cradle downward, follows the servo-side leg into clips on the rail's outer face, runs back to the rear bridge and leaves the head at the occiput pad carrier through a P36 strain relief to a 1.5 m extension. It never crosses the float, the yoke's sweep or the hair canopy; its only exposed length on the head is 45 mm from the skin. The X3P connector pulls apart at ≈ 5–10 N, so a tug disconnects it (comm loss → torque off) before it can drag the halo.

## 7. Noise

The structure-borne path is new: XL330 gear noise (2–4 kHz, plus the 1–3 Hz stroke thump) → cradle → carriage leg → shoe → rail channel → bridges → pads → frontal and occipital bone. The monitor-arm rig has no such path. Mitigations, in the order they pay: (1) the servo sits in the cradle on four 2 mm TPU 90A isolator pads and the back-face M2 screws pass through TPU grommets, so the cradle sees the servo through 70A–90A rubber, not PETG; (2) each pad is EVA on a 2 mm TPU 85A plate, a second soft layer in series with the bone; (3) the forehead pad, the most bone-conductive one, gets the softest EVA (25 Shore A); (4) the detent pin seats in a TPU sleeve so the latch does not rattle at the stroke frequency; (5) the halo-on-pads resonance (≈ 9 Hz, §3.2) is above the stroke harmonics that matter and heavily damped. Airborne: the XL330 at 0.3 m is ≈ 45–50 dBA; at the ear, 0.15 m from the servo, ≈ 50–55 dBA, inside the ≤ 60 dBA target and the 70 dBA limit (SR §2.7). Bone conduction cannot be measured on the mannequin; the test is on Michael with the hand lifted (no scalp contact), servo stroking at 2 Hz, ear plugs in and out, rated 0–7; fail if the plugged rating is ≥ 3 ("noticeable hum") after mitigation (1)–(3). The servo stays in the yoke as required.

## 8. Build

**XL330-M288-T facts (bom-verified.md §11, binding):** no side mounting holes; 4 × Ø 1.6 mm (M2) holes on a 16 × 30 mm pattern on the horn-end face and on the back face; output axis 9.5 mm from the horn-end face; horn Ø 16, PCD Ø 12, M2 × 6; connectors on the 23 × 34 mm side faces. C1 therefore mounts the servo through its **back-face holes**: the cradle's outboard wall (Y −124 to −127) carries 4 × M2 × 6 on 16 × 30, the cradle floor datum is 9.5 mm from the horn-end face, and the horn disc P16 is re-cut to PCD Ø 12 / 4 × M2. The MECH §5.3 strap P14 and the "M2 side screws [VERIFY]" are deleted. **Supply:** the XL330 is on a 2-month back-order at robotis.us; order from ROBOTIS Korea (DHL, about a week) in the first cart.

**New printed parts** (PETG unless stated, 0.2 mm layers; W/I = perimeters/infill):

| # | Part | Qty | Size (mm) | Notes |
|---|---|---|---|---|
| C1 | Carriage, servo side: shoe 40 × 14 × 18, leg 4 × 24 × 70, cradle with back-face M2 pattern, ±32° bumper lugs, zero-pin bore, guard shell, tube boss, latch pivot | 1 | 60 × 30 × 110 | lying on its side, 4/40 %, PTFE tape on shoe faces |
| C2 | Carriage, idler side: shoe, leg, 625-2RS bore (Ø 16 press) with ±1.5 mm alignment slots, guard shell, tube boss | 1 | 60 × 20 × 100 | as C1 |
| R1/R2 | Rail channel, left/right: C-section 16 × 20, walls 1.6 (1.2 side walls), R 120/140 arc φ −60°…+45°, 12 mm top slot, 6 detent holes Ø 3.2, strap anchor boss, temple-arm socket, cable clip bosses, bridge sockets | 1 + 1 | 240 chord × 65 × 16 | flat on a 256 bed (two-piece lap splice on a 220 bed), 3/30 %, splice M3 × 2 |
| B1 | Front bridge: two 6 × 10 struts from the rail ends to the forehead-pad carrier; 2 mm clip leaf with M4 thumbscrew; grab handle 20 × 60 | 1 | 250 × 70 × 60 | 3/30 %, 1 × M4 insert |
| B2 | Rear bridge: two struts, occiput-pad carrier, cable strain-relief clip | 1 | 250 × 60 × 50 | 3/30 % |
| T1/T2 | Temple pad arm, sprung, 3 shim positions | 2 | 50 × 12 × 40 | 4/40 % |
| L1 | Detent latch lever, Ø 3 pin, TPU sleeve | 1 | 30 × 8 × 20 | 4/100 % |
| K1 | Buckle halves with magnet pockets Ø 10.2 × 3 and keeper discs | 2 | 30 × 24 × 8 | 4/100 % |
| I1 | Servo isolator pads TPU 90A 2 mm; pad plates TPU 85A 2 mm (4) | 4 + 4 | — | TPU |

**Reused unchanged from cad/frame and cad/tips:** P16 (re-cut PCD), P19–P35 (yoke, crossbar/mast, shroud, stops, scale, riser, cleat, wrist seats, cap, knuckle plate, boot frame, palm, root bars, template), P36, P37–P40, P43, P46, P47, T1–T4 and all tips. P13/P15/P17/P18 are not printed; their geometry is copied into C1/C2 in gen_frame_stl.py (`xl330_pocket`, bearing-bore and guard helpers exist). **Deleted:** P1–P12, P14, P41, P42, P44, P45.

**Bought parts, delta vs the hand module alone:** Ø 8 × 1 mm aluminium tube ($5), 8 mm EVA sheet ($6), 20 mm knitted elastic ($3), 2 × N42 Ø 10 × 3 magnets and keepers ($3), X3P extension 1.5 m ($4), ≈ 180 g PETG and 15 g TPU ($6): **+$27**. Not bought versus the monitor-arm rig: arm ($36), ballast ($45), electromagnet ($8), hinge springs ($10), 2020 pack and brackets ($35–48), Dyneema, pulleys, 623ZZ ($8): **−$140 to −$155 net**. The 625-2RS, shoulder screw and MGN9 kit stay.

**Hours:** 9 h printer time; 7 h hands-on (servo/idler alignment per MECH §13 step 9, rail splice and bridges, pads and strap, head fit and shims, §9 bench tests) against ≈ 12 h for the stand's adapter, hinge, springs, magnet, frame and arm.

## 9. Risks and the bench tests that retire them

| # | Risk | Bench test | Pass |
|---|---|---|---|
| R1 | As-built mass > 500 g at W3; the force range shrinks | Kitchen scale, halo complete, each W setting | ≤ 500 g at W2 with slug; W3 by trim cord; else lighten C1/C2/R1/R2 walls |
| R2 | Halo slips or rotates on the head under drag or at the rear detents; strap too weak or uncomfortable | Mannequin with wig, halo on, servo stroking at 2 Hz; spring scale pulls 1.5 N at the nails in ±X at each detent, upright and at 30° forward lean, strap on/off; marker dots on the pads and skin; also one-handed doff timed, buckle pull-apart measured | ≤ 2 mm pad migration in 60 s at every detent with strap; doff ≤ 3 s; buckle 8–12 N |
| R3 | Hair entering the rail channel or the detent latch | Long Kanekalon wig draped over the sides; slide the carriage through all detents 20 times, both directions; comb-through and count | 0 strands in the channels or latch; otherwise add the inner skirt or restrict to ≤ 5 cm hair |
| R4 | Bone-conducted servo noise through the pads | On Michael, hand lifted (no contact), 2 Hz stroke, ear plugs in/out, 0–7 rating; phone SPL at the ear | ≤ 60 dBA at the ear; plugged rating ≤ 2 after §7 (1)–(3) |
| R5 | Head-shape mismatch along the arch: E varies > ±6 mm between detents so the float bottoms or never floats | Apex gauge P43 at each detent on Michael and the mannequin; pointer reading at mid-stroke | E within 8 ± 6 mm at every detent using the ±6 mm radial trim; else re-cut the rail radius (one reprint) |

Also run MECH §14's float, breakaway and proof tests unchanged, plus the tilt test of §2.3 (mannequin pitched 0/15/30/45°, nail force by the scale under the tips: N = W cos φ_eff ± 0.05 N).

## 10. Verdict

Better than the monitor-arm stand for SP1 on the four things that decided the tournament against head-worn designs, because the float answers all of them: the force reference is the dead weight and does not drift with the head (J2 F1 is answered, not dodged); the flinch and reflex-exit hazard that forced RT2's electromagnet lift disappears because the hand is referenced to the head; nothing is clamped to furniture, there is no ballast, no desk, no 1.1 kg at the end of an arm, and Michael can sit, lean forward or walk to the mirror; it is $140 cheaper and closer in form to the product. It is worse on four things, honestly: the engineered module weighs 305 g, not 150–200, so the halo lives at the 500 g line and buys force range with mass; the servo now has a bone path to the skull; the sliding rails sit 30–45 mm from the hair on the sides; and the de-energised state is "limp at W" with a manual lift rather than a mechanical lift. I would choose the stand after all if the sensation gate needs 1.5 N routinely and the as-built halo exceeds 440 g (R1), if the safety gate rules that limp-at-W is unacceptable even with the head as the reference and the park bias is not enough, if R4 shows the servo hum through the forehead is intrusive, or if Michael's head profile makes E swing more than the ±6 mm trim between detents (R5). Each of those is a two-hour bench answer on the printed halo before any human session, and the hand module is identical either way, so the halo is the cheaper first try.
