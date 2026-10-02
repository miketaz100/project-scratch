# LEAP 3-B — The circle-and-line pad drive, as light and quiet as a helmet allows

**Project SCRATCH · 11-leaps/round-3 · Agent B · 2026-10-02**
**Provocation:** the scrub drive for the travelling pad on a helmet. It must give a circle, a straight line, and (Director's update, mid-task) **the slowly precessing line as the default mode**: counter-rotation with ε ≈ 2.5 % speed difference, so the line turns 180·ε = 4.5° per revolution (2.25° per half-stroke; ε = 5 % gives 4.5° per half-stroke). Clean switching is required, and any drive that cannot precess smoothly is scored down.
**Read:** LEAP3-BRIEF; leap2-A, B (esp. L1, L4), C (C1–C2), D (§1, D1), E (§2, L2), F (L1–L4, §4); safety-requirements §2.6–2.7, §7; hair-interaction §5–6; scratch-model §3, §7; concept-A §3–4, §7. Firewall kept: no other round-3 file read.
**Tags:** [KNOWN] sourced · [EST] computed here (script `l3b.py` in the session scratchpad) · [UNKNOWN] bench only.

---

## 0. The numbers every candidate has to meet

**The path family.** All three modes are sums of two equal rotating vectors, z = r e^{iθ₁} + r e^{iθ₂} with r = 7.5 mm:
- **Line:** θ₂ = −θ₁. Length 30 mm; heading set by mean phase.
- **Precessing line (default):** θ₂ = −(1 − ε)θ₁. At ε = 0.025, a 25 mm stroke bows only **0.16 mm** [EST]: as straight as a ruler.
- **Circle:** θ₂ = +θ₁ + δ. Radius 15·cos(δ/2): **15 / 13 / 10.6 / 7.5 / 3.9 mm** at δ = 0 / 60 / 90 / 120 / 150° [EST].

**Error budget.**

| Error source | Effect on the line [EST] |
|---|---|
| r₁ − r₂ = 0.3 mm | opens a 0.3 mm half-axis ellipse; 0.14 mm bow per 25 mm |
| ±2° phase jitter between stages | 0.26 mm half-axis |
| ±0.2° phase jitter | 0.03 mm |

Anything under ~0.5 mm is invisible next to scalp two-point acuity (15–39 mm).

**Rate.** Peak speed on the 30 mm line is 2πf·15 mm:

| f | Peak speed | Peak acceleration | Within H-5.4 (≤ 200 mm/s, ≤ 2 m/s² in contact)? |
|---|---|---|---|
| 1.0 Hz | 94 mm/s | 0.59 m/s² | yes |
| 1.5 Hz | 141 mm/s | 1.33 m/s² | yes |
| 2.0 Hz | 188 mm/s | 2.37 m/s² (at the ends, where pins are lifted) | yes |
| 3.0 Hz | 283 mm/s | 5.3 m/s² | **no** |

So **any fixed-r synthesiser caps the full line near 2.1 Hz.** Faster grain (3–4 Hz) has to come from small circles (r ≤ 5 mm at 4 Hz gives 126 mm/s), or from a drive whose amplitude can be varied. That is a point in favour of Leap 1 below.

**Loads at the pad** [from leap2-B and F, EST]:
- Stroke drag: 0.3–0.5 N typical, 1 N plough spikes.
- Torque on a 7.5–14 mm crank: about 6 mN·m rms, 15 mN·m peak.
- Inertial shake from a 60–90 g moving pad: 0.14–0.21 N at 2 Hz, 0.57–0.85 N at 4 Hz.

**Helmet budget.**
- The leap2-E helmet is 455 g against the 500 g red line, and that includes a 55 g passive pad. **The whole scrub drive must fit in roughly 45 g, or displace something.**
- Pad top sits 55–60 mm above the scalp (30 mm hair zone plus pins), and every drive adds height above that.
- Noise: the hard limit is 70 dBA at the ear and the target is 60 dBA. The project's real goal is that the hiss of nails in hair is the loudest thing (leap2-C, E).

**Anchor data** [KNOWN, vendor listings]:
- **N20 gearmotors** are sold as 55 / 47 / 38.5 dB grades, and one datasheet says only "≤ 75 dB" ([ineedmicromotors](https://ineedmicromotors.com/choose-right-n20-gear-motor-for-your-project/), [Handson GA12-N20](https://www.handsontec.com/dataspecs/motor_fan/GA12-N20.pdf)).
- **2204 260KV gimbal BLDC:** 24 g, Ø27.9 × 13.1 mm, about 11 Ω, 0.6 A max ([MakerStore](https://www.makerstore.com.au/product/mb-elc-motor-bldc-gim2204/)). That gives Kt ≈ 0.037 N·m/A and Km ≈ 0.011 N·m/√W.
- **GBM2804H hollow-shaft gimbal BLDC:** 51 g with AS5048 encoder, 9 Ω, 0.025–0.034 N·m ([RCTimer](https://www.rctimer.com/rctimer-gbm2804-hollow-shaft-brushless-gimbal-motor-p0445.html)). Km ≈ 0.022 N·m/√W.

---

## 1. The candidates, scored on the same sheet

Noise at the ear assumes the pad is on the crown, 110–130 mm from the ear canal; on the parietal side, at the 25 mm ear fence, add about 6–8 dB. Bone conduction through the helmet shell is UNKNOWN and is not included.

| Drive | Line bow / circle roundness | Circle↔line switch | Precessing line (default) | Max rate | Head mass | Height above pad top | Noise at ear | Heat | Parts cost | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| **(1) Director: 2 N20 stacked eccentrics + Oldham** (leap2-B L4) | 0.14–0.3 mm bow (radius match, ±2° lock); 0.1–0.2 mm gear backlash; circle ±0.2 mm | **150–300 ms**: one N20 must stop, reverse and re-lock | **Yes**, smooth with encoder phase lock; heading jitter about ±1° | line 2.1 Hz; circle r 5 at 4 Hz | **55–60 g** | 45–55 mm | **35–50 dBA** (38–55 dB motor grades at 10 cm, plus a backlash tick at every load reversal) | 0.3–0.6 W | ~$35 | Works; it is the noise floor everyone else must beat. |
| **(2a) Leap2-C C1, all-air synchro, fixed 3-throw crank** | circle only, about ±0.3 mm | — | **No.** A 3-throw crank can make only a circle. | 4 Hz | 25–30 g | ~20 mm | ≈ 0 at head | 0 | ~$25 | **Scored down hard:** no line, no precession. |
| (2b) C1 with three independent desk syringe motors | software paths, but each master reverses: 0.1–0.3 mm kink per reversal | ms | yes, with reversal kinks | 3–4 Hz | 35–45 g | ~22 mm | ≈ 0 at head | 0 | ~$60 | Superseded by Leap 1. |
| **(3) Leap2-E L2, travel motors draw the path** | software, under 1 mm if stiff enough | ms | yes, smooth in software | limited by heat | +60 to +140 g of motor over E's 80 g | arcs 60–70 mm above the scalp | 25–30 dBA | **12–18 W per axis** with 40–50 g gimbals; about 1 W with 110 g 4108-class | ~$60 | **Fails on a helmet** (§2). |
| (4a) **Clutched single-motor Tusi** (Leap 3) | 0.1–0.2 mm bow; circle radius set by when the clutch engages | 0.3–0.7 s (≤ 1 revolution) | **Only stepwise**, by micro-slips of 2–5°. | line 2.1 Hz | **45–50 g** | 30–35 mm | 25–32 dBA, plus a clutch "shh" | 0.3 W | ~$30 | **Scored down** by the precession rule. |
| (4b) **Twin direct-drive Tusi ("ring motor")** (Leap 2) | **< 0.1 mm** bow (±0.2° FOC lock, one plastic mesh); circle ±0.1 mm, radius continuous 0–14.4 mm | **< 50 ms**, no reversal under load | **Best motorised:** the ring turns at 6.75°/s, continuously | line 2.1 Hz | **75–85 g** | 40–45 mm | **20–30 dBA** [EST] | 0.6 W typical, 4 W for a few ms at spikes | ~$55 | **Motorised fallback.** |
| (4c) **Air puppet: replica-master synchro** (Leap 1) | as good as the desk master; **amplitude shrinks 0.4–0.8 mm** under 0.5 N drag; ±0.15 mm lateral | as fast as the desk master (< 50 ms) | **Yes**, exactly as smooth as the master; the tube lag of 2 ms is common to all three lines, so it does not distort the path | **4 Hz, and any amplitude** if the master is an XY | **35–45 g** (+6 g of tube on the head) | **~22 mm** | **≈ 0 at head**; desk box 30–35 dBA at 1 m | **0** | ~$45–70 | **Best bet.** |
| (4d) Voice-coil XY at the pad | excellent in closed loop | ms | yes | 10 Hz | **~250 g** (two ±15 mm voice coils) | 30 mm | ~20 dBA | 0.5 W rms, 5 W peak | $150+ | Reject for the 30 mm line. Keep as a ±3 mm grain idea. |
| (4e) Steel-rod flexure XY guide | — | — | — | — | — | — | — | — | — | Reject. ±15 mm on 50 mm Ø0.6 rods means **2.2 GPa** bending stress [EST]. Use Leap 4's polypropylene hinge instead. |

---

## LEAP 1 — THE AIR PUPPET: three sealed lines copy a desk master plate, so the pad has no motor, no heat and no sound

**(a) Assumption broken.** "Something on the head must *generate* the path." Leap2-C C1 already moved the orbit's power to the desk. But its fixed 3-throw crank meant the head could only copy a circle, and its short bellows could not stroke 30 mm. **The leap is to transmit position, not phase.** Three sealed air lines can copy *any* planar motion of a desk plate onto the head plate. So the path generator can be as big, loud, heavy and clever as we like, because it lives in a foam box. Michael's three modes, ε-precession, variable radius and variable line length all become properties of the desk master. The head carries a passive puppet.

**(b) Principle and sketch.**

*Head side:*
- The **slave plate** (the pad) carries three short **rolling-diaphragm cylinders** (Ø16 mm bore, 2.0 cm², ±16 mm stroke). They lie flat in a **pinwheel**: tangential, at 120°, around a 50 mm circle, on the pad's top deck.
- Each pushes a 30 mm rod with ball ends onto the plate rim.
- Three lines at 120° with tangential offsets fix x, y **and** plate rotation θ, so no separate anti-rotation guide is needed. Leap 4's polypropylene hinge can be added as a backstop.
- The plate rides on three caged 4 mm balls against the deck. The pins' own reaction (1–3 N upward) preloads them.

*Desk side:*
- The **master** is a geometric replica: the same three cylinders, rods and plate, so the rod-angle nonlinearities cancel instead of having to be calibrated out.
- Any motion source pushes the master plate. The default is the Director's two-motor stacked-eccentric synthesiser (noise is irrelevant in the box). A $30 two-stepper XY stage is the alternative, adding variable line length.
- The lines are charged to p₀ = 30–100 kPa through a brake-master-style **compensating port** that opens during each P5 rest, so leaks and temperature drift re-zero every 10–20 s.

```
 DESK (foam box, 30–35 dBA at 1 m)                       HEAD (pad top deck, 22 mm tall, plan view)
  synthesiser (2 motors, any kind)                                  cyl 1 ═╗
     │ drives                                                         rod ╲   ┌───────────────┐
  MASTER plate ── 3 cylinders (replica) ══ 3 sealed lines ═══▶  cyl 3 ═╗   ●══┤  SLAVE plate   │
     │                                     2.5/1.5 PU, 1.2 m          ╲rod  │  = pad, 16 pins │
  p₀ charge + compensating port +           (join the pin bundle)     ●═══┤  on 3 balls     │
  XGZP6847A on each line (= drag sensor)                                  │      ●═══ rod ╲ │
  relief +12 kPa per line (= tangential cap)                              └───────────────┘ ╚═ cyl 2
  path(t) master ≡ path(t) slave (lag 2 ms, gain 0.999 at 4 Hz)       pinwheel rods fix x, y, θ
```

**(c) What moves, and by how much.**

*Sound (§7 rank 15).* The drive goes from 35–50 dBA at the ear (N20s) to **nothing at the head**. Nail hiss becomes the only head-borne sound. Neither of the motorised options reaches that.

*Precessing line, the default.* The puppet reproduces the master exactly, including:
- ε-precession;
- ε random walks;
- heading jumps;
- the circle radius set by δ.

On a 1.2 m line of 2.5 mm ID, the lag is a common-mode 2.1 ms: 1.5° of phase at 2 Hz, gain 0.999. Firmware fires the gates early by that amount, as it already does for the pins. With 1.5 mm ID the lag is 10.7 ms: 7.7° and gain 0.99 at 2 Hz, still uniform across the lines.

*Amplitude.* With a stepper XY master, the line length itself is a firmware variable. A 12 mm line at 4 Hz gives 151 mm/s, the leap-A/D grain inside H-5.4, which no fixed-r head drive can make.

*Tangential force sensing and cap (§7 rank 7, H-6.6, red line 3).* The line pressures *are* the drag vector: Δp·A = 0.1 N per 0.5 kPa, and the sensors resolve about 50 Pa. That gives:
- free snag detection;
- a per-stroke "did the nail reach skin" signal, since skin drag is much greater than canopy drag (§7 rank 2).

A +12 kPa relief per line caps tangential force at about 2.4 N (red line 3) by mechanics, not firmware.

*Compliance.* Air stiffness is P·A²/V:

| Charge | Per line | Plate |
|---|---|---|
| p₀ 30 kPa | 0.37 N/mm | ~0.55 N/mm |
| p₀ 100 kPa | 0.79 N/mm | ~1.2 N/mm |

So 0.5 N of drag shortens the stroke by **0.4–0.9 mm**, and lateral drag (about ±0.2 N) bows it by ±0.15–0.35 mm. A finger is compliant at 0.1–1 N/mm (scratch-model 3.12), so this **is the finger's own compliance**, and plough spikes are absorbed rather than knocked through (H-4.11). Plate resonance is about 20 Hz with 65 g on 1 N/mm, 5× above the 4 Hz drive and damped by the tubes.

**(d) Plausibility with numbers.**

*Head-side mass* [EST]:

| Part | g |
|---|---|
| 3 printed rolling-diaphragm cylinders (diaphragm, piston, cap) | 3 × 7 |
| 3 rods with ball ends | 3 |
| Ball cage and deck | 8 |
| Fittings | 3 |
| **Total** | **35** |

Add about 6 g of tube carried by the head: 3 × 3.8 g/m × 0.5 m. **That is 35–45 g with no heat and nothing that can stall hot,** inside the 45 g margin.

*Bundle.* 16 pin tubes plus 3 synchro lines at 2.5 mm OD pack to about **12.5 mm** (16 alone: 11.5 mm).

*Fail states.*

| Failure | Result |
|---|---|
| Line kinked | that axis freezes; the pins still gate; benign |
| Line burst | the plate goes slack; benign |
| Master motor stalls | the pad stops; the pins are still gated and vented |

None of these can hold a pin down, and red line 8 stays with the pin valves.

*Integration.*
- The synchro lines ride the same nape plug as the pins (leap2-E L3's face-seal block, 3 more ports) and add **no valves**.
- The pin manifold rides on the slave plate. Its 16 tubes must flex ±15 mm at the scrub rate (leap2-F F6: about 2,700–4,800 flexes per session). Route them as one 16-lumen ribbon in a single 60 mm service loop, or adopt leap2-F L2's still-dome tilting pins so the tubes never move.

*Cost* [EST]:
- Desk synthesiser: $35.
- 6 cylinders: $30 printed with cast silicone diaphragms, or $120+ with Bellofram parts.
- Lines and sensors: $15.

**(e) Cheapest experiment ($25, one weekend: ink traces).**
1. **Head side:** three 10 ml *glass* Luer syringes ($8 each; ground-glass plungers have almost no stiction), pinwheeled around a printed plate on three marbles. The plate carries a felt pen on paper.
2. **Desk side:** three 10 ml plastic syringes on an identical plate, moved by hand along a printed rosette template. Then use leap2-B's $15 Tusi rig as the master, with its ring turned slowly by hand for precession.
3. **Measure** the slave trace against the master trace for:
   - line bow over 25 mm;
   - circle roundness;
   - shrink with a 50 g drag weight hung on the pen;
   - drift over 20 minutes.
4. **Pass:** bow ≤ 0.5 mm; shrink ≤ 1 mm at 0.5 N; drift ≤ 1 mm per 20 min with the port opened every 20 s; a 60 s precession rosette that never retraces a stroke within 2 mm.

**(f) Replaces or combines.**
- **Replaces** every motor, gear, Oldham coupling and encoder on the head.
- **Keeps** the Director's synthesiser at the desk, unchanged and unconstrained by mass or noise.
- **Combines with** the air-pin architecture, the κ-grammar (any phrase path) and the fatigue ledger. The drag signal feeds leap2-D D3.

**(g) Honest reasons it might fail.**
1. **Stick-slip.** A compliant drive plus static friction from nails or seals gives micro-judder. 0.2 N of breakaway on 1 N/mm is a 0.2 mm jump, which could read as "stutter". Glass or rolling-diaphragm seals are mandatory; rubber syringe plungers (0.5–1 N stiction) will fail.
2. **Rolling diaphragms are the hard part.** Printed or cast ones may leak or wrinkle at 10⁴ cycles per session [UNKNOWN].
3. **Footprint.** The pinwheel deck is about 95 mm across, against a 76 mm pad, which limits approach to the ear fence.
4. **Stiffness.** If drag-induced shrink proves perceptible, go hydraulic: water in nylon tube is about 50–1,000× stiffer. Disney Research's rolling-diaphragm hydrostatic transmission did this for haptic telepresence ([KNOWN from memory; verify: Whitney et al., ICRA 2016]). The cost is a wet helmet.

---

## LEAP 2 — TWIN DIRECT-DRIVE TUSI: the ring becomes the second motor, so there is no Oldham, no gearbox, and precession is a slow ring rotation

**(a) Assumption broken.** "A two-motor synthesiser needs two stacked stages and an Oldham coupling," and "motors at the pad must be gearmotors."

Look at leap2-B's Tusi couple with the ring *driven* instead of held. The planet rolls in a ring of twice its size, so its absolute rate is ω_p = 2ω_r − ω_c. The pen at d = a traces:

  z = a·e^{iθ_c} + a·e^{i(2θ_r − θ_c)}

**That is leap2-B L4's two-vector synthesiser in one gear stage:**
- **Ring held** (ω_r = 0): line, with heading = θ_r.
- **Ring spinning with the carrier** (ω_r = ω_c): circle. The planet stops rolling and the mesh is idle, so circle mode is **silent at the gear**. Radius is 14.4·cos(ψ/2), set by the ring–carrier phase ψ.
- **Ring creeping** (ω_r = ε·ω_c/2): the precessing line.

At 1.5 Hz and ε = 0.025 the ring turns at **6.75°/s**: 4.5° per revolution, sweeping 180° in 27 s. That is exactly the slow, smooth regime gimbal BLDCs are built for.

**(b) Sketch.**
- **Carrier motor:** a 2204 gimbal (24 g, 13 mm tall), shaft down through a hollow ring motor. Use the GBM2804H (6.5 mm bore, 51 g with encoder), or a second 2204 if its 3.4 mm hole takes a 3 mm shaft [UNKNOWN fit].
- **Ring motor:** its rotor carries the 36T m0.8 internal ring (Ø ≈ 34 mm, matching the 2804 rotor).
- **Gears and output:** one 18T planet with a felt drag pad, and the pad bearing on the planet's pitch circle.
- **Anti-rotation:** Leap 4's polypropylene hinge.
- **Control:** two SimpleFOC drivers phase-lock to ±0.2° (14-bit encoders).

**(c) What moves.**

*Switching.* Circle↔line takes **< 50 ms**. Only the ring changes speed, and the carrier never reverses. Heading jumps are instant ring steps.

*Precession.* Continuous, at any ε. ε can itself be random-walked, which matches the pattern spec's ±20° per 3 cycles.

*Path accuracy.*

| Source | Effect [EST] |
|---|---|
| ±0.2° lock | 0.03 mm |
| Printed m0.8 tooth runout | ~0.1 mm |
| Backlash | 0.1 mm, crossed only at the line ends with the pins lifted, and held by the felt drag |

*Noise.* No gearbox. One plastic mesh at 0.18 m/s pitch-line speed and about 0.5 N tooth load. FOC sine drive with PWM above 20 kHz. **20–30 dBA at 10 cm** [EST], 10–20 dB under the quietest N20 grade.

**(d) Plausibility.**

*Torque and heat.*
- 6 mN·m rms on a 2204 dissipates **0.3 W**; on a 2804, 0.07 W.
- The 15 mN·m plough spikes cost 1.9 W for tens of ms.
- Total is about 0.6 W, so housing rise is a few K [EST]. H-21 is met at ≥ 10 mm from skin, which is trivial at 55 mm.

*Mass* [EST]:

| Part | g |
|---|---|
| Motors (2 × 2204 with AS5600 boards) | 54 (78 if one is a 2804H) |
| Gears | 5 |
| Frame | 12 |
| Bearings and hinge | 6 |
| **Total** | **≈ 77–101** |

That is **≈ 80 g with two 2204s**, 20–25 g over the N20 version and 35 g over the budget. It needs a trade, such as 12 pins instead of 16 (−10 g) or a lighter shell.

*Cost.* About $55 (two motors at $12–20, two drivers at $10, gears and bearings).

*Height.* About 40–45 mm.

**(e) Cheapest experiment ($35, one evening).** Put leap2-B's printed Tusi on a 2204 + SimpleFOC mini as the carrier and turn the ring by hand.
1. Phone SPL meter at 10 cm, against an N20 driving the same rig at 1.5 Hz.
2. Ink a 60 s precession rosette.
3. **Pass:** ≤ 30 dBA, and no stroke retraced within 2 mm.

**(f) Replaces / combines.** It replaces the stacked plates, the Oldham coupling and both gearboxes of the Director's design, with identical math. It is also the ideal *desk master* for Leap 1.

**(g) Why it might fail.**
- 80 g on a helmet.
- Hollow-shaft stacking is fiddly.
- Gimbal-motor cogging (12N14P) may put a faint 14-per-rev ripple into a slow precession. Use FOC cogging compensation, or let the ring be a 2804.
- A seized planet stalls both motors hot, so FOC current limits plus a thermal fuse are needed.

---

## LEAP 3 — THE CLUTCHED TUSI: one quiet motor, and the 17th air valve chooses circle or line

**(a) Assumption broken.** "Two modes need two motors." Same Tusi, but the ring is never motorised. A sprung friction brake holds it to the frame (**line**, the vented and fail-safe state). A Ø10 mm air diaphragm on its own desk valve (3 N at 40 kPa) pushes it instead against a friction face on the carrier (**circle**). An AS5600 on the ring reports its angle.

**(b, c)** The firmware gets three abilities from clutch timing:
- **Heading:** engage the clutch for Δt and the ring is dragged ω_c·Δt.
- **Circle radius:** engage at the right ψ.
- **Precession:** engage for 2–5° once per revolution.

Mass is **45–50 g** with one 2204, noise 25–32 dBA plus a soft clutch "shh", cost about $30. Switching takes ≤ 1 revolution (0.5–0.7 s at 1.5–2 Hz).

**(d, g)** It is lighter than any other motorised option and fits the 45 g margin. **But the precessing line is stepwise:** 2–5° micro-slips, each a small jerk, plus slip scatter of about ±1°. The Director now makes that line the default, so this **scores down**. It survives only as the lightest fallback if 80 g cannot be found and the air puppet fails.

**(e) Test ($5 on Leap 2's rig).** Swap the hand-turned ring for a rubber-band brake and finger clutch, and ink the stepped rosette beside the smooth one.

---

## LEAP 4 — POLYPROPYLENE LIVING-HINGE PARALLELOGRAM: silent anti-rotation for any drive

**(a) Assumption broken.** "Pure translation over a ±15 mm disc needs an Oldham cross-slide (sliding keys that tick at every reversal) or flexures (which cannot stroke that far)." Steel-rod flexures are overstressed by 4× (2.2 GPa at ±15 mm on 50 mm rods). A **two-stage parallelogram** lets the strain concentrate in **polypropylene living hinges**, which routinely survive more than 10⁶ flexes at ±90° [KNOWN, PP hinge practice].

**(b) Layout.**
- **Outer frame → middle frame:** two parallel 40 mm links at 0°.
- **Middle frame → pad:** two parallel 40 mm links at 90°.
- **Hinge swing:** ±22° at ±15 mm. In-plane coupling is L(1 − cos θ) = 2.9 mm, absorbed by the other stage.
- **Material:** one flat 0.6–0.8 mm PP sheet, cut or printed, **≈ 3 g, about 2 mm tall**.

There is no sliding, no clearance and nothing to tick. Life at 4,800 cycles per session is about 200 sessions per 10⁶ cycles (UNKNOWN for printed PP; die-cut folder PP is the conservative pick).

**(c–g)** It removes the Oldham coupling's reversal tick, the last mechanical noise in Leaps 2–3 and in the Director's design. Rotation stiffness of about 1–3 N·m/rad (EST, set by hinge width) keeps pad yaw under 1° against 20 mN·m of off-centre drag. **Test ($2):** cut it from a folder, hand-move the plate around a 30 mm disc 10⁴ times with a drill crank, and check yaw with a laser pointer on the wall. It might fail through hinge creep at 34 °C, or through PP printing badly (so die-cut it).

---

## 2. Why the travel motors cannot draw the path on a helmet (leap2-E L2, quantified)

Leap2-E's helmet carries pad, carriage and arm (105 g) at r 150 mm plus a 30 g arc, so I ≈ 2.7 × 10⁻³ kg·m². A ±15 mm stroke at the nails (R 95 mm) is ±0.16 rad. Peak inertial torque is **0.038 N·m at 1.5 Hz and 0.067 N·m at 2 Hz**, plus 0.07 N·m rms of drag, for **0.075–0.094 N·m rms per axis** [EST]. Heat follows from (τ/Km)²:

| Motor class | Mass | Heat per axis |
|---|---|---|
| GBM2804 (Km 0.022) | ~51 g | **12–18 W** (a 50 g motor would pass 100 °C) |
| 3506 class | ~70 g | 3–4 W |
| 4108 class | ~110 g | ~1 W, but two of them push the helmet to **≈ 595 g**: red line 10 |

On top of that, the whole arc oscillates, which feeds the helmet a 0.04–0.09 N·m rocking torque at the scrub rate. That is 2–3× the reaction of a pad-local drive, and concept-A's holding margin falls from 2.9 to about 1.5 at µ 0.3.

**Software precession would be perfect, but the hardware cannot carry it on a head.** It stays a cradle idea.

**Integration warning that applies to every pad-local drive:** the scrub drag (±0.07–0.1 N·m, reversing at the stroke rate) also flows into the travel axes. Leap2-E's 40 g travel gimbals would need about 10 W just to *hold* it. Travel must therefore be one of:
- geared, with a **bias spring** larger than the drag torque so backlash never changes flank (otherwise there is a tick at 2–4 Hz);
- braked.

The air puppet does not remove the drag reaction, but it is the only drive that **measures** it.

---

## 3. Best bet: the AIR PUPPET (Leap 1), driven by a twin-direct-drive Tusi at the desk (Leap 2), with a PP hinge backstop (Leap 4)

Michael's default mode is a slowly precessing 30 mm line, with circles and fixed lines one tap away. The question is where the machine that draws it lives. On the head, every option pays for the path with something the helmet cannot spare:

| On-head drive | Cost to the helmet |
|---|---|
| Director's N20 pair | 35–50 dBA of gear noise 110 mm from the ear, plus a 150–300 ms reversal to change mode |
| Silent twin-FOC Tusi | ~80 g, 35 g over the margin |
| Light clutched Tusi | a jerky, stepwise precession |
| Travel motors | 12–18 W per axis, or ~595 g |

The air puppet moves the entire synthesiser into a foam box and sends the helmet only its **position**, through three sealed 2.5 mm lines with no valves.

The head then carries **35–45 g** of passive cylinders on a **22 mm** deck that makes **no sound and no heat**. It copies the master to within a 2 ms common lag and 0.4–0.9 mm of finger-like compliance under drag. It inherits whatever the master can do:
- smooth ε-precession and ε random walks;
- < 50 ms mode switching;
- circle radius 0–15 mm;
- with an XY master, variable line length that lifts the 2.1 Hz full-line ceiling and gives 4 Hz grain.

As by-products it adds a mechanical 2.4 N tangential cap (line reliefs) and a free drag sensor (line pressures).

**The $25 weekend test settles it in ink:** glass syringes on the slave, plastic on the master, one pen. It passes if a 60 s precession rosette shows ≤ 0.5 mm bow, ≤ 1 mm shrink at 0.5 N and no retraced stroke. If it fails on stick-slip or stiffness, the fallback is already the desk master: put the twin-direct-drive Tusi on the pad (20–30 dBA, ≈ 80 g, < 50 ms switching, perfectly smooth precession) and find 35 g elsewhere on the helmet. The Director's two-N20 synthesiser remains a valid third choice. It is the cheapest and lightest that precesses smoothly, but it is the loudest thing that would ever sit on Michael's head.
