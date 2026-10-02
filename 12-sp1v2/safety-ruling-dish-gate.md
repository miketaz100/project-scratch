# SAFETY RULING: dish-gate snag pull (leap4-A L3-2)

**Project SCRATCH · 12-sp1v2 · Red Team 2 (safety continuity) · 2026-10-02**
**Read:** leap4-A (§1.3, §4, §7), redteam-2-mechanical (all), SYSTEM-SPEC §7, hair-interaction (all), safety-requirements (all), decision-analysis must-fix list.
**Tags:** [KNOWN] from a project file · [EST] my arithmetic (`snag.py` in the session scratchpad) · [JUDG] judgement · [VERIFY] needs the bench.

---

## 0. Ruling

**ACCEPT WITH CONDITIONS.**

The author's 0.5–0.6 N figure is the **sustained** pull after a vent. It is not the worst case. The worst case is a strand caught **during rim lift, before the vent**. The block is rigid, so every other pin still on the skin pushes it up into the strand through the snagged pin's stop. That is **0.8–2.9 N** across the operating rail, and up to 5.2 N at the relief, against a baseline lift pull of 0.05–0.31 N.

None of the four proposed mitigations bounds that transient mechanically.

One cheap part does: an **axial magnetic breakaway at each piston–shaft joint**, set at 0.12–0.25 N.
- In every normal state that joint is in compression.
- It goes into tension only when a strand pulls a nail toward the scalp.
- It therefore caps the lift-direction pull on any strand at ≤ 0.25 N, as a mechanical constant, in every state: contact, rim, reflex, fail-to-free and doff.

For the dish gate it **replaces** RT2's "reserve ≥ 12 mm" must-fix. The reserve only covered the 10 mm reflex retract. The breakaway also covers fail-to-free and doff.

Seven more conditions follow (§4). One of them is new and unrelated to snags: the 12 mm stroke halves the margin before a pin bottoms, and red line 2 depends on that margin.

---

## 1. The snag scenarios, quantified

### 1.1 Free body [EST]

**Inputs.**
- **Block:** 35 g, so W = 0.34 N. Its component toward the scalp, W_n, is +0.34 N at the vertex, 0 at the sides, and −0.11 N at the low occiput (α 108°).
- **Lift tension:** T = 0.5–0.6 N.
- **Pins:** force F = 0.08–0.50 N (firmware limit 0.60, relief 0.96); return spring f_s = 0.03 N; reserve 1–3.5 mm; stroke 12 mm.
- **Hair:** a hair-plus-scalp tether is stiff, about 0.3–1.5 N/mm (EA ≈ 15 N over 10–40 mm, plus skin tenting).

**Snagged pin at its stop.** When the stop catches a strand that holds the nail down, the stop passes −H to the block, where H is the strand pull. While the block is pulled off the dish, nothing but the strand resists the net upward force:

> **H = T − W_n + Σ_others (F_i − f_s)**

Here Σ_others counts the pins still on the skin. Before the vent that can be all five; after the vent it is none.

Tilt about the trailing domes relieves H by ≈ ×0.5–1.0 [JUDG]. The ceiling rises ≈ 66 mm/s on the 38° band, so H builds over 15–80 ms, then holds.

**Thresholds** [KNOWN, hair-interaction §1.8, safety-requirements §2.3]:

| Load on one hair | Meaning |
|---|---|
| 0.05–0.1 N | felt tug |
| 0.15 N | H-4.11 mount-yield target |
| 0.3 N | design pluck floor |
| 0.36 N | anagen, slow extraction |
| 0.53 / 0.70 / 0.85 / 0.94 N | epilation: telogen / mean / anagen / occipital anagen |
| 0.3 N delivered in 10 ms | a pluck (H-5.4) |
| 2 N over ~50 hairs | a tug, not an injury |

### 1.2 Scenarios (fixed-spring T plus the author's mitigations, against baseline and against condition C1)

| # | Scenario | Pull on the strand (dish gate as proposed) | How long | Verdict | Baseline (with must-fixes) | With C1 breakaway |
|---|---|---|---|---|---|---|
| S1 | **Single strand, contact zone** (\|d\| ≤ 7, ceiling flat), tangential drag | Synchro lag at 1.0 N/mm → 0.8 N trip, then 30 ms latency → up to the 2.5 N synchro relief, **tangential**. No vertical component. | 10–50 ms rise; afterwards the **synchro lag load persists** while the master holds | pluck likely | **Same** (rigid shaft; H-4.11 scores 1 in every design) | tangential unchanged; vertical ≤ 0.25 N |
| S2 | **Single strand, reflex retract after the vent** (float up 10 mm) | Reserve of 1–3.5 mm used, then the block lifts off the dish onto its 12 mm free travel: **T − W_n = 0.16–0.26 N (vertex), 0.50–0.60 (sides), 0.61–0.71 (low occiput)**. Without free travel: float spring minus pad weight, 0.7–2.25 N | **sustained until doff**: seconds to minutes | above the 0.3 N floor at the sides and occiput, so a pluck within seconds | ≤ 0.05 N while the 12 mm reserve lasts | ≤ 0.25 N for < 20 ms, then the nail drops free |
| S3 | **Small bundle (5–10 hairs)**, contact, then reflex | Tangential 0.8–2.5 N ÷ n = 0.08–0.5 N per hair (transient); then T ÷ n = 0.05–0.13 N per hair sustained | as S1 and S2 | some plucks at the top end; sustained part is only a tug | same transient | ≤ 0.05 N per hair vertical |
| S4 | **Rim lift** (\|d\| 8.3–11.5): the snagged pin reaches its stop first, five others still pressing | **U = 0.80 / 0.90 / 1.65 / 2.90 / 5.20 N at F = 0.08 / 0.10 / 0.25 / 0.50 / 0.96 N** (sides; tilt relief takes it to ≈ 50–100 %) | ramp 15–80 ms, then held until the pins vent. With a trailing strand the drag trip comes ≈ 40–60 ms in, plus 50–100 ms of line exhaust. **With a near-vertical strand there is no tangential signal**, so it is held for the rim dwell (≈ 100–200 ms) and **repeats every stroke** | single hair: certain pluck. Bundle: 0.1–0.5 N per hair, a **tuft-pull event** (stop and redesign) | hover 0.05–0.13 N, park 0.31 N | ≤ 0.25 N (+ ≤ 0.1 N bush friction), ≤ 20 ms, released |
| S5 | **Fail-to-free with a snag** (power loss or e-stop) | Pins vent through the line (50–100 ms; **≈ 1 s if the 250 ml accumulator sits downstream of the PIN valve**). Float QEV retracts 25 mm in 60–90 ms. The float can outrun the pin vent, so S4's U can appear first; then T; then the float spring once free travel runs out: 0.7–2.25 N **indefinitely** | until doff | pluck or tuft | float spring after 12 mm (same end state) | ≤ 0.25 N, released |
| S6 | **Doff with a snag** | the hand's pull, tens of N | seconds | tuft | same | ≤ 0.25 N per caught nail |

### 1.3 What the leap missed [EST]

1. **The other pins' air.** Venting removes it, but S4 happens before any vent. In the baseline it is never carried, because per-pin valves lift each pin on its own and no stop lifts a held nail. On the dish it can be carried. That is the real change, not T.
2. **Vertical snags are invisible to the drag sensor.** It reads only the tangential part. On the rim, the 1.6–1.7 N rim reaction also sits in the drag baseline, so a "3× baseline" trip there means about 5 N. Unless the rim load is modelled out, the firmware layer is weakest exactly where the new hazard is.
3. **Accumulator placement.** Downstream of the PIN valve, 250 ml through a Ø 0.8 exhaust takes ≈ 1.0 s to fall from 13 to 1.3 kPa. Upstream, only ≈ 8 ml of line and gallery has to leave, ≈ 40–100 ms. leap4-A does not say which.

---

## 2. Mitigations evaluated

| Mitigation | What it bounds | What it misses | Verdict |
|---|---|---|---|
| **A1** Drafted cone, no neck | Likelihood of capture. A loop pulled toward a tip that narrows loosens and slides off as the nail rises. | No bound on force once captured. As written ("drafted cone on a Ø 1 shaft") it can still be a **mushroom**: a Ø 4–5 cone under an exposed Ø 1 shaft is a neck (RT2 §1.1). Credit it only if the profile never narrows anywhere from tip to nose. | **Required, not sufficient** (C2) |
| **A2** ≥ 12 mm block free travel | The reflex retract pull, at T − W_n | 0.5–0.7 N at the sides and occiput is above the pluck floor and sustained; no effect on S4. Also, a limp block at the vertex sinks toward the scalp, so the 30 mm exclusion becomes a CAD fight. | **Not required** if C1 is fitted. Do not build it. |
| **A3** Snag reflex = stop + vent | S4 after detection | Firmware only (red line 13). Blind to vertical snags; masked by the rim load. | **Required as the F layer** (C4) |
| **A4** Inverted pin cartridge drives T (vent → limp) | Sustained T after a vent: ≤ 0.1 N | On the PIN line, T scales with the rail. At 2 kPa (≈ 0.08 N on a pin) that cartridge would pull ≈ 0.1 N, too weak to carry the 0.34 N block at the vertex; at 13 kPa it pulls 6.5× more. When group A sits out it vanishes. S4 still happens. | **SP2 recommendation**: a palm-line *latch* holding a fixed spring's anchor (T set by the spring, its presence gated by air) |
| **B1** Compliant link, T ≤ 0.3 N | — | Cannot carry the 0.34 N block at the vertex; misses S4 | **Reject** |
| **B2** Magnetic breakaway of the *block* | Sustained part | Peak is still T(0) + Σ others | **Reject** for C1 |
| **B3** Rim lifts the block (cam floor) | — | Whatever raises the block pulls the strand; a cam puts the float force (3–5 N) on it | **Reject** |
| **B4** Nose geometry | Capture at the nose | A taper through a wiper is a changing gap | **Required** (C2) |
| **NEW: axial magnetic nail breakaway** (piston face magnet holding the steel shaft end, above the nose) | **Every lift-direction pull, every state, mechanically, ≤ B** | Tangential snags (unchanged from baseline); a dropped nail lies in the hair | **Primary** (C1) |

**Why the breakaway works.**
- In normal running the piston–shaft joint is only ever compressed.
- Its largest service tension is min(return spring, wiper and bush friction) ≈ 0.03–0.05 N on a vent retract; shaft weight, hair drag on exit and rim-fillet acceleration add < 0.015 N.
- So 0.12–0.25 N sits 2.5–5× above service loads and at or below the pluck floor.
- A228 music wire is ferromagnetic: a Ø 3 × 2 magnet in the piston, ≈ $1 per pin. It is must-fix #1's "breakaway above the nose", specified in the axis that matters on the dish.

---

## 3. Red lines and hair checklist: dish gate (with conditions) against the baseline with must-fixes

| # | Red line | Change from baseline | Status |
|---|---|---|---|
| 1 | No rotation or open slot within 30 mm | Domes and PTFE ride ≥ 70 mm up. The block now rises 8.5 mm and tilts 5.5°, so the block–deck gap changes, but at ≥ 32 mm. | Pass; C8 CAD |
| 2 | ≤ 2.5 N per element, by a mechanical constant | Reliefs unchanged; line B's PWM servo must sit downstream of R1a/R1b. **New:** retraction margin falls from 20 mm to 8.5–11 mm. A 10° pad tilt across 50 mm (a skid dropping off an edge) or a finger bottoms a pin, and then the float's ≤ 7.8 N rides on one Ø 2 flat (≈ 2.6 MPa). | **Conditional** (C3, C6) |
| 3 | ≤ 12 N total; ≤ 2 N tangential per element | Total unchanged; T is internal to the pad. The rim reaction (≈ 1.7 N) uses up part of the 2.5 N synchro cap. | Pass (must-fix p₀) |
| 4, 5 | E-stop; mains and lithium | none | Pass |
| 6 | Hairline, ear, eyes | Amplitude 15 → 15.5 mm; tilt swings nail tips ≈ 3–4 mm | Pass; C8 adds both to the fence CAD |
| 7 | No self-locking drive in the force path | none; the XY master is relief-capped in the box | Pass |
| 8 | Free on any fault | Float QEV retracts 25 mm; fixed T keeps the block seated, so nails rise with the deck. Pin vent now passes through 1.4 m of line. | Pass with C3 |
| 9 | Retention, 3× proof | The joint changes: compression proof ≥ 3.1 N on the face, lateral ≥ 3 × 1.0 N in the guides; axial tension is a deliberate breakaway (H-4.13). This is magnet plus mechanical pocket, which §3.6 allows. | Pass with C1 wording |
| 10 | Doff, strap, ≤ 500 g | 362 / 463 g, better than baseline. A doff with a snag now releases nails instead of pulling tufts. | Pass, improved |
| 11 | Edges | A dropped shaft's top end must be domed | C1 |
| 12 | Procedure | add a per-session breakaway check and a nail count | C1 |
| 13 | Firmware never alone | Lift before reversal moves from six valve latencies plus a scheduler (E/F) to rim geometry (M) plus a path checker (F). Snag pull moves from reserve geometry to the breakaway (M) plus the reflex (F). | **Improved**, with C1 |

**Hair checklist H-6.8** (gating items 1–7):

| Item | Score | Note |
|---|---|---|
| 1 Rotation | 2 | |
| 2 Joint methods | 2 | |
| 3 Changing gaps | 2 | needs the C8 tilt-inclusive skid CAD |
| 4 Lift before reversal | **1** | nails rise 5–7.5 mm, still in the pile, as with baseline hover; now set by geometry |
| 5 Rigid group | 2 | |
| 6 Drafted nail | 2 | only with C2 |
| 7 Yield ≤ 0.15 N | **1** | tangential is unchanged; pull-off improves to ≤ 0.25 N |

Non-gating: 8 → 1; 9, 10 → 2; 11 → 1; 12 → 2 (widens above the guard); 13–15 → 2; 16 → 1 (no PTFE in the pile); 17 → 2; 18 → 1.

**Total ≈ 30/36, no gating zero.** Same as RT2's fixed baseline (≈ 30). Items 4 and 7 stay at 1 by design, as the project already accepted.

---

## 4. Conditions: must-fix requirements for the design freeze

| # | Requirement | Bench test that verifies it |
|---|---|---|
| **C1** | **Axial nail breakaway.** Each shaft is held to its piston by a face magnet above the nose, laterally located only by its two guides. Release in axial tension at **0.12–0.25 N** per nail, ≤ 0.35 N with 0.5 N tangential at the tip, and **B_min ≥ 3× the measured aged wiper and bush friction**. The released part is one piece (cone + shaft), untethered, both ends radiused ≥ 0.5 mm, red or orange. The wiper recloses. **Replaces RT2's reserve ≥ 12 mm for the dish gate**; the reserve stays 1–3.5 mm. | (a) Kitchen-scale pull on a monofilament loop at the cone, 10× per nail on all 12 + spares: 0.12–0.25 N; repeat with a 50 g side load. (b) 1,000 vent/re-pressurise cycles and a 20-min wig PLINE: **zero nuisance releases**. (c) **Rim-snag tether:** a real hair looped on a nail at the lift zone, to an HX711 at 1 kHz, PLINE on the R 85 ball at F = 0.25 and 0.50 N: peak ≤ 0.30 N, ≤ 20 ms above 0.15 N, nail released. (d) Same with an e-stop and with a 10 mm reflex retract mid-snag. (e) Per session: a 25 g hang test on each nail must release it, and the nails are counted after the session. |
| **C2** | **Nail profile monotonic from tip to nose** over the whole stroke: 90° tip cone from a Ø 2 flat (R 0.4) to Ø 4–5, then a taper of ≥ 2° per face or a constant stem. No section is ever narrower than any section below it. A cylindrical wiper land runs ≥ stroke + 3 mm. No shoulder reaches within 3 mm of the nose at full retract. | Shadowgraph against a printed template. Loop test: a slip loop of real hair around mid-stem, block lifted 10 mm by hand, loop sheds 10/10 (a load cell reads ≤ 0.1 N before C1 acts). Hair §7.3.3 reversal test: zero loops in 50 D-path and line strokes. |
| **C3** | **Vent path.** The 250 ml accumulator sits on the **rail side** of both PIN valves. Both PIN valves are normally closed to the rail and vent when de-energised. Line B's PWM servo is downstream of R1a/R1b. Gallery force falls below 0.05 N (< 1.3 kPa) **≤ 100 ms** after de-energise; if not, fit a gallery QEV. The Ø 0.15 gallery bleed takes a kinked, pressurised line below 2 kPa in < 1 s. | Temporary sensor tee at the gallery: scope trace of the de-energise on both lines; kinked-line bleed timing; Stage A relief calibration with line B at 100 % servo duty, ≤ 1.04 N per nail. |
| **C4** | **Dish snag reflex.** Vent PIN A and B, master holds (never reverses), float retracts 10 mm, log, and prompt a nail check. The drag baseline **subtracts the modelled rim reaction** as a function of d and F, so the 0.8 N absolute trip applies on the rim. | Wig tether at the centre and at the rim: trip ≤ 50 ms. 20 min each of PLINE, D-paths and CIRCLE with no tether: zero false trips (RT1 #11). |
| **C5** | **Gate geometry.** The landing band of the rim is ≤ 35° (print 33–35°; H-5.3 and spec §4.1). Lift is ≥ 5 mm at the worst reserve. Lift happens at ≥ 0.3 v_peak. The path checker, active in every mode (line, PLINE, D, chords, offset circles, hops), rejects any token that reverses inside \|d\| < 12.8 mm. | 240 fps phone and feeler gauges on the R 85, R 65 and 70 × 150 mocks. Checker unit tests with deliberately bad tokens. |
| **C6** | **Retraction margin ≥ 15 mm** from contact to the retract stop at the worst residual curvature (stroke ≈ 18.5 mm, ≈ +2 g per pad), or a series overtravel spring capping a bottomed nail at ≤ 2.0 N. | Calipers at each pin on all three mocks. Bottoming test: a 15 mm block under each nail with the float at R2b; load cell ≤ 1.04 N. |
| **C7** | **Vented pins retract fully:** return spring ≥ 2× the aged wiper and bush friction, so a sat-out group does not drag through reversals at near-zero force. | With group B vented, every B nail retracts ≥ 8 mm within 200 ms at the vertex and sides, both new and after a 20-min run. |
| **C8** | **CAD:** nail–skid ≥ 8 mm including 5.5° tilt and 8.5 mm rim rise. The ear and hairline fence includes the 15.5 mm amplitude and the tilt reach. The block–deck gap is > 3 mm (or booted) and ≥ 30 mm from nominal skin at every block pose. | CAD sweep over (ψ, d, tilt); feeler check on the Stage B pad. |

**Recommended, not required:** a palm-line latch that makes T present only while the palm line is pressurised (A4 done right). It adds a second mechanical layer under C1 for the sustained S2/S5 load. Re-evaluate at SP2.

---

## 5. Residual risks accepted

- **Tangential snags (S1)** still load a single strand to 0.8–2.5 N for 10–50 ms, unchanged from baseline (item 7 = 1). Holding the master leaves the synchro lag on the strand; a firmware back-off by the measured lag is NICE, never credited.
- **A dropped nail** is a blunt 0.3 g part loose under the pad (S1–S2), undetectable on a sensor-free pad; covered by the C4 prompt and the count.
- **Capture likelihood** rests on C2 and geometric lift; item 4 stays at 1 until the lift clears Michael's measured pile.
