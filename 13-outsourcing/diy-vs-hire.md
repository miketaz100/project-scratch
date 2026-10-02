# DIY vs hire: who builds SP1 "Puppet Halo, Lean"

**Project SCRATCH · 13-outsourcing · Cost & Schedule Estimator · 2026-10-02**
**Design costed:** the LEAN design in 12-sp1v2/DECISION-3.md, with all must-fixes from decision-analysis §4.4.
**Read:** DECISION-3; decision-analysis; leap4-A §4 and §7; leap4-C C3; leap4-D L1 and §3; leap4-E in full; leap4-F §0–5; redteam-3 §1, §3, §6, §8; outsourcing-options in full.
**Tags:** **[SRC]** = from a named project file or the vendor page it cites (the repo's hour figures are themselves judgement) · **[EST]** = my arithmetic or judgement · **[VERIFY]** = check before relying on it.

---

## 0. Answer first

Comparison table: §3. "Good session" = rated ≥ 7/10, "as satisfying as being scratched well".

**The finding that frames everything.** Every route lands between 0.20 and 0.32 for a good session within six months [EST]. Two things cap it:
- **P(the design feels good on his scalp, given a session) ≈ 0.38–0.42**, whoever builds it. Money barely moves this number; a $40 bench rig answers it.
- **Calendar.** Recruiting, a design phase and part-time schedules eat a professional's speed advantage (as outsourcing-options §0 found) [SRC].

**What money does buy:** Michael's hours (≈ $190–250 per hour saved, central); P(finishing) on a 12-month horizon; an independent safety check of a head-worn device; professional CAD and documents he owns, the start of any path to SP2 or a product.

**Recommendation in one line.** Run the S0 bench rigs now (≈ $100–200, one or two weekends). In parallel, buy a **paid design review** (option d). Add a second short paid **safety checkpoint before the first head session**. Escalate to (e) or (a) only if S0 passes **and** Michael either wants a product path or finds he does not enjoy building. See §5 for the decision rule.

---

## 1. DIY bottom-up estimate for the lean design

### 1.1 What is being built

Six sleeve pins with drafted POM cones on two gallery lines, riding a printed dish (leap4-A L3-2). A three-drum tendon puppet with series springs, a 2.0 N magnetic fuse and Hall-flexure stops (leap4-D L1). One air rail with deadhead pumps and diverse reliefs, plus a palm line with an Airpel float, QEV and relief. A carbon polygon bail on printed nodes with a carbon band, two friction hinges, a detented carriage, mechanical ±40° stops and pad-2 bosses. A BTT Manta M8P + CB1 on Klipper, with an independent hardware loop: NC e-stop, weld-checked relay hold-to-run, and a comparator snag vent. Knobs and an armrest switch. No egg, no scan, no pad-B parts.

**Architecture flag (needs the architect's freeze v3).** DECISION-3 lists both an "XY belt master" (item 2) and three drums on box steppers (item 3). leap4-D L1 is explicit: "There is no XY stage." Inverse kinematics on the three drums *is* the master [SRC]. I cost the drums only. If freeze v3 keeps a physical XY stage driving the cables, add **6–8 h and ≈ $70** [SRC, the baseline XY line].

### 1.2 Hours by subsystem

The first-timer column uses RT3's method: 11 focused hours a weekend, print time overnight and not counted, and a **1.5× first-timer factor** already inside the repo figures [SRC redteam-3 §1.2]. The experienced column divides the build tasks by 1.5. Tests and sessions are left unscaled, because a load cell does not run faster for an expert.

| Subsystem | First-timer h | Experienced h | Basis |
|---|---|---|---|
| S0 de-risk rigs (one-nail rig, coin helmet with hinges, Klipper Pico sync) | 8–12 | 6–9 | leap4-E S0 [SRC] |
| Box (case, pumps, reliefs, accumulator, 2 PIN valves, dumps, filters) | 8–12 | 5–8 | E-plan box, minus vacuum and 6 valves [EST] |
| Master (3 drums, tensioner, Hall stops) | 5–8 | 3–5 | leap4-D L1 [SRC] |
| Cable puppet (3 lines, pad stops, tendon plate, magnetic fuse, ink and life rigs) | 13–20 | 9–13 | L1 minus firmware, 3 cables [EST] |
| Pad + dish (6 pins, 2 galleries, dish + 2–3 print rounds, palm, skids, float + QEV, snag mitigation) | 22–32 | 15–21 | leap4-A §4 + E3 [SRC/EST] |
| Halo + stations (cradle, carbon band and 7-node bail, hinges, detented carriage, stops) | 12–18 | 8–12 | C3 + E4 [SRC/EST] |
| Umbilical (ear-axis exit, housings, breakaway, head switch) | 6–9 | 4–6 | E-plan C′ [EST] |
| Electronics + safety loop | 7–10 | 5–7 | E1 + loop extras [SRC/EST] |
| Klipper config + patterns (winch, backlash, pressure loop, valves, `score.py` path rules, jitter, dwell ledger) | 14–22 | 9–15 | E1 + dish rules + L1 IK [SRC] |
| Bench gates (hair suite, force map, proof, fail-to-free, breakaway, endurance, mass, noise, doff) | 10–14 | 8–11 | RT3 B + C′ gates [SRC/EST] |
| Integration and rework | 8–14 | 5–9 | E-plan must-fix spread [SRC] |
| First sessions (5 → 10 → 20 min; tune tip, force, jitter) | 6–10 | 6–10 | RT3 D [SRC] |
| **Total** | **≈ 120–180 (central ≈ 150)** | **≈ 85–125 (central ≈ 105)** | |

**Double-counting check.** Summing the leap savings overstates them:
- **Dish gate + Klipper.** E1's 18–27 h saving assumed the 1 kHz per-pin gate scheduler still existed. The dish gate deletes it, so E1's residual is only ≈ 7–12 h, and the dish's own net saving against the Klipper-box plan falls to ≈ 0–23 h [EST].
- **Tendon + Klipper + outsourced prints.** leap4-D's −18 to −35 h was against a hand-built synchro that E1 and E3 had already trimmed. The tendon nets ≈ ±5 h; its value is risk (V4, V5 and the rupture slam retired), not hours.
- **The E2 valve manifold** becomes moot, with its 6–8 h.

Top-down from leap4-E's 98–140 h with only de-duplicated deltas gives ≈ 70–150 h, central ≈ 110 [EST]. The bottom-up figure is higher because each leap claimed savings against the hand-built baseline. **Plan on 150 h for a first-timer**: sensibly above leap4-F's Spring Rake (75–100 h) and its ≈ 50–60 h floor for any legal design [SRC], since the lean design keeps air pins, a dish and a winch.

**Firmware risk.** Klipper's winch kinematics are, I believe, experimental, and Klipper has no built-in backlash compensation [VERIFY both]. leap4-D's per-cable compensation (circle flats ≤ 0.3 mm [SRC]) may need custom code: **+4–10 h** [EST], inside the high end. LINE and PLINE reverse while the pins are lifted, so they work without it.

### 1.3 Parts, tools and printer

**Parts, bottom-up [EST]:**

| Group | $ |
|---|---|
| Electronics: M8P + CB1 $154.59 [SRC E1], drivers, brick, safety loop, sensors | ≈ 300–330 |
| Pneumatics: pumps, reliefs, valves, QEV, Airpel float, fittings, sleeves | ≈ 240–330 |
| Tendon drive: 3 steppers, wire, coil housing ($20–40 [SRC L1]), springs, magnets | ≈ 85–110 |
| Halo: dial + helmet, carbon, epoxy, 2 hinges ($10–23 each [SRC E4]) | ≈ 130–160 |
| Pad: POM, PTFE tape, shafts, skids | ≈ 50–70 |
| Apache 2800 + foam [SRC RT3] | ≈ 60 |
| Outsourced SLA/MJF prints incl. DHL [SRC E3 range, scaled to 6 pins and no synchro] | ≈ 80–130 |
| Filament, fasteners, inserts, glue (fasteners alone were $130 in bom-verified) | ≈ 130–180 |
| Load cell, real-hair wig head, test consumables | ≈ 60–80 |
| Shipping across about 8 vendors | ≈ 60–80 |
| **Total** | **≈ $1,150–1,400** |

Top-down cross-check: baseline $1,450–1,500 [SRC] with de-duplicated deltas (dish −$115 to −275, tendon −$70 to −100, stations −$130 including pad B's servo, Klipper +$75–95, carbon +$10, prints +$50–100, remaining pad-B parts −$40–70) gives ≈ $1,000–1,360. Plan on **$1,300**, with a 15 % reserve (≈ $1,500 exposure).

**Tools:** ≈ $160–185. That is RT3's $185 [SRC] minus the bending form, plus a fine-tooth carbon saw.

**Is a printer needed, given outsourced printing?** Yes. Outsourcing is for *frozen* precision parts; E3's rule is "iterate at home until a part works once" [SRC]. The dish alone needs 2–3 print rounds, plus nodes, jigs and tips. Through JLC3DP each round is a 5–10-day loop [SRC], which with no printer adds **≈ 6–10 weeks** of calendar [EST]. A local service (3D Printing Expert of Naples [SRC §8]) is faster but dearer per part. Budget **$0** if he owns a ≥ 220 mm-bed FDM printer, else **$299–349** for a Bambu A1 [SRC RT3] plus 3–6 h to learn it.

**DIY cash total:** **≈ $1,300–1,900** for a first-timer buying a printer; **≈ $1,150–1,600** for a maker who has one.

### 1.4 Calendar and probability

**Calendar method.** Weekends needed = hours ÷ 11. Divide by 0.8 for attendance (0.85 for the experienced), then add 1–2 weekends of part and print waits and 2 holiday weekends [EST].

| | Work weekends | Calendar | First session (from 2026-10-03) |
|---|---|---|---|
| First-timer | 11–16.5 | 17–25 weekends, **≈ 4–5.5 months** | late Jan – late Mar 2027 (central mid-Feb) |
| Experienced | 8–11.5 | 12–17 weekends, **≈ 3–4 months** | late Dec 2026 – late Jan 2027 |

**P(good session within 6 months) = P(reach a full session) × P(≥ 7/10 | session).**

The conditional uses the decision analysis's gate method [EST]: G1 0.82 (dish: constant force on both flanks), G2 0.85, G3 0.84 (nothing powered on the head; cable-creak risk), G4 0.75 (A/B subsets, no automatic drift), G5 0.76 (manual stations, no THERE buttons). The product, 0.334, scaled by the analysis's correlation factor (0.347 → 0.40), gives **≈ 0.38 (0.28–0.48)**. The dish alone scores ≈ 0.44 (leap4-A); manual stations and no egg take some back.

P(reach) [EST] is **≈ 0.65 for a first-timer** (leap4-E's 0.70 for 98–140 h, adjusted for 150 h and new skills: carbon bonding, dish iteration, winch tuning) and **≈ 0.85 for an experienced maker**.

| | P(reach in 6 mo) | P(good session in 6 mo) | P(good session in 12 mo) |
|---|---|---|---|
| First-timer | 0.65 | **≈ 0.25** | ≈ 0.30 (reach 0.80) |
| Experienced | 0.85 | **≈ 0.32** | ≈ 0.35 (reach 0.92) |

---

## 2. Outsourcing re-scoped for the lean design

**Scaling.** outsourcing-options priced a "minimum concept" in the Spring Rake / Klipper-box class (75–140 h DIY). It said to multiply by 1.8–2× for the full Puppet Halo (165–230 h) [SRC].

The lean design (≈ 110–150 h central) sits in the upper Klipper-box class, so I scale **Phases 2–4 by 1.1–1.3×, not 1.8–2×** [EST].

**Up:** air pins plus a novel dish that needs print iteration; winch calibration; a pending snag-pull safety ruling; 13 red lines to verify. **Down:** the concept is decided and the must-fixes listed, so Phase 1 reviews one design instead of exploring; Phase 2 can start from freeze v3 and the repo's STLs (a further 15–30 % if the engineer accepts them); nothing is powered on the head; the controller is configuration, not firmware; one pad.

**Phase hours used** [EST]:

| Phase | Hours |
|---|---|
| P1 review | 12–20 |
| P2 detailed design | 60–120 |
| P3 build | 60–120, plus $1,350–1,750 parts (lean parts + 15–25 % spares and markup) |
| P4 iteration | 25–60, plus $150–500 parts |

**Michael's hours in every hired route** include scalp tests and a brief (15–25 h [SRC §7]), hiring, reviews, fittings and sessions.

### (a) Engineer who also builds: US senior, $85–150/h [SRC]

- **Cash:** P1 $1,000–2,500 + P2 $5,100–18,000 + P3 $5,100–18,000 + parts + P4 $2,100–9,000 = **≈ $15,000–50,000**. Central **≈ $27,000**: 16 / 85 / 85 / 40 h at $110 + $1,850 parts.
- **Michael's hours:** 35–60.
- **To first session: 4.5–6 months.** Brief 2 wk, hire + P1 2–4 wk, P2 6–9 wk, P3 7–10 wk, holidays +2–3 wk. Good engineer-builders book out 2–6 weeks [SRC §1].
- **P:** reach ≈ 0.62 (a local engineer-builder near Naples is a ≈ 50/50 find [EST]) × 0.41 = **≈ 0.25 at 6 months**; 0.90 × 0.42 ≈ **0.38 at 12**.
- **Risks:** scarcity near Naples; a moonlighting Arthrex engineer needs written employer consent [SRC §8]; highest spend; P2 scope creep.

### (b) Remote engineer ($50–90/h) + local builder ($35–60/h) [SRC]

- **Cash:** P1 $500–1,800 + P2 $3,000–10,800 + builder 70–145 h + 10–18 h engineer oversight + parts + P4 = **≈ $9,000–30,000, central ≈ $17,000**.
- **Michael's hours: 50–90.** He becomes integrator and project manager of two people.
- **To first session:** 5–6.5 months (two hires plus a hand-off).
- **P:** reach ≈ 0.50 × 0.40 = **≈ 0.20 at 6 months**; ≈ 0.32 at 12.
- **Risks:** split responsibility on a safety-critical device; the builder substitutes a part and the designer never knows [SRC §1c]. SW Florida's maker scene is thin, and FGCU has no ME or EE degree [SRC §8].

### (c) Local studio benchmark: 123 Design, Sarasota

- **Cash:** 123 Design's turnkey projects "typically begin around $15,000", 8–12 weeks to prototype [SRC §8]; that floor fits simpler devices. At $150–225/h blended [SRC] over ≈ 160–320 h: **$30,000–60,000, central ≈ $40,000** [EST], parts marked up 10–20 %.
- **Michael's hours:** 45–75, including 5–8 fittings at about 4 h round trip.
- **To first session:** 3.5–5 months if they accept (2–6-week queue).
- **P:** if they engage, reach ≈ 0.70 × 0.42 = **≈ 0.29 at 6 months**.
- **Risks:** may decline a one-off personal job or lack in-house pneumatics and Klipper; 2–3× freelancer cost [SRC §1d]. **Use the quote as a benchmark.**

### (d) Hybrid: paid design review only ($1,000–2,500), then Michael builds

- **Cash:** review + DIY = **≈ $2,300–4,400**.
- **Michael's hours:** DIY + 5–10 h (brief with AI help, hiring, call) − 0–15 h of dead ends avoided = **125–185** (≈ 90–130 experienced).
- **To first session:** 4–6 months (the review overlaps S0; net +1–3 weeks).
- **P:** reach 0.68 (stalls caught early) × 0.39 = **≈ 0.27 at 6 months**; ≈ 0.33 at 12.
- **Gets:** a 4–8 page memo against the red lines, top-5 risks with bench tests, a make/buy/print list, a P2 quote [SRC §2], a snag-pull ruling, and a vetted engineer for later.
- **Risk:** nobody checks the build. **Add a "bookend":** a 4–10 h paid check of the verification log and hardware loop before the first head session, $500–1,200 [EST].

### (e) Hybrid: engineer does detailed design + safety sign-off; Michael builds

- **Cash:** P1 + P2 ($6,100–20,500) + a 10–20 h build-support retainer + 8–15 h sign-off of the bench verification + DIY = **≈ $9,000–28,000, central ≈ $16,000** (≈ $6,000–14,000 with a remote engineer at $50–90/h).
- **Michael's hours: 105–170.** Real CAD with verified fits saves ≈ 15–25 % of build hours [EST]: less than outsourcing-options' 25–35 %, because the AI program already supplies most of the design.
- **To first session:** 4.5–6.5 months. P2 takes 6–9 weeks; S0, electronics and the box run in parallel.
- **P:** reach 0.60 × 0.41 = **≈ 0.25 at 6 months**; 0.88 × 0.41 = **≈ 0.36 at 12**.
- **Risks:** P2 money is wasted if S0 later fails the sensation gate. At ≈ $1,000 per hour saved it is a poor *hours* purchase; it buys **quality, safety assurance and owned design data**.

---

## 3. One-screen comparison

| Option | Cash | Michael's h | First session | P 6 mo | P 12 mo | What Michael has at the end |
|---|---|---|---|---|---|---|
| DIY first-timer | $1.3–1.9k | 120–180 | 4–5.5 mo | 0.25 | 0.30 | Working prototype; AI-generated specs and STLs; his own Klipper config; skills. No independent safety check. |
| DIY experienced | $1.15–1.6k | 85–125 | 3–4 mo | 0.32 | 0.35 | Same |
| (a) Engineer-builder | $15–50k (≈ 27k) | 35–60 | 4.5–6 mo | 0.25 | 0.38 | Bench-verified prototype + native CAD/STEP, drawings, BOM, schematic, firmware repo, FMEA, verification log; IP assigned |
| (b) Remote eng + local builder | $9–30k (≈ 17k) | 50–90 | 5–6.5 mo | 0.20 | 0.32 | As (a); build quality varies; checklist signed remotely |
| (c) Studio | $30–60k (≈ 40k) | 45–75 | 3.5–5 mo* | 0.29* | 0.37* | Fullest documentation and process; team coverage; often insured |
| (d) Review → DIY (+ bookend) | $2.3–4.4k (+0.5–1.2k) | 125–185 | 4–6 mo | 0.27 | 0.33 | Prototype + expert memo and risk list + a vetted engineer on call; independent check before first head session |
| (e) Design + sign-off → DIY | $9–28k (≈ 16k) | 105–170 | 4.5–6.5 mo | 0.25 | 0.36 | Prototype + professional CAD, drawings, BOM, FMEA, signed verification; a base for SP2 |

\* if the studio accepts the job. All figures [EST], built on the [SRC] rates above.

---

## 4. What an engineer adds beyond building SP1

1. **A safety review of a head-worn device, by someone who can touch it.** An independent FMEA mapped to the 13 red lines; a ruling on the dish snag pull; the hold-to-run weld check, fail-to-free timing (≤ 150 ms), breakaway and wig hair protocol checked on real hardware. This is the main thing DIY lacks. **≈ $1,500–4,000** standalone (15–30 h) [EST]; included in (a) and (e).

2. **Catching what the AI program cannot see.** The repo is internally rigorous but has never met a physical part. It cannot see tolerance stacks as printed, PTFE-on-POM stick-slip at 130 mm/s, cable creak at 1–4 kHz, carbon nodes cracking, how awkward a mid-session station move is, or which vendor quietly ships the wrong coil. Mass ledgers here have already run low (decision-analysis §2) [SRC]. Paper issues slip through too: this estimate found two (the XY-stage vs drum ambiguity in DECISION-3, and Klipper's missing backlash compensation [VERIFY]). An experienced engineer finds this class of problem in the first hour of review.

3. **Real CAD and drawings.** Parametric native CAD plus STEP and toleranced drawings, instead of SCAD and STL. Every later quote, revision and supplier depends on them.

4. **Design for reliability.** Strain relief, cable and sleeve life, PTFE-tape wear, connectors and serviceability, so the prototype survives 50+ sessions instead of 5.

5. **A path SP1 → SP2 → product.** SP2: powered drift by box cables (leap4-C C2), the twin, a lighter frame, ≈ $10,000–30,000 of design [EST]. Product: one MCU instead of the CB1 Linux box, a custom PCB, moulded parts, cost-down from a ≈ $1,300 one-off toward a few hundred dollars at volume, with UL 1647 / IEC 60335-2-32 as checklists and Class I exemption (21 CFR 890.5660) if sold as a massager [SRC §4]. A product programme (DFM, engineering builds, certification testing) is **≈ $50,000–250,000+ over 12–24 months** [EST, consistent with outsourcing §1d].

6. **IP and patentability.** An engineer documents the inventive steps (dish gating; the tendon puppet with a magnetic fuse) with dated records and knows the haptics and massager prior art. The opinion itself comes from a patent attorney (a consult is typically a few hundred dollars [EST, VERIFY]). **Important now:** public disclosure (a Hackaday log, a shared page) starts the clock on patent rights, so keep build logs private until he decides. Any hire needs a present-tense IP assignment [SRC §4].

7. **Supplier knowledge.** Alternatives when SMC, Airpel or coil housing stalls; who moulds 500 parts; local machining; PCBA.

**Worth paying for when:** Michael wants a product path or might sell; his time is worth more than ≈ $150–250/h to him; he does not enjoy building; he is a first-timer with no soldering, pneumatics or Linux; or he wants an independent safety signature before anything goes on his head.

**When it is NOT worth it:**
- **Before the S0 sensation gate passes.** Whether a drafted cone on a dish feels like a good scratch through *his* hair costs ≈ $30–45 and a weekend to learn (leap4-A §4e, leap4-D §e) [SRC]. $10,000+ of design before then may perfect a concept that fails on contact.
- **To raise P(good session).** No engineer moves P(≥ 7/10 | session) much above ≈ 0.42; sensation is empirical.
- **For calendar time**, or for **studio-grade process on a one-off** that will never be sold.

---

## 5. Recommendation and decision rule

**Do now, whatever the route (≈ $100–200, 1–2 weekends):** the S0 one-nail rig, the dish bench on a Ø 170 ball, the tendon ink rig, the coin helmet with hinges and the Klipper Pico sync test. Post the Phase 1 job (outsourcing §6) at the same time [SRC]. **S0 GO:** cone scratch-like in ≥ 6/8 headings and ≥ 6/10 on the scalp; dish chords ≥ 15 mm with lift ≥ 5 mm; tendon lost motion and creak pass. **Nobody is paid for Phase 2 or later until S0 passes.**

**Decision rule** (cash ceiling for SP1):

| If… | Then |
|---|---|
| Ceiling **< $5k** and he enjoys building, or is willing to learn | **(d) review + DIY, plus the pre-session safety bookend.** ≈ $3,000–5,500 all-in. **My default recommendation.** |
| Ceiling **< $5k** and he does *not* want to build | Hiring is not affordable at this scope. Build anyway with (d), or wait. |
| Ceiling **$5k–15k**, wants to build, wants real CAD or a product option | **(e) with a remote engineer at $50–90/h**, after S0 passes |
| Ceiling **$15k–35k**, time-poor or dislikes building | **(a)** a local engineer-builder, P1 first. If none is found in 4–6 weeks, **(b)** with a signed verification checklist. |
| Ceiling **≥ $40k**, wants turnkey and the best documentation | Get the 123 Design quote; **(c)** if it lands near $40k and they do pneumatics and firmware |
| **Any product ambition** | At minimum (e) after S0. Insist on native CAD, IP assignment and no public disclosure. A patent-attorney consult before showing anyone. |

**Why (d) is the default.** Michael chose to self-build on 2026-10-01 [SRC RESUME], and the AI program already supplies most of the design. The six-month P is about the same for every route, and (d) is cheapest by $5,000–45,000. The review plus bookend buys the one thing DIY truly lacks, an independent safety-literate pair of eyes, at the two moments that matter: before the cart and before the head. If the build stalls at month 3, (d) converts cleanly into (e) or (a) with the same engineer.

### Questions Michael still needs to answer

1. **Budget ceiling** for SP1, and separately for SP2 or a product.
2. **Target date** for a first session. Is six months a hard line?
3. **Experience:** soldering, 3D printing, Linux, pneumatics. Does he enjoy building, and how many weekends at 11 h are realistic?
4. **Does he own an FDM printer** with a ≥ 220 mm bed?
5. **Product ambition:** yes, maybe or never? This decides the CAD and IP spend and whether logs stay private.
6. **Drive distance** (30 / 60 / 120 min), and whether a builder may work in his apartment.
7. **Safety posture:** does he want an independent sign-off before the first head session even on DIY? (I recommend yes.)
8. **What an hour of his time is worth** to him. Hired routes cost ≈ $190–250 per hour saved.
9. **Architecture (for freeze v3):** confirm drums-only inverse kinematics vs a physical XY stage, and the dish snag-pull safety ruling.
