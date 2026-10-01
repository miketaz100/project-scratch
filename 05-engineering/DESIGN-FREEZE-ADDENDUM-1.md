# DESIGN FREEZE ADDENDUM 1 — director rulings on engineering deviations (2026-10-01, cloud session)

Binding for the CAD agent, BOM agent, integrator and all three gates. Where this addendum and DESIGN-FREEZE.md disagree, this addendum wins. Source of each deviation: 05-engineering/mechanical.md §1 (D1–D13) and §15, 05-engineering/tips.md §1 and §10.

## Accepted as written in mechanical.md
- **D1** Paddle thickness: the freeze's "1 mm" was an error. Paddles are the tip lead's paddle_with_pocket (14 × 9 mm nose, 28 × 14 mm root, 44.0 mm from leaf floor to nail edge).
- **D2** Nail pitch 24 mm in Y (span 48 mm), not 20 mm. Reason accepted: at 20 mm, paddle roll under leaf bending closes adjacent tip gaps to 0.4 mm, inside the hair-trap range. 24 mm is inside the human 20–25 mm spread-finger range. **The SENSATION GATE must explicitly assess whether 24 mm pitch changes the fingernail illusion**, and the experiment matrix keeps pitch as a noted constant.
- **D3** Paddle SCAD overrides: `DRAFT_Y = 10`, and a new `RISER = 9` mm on the centre paddle so its leaf crosses one level above the left paddle. Implemented by the tip lead follow-up (this session), STLs regenerated.
- **D4** One shared knuckle-plate slot sealed by one slack 0.25 mm silicone membrane bonded to each paddle; no sliding seal.
- **D5** Leaf travel to the hard stop 5.0 mm (range 4.5–5.5 mm), not 8–10 mm.
- **D6** Servo beside the palm on the −Y side, horn facing +Y, driving a two-sided yoke with an idler bearing on +Y; MGN9 rail on the yoke's front mast. Lift-off geometry, L_max = 84 mm and all firmware constants unchanged. **The BUILD REVIEW must check the yoke's alignment procedure and the idler bearing's hair exposure.**
- **D7** MGN9C carriage (16 g) instead of MGN9H; H allowed if the scale shows margin.
- **D8** Module frame is 2020 extrusion: 270 mm elbow-carrier beam, 90 mm post, 80 mm spine.
- **D9** Coordinate clarification: scalp sphere centre (0, 0, −86) mm, apex at Z = +4 mm, O = centre nail edge at mid-stroke with the float on its down-stop. All geometry uses freeze §1.5 numbers.
- **D10** The leaf hard stop is a backstop, not the absolute force cap. While the float is free, the cap is the dead weight W ≤ 1.5 N. If the float reaches its up-stop (head rise > 24 mm) force can rise to about 9 N total before the hinge yields. **The SAFETY GATE must rule on D10**: the procedural cover is hold-to-run release; the bench test is L5 plus a deliberate float-jam test at the up-stop.
- **D11** Two extension springs in parallel, 6.5 N each at working extension, acting through Dyneema cords over 623ZZ pulleys at a 64 mm lever; one spring alone must still lift the module (redundancy test in L5).
- **D12** Lift-off clearance at ±25° is 15.9 mm at the down-stop (freeze's 19.9 mm was for L = 80 mm). Still ≥ 10 mm; accepted.
- **D13** Leaf torsion under 0.3 N drag is 3.6–5.0°, not ~2°; accepted as useful tangential compliance.

## Additional rulings on mechanical.md §15 conflicts
1. **Proof load.** The leaf stop structure is designed to 7.5 N per nail (safety-requirements §3.6). test-protocols L6(b) is amended: proof the stop at 7.5 N; confirm force at the stop stays ≤ 2.4 N in normal operation (L2).
2. **Wrist breakaway test point.** test-protocols L6(a) is amended: pull at nail height, not at the knuckle plate; expected release 1.9–2.1 N tangential.
3. **Tether length 25 mm, not 60 mm.** The fail-safe lift (32.9 mm rise) must lift a released hand clear of the head; a 25 mm tether does, a 60 mm one does not. The hand hangs above the head, so a 25 mm drop cannot reach the face. Freeze §1.6 is overridden.
4. **Engagement E is geometric engagement** (down-stop position relative to the scalp apex), read on the rail scale; the pointer reads E minus leaf deflection. E4 stays the default for the first sessions; E6 is added to the matrix as a candidate default if the dead weight does not float at E4 (integrator: note in sections C, M and N).
5. **Servo zero.** ELEC zeroes the servo against the mechanical zero pin added in mechanical.md §13, never by letting the arm hang (it is top-heavy). Integrator: add to the bring-up steps in section I/J; build reviewer: check the firmware's zero procedure matches.
6. **Trailing-nail clearance at ±28° is 9.1 mm**, not the 10 mm K2.13 asks for, caused by the frozen ±8 mm stagger. Accepted for SP1 (≥ 3 mm hair rule is satisfied by a wide margin); K2.13 amended to ≥ 9 mm.
7. **Servo brown-out window (3.3–3.7 V) while the magnet still holds.** ELEC: the firmware's rail-sense threshold must treat < 4.0 V as rail-dead and torque off; BOM: the 5 V 4 A brick and 22 AWG rail keep the drop under 0.2 V at 0.6 A. Safety gate to confirm.
8. **Stage 1 yaw** uses the monitor-arm head swivel (0/45/90° by tape marks); the internal 40×40 joint works only at 0°/180°. Freeze §1.4(a) Stage 1 wording is overridden; §Q6 is satisfied by the arm head.

## Items still open for the build reviewer
- Several XL330 vendor dimensions (axis position, horn and body hole patterns) and the MGN9 hole pitch are marked [VERIFY] in mechanical.md; check against the Robotis and HIWIN drawings before printing the servo cradle and rail mast.
- Lift-spring part number: mechanical.md gives a McMaster 9654K family and a selection rule; the BOM agent must pin an exact part.
- Bare floating weight margin is 2 g against the 92 g limit; the scale decides (L1), fallbacks listed in mechanical.md §6.5.
- Firmware has not been compiled with a real toolchain (unreachable from the cloud session); compile in the Arduino IDE per firmware/README.md as the first step of the build review.
