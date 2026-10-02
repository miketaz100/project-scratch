# LEAP 3-D: A helmet Michael wants to put on every evening

Leap-3 agent D · Project SCRATCH · 2026-10-02 · Provocation: a helmet that is light, comfortable, quiet and pleasant.
Read: LEAP3-BRIEF; leap2-A (§0–1, L1, L2), leap2-B (L4), leap2-C (§0, C1, §5), leap2-D (P2 sweeps), leap2-E (all), leap2-F (L3, L4, §4); safety §1 H13/H21–23, §2.6–2.7, §7, §8; hair-interaction §1.3, §6; scratch-model §3, §7; crown concept-A §1.4–4, §6–7. Firewall kept (no other round-3 files).
Tags: `[KNOWN]` sourced · `[EST]` computed here, arithmetic shown · `[UNKNOWN]` only a test answers it.

---

## 0. What decides whether he puts it on

Round 2's honest helmet (leap2-E §2) weighs **455 g**, carries two motors and an inner shell, and E predicted "after the first month, never the helmet." Four things settle evening use, in order: **what he hears** inside his skull; **steps and seconds** to being scratched; **the tug** of hose and leaning hat; and **mass**, which matters mostly through the tug (300–350 g is a bicycle helmet).

The finding that drives this report concerns noise. **Bone conduction is the deciding noise path, and it is frequency-selective.** ISO 389-3 reference thresholds for bone-conducted force at the mastoid are about **67 dB re 1 µN at 250 Hz (≈ 2.2 mN), 42.5 dB at 1 kHz (≈ 0.13 mN) and 31 dB at 2 kHz (≈ 35 µN)**. The forehead is roughly 10 dB less sensitive `[KNOWN, values from memory; check]`. The ear is therefore about **60× more sensitive, in force, at 2 kHz than at 250 Hz.**

- **Slow travel is in the deaf band.** A geared servo turning the travel axes at 2–9 rpm puts its gear mesh at roughly 90–450 Hz.
- **The orbit motors are in the sensitive band.** An N20 driving the orbit at 2–3 Hz spins at 12–18 krpm, which puts brush and mesh tones at 1–3 kHz. On the pad it is coupled straight into the scalp through the nails and palm skids.

So the rule is: **slow motors may ride the helmet; fast motors may not.** Leap D2 follows directly from it.

---

## 1. Structure options, with numbers

| Option | Mass `[EST]` | Stiffness per gram | Heat and sweat | Sound | Hygiene | Verdict |
|---|---|---|---|---|---|---|
| Hard-hat suspension | 110 g | n/a | band ~60 cm² | quiet | washable | **rear band sits on the occipital bun** (concept-A §5) |
| Bike retention with dial | 30–50 g | needs a frame | ~35 cm² pads | quiet | removable pads | **cradle hooks under the inion, bun free**: keep |
| Thermoformed PETG shell, 1–1.5 mm | 80–120 g | good | 600 cm² air layer, +1–2 °C `[EST]` | **drums** | wipeable | reject; shroud the pad only |
| Printed lattice dome | 120–180 g | poor | open | lively | **porous crevices** (safety §8) | reject |
| **Carbon tube frame** (10 × 8, 0.044 g/mm) | 30–60 g | best | open | rings; butyl under heat-shrink (+3 g) | wipeable | **keep** for the bail |

---

## LEAP D1: THE SKELETON HALO. A bike-helmet dial cradle, one carbon bail on ear-axis hubs, no shell (≤ 350 g)

**(a) Assumption broken.** That a head-worn travelling pad needs a hard-hat suspension, an inner hair-shedding shell and motors riding the moving arcs. It needs none: the bike cradle grips *under* the occipital bun; the pad's drafted shroud already meets H-6.3 and the bail stays ≥ 55 mm up, outside the 30 mm zone; both motors sit at static hubs, the carriage driven by a tendon inside the hollow bail.

**(b) Principle and sketch.** Leap2-A's L1 bail, transplanted onto the head:
- **Bail:** carbon arc, R 165 about skull centre O, pivoting on the ear axis. **Hubs** at |Y| = 115 mm, 45 mm above the ear canal: ≈ 64 mm from it (red line 6: ≥ 25) and ≥ 15 mm outboard of the helix.
- **α** (left hub servo): −30° (frontal hairline) to +95° (occipital bun). **β** (right hub servo): carriage ±55° via a 0.5 mm Dyneema loop inside the tube; the coaxial pulley couples α into β and firmware cancels it.
- **Zero-length (Anglepoise) spring** from a post 35 mm above each hub cancels the bail's gravity torque, head upright.
- **Head interface:** front half-band (Al 20 × 1.5 mm or PA12) hub to hub over a forehead pad 45 mm above the brows; a bike-retention **dial cradle** hung from the hubs, closing under the inion.

```
 FRONT (α = 0, bail over the vertex)                SIDE (bail swings about the ear axis ●)
          carriage ▣  β ±55°                                 α=0  ▣
      .-~~~~~~~~~~~~~~~~~~~-.   bail R165 (carbon 10×8)   .-~~~~~~|~~~~-.
    .'     pad ▼▼▼ (≥55 mm    '.  tendon inside tube   .'     ▼▼▼      '.   α=+95°
   /     .-""""""""""-.  up)    \                     /  .-"""""""""-.   ▣◀ pad on the bun
  [α]●━━━━━━━━━ O ━━━━━━━━━━━●[β]  hubs |Y| 115     |  /    O ●      \ ◀▼|
   |  |   R 75–100    |         |  spring post ↑35   brow ═╗          /   |
      ╚═ forehead pad ═╝ (brow +45 mm, 45×35, 1 W warm)     ╚═ band ═ cradle (dial) under inion
   width at hubs ≈ 250 mm, at the bail ≈ 290 mm; vertex clearance 70 mm   bun free ≥ 60 mm above cradle
```

**Mass ledger (8 pins; the 16-pin variant adds 28 g):**

| Part | g |
|---|---|
| Front half-band | 25 |
| Forehead pad (TPU, foam, washable sleeve, 1 W heater) | 12 |
| Dial cradle, harvested from a $20 bike helmet | 35 |
| Two hubs (688 bearings, sealed housing, TPU grommets) | 24 |
| Two travel servos (XL330-M288 class, 18 g each) | 36 |
| Bail, carbon tube with legs and nodes | 31 |
| Carriage (no motor) | 12 |
| Springs, tendon, pulleys | 8 |
| **Pad** with D2 slave, palm skids and radial piston | 82 |
| Chin elastic with magnetic fuse | 12 |
| Umbilical plug at the left hub | 18 |
| Head-borne share of the umbilical (D3) | 8 |
| Head-side wiring and fasteners | 15 |
| **Total** | **318** (16 pins: **346**) |

This is 455 → 318 g, below the brief's 350 g target.

**(c) Variables moved.**
- **Mass** −137 g (−30 %). **Gravity moment** of the moving 94 g (pad + carriage, CoM at 135 mm): 0.094 × 9.81 × 0.135 = **0.12 N·m** (E: 0.15).
- **Coverage:** pad centre α −30…+95°, β ±55°, plus the ±24° footprint: ≈ 450 cm², ~75–80 % of the hair-bearing scalp, **including the occipital bun** (the hard-hat band covers it). Lost: lower occiput, nape (cradle), temples.
- **Contact area** ≈ 56 cm² (forehead 16, cradle 20, two temple pads 20), ~8 % of the head above the brow; a bike helmet covers 20–30 % `[EST]`.

**(d) Plausibility.**
- **Pitch hold, pad at the back:** the helmet tries to roll back about the cradle, forehead pad sliding up. Dial load ≈ 6 N on the forehead × µ 0.3–0.5 on a 180 mm lever = **0.32–0.54 N·m**, margin **2.7–4.5×** `[EST]`. The chin elastic (1.5 N per side, 12 ± 3 N magnetic fuse, concept-A §3.3) is lift-off retention only.
- **Servo heat:** unbalanced, α holds 0.18 N·m (35 % of XL330 stall): ≈ 0.5 A, 1–2 W in an 18 g case by the temple, **failing ≤ 43 °C** (§2.6) `[EST]`. Spring-balanced, the residual at ±20° head pitch is 0.18 × 2 sin 10° ≈ **0.06 N·m**: ~0.15 A, ≤ 0.2 W.
- **Travel speed:** drift 2–5 cm/s ≈ 2–5 rpm; P2 sweeps at 80 mm/s ≈ 8 rpm. Motor 550–2,400 rpm, first mesh 90–400 Hz: the band where bone conduction needs millinewtons (§0).
- **Orbit reaction:** 30 g plate, r 15 mm, 3 Hz → 0.16 N rotating; on ≈ 1 N/mm pad shear, ~0.16 mm of sway, about what a hand does to a head.

**(e) Cheapest experiment (≈ $30, a weekend).** A $20 bike helmet; weigh it whole and the retention harness alone. Tape a stick across the top and hang a **94 g coin bag 135 mm from the ear axis**. Wear 20 min watching TV, moving the bag front/top/back/sides every 2 min. A phone inclinometer on the helmet against a second on a headband gives pitch slip, with and without a 1.5 N chin elastic. Hair-clip the cradle's top edge and measure the free bun. **Pass:** slip ≤ 3°, no pressure spot at 20 min, ≥ 60 mm of free bun.

**(f) Replaces or combines.** Replaces E's suspension, inner shell, twin arcs and carriage-borne motors. Needs leap2-A L2 (palm datum) and D2.

**(g) Why it might fail.** Without a top contact, the band may **yaw** under β drag at 55° (0.1 N·m about Z); the temple pads in the ledger are the fix. A 290 mm halo may read as "apparatus," not a hat `[UNKNOWN]`. Bike cradles must be adapted to custom hub mounts.

---

## LEAP D2: THE AIR PANTOGRAPH. The path synthesiser lives behind the chair, and the pad copies it through three sealed lines

**(a) Assumption broken.** That the binding two-stage path synthesiser (leap2-B L4: r1 = r2 = 7.5 mm, Oldham, two one-way N20s with encoders) must ride on the pad. It must not, because it is the only fast motor on the head (§0).

**(b) Principle.** Build leap2-B L4 exactly as specified, in the box behind the chair (D3). It drives a **master plate** carrying three Ø22 bellows at 120°. Three sealed 4/2.5 mm PU lines, 0.7 m long and charged to 15 kPa, run to three identical **slave bellows** around the pad's pin plate, which hangs on four flexure legs (leap2-C C1). The total volume is constant, so the slave plate copies the master's (x, y): line, circle, precessing line or heading jump, exactly as the synthesiser draws them. A brake-master compensating port re-zeroes leaks at top dead centre. The pad holds pins, bellows, flexures and plastic. **No motor, no wire, no heat.**

```
 CHAIR-BACK BOX                                        PAD (on the scalp)
 N20 ─► stage 1 ─Oldham─ stage 2 (B-L4, encoders)       B1 Ø22
          master plate ── M1 Ø22 ══ line 1, 0.7 m ══╗      ║
                       ── M2 Ø22 ══ line 2 ═══════╗ ╚══ ┌──╨───────┐
                       ── M3 Ø22 ══ line 3 ═════╗ ╚═B2 ─┤ 8–16 pins├─ B3   slave plate on
 charge 15 kPa, compensating port, relief +8 kPa║       └──────────┘      4 TPU flexures
 path: line 30 mm │ circle r = 15 cos(δ/2) │ precessing line │ heading jump   copied 1:1
```

**(c) Variables moved.**
- **Sound at the head:** the N20s' 1–3 kHz tones are gone. An N20 gearmotor is ≈ 45–55 dBA at 10 cm `[EST]`, and on the crown it sits 100–150 mm from the ear. Worse, the pad touches the scalp through 8–16 nails and three skids: coupling even 1 mN at 2 kHz is ~30 dB above the bone-conduction threshold, heard *inside* the head `[EST]`. Sealed bellows run at room level.
- **Pad mass:** N20s with encoders, six MR63 bearings, Oldham disc, upper plate and wires (≈ 43 g) become bellows and flexures (≈ 14 g): **−29 g at 135 mm**, ~25 % less gravity moment.
- **Heat and hygiene:** two 0.3–0.5 W motors leave the pad, and with the pin cassette out the pad is rinseable.

**(d) Plausibility (Ø22 bellows, A ≈ 3.8 cm²).**
- **Stiffness:** gas volume ≈ 3.4 ml line + 4 ml slave + 2 ml master ≈ 10 ml; k = P_abs·A²/V = 116 kPa × (3.8 cm²)²/10 ml ≈ **1.7 N/mm per line**, ≈ 2.5 N/mm across the plate. Copy error under 0.5 N of drag: **0.2 mm**. A 30 g plate resonates at √(2500/0.03)/2π ≈ **46 Hz**, far above the drive.
- **Flow:** a 30 mm line at 3 Hz peaks at 0.28 m/s, 107 ml/s per bellows. Poiseuille loss 128µLQ/πd⁴ ≈ 1.4 kPa over 0.7 m in a 2.5 mm bore; Re ≈ 3,500, so call it **2–3 kPa** against a 15 kPa charge. A 1.5 m desk run doubles it, one reason for D3. Air inertance ≈ 0.7 kPa (water: ~600 kPa, so not water).
- **Cost and umbilical:** ≈ $15 over the synthesiser. Three more tubes: with the palm piston and lock lines, **13 tubes + a 3-core servo bus, ≈ 12.5 mm**.

**(e) Cheapest experiment (≈ $35, a weekend).**
1. **Copy fidelity:** three 20 ml syringes on a hand-moved plywood master plate; three Ø20–25 suction-cup bellows at 120° under a printed slave plate on four TPU legs; 0.7 m of 4/2.5 line each; a pen on each plate. Drive the master along a ruler and round a jar lid at 1, 2 and 3 Hz (metronome app). **Pass:** slave trace within 1 mm of the master.
2. **Noise:** tape a $4 N20 (100:1, at 120–180 rpm) to a worn bike helmet's crown. Phone SPL app at the tragus (A, slow): motor on, off, and slave cycling; then again with foam earplugs. Whatever remains is bone-conducted, and the on/off contrast cancels the occlusion effect. **Pass:** slave indistinguishable from off.

**(f) Replaces or combines.** Keeps leap2-B L4's kinematics, encoders and modes untouched, off the head; realises leap2-C C1 with circle *and* line. With leap2-F L4, an antiphase slave group is only three more lines.

**(g) Why it might fail.** Bellows may buckle sideways or fatigue at ~11,000 cycles per session (C1's risk). Flexure yaw drags pins sideways (needs an X-flexure or a printed Sarrus). In line mode not every master passes TDC, so the compensating port may not re-zero; a needle-valve equaliser may be needed. Fidelity at 4 Hz is `[UNKNOWN]` until the pen test.

---

## LEAP D3: THE CHAIR IS THE STATION. Valves behind the headrest, the umbilical held at nape height, the head (not the helmet) on a nape roll

**(a) Assumption broken.** That the helmet's support system is a desk box and a hose to the body, and that the right use of a headrest is to carry helmet weight.

**(b) Principle.** One high-back chair (wingback, recliner or gaming chair) becomes the base. Sketch, side view:

```
          helmet ─ plug at L hub ─╮ 250–350 mm free loop, LOOSE tubes in knit sleeve
   wing hook (dock) ◄──┐          ╰─► hose-lift whip on headrest post ─► magnetic breakaway 15–20 N
                       │                                         │
   nape roll (U-pillow, 80–100 mm) under the cradle line         ▼ 0.7 m
   chair back ────────────────────── VALVE + SYNTHESISER BOX (foam-lined, sorbothane) strapped behind
   armrest: palm-rest pad = hold-to-run (3 N closes it); e-stop beside it
   floor, 2 m: pump + 1 L reservoir + 40 kPa relief in a foam box, inlet muffler (supply latency irrelevant)
```

**(c) Variables moved.** The table compares four valve locations.

| Valve location | Tube to pad | Tube latency | Head or shoulder mass | Valve clicks at the ear `[EST]` | Umbilical |
|---|---|---|---|---|---|
| Desk box (round 2) | 1.2–1.5 m | 5–6 ms | 0 | ≈ 20–25 dBA | 13 tubes, 12.5 mm, sags to the floor |
| Neck pack | 0.2 m | ~1 ms | **+125 g on the head** (16 × 5 g S070 + manifold + drivers) | **40–50 dBA**, 60–80 mm from the ear, plus a bone path | 6 mm |
| Shoulder yoke | 0.3 m | ~1 ms | +150–250 g on the shoulders | 30–40 dBA at 150 mm | 6 mm |
| **Chair-back box** | **0.7 m** | **≈ 3 ms** | **0** | **≤ 20 dBA** (−15 dB foam, −17 dB distance, −5 dB chair padding) | 13 tubes, held at nape height |

Latency barely matters: swept volume dominates at 20–30 ms (leap2-C §0). Noise and the hose decide, and the chair-back box wins both.

**Umbilical torque, the real tug.** One 2.5 mm PU tube has EI ≈ 30 MPa × 1.67 mm⁴ = 50 N·mm²; thirteen loose tubes plus the cable ≈ 1,700 N·mm². A 60° head turn bends the 300 mm loop to R ≈ 200 mm: M ≈ EI/R ≈ **0.009 N·m**. The *same tubes bonded* into one 12.5 mm rod (tight spiral wrap, ties every 50 mm, or expandable braid that cinches under tension) have EI ≈ 30 MPa × π/64 × 12.5⁴ ≈ 36,000 N·mm²: **0.18 N·m**, more than the pad's whole gravity moment. **Rule: tubes loose in a loose knit sleeve, never tied or braided tight.** At ≈ 80 g/m, the whip leaves the head carrying 8–12 g; draped to a desk, 40–55 g plus tug.

**The headrest question.** Should the headrest carry part of the helmet's weight? **No: it should carry the head.** The helmet's 3.1 N is **7 %** of the 45 N head, and neck fatigue is holding the head. On a nape roll reclined 20–30°, neck extensor load is near zero and the helmet's weight passes through the head into the roll. Docking the helmet itself on the headrest is worse three ways: it puts 15–22 N through the cradle (5–7 kPa, over the 5 kPa pad limit); it blocks the occiput; and at α ≈ 90° the bail is a horizontal half-ring 70 mm behind the occiput at O height, exactly where a headrest sits. So a U-shaped nape roll, 80–100 mm thick under the cradle line, holds the occiput ≥ 80 mm off the chair back, giving ≥ 10 mm bail clearance at α ≤ 75° `[EST, test]`. **Lean-back mode caps α at 75°** (crown, top, sides, upper bun); sitting up unlocks +95°. A 1 g tilt switch in the hub reads the mode, and a servo current spike stops the bail if it touches the chair.

**Hold-to-run.** A palm-rest pad on the armrest, closed by a resting hand (3 N): rest the hand and it runs, lift it and the pins lift, with no button gripped for 20 minutes. A sleeping hand stays resting, so the 20-min session timer (safety H13) is the sleep backstop.

**(d) Plausibility.** Parts: a CPAP hose-lift whip (≈ $20) or bent coat hanger, a $15 U-pillow, and leap2-B's desk box moved. The magnetic port block (leap2-E L3) at the headrest post breaks away at 15–20 N if he stands up wearing the helmet. Unplugged, every pin vents and lifts, the pantograph plate centres on its flexures, and servo power drops so the bail goes limp.

**(e) Cheapest experiment (≈ $40, an evening).** Two 1.5 m dummy bundles of 13 × 4 mm PU, one loose in a knit sleeve, one tied every 50 mm, clipped to the D1 bike helmet. Turn 60° against a luggage scale on a 100 mm lever (torque); hang the free end from a kitchen scale (head share); repeat draped to the floor and on a coat-hanger whip. In the chair with the U-pillow, measure the occiput-to-chair gap. **Pass:** loose ≤ 0.02 N·m, head share ≤ 15 g, gap ≥ 80 mm.

**(f) Replaces or combines.** Replaces the desk box and draped hose; realises leap2-E L3's "unplug = lifted" at the chair; makes D2's 0.7 m lines possible.

**(g) Why it might fail.** It ties evening use to one chair (the couch needs a clamp-on version). Chair padding passes low-frequency thumps from the box. A partner may veto a box and a whip on the good chair.

---

## LEAP D4: THE TWO-SECOND RITUAL. A dock on the chair wing, a warm brow, one click, a pad parked at the crown

**(a) Assumption broken.** That donning is fitting. With the dial set once and the helmet living plugged in on the chair, donning is just putting it on.

**(b) Principle.**
- **Dock:** the helmet hangs by its front band on a hook on the left chair wing, plugged in, pad **parked at the vertex (α = 0, β = 0)** so its CoM is centred when lifted.
- **Don:** lift by the brow tab, one hand; seat forehead first and rotate back (the preset dial cradle flexes 10 mm under the bun); the keyed magnetic chin fuse self-locates with a click.
- **Warm brow:** the forehead pad holds **34–35 °C** on 1 W (thermistor loop, 40 °C bimetal cut-out, under §2.6's 41 °C). It reads as a hand on the forehead, the second hand a person scratching often places.
- **First touch:** all pins land at 0.1 N on a 0.5 s ramp, 3 s without motion (leap2-E L4).
- **Doff:** lift the resting hand (pins vent and lift in ≤ 100 ms, pad returns to the vertex); pull the brow tab (fuse releases at 12 N after 60 mm of elastic); hang it on the hook.
- **Cleaning:** the nails come out as one **snap-in pin cassette** (two sets, IPA-wiped, 1 min flash-off, §8); a removable merino or terry sleeve over closed-cell foam (two, washed weekly); a drafted PETG shroud with a tool-free shed-hair audit (H-6.7). No open-cell foam, no unsealed print on skin.

**(c) Variables moved.**
- **Time and steps:** don ≈ 3 s, doff ≈ 1.5 s (concept-A: ~6 s don) `[EST, test]`. E counted seven helmet steps (shelf, plug, don, ratchet, chin fuse, sit upright, hold switch); here four: lift, seat, click, rest the hand.
- **Component E** (warmth, someone present) comes from the brow with no extra actuator.
- **Sound:** with D2 and D3 the loudest thing at the ear is nails in hair, a mostly bone-conducted broadband hiss the brain expects. The device must not mask it. **Target: every machine source ≥ 10 dB below the nail hiss and ≤ 25 dBA at the ear.**

**(d) Plausibility.** The 16 cm² pad loses ≈ h·A·ΔT = 10 × 0.0016 × 13 ≈ 0.2 W through its outer face, so 1 W is ample. Insensible sweat under it at rest is ≈ 0.02–0.03 g/h `[EST]`. The open skeleton adds ≈ 0 °C at the scalp (a shell adds 1–2 °C). About 2.5 kPa of band pressure for 20 min leaves a crease at the brow and under the bun, acceptable for an evening device.

**(e) Cheapest experiment (≈ $10).** Hook on the chair, 94 g bag at the vertex of the D1 dummy. Ten don and ten eyes-closed doff trials on a phone stopwatch. Warm brow: a microwaved wheat pack in a sock (≤ 40 °C on a $10 IR thermometer) under the band, 2 × 5 min with a partner scratching, warm against room temperature, rating "being cared for" and pleasure 0–10. **Pass:** don ≤ 3 s, doff ≤ 2 s, warm ≥ room.

**(f) Combines** with D1–D3, folding leap2-E L4's arrival and departure ritual onto a head-worn device.

**(g) Why it might fail.** A warm brow under a hat may read as a fever compress, not a hand. The chin click is one step more than a pillow. If the cradle must be loosened to pass the bun, don time doubles.

---

## LEAP D5 (radical alternative): THE PASSIVE HELMET. Travel by sealed water lines, so nothing on the head is powered

**(a)** That travel needs motors on the helmet. **(b)** Each travel axis becomes a pair of antagonistic **rolling-diaphragm** slaves at its hub, on water-filled 4/2.5 lines from masters in the chair box (Whitney et al., IROS 2014, rolling-diaphragm hydrostatic transmission `[KNOWN, from memory]`). With D2 and air pins, the helmet has **no wire, no heat, no electronics** and could be rinsed under a tap. **(c, d)** PU wall compliance for 1.5 m of line is dV/dP ≈ 2.5 × 10⁻¹² m³/Pa, so a Ø20 slave gives k = A²/(dV/dP) ≈ **39 N/mm**. The spring-balanced 0.06 N·m on a 15 mm pulley is 4 N: 0.1 mm of sag, ≈ 1 mm at the pad. Inertance is trivial at travel speed. Mass ≈ +15 g against servos; head noise zero. **(e, $15)** Two 10 ml syringes, 1 m of bubble-free water line: kitchen-scale stiffness, then push the master at 2 cm/s and film the slave at 240 fps. Syringe seals have 1–3 N of stiction `[EST]`, so jerks would mean diaphragms are mandatory. **(f)** Replaces both servos and all head wiring. **(g)** Eight rolling diaphragms at $25–40 each; bubbles kill stiffness; a leak is water in the hair; stick-slip would read as the hand "jumping." Keep it as the route if the D1 servos prove audible or hot.

---

## 2. Noise budget at the ear (best bet, D1–D4)

| Source | Where | Path | Fix | At ear `[EST]` |
|---|---|---|---|---|
| Orbit synthesiser (N20 ×2, 1–3 kHz) | chair box | air through foam, 0.7 m | D2: off the head | ≤ 20 dBA, no bone path |
| Valves (S070 ×8–16 clicks) | chair box | air | foam + sorbothane | ≤ 20 dBA |
| Pump (63 dB at 30 cm bare) | floor, 2 m | air | foam box, muffler, reservoir duty-cycling | ≤ 25 dBA |
| Exhaust puffs (1.1 ml per landing) | box exhaust | air | sintered silencer inside the box | ≈ 0 |
| Travel servos (90–400 Hz mesh) | hubs, 64 mm from the ear canal | **bone via the band** + air | slow, spring-balanced, TPU grommets (f_n ≈ 25 Hz gives −20 to −30 dB in practice) | 20–30 dBA; bone path below 250 Hz threshold `[UNKNOWN: PWM whine]` |
| Constant pin bleed (leap2-F §4) | pad | air, 5 cm | use end-of-stroke bleed (leap2-E L1 d) instead | ≈ 0 |
| Creak of printed joints at the 3 Hz reaction | hubs, band | bone | no sliding joints at the band; PTFE at the hub; butyl in the carbon | must be 0: the cheapest signature of "cheap" |
| Umbilical rustle on the collar | nape | bone | held off the shoulder by the whip | ≈ 0 |
| **Nails in hair** | scalp | bone + air | keep, never mask | the only thing he should hear |

**Test protocol** (phone SPL app at the tragus, A, slow; night room ≈ 25–30 dBA): each source alone; (2) all on, pins parked; (3) all on, scratching; then earplugs in, on against off, so whatever remains is bone-conducted. **Pass:** (2) within 3 dB of the room, (3) clearly louder than (2).

---

## 3. Best bet: D1 + D2 + D3 + D4. The skeleton halo with an air-pantograph pad, run from the chair

**The case.** With the helmet mandatory, what makes it the thing Michael reaches for at 10 pm is being **silent inside his skull, ~320 g, and on in three seconds**. All three come from one move: **take everything fast or heavy off the head and put it in the chair.** The binding path synthesiser is built exactly as leap2-B L4 specifies, but in a foam box behind the headrest, driving the pad through three sealed air lines (D2). The only kHz motors, in the band where bone conduction needs tens of micronewtons, never touch the scalp. The valves share the box on 0.7 m of tube (≈ 3 ms, unfeelable), and 13 loose tubes hang from a nape-height whip: 0.009 N·m against a head turn, where bonded tubes would give 0.18. What stays on the head is a skeleton (D1): a bike dial cradle gripping *under* the occipital bun, freeing the region the hard-hat band covered; one carbon bail on ear-axis hubs reaching ~75–80 % of the hair-bearing scalp; two slow, spring-balanced hub servos (≤ 0.2 W, meshing below 400 Hz); and an 82 g pad of plastic, bellows and pins. That is **318 g (8 pins) or 346 g (16), against E's 455**, with a 0.12 N·m gravity moment. The headrest should carry his head on a nape roll, not the helmet, which weighs 7 % of the head and would block the occiput and hit the bail. The ritual (D4) is: helmet plugged in on the chair wing; lift, seat, click, rest the hand; a warm brow and a 0.5 s first touch; lift the hand and the nails lift. Every risk has a sub-$50 weekend test with a $20 bike helmet, coins, kitchen and luggage scales, earplugs and a phone. Pass lines: slip ≤ 3° with 94 g swinging; loose bundle ≤ 0.02 N·m; pen trace within 1 mm at 3 Hz; slave inaudible with earplugs where a crown-mounted N20 is not; don ≤ 3 s. If the hub servos prove audible or hot, D5 removes the last powered part from the head.
