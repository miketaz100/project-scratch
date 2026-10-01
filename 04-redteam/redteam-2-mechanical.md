# RED TEAM 2 — Mechanical, Hair, Safety, Tolerances: attack on LEADING ARCHITECTURE v0 ("SP1 FLOAT-ARM")

**Role:** adversarial reviewer. **Date:** 2026-10-01. **Inputs:** BRIEF §9/§10/§14/§22, hair-interaction, safety-requirements, component-landscape, tip-interface, LEADING-ARCHITECTURE-v0, judge-2-engineering, team-D/G/F/E. All numbers recomputed in a scratch script (leaf stress, float statics, three-nail load split, Hertz line contact, nail root stress, flexure stiffness). **[KNOWN]** sourced · **[EST]** my estimate, arithmetic shown · **[VERIFY]** must be checked on the bench.

**Verdict:** v0 is salvageable, but as written its central promise — "normal force is a mechanical constant set by a dead weight" — is false by geometry (§1); its fail-safe is wrong-way for the crown configuration (§5, §8); and its hand scores 27/36 on the hair checklist, below the 28 floor for human testing (§9). All three are fixable for under $30 and ~6 h, and the fixes simplify the machine.

---

## 1. The inclined float is a friction amplifier, not a constant-force device

v0 §3 adopts D's "inclined-parallelogram float, links inclined 30° from radial toward the stroke direction, so the tip lifts up-and-forward". Free body of the hand: dead weight W, scalp normal N, drag µN opposing the stroke; parallelogram links transmit only axial force. With the hand *leading* its pivots (the geometry that gives up-and-forward lift), vertical equilibrium gives **N = W/(1 − µ·tan 30°) = W/(1 − 0.577µ)** [EST, derived]:

| µ at the tip | N/W, leading hand (v0 as drawn) | N/W, trailing hand (links flipped) |
|---|---|---|
| 0.3 (hair interposed) | 1.21 | 0.85 |
| 0.5 | 1.41 | 0.78 |
| 0.7 (sebum-rich scalp, tip-interface §2.6) | 1.68 | 0.71 |
| 1.0 (bare or damp scalp) | 2.37 | 0.63 |
| 1.73 | ∞ (jams) | 0.50 |

Consequences: (a) at the µ = 0.6–1.0 the tip-interface doc expects on a scalp, a "0.6 N" setting delivers 0.9–1.4 N and a "2.0 N" setting 3.0–4.7 N, caught only by the leaf stops (3 × 2.4 = 7.2 N); (b) the gain depends on hair state and tip material, so the force–pleasure experiment loses its independent variable; (c) it is positive feedback — a snag raises drag, drag raises N, N raises drag — so a nail that catches a strand digs instead of yielding, undoing the "drag lifts the nail" leaf orientation one level down; (d) the lift servo must overcome the amplified N, not W. Judge 2 flagged the float only for friction and play; this flaw survives a perfect float. **Fatal to the "mechanical constant" claim; certain by statics.** Fix: a purely vertical float (α = 0 → N = W for any µ); the up-and-forward tip path comes from the elbow still moving forward when the lift fires (100 mm/s forward + 5 mm in 40 ms up ≈ 50° path). Hardware in §11.

Residual float facts after the fix: inertial force/W = ω²x/g with x = 3.85 mm (half the 7.7 mm arc rise: 4.1 mm arm arc + 3.6 mm scalp drop at ±18°) = 6 % at 2 Hz, 14 % at 3 Hz [EST] — acceptable. Any float reverses direction twice per stroke, so a stiction band F_f is a ±F_f step at the same point every stroke — predictable jitter, the wrong kind. If the float **binds**, the leaves take the whole 7.7 mm: 0.4 N/mm × 7.7 = 3.1 N swing, so every stroke becomes a 0 → 2.4 N (stop) → 0 bell per nail, 7.2 N total; the load cell sees it, the leaf stop is the only barrier.

---

## 2. Where hair gets caught

The design-basis exclusion zone is 30 mm, but for 5–8 cm hair the same rule (H-6.1) makes it hair length + 10 mm = 60–90 mm, and the paddles stand hair up. v0 inherits G's *open* hand (leaves and carrier exposed under a flat guard at z ≈ 58 mm), not D's closed palm shell.

| # | Feature (height) | Trigger → consequence | Fix |
|---|---|---|---|
| H1 | Tip edge, corners R 1.5 | Strand folded under the edge, then a reversal in contact from head motion (§5) → loaded at µN = 0.3–0.65 N, above the 0.36 N pluck floor | Lift-at-reversal (present) + head-motion reflex |
| H2 | TM1 seam under a TPU collar (8–10 mm, *in the pile*) | ≥1 mm step facing the stroke on a hair-grabbing surface (H-4.7) → strand hooked; the snag reflex lifts with it hooked → pluck | Bond blade to paddle for human tests (no seam in the pile); swap paddles, not tips |
| H3 | Paddle root → TM1 block (≈30 mm) | Re-entrant step unless filleted | 1 mm fillet, polish |
| H4 | 0.3 mm feeler-stock leaves, sheared (30–45 mm) | Burr, edge R ≈ 0.05 mm, moving 8–10 mm relative to the carrier → strand sawn or carried into H5 | De-burr, R 2 corners; enclose (H6) |
| H5 | Leaf-to-carrier wedge and the leaf **stop lug** (35–45 mm) | Gap closes from ~8 mm to 0 every stroke: the classic closing V → strand clamped at 2.4 N and dragged by the arm, S3–S4 | Enclose (H6) |
| H6 | Carrier clamps, M3 heads, print seams | Trap-band gaps | **Adopt D's closed palm shell**: only three drafted stems exit through ≥3.5 mm pass-throughs that widen inside |
| H7 | Parallelogram links, four 623ZZ pivots (35–60 mm if "between the arm and the hand" means below the guard) | Scissoring link/housing gaps change every float stroke; bearing shields 0.1–0.2 mm → S3–S4 | Float **above the guard** on the stem (§11), or boot it |
| H8 | Dyneema tendon, slack by design | A slack 0.4 mm cord in hair reach is a loop former; H-6.1 names "cable" → lasso at full lift force | Tendon only above the guard, or a rigid lift lever |
| H9 | 1 kg bar load cell in series (gauge slot ≈ 1 mm, bolt heads) | Trap-band gaps if below the guard | Above the guard with the float |
| H10 | Guard window (32 × 14 mm, stem ±18°) | Open ≥4 mm gap, hair wiped not pinched | Keep; R 2 edges, stem widens upward |
| H11 | Elbow horn | <40° oscillation above the guard | Confirm no slot in the horn adapter |
| H12 | Wrist detent after a break | D specifies no return; the palm stays swung 15 mm → next stroke runs floppy: judder, chatter, strand pinched as the palm/float gap closes | 0.2 N return spring; bumper inside the shell |

All of H2, H5–H9 are one decision: close the hand and lift the float above the guard (≈30 g PETG, 2 h).

---

## 3. What hurts

**Per-nail force.** Three nails on 0.4 N/mm leaves, preloads 0.3/0.4/0.2 N, centre nail landing first by the curvature mismatch, float descending until the sum equals the hand force [EST]:

| Hand force | Mismatch | Per nail (centre / outer / outer) |
|---|---|---|
| 2.0 N (max dead weight, α = 0) | 0 | 0.67 / 0.77 / 0.57 |
| 2.0 N | 2.2 mm (R 90 carrier on a flatter or R 75 patch) | 1.25 / 0.47 / 0.27 |
| 2.0 N | 3.0 mm | **1.50 / 0 / 0** |
| 3.36 N (2.0 N through the v0 incline at µ 0.7) | 3.0 mm | **1.92 / 0.82 / 0.62** |

With the float as drawn and 3 mm of mismatch, the heaviest nail carries 1.9 N: 2× the top of the scratch window (0.9 N), above the human "high" scratch (1.56 N). With the incline fixed, 3 mm still puts the whole 2.0 N on one nail — inside red line 2 but a single hard nail, not a hand. ±3 mm is ordinary: R 90 vs R 75 across 40 mm (sagitta 2.2 vs 2.7 mm) plus a 5° roll of the module (20 mm × sin 5° = 1.7 mm).

**Pressure** (Hertz line contact, E* = 40 kPa, as tip-interface §2.2) [EST]:

| Edge R | Force | Loaded length | p₀ | Line load |
|---|---|---|---|---|
| 0.6 / 0.4 mm | 0.65 N | 6 mm | 48 / 59 kPa | 0.11 N/mm (crisp scratch) |
| 0.6 / 0.4 mm | 1.6 N | 6 mm | 75 / 92 kPa | 0.27 N/mm (pricking at ≤0.3 mm edge) |
| 0.4 mm | 2.0 N | 6 mm | 103 kPa | 0.33 N/mm |
| 0.6 mm | 0.65 N | **2 mm** | 83 kPa | **0.33 N/mm** |
| 0.4 mm | 2.0 N | **2 mm** | 178 kPa | **1.0 N/mm** |

Depth exceeds R in every row, so these are plough regimes and the line load is what the skin reports (tip-interface §2.3–2.4: window 0.05–0.15 N/mm; ~0.3 N/mm on a loaded corner is sharp pain). **The 2 mm rows are the occipital protuberance:** a press-on nail is transversely convex (R 9), so on a ridge of R 10–15 mm its two R 1.5 corners touch first and the loaded length collapses to ~2 mm — 0.33 N/mm at the *nominal* 0.65 N, 1 N/mm at the mismatch load. Bone-backed PPT (106–226 kPa) is not the limit; corner line load is. The nape adds thinner skin, nuchal ridges, and a hairline the outer nail runs off onto bare neck (µ 0.6–1.0, drag doubles, and with the v0 incline N follows). Fix: occiput/nape lanes at ≤0.3 N per nail; a flat pick-stock blade variant for ridges; aim ≥20 mm from the inion.

**Flinch (±20 mm at 0.3 m/s).** Away: float goes 10 mm to its stop, nails leave the skin, dead-man opens — safe. Sideways: §5. **Toward the hand:** ~10 mm of float up-travel, then 6 mm of leaf to the 2.4 N stops; after 16 mm the hand is rigid to the arm and the rest of the motion (4 mm, or 30 mm if it is a sneeze or a sit-up) loads arm, elbow and monitor arm. Accelerating the 100 g float to 0.3 m/s over 5 mm costs 0.9 N — the float is fine; the rigid stage is not. Consumer gas-spring arms have a ~2 kg *minimum* load [KNOWN: hardvance, monitorarmguide]: a 0.5 kg module floats up, so Michael will ballast to ~2 kg or crank the joint friction, after which the arm yields at 10–20 N. The §3.1 "actuator stop" condition cannot be met: the closest credible head position is set by the user's neck, and a forehead pad constrains the head only downward. The dead-man cuts motor power; the obstacle is a dead structure. The 1 kg bar load cell is in that path: safe overload ~150 %, so a 20 N push zero-shifts it permanently. Fix: §8 ruling plus a float biased to ≥15 mm up-travel: 15 (float) + 6 (leaves) + 25 (fail-safe lift) = 46 mm of yielding before anything rigid; and a 5 kg cell (still ~0.05 N resolution on the HX711).

---

## 4. What breaks

- **Leaf fatigue.** k = E·w·t³/(4L³) = 0.40 N/mm for 0.3 × 12.7 mm at 35 mm (matches Judge 2). σ = 3Etδ/(2L²): 73 MPa at 1 mm, 147 at 2 mm, **441 at 6 mm, 588 at 8, 735 at 10 mm** [EST]. Feeler stock yields at ~1.2–1.5 GPa; endurance with sheared, unpolished edges ~500–600 MPa [EST]. Scratching (1–2 mm) is infinite-life; stop hits at 8–10 mm are above the endurance limit, so leaf life is counted in stop hits — which the v0 incline and the flinch case generate. Stop at 6 mm, de-burr. A cracked leaf is a 0.3 mm steel edge 30 mm from the scalp inside the hand — another reason for the shell.
- **Printed parallelogram pins.** Link stress at 2 N is nil; the joints fail. An M3 thread in a 623ZZ bore gives 0.1–0.2 mm radial play per pivot, ±0.3 mm at the hand, a clunk at every touchdown; PETG under the screw heads creeps and the play grows per session.
- **Press-on nails at 3× proof.** ABS 0.6 mm thick, 12 mm wide, 4 mm overhang: σ = 6FL/(wt²) = 13 MPa at the 2.4 N cap, **40 MPa at the 7.2 N proof** — ABS yield [EST]. Keep the overhang ≤3 mm (30 MPa, more nail-like anyway) or use nylon/Tortex pick stock.
- **Magnets.** N52 6 × 2 discs chip when the steel disc slams back after a breakaway: NdFeB flakes in the pocket 30 mm from the scalp. Pot flush, inspect after every breakaway.
- **Tendon knots.** Dyneema creeps under cyclic load; 2 mm of growth drifts the lift zero and the tendon starts stealing dead weight (D's own warning). Cleat termination with a CA drop; re-zero at every park via the load cell.
- **XL330 horn under side load.** The horn carries arm + float + cell + hand + slugs (250–350 g) at 80–100 mm ≈ 0.3 N·m of bending; Robotis lists its radial load as "NA" [KNOWN]. An 18 g plastic servo will wobble and wear. Put an idler bearing on the far side of the arm so the horn carries torque only.
- **Monitor-arm creep.** Below its minimum load the arm is held by joint friction, which creeps 1–3 mm per session as the gas spring warms; the float absorbs it, the aim (and the eye margin, §8 line 6) drifts.

---

## 5. Misuse and misalignment

- **Aim 15° off normal.** Roll: outer nails sit 20 × sin 15° = 5.2 mm apart in height → the low nail carries the full 2.0 N (the §3 table at 3 mm already gives 1.5/0/0). Pitch: attack 45° → 30° (glides, plates hair) or 60° ("digs and catches"). v0 has no roll/pitch compliance beyond the leaves. Fix: passive ±10° wrist gimbal with soft TPU centring, or at least a bubble level and a mannequin alignment procedure.
- **Half on bare nape skin.** µ doubles on bare skin: with the v0 incline the bare-skin nails press 1.7–2.4× harder than the nails in hair and the hand tilts into them; with the incline fixed it is a 2× drag asymmetry and a wrist moment. ≤0.3 N per nail there.
- **Head sideways 30 mm mid-stroke.** Leaves are ~100 N/mm in-plane, the paddle is stiff sideways, D's wrist detent yields in the stroke direction only, elbow and arm are rigid. The 12 mm edge is dragged along its own length with R 1.5 corners leading: a scrape, and a strand pinned at a corner sees µN = 0.45 N → pluck; the 3 N hand breakaway does not fire (3 × 0.45 = 1.4 N). Fix: two-axis detent or lateral flexure; load-cell/elbow-current head-motion reflex → lift.
- **Forehead off the dead-man mid-stroke.** Rail off; elbow and lift servos hold (288:1, non-back-drivable); a lowered hand stays at W. The user's own motion is the problem: in the **crown configuration** (hand above the crown, head tilted 20–30° forward), lifting the forehead off the pad is neck extension, which moves the crown up and back — *into* the hand — by ~15–25 mm [EST]. In the occiput configuration the same motion moves the occiput down and forward, away. D's "chin down, slide back" exit was for a yoke; a monitor-arm hand over the crown inverts it. This drives the §8 ruling.
- **Buzz cut vs 8 cm.** Buzz is easiest for hair and *worst* for the incline flaw (bare-scalp µ 0.6–1.0 → N = 1.5–2.4 W). At 8 cm the pile is 10–25 mm (hair-interaction §1.3); v0's ≥25 mm protrusion leaves 0–15 mm where H-4.5 asks pile + 10 = 35 mm. A carrier riding on the pile carries part of W and the nails lose force silently — the load cell cannot tell pile support from skin support. ≥32 mm protrusion, or ≤5 cm hair first.
- **Damp hair.** Hair–hair µ 0.13 → 0.25, wet skin µ > 1 [KNOWN]; the incline gain goes to 2.4–7× and matting rises. Out of scope on the rig label.

---

## 6. Motor stall, runaway, power

- **Firmware hang (current-based position mode):** the XL330 completes its last goal within the ±35° stops and holds; a lowered hand rests at W with the stroke stopped in place — H-5.9's forbidden "stop with a loaded strand". Only the pedal ends it. Relevant fact: OpenRB-150 DYNAMIXEL-port power is switched by an on-board FET that is **off at boot** [KNOWN: Robotis e-manual], so a hardware-watchdog *reset* does drop the bus — credit it as the firmware layer only; the e-stop/pedal/dead-man loop belongs on the VIN terminal, never a GPIO.
- **USB back-feed [VERIFY]:** the OpenRB-150 takes board power from USB (500 mA fuse) or VIN by jumper. With the series loop open and USB connected, the DXL port must meter 0 V; an XL330 runs on USB 5 V and 500 mA is enough to push a hand into a scalp slowly.
- **Runaway into the hard stop:** 0.52 N·m at 80 mm = 6.5 N tangential at the hand. Layers: detent 0.8 N (15 mm), rigid bumper, then the 3 N breakaway, which **drops the hand onto the head** (100 g nails-first from ~50 mm = 0.05 J; harmless on the scalp, glasses in case it slides to the face). Red line 3 (≤2 N per element) holds with three nails and fails with one: breakaway ≤2 N when running 1–2 nails.
- **Unpowered XL330 back-drive:** torque unmeasured (G: 0.02–0.05 N·m [EST]). Gravity on the hand at ±18° is ≈0.05 N·m — the arm may drift to centre, harmless. The lift tendon at 2–3 N on a 12.5 mm horn is 0.025–0.04 N·m — *the same magnitude* — so v0's "power loss → tendon slack → hand at W" is one of two outcomes: a lifted hand may stay lifted or sag over seconds. An indeterminate fail-safe is not a fail-safe.
- **Dead-man chatter:** a 2 N switch under 10–20 N of pad load is fine, but every opening power-cycles the XL330s (Torque Enable → 0); require an explicit re-arm, never auto-resume.

---

## 7. Twenty-minute effects

XL330 at ~0.1 N·m / 0.25 A dissipates ~0.2 W; its 70 °C shutdown goes torque-off, fine once the fail-safe is a lift. HX711 + bar cell drift ≈ 5–10 mN per 20 min — re-tare at every park. Tip wear: ~3,600 strokes × 40 mm = 144 m of sliding per session; PETG/ABS whiten and the radius *grows* (safe direction); loupe check. Sebum and shed hair collect on paddles and in the pass-throughs: H-6.7 audit, tool-free shell. Noise: two plastic-gear XL330s at 300 mm, my estimate 45–55 dBA [EST], plus desk-borne vibration into the forehead pad — rubber-washer the pad bar off the arm clamp. Posture: 20 min at 30–45° neck flexion for the occiput is untested; run it unpowered first.

---

## 8. Red-line audit and fail-safe ruling

| Line | Verdict | Why |
|---|---|---|
| 1 Rotation/open slot within 30 mm | **Ambiguous → pass only with the closed hand** | Horns above the guard; leaves, lugs, float pivots and a slack tendon are in hair reach for 5–8 cm hair (§2) |
| 2 Mechanical constant ≤2.5 N | **Fail as written; pass with a vertical float** | Dead weight is W/(1 − 0.577µ) (§1). The real cap is the leaf stop at 2.4 N, 0.1 N from the line with ±10 % leaf tolerance and ±0.3 mm stop position (±0.12 N): set the stop at 5–6 mm so the measured cap is ≤2.0 N |
| 3 ≤12 N total; ≤2 N tangential | **Fail for head rise; tangential fails with 1 nail** | No stop bounds a head rising into a rigid arm (§3) |
| 4 NC e-stop + hold-to-run in series | Pass [VERIFY] | Loop on VIN; confirm 0 V on the bus with USB connected |
| 5 ≤24 V, no mains, no lithium | Pass | 5 V 4 A brick |
| 6 Nothing anterior to hairline / near ear / above eyes | **Fail — no aim limit** | Elbow has ±35° stops; the monitor arm has none, so a mis-aim reaches the temple or forehead. Reach-stop ring (E) or two indexed aim positions |
| 7 No self-locking drive without a spring cap | Pass with the latch | Elbow is tangential through a 0.8 N detent; lift can only unload; its non-back-drivability is in the safe direction once the fail-safe is a spring lift |
| 8 De-energised = lifted or limp | **Ruling: LIFTED** | "Limp at W" passes the letter and fails the crown configuration (§5); and the state is indeterminate (§6) |
| 9 Tips retained, tough, 3× proof | Pass with 3 mm overhang | ABS press-ons yield at 7.2 N with 4 mm (§4) |
| 10 Head-borne mass / release | N/A → pass | — |
| 11 Edges ≥1 mm, tips ≥0.4 mm | **Ambiguous** | Tip A (0.3 mm) is a per-se violation: strike it for SP1 or amend the line at the Safety Gate. Paddle long edges are R 0.5 and skin-accessible on a buzz cut or a rolled hand; hair doc allows 0.5, safety says 1.0 — reconcile |
| 12 Procedural | — | — |
| 13 Firmware never the sole barrier | Pass | Every S≥3 item has a weight, spring, stop, magnet or wire |

**Fail-safe ruling: LIFTED, mechanically, on loss of the actuator rail.** (1) In the crown configuration the reflexive exit moves the head *into* a limp hand; (2) a stopped stroke leaves any trapped strand loaded (H-5.9); (3) v0's limp state is indeterminate. **Mechanism:** D's electromagnet latch, re-specified — a 5 V holding electromagnet (25 mm, ~2.5 kg hold, ~0.3 A, $6) powered **from the actuator rail downstream of e-stop → pedal → dead-man** holds a latch plate on the float carriage against a 25 mm extension spring pre-tensioned to ≈ W_max + 0.5 N ≈ 2.5 N; the spring's travel ends on the float's upper stop, so it can never add scalp force; any opening of the loop, a dead brick or a blown fuse releases the latch and the hand rises 25 mm in <100 ms. The lift servo then only modulates. ≈1.5 W for 20 min (≈45 °C surface, ≥60 mm from the scalp). Cost $8–12, 2–3 h. Bench test: pull the mannequin's forehead off the pad mid-stroke, film at 240 fps. With the latch the head-rise margin is 46 mm (§3); without it, 21 mm.

---

## 9. Hair checklist, scored by me for v0 as written

| # | Item | Score | Note |
|---|---|---|---|
| 1 | No exposed rotation in zone (G) | 2 | Horns oscillate above the guard |
| 2 | Every zone joint has a method (G) | 1 | TM1 named; leaf clamps, lugs, float pivots, tendon unnamed and in reach for 5–8 cm hair |
| 3 | No changing / 40 µm–3 mm gap within 25 mm (G) | 1 | Collar step at 8–10 mm; closing leaf-stop gaps with hair stood up into them |
| 4 | Lift before every reversal (G) | 2 | Lifted return; user-induced reversals are a §5 reflex item |
| 5 | Rigid group (G) | 2 | One carrier |
| 6 | Radiused blade, drafted root, no re-entrants (G) | 1 | Collar step; paddle-to-block step |
| 7 | Yields ≤0.15 N tangential (G) | 1 | 0.8 N one-axis detent (as every team) |
| 8 | Protrusion ≥25 mm | 1 | 25 mm is the floor for 2–5 cm; 35 needed at 8 cm |
| 9 | Spacing ≥8 mm | 2 | 20 mm |
| 10 | No silicone/TPU sliding surface | 1 | TPU collar in the pile |
| 11 | Breakaway 3–5 N, no tether | 2 | Verify the wrist microswitch wire stays on the float side |
| 12 | Hair-shedding guard | 1 | Flat plate, open window, unshielded hand below |
| 13 | Grain map | 1 | Manual rotation, firmware flag |
| 14 | Dwell limits | 2 | PATTERN SPEC v1 |
| 15 | Snag reflex lift-and-retract | 2 | Detent switch + load cell |
| 16 | Antistatic | 1 | Insulating tips; frame grounded |
| 17 | Tool-free cleaning | 2 | Magnets, snap shell (if built) |
| 18 | Variants stated | 2 | Long and curly out |
| | **Total** | **27/36** | **Below the 28 floor; no gating 0** |

With the closed shell, float and tendon above the guard, and blades bonded to paddles: items 2, 3, 6, 10, 12 → 2, giving **32/36**; 33 with 32 mm protrusion.

---

## 10. WR-1 wand: the N20 eccentric above an open window

F's housing floor has a 60 × 28 mm window (≥10 mm clear around the lift-frame columns); carrier underside 30–46 mm, floor 50 mm; inside, two scotch-yoke slots with 623 bearings and a Ø46 eccentric turning continuously at 0.5–1.6 rev/s. For 2–5 cm hair the window is out of reach. **For 5–8 cm hair, and in wand mode (the user tilts the device so strands hang into the window from the side), it is a three-stage trap:** (1) a strand enters the open window — lawful, >3 mm; (2) it meets the yoke slot, whose free length closes to ~0.1 mm as the bearing reaches each end twice per revolution — a changing gap in the trap band (H-4.9) that clamps and drags; (3) it reaches the eccentric: capstan with µ 0.3–0.5 on printed PETG, e^(2πµ) = 6.6–23× per turn, one turn per 0.6–2 s — the 0.36 N pluck threshold is exceeded within two turns, and the N20 has ~10 N of pin force to deliver it. Red line 1 is satisfied on paper and violated in practice for the upper half of the design basis. Fix before any scalp use: a TPU 95A bellows gaiter sealing the window to the carrier perimeter (the carrier's 40 × 16 mm ellipse is small enough for a two-fold bellows); no brush seals (H-6.2). Rule until fitted: ≤5 cm hair or hair clipped back. The yoke-slot clunk Judge 2 found is a comfort item.

---

## 11. A simpler float that keeps force a true constant

Requirements: N = W independent of µ, position and velocity; friction <0.05 N; zero play; ≥20 mm (preferably 30 mm) travel; takes the drag moment (0.5–1 N at 50–60 mm below the guide) without stick-slip; nothing in hair reach; bought or trivially printed.

| Option | Friction / play [EST] | Drag → N coupling | Build risk | Verdict |
|---|---|---|---|---|
| v0 inclined printed parallelogram, 4 × 623ZZ | 0.05–0.3 N by pivot alignment; ±0.3 mm play | **W/(1 ± 0.577µ)** | Highest-risk printed part (Judge 2, D) | Reject as specified |
| Same, links horizontal (vertical float) | As above | None | Four printed pivots | Only after measuring friction |
| Flexure parallelogram, two 0.5 × 20 × 80 mm polypropylene strips | ~0; zero play; k = 0.015 N/mm (±0.15 N over ±10 mm) | None | Strip Euler load ≈1.9 N: drag must load the strips in tension (hand trailing) | Good second choice |
| igus drylin bushings on an 8 mm rod | µ 0.1–0.2 × 2D bushing reaction ≈ 0.5 N | None | Stick-slip certain | Reject |
| LM8UU | ~0.02 N; 0.1–0.5 mm play | None | Rattle | Marginal |
| **MGN7/9 rail, vertical, carriage down** | Rolling ~0.01–0.03 N; **end seals add 0.1–0.3 N — remove them**; zero play (preloaded) | **None: the carriage takes the moment as a moment** | Bought, $12, two flat plates, 1 h | **Recommended** |
| Tonearm lever, 150 mm, one 623ZZ or 0.1 mm shim-steel flexure pivot, counterweight | 1–3 mN; zero play with the flexure | W/(1 ± µ/3) — relieving with the hand trailing | Low; ±3.8° hand pitch over ±10 mm is harmless | Good alternative |
| Pendulum from the elbow | — | Swings in the stroke plane: it *is* the stroke | — | Not a float |
| Torsion/leaf spring with stop | Zero friction | None | Lowest | ±1.2 N for ±3 mm of head motion — the strap problem the judges rejected; not a constant |

**Recommendation:** MGN9H (or MGN7H) rail, 50–100 mm, bolted vertically to the stem above the guard, seals removed; hand plate, wrist detent and dead-weight post on the carriage; 5 kg bar cell between carriage and hand plate; lift tendon (or a direct lever from the lift horn) and the electromagnet latch acting on the carriage. N is then exactly m·g·cos θ (≤5 % over ±18°) for any friction, hair state or tip material; moving mass 100–150 g (6 % inertia at 2 Hz); no printed tolerance in the force path; every §2 item H5–H9 moves above the guard. Measure friction by tilting the loaded rail until the carriage slides (µ_eff = tan θ; target <3°); if a seal-less carriage still shows >0.05 N, fall back to the tonearm with the hand trailing. Two simplifications follow: the inclined geometry and its "lift up-and-forward" argument disappear, and the hand module becomes carriage → detent plate → palm shell.

---

## 12. Ranked attack table

| # | Attack | Severity | Likelihood | Fix | Cost |
|---|---|---|---|---|---|
| 1 | Inclined float: N = W/(1 − 0.577µ), 1.2–2.4× W, positive feedback on snags; "mechanical constant" false (§1) | Fatal to the premise; major for pain/hair | Certain (statics) | Vertical float on an MGN9 rail, seals removed | $12, 1 h |
| 2 | Limp fail-safe: crown-config startle moves the head into the hand; unpowered state indeterminate (§5, §6, §8) | Fatal (red line 8 in substance) | High | Electromagnet-latched 25 mm spring lift on the actuator rail | $8–12, 2–3 h |
| 3 | Open hand: leaves, lugs, float pivots, slack tendon in reach of 5–8 cm hair; checklist 27/36 (§2, §9) | Major (S3–S4) | Medium at 5–8 cm, low at ≤5 cm | Closed palm shell; float + tendon above the guard; bonded blades, no collar | 30 g PETG, 2 h |
| 4 | Head rise ≥16 mm meets a rigid arm; no actuator-stop condition possible; 1 kg cell destroyed at 20 N (§3) | Major (red line 3) | Medium | #2 + float biased 15 mm up + 5 kg cell | +$3 |
| 5 | 3 mm mismatch → 1.5–1.9 N on one nail; occipital corner loading 0.33–1.0 N/mm (§3) | Major (prick/pain) | High on the occiput | ≤0.3 N per nail on occiput/nape; flat blade variant; ±10° wrist gimbal; leaf stop at 5–6 mm | $5, 2 h |
| 6 | No aim limit on the monitor arm (red line 6) (§8) | Major | Low–medium | Reach-stop ring or indexed aim positions | $2, 1 h |
| 7 | 30 mm sideways head motion, one-axis detent: corner scrape, pluck at 0.45 N (§5) | Major | Medium | Two-axis detent; head-motion reflex | $3, 2 h |
| 8 | WR-1 window: yoke slot + eccentric reachable by 5–8 cm hair / wand tilt (§10) | Major | Medium (wand) | TPU gaiter; ≤5 cm hair until fitted | $4, 2 h |
| 9 | USB back-feed of the DXL bus; dead-man chatter power-cycles servos (§6) | Major if real | Unknown [VERIFY] | Meter the bus; explicit re-arm | 0 |
| 10 | Leaf stop hits at 8–10 mm = 590–735 MPa, above endurance (§4) | Minor–major (steel fragment) | Medium | Stop at 6 mm, de-burr, inspect | 0 |
| 11 | ABS press-ons yield at the 7.2 N proof with 4 mm overhang (§4) | Minor | High at proof | 3 mm overhang or pick stock | 0 |
| 12 | XL330 horn under 0.3 N·m of cantilever bending, radial rating "NA" (§4) | Minor–major (wear) | High over sessions | Idler bearing on the arm | $1, 1 h |
| 13 | 25 mm protrusion vs 25 mm pile at 8 cm: nails lose force invisibly (§5) | Minor (sensation) | Medium | 32 mm, or ≤5 cm hair first | 0 |
| 14 | Detent does not re-seat; tendon knot creep; arm minimum load/creep; pad-borne vibration (§2, §4, §7) | Minor | High | 0.2 N return spring; cleat + re-zero; ballast to the arm minimum; isolate the pad bar | <$10 |
| 15 | Tip A 0.3 mm is a per-se red-line 11 violation; paddle edges R 0.5 skin-accessible (§8) | Minor (procedural) | Certain on paper | Safety Gate strikes tip A for SP1 or amends line 11 | 0 |

**What survives:** the frame mount, the elbow stroke axis, the dead-weight principle, the lift-can-only-unload rule, the three-leaf hand with staggered preloads, the series e-stop loop, and WR-1 as the control instrument. What does not: the specific float, the limp fail-safe and the open hand — fixed by a $12 rail, a $10 electromagnet and a printed shell.
