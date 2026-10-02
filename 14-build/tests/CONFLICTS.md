# TEST PROTOCOLS WP — CONFLICTS and testability requests

**Project SCRATCH · 14-build/tests · 2026-10-02**
SYSTEM-SPEC-v3.md is not edited. Each item below is a place where a spec or ruling pass line cannot be tested as written, or where a test needs something another work package has not specified. Each gives the operational definition that `test-protocols-v3.md` uses meanwhile and a proposed wording for a numbered ADDENDUM (spec §14). Numbers match test-protocols-v3.md §15.

## A. Pass lines not testable as written

| # | Where | Spec / ruling text | Problem | Proposed addendum wording | Decide |
|---|---|---|---|---|---|
| 1 | ruling §4 RC1(c); spec §10 B5 | "a real hair … to an HX711 at 1 kHz" | HX711 output rate is 10 or 80 SPS only (datasheet RATE pin). 12.5 ms sampling cannot verify "≤ 20 ms above 0.15 N". | "…to a load cell read at ≥ 800 samples/s (e.g. TAL221 100 g + ADS1115 at 860 SPS)". Cost ≈ $34 (Pico $4, ADS1115 $15, TAL221 $14.50). | Director |
| 2 | spec §10 A1; §4.1 V12 | "deadheads measured (P1 ≤ 50, P3 ≤ 30 kPa)" | in-box sensors are XGZP6847A 0–40 kPa; 50 kPa is off scale | add "measured with an external 0–15 psi gauge on a tee" to A1; BOM adds the gauge ($5–16) | BOM / DRIVE BOX |
| 3 | §10 A0; §7.1; §5.4 E3; H16 | "each element opens ACT-24 within 5 ms" | ACT-24 has 470 µF + TVS; with light load the bus voltage can take longer than 5 ms to fall even when K1 opens fast | "K1 contacts open ≤ 5 ms after any element opens (measured on K1's force-guided NC aux); ACT-24 < 2 V within 50 ms" and a bleeder (≈ 2.2 kΩ 1 W) on ACT-24 if needed | ELECTRONICS |
| 4 | §10 A3 | "PLINE never retraces within 2 mm in 60 s" | all PLINE strokes cross the centre; consecutive strokes are 4.5° apart (≈ 0.8–1.3 mm apart at the chord ends) and the heading comes back every ≈ 28.6 s. A literal reading fails by design. | "Over 60 s the ink rosette shows no heading gap > 15° and no trace visibly darker than its neighbours, and the `B` log passes the §8.4 no-repeat rule (tolerances ±1 mm, ±5 %, ±2°)" | Director / FIRMWARE |
| 5 | §6, §10 A5, §4.9 | "≤ 30 dBA at 1 m" | below a phone SPL app's floor and below typical room noise | "≤ 30 dBA at 1 m, background-corrected; where room noise exceeds 30 dBA, measured at 0.25 m minus 12 dB" | Director |
| 6 | §10 Stage A sensation | helper-held bench pad on Michael's head before B5/B6 | red line 12 needs a wig test and the checklist before *any* first session; red line 3 needs the total force set by a constant, and a helper's pressing hand is not one | "A-S requires HB-mini (HB-3/4/5/6 on the bench pad) and PHC-A (bench variant). The bench pad rests on the scalp under its own weight plus a slug, total ≤ 4 N measured; the helper only steadies it." PAD to provide a slug seat on the bench deck. | Director / PAD |
| 7 | ruling RC1(d) | "same with an e-stop and with a 10 mm reflex retract mid-snag" | v3 has no 10 mm partial retract (spec §1 C22) | "…with an e-stop, a latch trip (`inject snag`, full fail-to-free) and a lanyard pull" | Director (already implied by §7.3 deviation) |
| 8 | §7.3 RC4; §10 A4; §4.11 | "trip ≤ 50 ms" | start point undefined; with a real single hair, pluck (≈ 0.7 N) or break (≈ 1 N) happens near the 0.8 N firmware threshold, so the test measures the hair, not the reflex | "Tether = 0.25 mm monofilament to a load cell; time from tether force > 0.8 N to rail-sense low ≤ 50 ms (E or F layer, whichever acts)". Real hair stays in RC1(c)(d). | Director |
| 9 | §10 B1 | "moving group ≤ 125 g" | undefined | "moving group = carriage + float + pad (what the hand moves between stations; ledger 115.5 g)" | Director / HALO |
| 10 | §10 GO B | "≥ 7/10 … ≤ 3/10, zero pulls, nail count intact every session" | which session(s) the ratings come from is not stated | "End-of-session ratings at the 20-min session (B-S4), confirmed by ≥ 7 at one other B session or at B-S4's 10-min form; zero felt pulls in every B session" | Director |
| 11 | §10 B5; §7.4 H-5.5 | "matting run sets T_dwell" | no matting criterion | "Matting onset = comb-through force > 1.5× the pre-run value, a visible clump, or shed > 2× combing in a step; T_dwell = the last clean step of 30/60/90/120/180 s contact (cap 180 s)" | Director |
| 12 | §10 C5, A5 | "with pins up" | no command runs paths with the pad retracted (§8.6 diagnostics are valve/pump only) | FIRMWARE adds `dryrun on` / `dryrun off`: drums play the current mode, valves switch, PALM held off (pad retracted), only allowed with rail sense and the lever held; logged as `E dryrun` | FIRMWARE |
| 13 | §10 GO D | "≥ 7/10 … wants it again tomorrow; zero tuft pulls over 5 sessions" | aggregation not stated | "Over 5 consecutive Stage D sessions at Michael's preferred settings: median Q1 ≥ 7, median 'machine on my head' ≤ 3, 'again tomorrow' YES in ≥ 4/5, zero tuft pulls" | Director |
| 14 | §10 D5 vs §4.3 force budget | "F 0.2 / 0.3 / 0.45 N" | all-six-down is limited to ≈ 0.37 N per nail (Σ F_pins + 0.45 ≤ F_float); 0.45 N is only deliverable with one group down, so the firmware would clamp or reshape the group pattern and the arm is not what it claims | "The force block runs single groups alternating A/B with `bratio 1`" (or drop 0.45 → 0.37 N) | Director / FIRMWARE |
| 15 | §10 D5 | "stations moved by Michael vs by a helper" listed in the blind matrix | cannot be blinded | mark it open-label | Director |
| 16 | §10 S0, C5 | "earplug A/B indistinguishable" | no count or criterion | "10 random on/off trials; ≤ 7 correct" | S0 author / Director |
| 17 | §10 C7; §7.7 | "≤ 3 s (max ≤ 2.5 s)" | two limits; reading unclear | "every one of 10 trials ≤ 2.5 s" | Director |
| 18 | §10 B5 | "shed ≤ 2× combing" | normalisation not stated | "per 100 machine strokes ≤ 2× per 100 comb strokes; any 5-min block with > 5 bulb hairs is a stop-and-look item" | Director |

## B. Testability requests to other work packages (additions, not deviations)

| To | Request | Needed by |
|---|---|---|
| FIRMWARE | `dryrun` (item 12) | A5, C5 |
| FIRMWARE | a hold at block d = 0 with pins pressurised (`hold centre`), pad on the head side retracted only by command | HB-1 static reach |
| FIRMWARE | a loop macro for 1,000 vent/re-pressurise cycles (e.g. `cal lines cycles=1000`) | A2.6 (RC1 b) |
| FIRMWARE | `blind` / `bset` / `next` / `reveal` documented with exact syntax and usable from one hand-controller key | D5, A-S |
| FIRMWARE | contact-seconds per station shown in `status` (for HB-9 matting steps) | HB-9 |
| ELECTRONICS | ACT-12 test LED (5 mm, 1 kΩ) visible on the box face, and a 2-pin test header with ACT-12 and GND for the logger's rail sense | R-3, A4, B4 |
| ELECTRONICS | K1 aux NC brought to a test header | A0 |
| ELECTRONICS | bleeder on ACT-24 if A0 shows > 50 ms decay | A0 |
| PAD | nail-reach line painted on the pad skirt (radius from the C8 CAD sweep) | C4 |
| PAD | printed nail shadowgraph template and a 34° rim angle template | A2.3, A3 |
| PAD | a slug seat on the bench deck (A-S ≤ 4 N by weight) | A-S |
| PAD | nail ID marks (N1–N6, S1…) on each shaft top | A2, B3, PHC-B |
| PAD / HALO | a hook or eyelet on the yoke and on the block for the pull tests | A3 rim reaction, B2 coupling |
| HALO | the α/β zero gauge readable to ±2° | C1, C4 |
| BOM | test-only kit ≈ $230 (test-protocols-v3 §1): Pico, ADS1115, TAL221 100 g and 500 g, 0–15 psi gauge, pocket scale 0.01 g, two real-hair heads, Kanekalon, feeler set, manometer tube, hygrometer, IR thermometer, small parts | Carts 2 and 3 |
