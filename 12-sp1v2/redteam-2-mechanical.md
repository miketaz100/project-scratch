# RED TEAM 2 — Mechanical, hair and safety attack on SP1 "PUPPET HALO" (Design Freeze v2)

**Project SCRATCH · 12-sp1v2 · Red Team 2 · 2026-10-02**
**Read:** DECISION-2, SYSTEM-SPEC (all), safety-requirements (13 red lines), hair-interaction (all rules and the §6.8 checklist), 04-redteam/redteam-2-mechanical, leap3-A, leap3-B, leap3-E, leap2-C. I checked redteam-3-buildability only for overlap (§11).
**Tags:** **[KNOWN]** = stated in a project file · **[EST]** = my arithmetic (script `rt2.py` in the session scratchpad) · **[VERIFY]** = only a bench can close it.

---

## 0. Verdict

The puppet architecture is sound where it matters most:
- pin and palm normal caps really are pressure × area;
- nothing on the head turns continuously;
- nothing on the pad is powered;
- every de-energised valve vents.

The spec's cap arithmetic checks out exactly: 0.96 N per nail, 7.18 N single, 7.81 N at the double fault.

What fails is mostly **geometry and integration that §7 never drew**:

1. **The omni-nail is a necked mushroom in the pile.** It has a Ø 7 head on a 0.38 mm neck, and it reverses at every line end while hovering 5 mm deep in a 10–25 mm pile. This is the loop former that H-4.3 and H-3.4 forbid. Gating item 6 scores **0**, and my checklist total is **23/36**, not 32.
2. **The umbilical crosses the bail's sweep.** The loop from the clip to the rear node passes through the bail's R 210 shell at α ≈ 29–55° for every clip position the spec allows. The bail sweeps −35…+108°. The pad's own 16-tube harness has **no route and no mass budget**.
3. **The synchro "≤ 4 N" tangential cap is about 10.4 N.** A torn diaphragm slams the block 15 mm in 15 ms at 1.7 m/s, which is 60 mJ against a 50 mJ limit.
4. **The pad drives into the hub pods beyond β ≈ 41–46°.** Firmware allows ±55°. The twin guard of |β| ≥ 8° should be about 36°.

All the fixes are cheap. Only the nail and the routing need real redesign.

---

## 1. Hair: every feature within 30 mm (and within reach of 5–8 cm hair)

### 1.1 The omni-nail stick is an upside-down hook (gating)

From the skin up [KNOWN §4.1], the stick is:
- a Ø 2 flat;
- a 45° cone to **Ø 7 at 2.5 mm**;
- a flat top (the neck is "hooked into a cross-drilled tip and resin-filleted");
- a **0.38 mm wire neck, 12 mm free**, with a PTFE 1.0 × 2.0 sleeve 8 mm long;
- a Ø 1.59 brass ferrule;
- the Ø 1.0 shaft.

That is four steps and a neck between 2.5 and 14.5 mm above the skin, all inside the design pile. H-4.3 asks for "a continuously widening wedge… no steps, no necks". H-6.3 says an element "widens above the guard, never below it". This one is widest at its foot.

**How it fails.**
1. In a bite, strands that ride up the cone pass over the Ø 7 rim and settle on the neck.
2. At lift, the flat shoulder carries them up.
3. The nail then reverses while hovering 5 mm into the pile. §7.3 relies on H-5.2's "≥ 5 mm at zero force" clause here.
4. A strand around the neck is dragged back: this is the H-3.4 lasso ("any feature a loop can tighten around (a neck…)").

Zero force releases strands **under** a tip, not strands **around** a neck. Leap3-E's "net winding zero in line mode" is about capstan wrap, not loops. Each pin makes about 3,400 hover reversals per 20-minute session [EST].

**The safety reflex makes it worse.** The snag reflex and every fail-to-free path retract the float. The pin has only **4 mm of reserve stroke** past contact (contact at 20 of 24 mm). After 4 mm it bottoms, and the 1.5–2.25 N retract spring loads the loop. The safety reflex delivers the tuft pull (S3).

**Fix (≈ $10, one weekend):**
- move the neck compliance into the cartridge above the 32 mm nose, as a flexure between piston and shaft;
- make everything below the nose one **drafted POM cone**: Ø 2 flat, R 0.4 rim, widening at ≥ 10° to Ø 4–5;
- no shoulder, sleeve, ferrule or lean stop in the pile;
- pin reserve ≥ 12 mm, at least the 10 mm snag retract, so a captured nail stays down while the pad lifts.

### 1.2 The neck sleeve is a trap-band gap and a crevice

A 0.38 mm wire in a 1.0 mm-ID sleeve leaves a **0.31 mm annulus**, 2.5–14.5 mm above the skin. It changes shape every time the neck leans. That breaks H-4.9 (gating item 3).

"Bonded PTFE" does not stay bonded without sodium etching, especially under thousands of flexes and IPA wipes. Once loose, the neck stiffness that the stability margin depends on (V22) drifts, and the sleeve can migrate. The §1.1 stick deletes the sleeve.

### 1.3 Nails scissor against the skids at the scalp

Pins sit at (±9, ±27), skids on a Ø 100 circle, and the stroke reaches ±15 mm in every heading, because PLINE precesses through all of them. Scanning every heading, the **minimum nail-axis-to-skid-axis distance is 7.8 mm** [EST] (pin (−9, −27) against the 240° skid).

| Skid foot | Clear gap at the nail rim (r 3.5) |
|---|---|
| Ø 8 | **0.3 mm** |
| Ø 12 | collision (−1.7 mm) |
| Full R 15 cap (r 8.3 at 2.5 mm) | collision (**−4.0 mm**) |

This is a gap that closes at the skin between a moving and a fixed element: H-3.8 scissoring and H-5.6.

**Fix ($0):** skid circle Ø 116; skid foot ≤ Ø 8; rotate the triangle toward the field's notched corners; CAD check of ≥ 8 mm over all (ψ, s).

### 1.4 Skids never lift

The skids stay loaded at 0.15 N for the whole of PLAY:
- through every travel reversal;
- through "THAT WAY" overshoots;
- through **N1 hover spirals**, which drift R 15–25 mm circles around a target: a loaded in-place circle (H-5.7).

At 20–50 mm/s of drift for half the session, each R 15 dome slides **18–60 m per session** in all directions [EST], and none of it is ledgered. An R 15 dome rides on hair rather than parting it, so the risk is backcombing and matting (S1–S2, certain), not capture.

**Fix ($0):** ledger skid passes per cell; make N1 a sequence of lifted hops.

### 1.5 Bore exit, guard, strut, tendon, circle mode

- **Wiper.** A silicone seal at the 32 mm nose is allowed. **Unspecified:** the rod side of each cartridge changes volume by **0.77 ml per park** (38.5 mm² × 20 mm). If it breathes past the wiper, every park inhales air, sebum and short hairs at the nose. **Fix ($2):** a filtered vent port above the block.
- **Block, struts, carriage, bail.** The block underside at 32 mm (drafted, Ra ≤ 0.8) is a good guard. RCC struts, bell cranks and MR63s are ≥ 40 mm from the skin; the carriage ≥ 105 mm. Pass.
- **β-tendon idlers "at both legs".** The legs meet the hubs 43 mm outboard of the parietal scalp, so an exposed Dyneema-on-idler nip there is within reach of 5–8 cm side hair. Put the idlers inside the sealed pods.
- **Circle mode.** The C19 gate holds: about 144° of winding per entry (×1.9 capstan factor), never cumulative. But:
  - The score's example phrase (R 12 at 0.8 Hz) ploughs in at **40°**, breaking the spec's own 35° rule. It needs f ≥ 0.95 Hz.
  - Descent plus park (0.52 s) caps 75° windows near **1.5 Hz**.

  The token checker must actually run in circle mode.

---

## 2. Force caps

### 2.1 Normal: the arithmetic holds, but the third barrier is not yet a constant

C8's logic is right. Pins react against a pad that is held by an air float, so scalp load = float force + pad weight. The float spring subtracts a further 1.5–3 N, so the real cap is lower.

The spec's backstop is "pump stall 53 kPa", but that figure is a catalogue **minimum** for the KPM27C ("> 53 kPa", leap2-C). The real third barrier is where the pump and bleeds balance at 100 % duty with both reliefs failed. With a linear pump curve against the Ø 0.25 rail bleed and the Ø 0.2 + Ø 0.3 palm bleeds [EST]:

| Pump deadhead | Rail → per nail | Palm → total |
|---|---|---|
| 53 kPa | 39.6 kPa → 1.53 N | 29.1 kPa → **10.1 N** |
| 70 kPa | 53.3 kPa → 2.05 N | 39.9 kPa → **13.4 N** (red line 3 fails) |
| 80 kPa | 61.9 kPa → 2.38 N | 47.0 kPa → **15.7 N** |

R1a/R1b and R2/R2b are the same printed poppet, set in one session, so a double failure has a common cause.

**Fix ($10–20):**
- P3 (palm pump) with a **deadhead ≤ 30 kPa**: then the total is ≤ 10.3 N with no relief at all;
- P1 (rail pump) with a deadhead ≤ 50 kPa;
- R1b and R2b of a different design;
- measure the equilibrium at A1 and print that number in place of "pump stall".

**Float stiction.** The float rides two parallel rods. A 1 N drag at the nail plane acts about 100 mm below the bushings, which loads them about 4.4 N each (24 mm spacing). At µ 0.15 that is about **1.3 N of stiction**. It adds to the cap on rising contours (9.1 N at the double fault) and makes the skids pat (R11). Use an MGN7 rail with the seals removed, as the earlier red team recommended.

### 2.2 Tangential: the "≤ 4 N" cap is about 10.4 N, and the lean stop makes the neck rigid

**Pad level.** In a snag the slave is held while the master drives 15 mm. The compressed line relieves at 28 kPa, but **the expanding lines are bounded by nothing**: one opened by 4.7 ml of its 18 ml falls to **−5.2 kPa**. Taking the worst direction, the pad sees **10.4 N** [EST]. A stuck relief takes one line to 63 kPa (19.8 N), which the 0.13 N·m stepper carries.

**Per nail.** Red line 3 allows ≤ 2 N tangential per element "before something slips, deflects or breaks away".
- The 0.38 mm neck yields at about 0.9 N (σy ≈ 2 GPa, M_y 10.8 N·mm at 12 mm).
- At the 30° lean stop the load passes to 17.5 mm of Ø 1.0 shaft at **5.5 N/mm: rigid**.
- A snagged nail can then be loaded toward 10.4 N. Only the firmware snag reflex (0.8 N, 30 ms) stops it.

Skin shear is limited by friction (≤ 0.3 N per nail), so what gets hurt is a captured strand or tuft. Red line 13 fails in substance.

**Fix ($3 + firmware):**
- p₀ 20 → 8 kPa;
- relief at p₀ + 4;
- a duckbill **vacuum breaker** per line that admits air below p₀ − 4.

That gives a two-sided cap of **2.5 N** [EST], at the cost of about 10 % of stiffness, because air stiffness comes mostly from atmospheric pressure. Also delete the lean stop, and set the TMC2209 current by **VREF** so the master stalls at ≤ 6 N at the plate.

### 2.3 Faults

| Fault | Result [EST] | Verdict |
|---|---|---|
| Pump MOSFET fails short ("regulator fails open") | Rail held at R1a, palm at R2. Out-of-band trip at 0.5 s; NO dumps open while the pump runs. | Pass |
| One rail relief stuck | R1b holds at 1.04 N | Pass |
| Both rail reliefs stuck | 1.53–2.38 N | Pass once V12 is measured |
| Pin line kinked, pressurised | 6.2 ml trapped; bleed takes it below 2 kPa in ≈ 0.5 s | Pass |
| Palm line kinked, pressurised | Float vents only through its Ø 0.3 bleed: **1.9 s** | Slow |
| Palm kinked, then float compressed 10 mm (headrest, hand) | Reliefs are box-side, so the trapped 7.85 ml goes from 15 to ≈ 90 kPa: **≈ 29 N** transient | **Fail.** Fit a relief poppet at the float. |
| Synchro relief stuck | 19.8 N | **Fail.** VREF current limit. |

---

## 3. Synchro

**Stiffness.** P·A²/V = 0.67 N/mm per line, **1.0 N/mm at the block** [EST]. Confirmed.

**Temperature.** A foam-lined box on a couch cushion at 22 W heats by about +16 K per 20-minute session and +28 K per hour (τ ≈ 29 min) [EST].
- Common-mode heating only raises p₀, by about 1.7 kPa.
- A 5 K difference between master cylinders shifts the slave centre by about 0.2 mm, which the 60 s re-zero absorbs.

The heat matters more for the PETG mounts and the sensors. Add a vent and trim idle power: the five held-closed NO dumps alone draw 4 W.

**Leaks.**
- At budget (0.24 mm/min) the drift is harmless: velocity is unchanged, so lift-before-reversal survives an offset.
- A pin-holed diaphragm at about 5 kPa/min shifts 2.4 mm per 60 s and drags the drag-vector baseline with it. That means false snag trips or masked real ones.
- Plug sealing has a margin of about 1: 12 N over the gasket gives roughly 30 kPa of contact stress against 28 kPa in the line, and a head-turn peel moves about 1.5 N off one row.

**One line ruptures.** A torn 0.4 mm cast diaphragm is plausible (R2 rates diaphragm life at P = 0.30). The other two lines push **6.3 N** unbalanced:

| | Unbalanced force | 15 mm takes | Impact speed | Energy |
|---|---|---|---|---|
| p₀ 20 kPa (frozen design) | 6.3 N | 15 ms | **1.73 m/s** | **60 mJ** |
| p₀ 8 kPa (my fix) | 2.5 N | 28 ms | 0.58 m/s | 7 mJ |

At p₀ 20 kPa, nails in contact are dragged at 9× the H-5.4 limit and the energy exceeds the §2.4 limit of 50 mJ. The end-stop bang reaches the skull by bone conduction. §7.7 calls this "slack, benign"; it is a startle and a probable pluck.

**Reverse pressure.** Two conditions put rolling diaphragms into reverse pressure:
- the −8 kPa park, about 3,000 times per circle-mode session;
- snags, which pull the synchro lines to −5 kPa.

Inverting the convolution is the classic way rolling diaphragms crease and tear. It feeds both R2 and the rupture above, and redteam-3's latex and nitrile sleeves share it. **Fix:** run the R2 rig *with* the park cycle; fall back to R3's −2 kPa or spring park; add the §2.2 vacuum breakers.

**Bell cranks off-centre.** The lines of action are concurrent only at the centre. At ±15 mm (about ±37° on ~25 mm arms), each 6.3 N push is offset by a few mm. That gives roughly 0.01–0.03 N·m of yaw on the PP parallelogram, or 0.3–0.8 mm at the outer nails [EST, geometry not drawn]. Lower p₀ scales it down.

---

## 4. Helmet

**Lean, yaw and creep.** My lean is 0.21 N·m (spec 0.24). The 1–1.5 N·m form lock covers it 4–6×.
- Yaw is held by friction only: 0.57 N·m against an inertia of 5 × 10⁻³ kg·m². The helmet slips at **114 rad/s²** [EST], which a brisk head turn exceeds. This costs registration, not safety, because the fence moves with the helmet.
- §7.7 trips on "head jerk > 60 rad/s²", but there is **no IMU**. Fit one on the spare pogo pin ($3) or delete the claim.
- Creep: about 20 N·m/rad of pad stiffness gives 0.7° (≈ 1.2 mm at the forehead), plus 30–50 % foam creep over a session.
- A sneeze at 3 g puts about 10 N on the 352 g helmet, which equals the cradle override.

**Doff ≤ 3 s.** It passes if the lever is released first. Two paths fail:
1. **Lever still clenched** while the free hand lifts the band: nails at bite force drag out through the hair. **Fix ($3):** a head-present switch (forehead pad or cradle) in the hardware loop.
2. **High-backed seat.** With the pad at the bun, the bail is a horizontal hoop **112 mm behind the bun at ear height**, and the rear node sits on the occiput. A headrest closer than about 110 mm blocks the doff, loads the forehead band with 20–40 N (the structural limit is 20 N) and presses the plug into the occiput. Couch backs, where the box is meant to sit, are where heads rest. Write a posture rule and cap reclined α at 45°.

**Breakaway chain.**
- The plug's **2 × Ø 4 × 8 mm dowels lock shear**, so it releases only when the normal component reaches 12 N. At 60° off-axis that is **24 N**, so the helmet sheds first.
- The 3 N clip spans 278 mm on a 300–350 mm loop, so a 60° yaw or a 100 mm lean pops it routinely.

### 4.1 The umbilical lives inside the bail's sweep (certain)

With the clip 100–200 mm above and behind the crown and the rear node at about (−95, 0, −40), the loop crosses the R 215 bail-and-carriage shell at **α = 29–55° on the midline** for all nine clip positions I checked [EST]. The bail sweeps −35…+108° over |β| ≤ 62°, so every trip to the occiput drives the bail, rollers and tendon guide into the bundle.

At R 210 the α drive pushes about 2 N. That is a helmet tug of about 0.4 N·m (**twice the lean**), plus clip pops, plus the bundle draped over the bail and carried toward the face on the return to α −25°.

**Fix ($0–15):** exit along the **ear axis from the right hub pod**, the only line the bail never sweeps. Put the clip beside the head and lengthen the loop to ≥ 450 mm.

### 4.2 Hub-pod collision and twin scissoring

The hub pods are the bail's poles; their inner faces press the scalp at (0, ±77, 0). The pad's angular distance from the pole is therefore 90° − β **at every α**. Adding up a skid 43–50 mm along the scalp, its radius, and a ≥ 25 mm hub pad, the pad reaches the pod at **β ≈ 41–46°** [EST]. Firmware allows ±55° and the hard stops sit at ±60°.

The consequences:
- a closing wedge at the scalp between a moving skid and a static pad pressing hair down;
- a finger pinch at the β tendon's 10–15 N;
- side coverage overstated (the spec claims 94 %).

**Twin.** Near the vertex the two mirrored pads need:

| To clear | Required separation |
|---|---|
| Nail fields | **\|β\| ≥ 32°** |
| Skid circles | **≥ 36°** |
| Decks | ≥ 23° |

The spec's guard is **|β| ≥ 8°, in firmware only**. Antiphase nail fields are H-3.8 scissoring (S3–S4), so red line 13 applies.

Also, a parked pad B (pins tee'd to A's valves) retracts 25 mm while its nails extend 24 mm, ending about 1 mm from the scalp at the bun. Restore leap3-A's palm-pilot interlock.

**Fix:**
- hard stops at ±40° with bumpers;
- firmware limit ±36°;
- a **mechanical** twin stop at ≥ 36°.

---

## 5. Fail-to-free lift

**Every path de-energises correctly:** power loss, e-stop, hold-to-run, PS1, watchdog, helmet loop, either plug pulled, FAULT. Pump failure is benign. If the rail MOSFET fails short, the watchdog and loop interlocks are lost but the series contacts still work, which leaves two layers. Acceptable.

**Speed.** The spec's 80 ms is frictionless dynamics. In reality 7.85 ml must leave through 1.65 m of 2 mm tube and a cheap 3-way exhaust (Ø 0.8 assumed), pushed by 1.5–2.25 N of spring, against 0.83 N of pad weight at the vertex [EST]:

| Case | Retract time |
|---|---|
| Vertex | **390 ms** |
| Bun or sides | **270 ms** |
| Kinked palm line | **1.9 s** |
| With a quick-exhaust valve (QEV) at the float | ≈ 60–90 ms (dynamics-limited) |

Gate B4 (≤ 150 ms) fails as built. Contact force does drop within tens of ms, so red line 8 holds in substance.

**Fix ($6, 4 g):** the float QEV.

**Pinch.** The float ring rising toward the carriage has 1.5–3 N of spring force at ≥ 120 mm from the skin: harmless. The real pinch is §1.1's 4 mm reserve.

---

## 6. Electrical

- **12 V certified adapter, no mains, no lithium:** pass. 47 W peak on 60 W with a 5 A fuse.
- **Dead-man welding.** The 2.5 N hold-to-run microswitch closes the actuator rail onto ≥ 470 µF of bulk capacitance plus driver and buck input caps. The inrush is tens of amps, and repeated make-on-capacitance welds microswitch contacts. A welded dead-man fails silently.
  - **Fix ($5–15):** switches drive a force-guided relay or a MOSFET gate (still hardware); firmware checks on every release that rail-sense falls.
- **Stale outputs.** TPIC6B595 /G is tied to rail-enable, so latched outputs go live the instant the rail returns. AND /G with a firmware output-enable line ($0), so that start-up lifted is a hardware fact (H-5.9).
- **Servos.**
  - Up to 1.2 A on 26 AWG drops about 0.55 V over the loop; verify brownout behaviour (V3).
  - No servo wire crosses a moving joint.
  - Check the pod's inner face against 43 °C with the bail parked off-balance.
  - Keep skin-contact metal (hub shaft, splice) isolated from the 6 V ground, because a USB laptop ties in a mains SMPS.

---

## 7. Mass, centre of mass, neck

**The pad harness is missing.** Twelve pin lines, the palm line and three synchro lines must run rear node → hub → leg → arc → carriage to a pad that travels 143° in pitch, ±200 mm along the arc and 50 mm radially.
- Weight: 13 × 4.7 + 3 × 9.2 = **89 g/m** of bare PU [EST].
- Length: **0.55–0.7 m, so 50–63 g**.
- The ledger carries 18 g for "plug + harness", and the pneumatic table lists 0.30 m.

| | Spec | Corrected |
|---|---|---|
| Single | 352 g | **≈ 395–400 g** (no reserve left) |
| Twin (second harness to pad B) | 479 g | **≈ 575 g**: red line 10 fails |

The twin needs multi-lumen extrusion or 2 mm-OD lines.

**Neck** [EST]: at 20° forward tilt the added flexion moment is 0.16 N·m at 352 g, 0.20 at 479 g and 0.26 at 575 g, against the head's own 0.4–0.9 N·m. Single mode is bike-helmet territory. The 85 mm of CoM wander is a perception problem, not a fatigue problem.

---

## 8. Cleaning and hygiene: 12 nails and 12 bores

- **Sticks:** good. ¼-turn bayonet, POM, IPA-safe, about 2 minutes per session; keep two sets.
- **Crevices at the skin end:** the cross-drilled resin joint, the 0.31 mm sleeve annulus (wicks sebum and IPA) and the ferrule ends. The §1.1 one-piece cone deletes all three.
- **Bores.** The wiper scrapes sebum off the shaft every stroke and pumps some into the PTFE guide. The hover collar has to sit in a **0.07–0.10 N window** (R3); a 0.01–0.03 N friction shift moves pins out of it, so they tap or stop hovering. Hygiene is a function risk here, and noses cannot be cleaned without pulling cartridges.
  - **Fix:** carry the 12 wipers on a tool-free snap-off skirt plate; wash weekly; pull cartridges monthly.
- **Restrictors and bleeds** (Ø 0.22 / Ø 0.15) have no upstream filter, and pump-diaphragm dust will clog them. Leap2-C called a 10 µm filter mandatory ($3). A clogged bleed silently removes the kinked-line backstop.

---

## 9. The 13 red lines, audited

| # | Verdict | Why |
|---|---|---|
| 1 Rotation / slot within 30 mm | **Pass** | Enclose the β idlers in the pods |
| 2 Per-element normal ≤ 2.5 N, mechanical | **Conditional** | 0.96/1.04 N is real; the third barrier (1.53–2.38 N) is unverified (V12) |
| 3 ≤ 12 N total; ≤ 2 N tangential per element | **Normal conditional; tangential FAIL** | 13.4 N with a 70 kPa palm pump and both reliefs stuck. Pad cap 10.4 N; the lean stop goes rigid; rupture gives 6.3 N |
| 4 E-stop + hold-to-run | **Pass, weld risk** | Release weld check |
| 5 Mains / 24 V / lithium | **Pass** | |
| 6 Hairline, ear, eyes | **Conditional** | The band is a real guard; set the α stop from Michael's hairline. Pads hit the hub pods past β ≈ 41°, so the ±60° stop is a collision, not a fence. Displaced 15 mm there, the skid is within ≈ 21 mm of the canal |
| 7 Self-locking drive | **Pass** | Servos sit in travel only |
| 8 Free on any fault | **Pass on force; spec timing fails** | 270–390 ms; 1.9 s with a kink |
| 9 Retention, proof 3× | **Fail as written** | 1.5 N axial is 1.6× the 0.96 N cap, not 3× (≥ 3.1 N). The B3 "1.0 N lateral, no set" contradicts the 0.75–0.9 N neck yield |
| 10 Doff, strap, ≤ 500 g | **Single pass (≈ 400 g); twin FAIL (≈ 575 g)** | Needs a head-present switch and a posture rule |
| 11 Edges | **Pass, pending tape test** | Ferrule ends are burrs in the pile |
| 12 Procedure | **Pass** | |
| 13 Firmware never alone | **FAIL** | Per-nail tangential past the lean stop; twin scissoring guarded by firmware \|β\| ≥ 8°; head-jerk trip has no sensor |

---

## 10. Hair checklist (H-6.8), my score

| # | Item (G = gating) | Spec | Me | Note |
|---|---|---|---|---|
| 1 | No rotation in zone (G) | 2 | **2** | |
| 2 | Every zone joint has a method (G) | 2 | **1** | Annulus, rod-side vent, ferrule and cross-drill have no named method |
| 3 | No changing or 40 µm–3 mm gap (G) | 2 | **1** | 0.31 mm flexing annulus; nail–skid 0.3 mm or collision |
| 4 | Lift before reversal (G) | 2 | **1** | Hover reversals with a neck in the pile; skids never lift |
| 5 | Rigid group (G) | 2 | **1** | Skids move ±15 mm relative to the nails |
| 6 | Nail, drafted root, no re-entrants (G) | 2 | **0** | Ø 7 head on a 0.38 neck, flat shoulder, three steps |
| 7 | Yield ≤ 0.15 N (G) | 1 | **1** | |
| 8 | Protrusion (35 mm at 8 cm hair) | 2 | **1** | 32 mm |
| 9 | Spacing ≥ 8 mm | 2 | **2** | |
| 10 | Low-friction surfaces | 2 | **2** | The wiper is a seal |
| 11 | Breakaway 3–5 N | 1 | **1** | Pad breakaway is ≈ 25 N tangential at the nail plane (2 N·m / 80 mm) |
| 12 | Guard pass-throughs | 2 | **1** | The element widens below the guard |
| 13 | Grain map | 2 | **2** | |
| 14 | Dwell limits | 2 | **2** | Skid passes not counted |
| 15 | Snag reflex | 2 | **2** | Meets the rule; §1.1 makes the retract pull loops |
| 16 | Antistatic | 1 | **0** | PTFE (the most electronegative polymer) in the pile; the "piston-clip ground" has nothing to connect to on a wireless pad |
| 17 | Tool-free cleaning | 2 | **2** | |
| 18 | Variants stated | 1 | **1** | |
| | **Total** | **32** | **23/36** | **Below 28, with a gating 0** |

With the §1.1 stick, the §1.3 skids, and an ESD-POM nail grounded through a conductive guide rod to the carbon bail and the hub GND, the score rises to **≈ 30/36**. Item 4 stays at 1 by design (hover).

---

## 11. Redteam-3's proposal to delete the helmet plug

**Confirmed, on two conditions:**
1. **A float QEV (§5).** Without the helmet-end vent, every retract runs through 1.7 m of line (270–390 ms), so a yank that sheds the helmet drags limp nails and skids through the hair.
2. **The loop-wire pogo lanyard must be the shortest member of the bundle**, so that any pull cuts the rail before the tubes go taut.

---

## 12. Ranked attacks

| # | Attack | Severity | Likelihood | Fix | Cost |
|---|---|---|---|---|---|
| 1 | **Omni-nail neck in the pile:** loops form on hover reversals, then the safety retract pulls them after 4 mm of reserve. Item 6 = 0 | S3–S4 | Medium at 5–8 cm; low at ≤ 3 cm | Neck compliance in the cartridge; one drafted cone below the nose; reserve ≥ 12 mm | ≈ $10, a weekend |
| 2 | **Umbilical in the bail sweep:** crosses at α 29–55°; the bail sweeps −35…108° | S2–S3 | **Certain** | Exit on the ear axis from the right pod; clip beside the head; loop ≥ 450 mm | $0–15 |
| 3 | **Synchro cap ≈ 10.4 N, not 4 N;** stuck relief 19.8 N; rupture slam 60 mJ | S3 | Medium | p₀ 8 kPa, relief +4, vacuum breakers (cap 2.5 N); VREF stepper limit | ≈ $3 |
| 4 | **Pad hits the hub pods past β ≈ 41–46°;** twin guard 8° (needs 36°), firmware only | S2–S3 | Certain if commanded | Stops ±40°, firmware ±36°, mechanical twin stop, pad-B palm interlock | $0–5 |
| 5 | **Nail–skid scissor:** 0.3 mm gap or collision at the scalp | S3 | High | Skid circle Ø 116, foot ≤ Ø 8, reoriented, CAD ≥ 8 mm | $0 |
| 6 | **Pad harness unrouted and unbudgeted:** single ≈ 400 g, twin ≈ 575 g | S2 (red line 10, twin) | Certain | Route in a bail guide; budget 50–63 g; multi-lumen lines for the twin | $10–20 |
| 7 | **Retract 270–390 ms, not ≤ 150 ms;** kink 1.9 s; kink plus compression ≈ 29 N | S2 | Certain (B4) | QEV and relief poppet at the float | ≈ $10 |
| 8 | **Third normal barrier not a constant:** 13.4 N with a 70 kPa pump and a double relief fault | S3 | Low | P3 deadhead ≤ 30 kPa, P1 ≤ 50; diverse R1b/R2b; measure at A1 | $10–20 |
| 9 | **Reverse pressure on rolling diaphragms:** feeds R2 and #3 | S2 → S3 | High | Test the R2 rig with the park cycle; −2 kPa or spring park; vacuum breakers | $0–10 |
| 10 | **Hold-to-run welds on inrush;** stale outputs on rail return | S3 (silent) | Low–medium | Relay or MOSFET gate switching; weld check; /G AND OE | $5–15 |
| 11 | **Red-line-9 proof contradictions** | S2 | Certain on paper | Proof to 3× R1b (≥ 3.1 N); redesign the neck | $0 |
| 12 | **Doff and posture:** lever-held doff; bail blocks high seats; no IMU; yaw slip at 114 rad/s² | S2–S3 | Medium | Head-present switch; posture rule; reclined α ≤ 45°; IMU or drop the claim | $3–6 |
| 13 | **Float stiction ≈ 1.3 N:** patting, cap creep | S1–S2 | High | MGN7 rail or flexure | ≈ $10 |
| 14 | **Hygiene:** annulus crevice, sebum in guides shifts the hover window, unfiltered orifices | S2 | High over weeks | One-piece stick; wiper skirt plate; 10 µm filter | ≈ $5 |
| 15 | **Static:** PTFE in the pile, no ground path | S1 (feeds #1) | High below 40 % RH | ESD-POM, grounded via rod and bail | ≈ $10 |
| 16 | **Skids slide 18–60 m per session unledgered;** N1 circles | S1–S2 | Certain | Ledger skids; N1 as hops | $0 |
| 17 | **Breakaway order:** dowels lock shear (24 N); clip pops | S1–S2 | High | Short chamfered dowels or plug deletion (§11); longer loop | $0 |
| 18 | **Box heat on a cushion:** +16 to +28 K | S1 | Medium | Vents, quiet fan, cut idle power | ≈ $5 |
| 19 | **Circle tokens:** 40° plough in the example; ≈ 1.5 Hz ceiling | S1 | Certain on paper | Checker active in circle mode | $0 |

**What survives:** pressure × area pins, the palm float as the total cap, all-vent de-energised states, the puppet principle, the ear-axis bail and the dial cradle.

Fixes 2, 4, 5 and 6 are geometry the CAD WP must draw before anything is cut. Fixes 1 and 3 change two parts (the stick and the synchro charge) and belong in an ADDENDUM before Stage A2 and B.
