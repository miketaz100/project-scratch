# LEAP 4-B: Make the scratch itself better than a person's

**Project SCRATCH · 11-leaps/round-4 · Agent B · 2026-10-02**
**Read:** LEAP4-BRIEF; DECISION-2 (incl. NORTH STAR AMENDMENT); decision-analysis; SYSTEM-SPEC (nail, valves, rail, scrub tables); redteam-1/2/3 (grep and key sections); scratch-model §1–3, §7–8; tip-interface (all); hair-interaction §4–5; safety-requirements §2, §7; prior-art §2–3; leap-A (round 1). Skimmed the round-2/3 headings. Firewall kept: no other round-4 file read.
**Tags:** [KNOWN] = cited · [EST] = my arithmetic · [JUDG] = judgement · [VERIFY] = bench it.

---

## 0. What "better than a person" can mean inside the red lines

Under the amendment the target is a scratch rated ≥ 7/10 against "being scratched well". That lets the machine beat a person on some dimensions so it can afford to lose on others (no warm hand, no social cue). Before listing leaps, here is what the constraints already rule out.

**Sharper is illegal.** A filed human nail edge has a radius of about 0.15–0.3 mm (tip-interface §1.1). Red line 11 forbids any tip radius under 0.4 mm. So "a crisper edge than a fingernail" cannot come from radius. It has to come from four other places:
- **line load:** force per mm of loaded rim (window 0.05–0.15 N/mm, tip-interface §2.5);
- **friction and stick-slip:** the skin-fold release at 10–100 Hz is what reads as crisp (tip-interface §2.6);
- **timing:** onset and release transients;
- **sound.**

**Denser is not a lever.** A person gives ≈ 4 nails × 120 mm/s × 0.6 duty ≈ 290 mm/s of edge track, ≈ 4,000 root deflections/s (scratch-model §2.3). The 6-pin baseline in PLINE at 1.4 Hz gives ≈ 21.75 mm of contact per half-stroke × 2.8/s × 6 pins ≈ 365 mm/s, ≈ 4,400 deflections/s [EST]. It is already at par. More dose per spot is capped by:
- abrasion (≤ 50 passes/min/spot);
- matting (H-5.5, ≤ 8 strokes per patch);
- CT fatigue (10–30 s refractory).

**Where a machine can beat a person:**
1. **Edge consistency.** Nail keratin falls from E ≈ 3 GPa dry to 0.2–0.5 GPa at 100 % RH (scratch-model 3.11c [KNOWN]), so a human nail softens on a humid, sebaceous scalp. POM does not.
2. **Endurance.** Minute 20 equals minute 1.
3. **Exact per-stroke force shaping.**
4. **Variety of edge on demand.**
5. **Targeting an itch the scratcher cannot feel.**
6. **Engineered sound.**

The honest headline: **the scratch-quality levers are tips and firmware on top of the baseline. They move P(on-par) by about +0.08 for ≈ 12–15 h and ≈ $50, not by a factor.**

---

## LEAP B1: THE MIXED HAND. Six different edges, not six copies of one

**(a) Assumption broken.** That all pins carry the same nail, chosen beforehand by A/B on a wand, and that pin subsets only change *where* the pad scratches.

**(b) Principle and sketch.** The pins become a palette of 2–3 edge types. Every cartridge stays one-piece and drafted ≥ 10° (H-4.3), with every rim R ≥ 0.4 (red line 11). Firmware subsets then select the **character** of the scratch as well as its place.

```
 pad (centre + pentagon R 18), seen from the scalp

            W                 K  "keystone":  Ø 1.2 flat, R 0.4 rim, 20° draft -> Ø 4 at 2.5 mm
       S         S                loaded arc ~1.8 mm; run 0.15–0.22 N -> 0.08–0.12 N/mm
            K                 S  "standard":  Ø 2.0 flat, R 0.4 rim (baseline cone), 0.20–0.25 N
       W         S                loaded arc ~3 mm -> 0.07–0.08 N/mm
                              W  "wide arc":  Ø 3.0 flat, R 0.6 rim, 15° draft -> Ø 5 at 2.5 mm
                                  loaded arc ~4.5 mm; run 0.30–0.35 N -> ~0.07 N/mm, broader root sweep

 subsets:  DIG = K alone or K+S (short, crisp, itch work)    SCRATCH = all six
           SOFT = W+W+S (pleasant rake, more hair, less bite) MATERIAL A/B = S(POM) vs S(PA6)
```

Second axis, material. The S positions can carry different materials: POM (baseline) or PA6, both polished to Ra ≤ 0.8. PA6 is hydrophilic, takes up 2–3 % water, and has higher surface energy, so its adhesive friction on sebum-wet skin is higher [EST]. A polished buffalo-horn cone (real keratin) is an optional fourth arm.

**Do not roughen the rim to make it "grab".** For skin, friction *falls* as counterface roughness rises, with a minimum near Ra ≈ 4 µm, because adhesion dominates (Derler; Tomlinson; skin–counter-material study, JMBBM 2019 [KNOWN]). A matte rim would make the scratch slipperier, not crisper. A rough rim also breaks H-4.8. Grab comes from material and polish, not texture.

**(c) Numbers moved.**
- **G1 (crisp edge at the right force): 0.75 → ≈ 0.83.** G1's largest residual risk is that the tip picked on a wand is wrong in his hair at minute 10. Three edges on the head hedge that, and the in-situ A/B converges during real sessions.
- **G4 (no habituation): +0.03–0.04.** Switching stimulus *class* (DIG ↔ SCRATCH ↔ SOFT) rests one afferent population while another works; jitter inside one class cannot (leap-A L4; Vallbo 1999 CT fatigue; Triscoli 2014 satiety at the most pleasant setting).
- **Cost** +$15–25: Ø 5 POM and PA6 rod; optional horn picks or blanks.
- **Hours** +4–6 (turn and polish ~24 sticks), partly recovered from a shorter wand A/B.
- **Mass** ±0.2 g.

**(d) Plausibility.**
- **Line load.** K at 0.2 N over 1.8 mm gives 0.11 N/mm, inside the window, but K must run lighter than S. That needs per-pin force, which B3 supplies; without B3, K gets a smaller piston bore (Ø 6 instead of Ø 7: area −27 %).
- **Hair.** K's 20° draft sheds hair at least as well as the 10° baseline; W parts hair less, by design.
- **Making them.** Drill-chuck turning (rod in a cordless drill, file to a printed form gauge, 600 → 2000 wet, polish). No lathe needed.
- **Safety.** 3× proof load per stick (red line 9); rim checked with a loupe against a 0.8 mm drill shank.

**In-situ blind A/B (firmware, 2–3 h).** Over 20 s, the bar engine alternates two subsets that differ in one variable only (K vs S, POM vs PA6, W vs S). Michael presses THERE (or a new BETTER button) for the one he prefers. He cannot know which edge is which. Fifty votes over 3–4 evenings settle each pair at roughly 70/30 discrimination [EST]. This is the tip-interface T3 protocol run on the real machine with no helper.

**(e) Cheapest test (< $30, one weekend, helper).** A **spring-pen wand**: a printed pen body with a click-pen spring (~0.3–0.4 N/mm) behind a Ø 1 shaft, taking the three cone types (K, S, W in POM) and S in PA6.
1. Practise each force on a kitchen scale: K 0.2 N, S 0.25 N, W 0.35 N.
2. The helper runs 12 blinded pairs, 20 s each, crown and occiput, in both orders.
3. Michael names the more satisfying of each pair and rates each 0–10.

**Decision rule:** if ≥ 2 types each win ≥ 1 region or ≥ 1 rating dimension (crisp vs pleasant), build the mixed hand. If one type wins everything, fit six of it and keep the others as the swap palette.

**(f) Replaces.** The single cone spec (one cone, 6 copies) and part of the S0/B-stage tip A/B. Nothing structural changes.

**(g) Why it might fail.** At R ≥ 0.4, edge differences may be below what Michael can feel through hair; then B1 costs only the turning hours. Per-pin force calibration gets more complex. PA6 friction drifts with humidity.

---

## LEAP B2: ITCH HUNTER. Tease, dig, smooth: scratch the itch a person cannot find

**(a) Assumption broken.** That the device delivers good touch to a neutral scalp, and that THERE just means "stay here".

**(b) Principle.** Scratching's strongest measured pleasure is itch relief: pleasure tracks itch intensity (bin Saif 2012 [KNOWN]). The spinal inhibition from scratching is **state-dependent**. Scratching inhibits primate spinothalamic itch neurons only while they are in an itch state, and the inhibition lasts **≈ 30 s** before activity returns (Davidson et al., *Nat Neurosci* 2009 [KNOWN]). Everyday scalps carry micro-itches. A helper cannot feel them; Michael can point to them. ITCH HUNTER is a three-phase firmware mode.

```
 THERE pressed ─► [optional TEASE 1–2 s] ─► gap 0.3–1.2 s (random) ─► DIG 3–6 s ─► SMOOTH 2–4 s ─► back to score
                   hovering S/W pins swept       anticipation           K (+S) bite       W+S, one with-grain
                   through the pile at 5 mm,                            12 mm strokes,    40–80 mm/s sweep, lifted
                   NO skin load (mid-shaft                              2.5–3 Hz,         return (P2 primitive)
                   hair bending = itch/tickle,                          cross-hatch: two
                   Fukuoka 2013)                                        headings 90° apart,
                                                                        alternate each stroke,
                                                                        K 0.22 N peak (B3 envelope)
 revisit rule: re-offer DIG on the same patch after 25–40 s (the ~30 s inhibition window), at most 3×
```

The key move reuses RT1's hover-comb defect **as a deliberate tease.** Hovering pins brush hair at mid-shaft, the known *mechanical itch* stimulus (Fukuoka, Miyachi & Ikoma, *Pain* 2013; Fatima et al. 2026 [KNOWN, via leap-A]). Gated to 1–2 s before a DIG on the same patch, and opt-in, it makes the itch the DIG relieves. Zero hardware.

**Why the DIG is shaped that way:**
- **Short and fast:** 12 mm at 2.5–3 Hz gives a peak of ~95–115 mm/s.
- **Cross-hatched**, so successive strokes cross fresh fold lines.
- **Focal (K)**: itch scratching runs harder and faster (Padmanabha 2023 [KNOWN]: 1.56 N per finger at ~178 mm/s). K's short arc delivers that intensity in line load, not newtons.

**(c) Numbers moved.**
- **G5 (stays where wanted, steering): 0.85 → ≈ 0.88.** THERE now produces a distinct, satisfying response, not just a stop.
- **G4: +0.02.** A new stimulus class with its own build-up and release.
- **Cost** $0. **Hours** +3–4 firmware: a phrase type in the existing JSON score, the cross-hatch heading toggle on the XY master, and a 30 s revisit timer in the safety ledger.
- **Mass** 0.

**(d) Plausibility.**
- **Hair.** Heading changes only while lifted (H-5.2). 12 mm strokes are under H-5.1's 25 mm against-grain limit, so the cross-hatch is allowed.
- **Dose.** 3–6 s at 2.5–3 Hz is 8–18 strokes on one patch. **That exceeds H-5.5's 8**, so DIG is capped at 8 strokes per heading pair (≈ 3 s), then the pad shifts 20 mm and the revisit timer starts. Abrasion: 8 passes in 3 s, then nothing for ≥ 25 s, is ≈ 16 per minute, under the 50/min rule.

**(e) Cheapest test ($0, one evening, helper).** The helper holds a stick (B1 test wand) and a size-0 paintbrush. Twelve trials, sites rotated across nape, behind the ears, hairline and crown. Random order:
1. Michael points to any itchy or wanting spot; helper does a DIG (short, fast, cross-hatched, ~5 s) there;
2. normal scratching at the same spot;
3. brush-tease 1.5 s, then DIG;
4. DIG 5 cm away from the pointed spot.

Rate satisfaction 0–10 after each. **Rule:** 1 beats 2 by ≥ 1.0 → build DIG. 3 beats 1 by ≥ 1.0 at ≥ 2 sites → make tease opt-in.

**(f) Replaces.** The "THERE = STAY" behaviour of the hybrid. It also turns RT1's hover-comb defect into a gated feature.

**(g) Why it might fail.** Without real itch, DIG may just feel harsher. The tease can leave a lingering itch (alloknesis), so it stays opt-in. Asking for relief by button may break immersion.

---

## LEAP B3: ENVELOPE STROKES. Attack, peak, release, written per pin, per stroke

**(a) Assumption broken.** That force is constant through a contact (rail pressure × area, with the rail slewing only between strokes: ≤ 60 ms up, ~20 kPa/s down), and that the stroke has a sinusoidal speed profile.

**(b) Principle.** Fast-adapting afferents (hair units, field units, RA) report **change**: the onset (the fold forms) and the release (fold and hairs spring back). A nail does this roughly; the machine can do it exactly on every pin. **High peak force for crispness, low mean force for comfort.** Mean force is what drives abrasion, hair drag and the force-related drop in pleasantness at speed (bioRxiv 2026 force study: pleasantness falls with force, more steeply at higher velocity [KNOWN, abstract]).

**Mechanism, with no new hardware.** Each pin has an S070 3-port valve (3 ms open and close [KNOWN datasheet]), a ~5 ml PU line, and an inlet restrictor with a free-venting duckbill. A **stepped-vent envelope** works like this:
- the pin bites at full rail pressure (peak);
- at 40 % and 70 % of the contact, the valve vents for 3–6 ms and recloses;
- the line volume and restrictor low-pass each step into a ~20 ms ramp, so force falls in two steps to ~45 % of peak before the lift.

```
 force per pin (S tip)                          speed (XY master, contact segment)
 0.30 N |   ___                                 150 mm/s |    ____________________
        |  /   \__        attack ≤ 20 ms        (power   |   /                    \   lifted turnarounds
 0.20 N | /       \___    decay in 2 steps       stroke) |  /                      \  at up to 3 m/s²
 0.13 N |/            \__ (vent 3–6 ms pulses)           | /                        \ (H-5.4 binds only
        +-----------------\--> lift at s=0.85            +-----------------------------  in contact)
         land    40%  70%                                  land                  lift
 mean ≈ 0.22 N vs peak 0.30 N  (mean/peak ≈ 0.73)        all contact at 140–160 mm/s (Padmanabha med–high)
```

That is 2 extra valve clicks per contact, not a PWM buzz. It keeps the box noise budget (12 S070 clicks ≤ 20 dBA) and valve life: ≈ 3,400 contacts per pin per 20-minute session × 2 ≈ 7,000 extra cycles. Variants for anti-habituation:
- **crescendo** (land at 60 %, add a fill pulse mid-stroke): the "dig-in" for DIG;
- **flat** (control);
- **decay** (default).

All are drawn per stroke from the score, adding a new jitter dimension that the RT1 "crank clock" fix lacks.

**Speed half.** The XY master runs a trapezoid: constant 140–160 mm/s in contact, turnarounds lifted (H-5.4's 2 m/s² binds only in contact). At 3 m/s² lifted, a 30 mm half-stroke at 150 mm/s takes 0.25 s: a 2 Hz cycle with ~25 mm of constant-speed contact [EST]. The gain is modest (the sinusoid already averages ≈ 115 mm/s in contact), but **every millimetre is in the human scratch band** (112–178 mm/s, Padmanabha 2023). It also allows a **power stroke** (bite outbound, return lifted), halving passes per spot so the pad can dwell longer where it is liked.

**(c) Numbers moved.**
- **G1: +0.03** (peak crispness without a higher mean).
- **G2: +0.01**.
- **G4: +0.02** (envelope class per stroke).
- **G3: −0.01** risk (valve clicks).
- **Cost** $0, plus about $35 for one spare S070.
- **Hours** +4–6: envelope generator in the 1 kHz valve queue, bench verification on the S0 rig with a load cell, trapezoid path in the XY stage.
- **Mass** 0.
- It also supplies B1's per-pin force (a steady-state duty, or one early vent step for K).

**(d) Plausibility.**
- **Valve speed is not the limit; the line time constant is** (~15–40 ms [VERIFY]). A 150–250 ms contact holds 4–8 such time constants, enough for one attack and two decay steps.
- **Floor.** RT1's 0.20 N crispness floor applies at *peak*; the tail may go lower, since the release is the point.
- **Relief cap untouched.** Peak force is still bounded by the rail's mechanical relief (red line 2).

**(e) Cheapest test (+$0 on the S0 one-nail rig, plus ~$12 for a 1 kg load cell and HX711).**
1. **Bench.** Program decay, crescendo and flat. Log force at 1 kHz on the load cell under the rig. Pass: ramps of ≤ 25 ms per step, no ringing above 20 Hz greater than 5 % of peak (the B4 boundary).
2. **Head.** Hand-hold the rig on the crown; the helper triggers the master. Run 10 blinded pairs of decay vs flat at equal *peak*, then at equal *mean*.

**Rule:** decay ≥ flat at equal mean on ≥ 7 of 10 → adopt.

**(f) Replaces.** Constant-force bites and the sinusoidal line profile. Neither change is binding: the PLINE, LINE and CIRCLE modes are kept, only the speed law along them changes.

**(g) Why it might fail.** Through 2–8 cm of hair, 20–40 ms ramps may be too smeared to feel. Vent steps may disturb bite-latency calibration. A crescendo on K risks prick, so cap it at 0.25 N.

---

## LEAP B4: SCRAPE OVERLAY. A fast component that stays a scratch, and the boundary that keeps it one

**(a) Assumption broken.** That any content above ~20 Hz at the contact is "vibration" (scratch-model §8 item 5). A real nail scrape is *full* of high-frequency content: in instrumented scratching, accelerometer energy above ~70 Hz and contact-microphone energy above ~150 Hz scale with scratch power (Padmanabha 2023 [KNOWN]). That is the stick-slip of a skin fold and of hairs flicking off the edge.

**(b) Principle.** Superimpose a small tangential ripple on the scrub while sliding, to turn a smooth glide into a scrape. **The boundary that keeps it a scratch** [EST, derived from the physiology]:

| Criterion | Rule | Why |
|---|---|---|
| 1. Never reverses on the skin | ripple velocity amplitude 2πfA ≤ 0.5·v_slide | Keeps one-way sliding with ±50 % speed modulation. If 2πfA > v, the tip stops and back-slips every cycle, which is what a vibrator does. At v = 140 mm/s: f = 30 Hz → A ≤ 0.37 mm; f = 50 Hz → A ≤ 0.22 mm |
| 2. Flutter, not hum | band 20–60 Hz | Sensation changes from flutter to "vibratory hum" near 60 Hz, as the Pacinian channel takes over; Pacinians adapt in < 1 s and are the signature of a massager [KNOWN] |
| 3. Aperiodic | band-limited noise, not a tone | A natural scrape is broadband and irregular; a fixed tone is a motor |
| 4. Gated to sliding | zero amplitude when v_slide < 50 mm/s and when lifted | A real scrape stops when the nail stops; a vibrating pin at rest is a buzzer |
| 5. Small share | ripple RMS displacement ≤ 5 % of stroke length; ≤ 30 % of contact time | The stroke must dominate the percept |

**Implementation and verdict.** The puppet cannot carry it: the synchro block resonates at 25 Hz and the lines are tube-damped. It would need a 3–9 g voice coil on the pin block, a pad wire, and a hum source on a bone-conduction path. The passive route to the same "scrape" is B1's higher-adhesion polished material plus B3's attack transient. **Do not build B4. Adopt its boundary table as an acceptance spec** for B3's ripple and for the RT1 25 Hz synchro ring.

**(c) Numbers moved.** If built: P(on-par) ±0.02 [JUDG], with G2 and G3 risk. Cost +$60–110, +12–20 h, +6–12 g on the pad, against the twin's ≈ 20 g margin.

**(d) Plausibility.** The physics is easy; the percept is the doubt. 100 Hz vibration *reduces* itch (Ward et al., *Pain* 1996 [KNOWN]), but vibration can also *induce* itch (Mueller 2019 [KNOWN]).

**(e) Cheapest test (~$10).** A POM pick on a 130-size toy motor with an offset washer, PWM'd to 30–60 Hz. The helper scratches blind, motor off vs on, at equal force. **Rule:** if on beats off by ≥ 1.5 *and* is called "scratch" (not "massager") ≥ 80 % of the time, reconsider B4 for SP2.

**(f) Replaces.** Nothing; it would be an add-on.

**(g) Why it fails.** It most likely reads as "vibrating scratcher", the category the north star excludes.

---

## LEAP B5: SOUND LENS. Hear the scratch, crisper than it is

**(a) Assumption broken.** That sound is a by-product to keep quiet: scratch-model §1.3 ranks it fourth, and the spec only budgets motor noise under the "wanted nail hiss" of 30–40 dBA.

**(b) Principle.** What we hear changes what we feel:
- Amplifying the high frequencies of the sound of rubbing hands makes the skin feel **drier and rougher**: the parchment-skin illusion (Jousmäki & Hari, *Curr Biol* 1998 [KNOWN]).
- Boosting 2–20 kHz made potato chips taste **crisper and fresher** (Zampini & Spence, *J Sens Stud* 2004 [KNOWN]).
- Turning down motor sound made a toothbrush more pleasant (Zampini 2003, leap-A).

Crispness is exactly the quality G1 is about, and sound is the one place where "crisper than a nail" is legal.

```
 piezo contact disc Ø 12 (0.5 g), bonded to the pin block (hears every rim on skin and hair)
   │ 0.8 mm micro-coax along the bail (≈ 1.5 g)
   ▼
 drive box: JFET buffer → shelf EQ (+6…+10 dB above 2 kHz, −12 dB below 300 Hz to drop pump rumble)
   → noise gate (opens only when ≥ 1 pin is in contact: valve-state gated) → 2 × 0.5 W class-D
   ▼
 Ø 10 micro-speakers (1.5 g each) in the two ear-axis hub pods, aimed at the ear canal, 15–25 mm away
 (no earbuds, no bone path back to the piezo; analog chain latency < 1 ms)
```

**(c) Numbers moved.**
- **G1: +0.02–0.04** (perceived crispness).
- **G3: +0.02.** A wanted sound masks pump, valve and servo noise rather than competing with it.
- The scratch sound is also an ASMR channel that a person scratching cannot amplify.
- **Cost** $25–40. **Hours** +6–8. **Mass** ≈ +5 g head-borne. **Wire:** a 2-conductor micro-coax on the bail (the brief makes the puppet's "no wires on the pad" non-binding).

**(d) Plausibility.** A contact piezo easily hears a nail on hair. The valve-keyed gate silences pump hiss between bites. Feedback is unlikely: the speaker couples by air, and a contact piezo is insensitive to air. The 300 Hz high-pass keeps the synchro ring and valve clicks out of the chain.

**(e) Cheapest test (~$20, one evening, helper).** A $2 piezo disc taped to the B1 wand → a guitar headphone amp with a treble control (≈ $15–20) → open earbuds. The helper scratches. Blind blocks, 30 s each:
- earplugs (nothing);
- natural hearing;
- flat amplification;
- high-frequency boost.

Rate "crisp" and "satisfying". **Rule:** the HF boost beats natural hearing by ≥ 1.0 on satisfying → build.

**(f) Replaces.** It adds a channel. It also turns the noise-budget work (mufflers, foam) into "mask with the right sound" rather than "silence everything".

**(g) Why it might fail.** It may feel artificial: a speaker by the ear announcing a sound effect. The illusion is strongest when sound and touch are tightly synchronous and plausibly from the same source; with 15–25 mm speaker distance and sub-ms latency that should hold [JUDG]. Some people find amplified scratch sounds unpleasant (misophonia), and Michael may be one of them.

---

## Considered and folded

| Idea | Finding | Verdict |
|---|---|---|
| Serrated / multi-edge tip | 0.2–1 mm serrations are gaps in the 40 µm–3 mm hair-capture band (H-4.9); a double rim needs a step (H-4.3) | Rejected; more edges come from more pins or from B1 variety |
| Sharper edge | Red line 11: R ≥ 0.4 | Use line load (K tip) |
| Matte micro-texture | Skin friction *falls* with roughness up to Ra ≈ 4 µm | Polish; choose material (B1) |
| Keratin-like material | PA6 or horn as B1 arms; horn on hair is keratin-on-keratin, so expect more drag | Wig-test first |
| Tip temperature | Tip at 22 °C on 34 °C skin: POM contact ≈ 29 °C, stainless ≈ 23.5 °C (effusivity 800 vs 7,950) [EST]. But the ~1.5 mm² rim is far below thermal spatial summation, and the tip warms in seconds | Skip hardware. Cooling inhibits itch via TRPM8 (Palkar 2018 [KNOWN]): test an $8 menthol scalp tonic instead |
| Hair-follicle drive | The cone already bends hair at L ≈ 0.5–2.5 mm (the 1/L² sweet spot) | Covered; extra via W tip and B2 cross-hatch |
| Stroke density / coverage | At par (≈ 4,400 vs ≈ 4,000 deflections/s); per-spot dose capped | Not a lever; the machine's edge is endurance |
| Carrier + grain | Leap-A L2, round 1 | Compatible with B3 |

---

## Summary

| # | Leap | Hardware | P(on-par) effect [JUDG] | Hours | Cost | Head mass | Cheapest test |
|---|---|---|---|---|---|---|---|
| B1 | **Mixed hand**: K / S / W edges, POM vs PA6, in-situ blind A/B | turned tip sticks | **+0.04–0.05** (G1, G4) | +4–6 | +$15–25 | ±0.2 g | spring-pen wand, 12 blind pairs ($30) |
| B2 | **Itch hunter**: tease → dig (cross-hatch, K) → smooth; 30 s revisit | none | **+0.02–0.03** (G5, G4) | +3–4 | $0 | 0 | helper DIG vs normal at pointed spots ($0) |
| B3 | **Envelope strokes**: stepped-vent attack/decay per pin; constant-speed power stroke | none (spare S070) | **+0.02–0.03** (G1, G4) | +4–6 | +$12–45 | 0 | S0 rig + load cell, blind decay vs flat ($12) |
| B4 | **Scrape overlay**: 20–60 Hz aperiodic ripple, quantified boundary | voice coil on pad | ±0.02, high risk | +12–20 | +$60–110 | +6–12 g | pick on a toy motor ($10) → **don't build; use the boundary as a spec** |
| B5 | **Sound lens**: contact piezo → HF shelf → hub-pod speakers | piezo, amp, 2 speakers | **+0.02–0.04** (G1, G3) | +6–8 | +$25–40 | +5 g | piezo + headphone amp ($20) |

All five tests fit one weekend for ≈ $75 total, with a helper (self-generated scratching is attenuated: Blakemore 1999).

---

## Best bet: THE TUNED HAND (B1 + B2 + B3), with B5 as a cheap option once its test passes

**The case.** Under the amended goal the scratch is the product, yet the baseline bets G1 on one tip chosen on a wand. The tuned hand:
- puts **three edges** on the head and converges on Michael's preference **in his own hair** during real sessions;
- writes a **crisp attack and soft release** into every stroke with the valves he already has, raising peak crispness while lowering mean force, drag and abrasion;
- turns THERE into **itch relief**, timed to the ~30 s window over which scratching inhibits itch neurons.

It touches no halo, bail, synchro, twin provision or red line, and costs about one weekend. It beats a person on things a person cannot do: an edge that does not soften with humidity, identical shaped force at minute 20, an edge class on demand, and an itch located by the person who has it.

**Revised estimate if adopted (on the recommended 6-pin hybrid):**

| | Baseline hybrid | + Tuned hand (B1+B2+B3) | + B5 sound lens |
|---|---|---|---|
| Parts | ≈ $1,450–1,500 (+$185 tools) | **≈ $1,480–1,560** (+$12 load cell) | ≈ $1,510–1,600 |
| Hands-on hours | 165–230 | **≈ 175–243** (+11–16; ~3 h recovered from the wand A/B) | ≈ 181–251 |
| Head mass, single / twin | ≈ 386 (370 light) / 480 g | **≈ 386 (370) / 480 g** (±0.5 g) | ≈ 391 / 485 g (twin margin 20 → 15 g) |
| Gates G1 / G2 / G3 / G4 / G5 | 0.75 / 0.85 / 0.80 / 0.80 / 0.85 | **0.83 / 0.86 / 0.79 / 0.87 / 0.88** | 0.85 / 0.86 / 0.81 / 0.87 / 0.88 |
| Product (independent) | 0.35 | **0.43** | 0.45 |
| **P(on-par ≥ 7/10), correlated** [JUDG] | **≈ 0.40** (0.30–0.50) | **≈ 0.48** (0.37–0.58) | **≈ 0.50** (0.39–0.60) |
| P(≥ 7/10 within 26 weekends) | ≈ 0.20 | **≈ 0.24** (P(reach) 0.49 × 0.48) | ≈ 0.24 |

**Order.** Run the B1, B2 and B5 helper tests in S0 week 1, alongside the baseline's coin-and-helmet evening. Run B3 on the S0 rig as soon as it bites. Build only what passes its rule. If all three tuned-hand tests fail, the baseline loses about 4 hours, and we learn that the scratch is limited by contact through hair (G1's other half), not by edge quality. That would point the next round at reach, not at the tip.

**Most likely way the best bet fails.** At R ≥ 0.4 through Michael's hair, edge differences, envelopes and itch-digs are all below his discrimination. The ceiling is then set by contact fraction and pattern, not tip craft. The wand test answers that in one evening for $30.

---

### Sources (new in this file; others via the project files cited inline)
- Jousmäki & Hari 1998, parchment-skin illusion: [Semantic Scholar](https://www.semanticscholar.org/paper/Parchment-skin-illusion:-sound-biased-touch-Jousm%C3%A4ki-Hari/60e2b097a0ffdc62a249c363f12256aecb7b240b), [Aalto](https://research.aalto.fi/en/publications/parchment-skin-illusion-sound-biased-touch/)
- Zampini & Spence 2004, auditory crispness: [Oxford ORA](https://ora.ox.ac.uk/objects/uuid:853d9b0d-0249-4761-b329-936a791ecedd)
- Davidson et al. 2009, state-dependent itch inhibition by scratching (~30 s): [Nat Neurosci](https://www.nature.com/articles/nn.2292)
- Palkar et al. 2018, cooling relief of itch requires TRPM8: [JID](https://www.sciencedirect.com/science/article/pii/S0022202X1733364X)
- Ward, Wright & McMahon 1996, counterstimuli (100 Hz vibration best) on itch: [Pain](https://www.sciencedirect.com/science/article/abs/pii/0304395995000801); vibration-induced itch: [Mueller 2019](https://pubmed.ncbi.nlm.nih.gov/30151997/)
- Flutter/vibration boundary near 60 Hz: [eLife 2019](https://elifesciences.org/articles/46510), [Sci Rep 2017](https://www.nature.com/articles/s41598-017-15767-x)
- Skin friction vs counterface roughness (minimum near Ra 4 µm; adhesion): [JMBBM 2019 hardness and finish study](https://www.sciencedirect.com/science/article/abs/pii/S1751616118312943), [Derler & Gerhardt 2012](https://link.springer.com/article/10.1007/s11249-011-9854-y)
- Padmanabha et al. 2023, scratch force, speed and vibration content: [Commun Med](https://www.nature.com/articles/s43856-023-00345-2)
