# Leap-4 C: part-by-part mass ledger (extends mass.py, RT2-calibrated) + skyhook moment model.
# Run: python3 mass_leap4c.py
import math
H=0.62; U=0.175; g_pin_tube=4.7; g_light=2.4; g_syn=9.2; g_syn_light=4.7
cart=2.3; block=1.0; N=6

def baseline_single(light):
    gp = g_light if light else g_pin_tube
    gs = g_syn_light if light else g_syn
    L = {
     'front half-band':20, 'forehead pad + sleeve':10, 'dial cradle':30, 'temple pads x2':6,
     'doff handle / visor guard':8,
     'hub pods x2 (bearings, capstan, drum, balancer, parietal pads)':36,
     'hub servos STS3032 x2':41,
     'bail (Al 10x1 bent, nodes, splice, tendon guide)':58,
     'carriage':10, 'radial float + rods + spring':12,
     'pad non-pin (deck, 3 slaves, cranks, RCC, skids)':40.4, 'pins 6 x 3.3':N*(cart+block),
     'must-fix hw (QEV+relief 6, head switch 3, stops/filters 1, mufflers 0.6/pin)':10+0.6*N,
     'tendon, idlers, balancer parts':6,
     'head-side harness 0.62 m (6 pin + palm + 3 synchro)':H*(N*gp+g_pin_tube+3*gs),
     'umbilical head share 0.175 m':U*(N*g_pin_tube)+10.1,
     'plug / strain relief / clips':9.1,
     'fasteners, wiring, misc':10, 'twin provisions':4,
    }
    return L

def tot(L): return sum(L.values())

def twin_add_baseline(light, ladder):
    # mass.py twin add (RT2 178 g calibrated), itemised; reconciliation row closes to mass.py
    gp = g_light if light else g_pin_tube; gs = g_syn_light if light else g_syn
    A = {'alpha_R servo':21, 'carriage B':10, 'float B':12, 'pad B non-pin':40.4, 'pad B pins':N*(cart+block),
         'harness B 0.62 m':H*(N*gp+g_pin_tube+3*gs), 'tendon crossed loop':4, 'tee manifold, umbilical, misc':6,
         'splice off, dummy cartridge out':-6, 'pad-B fixes (QEV, interlock, twin stop, mufflers)':12+0.6*N+0.6*N,
         'per-pin umbilical share':0.3*N}
    target = (178-12*(cart+block+H*g_pin_tube+0.3)) + N*(cart+block+H*(gp)+0.3)
    if light: target -= 3*H*(g_syn-g_syn_light)
    target += 12+0.6*N
    A['RT2 model reconciliation'] = target - tot(A)
    if ladder:
        A['ladder: Ø16 slaves x2']=-12; A['ladder: thin cradle/band']=-10; A['ladder: defer balancers']=-5
    return A

# ---------------- Leap deltas (single) ----------------
HOUS=30.0   # g/m, Bowden housing incl. two Dyneema strands [VERIFY 15-42 g/m; Nissen 4 mm ~42 g/m]
def leaps_single(light_base=True):
    gp = g_light; gs = g_syn_light
    D = {}
    # C1 SKYHOOK: bundle drops from an overhead constant-force line straight to the carriage
    harness = H*(N*(g_light if light_base else g_pin_tube)+g_pin_tube+3*(g_syn_light if light_base else g_syn))
    jumper = 0.12*(N*g_pin_tube+g_pin_tube+3*g_syn)       # 0.12 m carriage->pad jumpers, full 4 mm lines
    D['C1 skyhook: delete head-side harness along bail'] = -harness + jumper
    D['C1 skyhook: plug/strain relief -> carriage clip + breakaway'] = -9.1 + 4
    share_new = 0.05*(N*g_pin_tube+g_pin_tube+3*g_syn) + 1.0   # bottom 50 mm of rising bundle + head-switch wire
    D['C1 skyhook: umbilical head share'] = -(U*(N*g_pin_tube)+10.1) + share_new
    # C2 BOX-DRIVEN TRAVEL: both axes from the right hub, pull-pull Dyneema in common housings
    D['C2 Bowden: delete 2 servos'] = -41
    D['C2 Bowden: delete motor bays/cartridge plates in pods'] = -6
    D['C2 Bowden: delete servo bus wire on head'] = -3
    D['C2 Bowden: housings 2 x (0.175 share + 0.03 route)'] = 2*(0.175+0.03)*HOUS
    D['C2 Bowden: terminations, R30 sectors, hub friction brake'] = 3+2
    # C3 FEATHER CHASSIS
    poly = 0.69*34.1 + 7*1.5 + 0.45*4.8     # 8x6 carbon chords+legs, 7 printed nodes, 3x1 carbon track strip
    D['C3 polygon carbon bail (8x6 chords, printed nodes, bent-strip track)'] = poly - 58
    D['C3 carbon 20x1 front band (was Al 20x1.5)'] = 8 - 20
    D['C3 forehead pad thinner closed-cell'] = -4
    D['C3 doff lip moulded into band node'] = -5
    D['C3 balancer parts deleted (skyhook balances)'] = -3
    return D

def leaps_twin_extra():
    E = {}
    # twin add changes vs baseline twin add (light lines)
    E['C2 third Bowden (alpha_L, routed behind cradle) replaces alpha_R servo'] = -21-3-1.5 + (0.175+0.30)*HOUS + 2.5
    harnessB = H*(N*g_light+g_pin_tube+3*g_syn_light)
    jumper = 0.12*(N*g_pin_tube+g_pin_tube+3*g_syn)
    E['C1 second skyhook line: delete harness B'] = -harnessB + jumper + 4 + 0.05*(N*g_pin_tube+g_pin_tube+3*g_syn)
    return E

if __name__=='__main__':
    for light in (False, True):
        B = baseline_single(light)
        print(f"\nBASELINE single 6-pin, {'light' if light else 'normal'} lines: {tot(B):.1f} g")
    B = baseline_single(True)
    print("\nBaseline single ledger (light lines):")
    for k,v in B.items(): print(f"  {v:6.1f}  {k}")
    print(f"  {tot(B):6.1f}  TOTAL")
    A = twin_add_baseline(True, True)
    print("\nBaseline twin add (light + ladder):")
    for k,v in A.items(): print(f"  {v:6.1f}  {k}")
    print(f"  twin = {tot(B)+tot(A):.1f}")
    D = leaps_single(True)
    print("\nLeap deltas (single, vs light-line baseline):")
    groups={}
    for k,v in D.items():
        print(f"  {v:6.1f}  {k}"); groups[k[:2]]=groups.get(k[:2],0)+v
    for g,v in groups.items(): print(f"  subtotal {g}: {v:.1f}")
    s_new = tot(B)+sum(D.values())
    print(f"NEW single = {s_new:.1f} g  ({100*(s_new/tot(B)-1):.0f} % vs {tot(B):.0f}; {100*(s_new/386.4-1):.0f} % vs 386)")
    E = leaps_twin_extra()
    for k,v in E.items(): print(f"  twin extra {v:6.1f}  {k}")
    A0 = twin_add_baseline(True, False)
    t_new = s_new + tot(A0) + sum(E.values())
    print(f"NEW twin (no ladder) = {t_new:.1f}; with Ø16 slaves = {t_new-12:.1f}  ({100*((t_new-12)/480-1):.0f} % vs 480)")
    # what the margin buys: pins per pad under the new chassis (full 4 mm lines head-side now)
    per_pin_single = cart+block+0.12*g_pin_tube+0.05*g_pin_tube+0.6
    per_pin_twin = 2*per_pin_single
    for n in (6,8,12):
        print(f"  pins/pad {n}: single {s_new+(n-6)*per_pin_single:.0f} g, twin(Ø16) {t_new-12+(n-6)*per_pin_twin:.0f} g")
    # moving group (static load the skyhook carries)
    mg = 40.4+N*(cart+block)+6+0.6*N + 12+10 + 0.12*(N*g_pin_tube+g_pin_tube+3*g_syn)
    print(f"moving group per pad ≈ {mg:.0f} g")
