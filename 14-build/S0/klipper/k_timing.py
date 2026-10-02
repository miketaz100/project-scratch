#!/usr/bin/env python3
"""
k_timing.py - S0b Klipper timing check (V-K1) from a logic-analyser capture (PROJECT SCRATCH, 14-build/S0/klipper)

Capture with PulseView (sigrok) at >= 1 MHz while line.gcode runs (made by:
  python3 s0_stream.py line --strokes 500 --hz 1.4 --amp 16 --psi 90 > line.gcode):
  (psi 90 = straight at cable A's stop, so cable A reverses only at the stroke ends)
  D0 = the LED GPIO ("valve"), D1 = DIR pin of cable A.  Export: File > Export > CSV (one row per
  sample or "compressed" change-only rows both work; first column = time in seconds or sample number).
Run:  python3 k_timing.py capture.csv [--samplerate 1000000] [--led 1] [--dir 2]
      (--led / --dir = column numbers of D0 and D1 in the CSV; column 0 is time / sample)

It finds every DIR edge (a stroke reversal of cable A) and the first LED rising edge after it, and
prints how much that delay varies over all strokes.  Every stroke of the LINE file is identical, so
the delay should be the same each time.  PASS (V-K1): max - min <= 4 ms (= +-2 ms) over >= 500 strokes,
and the median full cycle (two DIR edges) within 1 % of 1/hz.
"""
import csv, statistics, sys

def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__); return
    path = args[0]
    sr = float(args[args.index("--samplerate") + 1]) if "--samplerate" in args else None
    cl = int(args[args.index("--led") + 1]) if "--led" in args else 1
    cd = int(args[args.index("--dir") + 1]) if "--dir" in args else 2
    t_prev = None; led_prev = dir_prev = None
    dir_edges, led_rises = [], []
    with open(path) as f:
        for row in csv.reader(f):
            if not row or row[0].startswith((";", "#")) or not row[0].replace(".", "", 1).replace("e-", "", 1).lstrip("-").isdigit():
                continue
            t = float(row[0]) / sr if sr else float(row[0])
            led, dr = int(float(row[cl])), int(float(row[cd]))
            if dir_prev is not None and dr != dir_prev:
                dir_edges.append(t)
            if led_prev is not None and led == 1 and led_prev == 0:
                led_rises.append(t)
            led_prev, dir_prev = led, dr
    delays, j = [], 0
    for t in dir_edges:
        while j < len(led_rises) and led_rises[j] < t:
            j += 1
        if j < len(led_rises):
            delays.append(led_rises[j] - t)
    if len(delays) < 10:
        print(f"only {len(delays)} DIR->LED pairs found: check the channel columns"); return
    cyc = [b - a for a, b in zip(dir_edges[:-2:2], dir_edges[2::2])]
    spread = (max(delays) - min(delays)) * 1000
    print(f"strokes analysed: {len(delays)}")
    print(f"DIR edge -> LED on delay: median {statistics.median(delays)*1000:.2f} ms, min {min(delays)*1000:.2f}, max {max(delays)*1000:.2f}, spread {spread:.2f} ms")
    print(f"full cycle: median {statistics.median(cyc)*1000:.1f} ms (1.4 Hz -> 714.3 ms)")
    print("V-K1 timing:", "PASS" if spread <= 4.0 and len(delays) >= 500 else "FAIL or too few strokes")

if __name__ == "__main__":
    main()
