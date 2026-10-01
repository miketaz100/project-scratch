# RESUME HERE — Project Scratch status (2026-10-01, cloud session)

Repo: github.com/miketaz100/project-scratch (branch main). Cloud session working copy: /home/user/project-scratch. CAD venv (trimesh + manifold3d, no scipy, no OpenSCAD binary): /tmp/claude-0/-home-user-ai-social/a9d4d996-bfe2-5b1b-8c54-ae462b273760/scratchpad/cadenv; a fresh session recreates it with `python3 -m venv cadenv && cadenv/bin/pip install trimesh manifold3d numpy`.

## Done
- Phases 1–4 and the DECISION / DESIGN-FREEZE (see DIRECTOR-LOG.md).
- Phase 5 engineering, all five deliverables now exist: test-protocols.md, electronics-firmware.md (+ firmware/), tips.md (+ cad/tips/*.scad, 14 STLs, README), mechanical.md (48 printed designs, 60 pieces).
- DESIGN-FREEZE-ADDENDUM-1.md: director rulings on the mechanical lead's 13 deviations (24 mm pitch, servo beside the palm on a yoke, MGN9C, two springs, 25 mm tether, proof load 7.5 N, E = geometric engagement, servo zero pin, brown-out threshold 4.0 V). Binding over the freeze.

## In flight (launched 2026-10-01 cloud; if their files are missing, re-run from the briefs in DIRECTOR-LOG)
- TIP follow-up: paddle DRAFT_Y = 10, centre-paddle RISER = 9 mm, regenerate cad/tips/stl, update tips.md §8/§9/§10.
- CAD agent: 05-engineering/cad/frame/ (one .scad per part or group, gen_frame_stl.py, stl/, README.md, CONFLICTS.md) for mechanical.md §11 P1–P48.
- BOM agent: 05-engineering/bom.md (totals by stage; pins the lift spring part number; [cited]/[est]/[verify] on every price).

## Next steps (in order)
1. When the three above land: read cad/frame/CONFLICTS.md and bom.md [verify] list; resolve anything that changes mechanical.md (add to the addendum, do not edit the freeze).
2. INTEGRATOR → 07-package/SP1-PACKAGE.md, sections A–P per BRIEF §19, pulling from DECISION, DESIGN-FREEZE + ADDENDUM-1, mechanical, tips, electronics-firmware, test-protocols, bom; include a file index of cad/ and firmware/; apply the addendum's amendments to test-protocols (L6(a) pull at nail height, L6(b) proof 7.5 N, K2.13 ≥ 9 mm, E6 in the matrix, servo-zero pin in bring-up).
3. GATES in parallel, each reads the package cold and is told not to be agreeable: BUILD REVIEW (BRIEF §20; first step: compile the firmware in the Arduino IDE instructions or flag), SENSATION GATE (BRIEF §21; must rule on 24 mm pitch, D2), SAFETY GATE (BRIEF §22; must rule on D10 float-jam force, brown-out window, tether). Write to 06-gates/. Fix the package; re-run any failed gate.
4. Final handoff to Michael: summary, package path, order list by vendor, first-weekend plan (Stage 0 wand first).

## Open items carried
- [VERIFY] OpenRB-150 logic survives VIN cut on USB (bench B2/B3 hard gate).
- Firmware not compiled with a real toolchain (cloud session cannot reach Arduino downloads); build review must compile or flag.
- XL330 axis/horn/body hole dimensions and MGN9 hole pitch marked [VERIFY] in mechanical.md; check against vendor drawings before printing the servo cradle and rail mast.
- Bare floating weight margin 2 g (90.1 g vs 92 g); kitchen scale decides (L1); fallbacks in mechanical.md §6.5.
- Tip edge radius: safety ≥ 0.4 mm; A45 (0.3 mm) gated behind forearm + tape test; tip P needs two nested nails to reach R 0.4.
- Michael's plan: self-build in his apartment (outsourcing considered and declined 2026-10-01).

## PAUSED 2026-10-01 (Michael asked to stop spending cloud credits until the limit resets)
- CAD agent was stopped mid-run. Partial output: 05-engineering/cad/frame/gen_frame_stl.py (in progress; its last self-report: "P3 has a stray placeholder cylinder at the origin and the P4 vent code is muddled"). No .scad files, no STLs, no README or CONFLICTS yet. On resume, relaunch the CAD agent with the same brief (DIRECTOR-LOG 2026-10-01 cloud entry) and tell it to start from the existing generator.
- bom.md and tips follow-up are complete and committed. Integrator and gates not started.
- Say "resume Project Scratch" to continue.
