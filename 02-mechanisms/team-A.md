# TEAM A — Single-Actuator Reciprocating Rake with Closed-Path Trajectory

**Project SCRATCH · 02-mechanisms · Team A · 2026-10-01**
**Seed family:** one cheap motor driving a compliant 3–4-nail rake along a closed path (engage → drag 15–40 mm → lift → return above the hair → re-engage).
**Inputs read:** BRIEF, scratch-model v1 (§1–3, §7, §8 as acceptance criteria), hair-interaction (H-4.x/H-5.x/H-6.x, 18-item checklist), safety-requirements (13 red lines), tip-interface (SP1-TM1 adopted), component-landscape. **Firewall:** no other team file and no prior-art.md were read.

Tags: `[CALC]` computed by us from a stated model (scripts run during this study) · `[EST]` engineering estimate · `[SPEC]` from a foundation document · `[UNKNOWN]` needs the bench.

---

## 0. What this family can and cannot do

A single motor produces one closed path: *where* the nails go is frozen into geometry; *when* they get there can still be varied by modulating motor speed against crank angle. So:

- **Geometry does the shape** (a flat-bottomed ellipse: chord, lift, entry/exit angles, attack angle) and the **force** (per-nail leaf springs with a hard stop).
- **The motor's speed-versus-angle profile does the time** (drag speed, return speed, pauses, stroke-to-stroke jitter) — the #1 sensation variable in scratch-model §7, for one $3 angle sensor.
- **A single actuator cannot** change region, stroke direction or stroke length on the fly. Those are manual in SP1 and are the family's structural weakness, scored honestly in §2j.

---

## 1. Concept generation

### A1 — "LOCOMOTIVE": twin parallel cranks, circular translation
Two crank shafts 50 mm apart, equal radius r, same phase, joined by the rake carrier (parallel-crank four-bar): the carrier translates in a circle of radius r without rotating, so attack angle is constant. Dead points are passed by a second "dummy" coupler on pins 90° away (locomotive side-rod trick, no gears). Contact chord at penetration d is 2·√(2rd − d²), lift 2r − d.

```
   motor──┤O├─────────────┤O├  idler        (both shafts along y, above guard)
          ╱ r              ╱ r
     pin •───────carrier────• pin           carrier translates in a circle of radius r
          │(dummy bar at 90° behind)
          ▼ hanger
    ──────┬──────┬──────┬────── comb bar (y)   3 leaves @ 20 mm
          ╲      ╲      ╲      blades 45°
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ scalp
```

`[CALC]` r = 24, d = 4: chord 27 mm, lift 44 mm, entry 34°, contact 22% of the cycle. Pros: revolute joints only, constant attack angle. Cons: 44 mm of vertical excursion (tall module, guard standoff ~50 mm); 22% duty needs 4:1 speed modulation; entry steeper than H-5.3. Fallback concept.

### A2 — "TRAMMEL": double Scotch yoke, true ellipse with independent a and b
One disc, two pins (radius a front, b back). Pin a drives a vertical slot in an X-carriage; pin b a horizontal slot in a Z-parallelogram riding on it: x = a·cosθ, z = b·sinθ, both set by screws. `[CALC]` a = 24, b = 12, d = 4: chord 36 mm, lift 20 mm, entry 29°, duty 27%.

```
      ┌─ disc (pin a front, pin b back) ─┐
      │        ○ ← pin b in horizontal slot of Z-plate
      │    ○ ← pin a in vertical slot of X-carriage
   ───┴─────────────────────────────────┴───
   X-parallelogram ⟷   Z-parallelogram ↕   → rake carrier (translation only)
```

Pros: independent stroke and lift knobs, compact. Cons: two pin-in-slot joints (rattle, print accuracy), eight pivots. Second choice.

### A3 — "PLANTIGRADE": Hoeken/Chebyshev four-bar — REJECTED by simulation
We simulated the textbook proportions (crank 1, ground 2, coupler 2.5, follower 2.5, point at 5) `[CALC]`: for a 35 mm stroke the lift is 6.7 mm (19% of stroke) and the coupler rotates through 65°, so a rigidly mounted rake would swing its attack angle ±32°. A 60,000-sample search for ≥15 mm lift, ≤25° tilt in contact and a monotonic 25–30 mm bottom found solutions only with 70–85 mm coupler extensions and in-contact velocity ratios of 0.1–0.5. Large, non-uniform, needs an orientation parallelogram. Rejected.

### A4 — "DWELL-CAM": conjugate plate cams on one shaft
X from a Scotch yoke, Z from a closed-groove plate cam on the same disc driving a lift lever: the lift profile is drawn, so the bottom can be a true dwell (constant force) with chosen entry/exit angles. `[CALC]` with sinusoidal X the usable window is still ≤120° (33% duty) because the slow ends must be avoided (H-5.3). Positive-return, no follower jump; one more lever and a printed groove whose 0.2 mm accuracy sets rattle. SP2 upgrade if a flat force plateau matters.

### A5 — "FEED-DOG": crank-rocker with the rake on the connecting rod — SELECTED
The sewing-machine four-motion-feed principle: the rake carrier *is* the connecting rod of a crank-rocker. A point on the rod traces an ellipse-like loop (semi-axes ≈ r and t·r, t = fractional position along the rod), and the rod's tilt is nearly constant through the bottom arc because sinθ ≈ −1 there. Three moving links, four bearings, one motor, no slots. Developed in §2.

```
        motor + crank arm (r=20)             rocker pivot Q   [crank plane sits BESIDE the rake]
            ◎──•pin                              ◎
                 ╲ connecting rod l=100         ╱ rocker q=40
                  •──────────┬──────────────•╱
                             │ L-hanger (t=0.45): 50 mm sideways, 20 mm down
                     ┌───────┴───────┐  moving shroud (smooth, drafted)
                     │ comb bar+TPU  │
                     └─┬─────┬─────┬─┘
                   leaf╲   leaf╲  leaf╲   0.3 mm spring steel, k≈0.2 N/mm
                        ╲       ╲      ╲  TM1 holders, blades at 45°
          ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ scalp
           tip path:  ⊂═══════════╗  (loop 48×22 mm; bottom 27 mm in contact)
```

### Irregularity from one actuator — options

| Option | Gives | Verdict |
|---|---|---|
| **Phase-aware speed modulation** (AS5600 on the crank, PWM vs angle) | per-stroke drag/return speed, pauses at the lifted phase, jitter, a "fully periodic" control mode | **Baseline**; zero parts; covers §4.4 except location/direction/length |
| **Per-nail compliance asynchrony** | 20–50 ms onset spread, ≥30% force spread `[CALC]` | **Baseline** (free) |
| Drag-link quick-return between motor and crank | mechanical 2–3:1 slow-drag/fast-return at constant voltage | no-microcontroller alternative; 4 extra pins |
| Wobble eccentric (crank pin on a slowly turning bushing, ~1:9) | stroke ±3 mm, chord shifts ±3 mm on a 9-cycle beat | optional add-on, sketch only |
| Elliptical gear pair | fixed 2:1 speed variation | inferior to firmware |
| Geneva / intermittent drive | dwell at a geometry-fixed phase | rejected; firmware pauses at θ = 90° do it |

### Wildcards (outside the family)
**W1 — "The head is the actuator."** The same comb bar on a mic-boom arm with a dead-weight preload (70–90 g per blade) and no motor; Michael moves his head under it and supplies the irregular trajectory himself. It isolates "does a stiff edge on a 0.2 N/mm leaf at 45° and 0.5–0.9 N feel like a fingernail, and do three feel like a hand?" from actuation. ~$40, one afternoon; recommended as the day-1 experiment whichever mechanism wins (the TM1 wand, tip-interface T0, is its one-nail version).

**W2 — Through-shell magnetic drive.** Any 2-D drive inside a sealed smooth dome; the rake carrier rides on the dome's underside on PTFE pads, dragged by magnet pairs through a 1.5 mm wall, so the hair sees a monolithic shell. Needs ~2 N of coupling through a 3 mm gap and a carrier-to-shell gap held >3 mm. Parked for SP2.

---

## 2. Selected concept: SP1-A "FEED-DOG" crank-coupler rake (CCR-3)

### 2a. Working principle and why it is a scratch, not a massage
An N20-class gearmotor turns a counterweighted crank arm (pin radius 20 mm). A 100 mm connecting rod runs from the crank pin to a 40 mm rocker whose ground pivot is 100 mm along and 40 mm above the crank axis. The crank plane sits *beside* the rake (y = +55 mm), not above it: an L-shaped hanger at 45% of the rod length reaches 50 mm sideways and 20 mm down and carries, 64 mm below the rod, a transverse comb bar with three leaf-sprung nail holders at 20 mm pitch. Because sinθ ≈ −1 through the bottom of the revolution, rod tilt varies only 2.4° during contact `[CALC]`: constant attack angle on the skin, lift-off while still moving forward. The tip traces a 48 × 22 mm loop whose bottom 27 mm is the scratch.

Against scratch-model §1.2/§1.3/§3/§8:
1. *Edge, not pad* — SP1-TM1 tip A: 12 mm blade, edge R 0.3, nylon/PETG, 45° (3.11f).
2. *Reaches the skin* — 30 mm protrusion below the shroud (H-4.5); depth screw puts the nail 0–5 mm "below" the nominal scalp plane, absorbed by the leaf; edge at skin level for the chord in short/medium hair (3.14 estimates 40–90%; bench confirms).
3. *Light, hump-shaped* — 0.15 N at entry → 0.95 N mid-stroke → 0.15 N at exit `[CALC]`, mean 0.67 N, inside the tip-interface window (0.3–0.9 N on a 6 mm edge); cap 1.8 N/nail.
4. *Slides* — 27 mm on skin per cycle at 100–150 mm/s (3.6/3.7 rake values); scalp displacement bounded by the ≤0.5 N the hinge transmits.
5. *Right band* — 2–15 cm/s by profile, 1.2–2 Hz; nothing >20 Hz reaches the skin (bearings only; motor 70 mm up on foam).
6. *Near-root hair deflection* — edge-first blade parts lanes and meets hair at the follicle exit (hair-interaction §2.1–2.2); 25° plough-in overruns hair.
7. *Three asynchronous contacts* — independent leaves + curvature: 20–50 ms onset spread, ≥30% force spread `[CALC]` (4.2).
8. *Irregular in time* — every stroke can differ in speed and pause; bouts and lifted pauses built in (§2c).
9. *Lift-off every stroke* — 18 mm clear; exit at 42% of peak forward speed (H-5.2/5.3, DR4, DR7).


### 2b. Architecture
- **Mount (primary): head-worn.** A $12–23 hard-hat ratchet suspension in a $10–15 shell; a 110 × 90 mm window cut over the occiput-to-crown region; the housing flange bolts over it with four M4 thumb-nuts. The shell is the outer guard (25–30 mm standoff); the ratchet is the one-hand release. Mass ≈ 250 g shell+suspension + 170 g module ≈ 420 g `[EST]`. Option M2: printed rails on the bare suspension (lighter, slidable). Option M3: the housing on a gas-spring monitor arm with a headrest (1/4-20 insert).
- **Coverage:** one patch ≈ 40 mm (three nails at 20 mm) × 27 mm, occiput or crown (scratch-model §5's two highest-value, simplest-curvature regions). Region change manual (second window + blanking plate, or M2 slide). Direction: re-mount in 90° steps (indexed holes); drag sense fixed by blade orientation, so with-lie/against-lie is the 0°/180° choice.
- **Contacts:** 3 (4 by a wider comb bar). **DOF:** 1 actuated + 3 passive normal + 3 passive tangential yields.
- **Heights above scalp:** crank axis 70 (arm sweep bottom 44); rocker pivot 110; rod 60–80; comb bar 40–58; leaves 28–46; blades 0–18. Only leaves and holders exist below 30 mm. Laterally, the crank compartment (y 40–70) is a closed box beside the open rake bay (y −40…+40); the two share only the L-hanger.

### 2c. Kinematics `[CALC]` (r = 20, l = 100, q = 40, Q = (100, 40), t = 0.45, hang 64 mm, d = 4 mm)

| Quantity | Value | Note |
|---|---|---|
| Tip loop | 48 (x) × 22 (z) mm | x-range 23…71 mm from crank axis |
| Contact chord | **27 mm** | d = 3 → 24; d = 5 → 30; r = 24 disc → 29 |
| Lift above skin | **18 mm** | ≥ pile + 5 for short/medium hair (H-5.2) |
| Contact fraction | 25% (90° of crank) | time share set by the motor profile |
| Entry angle | **25°** | H-5.3 ≤ 30° |
| Exit angle / forward speed at exit | 48° / 42% of peak | H-5.3 ≥ 30% |
| Rod tilt in contact | +9.2 … +11.6° | holder printed at 45° − 10.5° |
| Rod tilt over cycle | ±11.6° | only in the air |
| Min transmission angle | 54° | no binding |
| Per-nail force along chord | 0.15 → 0.95 → 0.15 N | k 0.2 N/mm, preload 0.15 N |

**Velocity profile.** At constant crank speed the drag is a quarter of the cycle, so 2 Hz = 220 mm/s, too fast (3.6, H-5.4). Two legal modes:
- *Constant speed, no sensor:* 1.2 Hz → drag 130 mm/s for 0.21 s, air 0.62 s. The control condition.
- *Phase-modulated (baseline):* AS5600 on the crank hub at 1 kHz; ESP32 velocity loop with a 36-entry ω(θ) table. Contact arc (θ 215–305°) at 55 rpm → 0.27 s drag ≈ 100 mm/s; return at 140 rpm → 0.32 s; **1.7 Hz**. Ratio 2.5:1; decelerating over the 90° before contact needs ≈0.06 N·m against a 210:1 gearbox's reflected inertia `[CALC]` (30% of stall) — feasible; DRV8871 brake mode helps.

**Irregularity engine (scratch-model §4.4 on one motor):**
```
SESSION = bouts separated by lifted pauses (parked at θ = 90°, 18 mm up)
BOUT: N ~ U(4,12) strokes
  per stroke: v_drag ~ N(100 mm/s, 25%) clipped 40–180; v_return ~ U(1.3, 2.0) × v_drag
              p(pause at top) = 0.15, pause ~ U(0.3, 1.5 s)
  once per minute: slow bout, v_drag ~ U(25, 50 mm/s)   (CT channel, 2.2)
BOUT PAUSE: ~ U(1, 3 s), p = 0.7
KNOBS: intensity pot scales v_drag 0.7–1.3× (force is the depth screw); speed pot scales cycle rate
CONTROL: "metronome" mode, constant ω  (scratch-model §9.5)
LIMITS (one clamped table): ω ≤ 150 rpm, in-contact v ≤ 180 mm/s, bout ≤ 12 strokes, no loaded dwell
```
Not jitterable: stroke length (depth screw only), direction, location; location wander is the operator (move the module every 1–2 min, rake parked lifted).

### 2d. Force path and caps
**Normal path:** scalp → blade → TM1 holder → leaf (0.3 × 10 mm spring-steel feeler stock, free length 40 mm, trailing the comb bar so drag loads it in tension) → root clamp → TPU living hinge → comb bar → L-hanger → rod → crank pin → motor.
- Leaf `[CALC]`: EI = 200 GPa × 10 × 0.3³/12 = 4500 N·mm²; k = 3EI/L³ = **0.21 N/mm** (L 35 → 0.31 as the stiff variant). Pulp-like (3.12; tip-interface 0.3–0.6 lower edge).
- Preload: pre-bent 0.75 mm against a stop → **0.15 N**.
- Hard stop at **8 mm** (boss under the holder meets the comb-bar skirt) → **F_max = 0.15 + 0.21 × 8 = 1.8 N/nail**, 5.4 N total (red lines 2, 3). Leaf stress 450 MPa at the stop, 225 MPa at 4 mm `[CALC]`, below tempered-strip fatigue limits.
- Actuator-stop condition (safety §3.1): depth screw limited to 0–5 mm; suspension gives ~3 mm more `[EST]`; worst case 8 mm = the stop. Beyond it the path is rigid and the DRV8871 limit (ILIM ≈ 0.8 A → ≈0.08 N·m at 210:1 → ≤4 N total at the 20 mm crank) is the second layer. Thin margin; measured in §2j risk 4.
- Operating: depth 2–5 mm → peak 0.57–1.2 N, mean 0.4–0.85 N. **Intensity is the depth thumbscrew — a mechanical setting with a mechanical ceiling.**

**Tangential yields (three layers):**
1. *Per-nail TPU living hinge + magnetic detent* (H-4.11): leaf root clamp joined to the comb bar by a 2 × 10 × 3 mm TPU 95A neck (≈110 N·mm/rad → 0.04 N/mm at the tip `[CALC]`), held forward against a stop by a D41 magnet on a 6 mm lever against the ~55 mm tip lever, shimmed to release at **0.45–0.55 N** at the tip (0.35 N scratch friction + 0.15 N snag margin). Beyond that the nail swings back, flattens and rises. Calibrate with the 15 g/50 g tether (hair-interaction 7.3.6).
2. *Comb-bar magnetic cup* (H-6.4): two D61 magnets, shear breakaway 3–5 N `[EST]`, no tether.
3. *TM1 tip magnet*: 4–8 N axial.

**Curvature:** comb bar printed to R 90 so the tips lie on the crown sphere; parietal mismatch ≤0.7 mm plus ±0.5 mm blade tolerance against 8 mm of travel. The leaf's end-slope under load (3δ/2L ≈ 8.6° at 4 mm `[CALC]`) steepens the attack angle with force and relaxes it on unloading — the nail lifts rotating about its trailing side, as a finger does (H-5.2).

### 2e. Hair safety
**Inside the 30 mm exclusion volume:** three polished steel leaves, three PETG TM1 holders, three blades. No rotating surface, bearing, gear, pin, slot or changing gap.

| Joint | Height above scalp (bottom … top) | Exclusion method (H-6.2) |
|---|---|---|
| TM1 tang/pocket seam (0.15 mm/side) | ~8 … 26 mm (in the pile) | sealed: holder carries a 1 mm overlapping skirt over the tang shoulder; static seam; optional TPU collar |
| Leaf-to-holder clamp (M2) | 25 … 43 | heads recessed under a smooth cap, 1 mm fillets |
| Root clamp + TPU hinge + detent | 40 … 58 | inside the moving shroud (method 1); hinge gap-free by construction |
| Comb-bar magnetic cup | 50 … 68 | inside the shroud |
| L-hanger through the compartment side wall | 60 … 80 | drafted slot 48 × 30 mm, open clearance ≥5 mm, above the bay |
| Crank arm, pin, rocker pins, hub, AS5600 magnet | ≥ 44 | inside the closed crank compartment beside the bay (own floor at 40 mm over intact shell) |

**Guards:** (1) the **moving shroud** — a smooth convex 15°-drafted PETG cap (70 × 50 × 18 mm, edges R 2) fixed to the comb bar, enclosing hinges, magnets and clamps and translating with them; underside 32 mm above the scalp at the bottom of the stroke (≥ pile depth, H-6.3); only the leaves pass through, each via a drafted 16 × 14 mm opening with ≥3 mm clearance; (2) the **fixed skirt** — housing walls down to 35 mm around the shroud's envelope with ≥5 mm open clearance; (3) the **crank compartment**, a closed box beside the bay with its own floor at 40 mm; the hard-hat shell closes the rest. The hair sees blades, leaves, a smooth moving cap, a smooth skirt, a shell.

**Motion:** lift-off every stroke (18 mm); exit while moving forward; entry 25°; nails move as one rigid group (independent travel is normal only; the hinge moves only on a snag); with-grain default by mounting (crown→nape on the occiput); against-grain is a short 27 mm stroke followed by lift (H-5.1). **Snag reflex:** the hinge yields within the stroke; INA219 current >1.5× baseline for 200 ms → firmware continues *forward* to θ = 90° and stops, never reverses (H-5.9).

**18-item self-score (hair-interaction §6.8):**

| # | Item | Score | Note |
|---|---|---|---|
| 1 | No exposed rotation in zone (gating) | 2 | all rotation ≥ 44 mm, in a closed compartment beside the rake |
| 2 | Every zone joint has an exclusion method (gating) | 2 | table above |
| 3 | No changing / 40 µm–3 mm gap within 25 mm (gating) | 2 | only the TM1 seam, static and skirted; fishing-line probe |
| 4 | Lift-off before every reversal (gating) | 2 | 18 mm every cycle |
| 5 | Canopy elements move as a rigid group (gating) | 2 | normal-only independence |
| 6 | Radiused blade, drafted root (gating) | 2 | TM1 tip A |
| 7 | Yields ≤ 0.15 N tangential on a snag (gating) | 1 | detent ≈0.5 N absolute (0.15 above friction); magnet tolerance ±30% until calibrated |
| 8 | Protrusion ≥ 25 mm | 2 | 30 mm |
| 9 | Tip spacing ≥ 8 mm | 2 | 20 mm |
| 10 | Low-friction polished sliding surfaces | 2 | nylon/PETG blades, polished steel; TPU only inside the shroud |
| 11 | Breakaway 3–5 N, no tether | 2 | comb-bar magnets + TM1 |
| 12 | Hair-shedding guard, drafted pass-throughs | 2 | shroud + skirt + shell |
| 13 | With-grain bias / grain map in control | 1 | direction is a mounting choice; no map in firmware |
| 14 | Dwell / repetition limits | 1 | bouts ≤ 12 with lifted pauses; relocation manual |
| 15 | Snag reflex lift-and-retract, never reverse | 2 | forward-to-park |
| 16 | Antistatic | 1 | steel leaves grounded; nylon blades; CF-nylon variant listed |
| 17 | Tool-free removal of zone parts | 2 | tips, comb bar (magnets), shroud (clips), shell (thumb-nuts) |
| 18 | States hair variants | 2 | buzz/short/medium straight-to-wavy yes; coarse yes (+1 mm depth); long (>15 cm) **no**; curly/coily **no** |
| | **Total** | **32/36** | no gating zero; ≥ 28 |

### 2f. Safety — the 13 red lines
1. No exposed rotation/open slot within 30 mm — **met** (≥44 mm, closed compartment beside the rake).
2. Normal force bounded by a mechanical constant ≤2.5 N — **met**: 1.8 N/nail, leaf + stop.
3. ≤12 N total, ≤2 N tangential before yield — **met**: 5.4 N; hinge 0.5 N, breakaway 3–5 N; current cap ≤4 N total as second layer.
4. NC e-stop in series with motor power; hold-to-run — **met**: 22 mm NC mushroom in the 12 V motor rail between fuse and DRV8871; momentary foot pedal; logic on its own buck ahead of the e-stop.
5. No mains inside, ≤24 V, no lithium — **met**: Mean Well GST60A12.
6. No moving element anterior to the hairline / near the ear / above the eyes unguarded — **met**: windows only at occiput/crown; housing end-stops; shell is a guard.
7. No self-locking drive without downstream spring cap *and spring-return lift-off* — **partial**: leaf cap downstream of the non-back-drivable gearbox ✓; spring-return lift ✗ (a stopped crank stays put). Mitigations: firmware parks at θ = 90° on every stop/stall/watchdog/pedal release; the pedal switches the motor rail through a P-MOSFET with a 0.5 s RC drop-out (hardware timer) so the park completes; the e-stop cuts instantly — in that case nails may rest at ≤1.8 N static, no drive force, until the ratchet is released (≤3 s). **Flagged for the Safety Gate.**
8. No contact held after power loss — **partial** as in 7: "limp" in force, not lifted.
9. No push-fit-only, PLA or brittle tips; proof-loaded — **met**: TM1 magnet + walls; nylon/PETG; 3× proof.
10. One-hand ≤3 s release, no chin strap, ≤500 g — **met**: ratchet, ≈420 g.
11. No skin-accessible edge <1 mm (tips <0.4) — **met** for structure (R ≥ 2); tip A's 0.3 mm edge is the tip-interface baseline vs safety's 0.4 — use tip B (0.6) or a 0.4 mm A for first sessions; flagged.
12. First human session only after checklist, wig test, glasses, ≤5 min — **procedural, adopted**.
13. Firmware never the only barrier for S≥3 — **met**: force (spring+stop), tangential (magnets), speed (a 210:1 gearbox at 12 V cannot exceed 150 rpm → tip ≤0.31 m/s in air, ≤0.28 m/s in contact on any firmware fault — the reason 210:1 is chosen over 100:1).

E-stop on the desk within reach of either hand; pedal under the foot; nothing on the head unit.

### 2g. Adjustability

| Variable | How | Range |
|---|---|---|
| Normal force (and chord) | **depth thumbscrew** (M5, 0–5 mm, hard end) | peak 0.15–1.2 N; chord 0–30 mm |
| Force slope / cap | leaf swap (0.25/0.30/0.35 mm stock, L 35–40) | k 0.12–0.45 N/mm |
| Drag speed, return speed, pauses, jitter | firmware tables + two pots | 25–180 mm/s; 1.2–2 Hz |
| Stroke length | crank-arm swap (pins at r 16/20/24) | chord 22–30 mm at d = 4 |
| Lift height | hanger position t (0.4/0.45/0.5) | 16–20 mm |
| Attack angle | TM1 holder variants 35/45/55° (with −10.5° rod-tilt offset) | |
| Contacts / spacing | plug 1–3 tips; comb-bar reprint (16/20/24 mm; 4 nails) | 1–4 |
| Direction vs lie / region | mounting index 0/90/180/270°; window position or rail slide | occiput, crown |
| Regularity | "metronome" vs "human" mode | control condition |
| Tip geometry/material | TM1 tips A–H | |

### 2h. Components and cost (prices per component-landscape; (~unverified) where it says so)

| Qty | Item | Unit | Ext. |
|---|---|---|---|
| 1 | Pololu micro metal gearmotor HPCB **210:1**, 12 V (≈140 rpm, ≈2 kg·cm) (~unverified SKU; 6 V HP + 6 V UBEC fallback) | $25 | $25 |
| 1 | Pololu micro gearmotor bracket pair | $4 | $4 |
| 1 | Adafruit DRV8871 (ILIM ≈ 0.8 A) | $7.50 | $7.50 |
| 1 | AS5600 breakout + 6 × 2.5 mm diametric magnet | $4 | $4 |
| 1 | ESP32 DevKitC | $10 | $10 |
| 1 | INA219 | $9.95 | $10 |
| 1 | Mean Well GST60A12-P1J 12 V 5 A | $19 | $19 |
| 1 | 22 mm NC mushroom e-stop | $12 | $12 |
| 1 | Momentary foot switch + P-MOSFET/RC delay parts | $13 | $13 |
| 1 | Inline rocker, blade fuse holder, 2 A fuses | $8 | $8 |
| 2+1 | 10 kΩ pots + knobs; SSD1306 OLED (optional) | — | $10 |
| 3 | 623ZZ bearings (10-pack) | $7 | $7 |
| 3 | 3 × 16 mm dowel pins + e-clips (or M3 shoulder screws) | — | $6 |
| 1 | Feeler-gauge set (0.25–0.35 mm = leaf stock) | $8 | $8 |
| 1 | Magnets: 6× D41, 2× D61, 3× N52 6×2; steel washers | — | $8 |
| 1 | Hard hat + 4-point ratchet suspension | $25 | $25 |
| 1 | PETG/TPU printing ≈330 g (library or JLC3DP) | — | $25–40 |
| 1 | M2/M3/M4 screws, heat-set inserts, thumb-nuts, 6-core cable 1.5 m, JST, 2 mm EVA | — | $22 |
| 1 | Tip stock: press-on nails, Tortex/nylon picks, 0.8 mm nylon sheet | — | $12 |
| 1 | Optional FSR 402 under one leaf root | $7 | $7 |
| | **Build subtotal** | | **≈ $255–270** |
| | Test gear (mannequin head $30, kitchen scale $12, load cell+HX711 $10, lint roller/hygrometer $12) | | ≈ $64 |
| | **Total** | | **≈ $320–335** |

**Printed parts (PETG, 0.4 mm nozzle, unless noted):**

| Part | Approx. size | Mass | Notes |
|---|---|---|---|
| Housing: closed crank compartment (floor at 40 mm) beside an open rake bay (105 × 80 mm) with a 10 mm skirt; motor clamp, rocker boss, AS5600 bracket, flange | 150 × 120 × 60 mm | 75 g | 4 perimeters; side-wall slot 48 × 30 for the L-hanger |
| Crank arm | 34 mm sector, 6 mm thick, 10 mm D-bore hub, pin holes r 16/20/24, counterweight pocket at r 16 (~25 g washers); sweep bottom 44 mm | 10 g | M2 set screw on the D-flat; an arm, not a disc, so nothing sweeps the shroud |
| Connecting rod | 100 mm centres, 8 × 12, bearing seats print 9.8 and ream, hanger boss at 45 mm | 10 g | |
| Rocker | 40 mm centres, 8 × 10 | 4 g | |
| L-hanger | 50 mm transverse × 20 mm drop, 8 × 12 PETG, magnet cup | 10 g | offset load is carried by the rod's two bearings 100 mm apart |
| Comb bar (TPU 95A) | 64 × 14 × 10, R 90 curve, three 2 × 10 × 3 living-hinge necks, D41 pockets | 10 g | alt.: PETG bar + 2 mm pin hinges |
| Leaf root clamps ×3 | 12 × 12 × 10, M2 clamp, pre-bend stop, 8 mm stop boss | 6 g | |
| TM1 holders ×3 (35/45/55° sets) | 16 × 12 × 20, pocket 10.3 × 4.3 × 12.5, N52 6×2, 1 mm skirt, leaf slot | 9 g | |
| Moving shroud | 70 × 50 × 18 cap, 1.6 mm wall, 15° draft, R 2 edges, three 16 × 14 openings | 20 g | clips to the comb bar |
| Shell window bezel + blanking plate | 120 × 100 frame | 25 g | bolts through the shell |
| Depth-screw clamp blocks ×2 | 25 × 20 × 15, M5 insert, 90° index pins | 16 g | |
| Off-head control box | 120 × 80 × 40 | 60 g | ESP32, DRV8871, INA219, pots, e-stop |
| TM1 wand handle (tip tests T0/T2) | 120 mm | 15 g | |

Moving mass ≈ **75 g** (rod 10, L-hanger 10, comb 10, clamps 6, holders 9, leaves/blades 6, shroud 20, bearings 4); KE at 0.31 m/s = 3.6 mJ ≪ 50 mJ; ≤30 g per element met.

### 2i. Buildability in an apartment
**Tools:** component-landscape §8 set plus a step drill/Dremel and a small vise. **≈ 26–32 hands-on hours**, printing excluded:
1. Day 0 orders (Amazon: hard hat, bearings, magnets, feeler gauges, e-stop, pedal, pots; Pololu: motor, bracket; Adafruit: DRV8871, INA219; DigiKey: Mean Well). Print the TM1 wand first; run tip-interface T0–T2 while waiting (4 h).
2. Print housing, disc, rod, rocker, hanger, clamps, holders, shroud, bezel (~14 h machine time; one library day or one JLC3DP batch); TPU comb bar (or the PETG pin-hinge alternative).
3. Leaves: cut three 0.3 mm feeler blades to 55 mm, corners R 2, polish to 1000 grit, pre-bend 0.75 mm (1 h).
4. Tips: three tip A from press-on nails on TM1 tangs; one tip B; one tip H control (1.5 h).
5. Dry-fit: press 623ZZ into rod and rocker, pin the crank arm, fit the rocker and L-hanger; hand-crank a full turn checking rod tilt, arm-to-compartment clearance and ≥5 mm shroud/skirt clearance; shim the counterweight until the crank turns evenly (2 h).
6. Comb bar: clamp leaves, fit holders, set detent shims; calibrate per-nail force on a kitchen scale at 2/4/6/8 mm and detent release with 50 g then 15 g tethers over a pulley (2 h).
7. Shell: cut the window, fit bezel and clamp blocks, mount the housing; set depth 0 = blades just touching a foam head at the bottom of the stroke (1.5 h).
8. Electronics per safety §4: fuse → e-stop → pedal MOSFET → DRV8871; logic buck before the e-stop; INA219 on the motor rail; AS5600 on I²C; 6-core cable with service loop and strain relief (3 h).
9. Firmware: AS5600 velocity loop, ω(θ) table, bout/pause engine, metronome mode, limits table printed at boot, stall/watchdog/park logic (8–12 h — the item most likely to slip).
10. Bench: safety §6 A–D; hair-interaction 7.3 tests 1–9 on the mannequin; tip-interface T1 (6 h).

**Risky tolerances:** 3 mm pins in printed seats (print 2.85, ream to a snug push fit; a loose crank pin is the main rattle source); 10 mm bearing seats (print 9.8, ream); blade heights coplanar to ±0.5 mm (shim on a flat plate); detent magnet gap (±0.1 mm ≈ ±30% force; calibrate); shroud/skirt clearance through the whole loop including ±11.6° rod tilt (hand-crank before power); TPU neck creep (re-check weekly).

### 2j. Honest weaknesses, top 5 risks, retiring tests
**Weaknesses:** (a) it scratches one 40 × 27 mm patch until someone moves it — H-5.5 and scratch-model 3.24 (≤50 passes/min on one spot) are met only through bouts, pauses and manual relocation every 1–2 min; (b) force and chord are the same knob and drift with head seating (±3 mm ≈ ±0.6 N peak, ±4 mm chord); (c) stroke length, direction and location never jitter, only time — if §4.3 is right that spatial unpredictability defeats habituation, this family delivers it only partly; (d) a stopped crank is not a lifted crank (red lines 7/8 partial); (e) the 25° plough-in through the pile is firmer than a finger's landing; (f) a gearmotor 70 mm above the scalp in a resonant shell — noise unproven.

| # | Risk | Test | Retire / fallback |
|---|---|---|---|
| 1 | Fixed-patch monotony: "a machine on one spot" within 30 s regardless of time-jitter | 5-min occiput self-session, metronome vs human mode; rate "person-like" at 0.5/1/2/5 min; erythema check | human mode holds >2 min → pass; else SP2 needs a slow traverse (second axis, outside this family) |
| 2 | Hair loops at entry (descending edge, cross/against grain) | hair-interaction 7.3.3: 200 cycles with/against grain, slow-motion video, shed count vs baseline | ≤2× baseline, zero loops → pass; else t = 0.4 (more lift), shallower depth, with-grain only |
| 3 | Jerky phase modulation (backlash clunk at the 2.5:1 deceleration) | AS5600 log at 1 kHz; accelerometer on the shroud; listen at the ear | smooth the ramp over 120°, brake mode; fallback constant 1.2 Hz or the drag-link stage |
| 4 | Force/depth coupling wanders with head position; leaf bottoms on the stop | FSR under one leaf root during a 5-min wear with deliberate head motion; count stop hits | drift >±0.3 N → softer leaf (0.25 mm, k 0.12) with r = 24, d = 6; tighten suspension |
| 5 | Attack angle + force-dependent blade rotation (rod +9…12°, leaf slope ≤8.6°) read as "digging" | 240 fps side view on the mannequin at 2/4/6 mm depth | 35° holder or stiffer leaf; if liked, keep (mimics a flexing DIP joint) |

Also watched: TM1 seam in the pile (probe 7.3.5); TPU creep; motor noise >60 dBA at the ear.

### 2k. Massager-vs-scratcher self-score (scratch-model §8)

| # | Criterion | Score | Evidence |
|---|---|---|---|
| 1 | Edge, not pad | PASS | TM1 tip A, 0.3 mm edge, nylon/PETG |
| 2 | Reaches the skin | PASS (verify) | 30 mm protrusion, 0–5 mm depth |
| 3 | Light | PASS | 0.15–0.95 N/nail, cap 1.8 N, total ≤5.4 N |
| 4 | Slides ≥10 mm with slip | PASS | 27 mm chord |
| 5 | Right speed band | PASS modulated / 1.2 Hz; FAIL at constant 2 Hz | 100–150 mm/s, 1.2–2 Hz, nothing >20 Hz |
| 6 | Deflects hair near the root | PASS | edge-first blade at skin level |
| 7 | 3–5 independent contacts, ≥20 ms / ≥20% spread | PASS | 3 at 20 mm; 20–50 ms, ≥30% `[CALC]` |
| 8 | Irregular (length, speed, force, direction, location, pauses, lifts) | UNSURE | speed/force/pauses/lifts yes; length/direction/location no; metronome control included |
| 9 | Compliant tip ≤0.5 N/mm, ≥5 mm travel | PASS | 0.21 N/mm, 8 mm |
| 10 | Unloads at reversal, lifts between bouts | PASS | 18 mm every cycle; parks lifted |
| 11 | Hair-safe geometry | PASS | §2e |
| 12 | Sounds like a scratch, not a motor | UNSURE | gearmotor 70 mm up, foam-isolated; untested |

No FAIL on items 1–6; item 8 is the family's declared limit.

---

## 3. Schematic (side view, stroke plane; not to scale)

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 700" width="760" height="700" font-family="Helvetica, Arial, sans-serif" font-size="11">
<rect width="760" height="700" fill="#fff"/>
<text x="20" y="22" font-size="14" font-weight="bold">SP1-A FEED-DOG crank-coupler rake — side view in the stroke plane (x = drag →, z ↑)</text>
<text x="20" y="38" font-size="10" fill="#555">Scale 3 px/mm, crank at 250° (mid-contact). Grey dashed parts lie in the crank plane (y = +55 mm) BESIDE the rake and are behind it in this view (see inset).</text>
<path d="M30,590 Q330,530 740,590" fill="none" stroke="#333" stroke-width="2.5"/>
<path d="M30,545 Q330,485 740,545" fill="none" stroke="#999" stroke-width="1" stroke-dasharray="4 3"/>
<path d="M30,500 Q330,440 740,500" fill="none" stroke="#c00" stroke-width="1" stroke-dasharray="6 4"/>
<path d="M30,512 Q330,452 740,512" fill="none" stroke="#555" stroke-width="3" stroke-dasharray="95 330"/>
<text x="640" y="600" fill="#333" font-size="10">scalp (R ≈ 90 mm)</text>
<text x="560" y="541" fill="#666" font-size="10">hair canopy top (5–20 mm)</text>
<text x="470" y="524" fill="#555" font-size="10">hard-hat shell, 26 mm standoff (window over bay)</text>
<text x="20" y="496" fill="#c00" font-size="10">30 mm hair-exclusion boundary</text>
<rect x="134" y="185" width="321" height="270" fill="none" stroke="#555" stroke-width="1.5"/>
<text x="140" y="199" fill="#555">housing: open rake bay (skirt to z = 35); crank compartment behind, own floor at z = 40</text>
<line x1="134" y1="440" x2="455" y2="440" stroke="#999" stroke-width="1" stroke-dasharray="3 3"/>
<circle cx="170" cy="351" r="60" fill="none" stroke="#888" stroke-width="1" stroke-dasharray="4 3"/>
<rect x="108" y="339" width="34" height="24" fill="#ddd" stroke="#666"/>
<line x1="170" y1="351" x2="149" y2="407" stroke="#666" stroke-width="6" stroke-linecap="round"/>
<rect x="176" y="298" width="20" height="16" fill="#aaa" stroke="#666"/>
<circle cx="170" cy="351" r="6" fill="#888"/>
<rect x="158" y="327" width="24" height="7" fill="#cfc" stroke="#666"/>
<circle cx="149" cy="407" r="5" fill="#fff" stroke="#666" stroke-width="1.5"/>
<line x1="149" y1="407" x2="444" y2="348" stroke="#666" stroke-width="4" stroke-dasharray="8 4"/>
<circle cx="470" cy="231" r="4" fill="#666"/>
<line x1="470" y1="231" x2="444" y2="348" stroke="#666" stroke-width="3" stroke-dasharray="6 3"/>
<circle cx="444" cy="348" r="4" fill="#fff" stroke="#666" stroke-width="1.5"/>
<text x="20" y="291" fill="#666">crank arm, pin r = 20</text><text x="20" y="304" fill="#666">axis z = +70; sweep bottom z = 44</text>
<line x1="120" y1="299" x2="150" y2="327" stroke="#999" stroke-width="0.8"/>
<text x="20" y="355" fill="#666">N20 gearmotor</text>
<text x="20" y="393" fill="#666" font-size="10">AS5600 on hub face (green)</text>
<text x="200" y="296" fill="#666" font-size="10">counterweight, r 16</text>
<text x="478" y="235" fill="#666">rocker pivot Q (+100, +40)</text>
<text x="458" y="293" fill="#666">rocker q = 40</text>
<text x="458" y="364" fill="#666">connecting rod l = 100</text><text x="458" y="377" fill="#666">tilt +9…12° during contact</text>
<circle cx="282" cy="381" r="7" fill="#fff" stroke="#333" stroke-width="2"/><circle cx="282" cy="381" r="2" fill="#333"/>
<line x1="282" y1="388" x2="282" y2="417" stroke="#333" stroke-width="5"/>
<text x="296" y="403">L-hanger (t = 0.45): 50 mm toward viewer, then 20 mm down</text>
<rect x="222" y="417" width="120" height="54" rx="12" ry="12" fill="#eef" stroke="#336" stroke-width="1.5"/>
<rect x="261" y="426" width="42" height="30" fill="#fc9" stroke="#333"/>
<text x="352" y="433" fill="#336">moving shroud 40 × 70 × 18 mm, 15° draft, R2 edges;</text>
<text x="352" y="447" fill="#336">comb bar (orange), TPU hinges, detent magnets inside;</text>
<text x="352" y="461" fill="#336">underside z = 32 at the bottom of the stroke</text>
<polyline points="294,456 294,477 174,477" fill="none" stroke="#06c" stroke-width="2.5"/>
<text x="352" y="477" fill="#06c">leaf (blue): 0.3 × 10 mm spring steel, L 40, k ≈ 0.21 N/mm,</text>
<text x="352" y="491" fill="#06c">trails the comb bar; its root hinge is inside the shroud</text>
<polygon points="160,477 182,477 200,525 178,525" fill="#ccc" stroke="#333"/>
<line x1="184" y1="525" x2="204" y2="563" stroke="#000" stroke-width="3"/>
<circle cx="204" cy="563" r="2.5" fill="#000"/>
<text x="20" y="519">TM1 holder,</text><text x="20" y="532">pocket at 45°</text>
<line x1="166" y1="507" x2="92" y2="521" stroke="#999" stroke-width="0.8"/>
<text x="20" y="550">nail blade (tip A),</text><text x="20" y="563">edge R 0.3, attack 45°</text>
<ellipse cx="203" cy="539" rx="72" ry="33" fill="none" stroke="#c60" stroke-width="1.5" stroke-dasharray="5 3"/>
<line x1="163" y1="561" x2="243" y2="561" stroke="#c60" stroke-width="4"/>
<text x="20" y="608" fill="#c60">tip loop 48 × 22 mm (dashed orange); contact chord 27 mm (solid), drag → +x;</text>
<text x="20" y="622" fill="#c60">entry 25°, exit 48° at 42% of peak speed, lift 18 mm above skin, depth setting 4 mm</text>
<rect x="560" y="52" width="180" height="130" fill="#fafafa" stroke="#333"/>
<text x="566" y="66" font-weight="bold">plan view (x →, y ↑)</text>
<rect x="576" y="78" width="154" height="40" fill="#eee" stroke="#666" stroke-dasharray="3 2"/>
<text x="580" y="92" font-size="9" fill="#666">crank compartment, y = 40–70:</text><text x="580" y="104" font-size="9" fill="#666">motor · crank arm · rod · rocker</text>
<line x1="640" y1="118" x2="640" y2="136" stroke="#333" stroke-width="4"/><text x="646" y="132" font-size="9">L-hanger</text>
<rect x="576" y="136" width="120" height="34" fill="#eef" stroke="#336"/>
<line x1="586" y1="144" x2="616" y2="144" stroke="#000" stroke-width="2"/>
<line x1="586" y1="154" x2="616" y2="154" stroke="#000" stroke-width="2"/>
<line x1="586" y1="164" x2="616" y2="164" stroke="#000" stroke-width="2"/>
<text x="622" y="156" font-size="9" fill="#336">shroud, 3 blades @ 20</text>
<text x="566" y="178" font-size="9" fill="#555">shell window 110 × 80 under the bay only</text>
<text x="20" y="646" font-size="10">Force path: scalp → blade → TM1 holder → leaf (preload 0.15 N + 0.21 N/mm, hard stop 8 mm → F_max 1.8 N per nail)</text>
<text x="20" y="660" font-size="10">→ TPU hinge + magnet detent (yields ≈ 0.5 N tangential) → comb bar (magnet breakaway 3–5 N) → L-hanger → rod → crank → motor (current cap).</text>
<text x="20" y="674" font-size="10">Hair sees only blades, leaves, moving shroud, fixed skirt and shell; all rotation ≥ 44 mm above the scalp, in the closed compartment beside the bay.</text>
</svg>

---

## 4. Summary
**SP1-A "FEED-DOG" (CCR-3):** one N20-class gearmotor turns a 20 mm crank arm whose 100 mm connecting rod, guided by a 40 mm rocker and running beside the rake, carries through an L-hanger a three-nail comb bar on independent 0.2 N/mm leaf springs; the nails trace a 48 × 22 mm loop that touches the scalp along a 27 mm chord, enters at 25°, leaves at 48° while still moving forward, and lifts 18 mm clear every cycle; an AS5600 on the crank lets the ESP32 shape drag speed, return speed, pauses and stroke-to-stroke jitter with the one motor. Force is a mechanical constant (0.15 + 0.21 × travel, stop at 8 mm → 1.8 N/nail); intensity is a depth thumbscrew; every joint sits ≥50 mm above the scalp inside a housing behind a moving shroud. Build ≈ $270 (≈ $335 with test gear), ≈ 30 hands-on hours, 420 g head-worn on a hard-hat ratchet. Hair checklist 32/36, no gating zero; red lines 7/8 partial. Biggest risk: it is a one-patch machine; if location unpredictability is what keeps a scratch from habituating, this rig proves the contact physics and hands the pattern problem to SP2.
