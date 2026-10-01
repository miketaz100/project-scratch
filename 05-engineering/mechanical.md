# SP1 "Float-Arm" Mechanical Design (MECH lead)

**Project SCRATCH · 05-engineering · 2026-10-01 · Mechanical Lead.** Builds to 05-engineering/DESIGN-FREEZE.md (cited as "freeze §x"). Inherits 01-foundations/safety-requirements.md ("safety §x"), hair-interaction.md ("H-x.y"), tip-interface.md ("TI §x"), component-landscape.md ("CL §x"), 04-redteam/redteam-2-mechanical.md ("RT2 §x"), 03-tournament/judge-2-engineering.md ("J2 §x"), 05-engineering/test-protocols.md ("TP §x"), electronics-firmware.md ("EF §x"), tips.md ("TIPS §x") and cad/tips/paddle_with_pocket.scad ("paddle SCAD").

Status: complete first issue. Numbers I chose where the freeze left a range are marked **[MECH CHOICE: range]**. Numbers that must be checked against a vendor drawing before printing are marked **[VERIFY]**. Calculations were run in a scratch script (leaf stiffness with clamp correction, paddle roll, lift-off geometry, hinge dynamics); the formulas are given inline so the build reviewer can repeat them.

## 1. Scope and deviations from DESIGN-FREEZE

This file owns freeze §1 items 2–7 and the mechanical side of item 8 (freeze §4): VESA adapter, fail-safe hinge, module frame, yaw joint, elbow servo mount, guards, arm (yoke), radial float, wrist, hand (palm, leaves, knuckle plate, paddle exits) and the face cradle, plus every printed part above the paddle and every bought mechanical part. The paddle itself and the TM1 tips belong to the tip lead (TIPS §8); I only override parameters the paddle SCAD exposes and request one new parameter. Electronics placement (board, magnet, button, e-stop, pots) is given mechanically here; wiring stays in EF §1.

The headline: the freeze architecture survives intact (dead weight on a vertical MGN9 float, one XL330 elbow, geometric lift-off at both stroke ends, three leaf-sprung nails, electromagnet-latched spring lift on the actuator rail), but three of its dimensions cannot be built as written. The hand with real paddles is about 60 mm tall and about 170 mm wide, the float needs 28 mm of free radial travel above it, and the elbow axis is only 84 mm above the nail tips. Nothing fixed can sit above the hand, so the servo moves beside it and the arm becomes a two-sided yoke. Every change is listed below; none is made silently.

| # | Freeze text | What this design does | Reason |
|---|---|---|---|
| D1 | §1.7 paddles "1 mm thick" | Paddles are the tip lead's paddle_with_pocket: 14 × 9 mm nose, 22.8 × 17.8 mm at the knuckle plate, 28 × 14 mm root, 44.0 mm from leaf floor to nail edge | A TM1 pocket (10.3 × 4.3 × 12.5 mm) needs a body at least 9 mm thick (TIPS §8 item 5). Freeze error; knuckle-plate exits are sized to the real paddle (§8.7). |
| D2 | §1.7 "three nails at 20 mm pitch in Y" | **24 mm pitch** in Y (span 48 mm) | Resolves conflict (b): with the leaves along Y every paddle rolls about X as its leaf bends (1.6–1.9° per mm of tip travel) and adjacent nail tips converge. At 20 mm pitch the worst tip gap falls to 0.4 mm (W tips) even with roll pre-tilt; at 24 mm it stays at 8.4 mm (W) and 4.4 mm (B45-12). 24 mm is inside the human 20–25 mm spread-finger range (TI §6). §8.7 gives every gap. |
| D3 | §1.7 draft "≥ 10°" (tip lead built 5° on Y faces) | Paddle SCAD override `DRAFT_Y = 10`; centre paddle gets a new `RISER = 9` mm straight extension above z = 25 mm | 10° now fits (6.2 mm paddle gap at the plate at 24 mm pitch). The riser lifts the centre leaf one level so it can cross over the left paddle (§8.2). Requested of the tip lead, flagged here. |
| D4 | §1.7 "≥ 4 mm clearance holes covered by a TPU boot or slit silicone" | One shared slot in the knuckle plate, ≥ 4 mm clear of every paddle, sealed by one slack 0.25 mm silicone membrane bonded to each paddle (no sliding contact) | Individual 4 mm-clearance holes overlap at any pitch below 26 mm with 10° draft. A slit sheet rubbing the paddles adds 0.03 N of friction per nail (about 10 % of the nail force); a bonded slack membrane adds none. |
| D5 | §1.7 "travel 8–10 mm to a hard stop" | Leaf travel to the hard stop **5.0 mm** [MECH CHOICE: 4.5–5.5 mm] | Paddle roll at 8 mm closes adjacent tip gaps below 3 mm; RT2 §4 independently asks for a 5–6 mm stop for leaf fatigue. Per-nail force at the stop is 0.6–0.9 N (leaf) and the dead weight (≤ 1.5 N) still caps the force while the float is free. |
| D6 | §1.4–1.5 servo above the hand, arm bracket on the horn | Servo **beside** the palm on the −Y side, horn facing +Y as frozen, driving a two-sided yoke with an idler bearing on the +Y side; rail on the yoke's front mast, carriage linked to the wrist by a short L-bracket | Stack check: knuckle plate 37.5 mm, leaves 40–53 mm, palm top 66 mm, wrist 74 mm above the centre nail edge; the float needs 28 mm more above that, i.e. up to Z = 102 mm, past the elbow axis (84 mm) and the XL330 body (bottom 10 mm below its axis). The yoke also removes the horn side-load RT2 §4 flagged. |
| D7 | §1.5 "MGN9H" carriage | **MGN9C** block (16 g) on the same 100 mm MGN9 rail; MGN9H allowed if the scale says the budget holds | Bare floating weight must be ≤ 92 g (TP §Q2); the H block is 26 g. Moment loads are below 0.06 N·m, far inside either block's rating. |
| D8 | §1.4 module frame "120–150 mm" | 2020 extrusion: 270 mm elbow-carrier beam, 90 mm post, 80 mm spine | The servo, palm (169 mm) and idler sit side by side in Y. |
| D9 | §0 "scalp sphere centred at (0, 0, −90)" with apex at O | Apex at Z = +4 mm, sphere centre (0, 0, −86) mm; O = centre nail edge at mid-stroke with the float on its down-stop | §0 and §1.5 disagree by the 4 mm engagement: H = 80 mm from axis to apex with the axis at +84 mm puts the apex at +4 mm. All geometry here uses the §1.5 numbers (which the frozen lift-off check uses). |
| D10 | §1.7 "hard stop (absolute cap ≤ 2.4 N/nail)" | The leaf stop is a backstop, not the absolute cap. While the float is free the cap is the dead weight W ≤ 1.5 N; only after a head rise of more than 24 mm (float on its up-stop) plus 5 mm of leaf does force rise further, until the fail-safe hinge yields at about 9 N total at the nails | Statics; RT2 §3 made the same point. Procedural cover: hold-to-run release. Flagged in §15. |
| D11 | §1.3 "an extension spring (6–10 N)" | **Two** extension springs in parallel, each 6.5 N at working extension, acting through cords over two bearing pulleys | One spring at 10 N cannot both hold the module at the up-stop with the +100 g slug and lift it in time; two give redundancy (§4.8). Read as 6–10 N per spring. |
| D12 | §1.5 lift-off figures (4.1 mm at 13°, 19.9 mm at 25°) | Kept, but those are the gap for a tip at L = 80 mm. With the float on its down-stop (L_max = 84 mm) the real tip clearance is 4 mm less: 15.9 mm at 25°, 24.5 mm at 28° | Clarification, not a change; §9 gives both columns. |
| D13 | §1.7 torsion "~2° at 0.3 N drag" | 3.6–4.2° (outer) and 4.3–5.0° (centre), i.e. 2.8–3.2 mm of tip motion in X | GJ/L of a 0.3 × 12.7 mm leaf is 180–210 N·mm/rad; the drag acts 44–53 mm below the leaf. Symmetric in ±X and useful as tangential compliance (about 0.1 N/mm). |

Not deviations but decisions the freeze left open: the stagger is read as left nail at X = −8 mm, centre at 0, right at +8 mm (a diagonal step; §8.1); preload shares 0.8 / 1.0 / 1.2 are set by leaf rate, not shims (§8.3); the electronics tray lives on the VESA adapter so only the DXL cable crosses the hinge (EF §1.3 row 12).


## 2. Coordinate frame and top-level dimensions

**Frame (freeze §0, with D9).** Z up (gravity −Z), X = stroke direction, Y = across the stroke (nail pitch). Origin O = edge of the centre nail at mid-stroke (arm at θ = 0°) with the float resting on its down-stop and the leaves unloaded. Elbow axis: the line parallel to Y through (X 0, Z +84 mm). L_max = 84 mm from the axis to the free centre-nail edge at the down-stop. Scalp: sphere R = 90 mm, apex at (0, 0, +4 mm), centre (0, 0, −86 mm), so H = 80 mm from axis to apex and nominal engagement e = 4 mm (freeze §1.5). In contact at mid-stroke the centre edge sits on the apex at Z = +4 mm. All Z values below are with the float on its down-stop, arm at 0°, module latched down, unless stated.

**Plan layout (looking down, +X to the right, +Y up the page).** The hand is centred on Y = 0 under nothing fixed. The XL330 sits at Y −101 to −127 mm with its horn facing +Y; the idler bearing sits at Y +101 to +111 mm. The yoke's two cheeks (Y ±93 to ±98 mm) carry a crossbar in front of the palm (X +45 to +57 mm) with a vertical mast in its middle; the MGN9 rail is on the mast's rear face and the carriage links back to the wrist over the palm. The fixed frame is behind (X ≤ −15 mm) and above (Z ≥ 130 mm) everything that swings or floats.

**Dimensioned stack, VESA plate to nail tip (Z and X in mm, global frame).**

| Level | Item | X | Z | Notes |
|---|---|---|---|---|
| 1 | Monitor-arm VESA plate (vertical, facing +X), ballast stack between it and the adapter | −139 to −126 | 72.5–147.5 (VESA 75 holes centred at 110) | 4 × M4 × 50, freeze §1.2 |
| 2 | VESA adapter plate (printed) | −126 to −120 | 25–170 | carries hinge ears (to X −60), magnet arm, pulleys, electronics tray |
| 3 | Spring pulleys (2, at Y ±60) on the adapter top edge; springs hang down its rear face | −123 | 148 | cords run forward, horizontal, to the post |
| 4 | Fail-safe hinge pin (M6, along Y, ears at Y ±30) | −60 | 84 | 60 mm behind the elbow axis, level with it (freeze §1.3) |
| 5 | Electromagnet face (P20/15, facing +X) / keeper on the keeper lever | −66 | 34 | r_m = 50 mm below the hinge |
| 6 | Module frame post (2020, vertical) | −70 to −50 | 92–196 | cord bar at Z 148 (p = 64 mm above the hinge) |
| 7 | Module frame spine (2020, horizontal, bracketed to the post's front face) | −50 to −15 | 196–216 | reset tab at its front end |
| 8 | Yaw joint plates, 70 × 70 mm (frame side / carrier side) | −60 to +10, axis −25 | 190–196 / 184–190 | 40 × 40 mm M3 pattern, 45° holes (freeze §1.4a) |
| 9 | Elbow carrier beam (2020, along Y, 270 mm) | −35 to −15 | 164–184 | drop legs at Y ±115 to ±135 come down to the axis |
| 10 | Elbow axis: XL330 horn (−Y side) and idler shaft (+Y side) | 0 | 84 | servo body Z 74–108 [VERIFY axis 10 mm from body end] |
| 11 | Yoke crossbar (moves with the arm) | +45 to +57 | 80–96 | Y −98 to +98 |
| 12 | Rail mast and MGN9 rail, 100 mm | mast +40 to +45; rail top face +33.5 | rail 68–168, mast top an arc R 90 mm about the elbow axis | carriage face at X +30 |
| 13 | Float down-stop thumbscrew tip / up-stop | +29 | 69 / 69 + 28 | sets L_max 82–88 mm (e = 2–8 mm) |
| 14 | Carriage (MGN9C) at the down-stop | +30 to +40 | 74–103 | riser (L-bracket) X +27 to +30 |
| 15 | Weight post top / upper wrist seat | 0 | 108 / 69–74 | M8 slugs on Ø 8 mm post |
| 16 | Wrist seat plane (keyed magnetic seat) | 0 | 69 | h = 69 mm to the centre edge |
| 17 | Palm lid top | −26 to +26 | 66 | palm 52 × 169 × 33 mm overall |
| 18 | Centre leaf floor (level 1) / outer leaf floors (level 0) | 0 / ∓8 | 53.0 / 40.4 | leaves along Y |
| 19 | Knuckle plate underside (spherical, R 90 mm) | | 37.5 at centre, 33.9 at outer nails | 25.0 mm above each pocket mouth |
| 20 | Pocket mouths (TM1) | | 12.5 / 8.9 | |
| 21 | Nail edges: centre / left and right | 0 / −8, +8 | 0 / −3.6 | outer nails at Y −24, +24 |
| 22 | Scalp apex (contact) | 0 | +4 | |

**Swept-volume checks (the CAD agent must re-run these with the final solids, ≥ 8 mm clearance each).** (a) Palm rear-top corner (X −26, Z 66) at θ = ±28°: reaches X −31, Z 80; at the float up-stop Z 112; elbow-carrier beam underside is at Z 164: 52 mm clear. (b) Weight-post top (Z 108, Z 136 at the up-stop) swings to X −24, Z 130 at ±28°: 34 mm under the carrier beam. (c) Every arm-mounted point lies within R 91 mm of the elbow axis above the axis (mast top cut to an arc), so nothing on the arm rises above Z 175 at any angle; the yaw plates start at Z 184: 9 mm clear. (d) Palm ends (Y +81 and −88) versus the cheek inner faces at |Y| = 93: 5 mm and 12 mm in Y; the palm floats past the cheeks, so this is a constant sliding gap ≥ 3 mm, 70 mm or more above the scalp at that Y. (e) During the fail-safe lift everything forward of the hinge rotates together, so only adapter parts need checking: at the 25° up-stop the post top (Z 196) moves back 47 mm to X −107, 13 mm short of the adapter plate front face (X −120); the keeper lever bottom moves forward 19 mm, away from the magnet.


## 3. Monitor arm and VESA adapter

### 3.1 Masses and moment at the clamp

| Group | Mass | Basis |
|---|---|---|
| Moving module (everything hung on the fail-safe hinge, float included, no slug) | 733 g | itemised in the hinge script: 2020 post 90 mm 36 g, spine 80 mm 36 g, carrier beam 270 mm 130 g, drop legs 70 g, servo and cradle 41 g, idler 33 g, yoke cheeks 30 g, crossbar 45 g, mast, rail and stops 64 g, shroud 15 g, float 92 g, hinge knuckle 20 g, keeper lever 25 g, yaw plates 30 g, brackets 30 g, guards 16 g, cables 10 g, misc 10 g |
| Slug sets on the float | +30 g or +60 g (up to +100 g allowed, freeze §1.5) | |
| Fixed parts on the adapter | about 260 g | adapter 120 g, magnet 30 g, springs, cords and pulleys 25 g, electronics tray with OpenRB-150 and terminal block 70 g, fasteners 15 g |
| Module plus adapter | 1.0–1.1 kg | |

The module CoG (no slug) is at X −10.7 mm, Z 106 mm, i.e. 49 mm in front of the hinge; its gravity moment about the hinge is 0.355 N·m (0.414 N·m with a 100 g slug). That moment matters for §4; for the arm, the whole 1.1 kg sits at the VESA plate.

**Moment at the desk clamp.** With the arm extended 450 mm horizontally [MECH CHOICE: 350–500 mm] and the ballasted payload at 2.1 kg: 2.1 kg × 9.81 m/s² × 0.45 m = 9.3 N·m, plus the arm's own mass (typically 2.5–3.5 kg with its centre about 200 mm out, 5–7 N·m). A 2–9 kg arm is designed for 9 kg at the same reach (about 40 N·m), so the clamp is loaded to a third of its design. The desk must be solid (no glass top, no hollow-core edge thinner than 18 mm); fit the arm's steel reinforcement plate under the clamp.

### 3.2 Required arm and ballast

Required: single-monitor gas-spring arm, VESA 75 × 75 (and 100), **load range whose minimum is ≤ 2.0 kg** (common 2–9 kg arms qualify; 1–6.5 kg "light" arms are better and need less ballast), reach ≥ 400 mm, VESA centre reachable 300–650 mm above the desk, head **tilt ≥ ±45°** (rail plumb in pitch for crown and occiput aims), **head swivel (pan about a vertical axis) ≥ ±90°** for the yaw aims, head rotation (portrait/landscape) with a friction or lock screw, desk clamp for 10–85 mm desks. CL §5.4 lists the HUANUO/VIVO class at about $36. Below its minimum load a gas arm creeps upward (RT2 §4), so ballast to the arm's printed minimum plus 10 %: for a 2 kg arm, 2.2 kg − 1.1 kg = **1.1 kg ballast**.

Ballast is fixed to the arm, never to the hinged module (it would change the §4 moment balance): a stack of 3 mm mild-steel plates 100 × 100 mm (235 g each, 4 holes Ø 4.5 mm on 75 × 75 mm, laser-cut, or bought steel VESA extension plates) clamped between the arm's VESA plate and the adapter by 4 × M4 × 50 mm screws. Five plates give 1.18 kg and a 15 mm stack; start with five and remove plates until the arm holds its height without drifting (K2.14: ≤ 2 mm drift in 30 min).

### 3.3 VESA adapter (printed, part P1 in §11)

A 6 mm PETG base plate 140 mm (Y) × 145 mm (Z) with two vertical ribs, VESA 75 holes Ø 4.5 mm (counterbored for the ballast stack screws from the front). From its front face: two hinge ears at Y ±30 mm (10 mm thick, 28 mm tall, ribbed) reaching forward 60 mm to the hinge pin at X −60, Z 84; a magnet arm from the plate foot forward to the magnet seat at X −81, Z 34; an adjustable up-stop boss (M4 screw with a rubber cap) between the ears; an electronics-tray seat on the front face at Y +15 to +50 mm, Z 120–165 mm (clear of the post, which moves back to X −107 mm when lifted, and of the cords at Y ±60 mm). On the top edge: two pulley bosses at Y ±60 mm (623ZZ on M3 × 16 mm). On the rear face: two spring channels at Y ±60 mm (outboard of the arm's VESA plate, which spans ±50 mm) and two spring-anchor hooks at Z 30 mm.

**Electronics mounting locations (EF §1).** OpenRB-150, Wago rail node, rail perfboard (divider, TVS, 470 µF) and fuse holder: in the electronics tray P3 on the adapter's front face (fixed side of the hinge), so the electromagnet leads never cross the hinge and only the DXL cable does (EF §1.3 row 12). That cable runs tray → down the adapter → across the hinge with a 60 mm service loop in clip P36 → along the carrier beam → down the −Y drop leg to the servo: about 330 mm, so the servo's stock 180 mm cable is too short; use a 340 mm or longer ROBOTIS X3P cable [VERIFY length available]. Electromagnet: on the adapter's magnet arm (§4.4). SPEED and VARIATION pots, PERIODIC/HUMAN toggle and status LED: control panel P37 on the desk beside the e-stop, linked to the tray by a 1.0 m 6-core 26 AWG cable (3V3, GND, A0, A1, D4, D5). E-stop: the boxed TWTADE unit on its steel plate on the desk, under the free hand in the test posture (K3.11). Hold-to-run: the handheld housing P39/P40 on its 1.5 m cable, gland at the handle, zip-tie anchor on the carrier beam. USB-C from the tray to the laptop is tie-wrapped down the monitor arm.

### 3.4 Aim: 0°, 45°, 90° yaw (TP §Q6)

**Yaw is set with the monitor-arm head swivel**, which is a vertical axis on every arm of the specified class: mark 0°, 45° and 90° with tape index marks across the swivel joint (TP §M0) and set the head rotation (roll) screw tight so the module cannot roll. The freeze's internal yaw joint (40 × 40 mm M3 pattern, §5.4) is built with the 45° hole set the freeze and TP §Q6 ask for, but I checked it and it **cannot** serve as the Stage 1 aim: the elbow carrier is 270 mm long and at 45° its −Y end lands at X −120 mm, through the frame post. In Stage 1 it is a 0° or 180° joint (180° swaps which side the servo is on; unbolt, lift, rotate, re-bolt) and the interface Stage 3 needs. Pitch (rail plumb ±1°, TP §0) is set with the arm head tilt and checked with the phone inclinometer on the mast; roll with the head rotation screw and the inclinometer on the carrier beam.


## 4. Fail-safe hinge analysis

### 4.1 Hinge geometry

Hinge axis parallel to Y at X −60 mm, Z 84 mm (freeze §1.3: about 60 mm behind the elbow axis; I put it level with the axis, which gives the most vertical nail motion for a given angle). Pin: M6 × 80 mm socket-head screw used as a pin, nyloc nut, through the adapter ears (Y ±25 to ±35 mm) and a printed frame knuckle (Y −24 to +24 mm) with 0.5 mm PTFE or nylon washers between them; bores Ø 6.3 mm, drilled to size after printing. The knuckle is bolted to the bottom of the 2020 post. Rotation sign: lifting is the front (hand) going up, which turns the post top backward and the keeper lever (which hangs below the hinge) forward.

| Feature on the hinged frame | Position relative to the hinge | Role |
|---|---|---|
| Nail centre (in contact) | 60 mm forward, 80 mm below | rises 32.9 mm and moves forward 28.2 mm at the 25° up-stop |
| Keeper lever foot (3 mm steel keeper on its rear face) | 0 mm, 50 mm below (r_m = 50 mm) | held back by the electromagnet = working position |
| Cord bar on the post | 0 mm, 64 mm above (p = 64 mm) | two cords pull it backward = lift |
| Post rear face at 20 mm above the hinge | | strikes the rubber up-stop at 25° |

### 4.2 Module centre of mass and moment about the hinge

From the §3.1 mass table: 733 g at X −10.7 mm, Z 106 mm, i.e. 49.3 mm in front of the hinge: M_g = 0.733 kg × 9.81 m/s² × 0.0493 m = **0.355 N·m** holding the frame down; 0.390 N·m with the +60 g slug, 0.414 N·m with +100 g. Moment of inertia about the hinge: 3.5–3.9 × 10⁻³ kg·m² (plus 0.5 × 10⁻³ kg·m² allowance in the timing check). Gravity alone holds the frame down, so the springs must overcome it, and the magnet holds only the surplus.

### 4.3 Spring selection

Two identical extension springs, each acting through a 1.0 mm braided Dyneema cord that runs horizontally from the cord bar on the post (Z 148 mm, Y ±60 mm) back over a 623ZZ-bearing pulley on the adapter's top edge (X −123 mm) and down to the spring, whose lower hook sits on the adapter's anchor at Z 30 mm. The cord keeps the line of pull horizontal, so the lever stays 64 mm (58 mm at 25°).

| Spring parameter (each) | Value |
|---|---|
| Rate | 0.095 N/mm (0.54 lbf/in) [MECH CHOICE: 0.08–0.11 N/mm] |
| Initial tension | 1.5 N [range 1.0–2.0 N] |
| Free length inside hooks | 64 mm (2.5 in) [range 55–70 mm] |
| OD / wire | 9.5 mm (3/8 in) / 0.8 mm (0.031 in) music wire, zinc plated, machine hooks |
| Working extension (latched) | 53 mm, force **6.5 N** (inside the freeze's 6–10 N) |
| At the 25° up-stop | 26.8 mm shorter, force 3.9 N |
| Maximum extended length required | ≥ 125 mm without set (working length 117 mm plus 8 mm margin) |

Source: McMaster-Carr "Precision Extension Springs" (catalogue family 9654K), select by OD 3/8 in, length 2-1/2 in, rate 0.5–0.6 lbf/in, maximum load ≥ 2.2 lbf (10 N), maximum extended length ≥ 5 in. [VERIFY: I could not confirm a single part number from here; the selection rule and the bench check below are binding, the part number is the BOM agent's to fill.] Amazon fallback: a 3/8 in OD extension-spring assortment, sorted on the luggage scale: accept a spring only if it reads 6.5 ± 0.5 N at 117 mm hook-to-hook and 3.9 ± 0.5 N at 90 mm. Buy four (two spares).

Moments: spring M_s = 2 × 6.5 N × 0.064 m = **0.832 N·m** latched. Net lift moment held by the magnet: 0.477 N·m (no slug), 0.442 N·m (+60 g), 0.418 N·m (+100 g). At the up-stop the net moment is still +0.185, +0.152, +0.130 N·m, so the frame stays up indefinitely with any slug.

### 4.4 Electromagnet holding force

Magnet: Adafruit 3872, P20/15, 5 V, 0.22 A, 25 N rated on thick steel, Ø 20 × 15 mm, M3 rear thread (EF §1.4, freeze §1.3), on the adapter's magnet arm at X −81 to −66 mm, Z 34 mm, face toward +X. Keeper: 25 × 25 × 3 mm mild-steel plate (full flux return needs ≥ 3 mm and ≥ Ø 20 mm) on the keeper lever, with one layer of 0.08–0.1 mm PTFE tape on the magnet face to stop residual magnetism from holding the keeper after power is cut.

| Load at the keeper (r_m = 50 mm) | Force |
|---|---|
| Static, net spring minus gravity, no slug / +100 g | 9.5 N / 8.4 N |
| Plus nails resting on the scalp (W ≤ 1.5 N at 60 mm: 0.09 N·m) | +1.8 N |
| Plus servo reaction couple at the 450 mA current limit (0.16 N·m, EF §4.2, K_t 0.354 N·m/A) | +3.2 N |
| Worst case while running | **14.5 N** |
| Available: 25 N × 0.9 (tape gap) × 0.85 (coil warm after 20 min, about +8 % resistance) | 19 N cold-to-warm; 22.5 N cold |
| Margin | 1.3 worst case running, 2.0 static |

If the frame ever unlatches during a run (K4.8, L7), the fix is the P25/20 (Adafruit 3873, 50 N, EF fallback) on the same arm with a Ø 25 mm seat, not a stronger spring. The magnet also sets the **frame overload yield**: an upward push at the nails lifts the frame when push × 60 mm + 0.477 N·m > F_hold × 50 mm, i.e. at about **8–11 N total** at the nails (warm to cold). That is the absolute normal-force cap when the float is jammed on its up-stop (D10).

### 4.5 Proof that loss of power lifts the nails ≥ 25 mm within 0.5 s

Time-stepped integration of I·φ'' = M_s(φ) − M_g(φ) (spring force falling with cord shortening, gravity lever shrinking as the CoG rotates over the hinge, I = 4.0–4.4 × 10⁻³ kg·m² including the allowance), from rest at the latched angle:

| Slug | Nail centre up 25 mm at | Reaches 25° up-stop at | Nail speed at the stop | Rise / forward shift at the stop |
|---|---|---|---|---|
| none | 80 ms | 91 ms | 0.85 m/s | 32.9 mm / 28.2 mm |
| +60 g | 85 ms | 97 ms | 0.78 m/s | 32.9 mm / 28.2 mm |
| +100 g | 89 ms | 102 ms | 0.74 m/s | 32.9 mm / 28.2 mm |

Add the release delay: the coil's L/R time constant is about 1 ms (22.7 Ω, tens of mH [EST]); the 1N5819 flyback diode stretches decay to a few ms and the PTFE shim removes residual hold; allow 30 ms. Total ≤ 0.14 s against the 0.5 s requirement (TP L5), a factor of 3.5. Clearance above the scalp at the stop: rise 32.9 mm minus the engagement e (the free tip was e below the surface) plus the scalp falling away 4.5 mm over the 28 mm forward shift: 33.4 mm at e = 4 mm, 29.4 mm at e = 8 mm, so ≥ 25 mm holds over the whole e = 2–8 mm range. Direction: the nails move away from the hinge as they rise; never aim with +X (away from the hinge) pointing at the hairline with the nails within 40 mm of it.

### 4.6 Up-stop and down-stop

Up-stop: M4 × 25 mm screw with a Ø 10 × 6 mm rubber bumper cap, in an insert in the adapter between the hinge ears, striking the post's rear face 20 mm above the hinge at 25° [adjustable 22–27°]. It takes a 0.74–0.85 m/s nail-speed impact; the bumper keeps the frame from rebounding below 20°. Down-stop (working position): keeper on the tape-covered magnet face. Its position is set by M3 washers under the magnet's rear screw (each 0.5 mm moves the frame 0.57° and the nails 0.6 mm); set it once so the rail is plumb with the module latched, then aim with the arm.

### 4.7 Reset procedure

Head out of the cradle (or nails at the +25° park, ≥ 15 mm clear), e-stop released, hold-to-run held: the rail powers the magnet and the servo (firmware INIT takes the arm to +25°, EF §4.1). With the free hand pull the **reset cord** (1.0 mm cord from the keeper lever, through a guide in the magnet arm, down the monitor arm to a toggle at the desk edge) with about 10 N until the keeper clicks onto the magnet, then let the cord go slack. Pushing the reset tab on the spine (X −15 mm) down with about 11 N does the same. Strokes begin only after the firmware's 1 s lifted hold. Every release of the hold-to-run lifts the frame and needs this re-latch; that is intended (freeze §1.10).

### 4.8 Under-voltage behaviour and failure modes

Holding force scales roughly with the square of coil voltage. The frame lifts when the hold falls below the load: statically below about 3.3 V (cold) to 3.5 V (warm); while stroking (14.5 N) below about 4.0 V. The XL330 runs from 3.7 V. Window of concern: 3.3–3.7 V with the servo browned out but the frame still latched, nails resting at the dead weight (≤ 1.5 N). Cover: the brick is regulated (a sag means a fault), the firmware's rail-sense input (EF §1.1, A2) can flag a low rail, and the hold-to-run release always drops the magnet.

| Failure | Effect | Detection / mitigation |
|---|---|---|
| One spring or cord breaks | Lifts in 0.25 s without a slug but does not hold at the up-stop; with +100 g it does not lift | Two springs inspected every session; one plug-pull lift check before every human session (added to K5, §14); spare springs |
| Both break | No lift; nails rest at W | same; hold-to-run release still kills the servo |
| Keeper tilted, dirty or misaligned | Hold drops; frame lifts early or will not latch | fail-safe direction; clean, re-seat; K2.12 |
| Residual magnetism holds after power-off | Delayed lift | PTFE shim; 9.5 N pull-off far exceeds residual (≈ 1 N [EST]) |
| Hinge or pulley binding (PETG swelling, dust) | Slower lift | L5 timing every build state; PTFE washers, bearing pulleys |
| Up-stop bumper lost | Hard stop on the post, rebound | visual check K1; bumper glued |
| Magnet wired anywhere but the rail | Frame stays latched with the servo dead | EF §1.6, bench test B1/B8 |


## 5. Module frame, elbow servo mount, yaw joint, guard plate

### 5.1 Frame material: 2020 extrusion with printed nodes (chosen)

Picked: **2020 aluminium extrusion** for the three long members (post 104 mm, spine 80 mm, elbow-carrier beam 270 mm), joined and terminated by printed PETG nodes. Reasons: (1) the carrier beam is 270 mm long, longer than the bed of most apartment printers (220–256 mm) and it must stay straight to ±0.3 mm so the servo and idler are coaxial; (2) the frame carries a permanent preload (13 N of spring pull, 9.5–14.5 N of magnet pull, 7–8 N of weight) for weeks, and PETG creeps under constant load while extrusion does not; (3) T-slots give free adjustment along Y for the idler alignment and along Z for the drop legs, so printing tolerances never stack into misalignment; (4) CL §5.1 already puts 2020 and bracket kits in the shopping list (about $25–30 and $10–18). Printed PETG is kept for every node, because those are short, compact and need complex shapes. Cut the extrusion square with a mitre box and hacksaw (deburr; ±0.5 mm on length is fine because every joint is slotted).

### 5.2 Elbow carrier (fixed, below the yaw joint)

The 270 mm beam runs along Y at X −35 to −15 mm, Z 164–184 mm. Two printed drop legs (P11, P12) bolt to its end faces (M5 × 10 into the tapped extrusion ends, plus two T-nut screws each) and come down and forward to the elbow axis. The −Y leg ends in the **servo cradle** (P13), the +Y leg in the **idler housing** (P15). Both legs carry a guard cap below them (§5.5).

**Idler.** A shoulder screw (Ø 5 × 25 mm shoulder, M4 × 6 mm thread) fixed in yoke cheek B with an M4 nyloc nut through a 625-2RS bearing (5 × 16 × 5 mm) pressed into the idler housing. The housing bolts to the +Y drop leg through two M3 slots (±1.5 mm in X and Z) so the idler can be aligned with the servo axis after assembly (§13 step 9): rotate the yoke by hand with the servo torque off; tighten when it swings freely through ±32° with no tight spot.

### 5.3 Elbow servo mount (Dynamixel XL330-M288-T)

Body 20 × 34 × 23 mm plus horn (26 mm deep overall, CL §1.2), 18 g, output axis parallel to Y, **horn facing +Y** (freeze §1.4b), axis at (X 0, Z 84 mm), long body axis vertical with the output 10 mm from the lower end [VERIFY against the ROBOTIS XL330 drawing; the cradle pocket is referenced to the output axis, so if the dimension differs only the pocket floor moves]. Servo body occupies Y −101 to −127 mm.

- **Cradle (P13):** pocket 20.4 × 34.4 mm, 23.5 mm deep, 2.5 mm walls, open at the horn face and at the cable end; a printed strap (P14) across the back clamps the body with 2 × M3 × 10 mm into inserts. Two M2 × 6 mm screws into the servo's side mounting holes locate it [VERIFY hole positions on the drawing; the strap alone holds it if they do not line up]. Cable exit downward with a 60 mm service loop (EF §1.3 row 12).
- **Horn interface:** the supplied XL330 plastic horn stays on the spline. A printed horn adapter disc (P16, Ø 24 × 3 mm) screws to the horn's M2 threaded holes with the M2 screws supplied with the servo [VERIFY the horn hole pattern: the disc is a 10-minute reprint if wrong], and yoke cheek A bolts to the disc with 4 × M3 × 10 mm on a 18 mm bolt circle into inserts in the cheek. The horn carries torque and about half the yoke weight (≈ 1.3 N radial at 4 mm from the servo face), not the cantilever load RT2 §4 warned about.
- **Hard stops:** a lug on cheek A strikes TPU bumpers on the cradle at ±32°, outside the firmware's ±28° (EF §3) and ±25° nominal.
- **Zero pin:** a Ø 3.1 mm hole through cheek A and the cradle flange, coincident at θ = 0°. The arm is top-heavy (rail, mast and carriage sit above the axis), so it does not hang plumb by gravity; zero calibration (EF §4.2 `zero`) is done with a 3 mm steel pin through this hole instead of "hand hanging freely". Flagged to ELEC (§15).

### 5.4 Yaw joint, Stage 1 (bolted)

Carrier-side plate (P9): 70 × 70 × 6 mm PETG on top of the carrier beam (2 × M5 T-nut screws), with 4 × Ø 3.4 mm holes on a **40 × 40 mm square** centred on the yaw axis (X −25 mm, Y 0). Frame-side plate (P8): 70 × 70 × 6 mm under the spine, with **8 × M3 heat-set inserts** on a Ø 56.6 mm circle at 45° spacing (the 40 × 40 square and the same square rotated 45°), so the carrier can be bolted at any multiple of 45°. Joined with 4 × M3 × 14 mm. As §3.4 explains, only 0° and 180° clear the frame post in Stage 1; Stage 3's yaw XL330 needs a bearing (a 100 mm lazy-Susan ring) under these plates because a 270 mm, 0.5 kg carrier on one horn repeats RT2 §4's side-load problem.

### 5.5 Guards

What the hair could reach, and what shields it:

| Guard | Covers | Geometry |
|---|---|---|
| G1 knuckle plate (P30) | everything inside the hand | spherical underside R 90 mm, all faces drafted ≥ 15° (H-6.3; freeze ≥ 10°), perimeter edge R 3 mm, slot edge R 1.5 mm with 15° lead-in, ≥ 4 mm to every paddle (§8.7) |
| G2 servo guard cap (P17) | horn, cradle, cheek A root | smooth PETG shell 2 mm thick under the cradle and around the horn, 15° drafted sides, R 3 mm edges; cheek A passes its inner edge with ≥ 10 mm all round through ±32° |
| G3 idler guard cap (P18) | bearing, shoulder screw, cheek B root | mirror of G2 |
| G4 rail shroud (P22) | lower 40 mm of rail, down-stop block, carriage at the down-stop | U-channel fixed to the mast, closed bottom, 2 mm walls, drafted 10° outside; the riser leaves through a 25 mm wide slot that is ≥ 10 mm clear of it on both sides |

The servo and idler sit at |Y| ≥ 101 mm, 75 mm or more above the scalp at that Y on an R 90 mm head, and the rail's lowest point is 71 mm above the scalp at X +35 mm, all outside the 30 mm exclusion zone of H-6.1 for 2–8 cm hair. The only parts inside it are tips, paddles, the boot and the knuckle plate. No guard has a gap between 0.04 mm and 3 mm to anything that moves; the one static seam near hair (palm lid to tray, Z ≥ 48 mm) is lapped and taped (§8.6).


## 6. Arm bracket and radial float

### 6.1 Arm (yoke) and rail mounting

The arm is a yoke that turns with the horn: cheek A (P19, servo side, Y −98 to −93 mm) and cheek B (P20, idler side, Y +93 to +98 mm), 5 mm PETG plates reaching from the elbow axis forward to X +57 mm, joined by the crossbar (P21: 196 × 16 × 16 mm box beam with 2 mm walls, X +45 to +57 mm, Z 80–96 mm, 4 × M3 × 12 mm into inserts at each cheek). The crossbar carries the **rail mast** in its middle: a 24 mm wide, 5 mm thick plate (X +40 to +45 mm) from Z 64 mm to an arc of R 90 mm about the elbow axis at its top (§2 check c). The arm points the rail radially: plumb at θ = 0°.

**Rail:** MGN9 miniature rail, 100 mm, 9 mm wide, 6.5 mm tall, M3 counterbored holes at 20 mm pitch with 10 mm end distance (holes at 10, 30, 50, 70, 90 mm) [VERIFY on the purchased rail], mounted on the mast's −X face from Z 68 to 168 mm with 5 × M3 × 8 mm socket screws into 5 M3 × 4 mm heat-set inserts. A 1 mm printed reference lip along the mast's −Y edge sets the rail parallel to the mast: push the rail against the lip while tightening from the middle hole outward, 0.6 N·m, with medium threadlocker.

### 6.2 Carriage and riser

Block: **MGN9C** (D7), with the two end seals and their wipers removed (keep the end caps and ball retainers; a block that loses balls is scrap), flushed and re-oiled with one drop of light machine oil. Its face sits at X +30 mm. The printed **riser** (P26) is an L: a 20 × 34 × 3 mm plate on the block (4 × M3 × 6 mm steel screws into the block's tapped holes, 15 × 10 mm pattern for MGN9C [VERIFY]; never longer than 6 mm or the screws touch the rail), and from its foot an arm 32 × 12 × 4 mm running back over the palm to the upper wrist seat at X 0. It also carries the pointer fin and the trim-cord hook.

### 6.3 Up-stop and adjustable down-stop

- **Down-stop** (P23): a block screwed to the mast below the rail end (Z 62–68 mm) with an M3 brass heat-set insert pointing up and an **M3 × 16 mm knurled thumbscrew with a jam nut**. The riser's foot tab rests on the thumbscrew tip. Six millimetres of screw travel move L_max from 82 to 88 mm, i.e. **e = 2–8 mm** with the axis 80 mm above the scalp apex (freeze §1.5); **default e = 4 mm (L_max = 84.0 mm)**. Lock the jam nut after setting.
- **Up-stop** (P24): block screwed to the mast so the carriage's top end meets a 2 mm TPU pad at 28 mm above the default down-stop. Travel between stops is therefore 24 + e mm: 26–32 mm over the e range, 28 mm at the default (freeze 25–30 mm; the e = 7–8 mm settings exceed 30 mm by up to 2 mm, harmless).

### 6.4 Scale and pointer (TP §Q1)

Scale (P25): a 45 × 8 × 2 mm printed strip in a dovetail on the rail shroud's side face, embossed ridges every 1 mm (0.4 mm wide), long ticks every 5 mm, raised numerals 0, 10, 20, 30; or a 40 mm piece of self-adhesive steel millimetre tape on the same strip. The strip slides and locks with an M3 thumbscrew, so zero is re-set with the carriage sitting on the down-stop after every e change. Pointer: a fin on the riser ending in a 0.6 mm edge 1 mm from the scale. What it reads: carriage rise above the down-stop. At mid-stroke with nails on the head the reading is e − W/Σk, not e, because the leaves take part of the engagement (§9.3); e itself is set with the apex gauge (§13, alignment).

### 6.5 Bare floating weight budget (TP §Q2: ≤ 0.9 N = 92 g)

| Item | Mass |
|---|---|
| MGN9C block, seals off | 16.0 g |
| Riser with pointer and trim hook (PETG) | 5.0 g |
| 4 × M3 × 6 mm steel screws (riser to block) | 1.6 g |
| Upper wrist seat with weight post and load-cell slot (PETG) | 4.5 g |
| Seat magnet K&J D61 | 0.9 g |
| Weight cap with M3 × 8 mm nylon thumbscrew | 1.0 g |
| 2 × M3 × 8 mm aluminium screws (riser arm to seat) | 0.4 g |
| Tether cord (60 mm loop) | 0.2 g |
| **Carriage side subtotal** | **29.6 g** |
| Palm lid with lower seat cone and keeper (PETG + 12 × 1.5 mm steel disc) | 7.3 g |
| Palm tray with root blocks and stop beams | 9.0 g |
| Knuckle plate | 4.0 g |
| Silicone boot and its clamp frame | 2.0 g |
| 3 leaves, 0.3 × 12.7 mm, 70 / 67 / 64 mm long | 6.0 g |
| 3 root clamp bars, 6 × M2 × 6 mm steel screws, 6 M2 inserts | 2.2 g |
| 3 nylon M3 stop screws, 3 M3 inserts | 1.1 g |
| 6 × M2 × 6 mm lid screws, 6 M2 inserts | 1.2 g |
| 3 paddles (2 perimeters, 10 % gyroid; outer 5.0 g each, centre with riser 6.5 g) | 16.5 g |
| 3 paddle clamp bars, 6 × M3 × 8 mm **aluminium** screws | 3.3 g |
| 3 TM1 magnets (N52 6 × 2 mm) and 3 TPU seam sleeves | 2.5 g |
| 3 tips type W | 5.4 g |
| **Hand subtotal** | **60.5 g** |
| **Bare floating mass W1** | **90.1 g = 0.884 N** |

The margin is 2 g, inside the print-to-print scatter, so the budget is enforced, not hoped for: weigh every subassembly before final assembly (§13). If the float comes out above 92 g: (1) swap the remaining steel screws for aluminium (−1.5 g); (2) fit the trim cord (§6.7) set to bring W1 to 0.90 ± 0.05 N; (3) last resort, MGN7C on an MGN7 rail (−6 g). If it comes out below 90 g, bring it to 92 g with M3 washers (0.12 g each) under the weight cap so W1 = 0.90 N exactly (TP L1).

### 6.6 Added-weight post and slug sets

Post: Ø 8.0 × 34 mm, part of the upper seat, M3 heat-set insert at the top, capped by the weight cap (Ø 16 mm) and an M3 × 8 mm nylon thumbscrew so slugs are captured (K2.15). Slugs: DIN 9021 M8 large washers, 8.4 × 24 × 2 mm, about 6.2 g each. **+30 g set:** 5 washers, trimmed to 30.0 ± 0.5 g on the kitchen scale with M3 washers taped to the stack, wrapped with yellow tape and labelled "+30 g". **+60 g set:** 10 washers, trimmed to 60.0 ± 0.5 g, red tape, "+60 g". The post takes up to 16 washers (100 g, the freeze maximum). W2 = 1.18 N and W3 = 1.47 N (TP §0: 1.2 / 1.5 N ± 0.05 N) with the 90.1 g float; trim with M3 washers to hit them.

### 6.7 Trim-spring hook (TP §Q2)

A loop of 0.5 mm clear elastic beading cord from the hook on the riser top up to the trim cleat (P27) on the mast near Z 160 mm, where an M3 thumbscrew clamps it. Free loop length 120 mm, stretched about 70 % in use, it lifts about 0.29 N (30 g) with a rate of about 0.003 N/mm, so over ±5 mm of float motion the force changes by ±0.016 N (under the ±0.05 N tolerance of TP L1). Calibrate by sliding the cord through the cleat until the kitchen scale reads 61 ± 2 g (0.60 N, the H1 feel stage) with the carriage floating mid-travel. Remove it for all other settings. Elastic creeps: re-check at the start of any session that uses it.

### 6.8 Float friction and stiction

Rolling friction of a seal-less, oiled MGN9 block: 0.01–0.03 N (RT2 §11); end seals would add 0.1–0.3 N, which is why they come off. The hand hangs 30 mm behind the carriage line, so the block carries a moment of up to 1.5 N × 0.030 m = 0.045 N·m as a moment (no coupling into the normal force, RT2 §11), far below the block's rated moments. Nothing else touches the float in Stage 1: no cable crosses it, the trim cord is off by default, the tether is slack. Stiction appears as a step of ±F_f at every float reversal, about ±3 % of W1 at 0.03 N. Pass level: F_f ≤ 0.1 N (K2.1, TP L3).

### 6.9 Force variation along the stroke from rail inclination

With the rail plumb at θ = 0°, the float carries the dead weight along the arm; at arm angle θ the frozen estimate is N = W cos θ / (1 ∓ µ sin θ) (freeze §1.5). For tip friction µ = 0.7: N/W = 0.92–1.08 at ±7°, 0.84–1.16 at ±13°. Because the float sits on its down-stop beyond about ±7° to ±15° (§9.3), the ends of the contact chord are leaf-controlled anyway, and force tapers to zero there. Inertia of the float following the arc profile adds about 3 % at 2 Hz (up to 2 mm of float motion per stroke), smaller than RT2 §1's 6–14 % because the leaves take part of the profile.


## 7. Wrist: keyed magnetic breakaway seat

### 7.1 Seat geometry

The wrist joins the carriage side (upper seat P28, on the riser arm) to the hand (lower seat moulded into the palm lid P33). Seat plane Z = 69 mm, centred on X 0, Y 0 (the nail force centroid with 0.8 / 1.0 / 1.2 shares is at X +1.1 mm, Y +3.2 mm, close enough that it is ignored).

| Feature | Lower seat (hand side) | Upper seat (carriage side) |
|---|---|---|
| Contact land | flat ring, Ø 40 mm outer, Ø 30 mm inner, top at Z 69 mm | matching flat face, Ø 44 × 5 mm plate (Z 69–74 mm) |
| Centring | 45° cone boss, Ø 18 mm base, Ø 12 mm top, 3.0 mm tall | conical recess Ø 18.4 / 12.4 mm, 3.1 mm deep |
| Magnetic pair | 12 × 1.5 mm mild-steel keeper disc bonded flush in the cone top | **K&J D61** disc (3/8 × 1/16 in, N42, 9.4 N rated pull to thick steel, CL §3) bonded flush in the recess floor, one layer of 0.05 mm tape over it |
| Orientation key | Ø 3 mm peg with a hemispherical end, 2 mm tall, at radius 17 mm on +X | radial slot 3.3 mm wide, 2.2 mm deep |

The shallow cone and the 2 mm round-ended peg both lift out freely when the hand tips about any point of the ring edge, so the seat releases by tipping, never by sliding (sliding would need several times the tipping force).

### 7.2 Breakaway at 2.0 N tangential at the nail tips

Moments about the pivot point on the ring edge (radius s) for a tangential force F_t at the nail edges, a height h below the seat plane: F_t × h = s × (F_m + W_upper), where F_m is the magnetic pull and W_upper the carriage-side weight resting on the seat (the scalp carries the hand's own weight). With s = 20 mm, h = 70 mm (69 mm to the centre edge, 72.6 mm to the outer edges), F_m = 6.5 N [design; D61 on a 1.5 mm keeper through 0.05 mm of tape, estimated 5.5–7.5 N, measured in L6]:

| Float setting | W_upper | F_t at breakaway |
|---|---|---|
| W1 (no slug) | 0.29 N | 1.94 N |
| W2 (+30 g) | 0.59 N | 2.03 N |
| W3 (+60 g) | 0.88 N | 2.11 N |
| hand lifted, hanging (seat in tension by the hand's 0.59 N) | | 1.69 N |

The ring is circular, so the value is the same in +X, −X, +Y, −Y and diagonally. Each nail therefore never carries more than 2 N tangential before the whole hand lets go (red line 3, freeze §1.6). **Straight-down pull:** the hand drops off when pull + hand weight > F_m, i.e. at 5.9 N (L6a asks ≥ 5 N). Tuning after L6: each added 0.05 mm tape layer lowers F_m by roughly 10 % [EST]; a second D61 stacked on the first raises it by roughly 40 % [EST].

**Measurement point conflict (flag, §15):** TP L6(a) hooks the fish scale to the knuckle plate, 31.5 mm below the seat, where the same seat lets go at 2.2 times the tip value (4.3–4.7 N), outside L6(a)'s 1.5–2.5 N band. I designed to the freeze wording ("2.0 N tangential", red line 3, at the tips) and supply a printed pull clip (P46, a loop that slips over the centre paddle's seam sleeve) so L6(a) can pull at nail height. The integrator should amend L6(a) or accept 4.3–4.7 N at the knuckle plate as equivalent.

### 7.3 Tether

A 60 mm loop of 1.0 mm braided Dyneema between an eyelet in the upper seat and an eyelet in the palm lid (freeze §1.6). Seated, the loop is folded into a Ø 12 × 6 mm cup in the lid at Y +25 mm, so there is no dangling cord in reach of hair (RT2 H8). Released, the hand hangs at most 60 mm below the carriage (K2.9), its edges about 55 mm lower than in use, so a released hand rests on the head at its own weight (0.59 N total, 0.2 N per nail) and cannot reach the face from any stroke angle. Two consequences flagged in §15: H-6.4 and H-4.13 prefer untethered breakaways (the freeze overrules them for good reason: there is nowhere for a hand above the crown to fall except onto the face); and with a 60 mm tether the 33 mm fail-safe lift does not lift a released hand off the head. A 25 mm tether would; I recommend the integrator shorten it to 25 mm (one knot change).

### 7.4 Reserved 40 × 12 mm load-cell slot (freeze §1.9)

The riser arm meets the upper seat through a 41 × 13 × 8 mm pocket bridged in Stage 1 by a printed 40 × 12 × 6 mm filler bar and 2 × M3 × 10 mm screws. In Stage 3 a 40 × 12 mm bar load cell (5 kg, RT2 §3: a 1 kg cell is destroyed by a 20 N push) replaces the filler, bolted riser-to-seat at its own hole pitch [VERIFY at Stage 3], so the cell carries everything the hand feels. Its cable will then cross the float (re-run TP L3).


## 8. Hand: nails, feeler leaves, palm, knuckle plate

### 8.1 Layout

| Nail | Edge position (X, Y) at mid-stroke | Free edge Z (down-stop) | Leaf rate | Share of W | Leaf runs from paddle toward | Leaf level (floor Z) |
|---|---|---|---|---|---|---|
| L (left) | (−8, −24) mm | −3.6 mm | 0.12 N/mm | 0.8 × W/3 | −Y (root outboard) | 0 (40.4 mm) |
| C (centre) | (0, 0) | 0 | 0.15 N/mm | 1.0 × W/3 | −Y, crossing over L | 1 (53.0 mm) |
| R (right) | (+8, +24) mm | −3.6 mm | 0.18 N/mm | 1.2 × W/3 | +Y (root outboard) | 0 (40.4 mm) |

Pitch 24 mm in Y (D2), stagger ±8 mm in X read as a diagonal step (freeze §1.7 leaves the sense open; each stroke direction then has one leading and one trailing outer nail, symmetric for bidirectional raking, and the 8 mm offset is an 80 ms landing spread at 100 mm/s). The outer edges sit 3.6 mm lower than the centre because the R 90 mm sphere drops 90 − √(90² − 8² − 24²) = 3.63 mm at that radius, so all three leaves deflect equally on a nominal head (TI §6 asks for this pre-curve). Paddles hang vertical (all parallel), so the knuckle plate is the scalp sphere shape (R 90 mm) translated up 37.5 mm.

### 8.2 Why two leaf levels

With leaves along Y (freeze §1.7) and pitch in Y, the three leaves are collinear: a leaf can only pass a neighbouring paddle by going over it, because the paddle body runs continuously from its root down through the knuckle plate. The 28 mm long (X) root blocks and the 8 mm stagger leave no side-by-side lane (a lane needs 23 mm of X offset). So L and R root outboard on their own sides, and C roots on the −Y side one level up, crossing over L. The level step is only 9 mm because L already sits 3.6 mm low: L's screw heads at Z 45.3 mm rise to 50.3 mm at L's 5 mm stop (+0.5 mm for roll at the root corner), and C's leaf underside is at 53.0 mm, sagging 0.4 mm when the hand hangs, leaving 1.8 mm inside the closed palm. C's paddle is therefore the tip lead's paddle with a 9 mm constant-section riser between its drafted body (z = 25 mm) and its transition (D3).

Every leaf also **rolls its paddle about X** as it bends: end slope θ = δ (a²/2 + ab)/(a³/3 + a²b + ab²), 1.63, 1.76, 1.87° per mm of tip travel for L, C, R, which swings the edge sideways by 44 mm (outer) or 53 mm (centre) × sin θ. The two outer nails roll toward the centre and C rolls toward R, so the C–R pair converges. Two measures keep every gap open: **roll pre-tilt** (each root seat is printed tilted about X by β = δ_nom × θ/δ: L 4.4°, C 4.7°, R 5.0°, so each paddle hangs vertical at the nominal 2.67 mm deflection and is rolled the other way when unloaded), and the 24 mm pitch with a 5 mm stop. Resulting gaps are in §8.7.

### 8.3 Leaf lengths, with the clamp correction (d)

Pure cantilever: k = 3EI/L³ with E = 200 GPa, I = w t³/12 = 12.7 × 0.3³/12 = 0.0286 mm⁴, EI = 5715 N·mm². The tip lead showed (TIPS §7.2) that this overstates the stiffness, because the leaf also bends inside each clamp's wall slot (3 mm at each end) and the load acts b = 4 mm beyond the paddle bar edge through the rigid clamp. **Correction applied:** k = EI / (a³/3 + a²b + ab²), with a = flexible length from root bar edge to paddle bar edge = face-to-face free length + 6 mm, b = 4 mm. My root blocks copy the paddle's slot geometry (bar edge 3 mm in from the block face) so the same formula holds at both ends.

| Leaf | Target k | a (bar edge to bar edge) | Free length face to face | Naive 3EI/L³ at that length | Overstatement | Cut length |
|---|---|---|---|---|---|---|
| L | 0.12 N/mm | 48.3 mm | 42.3 mm | 0.227 N/mm | 1.90 × | 70 mm |
| C | 0.15 N/mm | 44.5 mm | 38.5 mm | 0.301 N/mm | 2.00 × | 67 mm |
| R | 0.18 N/mm | 41.7 mm | 35.7 mm | 0.374 N/mm | 2.08 × | 64 mm |

(The tip lead's 1.75 × is the same formula at 48 mm face to face; the factor grows as leaves get shorter.) Shares come from rate, not shims: with equal free heights on the sphere all three leaves take the same deflection δ = W/Σk, Σk = 0.45 N/mm, so the 0.8 : 1.0 : 1.2 ratio holds at every weight, which shims would not give.

| Setting | δ | L | C | R | Heaviest / lightest |
|---|---|---|---|---|---|
| 0.6 N (trim cord) | 1.33 mm | 0.16 N | 0.20 N | 0.24 N | 1.5 |
| W1 0.88 N | 1.96 mm | 0.24 N | 0.29 N | 0.35 N | 1.5 |
| W2 1.18 N | 2.62 mm | 0.31 N | 0.39 N | 0.47 N | 1.5 |
| W3 1.47 N | 3.27 mm | 0.39 N | 0.49 N | 0.59 N | 1.5 |

All inside 0.1–0.25 N/mm (freeze §1.7), inside K2.5 (1.2–1.6, no nail above 0.6 N at W2). Sensitivity: feeler-stock thickness ±0.005 mm gives ±5 % in k; trimming 1 mm of free length changes k by 6–7 %; a 1 mm head-shape mismatch between nails shifts 0.12–0.18 N between them, which is the intended 20–40 % force spread (TI §6), not a fault. Leaf stress σ = F(a + b)(t/2)/I: 88–115 MPa at nominal, 165–216 MPa at the 5 mm stop, against hardened feeler stock yielding at 1.2–1.5 GPa and an edge-limited endurance of about 500 MPa (RT2 §4) once corners are rounded R 1 mm and edges stoned: infinite life.

### 8.4 Travel to the hard stop (≤ 2.4 N per nail)

Stop at **5.0 mm** of tip travel (D5). Force on the leaf at the stop: L 0.60 N, C 0.75 N, R 0.90 N, all far under the 2.4 N per-nail figure (freeze §1.7, TP K2.6). The stop is an M3 × 10 mm nylon screw, head down, threaded into an M3 insert in a stop beam of the palm tray, bearing on the leaf 3 mm outboard of the paddle's root-side wall (L at Y −34, X −11 mm, offset 3 mm from L's centreline to stay clear of C's leaf lane; C at Y −10, X 0; R at Y +34, X +8 mm). Turn the screw until TP L2 reads the stop at 5.0 ± 0.3 mm of tip travel, then lock with a drop of medium threadlocker. Beyond the stop the remaining 10 mm of leaf behaves as an 18 N/mm spring, effectively rigid.

**Proof load, conflict (c):** safety §3.6 proof-loads tips at 3 × rated force, about 7.5 N normal; TP L6(b) proof-loads at 3 × 0.8 N = 2.4 N "on the leaf hard stop". **The stop is designed to the 7.5 N value**: the stop beam, nylon screw, root clamp and paddle clamp must take 7.5 N per nail at the tip with the leaf on its stop without slip, crack or permanent set (leaf stress 394 MPa in the 10 mm segment beyond the stop, static, safe). The stop position (force at which the leaf reaches it) is the separate ≤ 2.4 N requirement, met at 0.6–0.9 N. I run the bench proof at 7.5 N (§14) and flag the inconsistency for the integrator; L6(b)'s 2.4 N is too low to prove anything about tips the safety document rates at 2.5 N.

### 8.5 Torsion check at 0.3 N drag

Drag acts in X at the edge, 44 mm (outer) or 53 mm (centre) below the leaf, and twists the leaf about Y. Torsional rate GJ/a with G = 77 GPa, J = w t³/3 = 0.114 mm⁴: 182, 198, 211 N·mm/rad for L, C, R. At 0.3 N drag: outer nails twist 3.6–4.2° (2.8–3.2 mm of edge motion in X), the centre 4.6° (4.3 mm). This corrects the freeze's "~2°" (D13). It is symmetric in ±X, it gives about 0.1 N/mm of tangential compliance (useful toward H-4.11), all three twist the same way under a common drag so X spacing is unchanged, and at the knuckle plate the paddles move only 0.5 mm (outer) and 1.3 mm (centre), allowed for in the slot clearance. At the stall drag the elbow allows (about 1.2 N total, 0.4 N per nail) twist reaches 5–6°, still inside the slot.

### 8.6 Palm (enclosed clamshell) and leaf clamping

- **Palm tray (P32):** overall 52 (X) × 169 (Y) × 28 (Z) mm, Y −88 to +81 mm, Z 38–66 mm, walls 0.8 mm (2 perimeters) stiffened by 1.2 mm ribs every 20 mm. Centre box 52 × 72 mm around the paddles; −Y arm 30 mm wide carrying L's leaf (level 0), C's leaf (level 1) and L's and C's stop beams; +Y arm 20 mm wide carrying R's leaf. Three printed root blocks with the β pre-tilt seat, a 12.9 × 1.0 mm leaf slot 3 mm long, a 24.2 × 8.4 mm clamp window, and 2 M2 heat-set inserts at ±8.6 mm. Root floors: L 44.1 mm, C 56.7 mm, R 44.0 mm (the pre-tilt drops each leaf 3.7 mm toward its paddle).
- **Root clamp bars (P34, ×3):** 24 × 8 × 3 mm, 12.9 × 0.25 mm groove (shallower than the leaf, so the bar presses the leaf, as in the paddle SCAD), 2 × Ø 2.4 mm holes at ±8.6 mm, M2 × 6 mm screws, 0.15 N·m. No hole in the leaf.
- **Palm lid (P33):** 52 × 169 × 1.6 mm top with a 2 mm lap skirt over the tray walls, 6 × M2 × 6 mm screws into tray inserts; carries the lower wrist seat (§7.1), the tether cup and eyelet, and a 2 mm relief above C's paddle. The lid-to-tray seam (Z 48–66 mm, at least 44 mm above the scalp) gets a band of 0.05 mm PTFE tape so no 0.04–3 mm seam is exposed (H-4.9, K1.8).
- **Leaf preparation:** cut 0.30 × 12.7 mm (0.012 × 1/2 in) feeler stock to 70 / 67 / 64 mm with aviation snips, round all four corners R 1 mm, stone both long edges and the ends (RT2 H4), wipe off oil. Mark the root bar edge position with a fine marker from the table in §8.3.
- **Paddle clamp, matching paddle SCAD:** leaf through both Y wall slots (`LEAF_THROUGH = true`), on the window floor 31.5 mm above the pocket mouth, clamp bar 24 × 8 × 3.2 mm with the 0.25 mm groove, 2 × M3 × 8 mm aluminium screws at x = ±9.5 mm into the 2.6 mm thread-forming holes, 0.3 N·m. Trim the leaf flush with the far wall and round the cut end.

### 8.7 Knuckle plate, paddle exits and resolution of (b)

**Knuckle plate (P30):** 64 × 90 mm spherical cap, 1.6 mm thick, underside R 90 mm passing 37.5 mm above the centre edge (33.9 mm above the outer edges), all edges R 3 mm, faces drafted 15° at the perimeter, Ra ≤ 0.8 µm (sanded 400 then buffed, H-4.8). It bolts under the palm tray with 6 × M2 × 8 mm into tray inserts, clamping the boot and the boot frame (P31) between them.

**Exits, resolution of (b): one shared slot plus one bonded slack boot.** Paddle section where it crosses the plate (z = 25 mm on each paddle, free state): 22.8 (X) × 17.8 (Y) mm with 10° draft on all faces. Clearance from the slot edge: **4.5 mm** around L and R, **6.0 mm** around C (it moves most at the plate: 1.3 mm roll plus 1.35 mm twist). The slot is the union of three R 4 mm-cornered rectangles, 31.8 × 26.8 mm at (−8, −24) and (+8, +24) and 34.8 × 29.8 mm at (0, 0); overall 47.8 × 74.8 mm. Individual holes are impossible: at 24 mm pitch, 17.8 mm sections plus 2 × 4.5 mm clearance need 26.8 mm. When a paddle is loaded it rises and the section in the plate comes from lower on the drafted body, so every clearance grows; the minimum is at rest.

**Boot:** one piece of 0.25 mm Shore 40A silicone sheet, cut with the template P35: an 8 mm flange outside the slot outline, and three holes at 70 % of the paddle section (stretched 40 % over the paddle at z = 26–28 mm, bonded with a 2 mm bead of silicone adhesive such as Smooth-On Sil-Poxy). The sheet between each paddle and the slot edge, and between paddles, is cut 40 % longer than the span, so it lies in a loose upward fold inside the palm and never pulls on a paddle (coupling under 0.002 N/mm [EST]; a slit sheet that slides would add about 0.03 N of friction per nail). Hair below the plate meets only the plate, 1.6 mm-deep clearances of ≥ 3 mm, and the soft underside of the boot.

| Gap (adjacent nails unless stated) | Static, free state | Worst case, any leaf state 0–5 mm with pre-tilt | Rule |
|---|---|---|---|
| Tip edges, W (8 mm wide) | 16.0 mm | 8.4 mm | ≥ 8 mm H-4.6, ≥ 3 mm freeze §1.4 |
| Tip edges, B45-12 (12 mm wide) | 12.0 mm | 4.4 mm (6.2 mm in normal use) | ≥ 3 mm |
| Seam sleeves (10.3 mm wide band) | 13.7 mm | 7.1 mm | ≥ 3 mm |
| Paddles at the knuckle plate (17.8 mm sections) | 6.2 mm | 4.2 mm | ≥ 3 mm |
| Paddle to slot edge, outer / centre | 4.5 / 6.0 mm | 3.4 / 3.4 mm | ≥ 3 mm |
| Paddle root blocks (inside the palm) | 10.0 mm | 8.6 mm | enclosed |
| C leaf over L paddle (inside the palm) | 3.2 mm | 1.8 mm | enclosed, above the boot |

"Normal use" means all three leaves within ±2 mm of nominal deflection; the worst case is every combination of 0–5 mm on each leaf, which is more than the dead weight can produce while the float is free. No gap anywhere within 25 mm of the scalp falls into the 0.04–3 mm band.

**Protrusion:** pocket mouth 25.0 mm below the plate at rest (freeze §1.7), 22.4 mm at nominal load; nail edges 37.5 mm below the plate at rest and 34.9 mm at nominal, above RT2's 32 mm for 8 cm hair and H-4.5's 25 mm.

### 8.8 Hair checklist (H-6.8), self-score for this hand

Items 1–4, 6, 8–10, 12, 14 and 18 score 2. Items 5 (independent leaves change tip spacing, never below 4.4 mm), 7 (no 0.15 N yield; leaf torsion gives about 0.1 N/mm and the wrist lets go at 2 N), 11 (tether), 13 (grain map is procedural), 15 (no snag sensor in Stage 1; the reflex is the hold-to-run release and the lift), 16 (insulating tips) and 17 (hand and tips come off tool-free; the boot needs M2 screws) score 1. **Total 29/36, no gating zero**, above the 28 floor (H-6.8). The build reviewer should re-score on the built hand.

### 8.9 Requests to the tip lead (paddle SCAD), flagged not made

`DRAFT_Y = 10` for all three paddles; a new `RISER` parameter (constant 22.8 × 17.8 mm section from z = 25 mm to 25 + RISER, then the 3 mm transition and the root) with `RISER = 9` for the centre paddle and 0 for the outer two; print at 2 perimeters, 10 % gyroid, 4 perimeters locally around the two screw holes (slicer modifier) to meet the mass budget. With `DRAFT_Y = 10` the drafted top (17.8 mm in Y) is wider than the 14 mm root block, so the 3 mm transition narrows above the plate; it is inside the boot and harmless, but `ROOT_Y = 18` removes it at +0.6 g per paddle if the tip lead prefers. Everything else in paddle_with_pocket.scad and tm1_tang_lib.scad is matched unchanged.


## 9. Geometry checks

### 9.1 Lift-off table (H = 80 mm, R = 90 mm)

The freeze formula d(θ) = (H + R) cos θ − √(R² − (H + R)² sin² θ) gives the distance from the axis to the sphere along the arm; d − H is the gap for a tip at L = 80 mm (freeze §1.5). The real free tip sits at L_max = 84 mm, so its clearance along the ray is d − 84 mm. The third column is what a ruler next to the tip reads (vertical clearance of the free centre tip, e = 4 mm), and the last two are the outer nails, which lead or trail by ±8 mm in X.

| θ | d − H (freeze) | d − 84 mm (free centre tip, along the arm) | Vertical clearance, centre | Left nail (−8, −24) | Right nail (+8, +24) |
|---|---|---|---|---|---|
| 0° | 0.0 mm | −4.0 mm (4 mm engagement) | −4.0 mm | −4.0 mm | −4.0 mm |
| ±10° | 2.4 mm | −1.6 mm | | | |
| ±13° | 4.2 mm | +0.2 mm | +0.2 mm | +4.2 / −3.1 mm | −3.1 / +4.2 mm |
| ±18° | 8.6 mm | 4.6 mm | 3.9 mm | +9.6 / −0.3 mm | −0.3 / +9.6 mm |
| ±22° | 14.0 mm | 10.0 mm | 7.8 mm | +14.9 / 2.8 mm | 2.8 / +14.9 mm |
| ±25° | 19.9 mm | 15.9 mm | 11.2 mm | +19.4 / 5.7 mm | 5.7 / +19.4 mm |
| ±28° | 28.5 mm | 24.5 mm | 14.9 mm | +24.3 / 9.1 mm | 9.1 / +24.3 mm |

(Outer-nail pairs read "at −θ / at +θ".) All three nails are clear of the sphere by ±22°; the trailing outer nail is the last to leave, 5.7 mm clear at ±25° (TP L4 asks ≥ 5 mm) and 9.1 mm at ±28° (TP K2.13 and L4 ask ≥ 10 mm). **Flag:** the frozen ±8 mm stagger costs the trailing nail 2.5 mm against the 10 mm check; either TP accepts ≥ 9 mm at ±28° for the outer nails, or the firmware's nominal maximum stays at ±25° for HUMAN mode and the ±28° figure applies to the centre nail. Reversals always happen beyond ±18°, where every nail is clear (H-5.2).

### 9.2 Contact chord at e = 4 mm

Contact lasts while the sphere is above the free tip: half-angle 12.75°, contact chord **37.4 mm** of arc for each nail (freeze: ≈ 36 mm), with the outer nails' windows shifted ±5.2° (≈ ±8 mm) either side of the centre's, so the hand lands and leaves one nail at a time. Chord by engagement: e = 2 mm 26.2 mm, e = 4 mm 37.4 mm, e = 6 mm 46.1 mm, e = 8 mm 53.6 mm (TP §0 expects 25 / 36 / 44 mm at E2 / E4 / E6: within its ±5 mm).

### 9.3 Where the dead weight is actually in charge

The leaves are in series with the float, so near the chord ends the carriage sits on its down-stop and force is set by leaf compression, falling smoothly to zero; the float lifts off its stop (force = W) only where the sphere is more than δ = W/Σk above the free tip. Chord over which the force equals W:

| e | W 0.6 N | W1 0.88 N | W2 1.18 N | W3 1.47 N |
|---|---|---|---|---|
| 2 mm | 15 mm | 0 (never floats) | 0 | 0 |
| 4 mm | 31 mm | 27 mm | 22 mm | 16 mm |
| 6 mm | 41 mm | 38 mm | 35 mm | 32 mm |
| 8 mm | 50 mm | 47 mm | 45 mm | 42 mm |

The pointer at mid-stroke reads e − δ: at the default E4 / W2 it reads 1.4 mm, not 4 mm. **Flag to the test lead:** E2 with W1 or more never floats, so at E2 the force is a leaf constant (≤ 0.9 N, still capped) rather than the dead weight; E4 gives a dead-weight plateau of 16–27 mm inside a 37 mm contact with smooth ramps (arguably more fingertip-like); E6 makes the plateau the whole middle. I recommend TP's E column be defined as geometric engagement set with the apex gauge (§13, alignment) and that E6 be considered as the default if L4 shows a short plateau.

### 9.4 Nails lifted by ±25°, limits ±28°

Fully lifted by ±25° (minimum 5.7 mm on the trailing outer nail, 11.2 mm centre), firmware absolute limit ±28° (EF §4.2), mechanical stops ±32° (§5.3). At ±32° the centre tip is 19 mm clear and nothing on the arm meets the frame (§2 checks). Firmware start and stop at the +25° park therefore always begin with every nail off the scalp.


## 10. Face cradle and posture

### 10.1 Posture options (TP §M0)

| | SEAT (primary, crown) | PRONE (occiput default, fallback for neck discomfort) |
|---|---|---|
| Support | Tabletop massage face cradle (horseshoe pad about 280 × 220 mm, adjustable tilt) on its own stand | Portable face-cradle cushion (horseshoe foam, about 300 × 250 × 100 mm) on the bed |
| Head attitude | flexed 30–45° for the crown so the scalp normal at the target is vertical | face down; gravity along the occipital normal (the posture the dead weight is designed for) |
| Arm mount | desk clamp, arm reaching over from behind or the side | nightstand clamp (top ≥ 18 mm solid) or a floor-stand monitor pole within 500 mm of the occiput |
| Head motion the float must absorb | ±5–10 mm | 5–15 mm breathing drift (TP §M0), inside the 24 mm free up-travel |
| Forehead pressure | 15 N over about 60 cm² of pad ≈ 2.5 kPa, below safety §2.2's 5 kPa sustained limit | similar |

### 10.2 Isolation (TP §Q7)

The stroke reaction (up to 0.16 N·m at the elbow) reaches the desk through the arm clamp. If the cradle stands on the same desk, the forehead feels the stroke rhythm, a confound for the realism ratings (RT2 §7). Preferred: the face cradle stands on a **separate small table or stool** that does not touch the desk. If it must share the desk: mount it on an 18 mm plywood baseboard 350 × 300 mm standing on **four Ø 30 × 15 mm rubber or Sorbothane isolation feet** in printed foot cups (P41, Ø 40 × 12 mm, screwed to the board with 2 × M3 × 12 mm wood screws each), with a 10 mm air gap between the board and any part of the arm's clamp. Note "rhythm felt in forehead: y/n" on every form (TP §M0).

### 10.3 Dimensions and setup aids

- Tilt wedges (P42, a pair): 15° wedges 120 × 60 mm that go under the cradle's front feet, giving 0° or 15° extra tilt for the crown or occiput without re-adjusting the cradle's own hinge.
- Apex height gauge (P43): a 12 mm square stick 120 mm long with a rounded foot and engraved rings at 80, 82, 84, 86 and 88 mm from the foot. With the module latched, arm at 0°, nails at their free state, stand it on the target point: raise or lower the arm until the 80 mm ring is level with the elbow-axis mark scribed on cheek A: that sets H = 80 mm, so e = L_max − 80 mm (4 mm at the default L_max = 84 mm); the other rings let H be checked when the setting changes. Used in §13, alignment and before every session.
- Clearances to the face: on the crown the hand is about 100 mm behind the hairline. For CROSS aims (Y along the head's front-back line), turn the module so the **idler side (+Y) faces forward**: the fixed guard cap G3 then sits between the moving cheek B and the eyes (red line 6), and the servo is over the occiput. Nothing moving is within 25 mm of the ear canals (the hand ends at |Y| ≤ 88 mm at Z ≥ 38 mm above the crown plane; ear canals are about 120 mm below it).


## 11. Printed parts list

All parts PETG unless stated (CL §5.2, safety §8: IPA-wipeable, no PLA near skin), 0.4 mm nozzle, 0.2 mm layers unless stated. "W/I" = perimeters / infill. Inserts are brass heat-set (M3: 4.0 mm hole, 4 mm long; M2: 3.2 mm hole, 3 mm long) unless stated. Hole sizes are as printed; drill or ream where noted. Dimensions X × Y × Z in the installed orientation.

| # | Part | Qty | Mat. | X × Y × Z (mm) | Key features (mm) | Print orientation | W/I | Inserts | Post-processing | Mates with |
|---|---|---|---|---|---|---|---|---|---|---|
| P1 | VESA adapter | 1 | PETG | 66 × 140 × 145 | 6 mm base plate; VESA 75 holes Ø 4.5 counterbored Ø 8 × 3; 2 hinge ears 10 thick × 28 tall, reaching 60 to the Ø 6.3 pin bore at (X −60, Z 84); magnet arm with Ø 3.4 hole for the magnet's rear M3 screw and a Ø 20.4 × 2 locating counterbore; up-stop boss (M4 insert); 2 pulley bosses at Y ±60 with Ø 3.2 axle holes; 2 spring-anchor hooks at Z 30; tray seat with 4 M3 inserts; ribs 4 mm | base plate flat on the bed | 5 / 40 % | 4 × M3 (tray), 1 × M4 × 6 (up-stop) | ream pin bore Ø 6.3 | arm VESA plate + ballast stack, P5, P2, P3, magnet |
| P2 | Pulley sheave | 2 | PETG | Ø 16 × 5 | V-groove for 1 mm cord, bore Ø 10 for 623ZZ (3 × 10 × 4) press fit | flat | 4 / 100 % | none | press bearing | P1, cords |
| P3 | Electronics tray | 1 | PETG | 32 × 36 × 92 | pocket for OpenRB-150 (approx 66 × 25 [VERIFY]) on 4 Ø 2.5 bosses, pocket for Wago 221-413 and the 30 × 20 rail perfboard (divider, TVS, 470 µF), USB-C opening 12 × 7, cable slots 8 × 4 top and bottom | open side up | 3 / 20 % | 2 × M3 (lid) | none | P1, P4 |
| P4 | Electronics tray lid | 1 | PETG | 2 × 36 × 92 | vent slots 2 × 20, 2 × Ø 3.4, label recess | flat | 3 / 20 % | none | none | P3 |
| P5 | Frame hinge knuckle | 1 | PETG | 24 × 48 × 30 | Ø 6.3 pin bore along Y at 8 above its base; 2020 socket 20.2 × 20.2 × 12 with 2 × M5 holes; PTFE-washer faces | bore axis horizontal, socket up | 6 / 50 % | none | ream Ø 6.3 | P1 ears, 2020 post |
| P6 | Keeper lever | 1 | PETG | 12 × 30 × 60 | clamps the post foot (2 × M5 T-nut); foot pad 30 × 30 with 25 × 25 × 3 recess for the steel keeper (epoxy + 2 × M3 × 6 countersunk); keeper face at r = 50 below the pin; reset-cord eyelet Ø 2.5 | lying on its side | 6 / 60 % | none | flatten keeper face to the magnet with 400-grit on glass | P5, magnet |
| P7 | Cord bar | 1 | PETG | 12 × 140 × 12 | clamps the post at Z 148 (2 × M5 T-nut); cord eyelets Ø 2.5 at Y ±60 with bowline posts | flat | 5 / 50 % | none | round eyelet edges | post, cords |
| P8 | Frame yaw plate | 1 | PETG | 70 × 70 × 6 | 8 M3 inserts on Ø 56.6 at 45° spacing; 2 × M5 slots to the spine | flat | 5 / 50 % | 8 × M3 | none | spine, P9 |
| P9 | Carrier yaw plate | 1 | PETG | 70 × 70 × 6 | 4 × Ø 3.4 on a 40 × 40 square; 2 × M5 slots to the carrier beam | flat | 5 / 50 % | none | none | P8, carrier beam |
| P10 | Reset tab and spine end cap | 1 | PETG | 25 × 30 × 25 | caps the spine end, finger tab 25 × 20 with R 5 edges | tab flat | 4 / 30 % | none | none | spine |
| P11 | Drop leg, servo side (−Y) | 1 | PETG | 50 × 20 × 105 | 2020 end socket with M5 end-tap screw and 2 T-nut slots; leg 20 × 12 section ribbed; foot flange with 4 × M3 inserts for P13 | on its side | 5 / 40 % | 4 × M3 | none | carrier beam, P13 |
| P12 | Drop leg, idler side (+Y) | 1 | PETG | 50 × 20 × 105 | mirror of P11; foot with 2 M3 inserts and 2 slots for P15 | on its side | 5 / 40 % | 2 × M3 | none | carrier beam, P15 |
| P13 | Servo cradle | 1 | PETG | 30 × 30 × 44 | pocket 20.4 × 34.4 × 23.5 open at the horn face (+Y) and cable end; 2 × Ø 2.2 for M2 into the servo [VERIFY]; TPU-bumper lugs at ±32°; zero-pin bore Ø 3.1 | horn face up | 4 / 40 % | 2 × M3 (strap) | none | servo, P11, P14, P17 |
| P14 | Servo strap | 1 | PETG | 30 × 4 × 10 | 2 × Ø 3.4, 0.3 interference on the servo back | flat | 4 / 100 % | none | none | P13 |
| P15 | Idler housing | 1 | PETG | 30 × 14 × 40 | bore Ø 16.0 × 5 for the 625-2RS (press, 0.05 interference after test print), shoulder relief Ø 8; 2 × M3 slots ±1.5 in X and Z | bore axis vertical | 6 / 60 % | none | test-fit bearing | P12, bearing |
| P16 | Horn adapter disc | 1 | PETG | Ø 24 × 3 | 4 holes for the XL330 horn's M2 pattern [VERIFY], centre relief Ø 6 for the horn screw, 4 × Ø 3.4 on Ø 18 to cheek A | flat | 4 / 100 % | none | none | XL330 horn, P19 |
| P17 | Guard cap G2 (servo) | 1 | PETG | 60 × 40 × 30 | 2 mm shell under P13 and around the horn, 15° drafted sides, R 3 edges, cheek A passes ≥ 10 clear through ±32° | open side up | 3 / 20 % | none | sand edges | P13 |
| P18 | Guard cap G3 (idler) | 1 | PETG | 60 × 40 × 30 | mirror of P17 around P15 | open side up | 3 / 20 % | none | sand edges | P15 |
| P19 | Yoke cheek A (servo side) | 1 | PETG | 75 × 5 × 40 | 4 M3 inserts on Ø 18 for P16; zero-pin bore Ø 3.1 at θ = 0 against P13; stop lug; 2 × M3 inserts for P21 | flat (5 mm thick, XZ plane on the bed) | 6 / 60 % | 6 × M3 | none | P16, P21 |
| P20 | Yoke cheek B (idler side) | 1 | PETG | 75 × 5 × 40 | Ø 5.0 reamed bore + M4 nut trap for the shoulder screw at the axis; 2 × M3 inserts for P21 | flat | 6 / 60 % | 2 × M3 | ream Ø 5.0 | shoulder screw, P21 |
| P21 | Yoke crossbar with rail mast | 1 | PETG | 17 × 196 × 108 | box beam 196 × 16 × 16, 2 mm walls; mast 24 × 5 from Z 64 to an R 90 arc about the axis; 5 M3 inserts at 20 pitch for the rail; 1 mm rail reference lip on the −Y edge; holes for P22–P24, P27 | mast face down, beam along the bed X | 5 / 40 % | 5 × M3 (rail) + 8 × M3 (stops, shroud, cleat) | check mast face flat to 0.1 with a straightedge, sand if needed | P19, P20, rail, P22–P24, P27 |
| P22 | Rail shroud G4 | 1 | PETG | 16 × 34 × 50 | U-channel, 2 walls, closed bottom, 25 wide slot for the riser, dovetail for P25 | open side up | 3 / 20 % | none | sand edges R 3 | P21, P25 |
| P23 | Rail down-stop block | 1 | PETG | 12 × 20 × 8 | 1 × M3 brass insert vertical for the thumbscrew; 2 × Ø 3.4 to the mast | flat | 6 / 100 % | 1 × M3 | none | P21, thumbscrew |
| P24 | Rail up-stop block | 1 | PETG | 12 × 20 × 8 | 2 mm TPU pad recess; 2 × Ø 3.4 to the mast | flat | 6 / 100 % | none | glue TPU pad | P21 |
| P25 | Float scale strip | 1 | PETG | 2 × 8 × 45 | dovetail, 1 mm ridges 0.4 wide, 5 mm long ticks, numerals 0/10/20/30, M3 lock screw slot | flat, face up, 0.12 mm layers | 3 / 100 % | none | ink the ticks | P22 |
| P26 | Carriage riser (L-bracket) with pointer and trim hook | 1 | PETG | 32 × 20 × 34 | plate 20 × 34 × 3 with 4 × Ø 3.4 on 15 × 10 [VERIFY]; arm 32 × 12 × 4 to P28 (2 × Ø 3.4); foot tab for the down-stop; pointer fin 0.6 edge; trim hook | on its side | 4 / 30 % | none | none | MGN9C block, P28 |
| P27 | Trim cleat | 1 | PETG | 10 × 16 × 12 | cord channel 1 mm, M3 clamp thumbscrew into an insert | flat | 4 / 50 % | 1 × M3 | none | P21, trim cord |
| P28 | Upper wrist seat with weight post | 1 | PETG | Ø 44 × 39 | plate Ø 44 × 5; conical recess Ø 18.4/12.4 × 3.1; D61 pocket Ø 9.6 × 1.6 at the floor; key slot 3.3 × 2.2; post Ø 8.0 × 34 with M3 insert at the top; load-cell pocket 41 × 13 × 8 with filler P47; tether eyelet Ø 2 | seat face down, post up | 3 / 15 % | 1 × M3 | sand seat face flat on glass | P26, P33, P29 |
| P29 | Weight cap | 1 | PETG | Ø 16 × 4 | Ø 3.4 hole, finger knurl | flat | 3 / 50 % | none | none | P28 |
| P30 | Knuckle plate | 1 | PETG | 64 × 90 × 8 (spherical cap, 1.6 thick) | underside R 90; shared slot 47.8 × 74.8 (union of 31.8 × 26.8 at (∓8, ∓24) and 34.8 × 29.8 at (0, 0), R 4 corners); slot edge R 1.5 with 15° lead-in; perimeter R 3; 6 × Ø 2.4 | convex side up (smooth underside on supports is not acceptable: print the underside as the top surface, 0.12 mm layers, ironing on) | 3 / 30 % | none | 400 grit then buff, Ra ≤ 0.8 µm; IPA wipe | P31, boot, P32 |
| P31 | Boot clamp frame | 1 | PETG | 60 × 86 × 1.2 | ring following the slot + 8 flange, 6 × Ø 2.4 | flat | 3 / 100 % | none | none | P30, boot |
| P32 | Palm tray | 1 | PETG | 52 × 169 × 28 | walls 0.8 with 1.2 ribs; 3 root blocks with β tilt (L 4.4°, C 4.7°, R 5.0°), 12.9 × 1.0 slots 3 long, 24.2 × 8.4 windows, floors at Z 44.1 / 56.7 / 44.0; 3 stop beams each with 1 M3 insert (L at Y −34, X −11; C at Y −10, X 0; R at Y +34, X +8); 6 M2 inserts for root bars, 6 for the lid, 6 for P30 | upside down (lid face on the bed) | 2 / 15 % (4 perimeters locally at root blocks) | 3 × M3, 18 × M2 | none | P30, P33, leaves, P34 |
| P33 | Palm lid with lower wrist seat | 1 | PETG | 52 × 169 × 9 | 1.6 top, 2 lap skirt; seat ring Ø 40/30; cone Ø 18/12 × 3 with keeper recess Ø 12.2 × 1.5; key peg Ø 3 × 2 hemispherical at r 17 on +X; tether cup Ø 12 × 6 and eyelet; 6 × Ø 2.4 | top face down | 2 / 15 % | none | sand seat land flat | P32, P28 |
| P34 | Root clamp bar | 3 | PETG | 24 × 8 × 3 | groove 12.9 × 0.25; 2 × Ø 2.4 at ±8.6 | groove up | 4 / 100 % | none | none | P32, leaves |
| P35 | Boot cutting template | 1 | PETG | 76 × 104 × 1 | outline of slot + 8 flange; 3 hole windows at 70 % of paddle section; alignment marks | flat | 2 / 100 % | none | none | silicone sheet |
| P36 | Cable clip | 6 | PETG | 12 × 10 × 8 | 2020 T-slot snap, 5 mm cable loop, zip-tie slot | flat | 3 / 100 % | none | none | 2020, DXL cable, reset cord |
| P37 | Control panel box | 1 | PETG | 100 × 60 × 40 | 2 × Ø 7.2 pot holes with anti-rotation slots, 1 × Ø 6.2 toggle hole, 1 × Ø 5.2 LED hole, 0/50/100 % tick recesses around each pot, cable gland Ø 6, 4 corner M3 inserts, rubber-foot recesses | face down | 3 / 20 % | 4 × M3 | none | P38, pots, toggle, LED |
| P38 | Control panel lid (base) | 1 | PETG | 100 × 60 × 2 | 4 × Ø 3.4, 4 × Ø 10 foot recesses | flat | 3 / 20 % | none | none | P37 |
| P39 | Handheld button housing, half A | 1 | PETG | Ø 36 × 110 (half) | split along the axis; top cup: 36 rim, 2 mm rim wall, button deck 2.0 thick with Ø 29.6 hole [VERIFY against the uxcell 30 mm button], deck placed so the button face is 3.0 below the rim (thumb well); 2 × Ø 3.4 counterbored; half of the gland boss Ø 12 × 10 with Ø 6 cable bore; zip-tie anchor bar 8 above the gland | split face down | 3 / 25 % | none | sand rim R 2 | P40, button, cable |
| P40 | Handheld button housing, half B | 1 | PETG | Ø 36 × 110 (half) | mirror of P39 with 2 M3 inserts; alignment pins Ø 3 × 3 | split face down | 3 / 25 % | 2 × M3 | sand rim R 2 | P39 |
| P41 | Cradle foot cup | 4 | PETG | Ø 40 × 12 | Ø 30.4 × 8 cup for the rubber foot, 2 × Ø 3.4 countersunk for wood screws | flat | 3 / 30 % | none | none | baseboard, rubber feet |
| P42 | Cradle tilt wedge | 2 | PETG | 120 × 60 × 32 | 15° wedge, anti-slip ribs, 2 mm TPU pad recess | flat face down | 3 / 20 % | none | glue pads | face cradle feet |
| P43 | Apex height gauge | 1 | PETG | 12 × 12 × 120 | rounded foot R 6; engraved rings at 80/82/84/86/88 from the foot | lying flat | 3 / 30 % | none | ink rings | scalp / foam head, cheek A mark |
| P44 | Reset cord toggle | 1 | PETG | Ø 14 × 40 | cord bore Ø 2.5, knot pocket | lying | 3 / 50 % | none | none | reset cord |
| P45 | Reset cord guide | 1 | PETG | 15 × 20 × 15 | screws to the magnet arm; Ø 3 polished cord channel, R 3 entry | flat | 4 / 50 % | none | none | P1, reset cord |
| P46 | Tip-height pull clip (for L6 a) | 1 | PETG | 18 × 13 × 20 | loop that slips over the centre seam sleeve, hook eye at nail height | flat | 3 / 100 % | none | none | fish scale |
| P47 | Load-cell filler bar (Stage 1) | 1 | PETG | 40 × 12 × 6 | 2 × Ø 3.4 matching P26 and P28 | flat | 5 / 100 % | none | none | P26, P28 |
| P48 | Tip box with slots (only if the tip lead has not supplied one) | 1 | PETG | 120 × 60 × 25 | 8 slots 11 × 5 for TM1 tangs, label recesses for blinding codes (TP §Q5) | flat | 2 / 15 % | none | none | tips |

**Printed by the tip lead's files, listed here because the hand mates with them:** T1 paddle, outer (`DRAFT_Y = 10`, `RISER = 0`), 2; T2 paddle, centre (`DRAFT_Y = 10`, `RISER = 9`), 1; T3 paddle clamp bar, 3; T4 TPU 90A seam sleeve, 3 (plus spares); the tips themselves.

**Count:** 48 MECH part designs (P1–P48), 60 printed pieces in all (P2 × 2, P34 × 3, P36 × 6, P41 × 4, P42 × 2, every other part × 1), plus 9 tip-lead pieces for the hand (T1–T4). Estimated filament: 0.9 kg PETG, 20 g TPU (pads, bumpers). Print-test first: P15 (bearing fit), P2 (bearing fit), P13 (servo fit), P34 + a leaf scrap (groove grip).


## 12. Bought mechanical parts list

Electrical parts (servo, OpenRB-150, brick, e-stop, button, pots, wire) are in EF §1.4; tips and TM1 magnets in TIPS §9. Prices are indicative. "[VERIFY]" marks a part number the BOM agent must confirm.

| Item | Spec | Qty | Plausible source |
|---|---|---|---|
| Miniature linear rail | MGN9 rail 100 mm with **MGN9C** block (MGN9H acceptable if the scale allows, D7) | 1 (+1 block spare) | Amazon "MGN9C 100 mm linear rail" kits, about $12 (CL §4) |
| Holding electromagnet | Adafruit 3872, P20/15, 5 V 0.22 A, 25 N, Ø 20 × 15 mm, M3 rear thread | 1 (fallback 3873, P25/20) | Adafruit (EF §1.4) |
| Magnet keeper | mild steel 25 × 25 × 3 mm (cut from 1/8 in × 1 in flat bar) | 1 | hardware store flat bar |
| Hinge springs | extension, 3/8 in OD, 0.031 in music wire, 2.5 in free length, about 0.54 lbf/in (0.095 N/mm), initial tension 1–2 N, max extended length ≥ 5 in (§4.3) | 4 (2 + 2 spare) | McMaster-Carr Precision Extension Springs, family 9654K [VERIFY part number]; or Amazon assortment, sorted on the scale |
| Hinge cord and reset cord | 1.0 mm braided UHMWPE (Dyneema) line, about 45 kg test | 3 m | Amazon braided fishing or kite line |
| Trim cord | 0.5 mm clear elastic beading cord | 1 roll | Amazon / craft store ("Stretch Magic" type) |
| Bearings | 625-2RS (5 × 16 × 5 mm), 623ZZ (3 × 10 × 4 mm) | 1 + 2 (packs of 10) | Amazon |
| Idler shoulder screw | Ø 5 × 25 mm shoulder, M4 × 6 mm thread, with M4 nyloc | 1 | McMaster alloy-steel shoulder screws [VERIFY], or Amazon shoulder bolt assortment |
| Hinge pin | M6 × 80 mm socket head screw, M6 nyloc, 2 × M6 nylon or PTFE washers | 1 set | hardware store / Amazon |
| 2020 extrusion | lengths 270, 104, 80 mm (cut from a 4 × 500 mm pack) | 1 pack | Amazon (CL §5.1) |
| 2020 hardware | corner bracket kit with M5 drop-in T-nuts and M5 × 10 mm screws | 1 kit (uses 2 brackets, about 20 T-nuts, 22 screws) | Amazon (CL §5.1) |
| Feeler stock (leaves) | spring steel 0.30 × 12.7 mm (0.012 × 1/2 in), 12 in strip | 2 strips (one is spare) | Precision Brand feeler stock, or McMaster feeler-gauge stock [VERIFY] |
| Wrist magnet | K&J D61, 3/8 × 1/16 in N42 disc, 9.4 N rated | 3 (1 + 2 spare, one for tuning by stacking) | K&J Magnetics (CL §3) |
| Wrist keeper | mild-steel disc 12 × 1.5 mm | 2 | Amazon "12 mm metal discs" or cut from sheet |
| Zero pin | 3 mm steel dowel or a 3 mm drill bit shank, 30 mm | 1 | hardware store |
| M8 slug washers | DIN 9021 M8 (8.4 × 24 × 2 mm), about 6.2 g each | 20 | hardware store |
| Boot | silicone sheet 0.25 mm, Shore 40A, about 150 × 150 mm; silicone adhesive (Smooth-On Sil-Poxy) | 1 sheet (makes 4 boots), 1 tube | Amazon |
| Tapes | PTFE thread-seal tape (0.075 mm) for the magnet face; 0.05 mm PTFE film tape (3M 5490 class) for the palm seam and wrist magnet | 1 + 1 roll | Amazon |
| Bumpers | self-adhesive rubber bumper Ø 10 × 6 mm (up-stop cap) | 4 | Amazon assortment |
| Isolation feet | rubber or Sorbothane feet Ø 30 × 15 mm | 4 | Amazon |
| Baseboard | 18 mm plywood 350 × 300 mm (only if the cradle shares the desk) | 1 | hardware store |
| Ballast | 3 mm mild-steel plates 100 × 100 mm, 4 × Ø 4.5 on 75 × 75, about 235 g each | 5 | laser-cut service (SendCutSend type) or steel VESA extension plates |
| Monitor arm | single gas-spring arm, VESA 75/100, minimum load ≤ 2.0 kg, reach ≥ 400 mm, tilt ≥ ±45°, head swivel ≥ ±90°, lockable rotation, desk clamp 10–85 mm (§3.2) | 1 | HUANUO / VIVO class, about $36 (CL §5.4) |
| Face cradle (SEAT) | tabletop / desktop massage face cradle with adjustable tilt | 1 | Amazon |
| Face cradle cushion (PRONE) | portable horseshoe face cushion | 1 | Amazon |
| Heat-set inserts | brass M3 (4 mm long) and M2 (3 mm), plus 1 × M4 | 100 + 50 + 1 (about 55 M3 and 18 M2 used) | Amazon kits (CL §5.1) |
| Fasteners, M2 | M2 × 6 socket (12: root bars 6, lid 6), M2 × 8 (6: knuckle plate), M2 × 6 for the servo (2) | 20 | Amazon M2 assortment |
| Fasteners, M3 steel | M3 × 6 (4 carriage + 2 countersunk keeper), M3 × 8 (5 rail + 8 mast parts + 1 magnet rear + 6 lids), M3 × 10 (4 cheek A + 2 strap + 2 idler + 2 filler), M3 × 12 (4 crossbar), M3 × 14 (4 yaw), M3 × 16 (2 pulleys + nyloc nuts), M3 washers (30) | about 50 | Amazon 1000-piece assortment (CL §5.1) |
| Fasteners, M3 special | aluminium M3 × 8 (6 paddle clamps + 2 riser-to-seat, 10-pack); nylon M3 × 10 (3 leaf stops); nylon M3 × 8 thumbscrew (weight cap); knurled M3 × 16 thumbscrew with jam nut (down-stop, trim cleat, scale lock: 3) | as listed | Amazon |
| Fasteners, M4 / M5 / wood | M4 × 50 (4, VESA and ballast) with washers; M4 × 25 (1, up-stop); M5 × 10 (22, frame); #4 × 1/2 in wood screws (8, foot cups) | as listed | hardware store |
| Adhesives | medium threadlocker (Loctite 243 class), gel CA, 5-minute epoxy | 1 each | hardware store |
| Light oil | sewing-machine oil (rail block) | 1 | hardware store |

Tools beyond EF and CL §8: aviation snips and a fine stone (leaves), mitre box and hacksaw (2020), 6.3 mm and 5.0 mm drill bits or reamers, a 0.5 N·m torque screwdriver or careful hand feel, luggage scale and kitchen scale (springs, magnets, slugs).


## 13. Assembly sequence and alignment

The order front-loads the bench tests: L2 runs on the bare hand, L3, L6 and L1 on the float before the arm exists, L5 as soon as the hinge and magnet are up (before the servo is even plugged in), and L4 last. Paint-pen torque marks on every screw once tightened (K2.15).

**Phase A: hand (about 5 h)**

1. Print the fit-test parts first (P15, P2, P13, P34 with a leaf scrap) and adjust hole compensation before the rest. Print everything else; weigh each float part as it comes off the printer and log it against §6.5.
2. Cut, round (R 1 mm) and stone the three leaves (70 / 67 / 64 mm). Mark each leaf's root bar-edge line: from the paddle end, 4 + a mm (52.3, 48.5, 45.7 mm for L, C, R).
3. Set heat-set inserts in P32 (18 × M2, 3 × M3) with the soldering iron at 220–230 °C, square to the surface.
4. Fit each paddle (T1, T1, T2 from the tip lead, with TM1 magnets and sleeves already in) onto its leaf: leaf through both wall slots, bar on, 2 × M3 × 8 mm aluminium screws, 0.3 N·m. Trim the leaf end flush with the far wall, round it.
5. Lay the leaves in the tray's root slots (L and R at level 0, C at level 1 over L), align the marked lines with the root bar edges, fit the root bars, 2 × M2 × 6 mm each, 0.15 N·m. Check by eye that each paddle hangs rolled outward by its β (4–5°) and that C's leaf clears L's paddle top by about 3 mm.
6. Thread the three nylon stop screws into the stop beams, backed well off.
7. **TP L2 (leaf rate and stop):** clamp the tray in a vise with the leaves horizontal. Press each nail on the kitchen scale against a steel rule; read force at 2, 4 mm. Trim free length (move the leaf in the root clamp; 1 mm = 6–7 %) until k = 0.12 / 0.15 / 0.18 ± 0.01 N/mm. Then turn each stop screw down until the stop is reached at 5.0 ± 0.3 mm of tip travel; threadlocker. Proof each nail to **7.5 N** on its stop (§8.4, §14) and recheck free height (no set > 0.2 mm).
8. Cut the boot with P35, bond its three holes to the paddles (Sil-Poxy bead at z 26–28 mm, cure 1 h), lay the flange over the tray underside, add P31 and the knuckle plate P30, 6 × M2 × 8 mm. Check every paddle swings full travel with no tug from the boot (the scale reading at 2 mm must not change by more than 0.01 N with the boot fitted).
9. Fit the steel keeper disc into the lid's cone (epoxy, flush), screw the lid on (6 × M2 × 6 mm), wrap the seam with 0.05 mm PTFE tape, tie the tether eyelet.

**Phase B: float on the bench (about 3 h)**

10. Set inserts in P21. Bolt the rail to the mast against the reference lip, middle screw first, 0.6 N·m, medium threadlocker. Pull the block's end seals and wipers, flush, one drop of oil, slide it on (never off the rail end without a retainer).
11. Riser P26 on the block (4 × M3 × 6 mm steel, 0.5 N·m). Down-stop block, up-stop block, shroud, scale strip, trim cleat on the mast. Upper seat P28 on the riser arm through the P47 filler (2 × M3 × 10 mm). Bond the D61 into the recess (CA), cover with one layer of 0.05 mm tape.
12. **TP L3 (float friction):** lay the crossbar flat (rail horizontal) and pull the carriage with thread and gram weights from the up-stop, mid and down-stop positions. Pass ≤ 0.1 N. Then clamp the crossbar so the rail is vertical.
13. Seat the hand on the wrist, knot the tether at 60 mm (or 25 mm, §7.3). **TP L6(a):** fish scale on the pull clip P46 at nail height: 1.5–2.5 N in +X, −X, +Y, −Y; straight down ≥ 5 N. Tune with tape layers. **TP L6(b):** tips 4–8 N pull-out (tip lead's numbers).
14. **TP L1 (dead weight):** rail vertical, hand resting on the kitchen scale with the carriage mid-travel: W1 = 0.90 ± 0.05 N; trim with M3 washers under the weight cap. Make up the +30 g and +60 g slug sets on the same scale and read W2, W3. Per-nail shares with the 10 mm block under one nail at a time: 0.8 : 1.0 : 1.2 ± 0.1.

**Phase C: elbow (about 3 h)**

15. Cut the 2020 (270, 104, 80 mm). Carrier beam with drop legs P11, P12 (M5 end screws plus T-nuts, 2 N·m), carrier yaw plate P9 on top. Servo into the cradle P13 with the strap; cradle on P11 with G2 (P17) under it; idler housing P15 (bearing pressed, one dot of CA on the outer ring) on P12 with G3 (P18).
16. Horn adapter disc P16 on the horn (servo's own M2 screws), cheek A on the disc (4 × M3 × 10 mm). Cheek B on the shoulder screw through the bearing (M4 nyloc, 1 N·m). Crossbar assembly between the cheeks (4 × M3 × 12 mm). **Idler alignment:** servo unpowered, swing the yoke by hand through the ±32° stops; slide the idler housing in its slots until there is no tight spot, then tighten. Insert the zero pin: it must slide in with the mast plumb to the carrier beam (square).

**Phase D: frame, hinge, arm (about 3 h)**

17. Adapter P1: magnet on the magnet arm (M3 rear screw, 0.5 N·m, washers to set depth), PTFE tape on its face; pulleys P2 on M3 × 16 mm with nyloc nuts; spring-anchor hooks checked; electronics tray P3 on its seat. Frame: post and spine joined with two corner brackets; knuckle P5 on the post foot; keeper lever P6 (keeper plate epoxied and screwed) and cord bar P7 on the post; frame yaw plate P8 under the spine; reset tab P10. Pin the knuckle between the adapter ears (M6 × 80 mm, PTFE washers, nyloc snug, free rotation). Bolt the carrier to the frame at 0° (4 × M3 × 14 mm).
18. Springs: hook each spring to its anchor, run its cord over the pulley to the cord bar, tie off with the frame latched (keeper on the magnet face) so each spring reads 117 mm hook to hook (6.5 N). Check on the luggage scale through the cord: 6.5 ± 0.5 N each. Fit the reset cord through P45 to the toggle P44.
19. Ballast stack and adapter onto the monitor arm (4 × M4 × 50 mm). Set the arm so it holds height without drift (K2.14).
20. **TP L5 (fail-safe lift), first pass:** with ELEC's rail wired to the magnet only (servo unplugged), latch the frame, release hold-to-run, film at 240 fps: ≥ 25 mm in ≤ 0.5 s, stays up, re-latches with the reset cord. Repeat with +60 g.
21. Plug the servo (ELEC B1–B5). **Zero** with the pin in (§5.3), not by gravity.

**Alignment (with the zero pin in, module latched):**

- Elbow axis parallel to Y: inclinometer on the carrier beam top reads 0 ± 0.5° along Y (head rotation screw); cheeks square to the beam (engineer's square on cheek A).
- Rail radial and plumb: inclinometer on the mast face and side reads 90 ± 0.5° (arm head tilt for pitch, rotation for roll). Recheck after every aim change (TP §0: ±1° for sessions).
- Axis height: apex gauge P43 on the foam-head apex, 80 mm ring level with the axis mark (H = 80 mm).
- Nails at O: plumb line from the axis mark on cheek A lands on the centre edge within ±1 mm in X; axis to centre edge 84.0 ± 0.5 mm (down-stop thumbscrew); outer edges 3.6 ± 0.3 mm below the centre edge (0.25 mm PETG shims under a root clamp raise that nail about 0.3 mm at the tip). Final check: on the 180 mm sphere at W1, all three nails touch together (carbon paper).

22. **TP L4 (lift-off chord)** on the R 90 mm form, then L7–L12 (§14).


## 14. Mechanical bench tests before human use

Every test below runs on the bench, mannequin or foam head before any human session (safety §6, TP §K, §L). Numbers are pass levels; TP's tables are the record.

| Test | TP ref | What MECH must show | Pass level |
|---|---|---|---|
| Float free, stiction | K2.1, L3 | carriage slides full travel under its own weight; horizontal pull and vertical hysteresis | F_f ≤ 0.10 N everywhere, no spot > 0.15 N |
| Float travel | K2.2 | stop to stop | 24 + e mm (28 mm at e = 4 mm; TP asks 25–30 mm) |
| Down-stop and pointer | K2.3 | thumbscrew locked, scale zeroed on the down-stop, apex gauge sets e | e = 2 / 4 / 6 mm ± 0.3 mm; pointer reads e − W/Σk at mid-stroke (§9.3) |
| Dead weight | K2.4, L1 | kitchen scale, carriage floating | W1 0.90, W2 1.20, W3 1.50 N, each ± 0.05 N; three reads within ± 2 g |
| Per-nail shares | K2.5, L1(c) | block under one nail | 0.8 : 1.0 : 1.2 ± 0.1; ratio heaviest / lightest 1.2–1.6; no nail > 0.6 N at W2 |
| Leaf rate, stop, set | K2.6, K2.7, L2 | scale and rule per nail | k 0.12 / 0.15 / 0.18 ± 0.01 N/mm (inside 0.1–0.25 N/mm); stop at **5.0 ± 0.3 mm** (D5; TP's 8–10 mm to be amended); force at stop ≤ 2.4 N (expected 0.6–0.9 N); set ≤ 0.2 mm after 5 stop hits |
| Leaf-stop proof (MECH addition, resolves c) | K1.2, safety §3.6 | 7.5 N per nail at the tip, leaf on its stop, 10 s, each nail | no slip at root or paddle clamp, no crack or whitening, free height back within 0.2 mm |
| Wrist breakaway | K2.8, L6(a) | fish scale on P46 at nail height, ±X, ±Y | 1.5–2.5 N (design 1.9–2.1 N); straight down ≥ 5 N; keyed re-seat by hand. At the knuckle plate expect 4.3–4.7 N (§7.2) |
| Tether | K2.9 | released hand hanging | ≤ 60 mm below the carriage (≤ 25 mm if shortened), cannot reach the face envelope |
| Tip breakaway and proof | K2.10, L6(b) | tip lead's method | 4–8 N pull-out; proof per safety §3.6 at 7.5 N normal, 6 N lateral (not 2.4 N, §8.4) |
| Fail-safe lift | K2.11, L5 | 240 fps video: hold-to-run release, e-stop, plug pull, 10 each, from mid-stroke and stroke ends, with +60 g | nail rise ≥ 25 mm (expected 33 mm at the frame, ≥ 29 mm clear of the scalp) in ≤ 0.5 s (expected ≤ 0.14 s), 30 / 30, stays up |
| Hold at up-stop and re-latch | K2.12 | heaviest hand and +100 g slug | stays at the up-stop indefinitely; re-latches at 5 V with the reset cord (about 10 N) |
| Spring check (MECH addition) | K2.11 support | luggage scale through each cord, latched and at the up-stop | 6.5 ± 0.5 N and 3.9 ± 0.5 N each |
| Magnet hold (MECH addition) | K2.12 support | luggage scale pulling the keeper lever foot forward, rail live, after a 20 min run | pull-off ≥ 19 N (load is ≤ 14.5 N) |
| Frame yield (MECH addition) | D10 | push up at the centre nail with the float jammed on its up-stop | frame lifts at 8–11 N; record it |
| Firmware limit vs mechanism | K2.13, L4(e) | `goto ±28`, carriage on the down-stop | centre nail ≥ 10 mm clear (expected 14.9 mm); trailing outer nail expected 9.1 mm (flag §15); no contact with the ±32° stops |
| Arm stability | K2.14 | 30 min with the module at set height | drift ≤ 2 mm |
| Fasteners, slugs captured | K2.15 | shake test, torque marks | nothing rattles; slugs held by the cap |
| Moving mass and speed | K2.16 | float mass, peak tip speed | ≤ 160 g including slugs (W3: 150 g); ≤ 0.4 m/s |
| Lift-off chord | L4 | carbon paper on the 180 mm sphere, E2 / E4 / E6 | 26 / 37 / 46 mm ± 5 mm; all three nails mark; gap at ±25° ≥ 5 mm on every nail |
| Hair probe of the hand | K1.8, K1.10, L8.6 | 100 µm monofilament at the slot, boot, sleeves, palm seam, wrist | no capture; all gaps within 25 mm of the scalp ≥ 3 mm (§8.7 table) |
| Clearances in motion (MECH addition) | §2 checks | full ±32° by hand with the float pushed to its up-stop, then a fail-safe drop at ±28° | no contact anywhere; ≥ 8 mm by feeler at the listed points |
| **Per-session lift check (MECH addition to K5)** | K5 | one hold-to-run release with the hand over the foam head before the head goes in | frame lifts fully and re-latches |


## 15. Known risks, open conflicts, build-review checklist

### 15.1 Open conflicts for the integrator

1. **(c) Proof load:** safety §3.6 (≈ 7.5 N normal, 6 N lateral, 3 × rated) versus TP L6(b) (2.4 N on the leaf stop). The leaf hard stop, root clamps and paddle clamps are designed and bench-proofed to **7.5 N per nail**; the stop *position* separately keeps leaf force at the stop ≤ 2.4 N (0.6–0.9 N). Recommend amending L6(b) to 7.5 N.
2. **Leaf travel:** freeze §1.7 and TP K2.6 / L2 say 8–10 mm; this design uses 5.0 mm (D5) because paddle roll at 8 mm closes adjacent tip gaps below 3 mm. Amend TP to 5.0 ± 0.3 mm.
3. **Pitch 24 mm** instead of 20 mm (D2). The sensation lead should confirm 24 mm is acceptable (it is inside the 20–25 mm spread-finger range, TI §6).
4. **L6(a) pull point:** at the knuckle plate the wrist releases at 4.3–4.7 N, at nail height 1.9–2.1 N. Amend L6(a) to pull at nail height (P46) or restate its band.
5. **K2.13 / L4 at ±28°:** the trailing outer nail is 9.1 mm clear, not 10 mm, because of the frozen ±8 mm stagger. Accept 9 mm for outer nails, or keep HUMAN mode inside ±25°.
6. **Engagement definition:** the pointer reads e − W/Σk, not e; at E2 the dead weight never floats (§9.3). Define E as geometric engagement (apex gauge) and consider E6 as the default.
7. **Zero calibration (ELEC):** the arm is top-heavy and will not hang plumb; EF §4.2 `zero` must be done with the zero pin (§5.3), and a limp arm may drift to a stop when unpowered (harmless: the frame lifts at the same moment).
8. **Absolute force cap (D10):** the leaf stop is not the absolute per-nail cap. Free float: dead weight (≤ 1.5 N). Float jammed on its up-stop by a head rise > 24 mm with the button held: up to the frame yield, 8–11 N total at the nails. Red line 2 is met in normal use by the dead weight; the residual relies on the hold-to-run release. The safety gate should rule on it.
9. **Tether (H-6.4, H-4.13):** the hair rules prefer untethered breakaways; the freeze tethers the hand so it cannot fall on the face. Keep the tether, stow it in its cup, and consider 25 mm instead of 60 mm so the fail-safe lift also lifts a released hand.
10. **Under-voltage window:** between about 3.3 V and 3.7 V the servo can brown out while the magnet still holds the frame (nails at the dead weight). Covered by hold-to-run release; the firmware's rail-sense input could warn.
11. **Paddle changes requested of the tip lead:** `DRAFT_Y = 10`, new `RISER` (9 mm on the centre paddle), lighter print settings (§8.9).
12. **Internal yaw joint:** usable only at 0° and 180° in Stage 1 (the carrier hits the post at 45°); Stage 1 yaw is the monitor-arm head swivel. Stage 3's yaw servo needs a bearing under the plates.
13. **Freeze frame text (D9)** and lift-off numbers (D12) should be corrected in the freeze for the next agents.

### 15.2 Known risks

| Risk | Likelihood | Consequence | Mitigation |
|---|---|---|---|
| Bare float above 92 g (budget margin 2 g) | high | W1 off spec | weigh as you print; aluminium screws; trim cord; MGN7C fallback (§6.5) |
| Paddle roll larger than calculated (leaf clamp compliance, print tolerance) | medium | tip gaps shrink | L2 measures roll too: photograph each paddle at 0 and 5 mm; gaps in §8.7 have 1.4 mm or more of margin over 3 mm |
| Boot tears or stiffens | medium | hair entry or a few hundredths of a newton of drag | weekly replacement, spare sheet (TP packing list) |
| Printed adapter ears creep under 13 N spring plus 8 N weight | medium over weeks | hinge droops, nail height drifts | ribs, 5 perimeters, 40 % infill; re-check axis height at every session with the apex gauge |
| Idler misalignment binds the yoke | medium at first build | servo current up, jerky strokes | slotted housing, free-swing check (§13 step 16), ELEC current log |
| XL330 drawing dimensions differ from my assumptions (axis position, horn holes, mounting holes) | medium | reprint of P13, P16 | marked [VERIFY]; both are small fast prints |
| Spring part not exactly as specified | medium | lift time or up-stop hold changes | bench acceptance numbers in §4.3 are binding |
| Nails move 28 mm away from the hinge during the lift | certain | lifted nails travel toward wherever +X points | aim rule §4.5 |
| Module size (about 270 × 200 × 220 mm, 1.0 kg plus 1.1 kg ballast) above the head | certain | looks large, needs a sturdy desk | clamp plate, arm rated load, glasses on |
| Stroke rhythm through the desk | medium | confound in ratings | separate stand or isolation feet (§10.2) |

### 15.3 What the build reviewer should check

1. The §2 swept-volume list with the CAD solids, including the float at its up-stop and the frame at its 25° up-stop.
2. That every gap in the §8.7 table is ≥ 3 mm on the printed hand at 0 and 5 mm of leaf deflection, with W and B45-12 tips.
3. The §6.5 mass ledger against real part weights before final assembly.
4. That the magnet is fed only from the rail after the hold-to-run (EF §1.6) and that L5 passes with the +60 g slug.
5. Spring forces through the cords (§4.3 numbers) and the up-stop hold with +100 g.
6. The 7.5 N proof on each leaf stop and the wrist breakaway at nail height.
7. The VERIFY items: XL330 axis position, horn and body hole patterns, MGN9C block hole pattern, MGN9 rail hole pitch, OpenRB-150 outline, uxcell button hole, spring part number, shoulder-screw part number.
8. That nothing fixed was moved above the hand during building (it would end the float travel), and that the zero pin, not gravity, sets the servo zero.

