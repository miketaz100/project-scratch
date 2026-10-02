"""
scadpy.py - one source, two outputs (PROJECT SCRATCH / 14-build/halo/cad / 2026-10-02)

Every printed HALO part is written ONCE in halo_parts.py with the functions below.
Each call builds
  (a) a manifold3d solid (numbers)  -> STL via trimesh, watertight-checked, and
  (b) OpenSCAD source text in which every dimension is an EXPRESSION of the
      names in halo_params.scad      -> the .scad files Michael can open, edit and render.
So the SCAD files and the STLs cannot drift apart.

Numbers: class E carries (value, scad_text).  Arithmetic on E builds both.
Only OpenSCAD primitives are emitted: cube, cylinder, sphere, polygon,
linear_extrude, rotate_extrude, translate, rotate, mirror, union, difference,
intersection, hull.  Rotation and mirror conventions are OpenSCAD's
(rotate([x,y,z]) = about X, then Y, then Z, degrees), which manifold3d shares.
"""
import math, re
import numpy as np
from manifold3d import Manifold, CrossSection

FN = 48


# ----------------------------------------------------------------- expressions
def _fmt(x):
    if isinstance(x, E):
        return x.s
    if isinstance(x, bool):
        return "true" if x else "false"
    if isinstance(x, int):
        return str(x)
    if isinstance(x, float):
        if abs(x - round(x)) < 1e-9:
            return str(int(round(x)))
        return ("%.6f" % x).rstrip("0").rstrip(".")
    if isinstance(x, (list, tuple)):
        return "[" + ", ".join(_fmt(v) for v in x) + "]"
    raise TypeError(type(x))


def V(x):
    """numeric value of a number / E / vector"""
    if isinstance(x, E):
        return x.v
    if isinstance(x, (list, tuple)):
        return [V(i) for i in x]
    return float(x)


class E:
    __slots__ = ("v", "s", "atom")

    def __init__(self, v, s, atom=False):
        self.v = float(v)
        self.s = s
        self.atom = atom

    def _p(self):
        return self.s if self.atom else "(" + self.s + ")"

    @staticmethod
    def _w(o):
        if isinstance(o, E):
            return o
        return E(o, _fmt(float(o)), True)

    def __add__(self, o):
        o = E._w(o)
        return E(self.v + o.v, self.s + " + " + o.s)

    def __radd__(self, o):
        return E._w(o).__add__(self)

    def __sub__(self, o):
        o = E._w(o)
        return E(self.v - o.v, self.s + " - " + o._p())

    def __rsub__(self, o):
        return E._w(o).__sub__(self)

    def __mul__(self, o):
        o = E._w(o)
        return E(self.v * o.v, self._p() + " * " + o._p())

    def __rmul__(self, o):
        return E._w(o).__mul__(self)

    def __truediv__(self, o):
        o = E._w(o)
        return E(self.v / o.v, self._p() + " / " + o._p())

    def __rtruediv__(self, o):
        return E._w(o).__truediv__(self)

    def __neg__(self):
        return E(-self.v, "-" + self._p())

    def __float__(self):
        return self.v

    # comparisons use the numbers (python-side decisions are baked)
    def __lt__(self, o): return self.v < V(o)
    def __gt__(self, o): return self.v > V(o)
    def __le__(self, o): return self.v <= V(o)
    def __ge__(self, o): return self.v >= V(o)

    def __repr__(self):
        return "E(%.4f, %s)" % (self.v, self.s)


def _fn1(name, f):
    def g(x):
        if isinstance(x, E):
            return E(f(x.v), "%s(%s)" % (name, x.s), True)
        return f(float(x))
    return g


sin = _fn1("sin", lambda a: math.sin(math.radians(a)))
cos = _fn1("cos", lambda a: math.cos(math.radians(a)))
tan = _fn1("tan", lambda a: math.tan(math.radians(a)))
asin = _fn1("asin", lambda x: math.degrees(math.asin(x)))
acos = _fn1("acos", lambda x: math.degrees(math.acos(max(-1.0, min(1.0, x)))))
sqrt = _fn1("sqrt", math.sqrt)


def atan2(y, x):
    if isinstance(y, E) or isinstance(x, E):
        y, x = E._w(y), E._w(x)
        return E(math.degrees(math.atan2(y.v, x.v)), "atan2(%s, %s)" % (y.s, x.s), True)
    return math.degrees(math.atan2(y, x))


# ----------------------------------------------------------------- params
_PY_FUNCS = {
    "sin": lambda a: math.sin(math.radians(a)), "cos": lambda a: math.cos(math.radians(a)),
    "tan": lambda a: math.tan(math.radians(a)), "asin": lambda x: math.degrees(math.asin(x)),
    "acos": lambda x: math.degrees(math.acos(x)), "atan2": lambda y, x: math.degrees(math.atan2(y, x)),
    "sqrt": math.sqrt, "ceil": math.ceil, "floor": math.floor, "max": max, "min": min, "abs": abs,
}


def load_params(path, overrides=None):
    """Parse 'NAME = expr;' lines of halo_params.scad.  Returns {name: E(value, name)}."""
    vals = {}
    order = []
    for raw in open(path):
        line = raw.split("//")[0]
        for stmt in line.split(";"):
            m = re.match(r"\s*([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.+?)\s*$", stmt)
            if not m:
                continue
            name, expr = m.group(1), m.group(2)
            if overrides and name in overrides:
                v = overrides[name]
            else:
                v = eval(expr, {"__builtins__": {}}, dict(_PY_FUNCS, **vals))
            vals[name] = v
            order.append(name)
    return {k: E(vals[k], k, True) for k in order}, vals


# ----------------------------------------------------------------- solids
class S:
    """solid = manifold + scad text"""
    __slots__ = ("m", "s")

    def __init__(self, m, s):
        self.m = m
        self.s = s


def _ind(t):
    return "\n".join("    " + l for l in t.split("\n"))


def cube(size, center=False):
    sz = V(size)
    return S(Manifold.cube(sz, center), "cube(%s, center = %s);" % (_fmt(size), _fmt(center)))


def cylinder(h, r=None, r1=None, r2=None, center=False, fn=None):
    fn = fn or FN
    if r is not None:
        r1 = r2 = r
    m = Manifold.cylinder(V(h), V(r1), V(r2), fn, center)
    if r is not None:
        txt = "cylinder(h = %s, r = %s, center = %s, $fn = %d);" % (_fmt(h), _fmt(r), _fmt(center), fn)
    else:
        txt = "cylinder(h = %s, r1 = %s, r2 = %s, center = %s, $fn = %d);" % (_fmt(h), _fmt(r1), _fmt(r2), _fmt(center), fn)
    return S(m, txt)


def sphere(r, fn=None):
    fn = fn or 24
    return S(Manifold.sphere(V(r), fn), "sphere(r = %s, $fn = %d);" % (_fmt(r), fn))


def _kids(objs):
    out = []
    for o in objs:
        if o is None:
            continue
        if isinstance(o, (list, tuple)):
            out += _kids(o)
        else:
            out.append(o)
    return out


def translate(v, *objs):
    k = _kids(objs)
    u = union(*k)
    return S(u.m.translate(V(v)), "translate(%s) {\n%s\n}" % (_fmt(v), _ind(u.s if len(k) != 1 else k[0].s)))


def rotate(v, *objs):
    k = _kids(objs)
    u = union(*k)
    return S(u.m.rotate(V(v)), "rotate(%s) {\n%s\n}" % (_fmt(v), _ind(u.s if len(k) != 1 else k[0].s)))


def mirror(v, *objs):
    k = _kids(objs)
    u = union(*k)
    return S(u.m.mirror(V(v)), "mirror(%s) {\n%s\n}" % (_fmt(v), _ind(u.s if len(k) != 1 else k[0].s)))


def union(*objs):
    k = _kids(objs)
    if len(k) == 1:
        return k[0]
    m = k[0].m
    for o in k[1:]:
        m = m + o.m
    return S(m, "union() {\n%s\n}" % _ind("\n".join(o.s for o in k)))


def difference(a, *objs):
    k = _kids(objs)
    m = a.m
    for o in k:
        m = m - o.m
    return S(m, "difference() {\n%s\n}" % _ind("\n".join([a.s] + [o.s for o in k])))


def intersection(*objs):
    k = _kids(objs)
    m = k[0].m
    for o in k[1:]:
        m = m ^ o.m
    return S(m, "intersection() {\n%s\n}" % _ind("\n".join(o.s for o in k)))


def hull(*objs):
    k = _kids(objs)
    m = Manifold.batch_hull([o.m for o in k])
    return S(m, "hull() {\n%s\n}" % _ind("\n".join(o.s for o in k)))


def linear_extrude(h, pts, center=False):
    cs = CrossSection([[tuple(V(p)) for p in pts]], CrossSection.FillRule.EvenOdd) if hasattr(CrossSection, "FillRule") else CrossSection([[tuple(V(p)) for p in pts]])
    m = cs.extrude(V(h))
    if center:
        m = m.translate([0, 0, -V(h) / 2])
    return S(m, "linear_extrude(height = %s, center = %s) polygon(%s);" % (_fmt(h), _fmt(center), _fmt(pts)))


def rotate_extrude(pts, angle=360, fn=None):
    fn = fn or FN
    cs = CrossSection([[tuple(V(p)) for p in pts]])
    a = V(angle)
    seg = max(3, int(round(fn * a / 360.0)))
    m = cs.revolve(seg, a)
    return S(m, "rotate_extrude(angle = %s, $fn = %d) polygon(%s);" % (_fmt(angle), fn, _fmt(pts)))


# ----------------------------------------------------------------- helpers (all built from primitives)
def norm3(v):
    vv = V(v)
    return math.sqrt(sum(x * x for x in vv))


def cyl_between(p0, p1, r, fn=None, r1=None):
    """cylinder from point p0 to p1 (radius r, or r at p0 and r1 at p1).
    Emitted as translate(p0) rotate([0, acos(dz/L), atan2(dy, dx)]) cylinder(h = L ...)."""
    d = [p1[i] - p0[i] for i in range(3)]
    L = sqrt(d[0] * d[0] + d[1] * d[1] + d[2] * d[2]) if any(isinstance(x, E) for x in d) else math.sqrt(sum(V(x) ** 2 for x in d))
    ay = acos(d[2] / L)
    az = atan2(d[1], d[0])
    if r1 is None:
        c = cylinder(L, r=r, fn=fn)
    else:
        c = cylinder(L, r1=r, r2=r1, fn=fn)
    return translate(p0, rotate([0, ay, az], c))


def box(x0, x1, y0, y1, z0, z1):
    return translate([x0, y0, z0], cube([x1 - x0, y1 - y0, z1 - z0]))


def to_trimesh(sol):
    import trimesh
    mesh = sol.m.to_mesh()
    v = np.asarray(mesh.vert_properties)[:, :3]
    f = np.asarray(mesh.tri_verts)
    return trimesh.Trimesh(vertices=v, faces=f, process=True)
