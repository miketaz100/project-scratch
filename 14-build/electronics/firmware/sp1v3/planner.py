"""Mode -> token stream.  Every token is checked (checker.assert_ok) before it is returned.

The planner owns the block's position between tokens (always at rest on the rim), the
heading psi, the precession sign and the group/force state.  It never returns a token the
checker rejects: a rejected candidate is replaced by a rim park and counted; the scorer
faults after 3 rejections in a row (a planner bug must not become motion).
"""
from __future__ import annotations

import math
from dataclasses import dataclass, field

from . import checker
from . import limits as L
from . import paths
from .variation import Variation


@dataclass
class Settings:
    mode: str = "pline"            # pline | line | circle | mix  (+ internal chord, dpath)
    f: float = 1.4
    f_circle: float = 1.2
    amp: float = 16.0
    dpsi: float = 4.5
    dpsi_jit: float = 1.5
    psi: float = 0.0               # LINE / D-path with-grain heading (deg)
    R: float = 11.5
    e: float = 3.5
    prec: float = 25.0
    chord: bool = True
    force: float = 0.30            # N per nail (INTENSITY knob)
    sF: float = 0.15
    groups: str = "auto"           # a | b | ab | auto
    bratio: float = 1.0
    palm: float | str = "auto"
    vary: bool = True
    seed: int = 1
    dwell: float = 90.0
    stage_b: bool = True           # INTENSITY band 0.20-0.45 N until D1
    float_spring: float = L.FLOAT_SPRING_N

    def as_dict(self):
        return dict(self.__dict__)


@dataclass
class PlannerState:
    pos: tuple = (0.0, -L.R_PARK)  # block parked on the rim
    psi: float = 0.0
    prec_sign: int = 1
    half: int = 0                  # half-stroke counter (PLINE alternates direction)
    t_session: float = 0.0
    groups: str = ""
    rejections: int = 0
    contact_s: float = 0.0
    strokes: int = 0
    ramp_left: int = 0             # APPROACH: strokes left in the force ramp
    dpath_left: int = 0
    phrase_mode: str = "pline"
    log: list = field(default_factory=list)


class Planner:
    def __init__(self, settings: Settings | None = None):
        self.s = settings or Settings()
        self.st = PlannerState()
        self.var = Variation(self.s.seed, self.s.vary)

    # ----------------------------------------------------------- force bookkeeping
    def force_setting(self, f_nail: float, groups: str, bratio: float) -> dict:
        """Rail/palm for a per-nail force; clamps the force so constant support holds at palm <= 20 kPa."""
        if self.s.stage_b:
            f_nail = min(max(f_nail, 0.20), 0.45)
        f_nail = L.clamp("force", f_nail)
        n = (3 if "A" in groups else 0) + (3 * bratio if "B" in groups else 0)
        if n > 0:
            f_cap = (L.float_net(L.PALM_MAX_KPA, self.s.float_spring) - L.SKID_FLOOR_N) / n
            f_nail = min(f_nail, f_cap - 1e-6)
        rail = L.clamp("rail", L.rail_for_force(f_nail))
        if self.s.palm == "auto":
            palm = L.palm_for_support(rail, groups, bratio, self.s.float_spring) + 0.5
            palm = min(max(palm, 8.0), L.PALM_MAX_KPA)
        else:
            palm = L.clamp("palm", float(self.s.palm))
        return {"rail": rail, "groups": groups, "bratio": bratio, "palm": palm,
                "float_spring": self.s.float_spring, "f_nail": f_nail}

    # ----------------------------------------------------------- helpers
    def _finish(self, tok, force, events=()):
        tok.force = force
        tok.contact = True
        tok.events = list(events)
        try:
            checker.assert_ok(tok)
        except checker.PathRejected as ex:
            self.st.rejections += 1
            self.st.log.append(("F", "checker", str(ex)))
            return None
        self.st.rejections = 0
        return tok

    def _connector(self, p_to, force):
        c = paths.connect(self.st.pos, p_to)
        if c is None:
            return []
        c = self._finish(c, force)
        return [c] if c else None

    def _contact_time(self, tok):
        tsum = 0.0
        s = tok.samples
        for i in range(1, len(s)):
            if math.hypot(s[i][1], s[i][2]) < L.R_LAND_OUTER:
                tsum += s[i][0] - s[i - 1][0]
        return tsum

    def park_token(self, duration, force=None):
        p = self.st.pos
        r = math.hypot(*p)
        if r < L.R_NO_REVERSAL:          # never park inside: go to the rim first
            p = (p[0] / max(r, 1e-9) * L.R_PARK, p[1] / max(r, 1e-9) * L.R_PARK)
        tok = paths.park(p, duration)
        tok.force = force
        tok.contact = force is not None
        return tok

    # ----------------------------------------------------------- the main entry
    def next_tokens(self, approach_force: float | None = None) -> list:
        """Plan the next phrase element (connector + stroke(s) [+ pause]).  Returns checked tokens."""
        s, st = self.s, self.st
        mode = s.mode
        new_phrase = False
        if mode == "mix":
            mode, new_phrase = self.var.mix_mode(0.0 if st.strokes == 0 else self._last_dur)
            st.phrase_mode = mode
        groups, bratio = self.var.groups(s.groups == "auto",
                                         {"a": "A", "b": "B", "ab": "AB"}.get(s.groups, "AB"))
        if s.groups != "auto":
            bratio = L.clamp("bratio", s.bratio) if "B" in groups and "A" in groups else 1.0
        f_target = self.var.force(s.force, s.sF, new_phrase or st.strokes % 8 == 0)
        if st.ramp_left > 0:             # APPROACH: first strokes at 0.10 N ramping to target
            k = 3 - st.ramp_left
            f_target = (approach_force or 0.10) + (f_target - (approach_force or 0.10)) * k / 3.0
            st.ramp_left -= 1
        force = self.force_setting(f_target, groups, bratio)
        events = []
        if groups != st.groups:
            events.append((0.0, "groups", groups))
            events.append((0.0, "bratio", bratio))
        out = []
        draw = self.var.stroke(s.chord and mode in ("pline", "chord", "mix"), s.f, st.t_session)
        if draw.pause_s > 0:
            pk = self.park_token(draw.pause_s, force)
            out.append(pk)
            if draw.flip_precession:
                st.prec_sign *= -1

        if mode in ("pline", "line", "chord"):
            toks = self._line_stroke(mode, draw, force, events)
        elif mode == "circle":
            toks = self._circle(force, events)
        elif mode == "dpath":
            toks = self._dpath(force, events)
        else:
            raise ValueError(mode)
        if not toks:
            # rejected: park 0.5 s instead; the scorer faults after 3 in a row
            out = [self.park_token(0.5, force)]
        else:
            out += toks
            st.groups = groups
        for t in out:
            st.t_session += t.duration
            st.contact_s += self._contact_time(t)
        st.strokes += 1
        self._last_dur = sum(t.duration for t in out)
        return out

    _last_dur = 0.0

    def _line_stroke(self, mode, draw, force, events):
        s, st = self.s, self.st
        f = L.clamp("f", s.f)
        amp = L.clamp("amp", s.amp)
        if mode == "pline":
            jit = self.var.rng.uniform(-s.dpsi_jit, s.dpsi_jit) if s.vary else 0.0
            st.psi += st.prec_sign * (L.clamp("dpsi", s.dpsi) / 2.0) + jit / 2.0 + draw.kick_deg
        elif mode == "line":
            st.psi = L.clamp("psi", s.psi)
        else:  # chord phrase: heading precesses slowly, every stroke offset
            st.psi += st.prec_sign * 2.25 + draw.kick_deg
        e = draw.e
        if mode == "chord" and abs(e) < 1e-9:
            e = self.var.rng.uniform(2.0, 9.0) * self.var.rng.choice((-1, 1))
        e = math.copysign(min(abs(e), L.clamp("chord_e", 9.0), math.sqrt(amp * amp - 1.0) - 0.1), e or 1.0) if e else 0.0
        # keep v_c <= 195 mm/s: v_c = (2 s_c + 4 D_r) / T_h
        s_end = math.sqrt(amp * amp - e * e)
        s_c = math.sqrt(L.R_LAND_OUTER ** 2 - e * e)
        T_h_min = (2 * s_c + 4 * (s_end - s_c)) / 195.0
        ps = max(draw.period_scale, T_h_min * 2.0 * f)
        cands = [paths.line(st.psi, amp=amp, e=e, f=f, reverse=rv, period_scale=ps) for rv in (False, True)]
        tok = min(cands, key=lambda t: math.hypot(t.start[0] - st.pos[0], t.start[1] - st.pos[1]))
        out = self._connector(tok.start, force)
        tok = self._finish(tok, force, events)
        if tok is None or out is None:
            return []
        out.append(tok)
        st.pos = tok.end
        return out

    def _circle(self, force, events):
        s, st = self.s, self.st
        R = L.clamp("R", s.R)
        e = L.clamp("e", s.e)
        e = max(e, R - L.CIRCLE_RME_MAX, L.CIRCLE_RPE_MIN - R)      # feasible offset
        e = min(e, L.D_MAX - R)                                       # stay inside the rim top
        f = L.clamp("f_circle", s.f_circle)
        prec = L.clamp("prec", s.prec)
        phi0 = math.degrees(math.atan2(st.pos[1], st.pos[0]))      # far point where the block waits
        tok = paths.circle(R=R, e=e, phi0_deg=phi0, prec_deg=prec, f=f, revs=2,
                           direction=st.prec_sign)
        out = self._connector(tok.start, force)
        tok = self._finish(tok, force, events)
        if tok is None or out is None:
            return []
        out.append(tok)
        st.pos = tok.end
        return out

    def _dpath(self, force, events):
        s, st = self.s, self.st
        amp = L.clamp("amp", s.amp)
        stroke, ret = paths.dpath(L.clamp("psi", s.psi), amp=amp, f=L.clamp("f", s.f),
                                  side=self.var.rng.choice((-1, 1)))
        out = self._connector(stroke.start, force)
        a = self._finish(stroke, force, events)
        b = self._finish(ret, force)
        if a is None or b is None or out is None:
            return []
        out += [a, b]
        st.pos = b.end
        return out

    # ----------------------------------------------------------- non-play moves
    def to_rim(self, angle_deg=-90.0):
        """Retracted move from the current position to the rim park (pins vented)."""
        return self.to_point((L.R_PARK * math.cos(math.radians(angle_deg)),
                              L.R_PARK * math.sin(math.radians(angle_deg))))

    def to_point(self, p_to):
        """Retracted straight move at <= 40 mm/s (pad retracted, pins vented; used for ARMING,
        RETRACT and the index check only - never for play)."""
        x0, y0 = self.st.pos
        n = max(2, int(math.hypot(p_to[0] - x0, p_to[1] - y0) / 0.25))
        T = max(0.3, math.hypot(p_to[0] - x0, p_to[1] - y0) / 40.0)
        samples = []
        for k in range(n + 1):
            u = 0.5 - 0.5 * math.cos(math.pi * k / n)
            samples.append((T * k / n, x0 + (p_to[0] - x0) * u, y0 + (p_to[1] - y0) * u))
        tok = paths.Token("retracted", samples, contact=False)
        self.st.pos = p_to
        return tok
