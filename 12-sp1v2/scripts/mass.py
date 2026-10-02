# RT2-corrected mass model, calibrated: single 12-pin = 397 g, twin 12-pin = 575 g (RT2 §7)
H=0.62      # head-side harness length, m (RT2 0.55-0.7)
U=0.175     # umbilical head-borne share, m (0.35 m loop /2)
g_pin_tube=4.7; g_light=2.4; g_syn=9.2; g_syn_light=4.7
cart=2.3; block=1.0
def single(N, light=False, al=True, fixes=True):
    base=397 - 12*(cart+block+H*g_pin_tube+U*g_pin_tube)   # non-pin part
    m=base + N*(cart+block+H*(g_light if light else g_pin_tube)+U*g_pin_tube)
    if light: m -= 3*H*(g_syn-g_syn_light)
    if al: m+=18            # RT3 Al bail 10x1 (+13..23)
    if fixes: m+=10+0.6*N   # QEV+float relief 6, head-present 3, twin-ready stops/filters ~1; per pin muffler 0.3 + longer cartridge 0.3
    return m
def twin(N, light=False, al=True, fixes=True, ladder=False):
    s=single(N,light,al,fixes)
    nonpin=178-12*(cart+block+H*g_pin_tube+0.3)   # RT2 twin add minus per-pin part = second-pad non-pin
    add=nonpin + N*(cart+block+H*(g_light if light else g_pin_tube)+0.3)
    if light: add -= 3*H*(g_syn-g_syn_light)
    if fixes: add += 12+0.6*N   # pad-B QEV+relief 6, palm-pilot interlock 4, mechanical twin stop 2
    m=s+add
    if ladder: m -= 12+10+5     # spec ladder: Ø16 slaves x2 (-12), thin cradle/band (-10); RT3 defer balancers (-5)
    return m
print("N  single(RT2) single+fix  twin(RT2) twin+fix  twin+fix+light  twin+fix+light+ladder")
for N in (4,6,8,12):
    print(N, round(single(N,al=False,fixes=False)), round(single(N)), round(twin(N,al=False,fixes=False)), round(twin(N)), round(twin(N,light=True)), round(twin(N,light=True,ladder=True)), ' single light', round(single(N,light=True)))
