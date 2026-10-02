# DIRECTOR'S DECISION 3 — SP1 "PUPPET HALO, LEAN" (2026-10-02)

Builds on DECISION-2.md (+ its NORTH STAR AMENDMENT: an on-par scratching sensation, not a human illusion) and the must-fix list in 12-sp1v2/decision-analysis.md. Supersedes the per-pin valve system, the air synchro, powered travel, and the second-pad-parts purchase of SYSTEM-SPEC.md (freeze v2).

## Michael's decisions (leap round 4 review, 2026-10-02)
1. DISH GATE pins, two pin lines (11-leaps/round-4/leap4-A.md §4, variant L3-2). "Worth the simplicity." Pending: safety ruling 12-sp1v2/safety-ruling-dish-gate.md (snag pull).
2. XY BELT MASTER (path in firmware; needed by the dish gate for off-centre chords and one-way D-paths). Implied by 1; flagged to Michael.
3. CABLE DRIVE LINES instead of the sealed air synchro: three-drum tendon puppet, drums on steppers in the box (11-leaps/round-4/leap4-D.md L1; converges with leap4-F L3).
4. HAND-MOVED STATIONS for the first build: passive halo with friction hinges/detents, no travel motors on the head (leap4-E E4, leap4-F L4). Automatic drift (box-driven cable travel, leap4-C C2) is a later upgrade.
5. LIGHTER CARBON FRAME: straight carbon tubes in printed nodes, carbon front band, no balancers (leap4-C C3).
6. STOCK 3D-PRINTER CONTROLLER BOARD running Klipper (leap4-E E1), with the hardware safety loop kept independent of it. Director judges it at least as capable now that per-pin valve timing is gone; Klipper has cable-winch kinematics.
7. OUTSOURCED PRINTING of precision parts (leap4-E E3).
8. ONE PAD for the first build. Second pad deferred: its parts are NOT bought now; the halo keeps cheap mounting provisions (Director's assumption, flagged to Michael).
9. NO squeeze egg and NO head scan in this build. Controls: hold-to-run, NC e-stop, speed and intensity knobs (+ PC serial for experiments). Advanced pattern language (κ-grammar, fatigue ledger) deferred; simple anti-habituation variation (stroke length/chord, heading, timing jitter, pauses) required.
10. NOT adopted: skyhook (rejected); scratch-quality leaps of leap4-B (parked).

## Still open
- Who builds: DIY vs hired engineer + local builder (13-outsourcing/outsourcing-options.md). Needs from Michael: budget ceiling, target date, drive distance, whether a builder can work in his apartment.
- Safety ruling on the dish gate.
