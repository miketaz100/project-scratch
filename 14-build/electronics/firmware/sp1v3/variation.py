"""Simple anti-habituation variation (SPEC §8.4; DECISION-3 #9).

A seeded generator draws, per stroke, the deviations listed in the spec table.  It never
draws geometry directly into contact: every number goes back through `limits.clamp()` and
every resulting token through the checker.  `seed <n>` makes a session reproducible.
"""
from __future__ import annotations

import random
from dataclasses import dataclass

from . import limits as L

MIX_WEIGHTS = (("pline", 50), ("line", 15), ("circle", 10), ("chord", 15), ("dpath", 10))


@dataclass
class StrokeDraw:
    e: float = 0.0               # chord offset (mm), signed
    period_scale: float = 1.0
    kick_deg: float = 0.0        # heading kick at this turnaround
    pause_s: float = 0.0         # rim park before this stroke
    flip_precession: bool = False


class Variation:
    def __init__(self, seed: int = 1, enabled: bool = True):
        self.seed(seed)
        self.enabled = enabled

    def seed(self, n: int):
        self._seed = int(n)
        self.rng = random.Random(self._seed)
        self._recent = []                 # last stroke tuples for the no-repeat rule
        self._group = "AB"
        self._group_left = 0
        self._phrase_mode = None
        self._phrase_left = 0.0
        self._next_long_pause = self.rng.uniform(30.0, 90.0)
        self._phrase_force = None
        self._phrase_bratio = 1.0

    # ---------------------------------------------------------------- per stroke
    def stroke(self, chord_on: bool, f: float, t_session: float) -> StrokeDraw:
        if not self.enabled:
            return StrokeDraw()
        r = self.rng
        d = StrokeDraw()
        if chord_on and r.random() < 0.40:
            d.e = r.uniform(0.0, 7.0) * (1 if r.random() < 0.5 else -1)
        d.period_scale = min(1.3, max(0.7, r.gauss(1.0, 0.15)))
        if r.random() < 0.30:
            d.kick_deg = r.uniform(10.0, 30.0) * (1 if r.random() < 0.5 else -1)
        if r.random() < L.clamp("pause_p", 0.08):
            d.pause_s = r.uniform(0.2, 0.8)
            d.flip_precession = r.random() < 0.2
        if t_session >= self._next_long_pause:
            d.pause_s = r.uniform(2.0, 4.0)
            d.flip_precession = r.random() < 0.2
            self._next_long_pause = t_session + r.uniform(30.0, 90.0)
        # no (length, period, heading, group) tuple repeated for > 3 strokes
        key = (round(d.e), round(d.period_scale * 20), round(d.kick_deg / 5), self._group)
        self._recent.append(key)
        self._recent = self._recent[-4:]
        if len(self._recent) == 4 and len(set(self._recent)) == 1:
            d.period_scale = min(1.3, max(0.7, d.period_scale + r.choice((-0.12, 0.12))))
            d.kick_deg += r.choice((-12.0, 12.0))
            self._recent[-1] = None
        return d

    # ---------------------------------------------------------------- groups
    def groups(self, auto: bool, fixed: str = "AB") -> tuple[str, float]:
        """Group pattern A / B / A+B changed every 4-12 strokes; B at 0.5-1.0 x rail in contrast phrases."""
        if not auto or not self.enabled:
            return fixed, 1.0
        if self._group_left <= 0:
            self._group = self.rng.choice(("A", "B", "AB"))
            self._group_left = self.rng.randint(4, 12)
            self._phrase_bratio = 1.0 if self.rng.random() < 0.5 else self.rng.uniform(0.5, 1.0)
        self._group_left -= 1
        br = self._phrase_bratio if "B" in self._group and "A" in self._group else 1.0
        return self._group, br

    # ---------------------------------------------------------------- force
    def force(self, f_knob: float, sigma_rel: float, new_phrase: bool) -> float:
        if not self.enabled or sigma_rel <= 0:
            return f_knob
        if new_phrase or self._phrase_force is None:
            v = self.rng.gauss(f_knob, sigma_rel * f_knob)
            self._phrase_force = min(L.F_NAIL_MAX, max(0.20, v))
        return self._phrase_force

    # ---------------------------------------------------------------- MIX phrases
    def mix_mode(self, dt_elapsed: float) -> tuple[str, bool]:
        """Returns (mode, new_phrase).  Phrase length 5-20 s, weights per SPEC §8.4."""
        self._phrase_left -= dt_elapsed
        if self._phrase_mode is None or self._phrase_left <= 0:
            names, w = zip(*MIX_WEIGHTS)
            self._phrase_mode = self.rng.choices(names, weights=w)[0]
            self._phrase_left = self.rng.uniform(5.0, 20.0)
            return self._phrase_mode, True
        return self._phrase_mode, False
