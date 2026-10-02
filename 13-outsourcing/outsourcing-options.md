# Outsourcing options: hiring an engineer to design and build the SP1 prototype

**Project SCRATCH · 13-outsourcing · Outsourcing Advisor · 2026-10-02**
**Read for context:** 12-sp1v2/DECISION-2 (with the North Star amendment), decision-analysis §0–1, redteam-3-buildability §0–1 and §6, leap4-E and leap4-F (answer-first sections), 01-foundations/safety-requirements §7, scratch-model §3 and §9, RESUME.
**Tags:** prices are "as of Oct 2026" from the source named. **[UNVERIFIED]** = from a secondary or aggregator page, or a figure I could not confirm on a primary page. **[JUDG]** = my judgement, not a quote. Hours are my estimates, built from the repo's DIY figures with a professional-speed correction.

**Context in one line.** On 2026-10-01 Michael chose to self-build and declined outsourcing (RESUME). This document prices the alternative so he can decide with numbers. One fact frames it: the minimum concept is not picked yet. The two cheap candidates are leap4-F's Spring Rake (75–100 h DIY, about $520–600 in parts) and leap4-E's Klipper-box bet (98–140 h, $1,530–1,620). The full 6-pin Puppet Halo is the expensive case (165–230 h, $1,450–1,500). Costs below assume a **minimum concept** in the Spring Rake / Klipper class. **For the full Puppet Halo, multiply design and build hours by about 1.8–2×.**

---

## 0. Answer first

| | Design only (Michael builds) | Design + build (someone else builds) |
|---|---|---|
| Remote marketplace engineer + local builder | **$3,800–13,500** | **$7,500–27,000** |
| **US freelance engineer who also builds (recommended)** | **$6,000–21,000** | **$12,000–44,000 (central ≈ $24,000)** |
| Small product-development studio | $11,500–33,000 | $22,000–70,000 |
| University capstone | n/a | $0–5,000 fee + $700–2,000 parts, 1–2 semesters |
| *DIY (repo)* | *75–230 h of Michael's time, $520–1,620 parts* | |

**My recommendation:** a paid, fixed-fee Phase 1 review ($1,000–2,500) by a US-based senior freelance mechatronics engineer. If that goes well, the same person does Phase 2 on capped hourly and, ideally, builds (Phase 3–4). Pick someone **local**, because fitting the helmet and iterating after sessions need Michael's head in the room. Expect **about $13,500–35,000 in total, central about $24,000**. The first helmet session lands at **about month 4**, and the iterated prototype at **about month 5–6** (§7).

Outsourcing buys **Michael's hours, the probability of finishing and a safety-literate second pair of eyes**. It does **not** buy calendar time. Leap4-F's DIY Spring Rake reaches a helmet session in about 6–8 weekends, which is roughly as fast as a hired build.

---

## 1. Engagement models

Rates are what the client pays, as of Oct 2026. US anchor figures:
- **BLS (May 2024 data):** median **mechanical engineer** $102,320 a year (about $49/h salaried); **electrical and electronics engineer** $118,780 ([BLS TED](https://www.bls.gov/opub/ted/2026/force-mass-mechanisms-and-vectors-employment-projections-and-wages-in-engineering.htm)).
- **Independent contractors** bill about 2–2.5× salaried hourly. Predictable Designs cites an IEEE figure of about **$125/h** for an independent contract engineer, with a US range of **$50–300/h** and **$25–75/h** offshore ([Predictable Designs](https://predictabledesigns.com/how-much-will-a-prototype-cost/); the IEEE figure itself is [UNVERIFIED], since it is not dated on the page).

### (a) Freelance mechatronics or product engineer, design only

- **Rates:** US senior **$85–150/h** [JUDG, anchored on the above]. Upwork's own cost pages give a global median of **$35/h** for mechanical engineers (typical $30–50) and **$35/h** for embedded engineers (typical $25–50) ([Upwork ME cost](https://www.upwork.com/hire/mechanical-engineers/cost/), [Upwork embedded cost](https://www.upwork.com/hire/embedded-systems-engineers/cost/); both pages blocked direct fetch, so the figures come from search snippets, [UNVERIFIED]). Those medians are mostly offshore and mid-level. A US engineer who has shipped a body-contact device will not be at $35.
- **What you get:** a critique, CAD, a BOM, schematics, a firmware plan and a hazard analysis. No physical object.
- **Turnaround:** Phase 1 in 1–2 weeks. Detailed design in 4–8 weeks part-time.
- **Pros:** cheapest route to a professional design; works remotely; keeps Michael's self-build decision intact.
- **Cons:** the designer never touches the hardware, so build problems come back to Michael. Mechatronics spans three disciplines (mechanical, electronics, firmware), and one person is rarely strong in all three.
- **Fits this project if** Michael still wants to build himself. He would trade about 25–35 % of his hours (the CAD and part-selection share) for $4,000–15,000.

### (b) Freelance engineer who also builds

- **Rates:** the same as (a). Build labour is often billed at the same rate, sometimes 10–25 % lower [JUDG].
- **What you get:** one accountable person from paper to a working, bench-tested prototype.
- **Turnaround:** 3–5 months for design plus build, part-time.
- **Pros:** **a single point of responsibility for safety.** The person who chose the spring cap also checks it on the load cell. No hand-off losses.
- **Cons:** the highest freelance spend. They must be local, or Michael must ship or travel for fittings. Good engineer-builders are scarce and book out.
- **Fits best** for a head-worn device (see §7).

### (c) Engineer for design + a separate builder

The builder could be a makerspace member, a hobbyist, a prototype machinist or a student.

- **Rates:**
  - **Remote engineer:** $50–90/h.
  - **Builder:** $30–60/h [JUDG]. Employee wages give a floor: prototype model-shop workers average **$31.37/h**, most earning $19–39 (ZipRecruiter, 2026-09-30); prototype machinists earn about $30/h (Dallas, California) ([ZipRecruiter](https://www.ziprecruiter.com/Jobs/Prototype-Model-Shop?layout=2pane_v2), [ZipRecruiter CA](https://www.ziprecruiter.com/Salaries/Prototype-Machinist-Salary--in-California); [UNVERIFIED], aggregator).
  - **Job-shop machining:** billed at **$75–250/h**, with prototype work at **$120–200/h** ([Fabcon](https://fabcon.com/articles/precision-cnc-machining/cnc-machining-hourly-rate-us/), [UNVERIFIED]). That matters only if a part must be machined; the minimum concepts avoid it.
- **What you get:** cheaper labour on the build.
- **Pros:** the lowest cash cost for "someone else builds". A local builder can do the fittings.
- **Cons:** **split responsibility on a safety-critical device.** The builder will substitute a part or reroute a line, and the designer will not know. Michael becomes the integrator and project manager. Makerspace builders are often reliable for prints and wiring but less so for a 30-minute endurance test and a written log.
- **Mitigation:** the designer writes a build-and-verify checklist (the safety red lines as tests). The builder fills it in with photos and numbers, and the designer signs off remotely.
- **Fits if** no local engineer-builder exists.

### (d) Small product-development or prototyping studio

- **Rates:**
  - **Full-service design and engineering firms:** **$100–450/h** ([Design1st](https://design1st.com/how-product-design-firms-charge/)); hardware agencies **$100–300/h** ([Cad Crowd 2026 breakdown](https://www.cadcrowd.com/blog/how-much-does-it-cost-to-develop-a-new-physical-product-a-complete-2026-breakdown/)).
  - **Feasibility phase alone:** $1,500 at the low end, **$3,000–8,000 typical**. Mechanical prototypes **$3,000–30,000**, electronics-plus-PCB prototypes **$10,000–50,000** (Cad Crowd; [UNVERIFIED], vendor-authored blog).
  - Examples: Simplexity (Vancouver, WA) and Product Creation Studio (Seattle) do electromechanical prototypes but mainly serve funded teams ([lanpdt list](https://lanpdt.com/prototype-development-companies/), [UNVERIFIED]).
- **What you get:** a team (ME, EE, firmware, PM), process, documentation, an in-house shop and often insurance.
- **Turnaround:** 2–4 months. Studios queue work, so start dates can slip 2–6 weeks.
- **Pros:** the most complete skills coverage. The best documentation and safety process.
- **Cons:** 2–3× the cost of a freelancer for the same hours. Project-management overhead. Many studios decline one-off personal projects, or want a minimum engagement of $15–25k [JUDG]. Design1st warns that equity or royalty deals can cost more than 10× hourly over a product's life. They are irrelevant here: SP1 is not a product.
- **Fits if** budget is not the constraint and Michael wants a turnkey result.

### (e) University route

**Capstone or senior-design sponsorship:**
- **Fees:**
  - UNT: **$2,000 for individuals or companies under 100 employees**; the sponsor keeps the IP; deliverables are a prototype, source code, drawings and a report ([UNT](https://engineering.unt.edu/connect/capstone-sponsorship.html)).
  - Michigan State: $5,000 per project; Colorado School of Mines: $5,000 (Cornerstone projects are free); UT Austin: $5,000 subvention plus extraordinary expenses (search snippets of the [MSU](https://me.msu.edu/sponsor-design-project), [Mines](https://eds.mines.edu/project-sponsorship/) and [UT](https://www.me.utexas.edu/academics/undergraduate-program/senior-design-projects/senior-design-sponsorship) pages, [UNVERIFIED]).
  - University of Utah: **$15,000**, IP assigned to the sponsor before the project starts; deadlines Fall Jul 15, Spring Nov 15, Summer Apr 15 ([Utah](https://www.mech.utah.edu/capstone/sponsors/)).
- **Timeline:** one or two semesters on the academic calendar. From today, the earliest realistic start is **January 2027** (Utah's spring deadline is Nov 15), with a prototype in **May–December 2027**.
- **Quality:** variable. 3–6 seniors with a faculty advisor.
- **Human testing:** expect the program to restrict or forbid testing on a person's head without institutional review [JUDG]. Michael would do the human sessions himself, afterwards.

**Grad students or lab technicians as private contractors:**
- **Rates:** about $30–60/h [JUDG]. Engineering intern pay runs **$22–39/h** by source ([Glassdoor](https://www.glassdoor.com/Salaries/mechanical-engineering-intern-salary-SRCH_KO0,29.htm), [ZipRecruiter](https://www.ziprecruiter.com/Salaries/Mechanical-Engineering-Intern-Salary)).
- **Where to find them:** post free on **Handshake** ([Handshake](https://joinhandshake.com/employers/create-a-job/)) or through a robotics club.
- **IP check:** university IP policies typically claim work made with "significant use of university resources", such as lab equipment ([UMD policy](https://policies.umd.edu/research/university-of-maryland-intellectual-property-policy), [UNH policy](https://www.usnh.edu/policy/unh/viii-research-policies/d-intellectual-property-policy)). Require that the work is done off-campus on the student's own or Michael's equipment. Check that their assistantship allows outside work.

**Assessment:** the cheapest cash route, with the slowest and least predictable result. Good for a side-build or the wig-head test rig. Weak as the main path.

### (f) Specialised marketplaces

| Platform | Client cost (Oct 2026) | Hardware talent | Fit |
|---|---|---|---|
| **Upwork** | Marketplace fee **5 %** (3 % for eligible US clients paying by bank); Business Plus 10 %; contract-initiation fee $0.99–14.99 ([Upwork pricing](https://www.upwork.com/pricing/client), via [goLance](https://golance.com/blogs/upwork-fees-explained-2026); [UNVERIFIED], primary page blocked fetch). Fixed-price milestones are funded into "project funds" (escrow). 14-day review; mediation free, arbitration about **$337.50 per side** ([GigRadar](https://gigradar.io/blog/upwork-payment-protection-fixed-price), [UNVERIFIED]). | Largest pool. Filter by US location and "hardware prototyping". | **Best marketplace for this.** |
| **Toptal** | **$500 refundable deposit**, **$79/month** platform fee, $60–150+/h (markup embedded), up to 2-week no-risk trial ([HireInSouth](https://www.hireinsouth.com/post/how-much-does-toptal-cost); [UNVERIFIED], Toptal does not publish rates) | Strong in software; thin in hands-on mechatronics [JUDG] | Phase 1–2 only, if a matching hardware engineer exists |
| **Kolabtree** | Managed "service model" since Jul 2023: the expert submits a statement of work and Kolabtree prices it to the client, with escrow ([Kolabtree](https://www.kolabtree.com/blog/important-information-for-kolabtree-experts-transition-to-service-model/)). Older terms mention up to 20 % ([User agreement](https://www.kolabtree.com/user-agreement)). | PhD scientists and engineers, $30–150/h | **Good for a paid design review**, e.g. a biomechanics or haptics PhD; weak for builds |
| **Contra** | 0 % freelancer commission; client fees reported at about $19 per contract plus Stripe ([Remogrid](https://www.remogrid.com/blog/reviews/is-contra-worth-it-freelance-review), **[UNVERIFIED]**) | Mostly design, web and creative | Poor fit |
| **Fiverr Pro** | Buyer service fee **5.5 %** plus a small-order fee; paid upfront, held until delivery ([fee guide](https://www.fastlancer.org/en/fastlancer-blog/fiverr-review/), [UNVERIFIED]) | Mostly CAD-render and PCB-layout gigs | CAD clean-up or PCB layout only |
| **Cad Crowd** | Platform fee 10–20 % reported; $50–120/h ([Cad Crowd](https://www.cadcrowd.com/blog/how-much-do-engineering-design-services-cost/amp/), [UNVERIFIED]) | CAD and industrial design | CAD only |
| **Hackaday.io / Hackster** | Free. Hackaday.io is a project-sharing community, not a marketplace. Hackster's paid "Pros" are commissioned for content, not client builds ([Hackster Pro](https://www.hackster.io/pro)). | Excellent hobbyist builders with public build logs | **Best place to find and vet a builder** (public logs = portfolio). Message people whose projects show pneumatics, cable drives or wearables. |

### (g) Hardware-prototyping services that build from your design

**Parts made to order: yes, they take one-offs.**
- **JLCPCB:** PCBs from $2 for 5; Economic assembly setup about $8, MOQ 2 ([JLCPCB](https://jlcpcb.com/help/article/pcb-assembly-price)).
- **JLC3DP MJF:** about $10–30 a part (repo, RT3 §6).
- **Xometry and Protolabs:** no order minimums, but a practical floor of about $95 per order at Protolabs ([Xometry](https://www.xometry.com/capabilities/3d-printing-service/), [comparison](https://www.niro3d.cz/en/blog/niro3d-vs-xometry-protolabs-comparison), [UNVERIFIED]).
- **SendCutSend:** **$39 minimum order** ([SendCutSend](https://sendcutsend.com/pricing/)).

**Full assembly ("box build") from your design: mostly no.** US electronics manufacturers (Technotronix, Suntronic, Foxtronics) advertise prototype box builds, but they are set up for OEM customers with production intent [JUDG]. A one-off consumer mechatronic device with pneumatics, a helmet fit and a human-safety test is outside their process. Expect a refusal, or engineering setup charges (NRE) above freelancer cost.

**Practical rule:** the engineer or builder orders the parts from these services; nobody turnkey-builds a one-off head-worn device except a studio.

### Red flags (all models)

- A portfolio of renders only, with no physical prototypes.
- A fixed price for the whole project before any review.
- Firmware-only force limits ("the servo is torque-limited") offered as safety.
- A request for equity or royalties.
- Refusal to hand over native CAD and source.
- More than 30 % upfront.
- Undisclosed subcontracting.
- No questions about hair, power loss or how the helmet comes off.

---

## 2. Scoped phases and costs

Hours are for a **minimum concept** in the Spring Rake / Klipper class; the full Puppet Halo is about 1.8–2×.

The professional-hours logic:
- the repo's DIY hours carry a 1.5× first-timer factor (RT3 §1.2), so a pro is faster;
- but a pro also writes documentation, a hazard analysis and a test log, and has to learn the brief;
- net: a pro takes about 0.8–1.0× the DIY hours for the same scope, split roughly 45 % design and 55 % build [JUDG].

Model rates used below:
- **(b)** US engineer-builder: $85–150/h.
- **(c)** remote engineer $50–90/h plus local builder $35–60/h.
- **(d)** studio: $150–225/h blended.

### Phase 1: paid design review and feasibility

**Deliverables:**
- a 4–8 page memo with a critique of the concept against the 13 red lines and the sensation envelope;
- the **minimum buildable version**, named and sketched;
- the top 5 risks and the bench test that retires each one;
- a make / buy / print list;
- a fixed quote for Phase 2 and a range for Phases 3–4;
- one 60–90 min video call.

**Hours:** 10–20. **Calendar:** 1–2 weeks.

| (b) | (c) | (d) |
|---|---|---|
| $1,000–3,000 (often a fixed fee) | $500–1,800 | $2,500–6,000 (paid discovery) |

### Phase 2: detailed design

**Deliverables:**
- CAD (native file plus STEP) of the helmet structure, pad, drive box and umbilical;
- a mass budget against the ≤ 500 g red line;
- a BOM with sources and prices;
- an electronics schematic (KiCad), with a carrier PCB if justified;
- the safety loop: NC e-stop, hold-to-run, fail-to-free;
- a firmware architecture and plan (Klipper or custom; how scratch patterns are generated and varied to avoid habituation);
- an **FMEA / hazard table mapped to each red line, with a verification test for each**;
- a build-and-verify checklist.

**Hours:** 50–100 (full Puppet Halo: 100–200). **Calendar:** 4–8 weeks.

| (b) | (c) | (d) |
|---|---|---|
| $4,250–15,000 | $2,750–9,900 | $9,000–27,000 |

### Phase 3: build one prototype

**Deliverables:**
- the assembled box, helmet and pad;
- firmware flashed, in a git repo;
- the bench verification log: force map on a load cell, proof loads, fail-to-free on power cut, a breakaway test, a 30-minute endurance run, and the wig-head entanglement test (red line 12);
- mass and noise measured;
- a handover session.

**Parts:** $700–2,000 (the repo's $520–1,620 plus 15–25 % for spares and outsourced MJF, PCB and laser-cut parts).
**Labour:** 50–100 h. **Calendar:** 4–8 weeks, including 1–3 weeks of part lead time.

| (b) | (c) | (d) |
|---|---|---|
| $5,000–17,000 incl. parts | $3,200–10,500 (builder 60–120 h + 8–15 h engineer oversight + parts) | $7,000–22,500 (techs at $125–200/h, parts often marked up 10–20 %) |

### Phase 4: iteration after Michael's first sessions (1–2 rounds)

**Deliverables:**
- changes driven by Michael's session ratings and notes (force, speed, tip, fit, noise);
- the affected verification tests re-run;
- updated CAD, BOM and firmware.

**Hours:** 20–60. **Parts:** $150–500. **Calendar:** 2–3 weeks per round.

| (b) | (c) | (d) |
|---|---|---|
| $1,900–9,500 | $1,000–5,000 | $3,200–14,000 |

### Totals and comparison with DIY

| | Design only (P1 + P2 + 10–20 h build support) | Design + build (P1–P4) | Central case |
|---|---|---|---|
| (b) engineer-builder | $6,000–21,000 | **$12,000–44,000** | ≈ $24,000 (15 / 75 / 75 / 40 h at $110 + $1,600 parts) |
| (c) remote engineer + local builder | $3,800–13,500 | $7,500–27,000 | ≈ $14,000 |
| (d) studio | $11,500–33,000 | $22,000–70,000 | ≈ $40,000 |
| **DIY (repo)** | — | **75–230 h of Michael's time + $520–1,620 parts** | Spring Rake 75–100 h / $520–600 |

**Reading the comparison** [JUDG]:
- Design + build by a pro costs about **$110–190 per DIY hour saved**.
- **Design only** saves Michael about 25–35 % of his hours: roughly 20–35 h on the Spring Rake, 40–80 h on the full Puppet Halo. Its bigger value is a **pre-checked, simpler design**: fewer stalls, which is where the repo's P(finish) losses sit.
- On the **full Puppet Halo**, design + build under (b) scales to about **$25,000–80,000**. That is a strong argument for fixing the minimum concept before hiring anyone.

---

## 3. What to look for

### Required skills (in priority order)

1. **Safety mindset for devices on a body:** bounding forces mechanically (spring plus stop), fail-to-free, NC e-stop and hold-to-run, FMEA. Experience with medical, wearable, exoskeleton, haptics or massage products is the strongest signal.
2. **Small mechanisms:** linkages, push-pull cables or small pneumatics. Lost motion, friction and hysteresis at the 0.1–0.5 N, 1–30 mm scale.
3. **3D printing for function:** PETG and TPU on a desktop printer; MJF PA12 and SLA from services; knowing when a print is not good enough.
4. **Embedded firmware:** an ESP32 or Klipper-class controller, steppers or bus servos, a safety architecture where firmware is never the only barrier (red line 13).
5. **Head and fit sense:** helmet cradles and how mass sits on a head (or a willingness to iterate on Michael's head).
6. **Documentation habit:** git, native CAD plus STEP, a test log with numbers.

### Portfolio signals

- **Good signs:**
  - photos or video of **working physical prototypes** they built;
  - force or test data in their writeups;
  - a Hackaday.io or GitHub log with iterations and failures;
  - anything worn or touching skin;
  - small pneumatic or cable mechanisms;
  - a public repo of firmware they wrote.
- **Weak signs:** renders only; only enclosure design; only PCB layout; only software.

### Interview questions (concrete)

1. "This pad must never push more than 2.5 N per nail, and firmware alone may not enforce it. Sketch how you'd bound it." (Expect a spring with a hard stop, a dead weight or a breakaway, not a torque limit.)
2. "Power dies mid-stroke. Walk me through what the pad does in the next 500 ms." (Expect a spring lift to clear, and nothing held against the scalp.)
3. "Three axes over a 1.5 m umbilical: push-pull cable or sealed air lines? What would you measure in the first weekend to decide?" (Lost motion, hysteresis, friction, stiffness, leak rate.)
4. "How would you test for hair entanglement before anyone wears it?" (A real-hair wig head, stroke counts per mode, shed-hair counts, with and against the lie of the hair.)
5. "What would you delete from this concept first, and why?" (Tests whether they simplify or add.)
6. "Head-borne mass must stay ≤ 500 g, even with a second pad. How do you track mass during design?"
7. "Klipper or custom ESP32 firmware for scratch patterns with per-stroke randomness? What are the trade-offs?"
8. "Which parts would you buy, print or have made, and which can't you print well?"
9. "Describe a prototype that failed in testing. What did you change, and how did you find out?"
10. "Have you ever told a client a design was unsafe and refused to proceed? What happened?"
11. "Give me your Phase 1 fixed fee and a Phase 2 range. Which three assumptions move the range most?"
12. "What exactly will I receive at the end of each phase? File formats, please."
13. "Will you sign an IP assignment and an NDA? Do you carry professional liability insurance?"
14. "For the first session on my head: who is present, what checklist, how long?" (Expect ≤ 5 minutes, the safety checklist, glasses on, a free hand on the e-stop.)
15. "How many hours a week can you give this, and what is your earliest start?"

### Checking references

- Ask for **two past hardware clients** whose projects were built, not only designed. Call them; do not email.
- Ask each reference:
  - Did they hit the quote, and what happened when scope changed?
  - Did you get all source files?
  - Any safety or reliability problems after handover?
  - Would you hire them again for something you would wear?
- Verify that portfolio work is theirs. Ask for a screen-share of the CAD feature tree or the git history of a project they show.
- On Upwork, read only **hardware** job reviews and the Job Success Score. Ignore unrelated CAD-render gigs.
- On Hackaday.io or GitHub, check that build logs span months, with honest failures.

---

## 4. Contract and IP

This is not legal advice. For anything beyond a marketplace's standard terms, a one-hour review by an IP or contracts attorney (typically a few hundred dollars [JUDG]) is cheap insurance.

- **NDA.** A mutual NDA, 2–3 years, is normal; engineers will sign. Upwork and Kolabtree support NDAs in-platform. Its practical value for a personal prototype is modest. The IP clause matters more.
- **IP assignment, not "work for hire" alone.**
  - Under US copyright law, a contractor's work is "work made for hire" only in **nine statutory categories** and only with a prior written agreement ([Copyright Office Circular 30](https://www.copyright.gov/circs/circ30.pdf)). CAD and firmware mostly fall outside those categories, and **patentable inventions are never covered by work-for-hire**.
  - So the contract needs a **present-tense assignment**: "Contractor hereby assigns all right, title and interest in all deliverables, inventions and IP …".
  - It also needs a **licence to any background IP** (the contractor's pre-existing libraries and parts), a moral-rights waiver, and a duty to sign patent papers if ever needed.
  - **Upwork's default terms** already assign work product **upon full payment**, only for the portions paid for, excluding background technology ([terms.law summary](https://terms.law/2023/07/23/upworks-terms-ownership-of-freelancers-work-product/), [Upwork legal](https://www.upwork.com/legal)). Fine for Phase 1. For Phase 2–3, add your own clause.
- **Deliverables named in the contract:** native CAD (Fusion, Onshape or SolidWorks) plus STEP, drawings, KiCad project and Gerbers, firmware git repo with build instructions, BOM with sources, FMEA, test logs and photos. "Source files are deliverables" must be in writing.
- **Open-source compliance:** if they use Klipper (GPLv3) or other open-source code, that is fine for a personal device. They must list licences.
- **Payment structure:**
  - **Phase 1: fixed fee**, paid on delivery or through an escrowed milestone.
  - **Phase 2: capped hourly** (time and materials, not to exceed the quote plus 10 %), billed weekly with a timesheet. Written change orders above the cap. Hourly suits exploratory work; switch to fixed once the design is well defined ([Design1st](https://design1st.com/how-product-design-firms-charge/)).
  - **Phase 3: fixed fee for labour**, split into 3 milestones (box working, pad bench-verified, full verification log). **Parts at cost with receipts**, or Michael buys them directly from the engineer's BOM.
  - **Phase 4: capped hourly per round.**
  - **Never more than 20–30 % upfront** on any phase.
- **Escrow:**
  - **Upwork:** fund each milestone; 14-day review; mediation free; arbitration about $337.50 per side.
  - **Kolabtree:** escrow per milestone.
  - **Toptal:** a 2-week trial.
  - **Fiverr:** payment held until delivery.
  - **Off-platform** (a local builder): pay per milestone on delivery; no escrow.
  - **Moving a marketplace freelancer off-platform** usually breaches the platform's terms for a period, unless a conversion fee is paid. Check the current Upwork terms before doing it ([UNVERIFIED]: I could not fetch the current clause).
- **Liability and safety sign-off.** What a freelancer will and won't accept [JUDG, consistent with common practice ([liability-cap norms](https://clauseshield.app/blog/liability-caps-unlimited-liability), [insurance guide](https://www.freelancermap.com/blog/the-most-interesting-types-of-freelancing-insurance/))]:
  - **Will:** cap liability at fees paid, exclude consequential damages, deliver a hazard analysis and a verification log showing each red line was tested, and refuse to proceed with an unsafe instruction.
  - **Will not:** "certify the device safe", accept open-ended indemnity for personal injury from a device you wear, or be present as the operator in your sessions without a release.
  - A **$1M/$1M professional liability policy** is the common freelancer limit, but many hardware freelancers carry none. Ask, and do not rely on it.
  - The realistic arrangement: the engineer is responsible for **designing and verifying to the written red lines**. Michael, as the sole user, accepts the risk of use and signs a short acknowledgement. If the builder attends a session, get the release reviewed by a lawyer.
- **Certification: none is required for a personal, unsold prototype.**
  - FDA establishment registration is triggered by **commercial distribution** (held or offered for sale) ([21 CFR 807](https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-807)).
  - Even commercially, an electric therapeutic massager is **Class I, exempt from premarket notification** ([21 CFR 890.5660](https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-890/subpart-F/section-890.5660)).
  - The product-safety standards **UL 1647** (motor-operated massage machines) and **IEC 60335-2-32** (massage appliances) apply only if it is ever sold ([UL 1647](https://standards.globalspec.com/std/14552588/ul-1647), [IEC 60335-2-32](https://www.csagroup.org/store/product/iec_085019/)). Treat them as design checklists, not requirements.
  - A **PE stamp** is neither needed nor customary for consumer-device design ([industrial-exemption overview](https://peimpact.com/pe-industrial-exemption/)).
  - Red line 5 (≤ 24 V DC, no mains inside, no lithium) plus a **UL-listed external power supply** removes most electrical-safety exposure.

---

## 5. What Michael hands over

### The concept brief (5–10 pages, plus repo appendices under NDA)

1. **One page: the goal.** The North Star amendment in his words; success = a session rated ≥ 7/10 "as good as a good scratch", and it must be a scratch, not a massage. One-off personal prototype, not a product.
2. **Binding requirements.** DECISION-2's binding list, each marked *fixed* or *negotiable for the minimum concept*: helmet; scrub modes; portable box; one pad with provision for a second; air pins or cables.
3. **The 13 safety red lines,** verbatim (safety-requirements §7). These are the acceptance criteria.
4. **The sensation envelope,** one table from scratch-model §3: force per nail 0.15–0.3 N (ceiling 0.6 N), speed 2–20 cm/s, 1–4 Hz, edge radius about 0.15 mm, tip compliance 0.1–0.5 N/mm, nail angle 25–65°.
5. **Michael's measured numbers** from the tests below.
6. **The candidate minimum concepts.** One sketch and one paragraph each for the Spring Rake, the Klipper-box bet and the 6-pin Puppet Halo, with the repo's hours, cost, mass and P estimates and their must-fix lists (decision-analysis §1, RT3 §1).
7. **Constraints.** Apartment; the box sits on a desk, chair back or couch; no mains; budget ceiling; target dates; what Michael does himself (tests, sessions, maybe printing).
8. **Existing assets.** The repo folders (BOM-verified, CAD, firmware, test protocols) and the Day-0 parts already bought, if any.
9. **What he wants back per phase** (§2), and the IP and NDA terms (§4).
10. **Open questions for the engineer** (scratch-model §9 items not closed by the tests).

### Cheap scalp tests to run first (≈ 1–2 weekends, < $80)

These turn the brief's estimates into his numbers. The engineer then designs to real data, not literature.

| # | Test | Kit | Output for the engineer |
|---|---|---|---|
| T1 | **Human reference:** a partner scratches his head "well" while a kitchen or postal scale under the partner's resting fingers reads force (or FSRs on a headband); 240 fps phone video | Scale, phone, ruler | Per-nail force, stroke length, speed, Hz (scratch-model §9.13, "the highest-value experiment") |
| T2 | **Tip test:** 4–6 candidate tips (press-on nail, POM cone, PETG edge) on a hand block, blind, 8 headings; "nail or pad?" and rating | $20 of tips | Tip geometry that reads as a scratch |
| T3 | **Force sweep:** a tip on a known spring or luggage scale at 0.1 / 0.2 / 0.3 / 0.5 N | Spring set, scale | His force–pleasure peak and discomfort ceiling |
| T4 | **Speed and rhythm sweep** to a metronome: 1, 2, 3 Hz; short and long strokes | Metronome app | Preferred speed and frequency |
| T5 | **Hair check:** with and against the lie; shed hairs on a dark cloth after 5 minutes; hair length, density photo | Dark cloth | Snag risk; whether the tip reaches skin |
| T6 | **Habituation:** a 15-minute scratch with and without pattern changes, rated every 3 minutes | Timer | How fast satisfaction fades; which variation matters |
| T7 | **Helmet fit and mass:** tape measurements (circumference, ear-to-ear over the crown, front-to-back); a $20 bike helmet with a coin bag at 300 / 400 / 500 g for 20 minutes of TV (V1/V15) | Tape, helmet, coins | Head dimensions and tolerable mass |
| T8 | **Noise:** a small servo held to the skull at the ear axis, with earplugs (V16) | One servo ($15) | Whether head-mounted motors are acceptable |
| T9 | **Skin check:** look for redness or tenderness 1 h after T3 at his preferred force | Mirror, partner | A first abrasion data point |

---

## 6. Ready-to-post job descriptions

### Freelance platform (Upwork / Kolabtree): Phase 1 design review, about 300 words

> **Paid design review: head-worn scalp-scratching prototype (mechatronics, safety-critical)**
>
> I'm an individual (not a company) building a one-off personal prototype: a lightweight helmet frame carrying a small pad of six nail-like tips that scratch the scalp. A portable drive box (on a desk or a chair back) holds the motors, with either sealed air lines or push-pull cables to the pad, plus a small controller with firmware for stroke patterns. It touches a person's head, so safety is the first requirement. I have 13 written safety red lines: mechanically bounded force (≤ 2.5 N per tip, not firmware-only), lift-off on power loss, NC e-stop, ≤ 24 V DC, ≤ 500 g head mass, one-hand release.
>
> I have a 5–10 page concept brief, my own scalp-test measurements, and a repo of research and three candidate concepts. **I'm hiring for Phase 1 only:** a fixed-fee review.
>
> **Deliverables (1–2 weeks):**
> - a critique of the concept against the safety red lines and the sensation targets;
> - your recommended **minimum buildable version**, with a sketch;
> - the top 5 technical risks and the cheapest bench test for each;
> - a make / buy / print list;
> - a fixed quote for detailed design and a range for building one prototype;
> - one 60–90 min video call.
>
> **You have:**
> - built physical electromechanical prototypes (photos or video, please), ideally something worn or touching skin (medical, wearable, haptics, massage, exoskeleton);
> - small mechanisms (linkages, push-pull cables or small pneumatics);
> - functional 3D printing;
> - embedded firmware (ESP32, Klipper or similar);
> - the habit of bounding forces mechanically.
>
> US-based preferred. **Within driving distance of [CITY] is a strong plus**, because later phases include fittings and an optional build.
>
> **In your proposal:** (1) one physical prototype you built and what you'd do differently; (2) how you would guarantee a maximum tip force without relying on firmware; (3) your Phase 1 fixed fee and earliest start.
>
> NDA and IP assignment required. Budget for Phase 1: $1,000–2,500, fixed.

### University robotics club / makerspace board: short variant

> **Paid side project: build help for a head-worn scratching prototype**
>
> An individual in [CITY] is looking for a mechatronics-minded maker (student, grad student or member) to help design and/or build a one-off personal prototype: a light helmet frame with a small six-tip scratching pad, driven by cables or air lines from a desk-top motor box with an ESP32 or Klipper controller. Safety-first design with written limits: spring-capped forces, lift-off on power loss, e-stop, low voltage. Paid hourly ($30–60/h depending on experience) or per milestone. Work is done off-campus on my equipment and budget, with an IP assignment. Skills: 3D printing (PETG/TPU), small mechanisms, wiring and soldering, Arduino/ESP32. Show me a project log (Hackaday.io, GitHub, photos). Contact: [EMAIL].

---

## 7. Recommendation

**Model:** (b), a US-based senior freelance engineer who designs and builds, **found locally if at all possible**. Fall back to (c), a remote engineer plus a local Hackaday-style builder, with the engineer signing off a written verification checklist. Use Upwork (US filter) and Kolabtree for the engineer search; use the local makerspace, a university robotics club, Handshake and Hackaday.io for local talent. **For Naples specifically (§8):** the remote engineer does Phase 1–2. The builder should be within about 45 minutes of Naples. The likeliest find is a moonlighting med-device engineer in Naples or Fort Myers; next, an FGCU student; failing both, a Sarasota or Tampa maker who drives down for try-ons.

**Why:**
- One accountable person for a device on the head avoids the design-to-build hand-off gap where safety slips.
- Local presence matters for Phase 3–4: helmet fit, the first ≤ 5-minute session with the checklist, and fast iteration after sessions. Shipping a prototype back and forth costs 1–2 weeks per round.
- A studio is 2–3× the price for little extra on a one-off.
- Capstone is too slow (earliest start Jan 2027) and restricted on human testing.

**Phasing:**
- **Run the scalp tests (T1–T9) and write the brief first**, about 15–25 h of Michael's time.
- **Phase 1** as a fixed fee. **Hire two reviewers in parallel** if the budget allows ($2,000–4,000): comparing their minimum-concept picks is the cheapest way to choose the concept, and you keep the better engineer.
- Commit to Phase 2 only after Phase 1. Commit to Phase 3 only after Phase 2's FMEA and mass budget pass.
- If Michael still prefers to self-build, stop after Phase 2 and keep the engineer on a **10–20 h support retainer** (design-only total $6,000–21,000).

**Budget (minimum concept, model b):**

| Phase | Cost |
|---|---|
| 1. Review | $1,000–2,500 |
| 2. Detailed design | $5,000–12,000 |
| 3. Build (incl. $700–2,000 parts) | $5,500–14,000 |
| 4. Iteration (1–2 rounds) | $2,000–7,000 |
| **Total** | **$13,500–35,500, central ≈ $24,000** |

For the full 6-pin Puppet Halo, about $25,000–60,000.

**Timeline (from today, 2026-10-02):**

| When | What |
|---|---|
| Weeks 0–2 (to mid-Oct) | Scalp tests, brief, post the job |
| Weeks 2–4 | Interviews, references, Phase 1 delivered |
| Weeks 4–10 (to mid-Dec) | Phase 2 detailed design |
| Weeks 10–17 (to early Feb 2027) | Phase 3 build, bench verification, wig-head test |
| ≈ Week 16–17 | First helmet session (≤ 5 min, checklist) |
| Weeks 17–24 (to mid-Mar 2027) | Phase 4, two iteration rounds |

**About 5–6 months to an iterated prototype.** Holidays will add 2–3 weeks.

### Location

Michael is in **Naples, Florida**. The local options are in §8. Still useful to know:
1. how far he will drive (30 / 60 / 120 minutes);
2. whether a builder can work in his apartment, or must work at the builder's own place or a makerspace;
3. his budget ceiling and target date for the first session.

---

## 8. Local options: Naples and Southwest Florida

Drive times from Naples are approximate [JUDG]:
- Fort Myers / Estero (FGCU): 30–45 min
- Sarasota: 1 h 45 min – 2 h
- Tampa (USF): 2.5–3 h
- Orlando (UCF): 3.5–4 h
- Gainesville (UF): 4.5 h

Southwest Florida has **no large hardware-hacker scene**. The nearest strong maker communities are in Sarasota and Tampa. The local engineering talent pool is **medical-device engineers**: **Arthrex has its global headquarters in Naples** (1370 Creekside Blvd) and hires product-development and biomechanical-test engineers there ([Arthrex careers](https://careers.arthrex.com/go/Medical-Device-Jobs-in-Naples/7572000/)). That body-contact, test-minded background is exactly what this project needs.

### Should the builder be local while the engineer is remote? Yes.

**The builder (Phase 3–4) should be within about 45 minutes of Naples.** In-person contact is needed for:
- helmet sizing and the first try-on;
- the first ≤ 5-minute session, with the checklist and a second person present;
- each iteration round after a session.

That is roughly **5–8 in-person visits** over the project [JUDG]. At 2–3 hours each way (Sarasota or Tampa), each visit costs a day, and a builder bills that travel time.

**The engineer (Phase 1–2) can be remote anywhere in the US.** A Florida-based engineer is a bonus: one in-person review at the first fitting is worth a day's drive.

**If a local engineer-builder exists** (most likely a med-device engineer moonlighting in Naples or Fort Myers), prefer them: they combine model (b) with local presence. Otherwise use model (c): a remote engineer plus a local builder, with the engineer's signed-off verification checklist.

### Where to find people

| Source | Where | How to reach | Best for |
|---|---|---|---|
| **Moonlighting med-device engineers** (Arthrex and other SWFL device makers) | Naples / Fort Myers | LinkedIn search "mechanical engineer" or "R&D engineer" + Naples/Fort Myers; Upwork with a Florida location filter | **Local engineer-builder.** Ask them to confirm in writing that their employer's moonlighting and invention-assignment policy allows the work. Florida has no statute limiting employee invention assignments the way California's does [JUDG, verify with counsel], so an employer agreement could otherwise claim side-work IP. |
| **FGCU**, U.A. Whitaker College of Engineering | Fort Myers (30–45 min) | Senior design (bioengineering): Dr Seneshaw Tsegaye, stsegaye@fgcu.edu. Software engineering: Dr Fernando Gonzalez, fgonzalez@fgcu.edu. Jobs: the Eagle Career Network, or email the student-newsletter contact before the 10th or 25th of the month. General: Julie Rose, jrose@fgcu.edu, (239) 745-4310 ([FGCU employer resources](https://www.fgcu.edu/eng/internships/)) | Part-time student builder; a firmware student; a year-long bioengineering capstone (the course covers prototyping and testing; past sponsors include Arthrex and Lee Health). **Caveat: FGCU offers no mechanical or electrical engineering degree** (its majors are bio, civil, environmental, CS, software, construction management; [FGCU Engineering](https://www.fgcu.edu/eng/)). Its library makerspace (3D printers, laser, CNC mill, 3D scanner) is for FGCU affiliates only ([FGCU Makerspace](https://library.fgcu.edu/makerspace)). |
| **Suncoast Science Center / Faulhaber Fab Lab** | Sarasota, 4452 S Beneva Rd (≈ 2 h) | 941-840-4394; tours Saturdays 1:30 pm | Lab access $35–100 per 8 h by package; 3D-print package $40; business $400/month; **consultation $50/h**; machines include waterjet, mills and lathes; personal projects allowed ([Suncoast Science](https://www.suncoastscience.org/members/)). A workshop for a builder, and a place to find makers. |
| **UF Innovation Station Sarasota County** | Sarasota, 1468 Blvd of the Arts | Jason Krywko, jkrywko@eng.ufl.edu, 941-217-4268 ([UF Sarasota](https://www.eng.ufl.edu/sarasota/industry-engagement/sponsored-projects-and-research/)) | The door into UF's **IPPD** (two-semester multidisciplinary teams that design, build and test; sponsors give an "educational grant", amount not published, [UNVERIFIED]; [IPPD](https://www.ippd.ufl.edu/sponsors/)) and UF capstones. The 2026–27 IPPD cohort is already set, so the earliest start is fall 2027. |
| **Tampa Hackerspace** | Tampa (≈ 2.5–3 h) | Open Make Night, Tuesdays 6–8 pm; Meetup | About 300 makers; reported $50/month or $500/year ([Tampa Hackerspace](https://tampahackerspace.com/membership/), price from search snippet, [UNVERIFIED]). Post the short job ad (§6); good for a remote builder of sub-assemblies. |
| **USF** (Tampa) | Tampa | ME Industry & Community Partners Program (capstone sponsorship; fee not published, [UNVERIFIED]) ([USF ME partners](https://www.usf.edu/engineering/me/about-us/industry-and-community-partners-program.aspx)); student groups RoboBulls and 3D HAB-Lab via BullsConnect ([RoboBulls](http://usfrobobulls.org/)); the IEEE Florida West Coast Robotics and Automation Society chapter ([IEEE FWC RAS](https://r3.ieee.org/fwc/chapters/ras)) | ME and EE students for remote design help; capstone if the timeline allows |
| **UCF** (Orlando) | Orlando | MAE senior design coordinators: Kurt Stresau and Dr Mark Steiner; the CS senior design program asks sponsors for a $1,500 team donation ([UCF Senior Design Hub](https://www.cecs.ucf.edu/senior-design-hub/), [UCF CS SD](https://www.eecs.ucf.edu/cssd/)) | A firmware-only CS team; too far for fittings |
| **Handshake** | All of the above | Free employer posting ([Handshake](https://joinhandshake.com/employers/create-a-job/)) | One post reaches FGCU, USF, UCF and UF students |

### Local product-development and prototyping firms

| Firm | Where | Notes |
|---|---|---|
| **123 Design** | Sarasota, 1990 Main St | Industrial design, CAD engineering, prototyping; works with startups, consumer electronics and medical devices. States turnkey design-to-prototype projects **typically begin around $15,000**, idea to working prototype in **8–12 weeks**, with phased options ([123 Design](https://123.design/)). **The closest studio-model (d) option.** Ask whether they do pneumatic or cable mechanisms and firmware in-house. |
| **Prototype House** | HQ Miami; offices in Fort Lauderdale and Sarasota | Industrial design, ME, electronics, prototyping; works with individual inventors; no published pricing ([Prototype House](https://www.prototypehouse.com/about-us)). |
| **3D Printing Expert of Naples** | Naples (one-person shop) | 3D printing, rapid prototyping, CAD, **3D laser scanning** ([site](https://3d-printing-expert.com/3d-printing-prototyping-design-of-naples-fl/)). Useful for a **3D scan of Michael's head** (helmet-fit geometry for the engineer) and for local prints. Not a mechatronics designer. |

**Caution with "inventor services" firms in general** [JUDG]: some firms that market to inventors bundle patent searches, marketing and manufacturing. SP1 needs engineering only. Ask for an engineering-only scope, a named engineer and an hourly or phase price before signing anything.

### Recommended local setup

1. **Engineer, remote** (Upwork US or Kolabtree; a Florida engineer if one turns up), Phase 1–2.
2. **Builder, local**, found in this order:
   1. a Naples or Fort Myers med-device engineer moonlighting (could also take Phase 2: best case);
   2. an FGCU bioengineering senior or graduate student, paid hourly, working off-campus;
   3. a maker found via Tampa Hackerspace or Suncoast Fab Lab, working at their shop, with try-on visits to Naples.
3. **One local scan** at 3D Printing Expert of Naples before Phase 2.
4. **Quote check:** ask 123 Design for a Phase 1-equivalent quote as a benchmark against the freelancers.

---

### Sources (accessed 2026-10-02)

- BLS engineering wages: https://www.bls.gov/opub/ted/2026/force-mass-mechanisms-and-vectors-employment-projections-and-wages-in-engineering.htm
- Upwork cost pages (search snippets; direct fetch 403): https://www.upwork.com/hire/mechanical-engineers/cost/ · https://www.upwork.com/hire/embedded-systems-engineers/cost/ · https://www.upwork.com/pricing/client
- Upwork fees summary: https://golance.com/blogs/upwork-fees-explained-2026 · payment protection: https://gigradar.io/blog/upwork-payment-protection-fixed-price · https://support.upwork.com/hc/en-us/articles/211063748
- Upwork IP terms summary: https://terms.law/2023/07/23/upworks-terms-ownership-of-freelancers-work-product/
- Toptal cost: https://www.hireinsouth.com/post/how-much-does-toptal-cost
- Kolabtree: https://www.kolabtree.com/blog/important-information-for-kolabtree-experts-transition-to-service-model/ · https://www.kolabtree.com/user-agreement
- Contra: https://www.remogrid.com/blog/reviews/is-contra-worth-it-freelance-review
- Fiverr: https://www.fastlancer.org/en/fastlancer-blog/fiverr-review/
- Cad Crowd: https://www.cadcrowd.com/blog/how-much-does-it-cost-to-develop-a-new-physical-product-a-complete-2026-breakdown/ · https://www.cadcrowd.com/blog/how-much-do-engineering-design-services-cost/amp/
- Predictable Designs: https://predictabledesigns.com/how-much-will-a-prototype-cost/
- Design1st: https://design1st.com/how-product-design-firms-charge/
- Studios list: https://lanpdt.com/prototype-development-companies/
- Machinist and job-shop rates: https://www.ziprecruiter.com/Jobs/Prototype-Model-Shop?layout=2pane_v2 · https://fabcon.com/articles/precision-cnc-machining/cnc-machining-hourly-rate-us/
- Capstone: https://engineering.unt.edu/connect/capstone-sponsorship.html · https://www.mech.utah.edu/capstone/sponsors/ · https://eds.mines.edu/project-sponsorship/ · https://www.me.utexas.edu/academics/undergraduate-program/senior-design-projects/senior-design-sponsorship
- Intern pay: https://www.glassdoor.com/Salaries/mechanical-engineering-intern-salary-SRCH_KO0,29.htm · https://www.ziprecruiter.com/Salaries/Mechanical-Engineering-Intern-Salary
- Handshake: https://joinhandshake.com/employers/create-a-job/
- University IP policy examples: https://policies.umd.edu/research/university-of-maryland-intellectual-property-policy · https://www.usnh.edu/policy/unh/viii-research-policies/d-intellectual-property-policy
- Hackster Pro: https://www.hackster.io/pro
- Parts services: https://jlcpcb.com/help/article/pcb-assembly-price · https://sendcutsend.com/pricing/ · https://www.xometry.com/capabilities/3d-printing-service/ · https://www.niro3d.cz/en/blog/niro3d-vs-xometry-protolabs-comparison
- Copyright work-for-hire: https://www.copyright.gov/circs/circ30.pdf
- FDA: https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-807 · https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-890/subpart-F/section-890.5660
- Standards: https://standards.globalspec.com/std/14552588/ul-1647 · https://www.csagroup.org/store/product/iec_085019/
- PE industrial exemption: https://peimpact.com/pe-industrial-exemption/
- Liability and insurance norms: https://clauseshield.app/blog/liability-caps-unlimited-liability · https://www.freelancermap.com/blog/the-most-interesting-types-of-freelancing-insurance/
- Makerspaces: https://dallasmakerspace.org/join/ · https://www.makernexus.org/
- SW Florida (§8): https://careers.arthrex.com/go/Medical-Device-Jobs-in-Naples/7572000/ · https://www.fgcu.edu/eng/internships/ · https://www.fgcu.edu/eng/ · https://library.fgcu.edu/makerspace · https://www.suncoastscience.org/members/ · https://www.eng.ufl.edu/sarasota/industry-engagement/sponsored-projects-and-research/ · https://www.ippd.ufl.edu/sponsors/ · https://tampahackerspace.com/membership/ · https://www.usf.edu/engineering/me/about-us/industry-and-community-partners-program.aspx · http://usfrobobulls.org/ · https://r3.ieee.org/fwc/chapters/ras · https://www.cecs.ucf.edu/senior-design-hub/ · https://www.eecs.ucf.edu/cssd/ · https://123.design/ · https://www.prototypehouse.com/about-us · https://3d-printing-expert.com/3d-printing-prototyping-design-of-naples-fl/
