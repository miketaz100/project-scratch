# LEAP 2 · AGENT F — The skeptic who proposes leaps

**Project SCRATCH · 11-leaps/round-2 · 2026-10-02**
Provocation: find the biggest hidden flaws in the pressure-gated orbit on a small travelling pad, quantify each, and for each propose the leap that removes it rather than a patch.
Inputs per LEAP2-BRIEF, plus redteam-1/2 in full and leap-C §C2 (fallback only). Firewall kept.
Tags: **[KNOWN]** sourced in the cited project file · **[EST]** computed here (script in scratchpad, arithmetic shown) · **[UNKNOWN]** only a bench answers it.

---

## 0. Verdict in five sentences

The strong idea is P × A: a constant-force, capped, fail-vent pin, which survives every attack below and even neutralises two feared flaws (umbilical tug, valve latency). The weak idea is the **circle**: its "rake" returns 28–35 mm away on different hairs and turns the nail 60–90° inside every bite. The circle also makes the hair-facing shell wind any strand it carries, once per revolution and cumulatively, and puts a 1–2 Hz rotating push into whatever holds the pad. Separately, "vent = lift" makes every stroke-rate landing a 20 mm drop, which is either a 0.5–0.85 N tap or too late for its window. The four leaps keep P × A and phase gating and replace the circle, the orbiting skin, park-per-stroke and the single rigid carrier.

---

## 1. Flaw ledger

| # | Flaw | The number that matters | Severity | Likelihood | Leap that removes it | Cheapest test |
|---|---|---|---|---|---|---|
| F1 | Arcs read as "circling"; the "rake" is not one | Heading turns **60–90°** per bite (finger: 22–29°); return stroke **28–35 mm** from the outgoing one (P1: 0) | major: loses P1, Red Team 1's rank-1 fix | 0.45 | **L1 Precessing racetrack** | $0 forearm stencil; $10 eccentric swap on the Leap-2 bench |
| F2 | The orbiting underside and open bores wind hair | **1,257 mm²** enclosed per rev (≈ 2,500 shafts): a carried strand gains **60–120 wraps/min, cumulative** | major (S2–S3, matting) | 0.1 at ≤ 5 cm hair; 0.45 at 5–8 cm | **L2 Still skin, tilting pins** | wig head, orbiting plate vs still dome, 5 min |
| F3 | Park depth vs window: a tap or a late landing | 20 mm in 30–40 ms = **500–670 mm/s**, 76–79° stab, **0.46–0.85 N for 2–4 ms**; throttled to 25 mm/s it is 0.8 s late | major | 0.7 | **L3 Hover-and-bite pin** | scale, 240 fps phone, ink tip on moving paper |
| F4 | "A stamp moving": every simultaneous pin has the same velocity | 0 % speed, 0° direction spread; a hand ≈ ±12 %, 10–20° convergence [EST] | minor–major | 0.35 [UNKNOWN] | **L2** lever stagger + **L4** counter-orbiting halves | helper: rigid ruler-rake vs curling fingers, blind |
| F5 | Reaction and vibration conducted to the skull | Rotating **0.06–0.47 N** at 1–2 Hz (80–150 g, r 20); 0.1–0.5 N friction reaction; gearmotor 2–4 cm from bone | major for the "machine" reading | 0.5 | **L4** (inertia cancels, ÷20) + drive kept above the still dome | pins-parked null test |
| F6 | The umbilical | **43–145 g/m** (12–40 tubes), 0.1–0.35 N pull; **1,800–3,600 barb flexes/session** if tubes ride the orbit; 0–0.5 mm inter-tube gaps | minor for force (P × A rejects it); major if the bundle touches hair | 0.6 nuisance / 0.15 hazard | **L2** (tubes land on the non-orbiting dome) + a vertical boom drop | hang the real bundle, slide the pad ±60 mm on a scale |
| F7 | Failure states | Kinked tube defeats desk sensor *and* vent; stuck valve + running orbit = loaded circles 60–120/min | major (S3) | low per hour, high over the program [EST] | **§4 fail-limp layer** | fault injection on the wig head |

**Not flaws, on inspection.** (1) *Valve latency:* the orbit's phase is measurable, so gates fire early by the measured latency; it costs only a minimum window (~80 ms), and its ±5–10 ms jitter is welcome. (2) *Curvature as such:* a 60° arc at r 20 has a 2.7 mm sagitta, far below scalp two-point acuity (15–40 mm); what the skin feels is the heading rotating and the lanes splitting (F1). (3) *Umbilical tug on force:* a pin open to a rail pushes P × A at any extension, so a pad pulled 2 mm off the head changes nothing.

---

## 2. The arithmetic behind each flaw

**F1, circles.** At r 20 a 60° window gives a 20.0 mm chord, a 2.7 mm sagitta and a 60° turn; a 90° window gives 28.3 mm, 5.9 mm and 90°. A 30 mm chord turns 97° at r 20, 74° at r 25, 44° at r 40 and 29° at r 60. A finger arcing about the knuckles at R 60–80 turns 22–29° [EST]. **A larger radius fixes curvature only at r ≥ 60 mm, a 120 mm orbit bigger than the pad.** The deeper problem: leap-B's bidirectional rake uses windows at φ ≈ 0 and φ ≈ 180°, which are opposite sides of the circle. The two strokes run in parallel lanes 2r·cos(Δφ/2) = 28–35 mm apart, so the return never re-crosses the hairs the outgoing stroke bent. That is not P1. It is P3, a circular rub with gaps, which the pattern spec disables by default. Every contact of a pin also lies on one 40 mm ring, and neighbours firing 100–150 ms apart (the apparent-motion optimum) give the brain the dots of a circle to join [EST].

**F2, winding.** A strand carried around a closed path encircles every shaft standing inside it once per revolution. A reciprocating carrier's winding swings back and forth and returns to zero; an orbit's accumulates. A perforated plate rubbed in circles over hair is how a "twist sponge" coils short hair [KNOWN product class]. Parked pins leave 7 mm bores open below the shell: lawful statically (> 3 mm), but each is a moving hole that catches standing, static-charged hair (§3.6). At 5–8 cm the pile is 10–25 mm against a ≥ 25 mm standoff, so contact is intermittent, not hypothetical.

**F3, landings.** A pin open to 3 ml is a 0.055 N/mm gas spring (0.077 adiabatic), which is excellent for hair and irrelevant to the landing. Descent is what matters: 0.77 ml of swept volume fills through a 1.5 mm × 1 m tube in 20–30 ms, so the pin falls at 500–670 mm/s. A 2 g pin at 0.6 m/s on 300–1,000 N/m of scalp gives v√(km) = **0.46–0.85 N in 2–4 ms**, a Pacinian-band tap on every bite, at a 76–79° stab where H-5.3 asks ≤ 30°. Throttled to 25 mm/s it arrives 0.8 s late. **Park depth (15–25 mm, demanded by F2) against window time (110–250 ms) has no setting that satisfies both.**

**F4, stamp.** In P1 the wrist is shared, but fingers flex about different centres. Tip speed scales with finger length (little finger ≈ 0.75–0.8 of the middle, about ±12 %), and paths converge 10–20° [EST; scratch-model §4.2]. A translating carrier gives 0 % and 0°, the definition of a comb (Red Team 1: P 0.6). Phase gating differentiates only pins that are down at *different* times.

**F5, reaction.** m·ω²·r at r 20: 80 g gives 0.06/0.14/0.25 N at 1/1.5/2 Hz; 150 g gives 0.12/0.27/0.47 N. On a 4.5 kg head that is 0.01–0.1 m/s², around the low-frequency vestibular threshold (order 0.05–0.1 m/s² [EST, recall; verify]). It is felt mostly as a rotating push at the forehead pad or band (48 units/cm²): Red Team 1's "the forehead feels the rhythm", made rotary.

**F6, umbilical.** A 2.5/1.5 mm PU tube weighs 3.6 g/m with EI ≈ 42 N·mm², so bending is negligible (~4 mN for 50 mm over 300 mm) and weight dominates: a 0.3–0.5 m span of 16 tubes puts 0.1–0.35 N on the pad, varying 15–50 % with travel [EST]. Tubes on the orbiting carrier flex every barb ±20 mm: 1,800–3,600 cycles per 30-minute session, about 10⁵ a month. A loose bundle's 0–0.5 mm inter-tube gaps are H-4.9's worst band if it ever lies in hair.

---

## 3. The leaps

### L1 — PRECESSING RACETRACK: two counter-rotating eccentrics make a thin ellipse whose axis drifts

**(a) Assumption broken.** "A drive that never reverses must trace a circle, and per-stroke direction needs the circle."

**(b) Principle.** Sum two eccentrics turning in **opposite** directions: z(t) = r₁e^{+iωt} + r₂e^{−i(ωt−δ)} is an ellipse with semi-axes r₁ + r₂ and |r₁ − r₂|, axis at δ/2. With r₁ = 10, r₂ = 7 the tip runs a **34 × 6 mm racetrack**; neither motor ever reverses. Slip motor 2 and δ advances, so the racetrack **precesses**: 0.05 Hz of slip turns the axis 9°/s (the pattern spec's ±20° per 3 cycles), and jittering the slip makes it a random walk. Pins bite only on the straight flanks; the end turns (radius b²/a = 0.5 mm, 19–38 mm/s) happen at hover, so no nail reverses under load. Co-rotating motor 2 (one reversal per episode, at a P5 pause) turns the same hardware into a circle of radius 3–17 mm: P3/P4 flicks survive as a *mode*.

```
 TOP VIEW, tip path. r1 = 10, r2 = 7  →  34 × 6 mm racetrack (r = 20 circle shown for scale)

     .  -  -  -  -  -  -  -  -  -  .            heading inside a bite: ≤ 30°  (circle: 60–90°)
   /      .────────────────────.     \          lane offset out vs back: 6 mm (circle: 28–35 mm)
  |      (  ═══ bite out ═════►  )   ← 6 mm      63 % of each revolution is within ±15° of the axis
  |       '────◄═══ bite back ═'      |          end turns R 0.5 mm, 19–38 mm/s, gate at hover
   \            ←── 28 mm ──→        /
     ' -  -  -  -  -  -  -  -  -  '             axis angle = δ/2; motor-2 slip 0.05 Hz → 9°/s drift

 SIDE (stacked eccentrics, all above the guard)
  [N20 #1]─ecc r1 = 10 (CW)─►[intermediate plate on 3 flexure posts: translates, no spin]
                                 └─[N20 #2 rides it]─ecc r2 = 7 (CCW)─►[drive plate; Oldham link: no spin]
  AS5600 magnet encoder on each shaft ($3): phase for gate feed-forward and for δ
```

**(c) Sensory variables moved.** Restores P1 on one lane (Red Team 1's "make it rake"): heading change in contact 60–90° → ≤ 30°, return offset 28–35 → 6 mm. §7 rank 1: direction drifts continuously and never repeats, for free. Rank 8: axis set per region (against the lie on the occiput). Rank 9: 10–28 mm by window. Follicle drive, 3 pins on both flanks at 1.5 Hz: 3 × 2 × 28 × 1.5 × 10 ≈ 2,500 hairs/s vs ~1,800 for 60° circle windows, now inside human P1's 2,000–4,000 [EST].

**(d) Plausibility.** Torque is a few mN·m; a second N20 + encoder adds ~$12 and ~15 g (10 g orbiting, counterweighted). Peak tip speed a·ω = 107/160/214 mm/s at 1/1.5/2 Hz, so H-5.4's 200 mm/s caps it at ~1.8 Hz [EST]. One-motor alternative: a Cardan (Tusi) planetary with an off-rim pin, precessed by a slow stepper on the ring gear.

**(e) Cheapest experiment.** *$0, 30 min:* a paper stencil (40 mm ring, 34 × 6 mm racetrack) on Michael's forearm; a helper draws with one nail, blind and randomised: gated circle arcs, racetrack flank bites, a straight 28 mm back-and-forth. Ask "back and forth, or going round?" and "fingers, 0–10". *$10, an evening:* an r₁/r₂ hub pair on leap-B's Leap-2 bench, fixed cam-ring gating, ink traces, then blind A/B on the crown.

**(f) Replaces / combines.** Replaces the single eccentric and keeps phase gating. L2–L4 all sit on it.

**(g) Why it might not work.** Per-pin *direction* independence is gone (simultaneous pins rake along one axis, as fingers do in P1; P4 scatter lives only in circle mode). Slip-precession needs both encoders or the axis leaves the grain map. A 6 mm loop may still feel like a loop; b can shrink to 3 mm (r₂ = 8.5) at the cost of slower end turns.

---

### L2 — STILL SKIN, TILTING PINS: the hair-facing surface never orbits; only the nails do

**(a) Assumption broken.** "The part that orbits is the part that faces the hair." In leap-B the whole shell, bores and all, circles above the canopy.

**(b) Principle.** The pad's underside is a **stationary** smooth, drafted dome that moves only with the pad's 2–5 cm/s travel (a monotonic translation, hair-positive per H-5.7). Each pin passes through it at a **bonded silicone diaphragm pivot** (leap-B L3's sealed pivot). Above the dome the L1 drive moves a plate carrying each pin's upper end in a ball-slide; the tip traces the plate's path mirrored and scaled by L_below/L_above. The air piston lives in the tilting sleeve; the pin exits it through the pin-unit's wiper-lip seal.

```
 SECTION (stroke = page X)                          plate moves +x ─►
   ════════o═══════════════o═══════════════o════  drive plate (L1), ball-slides; above dome, out of reach
           │╲ L_above 30   │ 36            │╲ 42   ← per-pin lever stagger
           │ ╲             │               │ ╲
   ▓▓▓▓▓▓▓▓●▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓●▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓●▓▓▓▓  STILL DOME, silicone diaphragm pivots ●
           │  ╲ L_below    │               │  ╲    28 mm standoff (≥ pile + 10, H-4.5)
           │   ╲ 25–35     │               │   ╲   tilt ±25° at the ends, ±16° inside bite windows
           ▼    ▼ tip −x × L_below/L_above ▼    ▼
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  hair / scalp
   tip ratio across pins: 1.00 / 0.83 / 0.71, plus ±17 % from extension (L_below 30 ± 5) as the pad travels
```

**(c) Sensory variables moved.** F2: orbiting hair-facing area goes from 75,000 mm²/min (circle, 1 Hz) to **zero**; only nails orbit, biting or hovering on L1's 160 mm² racetrack (hair checklist items 3 and 12 → 2). F4: simultaneous pins differ in speed by **15–40 %**, re-drawn as curvature changes under the travelling pad (rank 6, now in velocity), and radial pins converge a few degrees. F6: tubes land on the dome and never orbit. F5: orbiting mass falls from 80–150 g to 30–40 g, rotating force ÷3.

**(d) Plausibility.** Tilt lifts the tip 2.8 mm at the ends; the constant-force piston just extends, and normal force varies by cos 16° = 0.96 inside windows. Attack angle 45° ± 16° stays inside 3.11f's 25–65° [EST]. Diaphragm duty ~10⁵ tilts per 60 sessions; pump membranes run ≥ 10⁶ [EST], the bond line is [UNKNOWN]. ~$10.

**(e) Cheapest experiment ($15 + a $15 Kanekalon wig, the conservative screen of hair §7.1, trimmed to 6–8 cm).** Leap-2 bench, 1.5 Hz, 5 min per arm: **A** orbiting flat plate with three open 7 mm holes at 25 mm standoff; **B** still dome, three dummy pins through finger-cot diaphragms, tips hovering 5 mm. Photograph, count twists, measure comb-out force with a luggage scale. Pass: B at baseline.

**(f) Replaces / combines.** Replaces the orbiting shell underside. L1 drives the plate, L3's piston sits in the sleeve, L4 splits the plate.

**(g) Why it might not work.** Two seals per pin double the leak and fatigue sites; the ±16° attack swing may read as a flick; hovering tips still trace the racetrack in the pile (L3 (g)); +25 g.

---

### L3 — HOVER-AND-BITE PIN: two travel scales, a friction-follower collar, gates fired ahead of phase

**(a) Assumption broken.** "Lift = vent = park, at stroke rate," and "latency is the limit."

**(b) Principle.** Each pin gets three states from the same 3-way valve plus a vacuum rail.
- **PARK** (vacuum, −8 kPa ≈ −0.31 N): 20 mm up, out of the canopy. Used at episode boundaries, region changes and at least every 15 s (DR7).
- **HOVER** (vent): the 0.05 N return spring lifts the pin only until it meets a **split-PTFE collar** riding in the bore at 0.08 N of friction, through a 5 mm lost-motion slot. The collar holds, so the pin hovers **5 mm above wherever it last touched**, whatever the seating.
- **BITE** (rail): the pin drops ≤ 5 mm. If the scalp has fallen away, it pushes the collar down, losing 0.08 N on that one stroke.

Gates fire early by each pin's measured latency, using the eccentric encoders. Latency then costs only a minimum window of about 80 ms.

```
  bore 7 mm   ┌────┐ bladder ← rail / vent / vacuum (desk valve)
              │▒▒▒▒│
              ├────┤ pin head
   collar ►  ═╡    ╞═  split PTFE ring, 0.08 N friction in bore
              │ ↕5 │  lost-motion slot pin↔collar; return spring 0.05 N
              │    │
              ▼ nail: BITE drops 5 mm in 60–80 ms; HOVER sits 5 mm up in the pile; PARK 20 mm up
```

**(c) Sensory variables moved.** Descent 5 mm in 60–80 ms = 62–83 mm/s: a **26–33° plough-in** at 126 mm/s (H-5.3: ≤ 30°) instead of a 76–79° stab. Landing transient 0.46–0.85 N → **0.05–0.08 N**: §8 item 5's tap and Red Team 1's "tapping" are gone, and force ramps over the 10–20 ms fill while moving, as a nail lands. Unload takes 30–60 ms, inside §3.10's 50–120 ms. A tip hovering 5 mm up still bends hair near the root (0.17 mN per hair, §2.3), so component A continues between bites [EST]. Air per bite ÷4.

**(d) Plausibility.** The 0.03 N holding margin (0.08 collar vs 0.05 spring) is thin: spec collar friction 0.07–0.10 N over humidity. BP-pump inlets pull ≥ −30 kPa [EST]. The collar is in the force path only on strokes where it moves (~20 % jitter, welcome).

**(e) Cheapest experiment ($5 on leap-B's three-pin bench).** Add the collar; ink the nail; pull paper under it at ~125 mm/s. A 20 mm drop leaves a dot then a streak, a hover-bite a tapered entry. Kitchen scale + 240 fps for landing peak; then blind on the forearm: "tap or stroke?"

**(f) Replaces / combines.** Replaces vent-to-park at stroke rate and keeps the rails, relief cap and fail-vent. It needs L1: hovering tips on a 1,257 mm² circle would stir, but on a 160 mm² racetrack with PARK every ≤ 15 s they are within H-5.2's "≥ 5 mm with zero force" clause.

**(g) Why it might not work.** Collar wear and humidity drift hover height. Hover tips in the pile are what leap-B (g)(1) feared; the bound is 8× less enclosed area, not zero. If the wig shows winding, hover rises to 8–10 mm and the plough angle steepens to ~40°.

---

### L4 — COUNTER-ORBITING HALVES: a finger plate and a thumb plate in exact antiphase

**(a) Assumption broken.** "One pad, one rigid carrier." That single assumption causes both the stamp (F4) and the rotating reaction into the head (F5).

**(b) Principle.** Split the drive plate in two. The *finger* plate (3 pins) is driven by L1. The *thumb* plate (1–2 pins, mass-matched) is driven through a **stick passing through a ball pivot** fixed to the dome, which maps (x, y) to (−x, −y) for any path. Gating rule: both halves bite together only on **converging** flanks (fingers curling toward the thumb); on diverging flanks one half hovers.

```
   ═══o═══o═══o═══   finger plate (3 pins) ◄── L1 drive
            │
            ●  ball pivot on the dome frame: (x, y) → (−x, −y)
            │
        ═══o═══       thumb plate (1–2 pins), mass × lever-arm matched
   nearest finger–thumb nails: 50 mm at mid-phase, 22–78 mm over a cycle (never < 3 mm)
```

**(c) Sensory variables moved.** F5: inertia cancels (residual couple 0.25 N × 40 mm ≈ 0.01 N·m vs a 0.25–0.47 N rotating force), and friction reactions cancel on converging bites [EST]. F4: two opposite velocity groups (relative 2v) plus L2's lever spread give the converging "hand closing" signature of scratch-model §4.2: §7 rank 6 and component C.

**(d) Plausibility.** ~$3, ~15 g. A strand bridging converging nails goes slack. Physical backstop for the diverging case: a nail at 0.4 N with hair µ ≈ 0.25 grips a strand with ≤ 0.1 N, below the 0.36 N pluck floor, so it slides out unless hooked [EST].

**(e) Cheapest experiment.** *$0:* helper, blind, 10 trials on the crown: one-hand rake vs "curl-to-thumb" rake. *$5:* pins parked, bench on a band, phone accelerometer: can Michael (eyes closed, ears plugged) tell when the orbit runs, single plate vs counter-orbiting?

**(f) Replaces / combines.** Replaces the single carrier. With L1–L3 it completes the pad.

**(g) Why it might not work.** Convergence may read as *pinching*. The diverging rule is firmware, backed only by the friction bound. Each half carries fewer pins.

---

## 4. Failure states (F7): the fail-limp layer

| State | As drawn in leap-B | Physical fix (not firmware) |
|---|---|---|
| **Kinked or pinched tube** (head leans on the umbilical) | Pin traps 10 kPa and stays down; the desk sensor reads vent (blind); the orbit drags it. **Worst case; leap-B misses it.** | **Bleed orifice at every pin** (30 G needle stub, ≈ 0.15 mm): trapped air falls below 0.08 N in < 1 s whatever the tube does; costs 0.4 L/min for 5 pressed pins, inside one BP pump [EST]; hiss ducted into the dome. |
| **Valve stuck to rail** | Loaded circles at 60–120 per minute: H-5.7's forbidden pattern and 3.24's 50 passes/min | Sensor/command mismatch > 1 cycle opens the NO **dump valve** and cuts orbit power on one relay; the stuck valve vents through the emptied rail. |
| **Burst or herniated bladder** | Limp (safe), rail sags; latex at 40 kPa can herniate into the 0.2 mm gap | A rolling diaphragm or a piston "hat" wider than the clearance; flow alarm on the regulator. |
| **Power loss mid-travel** | Pins go limp, not reliably lifted (0.05 N spring vs 0.01–0.03 N friction) | Limp meets RL-8; L2's dome presents no open bores |
| **Firmware hang** | Valves hold the last state while the orbit runs | Valve and motor power through a charge-pump watchdog relay (needs a toggling GPIO) in the e-stop loop |
| **Pad stalled at the temple / near the ear** | Global rail puts 0.39 N where ≤ 0.15 N is the rule; RL-6 rests on firmware | **Mechanical travel fence** (hard stops behind the hairline, ≥ 25 mm from the ear canal) + **region-keyed relief**: a cam on the travel axis sets a second relief valve to ~4 kPa (0.15 N) near temples and nape. The force map is a cam. |

---

## 5. Best bet: L1 + L3, "bite on the flank"

Red Team 1 showed the rating is made in the first 20 seconds, by motion signature, and the two flaws that decide it are F1 (the circle cannot rake) and F3 (park-per-stroke makes every bite a 0.5–0.85 N stab). L1 and L3 remove both for one extra N20, two printed hubs and a $1 collar per pin. The racetrack makes the orbit a true back-and-forth rake on one lane with ≤ 30° of heading change, whose axis drifts without ever repeating because two motors slip against each other. Hover-and-bite turns every landing into a 26–33° plough-in with a 0.05 N transient, keeps hair moving near the root between bites, and makes latency irrelevant by firing ahead of a measured phase. Nothing leap-B got right is lost: force is still P × A, the cap is still a relief valve, the fail state is still vent, the motors still never reverse, and every pin still picks its windows per stroke. L2 is the build gate before any session in hair over 5 cm; L4 follows only if the null test shows the orbit through the mount. The first three tests (stencil, hub swap, collar-and-ink) cost under $25.

---

## 6. If this direction fails

**Most likely reason (P ≈ 0.35): the clock shows through.** Even with racetracks and random windows, every landing sits on a phase of one motor's 1–2 Hz cycle, at that motor's speed, by pins sharing its velocity. Gating randomises *which* pieces of the cycle touch, not the cycle, and scratch-model §4.3 says a periodic carrier is found in 10–30 s. Next: in Michael's actual hair, hover/park forces a choice between stirring and stabbing (P ≈ 0.25); 12–40 lines leak, kink and fatigue faster than an apartment build tolerates (P ≈ 0.15).

**Fallback: round-1 contender C2, the METACHRONAL RAKE (leap-C),** carrying leap-B's air pins if benches 1–2 passed (springs if not). It keeps Michael's small travelling patch on one crank and answers the most likely failure directly: each nail has its own phase and so its own instantaneous velocity (up to 190 mm/s apart), lift-before-reversal is geometric, and the stems pass through bellows boots, so no hair-facing surface orbits. Its known risk, formication, has a $15 four-SG90 test. If the pneumatics are what failed, the next fallback is leap-F's scalp spider (per-leg actuators, gravity force, no tubes).
