# SP1 DESIGN FREEZE — frozen architecture and interfaces for the engineering phase
(All engineering agents build to this. Deviations must be flagged in your report, not silently made.)

## 0. Coordinate frame
Z = up (gravity = −Z). X = stroke direction (arm swings in the XZ plane). Y = across the stroke (nail pitch direction). Origin O = tip of the CENTER nail at mid-stroke, nominal 4 mm engagement into the scalp. Michael's head: crown/occiput apex at O, scalp approximated as a sphere R = 90 mm centered at (0, 0, −90).

## 1. Stack, top to bottom
1. MONITOR ARM: desk-clamp gas-spring single-monitor arm (VESA 75/100 plate, 2–9 kg rating; module ballasted to ≥ the arm's minimum rating if needed). Arm reaches over the seated user's head from the side/behind.
2. VESA PLATE ADAPTER (printed): bolts to VESA 75×75 (M4). Carries the FAIL-SAFE HINGE.
3. FAIL-SAFE HINGE: horizontal hinge axis parallel to Y, located ~60 mm behind (−X) the elbow axis. Module frame hangs from it. Working position = frame rotated DOWN against a stop, held by a 5 V HOLDING ELECTROMAGNET (≥ 25 N / 2.5 kg, 20–25 mm dia) on the adapter against a steel keeper on the frame; an extension spring (6–10 N at working extension) pulls the frame UP. Power to the magnet comes from the ACTUATOR RAIL (see §5). Loss of actuator power → frame rotates up to the up-stop → nails rise ≥ 25 mm. Reset by pressing the frame down until the magnet re-latches (power on).
4. MODULE FRAME (printed PETG or 2020 extrusion 120–150 mm): carries (a) the YAW JOINT — Stage 1: a fixed bolted joint with a 40×40 mm M3 pattern; Stage 3: an XL330 replaces it, rotating the elbow assembly about a vertical axis offset 25 mm (−X) from the hand center; (b) the ELBOW SERVO: Dynamixel XL330-M288-T, output axis parallel to Y, horn facing +Y, axis at (0, 0, +84) nominal (H = 80 mm above the scalp apex + 4 mm engagement); (c) the GUARD PLATE: smooth, drafted (≥10°), rounded (R ≥ 3 mm) plate under the servo/frame between mechanism and hair, with an opening giving ≥ 10 mm clearance to everything that moves through it (gaps ≥ 3 mm are hair-safe; gaps 0.04–3 mm are forbidden near hair).
5. ARM + RADIAL FLOAT: an arm bracket on the elbow horn carries an MGN9H miniature linear rail (100 mm) aligned RADIALLY (along the arm, i.e. vertical at mid-stroke). The carriage (MGN9H block, seals removed, lightly oiled) carries the HAND via the WRIST. Carriage travel 25–30 mm between an UP-STOP and an adjustable DOWN-STOP (M3 thumbscrew, sets engagement e = 2–8 mm; default 4 mm). Dead weight = carriage + wrist + hand + ADDED WEIGHTS (stack of M8 washers/nuts on a post, 0–100 g). Total floating weight W = 0.9–1.5 N (0.3–0.5 N per nail). Nominal elbow-axis-to-nail-tip distance at the down-stop L_max = 84 mm; in contact at mid-stroke L = 80 mm (float compressed 4 mm).
   Geometry check (frozen): gap between tip arc and sphere at angle θ: d(θ) − H with d = (H+R)cosθ − sqrt(R² − (H+R)² sin²θ), H = 80, R = 90 → 4.1 mm at 13°, 19.9 mm at 25°. Contact chord ≈ 36 mm at e = 4 mm; nails are fully lifted by ±25°. Stroke limits in firmware: ±28° absolute, ±25° nominal max. Both stroke directions are contact strokes (bidirectional rake, human primitive P1) with lift-off at both ends by geometry.
   Force variation along the stroke from the inclined rail is bounded: N = W cosθ/(1 ∓ µ sinθ) → 0.84–1.16 W at ±13° for µ = 0.7. Accepted.
6. WRIST: hand attaches to the carriage through a keyed magnetic seat that breaks away at 2.0 N tangential (red line 3), tethered by a 60 mm cord to the carriage so a released hand cannot fall onto the face; re-seats by hand.
7. HAND: three nails at 20 mm pitch in Y, stepped ±8 mm in X (fingertip-arc stagger). Each nail is on its own spring-steel feeler-stock leaf (0.3 × 12.7 mm, length tuned) cantilevered ALONG Y (perpendicular to the stroke) so normal compliance is symmetric in ±X and drag loads the leaf only in torsion (checked: ~2° at 0.3 N drag, negligible). Normal rate 0.1–0.25 N/mm, travel 8–10 mm to a hard stop (absolute cap ≤ 2.4 N/nail = red line 2). Preloads unequal: approx 0.8 / 1.0 / 1.2 × W/3 by leaf length or shim. Leaves, roots and stops are ENCLOSED in a printed palm (clamshell) above a smooth KNUCKLE PLATE; the printed PADDLES (1 mm thick, ≥10° draft, no steps, no fastener heads below the canopy) exit through ≥ 4 mm clearance holes covered by a TPU boot or thin silicone sheet with slits, and protrude ≥ 25 mm below the knuckle plate to the TM1 pocket.
8. TIPS: SP1-TM1 mount per 01-foundations/tip-interface.md (10 × 4 × 12 mm chamfered tang, 10.3 × 4.3 × 12.5 mm pocket, N52 6×2 magnet + 6×1 steel disc, 4–8 N breakaway, seam sleeved). Tip set for SP1 (all R ≥ 0.4 mm for first human sessions; 0.3 mm only after forearm screening + UL 1439 tape test):
   - W  symmetric wedge, 8 mm wide, two 45° faces, R 0.4 mm — DEFAULT for bidirectional raking
   - B45  nail-mimic 45° blade, 8 mm loaded edge, R 0.5 mm (unidirectional mode)
   - B45-12  same, 12 mm wide (width variable)
   - A45  nail-mimic, R 0.3 mm (experimental, gated)
   - E  B45 geometry on a TPU 90A pulp pad (compliance-in-tip variable)
   - H  3 mm ball — massager CONTROL tip
   - P  trimmed press-on acrylic nail in a TM1 carrier — zero-fabrication reference
9. ELECTRONICS (Stack A, trimmed): OpenRB-150 (logic powered by USB from a laptop or USB charger); Dynamixel power from a 5 V 4 A UL-listed adapter through the ACTUATOR RAIL; XL330 ID 1 = elbow (ID 2 = yaw, Stage 3); potentiometers: SPEED, VARIATION; toggle: PERIODIC/HUMAN; momentary HOLD-TO-RUN handheld button; NC 22 mm mushroom E-STOP. No OLED, no INA219, no load cell in Stage 1 (reserve a 40×12 mm bar-load-cell mounting slot in the wrist for Stage 3).
10. ACTUATOR RAIL (hardware safety loop): 5 V adapter (+) → E-STOP (NC) → HOLD-TO-RUN (NO momentary, held closed by the free hand) → [Dynamixel VIN on OpenRB-150] and [electromagnet] in parallel. Releasing the button or hitting e-stop removes servo power AND drops the magnet → spring lifts the module. Firmware additionally: watchdog, position limits ±28°, velocity limit, goal-current limit ≈ 1.2 N tangential-equivalent at the tip, torque-off on fault, start/stop only in the lifted (+25°) position.

## 2. Pattern spec v1 (firmware)
HUMAN mode: stroke amplitude 12–25° (chord 33–68 mm incl. lifted portions; contact chord ≤ 36 mm), peak tip speed 50–150 mm/s (SPEED pot scales), sinusoidal or trapezoidal profile with randomized asymmetry, 1–3 strokes/s; per-stroke jitter on amplitude ±25%, speed ±25%, and a random end-dwell 0–300 ms; every 4–10 strokes a pause 0.5–3 s in the lifted position; every 5–20 s an "episode" change (new amplitude/speed bands, occasional single slow long stroke). VARIATION pot scales all jitter 0–100%. PERIODIC mode: fixed 18°, fixed speed, no pauses. Startup: torque on at +25° lifted, 1 s hold, ramp in. Shutdown: finish stroke at +25°, torque off. Fault (comm loss, over-current, watchdog): torque off (hardware rail handles the lift).

## 3. Stage plan (gated)
- Stage 0 (3 h, ~$30): Day-0 HAND WAND — one TM1 holder on a 0.3 × 12.7 feeler leaf on a 150 mm printed handle; tips W, B45, A45, H, P. Go/no-go: nail reaches skin through Michael's hair; W or B45 clearly beats H on the scalp.
- Stage 1 (≈ 15 h, ≈ $250): full rig, elbow servo only, PERIODIC + HUMAN modes. Go/no-go: bench + wig head pass; first human sessions rate "fingernails" ≥ 4/7 on at least one tip.
- Stage 2 (0 h): experiment matrix on Stage 1 hardware (tips × weight × speed × variation × direction).
- Stage 3 (+ $27–45, 3 h): YAW servo if habituation/monotony dominates feedback; load cell if force data is needed.

## 4. Ownership
- MECH LEAD: §1 items 2–8 full mechanical design, dimensions, printed-part geometry, assembly sequence, bench tests of mechanics. File: 05-engineering/mechanical.md
- TIP LEAD: §1 item 8 tips + TM1 holder + Stage-0 hand wand, drawings, OpenSCAD. File: 05-engineering/tips.md (+ cad/tips/*.scad)
- ELEC/FIRMWARE LEAD: §1 items 9–10, §2, wiring diagram, firmware source. File: 05-engineering/electronics-firmware.md (+ firmware/sp1_scratch/sp1_scratch.ino)
- TEST LEAD: safety checklist, bench tests, staged human protocol, experiment matrix, feedback form, iteration map. File: 05-engineering/test-protocols.md
- CAD AGENT (after MECH): OpenSCAD + STL for every printed part. Folder: 05-engineering/cad/
- BOM AGENT (after MECH/ELEC/TIP): 05-engineering/bom.md
