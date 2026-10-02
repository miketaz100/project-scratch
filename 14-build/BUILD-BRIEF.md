# SP1 v3 BUILD ENGINEERING — common brief

Binding: 12-sp1v2/DECISION-3.md and 12-sp1v2/SYSTEM-SPEC-v3.md (freeze v3; its §11 work packages are your scope definitions), 12-sp1v2/safety-ruling-dish-gate.md (C1–C8), 01-foundations/safety-requirements.md (13 red lines), 01-foundations/hair-interaction.md.

Builder: Michael himself (decided 2026-10-02), in Naples FL, budget-sensitive ("can't drop thousands"), experience level and printer ownership UNKNOWN — write for a careful first-timer: every step explicit, every tool named, every screw length given, photos-in-words, what "good" looks like, what to do if it isn't. Assume he may NOT own a 3D printer: mark each printed part "print service OK" or "needs iteration, home printer recommended", and give JLC3DP-ready notes (material, process, orientation, tolerances).

Spending is staged: S0 → A → B → C → D (SYSTEM-SPEC-v3 §10). No stage's cart is bought before the previous gate passes. Keep every cart lean; prefer bought parts over fabrication; reuse earlier-stage parts.

CAD: OpenSCAD sources (basic primitives only; no binary available locally, so be meticulous) plus STL generated with the Python venv at /private/tmp/claude-501/-Users-michaeltaszycki/97b6a4f1-1d4a-4d86-ac07-7d01cd99e323/scratchpad/cadenv/bin/python (trimesh + manifold3d; verify watertight; print bounding boxes). Use SYSTEM-SPEC-v3 §3 datums and §5 interface tables; record any interface conflict in your package's CONFLICTS.md instead of silently changing it. Reuse earlier CAD where it still fits (05-engineering/cad/tips/, 05-engineering/cad/frame/lib_sp1.scad).

Prices: live-check every part you specify (WebSearch/WebFetch); tag [cited] with URL and date, [est], or [verify].

Write early and refine, so a stall does not lose work. Do not edit SYSTEM-SPEC-v3.md; propose changes in your CONFLICTS.md.
