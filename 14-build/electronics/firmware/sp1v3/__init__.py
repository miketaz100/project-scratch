"""SP1 v3 host software (runs on the BTT CB1 next to Klipper).

Modules
  limits    the one limits table and clamp point
  ik        dish-aware inverse kinematics: block offset d -> three cable lengths
  paths     path primitives (line, chord, circle, D-path, rim connectors, park)
  checker   the C5 path checker, run on every token before it is sent
  variation simple anti-habituation variation generator
  planner   mode -> token stream (uses variation, checker)
  klipper   Klipper API-socket client (+ a simulator for bench and tests)
  scorer    the state machine, streamer, controls, logging, command server
  reflexd   snag reflex daemon (tension frames from the Pico -> trip)
  scratchctl  console client
"""
__version__ = "3.0.0"
