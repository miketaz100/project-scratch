# PROJECT SCRATCH — Mechanism Team C: Compliant / Flexure / Elastic-Energy Mechanisms and Soft Actuation

**Team:** C (firewalled). **Date:** 2026-10-01. **Inputs read:** BRIEF, scratch-model v1, hair-interaction, safety-requirements v1, tip-interface (SP1-TM1 adopted), component-landscape. No other team file and no prior-art file was read.

**Seed family:** one or a few actuators driving printed/steel flexure fingers, living hinges, leaf-spring nail carriers, bistable snap elements, tendon-pulled flexures, pneumatic bending fingers, "stroke on tension, lift on release" shapes, and arrays where one sweep yields many independently compliant nail contacts.

**Selected concept:** **LEAFHAND** — a head-worn, motor-free compliant hand (3 leaf-sprung nail fingers on a rocking knuckle bar) driven by two Bowden tendons from a desk box, with elastic return. Stroke, soft landing and lift-off come from the geometry of a rocking arc; per-nail compliance comes from spring-steel leaves; the force ceiling is a mechanical constant (leaf stiffness × leaf stop, plus a lift hard stop). Estimated cost ≈ $300 build (+$60 test gear). 3 contacts (4th optional), one 40 × 35 mm patch per mounting position (crown / rear-crown / occiput), 2 DOF.

---

## 0. Answers to the family's key questions (summary; derivations in §2)

| Question | Answer |
|---|---|
| Can flexures give 0.1–0.5 N/mm and ≥ 5 mm travel per nail with lift-off before reversal? | **Yes.** A 1095 spring-steel strip 0.4 × 12.7 mm at 40–60 mm free length is 0.19–0.63 N/mm (set by sliding the clamp), 7–8 mm travel at ≤ 400 MPa. Lift-off is not from the leaf; it comes from (a) the rocking-arc geometry (nail exits the scalp 12 mm before reversal, passively) and (b) a 15 mm wrist lift on the return. |
| Can printed TPU/PETG flexures survive thousands of cycles? | **TPU 95A hinge straps at 1–3 % bending strain: yes (10⁵–10⁶ cycles expected).** PETG leaves at 9–25 MPa cyclic: uncertain (creep over a 20-min session, probable fatigue at 10³–10⁴ cycles) — used only as the zero-cost fallback; steel leaves are the baseline. |
| Does soft actuation give naturally bounded force? | **Only partly.** A tendon is position-driven; it bounds nothing by itself (and a series spring in the tendon is useless because it is referred to the tip by (r/L)² ≈ 1/40). Force is bounded by the leaf stop and the lift hard stop — mechanical constants downstream of the tendon. What tendons *do* give for free: they can only pull, so a runaway pulls the hand to its arc end (nails in the air), and spring return on power loss = lifted hand. Pneumatics bound force by pressure × area but cost speed, noise and leaks (§1.4). |

---

## 1. Concepts generated

### C1 — LEAFHAND: tendon-rocked compliant hand (SELECTED)

A rigid "knuckle bar" carries three horizontal spring-steel leaves (20 mm pitch) that trail behind it; each leaf ends in a drafted printed "stalk" (distal finger) that hangs 46 mm down to an SP1-TM1 pocket and a nail tip. The bar is part of a rocker that pivots on a pair of TPU living-hinge straps 62 mm above the scalp; the nail edges sit 66 mm from the pivot, so at mid-stroke they interfere with the scalp by 4 mm (leaf bends, ~1.2 N) and at ±30° of rock they are 12 mm above it. One Bowden tendon rocks the hand (pull stroke); an extension spring returns it. A second tendon lowers the whole hand against a lift spring (wrist lift, 15 mm; also the continuous force modulator); on power loss both springs lift the nails clear. Servos live in a desk box; nothing electrical is on the head.

```
 side view, stroke runs left→right (pull)                 to desk box
                                                           ROCK tendon ──────►
     bridge (on ratchet suspension) ════════════════════╗  LIFT tendon ──────►
                      LIFT hinge (TPU) ▪──── forearm ───╫──┐ lift stop screw
                                        │  ROCK hinge (TPU)│
                                        ▪ P (62 mm up)     │
                                       / rocker bracket     │
   leaf (steel, 50 mm) ◄──────────────▐ knuckle bar/palm shell (52 mm up)
   ┬ knuckle + magnet detent
   │ stalk (drafted, 46 mm)
   ╲ TM1 pocket, nail at 45°
 ~~~~~~~~~~~~~~~~~~~~~~~~ hair canopy ~~~~~~~~~~~~~~~~~~~~
 ======================== scalp ==========================
  nail path: arc about P, radius 66 mm; chord on scalp ≈ 33 mm, clearance 12 mm at ends
```

### C2 — Tendon-curl flexure fingers (soft gripper inverted)

Three printed fingers (PETG phalanges joined by TPU living hinges, or one-piece TPU 95A PneuNet-style solid finger), each with a braided-PE tendon along its palmar side pulled by its own frame-mounted servo; elastic straightening on release. The curling finger tip traces a finger-like arc, and with the base held at a fixed standoff the tip touches the scalp only in the middle of the curl, giving soft landing and lift-off for free. Rejected because: (1) a tendon-driven joint is kinematically locked in the curl direction, so contact force is set by tendon tension, i.e., by servo torque, unless a separate normal compliance is added (at which point the finger is just a lever — C1 does this with a simpler rigid rocker); (2) with one tendon and graded hinges, elastic return un-curls the proximal joint *first* and lifts the nail *last* (the moment on every hinge scales with the same tension, so unloading retraces loading), which is the opposite of the "lift on release" we wanted; (3) tip attack angle flips sign on the return stroke (a 45° plate dragged backwards scoops hair under itself, violating DR2), so a lifted return is still needed; (4) per-finger independent curl is forbidden inside the canopy anyway (H-5.6). What survives from C2 into C1: trailing geometry, the arc landing, tendon + spring return.

```
   tendon ──►(servo)        base pivot ▪ (fixed standoff h)
                  ╭──hinge──╮
     tendon ══════╪═════════╪══╗ nail
                  ╰─────────╯  ▼        tip arc: touches scalp only mid-curl
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ scalp
```

### C3 — Bistable snap-through "flick rake"

A pre-buckled PETG beam (two stable states) carries the nail bar; a servo or cam slowly pushes it past its snap point and the beam snaps, flicking the nails 20–30 mm across the scalp in ~50–100 ms, then a slow reset to the other state. Attractive for the family (elastic energy produces the stroke; the actuator is slow and cheap) but rejected: snap velocity is set by stored energy, not by control (200–500 mm/s, over the 200 mm/s hair cap H-5.4 and the 20 cm/s scratch band); in-contact tangential acceleration is tens of m/s² against the ≤ 2 m/s² rule, which turns any snagged strand into a pluck; stroke/speed/force are fixed by the print, so irregularity (sensation variable #1) is unavailable. The snap idea is kept at the tip level only, as the 0.4–0.8 N magnetic knuckle detent that lets a finger collapse backward on a snag (§2.4).

```
   push ▼                    snap!
  ╭──────╮        ──►       ╰──────╯   nail bar rides the beam midpoint
  nail▼                           ▼nail   30 mm flick, then slow reset
```

### C4 — Pneumatic bellows / balloon fingers

Printed TPU bellows (or latex balloons in a printed sleeve) curl a finger when pressurised by a cheap aquarium diaphragm pump (≈ 10–20 kPa) through 12 V solenoid valves; vent to straighten. Force is bounded by pressure × area (20 kPa × 300 mm² = 6 N on the bellows, ~1 N at the nail) — the only concept in the family where the bound is in the actuator itself. Rejected for SP1: pump noise (diaphragm buzz ~45–55 dB, must be boxed), leak-prone TPU bellows that are hard to print without a well-tuned printer, 0.3–0.5 s fill/vent times that limit cycles to ~1 Hz with poor velocity shaping, and the same arc/attack-angle issue as C2. Noted as the best candidate for the **LIFT axis** in a later version (pressure = down, spring = up, vent = fail-safe lift).

```
  pump ─valve─►[ bellows ]═══finger═══▶ nail      vent → spring straightens → lift
```

### C5 — Parallelogram comb-sweep array

One servo translates a curved bar of 4–5 leaf-sprung nails on a TPU-hinged parallelogram four-bar (links 50 mm). The coupler stays level (constant attack angle) and rises 50·(1−cos θ) at the ends of travel, so a 3 mm centre interference gives a ~34 mm chord with passive lift-off — the same trick as C1 with two link pairs instead of one rocker. Not selected: four hinges instead of two, more wobble, no advantage over C1 at this stroke length. Worth revisiting if the 60 mm sweep (P2) proves important, because a parallelogram scales to longer links more gracefully than a rocker.

### W1 — Wildcard (outside the family): hard-disk voice-coil fingers

Two or three actuator arms salvaged from dead 3.5-inch hard drives, frame-mounted over a seated head. Each arm is a direct-drive voice coil on a precision bearing: silent, cog-free, back-drivable, and torque ∝ current with a hardware current limit (a series resistor or DRV8871 ILIM) making the force ceiling an electrical constant (≈ 0.05–0.2 N·m → 1–3 N at a 60 mm arm). Swing ±15–20° gives a 30–40 mm arc stroke; each arm carries a TM1 pocket on a short leaf. Weaknesses: no lift DOF (needs a second axis or symmetric wedge tips), the magnet yoke is a steel/magnet block that must be shrouded from hair, an exposed bearing pivot ~60 mm from the scalp (boot it), free but un-specified parts, and a stationary frame means the head can wander ±20 mm. Worth one afternoon as a "what does direct-drive force control feel like" probe; not buildable to a spec sheet, so not the SP1 candidate.

```
   [voice-coil yoke]──bearing──arm═══════leaf═══▼nail   current limit = force cap
```

---

## 2. LEAFHAND — concept-level engineering design

### 2a. Working principle and why it will feel like fingernails

Scratch-model §1.2 says the two signatures unique to scratching are a stiff narrow edge that reaches the skin through hair, and hair deflected within 2–5 mm of the root. LEAFHAND reproduces both because it places real nail-like blades (TM1 tips A–G; press-on nails on day one) on stalks that protrude 46 mm below any other surface, so the edge is the only thing in the pile; everything above is either a 6–14 mm drafted cone or 50 mm up.

The *mount* behind the edge is the part the tip document says matters most (§1.3: "the compliance comes from behind it"). A horizontal steel leaf of 0.2–0.6 N/mm with 7 mm travel is the pulp-and-knuckle spring of a relaxed finger (scratch-model 3.12: 0.1–1 N/mm). Because the leaf is a cantilever, the nail also swings ~5 mm along the stroke for every 3 mm it is pushed up (cantilever end-slope × stalk length), which is the same arc coupling a curling finger has; the nail does not "stamp", it rides.

The stroke is an arc about a pivot above the scalp (§2c). The consequence is a force profile that starts at zero, rises to the set peak over the first ~8 mm, holds within 70–100 % for the central ~20 mm, and falls to zero over the last ~8 mm, after which the nail is in the air before the direction reverses. That is scratch-model 3.10 (force dip of 30–70 % at reversal) and hair rule DR4/H-5.2 (unload and lift before reversal), produced by geometry rather than by control, so it cannot be mis-programmed.

Three nails at 20 mm pitch on a bar curved to the scalp radius, with the middle stalk 2 mm longer than the outer two, land 20–40 ms apart and carry 20–50 % different force depending on local curvature — the asynchrony of scratch-model §4.2 arises passively. Irregularity in the time domain is firmware: per-stroke jitter of speed, lift depth (force), pause, and amplitude.

Against the §1.2 table: contact element = hard edge R 0.3 mm, 4–6 mm line; force 0.3–1.2 N per contact; pressure 100–200 kPa; scalp translation < 1 mm (the drag of 0.5 N bends the leaf in-plane by 0.004 mm, so the skin slips under the edge); 33 mm sliding per cycle; 60–150 mm/s; 1–1.5 Hz. Every entry lands in the SCRATCH column.

Why it is not a massager: no pad, no normal-direction oscillation, no skin-moving kneading load (total < 7 N even at the cap), and — because the hand is motor-free — no vibration at the scalp.

### 2b. Architecture

- **Mounting:** head-worn on a 4-point hard-hat ratchet suspension (no shell) plus a nape strap, carrying a printed PETG ring with three bridge positions (crown / rear-crown / occiput). The hand references its standoff to the skull through the suspension, which is what makes the geometric force cap a constant; a stationary frame would let the head wander ±20 mm, more than the 7 mm leaf travel. Zero electrical parts on the head; two Bowden housings run to a desk box 1 m behind the user.
- **Coverage:** one patch of 40 mm (across, 3 nails) × 33 mm (stroke, single-DOF) to 55 mm (coordinated 2-DOF, §2c) per mounting position; region change is manual (re-seat the bridge, rotate the ring 90° for across-the-lie strokes). Partial coverage is accepted per BRIEF §15.
- **Contacts:** 3 at 20 mm pitch (span 40 mm); 4th finger position printed in the bar for a 60 mm span experiment. Any finger pulls out with one thumb screw for 1- and 2-contact experiments.
- **DOF:** 2 actuated (ROCK ±30°, LIFT 0–15 mm) + 3 passive leaf compliances + 3 passive knuckle breakaways. Fingers move as one rigid group inside the canopy (H-5.6).
- **Head-borne mass (estimate):** suspension + nape strap 90 g, ring + bridge 60 g, forearm 30 g, rocker + bar 35 g, 3 fingers 27 g, springs/levers/housing ends 25 g, cowl 15 g → **≈ 280 g** (limit 500 g).

### 2c. Kinematics with numbers

Geometry (side view, stroke direction = x, scalp normal = z): ROCK pivot P at H = 62 mm above the local scalp (hinge-strap mid-length); nail edge at radius L_f = 66 mm from P; knuckle bar 10 mm below and 45 mm ahead (+x) of P, underside 50 mm above the scalp; leaves run −x 50 mm from the bar at 52 mm height; stalks hang 46 mm; TM1 pocket inclined 45° in the stroke plane, free edge leading in +x.

- **Interference and force:** at mid-stroke the nail would be 4 mm below the scalp plane; the leaf absorbs it → 1.2–1.3 N at 0.33 N/mm. On a convex scalp of R = 80 mm the interference is i(x) = √(66² − x²) − 62 − (80 − √(80² − x²)): 4.0 mm at x = 0, 2.3 at ±10, 0.9 at ±15, zero at ±16.5 → **contact chord ≈ 33 mm**, force ≥ 70 % of peak over the central 20 mm. On R = 90 (crown) the chord is 35 mm; on R = 65 (occipital bun) 29 mm. Lowering the hand 2 mm (lift axis) raises peak force by 0.65 N and lengthens the chord to ~42 mm; raising it 2 mm gives 0.65 N peak and a 22 mm chord.
- **Clearance at reversal:** at rock = ±30° the nail is 66·cos30 = 57.2 mm below P, i.e. 4.8 mm above the flat plane, and the R = 80 scalp has dropped 7.1 mm at x = 33 → **≈ 12 mm clearance with zero force** (H-5.2 minimum is 5 mm at zero force; preferred 15–25 mm). The LIFT axis adds 15 mm during the return → 27 mm.
- **Stroke rate and velocity:** servo-limited. ROCK tendon lever 20 mm → 21 mm of line for 60°; spool radius 12 mm → 100° of servo travel; STS3215 at ≈ 0.16–0.2 s/60° covers it in 0.27–0.33 s minimum. Operating pull 0.5–0.9 s per 60° (uniform angular rate) gives 70–130 mm/s on the chord; return (spring-driven, servo paying out) 0.3–0.4 s; lift/lower overlap the air phases. **Cycle 1.0–1.5 Hz, one scalp pass per cycle.** This is slower than a vigorous two-way human rake (2 Hz, four passes/s); the symmetric-wedge tip experiment (§2g) restores two passes per cycle.
- **Velocity profile:** firmware trapezoid on the ROCK servo with ≤ 2 m/s² in-contact tangential acceleration (at 66 mm radius that is ≤ 30 rad/s²; the servo's own acceleration register is set below this). Landing is at ≤ 30° to the skin because the nail enters along the arc tangent (H-5.3), and it exits still moving forward at full speed.
- **Lift-off mechanism (H-5.2, mandatory):** passive (arc geometry) + active (LIFT tendon raises the forearm 15 mm, 8.6° about the lift hinge, during every return) + fail-safe (both return springs park the hand lifted: rocker at −30° and forearm up).
- **Irregularity:** per stroke, sampled in firmware per PATTERN SPEC v1 — speed U(70, 130 mm/s) ±20 %; lift depth N(set, 30 %) clamped to the hard stop (→ force ±30 %, chord ±15 %); inter-stroke pause 0–2 s with p = 0.3; rock amplitude 24–30° (changes clearance, not the chord); occasional "slow mode" strokes at 20–50 mm/s with 1 mm lift (≤ 0.3 N, CT channel); bouts of 4–20 strokes then a 1–3 s lifted pause. Per-finger phase and force spread are passive (stalk-length stagger 44/46/44 mm; curvature). Direction wander ±20° is NOT available without re-mounting — an honest gap, see §2j.
- **Coordinated 2-DOF mode:** the LIFT servo tracks the scalp drop (lowers 0–3 mm as |x| grows) so the chord extends to ~55 mm within the ±30° reach and the force profile becomes flat-topped; also allows the force to be shaped arbitrarily along the stroke. Single-DOF arc mode (LIFT parked) is the control condition.
- **Region changes:** manual, between bouts; firmware has three stored "region profiles" (occiput: 1.0× force; crown: 0.8×; temples/nape: out of scope for SP1).

### 2d. Force path and caps

Chain: nail → TM1 tang (N52 6×2 magnet, 4–8 N axial breakaway) → stalk (rigid, PETG) → knuckle (2 mm pin in a clevis, D41 magnet detent, tangential breakaway 0.4–0.8 N at the nail) → leaf (0.19–0.63 N/mm, 7 mm stop with TPU bumper) → root clamp → curved knuckle bar → rocker bracket → ROCK hinge straps → forearm → LIFT hinge straps + lift stop screw → bridge → ring → ratchet headband + nape strap → skull.

- **Normal force ceiling (mechanical constant):** F_max = preload + k·x_max = 0 + 0.33 N/mm × 7 mm = **2.3 N per nail** (red line 2: ≤ 2.5 N). With the stiffest leaf setting (0.63 N/mm) the stop is moved to 4 mm (2.5 N). Total over 3 nails ≤ 6.9 N (≤ 12 N).
- **Actuator-stop check (safety §3.1 condition 2):** the lowest point the nail can reach is geometric (L_f below P) and P's height is bounded by the LIFT hard stop (M4 screw, 0.7 mm/turn). Stack at the stop: nominal 4 mm + curvature (−2/+1.5) + suspension slop (±3) → worst 8.5 mm, 1.5 mm past the leaf stop. In that corner the path goes rigid and the backstop is the headgear itself: the suspension is not anchored against upward push, so the whole hand lifts off the head at (headgear weight 2.8 N + headband/nape-strap grip, est. 3–6 N) — a dead-weight-like cap to be **measured** on the mannequin (§2j, R2). The ROCK tendon can never drive the nail lower than the arc bottom at any torque.
- **Tangential yield/breakaway:** scratch drag 0.3–0.6 N at μ 0.3–0.5 passes through the knuckle detent; the D41 magnet (5.3 N rated, ~4 N real) at 4 mm offset from the pin holds 16–21 N·mm → breakaway at 46 mm = **0.35–0.46 N; shimmed to 0.6–0.8 N** for the first tests. Beyond it the stalk swings back up to 30° (nail rises 6 mm, releasing a trapped strand) and re-latches when unloaded. Hard tangential cap if the detent is bottomed: the stalk's 30° stop plus the leaf's in-plane stiffness — the tendon stalls at the servo's current limit first (firmware), and the TM1 axial breakaway (4–8 N) is the last mechanical layer. No single element can see > 2 N tangential without something yielding (red line 3).
- **Compliance per contact and across curvature:** each leaf is independent, 7 mm travel; the bar is printed curved (outer roots tilted 14° to an R = 80 mm sphere) so the three nails see 4.0 / 4.0 / 4.0 mm nominal on R = 80 and 4 / 3.3 / 3.3 on R = 90, 4 / 4.8 / 4.8 on R = 65 — all inside travel.

### 2e. Hair safety

**Every joint, gap or rotation within 30 mm of the scalp:** none. Items inside the zone: three stalks (drafted ≥ 10°, 6 mm at the tip to 14 mm at 46 mm, no features), three TM1 pockets (mouth at 12 mm above the edge — a 0.15 mm/side push-fit seam, in the 40 µm–3 mm band; **sealed with a 10 mm silicone/TPU band rolled over the pocket mouth after each tip change**), and the nail blades. Hair-reach volume for the design basis (8 cm hair → 90 mm): leaves (sleeved end-to-end in 3:1 heat-shrink, no burrs, no edges), leaf-root grommets (TPU 95A, interference-fit, < 40 µm), knuckle clevis (pin ends capped, D41 recessed, 52 mm up; clevis sides filleted), knuckle bar/palm shell (smooth, R ≥ 2 mm edges, drafted underside), rocker bracket, TPU hinge straps (no gap, no rotation surface), and — above the forearm — levers, springs, tendons and housing ends, all under a printed **cowl** so a draped strand sees a smooth lid.

| # | Item | Score | Note |
|---|---|---|---|
| 1 | No rotating surface in zone | 2 | nothing rotates anywhere on the head; hinges are straps |
| 2 | Joint exclusion named | 2 | straps (no joint), pin knuckle at 52 mm capped, all drive above the cowl |
| 3 | No changing / 40 µm–3 mm gap within 25 mm | 1 | TM1 pocket seam at 12 mm is sleeved; grommets sealed; knuckle pin gap is 52 mm up but inside long-hair reach → capped |
| 4 | Lift before every reversal | 2 | geometric 12 mm + active 15 mm + spring fail-safe |
| 5 | Rigid group in canopy | 2 | 3 nails on one bar; knuckle collapse only on snag (lifts) |
| 6 | Radiused blade, drafted root, no re-entrant | 2 | TM1 tips; stalk is a drafted cone |
| 7 | Mount yields ≤ 0.15 N tangential on snag | 1 | detent yields at 0.6–0.8 N total (≈ 0.2–0.4 N above scratch drag); set by shim and test |
| 8 | Protrusion ≥ 25 mm | 2 | 46 mm below the leaf, 50 mm below the bar |
| 9 | Spacing ≥ 8 mm | 2 | 20 mm pitch, 8+ mm edge-to-edge |
| 10 | Low-friction polished sliding surfaces | 2 | tips per TM1; stalk polished PETG (sanded 400→1000) |
| 11 | Breakaway 3–5 N, no tether | 1 | tips 4–8 N (TM1); whole-hand breakaway deliberately omitted on a head-worn rig (a detached hand lands on the face); fingers collapse rather than detach |
| 12 | Hair-shedding guard | 2 | palm shell = bar underside; grommeted pass-throughs; cowl above |
| 13 | With-grain bias / grain map | 1 | direction fixed per mounting; firmware stores region profiles; against-lie chord 33 mm vs the 25 mm rule → lower lift to 3 mm (28 mm) when mounted against-lie |
| 14 | Dwell/repetition limits | 2 | firmware: ≤ 8 strokes per bout then lifted pause; no loaded stationary contact |
| 15 | Snag reflex = lift and retract | 2 | ROCK current spike → LIFT servo up 15 mm within 100 ms, ROCK holds (never reverses) |
| 16 | Antistatic | 1 | nylon/POM tips, steel leaves; no ground on the head; test at > 40 % RH |
| 17 | Tool-free removal for cleaning | 2 | fingers out by thumb screw; tips by magnet |
| 18 | Hair variants stated | 2 | buzz/short/medium straight–wavy, fine–coarse: in scope; long (> 15 cm) and curly/coily: **out of scope** |
| | **Total** | **31 / 36** | all gating items ≥ 1; items 3 and 7 are the ones to retire on the wig head |

### 2f. Safety (13 red lines)

1. No exposed rotation/open slot within 30 mm: **pass** (no rotation on the head at all). 2. Normal force bounded by a mechanical constant ≤ 2.5 N: **pass** (2.3 N leaf cap; headgear lift-off as backstop, to be measured). 3. ≤ 12 N total, ≤ 2 N tangential before yield: **pass** (6.9 N; 0.6–0.8 N knuckle). 4. NC e-stop in series with motor power + hold-to-run: **pass** (22 mm mushroom in the 12 V rail inside the desk box, cable to a hand button; foot pedal hold-to-run for staged tests). 5. No mains in the rig, ≤ 24 V, no lithium: **pass** (Mean Well GST60A12, 12 V; nothing electrical on the head). 6. No moving element anterior to the hairline / near ears / above eyes unguarded: **pass** — mounting positions are crown and rear only; the rocker's ±30° hard stops keep the nails within the bridge footprint. 7. No self-locking drive in the force path without a downstream spring cap and spring-return lift: **pass** (tendons can only pull; leaf cap downstream; springs lift). 8. De-energised = lifted/limp: **pass** (both springs lift; measured 27 mm clearance). 9. No push-fit-only or brittle tips: **pass** (TM1 magnet + pocket; PETG/nylon/POM; proof-load 3×). 10. One-hand release ≤ 3 s, no chin strap, ≤ 500 g: **pass** (lift the ratchet headgear off; the nape strap is elastic and slides over the occiput; Bowden ends are push-fit ferrules and the lines end in slip toggles that release at ~30 N — the box also slides). 11. No skin-accessible edge < 1 mm (tips < 0.4 mm): **pass** by design, verified by tape test; leaves are heat-shrunk. 12. Checklist, wig test, glasses, ≤ 5 min first session: procedural, adopted. 13. No firmware-only barrier for S ≥ 3: **pass** — the firmware snag reflex and current limit are layers 3 and 2 behind the geometry and the leaf/detent/stop constants.

Hazards specific to this design: H13 (headgear pressure) — the hand's 2.8 N plus nail reaction rests on the headband; reposition every 20 min. H23 (device slipping) — the nape strap and the suspension's crown straps; tether not needed because the head is the mount. Thermal: nothing warm on the head. Noise: servos 1 m away in a closed box; the head carries springs and leaves only.

### 2g. Adjustability

| Variable | How | Type |
|---|---|---|
| Force (peak per nail) | LIFT hard-stop screw (0.7 mm/turn → 0.23 N/turn) sets the ceiling; LIFT servo sets per-stroke depth below it; leaf clamp position sets N/mm | knob + firmware + 30 s mechanical |
| Compliance | slide the leaf in its root clamp: free length 40–60 mm → 0.63–0.19 N/mm; swap 0.5 mm strip for ×2 | mechanical, 1 min |
| Speed | ROCK servo velocity/accel registers | firmware |
| Stroke on scalp | arc mode: 22–42 mm via lift depth; 2-DOF mode: up to 55 mm; 80 mm rocker bracket (reprint) for 50 mm single-DOF | firmware / reprint |
| Cycle rate | firmware, 0.5–1.5 Hz; 2–3 passes/s with symmetric tips | firmware |
| Attack angle | TM1 holder printed into the stalk at 35/45/55° (three stalk prints); 0° stalk for the symmetric wedge | reprint, 10 s swap |
| Contacts | 1–4 by pulling fingers; two bar prints (20 mm and 25 mm pitch) | thumb screw / reprint |
| Direction vs lie | rotate the ring / flip the bridge (pull up vs pull down the occiput; across on the crown) | manual |
| Pattern | PATTERN SPEC v1 parameters, bout lengths, pauses, slow mode, "fully periodic" control | firmware |
| **Experiment tips** | symmetric-wedge tip W (90° included, R 0.3 edge, 0° stalk) allows bidirectional strokes without lift → tests whether two-way raking beats pull-only | reprint/file |

### 2h. Components and BOM

| Item | Qty | Unit | Ext. | Source (per component-landscape) |
|---|---|---|---|---|
| Feetech STS3215 12 V (ROCK, LIFT) | 2 | $24 | $48 | Seeed/Amazon |
| Waveshare Servo Driver with ESP32 | 1 | $16 | $16 | Waveshare |
| Mean Well GST60A12-P1J 12 V 5 A | 1 | $19 | $19 | Mouser/DigiKey |
| 22 mm NC mushroom e-stop + box | 1 | $15 | $15 | Amazon |
| Momentary foot pedal (hold-to-run) | 1 | $8 | $8 | Amazon |
| INA219, rocker switch, fuse holder + fuses | 1 set | — | $20 | Adafruit/Amazon |
| 10 kΩ pots ×2, SSD1306 OLED, wire/JST kit | 1 set | — | $30 | Amazon |
| Hard-hat 4-pt ratchet suspension + nape strap | 1 | $20 | $20 | Amazon |
| Bike shift-cable kit (2 × 1.2 m lined housing) + PTFE 4×2 liner | 1 | $17 | $17 | bike shop/Amazon |
| Braided PE line 50 lb | 1 | $9 | $9 | Amazon |
| Extension + compression spring assortment | 1 | $12 | $12 | Amazon |
| 1095 spring-steel strip 0.016" × ½" × 12" (McMaster 9075K41-class, ~unverified) | 1 | $10 | $10 | McMaster |
| 3:1 heat-shrink, silicone bands | 1 | $8 | $8 | Amazon |
| Magnets: D41 ×10, D61 ×4, N52 6×2 ×10; M4/M3 steel washers | 1 set | — | $12 | K&J/Amazon |
| M3 heat-set inserts (100), M3/M4 screw assortment, thumb screws | 1 set | — | $25 | Amazon |
| 2 mm steel pins (knuckles), 4 mm pin spares | 1 | $5 | $5 | Amazon |
| Press-on nails (set), Dunlop Tortex 1.14 + nylon .88 picks | 1 | $11 | $11 | drugstore/music shop |
| Printed parts: ≈ 260 g PETG + 35 g TPU 95A (JLC3DP, one order) | 1 | — | $55 | JLC3DP (or $25 library PETG + TPU from service) |
| **Build subtotal** | | | **≈ $340** | |
| Test gear: real-hair mannequin head $32, kitchen scale $12, luggage scale $12, FSR 402 $7 | | | $63 | |
| **Total** | | | **≈ $400** (tools excluded) | |

Substitutes: XL330-M077 ×2 + OpenRB-150 + 5 V 4 A (+$40, faster, quieter); MG90S/DS3218 hobby servos (−$30; acceptable here because all compliance and caps are downstream and the servos are off-head, but no current readback → snag detection lost).

**Printed parts (PETG unless noted, 0.4 mm nozzle, 4 perimeters):**

| Part | Approx. size | Qty | Notes |
|---|---|---|---|
| Suspension ring with 4 clip tabs and 3 bridge seats | Ø 170–190 × 20 mm, 8 mm section | 1 | print flat; tabs match the suspension's clip slots |
| Bridge (arch) | 180 × 40 × 25 mm | 1 | carries lift-hinge clamp, lift stop boss, housing ferrules |
| Forearm frame (window for ROCK lever) | 140 × 60 × 8 mm | 1 | ROCK hinge clamp, spring posts, lift lever |
| Rocker bracket + lever (one piece) | 70 × 60 × 20 mm | 1 | ±30° stop lugs; D61 seats optional |
| Knuckle bar / palm shell, curved R 80, 3 (+1) root seats | 70 × 28 × 22 mm | 2 (20 & 25 mm pitch) | underside smooth, R 2 edges |
| Leaf root clamps + thumb-screw plates | 14 × 12 × 12 mm | 4 | |
| Knuckle clevis (prints on the leaf-tip clamp) | 14 × 10 × 12 mm | 4 | 2 mm pin bore, D41 pocket |
| Stalk with TM1 pocket, 45° | 46 mm, Ø 6→14 mm | 4 + variants 35°/55°/0° | print pocket-up; sand 400→1000 |
| Leaf stop bumpers | 10 × 8 × 6 mm | 4 | TPU 95A |
| Hinge straps (ROCK ×2, LIFT ×2) | 25 × 2 × 40 mm (20/15 mm free) | 4 + spares | TPU 95A, print flat |
| Leaf grommets | 14 × 3 × 6 mm with 12.8 × 0.35 slit | 4 | TPU 95A |
| Cowl | 150 × 70 × 30 mm shell | 1 | 1.2 mm wall |
| Tendon spools (r = 12 mm) + servo horn adapters | Ø 24 × 10 mm | 2 | |
| Desk box with servo bays, e-stop, ferrule block | 160 × 100 × 60 mm | 1 | |
| Hand wand (TM1 holder with leaf, pen handle) for T0 tests | 150 mm | 1 | tip-interface §9 |

### 2i. Buildability in an apartment

**Tools:** Pinecil iron + heat-set tips, calipers, hex keys, needle files, tin snips or Dremel cut-off wheel (for the steel strip), 400/1000 sandpaper, heat gun or lighter (heat-shrink), CA glue, multimeter, kitchen and luggage scales. No lathe, no mill.

**Steps (≈ 24–32 h over two weeks, printing lead time excluded):**
1. Print the wand; make 6 tips (press-on nails A, pick C/F, ball H); run tip-interface T0–T2 (3 h). This de-risks the whole project before any mechanism exists.
2. Cut three 65 mm leaves from the strip, radius all corners with a file, deburr, heat-shrink (1 h). Measure k on the kitchen scale with the leaf clamped at 50 mm (target 0.33 N/mm ± 20 %).
3. Assemble fingers: root clamp, leaf, knuckle clevis with pin and D41, stalk, washer in stalk, TM1 magnet in pocket; proof-load each tip 3× (2 h).
4. Fit the ring to the suspension; mount the bridge; clamp the LIFT straps and forearm; clamp the ROCK straps and rocker; fit the knuckle bar with fingers; fit stops and springs (3 h).
5. Desk box: servos, spools, ferrule block, e-stop, pedal, PSU, ESP32 board, INA219; route housings; thread lines; tension return springs (4 h).
6. Firmware: Feetech bus, two position loops, PATTERN SPEC sampler, limits table, snag reflex, watchdog, OLED/pots (6–8 h; LeRobot/Waveshare examples exist).
7. Bench: force map on the kitchen scale under each nail vs lift screw; hysteresis loop (load cell at the lever); clearance by ruler; 20-min run with IR check (2 h). Then hair-interaction §7 wig-head sequence (3 h).

**Risky tolerances:** TM1 pocket clearance 0.15 mm/side (print pocket-up, test-fit, shim with tape); grommet slit width (0.35 mm for a 0.4 mm leaf — print three widths); strap clamp torque (over-tightening creases TPU); knuckle pin fit (2.0 mm pin in a 2.1 mm printed bore, ream with a drill bit); lift-stop thread (heat-set M4 insert); the suspension ring's clip geometry (measure the bought suspension first — print the ring last).

### 2j. Honest weaknesses, top risks, bench tests

**Weaknesses:** one scalp pass per cycle at 1–1.5 Hz (half a human rake's pass rate); stroke length geometrically tied to force in single-DOF mode (decoupled only in 2-DOF firmware); no direction wander or per-finger wiggle (P4) without remounting; Bowden hysteresis; TPU hinge straps wobble ±1–2 mm and may creep; coverage is one patch per mounting; headgear can lift under nail reaction, which is both the ultimate safety backstop and a repeatability problem; long and curly hair out of scope; the knuckle detent's 0.6–0.8 N yield is above the 0.15 N target.

| # | Risk | Bench test that retires it |
|---|---|---|
| R1 | Leaf–stalk coupling (5 mm swing per 3 mm compression) causes the nail to "walk" or chatter, reading as a machine | Wand first (hand-driven leaf finger on the forearm and scalp); then slow-motion on the wig head at 100 mm/s; retire by shortening the stalk to 35 mm or stiffening the leaf |
| R2 | Headgear slides/lifts at < 4 N upward push → interference lost, weak scratch, or unbounded force if it does not lift | Mannequin pull-up test with a luggage scale on the bridge: record lift-off force with and without the nape strap; design target 5–8 N; if lower, add 100 g to the ring or a second nape strap |
| R3 | Bowden friction/hysteresis spoils force modulation (lift) and velocity shaping (rock) | Load cell at each lever vs servo position, up/down loop; accept ≤ 0.5 mm position hysteresis; otherwise shorten housings, PTFE-line them, or move an XL330 onto the forearm (Plan B: +18 g, one bracket reprint) |
| R4 | Hair reaches the knuckle clevis / grommets / cowl seams (8 cm hair) | hair-interaction §7.3 tests 4 and 5 (wrap and gap probe) with the long wig draped in every orientation; any capture → add TPU boots to the clevises and declare hair > 8 cm out of scope |
| R5 | Single-DOF 33 mm pull-only strokes feel short and predictable | Human test A/B: arc mode vs 2-DOF 55 mm mode vs symmetric-wedge bidirectional; the scratch model's irregularity knobs are firmware, so this is a tuning risk, not a rebuild |
| R6 | TPU straps creep during a 20-min session → P drops, force drifts up | Measure nail height vs time at the lift stop over 30 min with the hand loaded; > 1 mm drift → swap the ROCK straps for the 4 mm pin pivot (same clamp plates, boot the pin) |

### 2k. Self-score: massager-vs-scratcher (scratch-model §8)

1 Edge not pad — **PASS** (TM1 A–G). 2 Reaches skin — **PASS** expected (46 mm protrusion, 4 mm interference, drafted stalk; verify in T1 static tip test). 3 Light — **PASS** (0.3–1.2 N operating, 2.3 N constant cap). 4 Slides — **PASS** (33 mm chord, scalp displacement < 1 mm). 5 Speed band — **PASS** (60–150 mm/s; 1–1.5 Hz; no > 20 Hz component). 6 Deflects hair near root — **PASS**. 7 Multiple independent contacts — **PASS** (3 at 20 mm, independent leaves, 20–40 ms passive stagger). 8 Irregular — **PASS** with caveat (no direction wander). 9 Compliant at tip — **PASS** (0.2–0.6 N/mm, 7 mm travel). 10 Unloads at reversal, lifts between bouts — **PASS**. 11 Hair-safe geometry — **PASS** (sleeved TM1 seam). 12 Sounds like a scratch — **PASS** expected (motor-free head). **12/12 PASS, two with caveats.**

---

## 3. Schematic (side view, not to scale)

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 560" width="960" height="560" font-family="sans-serif" font-size="12">
  <rect width="960" height="560" fill="white"/>
  <!-- skull and scalp -->
  <path d="M40 500 Q480 400 920 500 L920 560 L40 560 Z" fill="#f3e3d3" stroke="none"/>
  <path d="M40 500 Q480 400 920 500" fill="none" stroke="#8a5a3a" stroke-width="3"/>
  <text x="60" y="540" fill="#8a5a3a">scalp (R ≈ 80 mm)  ·  skull below</text>
  <!-- hair canopy -->
  <g stroke="#6b4a2a" stroke-width="1">
    <line x1="120" y1="486" x2="112" y2="466"/><line x1="160" y1="478" x2="152" y2="458"/><line x1="200" y1="470" x2="192" y2="450"/>
    <line x1="240" y1="462" x2="232" y2="442"/><line x1="280" y1="456" x2="272" y2="436"/><line x1="320" y1="450" x2="312" y2="430"/>
    <line x1="360" y1="446" x2="352" y2="426"/><line x1="400" y1="443" x2="392" y2="423"/><line x1="440" y1="441" x2="432" y2="421"/>
    <line x1="520" y1="441" x2="512" y2="421"/><line x1="560" y1="443" x2="552" y2="423"/><line x1="600" y1="446" x2="592" y2="426"/>
    <line x1="640" y1="450" x2="632" y2="430"/><line x1="680" y1="456" x2="672" y2="436"/><line x1="720" y1="462" x2="712" y2="442"/>
    <line x1="760" y1="470" x2="752" y2="450"/><line x1="800" y1="478" x2="792" y2="458"/><line x1="840" y1="486" x2="832" y2="466"/>
  </g>
  <text x="60" y="425" fill="#6b4a2a">hair canopy (pile 5–20 mm)</text>
  <!-- exclusion zone line -->
  <path d="M40 425 Q480 325 920 425" fill="none" stroke="#c0392b" stroke-dasharray="6 4" stroke-width="1"/>
  <text x="700" y="372" fill="#c0392b">30 mm hair-exclusion zone: no joints below this line</text>
  <!-- headband pads -->
  <rect x="70" y="482" width="40" height="14" rx="4" fill="#999"/><rect x="850" y="482" width="40" height="14" rx="4" fill="#999"/>
  <text x="30" y="515" fill="#555">ratchet headband + nape strap (one-hand lift-off)</text>
  <!-- bridge legs and bridge -->
  <line x1="90" y1="482" x2="150" y2="180" stroke="#555" stroke-width="5"/>
  <line x1="870" y1="482" x2="810" y2="180" stroke="#555" stroke-width="5"/>
  <rect x="150" y="170" width="660" height="14" rx="4" fill="#555"/>
  <text x="400" y="162" fill="#555">bridge on suspension ring (3 seat positions: crown / rear / occiput)</text>
  <!-- cowl -->
  <path d="M250 184 L250 150 Q480 110 760 150 L760 184" fill="none" stroke="#777" stroke-dasharray="4 3"/>
  <text x="300" y="138" fill="#777">cowl over levers, springs, tendon ends</text>
  <!-- LIFT hinge strap -->
  <path d="M300 184 q-6 15 0 30" fill="none" stroke="#2a9d8f" stroke-width="6"/>
  <text x="200" y="230" fill="#2a9d8f">LIFT hinge (TPU strap pair)</text>
  <!-- forearm -->
  <rect x="300" y="214" width="380" height="10" rx="3" fill="#777"/>
  <text x="330" y="210" fill="#777">forearm frame (lifts 15 mm = 8.6°)</text>
  <!-- lift stop screw -->
  <line x1="640" y1="214" x2="640" y2="184" stroke="#222" stroke-width="3"/>
  <text x="648" y="205" fill="#222">lift hard-stop screw (sets h_min = force ceiling)</text>
  <!-- lift spring -->
  <path d="M590 184 l0 4 l6 4 l-12 4 l12 4 l-12 4 l12 4 l-6 4 l0 2" fill="none" stroke="#e76f51" stroke-width="2"/>
  <text x="520" y="200" fill="#e76f51" font-size="11">lift spring (returns UP on power loss)</text>
  <!-- LIFT tendon -->
  <line x1="680" y1="219" x2="900" y2="140" stroke="#264653" stroke-width="2"/>
  <text x="790" y="128" fill="#264653">LIFT tendon → desk box servo 2</text>
  <!-- ROCK hinge straps -->
  <path d="M480 224 q6 15 0 30" fill="none" stroke="#2a9d8f" stroke-width="6"/>
  <circle cx="480" cy="254" r="4" fill="#2a9d8f"/>
  <text x="498" y="258" fill="#2a9d8f">P = ROCK hinge (TPU straps), H = 62 mm above scalp</text>
  <!-- rock lever through forearm window + spring + tendon -->
  <line x1="480" y1="254" x2="480" y2="196" stroke="#444" stroke-width="4"/>
  <path d="M480 196 l-8 0 l-4 6 l-8 -12 l-8 12 l-8 -12 l-8 12 l-8 -12 l-4 6 l-10 0" fill="none" stroke="#e76f51" stroke-width="2"/>
  <text x="330" y="190" fill="#e76f51" font-size="11">rock return spring (parks rocker at −30°, nails up)</text>
  <line x1="480" y1="196" x2="900" y2="100" stroke="#264653" stroke-width="2"/>
  <text x="790" y="90" fill="#264653">ROCK tendon → desk box servo 1</text>
  <!-- rocker bracket to knuckle bar -->
  <line x1="480" y1="254" x2="600" y2="282" stroke="#444" stroke-width="6"/>
  <rect x="580" y="276" width="46" height="26" rx="8" fill="#444"/>
  <text x="632" y="300" fill="#444">knuckle bar / palm shell (50 mm up, smooth, grommeted)</text>
  <!-- leaf -->
  <line x1="582" y1="296" x2="478" y2="296" stroke="#1d3557" stroke-width="3"/>
  <text x="482" y="316" fill="#1d3557">leaf: 1095 steel 0.4×12.7 mm, 50 mm, 0.33 N/mm, heat-shrunk</text>
  <!-- leaf stop bumper -->
  <rect x="470" y="268" width="14" height="10" rx="2" fill="#f4a261"/>
  <text x="380" y="276" fill="#f4a261" font-size="11">leaf stop 7 mm (F_max = 2.3 N)</text>
  <!-- knuckle clevis + magnet -->
  <rect x="472" y="294" width="16" height="14" rx="3" fill="#6d6875"/>
  <circle cx="486" cy="304" r="3" fill="#c0392b"/>
  <text x="200" y="306" fill="#6d6875" font-size="11">knuckle: 2 mm pin + D41 detent, yields 0.6–0.8 N tangential</text>
  <!-- stalk -->
  <path d="M474 308 L486 308 L483 400 L477 400 Z" fill="#a8dadc" stroke="#457b9d"/>
  <text x="300" y="360" fill="#457b9d">stalk: drafted cone, 46 mm, nothing else in the pile</text>
  <!-- TM1 pocket + sleeve -->
  <rect x="474" y="398" width="12" height="14" rx="2" fill="#457b9d"/>
  <rect x="471" y="408" width="18" height="4" fill="#2a9d8f"/>
  <text x="498" y="412" fill="#457b9d" font-size="11">TM1 pocket (magnet, 4–8 N) + silicone band over seam</text>
  <!-- nail blade -->
  <line x1="478" y1="412" x2="494" y2="432" stroke="#111" stroke-width="3"/>
  <text x="500" y="440" fill="#111">nail tip A, 45°, edge R 0.3 mm, interference 4 mm (leaf bent)</text>
  <!-- arc path -->
  <path d="M400 406 A165 165 0 0 0 560 406" fill="none" stroke="#e63946" stroke-dasharray="5 4" stroke-width="2"/>
  <text x="330" y="398" fill="#e63946" font-size="11">nail arc R 66 mm: lands → 33 mm chord → exits 12 mm clear → reverses in air</text>
  <!-- pull direction arrow -->
  <line x1="420" y1="470" x2="540" y2="470" stroke="#e63946" stroke-width="2"/>
  <polygon points="540,465 552,470 540,475" fill="#e63946"/>
  <text x="430" y="488" fill="#e63946" font-size="11">pull stroke 70–130 mm/s; return lifted +15 mm</text>
</svg>

---

## 4. Notes for the tournament

- The design's distinctive bet is **geometric lift-off plus passive asynchrony**: the two hardest sensation/hair requirements (DR4/H-5.2 unload-before-reversal, scratch-model §4.2 finger asynchrony) are produced by the shape of the hand, not by the controller, so they cannot be lost to a firmware bug or a tuning mistake.
- Its honest cost is **stroke rate** (one pass per cycle) and **fixed direction per mounting**. If the tournament values two-way raking, the symmetric-wedge tip W is the cheapest fix (no new DOF); if it values direction wander, this family cannot supply it without a third axis, and a servo-finger or carriage family will win that criterion.
- Everything on the head is passive and printable in one JLC3DP order; the desk box is Stack B from the component landscape and is reusable by any other mechanism that pulls a tendon.
