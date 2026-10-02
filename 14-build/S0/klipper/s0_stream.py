#!/usr/bin/env python3
"""
s0_stream.py - write S0b test paths as Klipper G-code in CABLE space (PROJECT SCRATCH, 14-build/S0/klipper)

The pen plate (stand-in for the pin block) is at offset d = (x, y) mm from centre.  Three cables
run from fixed housing stops at R 60 mm (90, 210, 330 deg) to posts at R 22 mm on the plate.
Inverse kinematics: cable length change l_i = |S_i - (P_i + d)| - |S_i - P_i|  (mm of cable).
Each 1 mm of path becomes one "G1 A.. B.. C.. F.." move, so 2 Hz on a 32 mm line is ~130-200
segments per second (spec 8.2 asks for <= 200/s).  The LED on FAN0 ("valve") turns on while
|d| < LAND_R, a stand-in for the nails being down; its edges are the timing test.

Usage (on the CB1 or any computer with Python 3):
  python3 s0_stream.py line   --strokes 500 --hz 1.4 --amp 16 --psi 0     > line.gcode
  python3 s0_stream.py pline  --strokes 120 --hz 1.4 --amp 16             > pline.gcode
  python3 s0_stream.py circle --revs 40 --hz 1.0 --radius 11.5 --offset 3.5 > circle.gcode
  options: --deadband 0.0,0.0,0.0  (per-cable lost motion in mm, measured in test T; compensation is
           added at each cable reversal, smoothed over 3 mm of path)   --dry (print a summary only)
Upload the .gcode in Mainsail (port 80 of the CB1) and press Print.  Every file starts at the
centre with AXES_ON and ends with the LED off; it never moves farther than |d| = 17 mm.
Units: cable mm.  Sign: +A pays cable A out.  If a cable winds the wrong way, invert that dir_pin
(add or remove "!") in printer.cfg.
"""
import argparse, math, random, sys

STOP_R, POST_R = 60.0, 22.0
ANG = (90.0, 210.0, 330.0)
LAND_R = 10.0
D_LIMIT = 17.0

def stops_posts():
    S = [(STOP_R * math.cos(math.radians(a)), STOP_R * math.sin(math.radians(a))) for a in ANG]
    P = [(POST_R * math.cos(math.radians(a)), POST_R * math.sin(math.radians(a))) for a in ANG]
    return S, P

S, P = stops_posts()
L0 = [math.dist(s, p) for s, p in zip(S, P)]

def ik(d):
    return [math.dist(s, (p[0] + d[0], p[1] + d[1])) - l0 for s, p, l0 in zip(S, P, L0)]

def line_pts(psi, amp, step=1.0):
    c, s = math.cos(math.radians(psi)), math.sin(math.radians(psi))
    n = int(round(2 * amp / step))
    out = [(-amp + 2 * amp * k / n) for k in range(n + 1)]
    return [(u * c, u * s) for u in out]

def stroke_times(n_pts, hz):
    # sinusoidal velocity profile per half-cycle: position u = -A cos(pi t / T), sampled at equal
    # path steps -> segment durations from the arc-cosine.  T = half period.
    T = 0.5 / hz
    us = [-1 + 2 * k / (n_pts - 1) for k in range(n_pts)]
    ts = [T * math.acos(max(-1, min(1, -u))) / math.pi for u in us]
    return [ts[k + 1] - ts[k] for k in range(n_pts - 1)]

class Writer:
    def __init__(self, deadband):
        self.out = []
        self.prev = ik((0.0, 0.0))
        self.prev_cmd = list(self.prev)
        self.dirn = [0, 0, 0]
        self.comp = [0.0, 0.0, 0.0]
        self.db = deadband
        self.led = 0
        self.t = 0.0
        self.n = 0

    def emit(self, d, dt):
        if math.hypot(*d) > D_LIMIT + 1e-6:
            raise SystemExit(f"refusing |d| = {math.hypot(*d):.2f} > {D_LIMIT}")
        L = ik(d)
        if max(abs(L[i] - self.prev[i]) for i in range(3)) < 1e-6:
            return
        for i in range(3):
            dl = L[i] - self.prev[i]
            sgn = (dl > 1e-9) - (dl < -1e-9)
            if sgn:
                self.dirn[i] = sgn
            target = 0.5 * self.db[i] * self.dirn[i]
            # approach the +-b/2 offset over ~3 mm of cable travel after each reversal
            self.comp[i] += (target - self.comp[i]) * min(1.0, abs(dl) / 3.0)
        cmd = [L[i] + self.comp[i] for i in range(3)]
        dist = math.sqrt(sum((cmd[i] - self.prev_cmd[i]) ** 2 for i in range(3))) or 1e-6
        f = 60.0 * dist / max(dt, 1e-4)
        want = 1 if math.hypot(*d) < LAND_R else 0
        if want != self.led:
            self.out.append(f"SET_PIN PIN=valve_led VALUE={want}")
            self.led = want
        self.out.append(f"G1 A{cmd[0]:.4f} B{cmd[1]:.4f} C{cmd[2]:.4f} F{f:.1f}")
        self.prev = L
        self.prev_cmd = cmd
        self.t += dt
        self.n += 1

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["line", "pline", "circle"])
    ap.add_argument("--strokes", type=int, default=120)
    ap.add_argument("--revs", type=int, default=40)
    ap.add_argument("--hz", type=float, default=1.4)
    ap.add_argument("--amp", type=float, default=16.0)
    ap.add_argument("--psi", type=float, default=0.0)
    ap.add_argument("--radius", type=float, default=11.5)
    ap.add_argument("--offset", type=float, default=3.5)
    ap.add_argument("--deadband", default="0,0,0")
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--dry", action="store_true")
    a = ap.parse_args()
    db = [float(x) for x in a.deadband.split(",")]
    rnd = random.Random(a.seed)
    w = Writer(db)
    w.out += ["; S0b s0_stream.py " + " ".join(sys.argv[1:]), "AXES_ON", "SET_PIN PIN=valve_led VALUE=0", "G1 A0 B0 C0 F600"]
    if a.mode in ("line", "pline"):
        psi = a.psi
        # lead-in: centre -> -amp along the first heading, slowly, LED off
        for d in line_pts(psi, a.amp)[: int(a.amp) + 1][::-1]:
            w.emit(d, 0.02)
        for k in range(a.strokes):
            pts = line_pts(psi, a.amp)
            if k % 2:
                pts = pts[::-1]
            for d, dt in zip(pts[1:], stroke_times(len(pts), a.hz)):
                w.emit(d, dt)
            if a.mode == "pline" and k % 2:
                # heading advances 4.5 deg per out-and-back cycle (+-1.5 deg jitter), turned ON THE RIM
                # (|d| = amp, nails up) along a short arc - never inside |d| < 13.7 (spec 8.3)
                dpsi = 4.5 + rnd.uniform(-1.5, 1.5)
                for j in range(1, 4):
                    ang = math.radians(psi + 180.0 + dpsi * j / 3)
                    w.emit((a.amp * math.cos(ang), a.amp * math.sin(ang)), 0.01)
                psi += dpsi
    else:
        R, e = a.radius, a.offset
        n = int(round(2 * math.pi * R))                    # 1 mm segments
        dt = (1.0 / a.hz) / n
        start = (e + R, 0.0)
        steps = int(math.hypot(*start))
        for k in range(1, steps + 1):
            w.emit((start[0] * k / steps, 0.0), 0.02)
        rot = 0.0
        for r in range(a.revs):
            for k in range(1, n + 1):
                th = 2 * math.pi * k / n
                cx, cy = e * math.cos(math.radians(rot)), e * math.sin(math.radians(rot))
                w.emit((cx + R * math.cos(th + math.radians(rot)), cy + R * math.sin(th + math.radians(rot))), dt)
            rot += rnd.uniform(15, 40)                     # spec 4.5: offset heading rotates 15-40 deg per rev
    w.out += ["SET_PIN PIN=valve_led VALUE=0", "G1 A0 B0 C0 F600", "M400", "; end"]
    if a.dry:
        print(f"{a.mode}: {w.n} segments, {w.t:.1f} s, {w.n / max(w.t, 1e-9):.0f} segments/s average", file=sys.stderr)
    else:
        print("\n".join(w.out))

if __name__ == "__main__":
    main()
