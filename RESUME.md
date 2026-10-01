# RESUME HERE — Project Scratch status at pause (2026-10-01)

## Done
- Phase 1 foundations (01-foundations/, 6 docs), Phase 2 mechanism teams (02-mechanisms/, 7 designs), Phase 3 tournament (03-tournament/, 3 judges + hybrid), Phase 4 red team (04-redteam/, 3 attacks), DECISION (03-tournament/DECISION.md), DESIGN-FREEZE (05-engineering/DESIGN-FREEZE.md).
- Phase 5 delivered so far: test-protocols.md, electronics-firmware.md, firmware/sp1_scratch/sp1_scratch.ino, firmware/README.md.
- Possibly delivered by background agents after the pause (check for files): 05-engineering/mechanical.md, 05-engineering/tips.md, 05-engineering/cad/tips/*.scad, cad/tips/stl/*.stl, cad/tips/README.md, cad/tips/gen_tips_stl.py.

## Next steps (in order)
1. Confirm mechanical.md and tips.md exist and read their reports; check mechanical.md absorbed test-protocols.md §Q (rail scale, ≤0.9 N bare weight + trim spring, tip-code marks, 0/45/90° rotation, cradle isolation).
2. Launch CAD AGENT: OpenSCAD + STL (venv: scratchpad cadenv with trimesh+manifold3d; a fresh session must recreate it: `python3 -m venv cadenv && pip install trimesh manifold3d numpy`) for every printed part in mechanical.md §11 → 05-engineering/cad/. Report dimensional conflicts.
3. Launch BOM AGENT: 05-engineering/bom.md from mechanical.md §11, tips.md BOM, electronics-firmware.md parts, test-protocols.md bench kit. Qty, spec, price, source URL, substitute.
4. Launch INTEGRATOR: 07-package/SP1-PACKAGE.md with sections A–P per BRIEF §19 (pull from DECISION, DESIGN-FREEZE, mechanical, tips, electronics-firmware, test-protocols, bom; include an index of cad/ and firmware/).
5. Phase 6 gates in parallel: BUILD REVIEW (BRIEF §20), SENSATION GATE (§21), SAFETY GATE (§22) — each reads the package cold, not told to be agreeable. Fix the package; re-run any gate that failed.
6. Final handoff to Michael: summary, package path, order list, first-weekend plan.

## Open items carried
- Tip edge radius: safety ≥0.4 mm vs tip-interface 0.3 mm → SP1 default W/B45 at R0.4–0.5; A45 (0.3) gated behind forearm + tape test.
- [VERIFY] OpenRB-150 logic survives VIN cut on USB (bench B3 hard gate).
- Firmware not compiled with a real toolchain; build reviewer should compile in Arduino IDE instructions or flag.
