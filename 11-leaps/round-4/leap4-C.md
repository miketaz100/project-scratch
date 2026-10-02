# LEAP 4-C: Mass and structure. A skyhook, box-driven travel and a feather chassis

Leap-4 agent C · Project SCRATCH · 2026-10-02 · Provocation: cut head-borne mass by 30–50 %.

**Read:** LEAP4-BRIEF; DECISION-2 (incl. the north-star amendment); decision-analysis; SYSTEM-SPEC §0–1, §3, §4.6–4.7, §5.1; redteam-2 §4, §5, §7; redteam-3 (bail, tools); leap3-A, leap3-D; safety red lines; hair-interaction §5–6; scratch-model §3, §7–8. Firewall kept (no other round-4 file).

**Tags.** [KNOWN] = from a project file or a cited vendor page. [EST] = computed here; scripts are `12-sp1v2/scripts/mass_leap4c.py` (part-by-part ledger, calibrated to `mass.py`: it reproduces 386.4 / 369.5 / 480.1 g) and `12-sp1v2/scripts/skyhook.py` (moment and line-clearance model on the spec's head ellipsoid, 1,326 pose × head-move cases). [VERIFY] = a scale or bench answers it. [JUDG] = judgement.

---

## 0. Where the baseline's grams are

The baseline is the 6-pin hybrid with must-fixes and the bent Al bail. With RT2's light head-side lines it is **369.5 g single** (386.4 g with normal lines) and **480.1 g twin**, which needs light lines and the whole §4.7 ladder [EST, `mass.py`].

| Block | Parts | g (single) | Share |
|---|---|---|---|
| Retention | front band 20, forehead pad 10, dial cradle 30, temple pads 6, doff handle 8 | 74 | 20 % |
| Travel | hub pods 36, STS3032 ×2 41, tendon/idlers/balancer 6 | 83 | 22 % |
| Bail | Al 10 × 1, bent, with nodes, splice and guide | 58 | 16 % |
| Moving group | pad 60.2, carriage 10, float 12, pad fixes ~10 | ≈ 92 | 25 % |
| Plumbing | head-side harness 20.6, umbilical share 15.0, plug/clips 9.1 | 44.7 | 12 % |
| Misc | fasteners 10, twin provisions 4, head switch and filters ~4 | ≈ 18 | 5 % |

Two facts set the strategy.

1. **The moving group (≈ 99 g per pad, including jumpers) is the one block a mass leap should not touch.** It is the scratch. The twin carries two of them, so no structural leap can take the twin down 50 %.
2. **Everything else is either a motor, or holds up a motor, a tube or the moving group.** Remove the reasons to carry those things and the structure that carries them shrinks too.

I also checked what keeps the pad square to the scalp, because every leap below has to preserve it. **Squareness does not come from the bail.** It comes from the RCC palm: three dome skids, pressed by the float, with the RCC lines crossing at the nail plane (C17). The bail has three jobs only:
- react the float's 3–5 N outward;
- hold the carriage tangentially against ±0.5–1.5 N of scrub drag, so the synchro copy is not eaten;
- hold its α/β pose under gravity.

A lighter bail is acceptable if it deflects **≤ 1 mm per N** at the carriage. Today it gives 0.3 mm/N. The synchro already gives 0.5–0.7 mm of copy error, and scalp acuity is 15–39 mm.

---

## C1 — SKYHOOK: the tube bundle drops from overhead straight onto the carriage, on a constant-force line that makes the moving group weightless

**(a) Assumption broken.** That the helmet must carry the pad's plumbing over its own structure (rear node or hub → leg → arc → carriage), and that only a second pad or a dead mass can cancel the single pad's 0.24 N·m lean. The spec's overhead hanger (C22) already holds the umbilical 100–200 mm above the crown. It is holding it at the wrong place, and with the wrong kind of support.

**(b) Principle and sketch.**
- Raise the hanger's tip to **≈ 600 mm above the skull centre O, directly over the head** (X ≈ −10 mm). That is about 510 mm above the crown, a desk-lamp boom clamped to the box, the chair back or the couch back.
- At the tip, a **constant-force reel** (a Negator spring on a drum, or simply an 85 g counterweight over a pulley) pays out a Dyneema line. The pad's 10 pneumatic tubes are clipped loosely along that line.
- Line and tubes land on the **carriage** through a 3 N magnetic breakaway. A 0.12 m jumper loop takes the tubes from the carriage to the pad deck across the 50 mm float stroke.
- Reel force ≈ **85 gf (0.83 N)**. The scan found this optimum; it is a little less than the 99 g moving group, because part of the line pull is always off-vertical.

```
              reel ◉  (hanger boom tip, ~600 mm above O, over the head)
                   │  Dyneema line + 10 loose tubes, 390–734 mm long
                   │
            .-~~~~~▣~~~~~-.   carriage (line lands here, 3 N magnetic)
          .'      ║jumper  '.   bail R 210
         /     pad ▼▼▼       \
   hub ●══════════ O ══════════● hub        no harness on the bail, no rear node
```

**(c) Numbers moved** [EST, part by part; single vs the 369.5 g light-line baseline]

| Part | Before (g) | After (g) | Δ |
|---|---|---|---|
| Head-side harness, 0.62 m along the bail (light lines) | 20.6 | 7.3 (0.12 m jumper in **full 4 mm** lines) | −13.3 |
| Plug, strain relief, clips | 9.1 | 4.0 (carriage clip + breakaway) | −5.1 |
| Umbilical head share | 15.0 | 4.0 (bottom 50 mm of the rising bundle + head-switch wire) | −11.0 |
| **C1 total, physical** | | | **−29.4 g single; twin a further −6.3 net** (second line, harness B deleted) |

- **Static load on the neck** falls by the reel force as well: **−83 g single, −166 g twin** (two lines). I do **not** count this toward red line 10, which counts mass. It does count for comfort and neck torque.
- **Lean** (skyhook.py: worst over every legal pose; upright, ±20° nod, ±45° turn, combined):
  - baseline unbalanced: **0.226 N·m**;
  - feather bail without a reel: 0.198 N·m;
  - **skyhook, hanger tip at (−10, 0, 600): 0.053–0.058 N·m**, a 75 % cut;
  - worst yaw 0.009 N·m.
  - A single pad then leans about as much as the balanced twin does at ±20° tilt (leap3-A: 0.105). **This is the counterweight-free balance the provocation asked for.**
- **Hanger placement matters.**
  - Hanger 100–200 mm behind the crown (spec-like): residual 0.10–0.18 N·m.
  - Hanger tip high and directly above: 0.053 N·m.
  - Line length runs 390–734 mm across all poses and head moves, so the reel needs ≥ 400 mm of stroke.
- **Line clearance.** In all 1,326 pose × head-move cases the line never comes within 8 mm of the bail tube (40 mm round the carriage excluded). The line lands on the outermost moving part, so the bail cannot sweep into it. This also retires RT2 §4.1 (the umbilical inside the bail's sweep) in a second way.
- **Registration and squareness.** Unchanged. The reel pulls on the carriage; the float force between carriage and pad is still set by the palm rail, so the pad's normal load is unchanged. Bundle bending at the carriage is ≈ 0.009 N·m (leap3-D's loose-tube figure), which is ≈ 0.05 N at the carriage, against 1 N of drag.
- **Light lines no longer needed.** RT2's 2 mm-OD head lines existed only to save mass. With 0.12 m of head-side tube there is nothing left to save. Full 4 mm lines restore vent and retract speed (RT2 §5: 270–390 ms through long thin lines), so **one must-fix risk goes away**.
- **Coverage:** unchanged (no new obstruction). **Cost:** +$15 (constant-force spring or pulley, longer boom, line), −$10 (harness clips, rear node) ≈ **+$5**. **Hours:** +4–6 (boom, reel, carriage anchor) −4–6 (RT2's "routed light harness along the bail" must-fix) ≈ **0**.

**(d) Plausibility.**
- The force is small: 0.83 N, which a badge-reel-class spring gives. A counterweight gives it exactly and lets Michael tune it with coins.
- Constant-force springs in the 0.2 lb (0.9 N) class are catalogue items [VERIFY rate and stroke ≥ 400 mm].
- With a counterweight, its inertia adds 85 g along the line. Drift accelerations are tiny (leap3-A: hop impulse 0.035 N·m). Scrub at 1.4 Hz moves the carriage only by bail compliance, ≈ 0.3 mm, so the counterweight's dynamic force is ≈ 0.85 g × 0.0003 × (2π·1.4)² ≈ 2 mN. Negligible.

**(e) Cheapest experiment ($15, one evening).**
1. Use the $20 bike helmet from leap3-D with a stick bail. Hang a 100 g coin bag 135 mm from the ear axis at the occiput pose.
2. Clamp a broom handle to the chair back with its tip 0.5 m above the crown. Run kite string over a curtain-ring pulley to an 85 g coin bag.
3. Measure with a phone inclinometer on the helmet against one on a headband: lean with the line, lean without, ±45° turns, a 150 mm forward lean. Use a luggage scale on a 100 mm lever for tug.
4. **Pass:** helmet pitch slip with the line ≤ ⅓ of slip without; turn and lean tug ≤ 0.05 N·m; "do I feel pulled?" ≤ 2/10.

**(f) Replaces.**
- The rear node and plug.
- The head-side harness and its RT2 must-fix routing.
- The light-line requirement.
- The hub spring balancers (RT3 already deferred them).
- Most of the cradle's job against lean (1–1.5 N·m form lock against 0.24 N·m). The cradle stays for sneezes and drag.

**(g) Why it might fail.**
- **The tether.** A room-fixed line on the helmet is the "tethered to the furniture" feel leap2-E warned about. A 0.83 N pull that swings with head moves may be noticed even when the moment is small.
- **Height.** A 600 mm boom over the head is furniture-like. On a low couch back it may not reach.
- **Hair.** Long hair draped upward could touch the line. It is ≥ 120 mm from the scalp, but it is a cord.
- **Breakaway.** If he stands up, the reel pays out its full stroke before the 3 N breakaway fires.

---

## C2 — BOX-DRIVEN TRAVEL: no motors on the head; pull-pull Dyneema in common housings from steppers in the drive box

**(a) Assumption broken.** That the travel motors must ride the head because a Bowden is soft and lossy. leap3-A L4 rejected neck-yoke Bowdens at 1–2° of backlash and 0.09 N·m of yaw push-back from three 5 mm housings. Both numbers belong to **single-strand** Bowdens, whose housing compression changes with load.

**(b) Principle.**
- Each axis is a **closed pull-pull loop**: two 1 mm Dyneema strands inside **one** common housing, with both ends on a drum.
  - At the box, a NEMA 17 drives an R 10 drum (GT2 3:1 if needed) with a spring preload tensioner (T₀ ≈ 10 N).
  - At the hub, the loop wraps an **R 25–30 mm sector** on the bail shaft, for α; or the spec's Ø 20 β drum, which drives the carriage tendon.
- The drive changes the strand tensions to T₀ + ΔT and T₀ − ΔT. **The housing load is 2T₀ whatever the torque**, so the housing never changes its compression with load.
- A head turn bends both strands' paths equally, so to first order **the hub does not move when the umbilical flexes**. Surgical cable drives work this way.
- **Single:** both axes terminate at the **right** pod (α and β are coaxial there already). Both housings leave with the ear-axis umbilical, as RT2 asked.
- **Twin:** the left half-bail's α needs a third housing, routed 0.3 m behind the cradle.
- **Holding.** A wave-spring PTFE friction washer on each hub (≈ 0.08 N·m) holds the pose when the steppers are unpowered. With C1 the residual is ≤ 0.06 N·m, so the bail cannot free-fall (leap3-E 8c).

**(c) Numbers moved** [EST]

| Part | Δ single (g) | Twin, extra |
|---|---|---|
| STS3032 ×2 | −41.0 | α_R servo −21 |
| Motor bays and cartridge plates in the pods | −6.0 | −3 |
| Servo bus wire on the head | −3.0 | −1.5 |
| Housings, 2 × (0.175 m umbilical share + 0.03 m route) at 30 g/m [VERIFY 15–42 g/m; Nissen 4 mm ≈ 42 g/m] | +12.3 | +14.3 (0.475 m) |
| Terminations, R 30 sectors, hub friction brakes | +5.0 | +2.5 |
| **C2 total** | **−32.7 g** | **−8.8 more** (−41.5 g for the twin) |

- **Stiffness and registration.**
  - 1 mm Dyneema has EA ≈ 27 kN [EST], so the loop gives 2EA/L = 38.6 N/mm at the drum.
  - On an R 30 sector that is **34.7 N·m/rad**. Scrub drag of ±0.10 N·m then moves the carriage **±0.6 mm** (±0.37 mm at the nail plane). The static C1 residual of 0.06 N·m sets a 0.36 mm offset.
  - On R 25 the figures are 0.87 and 0.5 mm.
  - Friction hysteresis at a travel reversal (preload 10 N, µ 0.1, ~2π of total bend) is ≈ 0.2 mm at the drum, **≈ 1.5 mm at the carriage**. That is harmless for drift, and smaller than the 4° fence margin.
  - Scrub-frequency drag (±3 N) is below the strand friction (≈ 9 N), so at scrub frequency the cable sticks in its housing and only the hub-side length stretches: stiffer still.
- **Noise.** The servo-hum and gear-hunting path into the parietal bone (RT1 #6, MUST; spec risk R6, P 0.30) is deleted. So are the servo current-limit tuning, gear bias and the gimbal fallback cartridge. Nothing on the head is powered except the head-present switch.
- **Coverage:** unchanged. The R 30 sector makes the pod ≈ 10 mm larger in Ø [VERIFY against the ±40° β stop].
- **Cost.** +2 NEMA 17 ($22), +2 TMC2209 ($10), housings and Dyneema ($25), printed drums; −2 STS3032 and their bus adapter (≈ $55). Net ≈ **±$10**; the twin saves one more servo.
- **Hours.** +8–12 (box drive module, tensioners, sector routing); −6–10 (STS bus, IDs, current limits, gear bias, servo zero jig). Net ≈ **+2**.

**(d) Plausibility.**
- Drive torque: with C1, about (0.06 + 0.11 N·m) / 0.03 m = 5.7 N of ΔT. With T₀ 10 N and a friction amplification of ~1.9, that is ≈ 30 N at the box drum, **0.3 N·m at R 10**. A NEMA 17 pancake holds 0.13 N·m, so add a 3:1 GT2.
- Cable speed is only 7 mm/s at 30 mm/s drift, the regime where UHMWPE on PTFE is least prone to stick-slip.

**(e) Cheapest experiment ($25, a weekend).**
1. Lay 1.4 m of 4 mm shift housing with two 1 mm Dyneema strands between two printed Ø 60 drums. The output drum carries a 210 mm pointer and a 100 g coin bag at 130 mm.
2. Turn the input by hand (or the master's spare stepper). Swing the housing through ±60° and through a 180° loop, as a head turn would.
3. Measure with a ruler at the pointer tip and a luggage scale on the input drum.
4. **Pass:** ≤ 1 mm pointer shift when the housing is flexed; ≤ 2 mm lost motion at reversal; ≤ 1 mm/N tip stiffness; no stick-slip visible on phone slow-motion at 7 mm/s.

**(f) Replaces.** The two (three) STS3032s, their bus and cartridge bays, RT1 #6's servo fixes, spec risk R6 and the M3 cartridge interface.

**(g) Why it might fail.**
- Dyneema creeps, so preload decays. It needs a box-side spring tensioner, and pose truth needs a home switch at each hub, which brings back one wire.
- Housing friction may make 20 mm/s drift jerky ("it won't glide"). The fallback is steel 7 × 7 strand on PTFE liners.
- The twin's third housing must cross behind the cradle. It is static and sheathed, but it is in the hair zone at the occiput ridge.

---

## C3 — FEATHER CHASSIS: a polygon carbon bail with printed nodes, a carbon band, no balancers

**(a) Assumption broken.** That the bail must be a smooth bent tube (RT3: carbon cannot be bent, so Al 10 × 1 at +18 g), and that retention can only be cut by buying lighter retention.

**(b) Principle.**
- **Bail.** Build the R 210 arc as **six straight carbon 8 × 6 chords of 20.7° (75 mm each)** plus two legs, bonded into **seven printed lattice nodes** (PA12 or PETG, 25 mm sockets).
  - The vertex node *is* the twin splice.
  - A pultruded **carbon 3 × 1 strip**, bent elastically to R 210, is bonded to the node crowns as the carriage's rolling track. Its strain is 0.24 %, far inside carbon's limit, and a spline over the nodes is smooth.
  - The polygon's 3.4 mm sagitta is absorbed by the float's 25 mm radial budget.
  - No bending form, no bending spring, no kinks.
- **Front band.** A 20 × 1 pultruded carbon strip (elastic bend to the forehead, 0.5 % strain) replaces Al 20 × 1.5. It matches in-plane stiffness: EI 8 × 10⁷ against 7 × 10⁷ N·mm².
- **Doff.** The doff handle becomes a moulded lip on the band's centre node.
- **Forehead pad.** Thinner closed-cell foam.
- **Balancers.** Deleted (C1 balances).

**(c) Numbers moved** [EST]

| Part | Before (g) | After (g) | Δ |
|---|---|---|---|
| Bail | Al 10 × 1, 58 | 8 × 6 carbon 0.69 m × 34 g/m = 23.5; 7 nodes × 1.5 = 10.5; track strip 2.2 → **36.2** | **−21.8** |
| Front half-band | Al 20 | carbon 20 × 1, 8 | −12 |
| Forehead pad + sleeve | 10 | 6 | −4 |
| Doff handle | 8 | lip on the node, 3 | −5 |
| Balancer parts | 3 (of 6) | 0 | −3 |
| **C3 total** | | | **−45.8 g single.** For the twin, −30.8 beyond what the ladder already took (thin cradle −10, balancers −5). |

- **Stiffness.** Carbon 8 × 6 gives EI ≈ 1.65 × 10⁷ N·mm², against 2.0 × 10⁷ for Al 10 × 1. Tip deflection is ≈ 0.35 mm/N against 0.3, well inside the 1 mm/N budget of §0.
- **Bought retention is not the lever.** A Petzl Sirocco climbing helmet is 160–170 g whole ([Petzl](https://www.petzl.com/US/en/Sport/Helmets/SIROCCO)), with its OMEGA headband not sold separately. A full Giro Roc Loc fit system is listed at about 3 oz ≈ 85 g ([Excel Sports](https://www.excelsports.com/giro-roc-loc-5-fit-system)). The baseline already uses a harvested 30 g bike cradle. Only ≈ 20 g is available in retention, and it comes from the band and trim, not from a purchase.
- **Coverage:** unchanged. **Cost:** carbon tubes 2 m ($25), strips ($15), resin; −Al tube, bending spring and form (≈ $30). Net ≈ **+$10**. **Hours:** cutting and bonding 7 nodes takes ≈ 4–6 h, against RT3's bend-and-splice at 6–8 h, so **−2 h**. One fewer precision job (the R 210 bend).

**(d) Plausibility.** These are 1 m pultruded 8 × 6 tubes of the drone-frame kind. Bonded socket joints with 25 mm engagement and epoxy carry far more than the 5 N float reaction. The track strip over seven nodes is how kite and tent spars hold curves.

**(e) Cheapest experiment ($35, a weekend).** Buy the tubes and strip; print the nodes on a 1:1 paper template of R 210. Bond, then weigh on the kitchen scale (**pass ≤ 40 g**). Clamp at the hub nodes and hang a 100 g coin bag at the vertex; measure the drop with a ruler (**pass ≤ 0.5 mm**). Roll the carriage over the track by hand (**pass:** no felt bump at the nodes).

**(f) Replaces.** RT3 2.7 (hand-bent Al, +13–23 g), the bending tools, the Al band and the balancers.

**(g) Why it might fail.**
- The track strip may peel at nodes under roller load.
- Carbon tubes crack at sharp node edges if the sockets are not chamfered.
- Carbon conducts. The spec wants skin-contact metal isolated from the 6 V ground; with C2 there is no 6 V on the head anyway.

---

## C4 — BAIL-LESS (tested and rejected): pad on the band, cables between the hubs, a net track

I give the numbers because the provocation asks for them and because "delete the bail" is the obvious 50 % idea.

| Variant | Fatal number [EST] |
|---|---|
| **Carriage running on the halo band** | The band sits at brow, temple and occipital-ridge height (Z ≈ −20…+30 mm). Reaching the vertex (Z 88) needs a ≥ 150 mm boom that pivots, which is the bail again. The carriage would also pass within 25 mm of the ear canals and run above the eyes (red line 6). |
| **Tensioned cable hub-to-hub, carriage riding it** | Radially it works: at the vertex T = 5 N / (2 sin 60°) = 2.9 N. But the far-side chord passes **104 mm from O at β = 0** (16–27 mm above the scalp, **inside the 30 mm hair zone**, H-6.1). It passes 86 mm from O at β = 20° (on the scalp) and **64 mm at β = 40° (through the skull)**. When the float retracts the cable goes slack and the pad drops onto the scalp: red line 8. |
| **Cable-driven parallel robot from halo anchors** | Anchors at scalp level put the cables in the hair zone. Opposite-side anchors put the chord through the skull at the bun. Standoff posts high enough to clear are a frame heavier than the bail (leap3-A: ~250 g shell). |
| **Fabric or net track** | A net in the hair zone is the textbook hair trap (H-6.1). A net held at R 210 needs a frame at least the bail's mass. |

**What this proves.** The ear-axis bail is the lightest legal spherical positioner. The mass leap is to make it light (C3) and unloaded (C1), not to delete it. **Cheapest test:** none needed; geometry decides.

---

## C5 — SPEND THE MARGIN (a consequence, not a part)

After C1 + C2 + C3 the twin is ≈ 372 g. That is **128 g under red line 10**, where the baseline had 20 g. The decision analysis chose 6 pins **because of mass** (12-pin twin ≥ 551 g). Under the new chassis, with full 4 mm head lines, Ø 16 slaves and 7.4 g per pin per pad [EST]:

| Pins per pad | Single | Twin |
|---|---|---|
| 6 | 262 | 372 |
| 8 | 271 | 391 |
| 12 | 290 | **429 ✓** |

So the leap re-opens the pin-count decision, and Michael can choose on sensation and cost (≈ $43 per pin), not on grams. It also buys the per-pad valves leap3-A L2 wanted if lockstep reads as a machine: the valves stay in the box; only 6 more tubes, ≈ 5 g on the head under C1.

---

## Best bet: C1 + C2 + C3 ("the unloaded halo")

### Revised mass, part by part [EST, `mass_leap4c.py`]

| Block | Baseline single (light lines) | New single |
|---|---|---|
| Retention (band, forehead pad, cradle, temples, doff) | 74.0 | 53.0 |
| Hub pods | 36.0 | 30.0 |
| Hub motors | 41.0 | 0 |
| Bowden housings, terminations, brakes | — | 17.3 |
| Bail | 58.0 | 36.2 |
| Carriage + float | 22.0 | 22.0 |
| Pad (6 pins) + must-fix hardware | 73.8 | 73.8 |
| Tendon, idlers, balancer | 6.0 | 3.0 |
| Harness / jumper | 20.6 | 7.3 |
| Umbilical share | 15.0 | 4.0 |
| Plug / clip | 9.1 | 4.0 |
| Fasteners, wiring, misc, twin provisions | 14.0 | 11.0 |
| **Total** | **369.5** | **261.6** |

| | Baseline | Best bet | Change |
|---|---|---|---|
| **Single, physical** | 369.5 g (386 with normal lines) | **≈ 262 g** | **−29 % (−32 % vs 386)** |
| **Twin, physical** | 480 g (needs light lines + whole ladder) | **≈ 372 g** (Ø 16 slaves; 384 without) | **−22 %**, margin 20 → **128 g** |
| Static neck load, net of reels | = physical | single ≈ 179 g; twin ≈ 206 g | −52 % / −57 % |
| Worst lean, single | 0.226 N·m | **0.053–0.058 N·m** | −75 %, with no counterweight |
| Powered parts on the head | 2–3 servos | **none** (head-present switch only) | |

**Honest limit.** The twin cannot reach −30 % physically, because its two 99 g moving groups are ≈ 53 % of the new total and none of my leaps touch them. The −30 % twin figure is reached only as static load, through the reels.

### The case

The baseline's head is built to carry three things that need not be there:
- motors, which C2 moves to the box;
- a harness that runs the long way round, which C1 drops straight onto the carriage from above;
- a pad's weight that the helmet must lever against the cradle, which C1 hands to the room.

Once nothing heavy or powered rides the hubs and nothing hangs off the bail but the carriage, the bail can be a polygon of drone tubes on printed nodes (C3). The band can be a carbon strip, and the balancers disappear.

None of this touches the pad, the pins, the synchro, the float or the safety chain. Fail-to-free is still the float spring. The scrub, the force caps and the hair rules are untouched.

The two side benefits are worth as much as the grams:
1. **The bone-conducted servo path is gone.** That retires RT1 #6, spec risk R6 (P 0.30) and the gimbal fallback.
2. **The light 2 mm head lines are no longer needed**, so the slow-vent risk RT2 found goes with them.

The 128 g twin margin turns pin count back into a sensation choice.

### Revised estimate if adopted

| Metric | Baseline | Best bet | Basis |
|---|---|---|---|
| **Head mass** | 370–386 g single; 480 g twin | **≈ 262 g single; ≈ 372 g twin** | §ledger |
| **Parts cost** | $1,450–1,500 + $185 tools | **≈ $1,475–1,530** (C1 +$5, C2 ±$10, C3 +$10, plus a ≈ $10 longer boom; bending tools no longer needed) | §C1–C3 |
| **Hours** | 165–230 | **≈ 165–232** (C1 ≈ 0, C2 +2, C3 −2, plus 2 for the hub home switches) | §C1–C3 |
| **P(full session ≥ 7/10)** [JUDG] | 0.40 | **≈ 0.42** (0.36–0.48) | G3 0.80 → 0.85: servo hum, hunting and hat lean gone; partly offset by tether feel |
| **P(≥ 7/10 within 26 weekends)** [JUDG] | 0.20 | **≈ 0.21** | |

### Order of the cheap tests

All before Stage C orders, about $75 in total:
1. **The C1 coin-and-broom evening.** It decides whether the tether is felt.
2. **The C2 shift-housing drum rig.** It decides whether pull-pull drift glides.
3. **The C3 node-bail weigh-and-sag.**

If C1 fails on feel, C2 + C3 alone still give ≈ 291 g single (−21 %) and ≈ 408 g twin (α registration then carries a ≈ 1.7 mm gravity offset). If C2 fails on smoothness, keep the STS servos: C1 + C3 give ≈ 294 g single.
