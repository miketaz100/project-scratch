# PROJECT SCRATCH — Director's Brief (verbatim from Michael, 2026-10-01)

Mission: develop the best physically achievable first prototype of a hands-free automated HEAD SCRATCHING DEVICE.

This is specifically a SCRATCHER. NOT primarily a scalp massager, vibration helmet, scalp brush, kneading device, or generic relaxation helmet.

The fundamental experience to reproduce: THE PLEASURABLE SENSATION OF ANOTHER PERSON SCRATCHING YOUR SCALP WITH THEIR FINGERNAILS. That distinction governs the entire project.

## 1. END GOAL
Project ends when we converge on ONE SPECIFIC PHYSICAL PROTOTYPE that Michael can realistically build, assemble, and test in his apartment. Output must be resolved enough that Michael can go DESIGN → ORDER PARTS → FABRICATE/PRINT → ASSEMBLE → TEST without solving major unanswered engineering questions. Name: SCRATCH PROTOTYPE 1 — SP1.
Quality bar: "the most intelligently designed Prototype 1 we can reasonably produce before physical testing becomes more informative than additional simulation/reasoning."

## 2. NORTH STAR: SCRATCH QUALITY
"Does this actually feel like someone scratching my head?" Not merely movement, pressure, vibration, relaxation.
Secondary: useful scalp coverage, comfort, adjustable intensity, repeatable motion, hair compatibility, minimal hair pulling, minimal entanglement, reasonable noise, cleanability, ease of iteration, apartment prototyping, affordable P1 construction. Commercial manufacturability NOT a primary constraint. SP1 is an experimental machine to answer the most important physical questions.

## 3. USER / ENVIRONMENT
Designed for Michael himself; one person testing in his apartment. Do NOT burden P1 with mass manufacturing, retail certification, universal sizing, packaging, waterproofing, miniaturization, battery, app, production tooling/cost. Favor commercially available components, simple fabrication, 3D-printable parts, common motors/servos/actuators, modular construction, adjustable components, replaceable scratching tips, rapid iteration. P1 can look like a prototype. It needs to WORK.

## 4. CORE ENGINEERING QUESTION
HOW DO WE MECHANICALLY REPRODUCE THE PHYSICS AND SENSORY CHARACTERISTICS OF HUMAN FINGERNAIL SCRATCHING ON A HAIR-COVERED SCALP?
Variables: contact geometry, tip geometry/radius/material, compliance, friction, normal force, tangential force, stroke length, velocity, acceleration, frequency, reciprocation, direction changes, randomness, spatial pattern, number of simultaneous contacts, contact spacing, scalp curvature, hair interference/direction, force variation, dwell time, movement across regions, human scratching patterns. Do not assume the mechanism before understanding the sensation.

## 5. MULTI-AGENT AUTONOMY
Director assembles the team. Do not optimize for minimizing tokens/agents/reasoning. Optimize for DESIGN QUALITY + SAFETY + PHYSICAL PLAUSIBILITY + INDEPENDENT EXPLORATION + BUILDABILITY + PROBABILITY SP1 FEELS GOOD.

## 6. INDEPENDENT EXPLORATION
Do NOT converge on the first plausible mechanism. Multiple independent mechanism-design efforts, initially not anchored on one another, attacking from different physical principles (reciprocating, oscillating, rotating trajectories, orbital, linkages, cams, servo fingers, compliant mechanisms, flexible arrays, moving carriages, articulated arms, cable-driven, combinations — examples, not recommendations). Invent alternatives.

## 7. FIRST-PRINCIPLES HUMAN SCRATCH MODEL
Before selecting mechanism, build an engineering model of human head scratching: fingers in contact, force, velocity, stroke length, patterns, nail vs. fingertip contact, nail/hair interaction, why normal scratching doesn't tangle hair, finger/nail compliance, variation by region (crown, sides, back, top, temples), which variables most determine pleasure. Separate KNOWN / ESTIMATED / UNKNOWN. No false precision.

## 8. RESEARCH
Aggressively research adjacent mechanisms: scalp devices, robotic massage, haptics, tactile stimulation, scratching/itch research, grooming tools, robotic fingers, wearable robotics, headgear mechanisms, hair-safe mechanical products, compliant mechanisms, cosmetic/medical scalp devices, automated brushing/combing, patents, academic literature, consumer products.

## 9. SAFETY ENGINEERING (independent track)
Analyze: hair entanglement, hair pulling, excessive normal/shear force, sharp edges, pinch points, motor stall, runaway actuation, mechanical failure, broken tips, skin abrasion, localized pressure, electrical safety, moving parts near hair, emergency shutoff, cleaning/hygiene. Do not solve safety by making it too weak to scratch. Prefer mechanical safety (force-limited mechanisms, compliance, clutches, current limits, breakaways, rounded geometry, guards, stops, e-stop, quick removal, hair exclusion around rotating parts) over software-only.

## 10. HAIR IS A PRIMARY CONSTRAINT
Model SCRATCHING ELEMENT ↔ HAIR ↔ SCALP explicitly. How does the element reach scalp? Push hair aside? Wrap? Can hair enter bearings/shafts/gears/joints? Can reciprocation catch strands? Does direction change pull hair? Can exposed rotation near scalp be eliminated?

## 11. SCRATCHING TIP DEVELOPMENT
Own subsystem. Interchangeable tips varying shape, radius, width, curvature, material, stiffness, compliance, finish, fingernail-like geometry. Michael must test multiple tips without rebuilding.

## 12. ADJUSTABILITY
Force, speed, stroke, frequency, contact angle, contact count, spacing, pattern — prioritize high-uncertainty, high-sensory-importance variables. SP1 is partly a RESEARCH RIG.

## 13. MECHANISM TOURNAMENT
Evaluate on: expected scratch realism, scalp contact quality, hair safety, force controllability, complexity, apartment buildability, component availability, cost, noise, reliability, adjustability, ease of iteration, coverage, failure modes. Do NOT let elegance beat sensation.

## 14. RED TEAM
Prove the leading design wrong: why won't it feel like fingernails? where does hair catch? what hurts/breaks? unrealistic tolerances? misused components? head movement? misalignment? motor stall? thick hair? after 20 minutes? what makes it annoying? could a radically simpler mechanism win? Converge only after surviving serious criticism.

## 15. DO NOT OVERENGINEER
Every subsystem must answer "does this help determine whether automated human-like scratching can feel excellent?" Partial coverage is acceptable. DO NOT REQUIRE FULL-HEAD COVERAGE IF IT COMPROMISES THE CORE EXPERIMENT.

## 16. PROTOTYPING STRATEGY
Do not preserve "helmet" architecture by default. Consider partial-head rig, single module, headband-mounted module, stationary test frame, manually positioned assembly. Goal: DISCOVER THE MECHANISM THAT CREATES AN EXCELLENT AUTOMATED HEAD SCRATCH.

## 17. PHYSICAL TESTING IS THE BOUNDARY
Continue until another hour of AI reasoning is less valuable than building and touching the prototype.

## 18. FINAL CONVERGENCE
Select ONE architecture. Not top three. Explain why it won. Fully engineer it.

## 19. SP1 FINAL ENGINEERING PACKAGE — required sections
A. Design overview (what, how, why it won, hypothesis tested)
B. Mechanical architecture (mechanism, DOF, motion generation, scratching module, mounting, adjustment, guards, safety)
C. Dimensions sufficient to fabricate
D. Component selection (motors, servos, actuators, bearings, shafts, springs, fasteners, electronics, controllers, PSU, switches, e-stop, wiring, structural hardware)
E. BOM (qty, spec, approx cost, sourcing, substitutes)
F. Fabricated components (3D printed parts, materials, geometry, orientation, tolerances, inserts, interfaces)
G. Scratching tips (several interchangeable variants)
H. Electronics (wiring architecture, controller, drivers, power, e-stop, inputs)
I. Control logic (pattern, speed, accel, limits, randomness, intensity, startup, shutdown, faults)
J. Assembly instructions (step by step)
K. Safety checklist (before touching Michael's head)
L. Bench testing (non-human)
M. First human test (conservative staged protocol)
N. Experiment matrix (what to vary)
O. Feedback form (realism, pleasure, intensity, hair pulling, discomfort, coverage, noise, desire to continue, qualitative)
P. Iteration map (what SP1 results imply for SP2)

## 20. BUILDABILITY GATE
Independent BUILD REVIEW agent, not told to be agreeable: "If Michael orders exactly these parts and follows these instructions in his apartment, can he realistically build this?" Identify missing parts, impossible fabrication, unspecified dimensions, incompatible components, unclear assembly, electrical omissions, hidden assumptions, tools not listed, tolerances likely to fail, unsafe steps. Fix. Repeat if necessary.

## 21. SENSATION GATE
Independent reviewer: "Have we accidentally designed a scalp massager instead of a head scratcher?" If meaningfully yes, do not ship; return to engineering.

## 22. SAFETY GATE
Independent safety reviewer: credible ways SP1 could injure skin, pull/entangle hair, pinch, over-force, fail dangerously, be electrically unsafe. Resolve before human testing.

## 23. COMPLETION CRITERIA (Michael's list was truncated after item 9; items 10+ inferred by Director)
1. Sensation decomposed sufficiently to guide engineering.
2. Multiple genuinely different mechanisms explored.
3. Strongest mechanisms compared.
4. Selected architecture survived adversarial review.
5. Hair interaction explicitly engineered.
6. Safety independently reviewed.
7. Scratching interface designed as an experimental variable.
8. One architecture selected.
9. Actual components selected.
10. [inferred] Complete engineering package (sections A–P) produced.
11. [inferred] Buildability, Sensation, and Safety gates passed.
12. [inferred] Michael can proceed to order parts without unresolved major engineering questions.
