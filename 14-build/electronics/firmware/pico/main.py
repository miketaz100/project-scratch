# SP1 v3 tension front-end — MicroPython for a Raspberry Pi Pico (RP2040).
# Copy to the Pico as main.py (Thonny: File > Save as > Raspberry Pi Pico > main.py).
#
#   GP26 / ADC0  <- Hall flexure A (DRV5053EA output via 1 k + 100 nF)
#   GP27 / ADC1  <- Hall flexure B
#   GP28 / ADC2  <- Hall flexure C
#   3V3(OUT)     -> the three Halls' VCC (ratiometric with the ADC reference) and the LM393 dividers
#   GP15         -> PICO_OK (high = reflexd alive and no trip).  10 k pull-DOWN on the safety board,
#                   so a dead, unplugged or resetting Pico reads as "trip".
#   GP25         -> on-board LED: on = healthy
#
# Protocol (USB serial, 500 frames/s):  "T,<seq>,<a>,<b>,<c>\n"  raw ADC counts 0-65535 (4x averaged)
# From the host:  'H' heartbeat (every 50 ms)    'X' trip (PICO_OK low for 50 ms)
# If no 'H' for 250 ms, PICO_OK stays low until heartbeats return (the latch has already set).
# The RP2040 hardware watchdog resets the Pico if this loop ever stalls (> 300 ms).

import sys
import time
import select
from machine import ADC, Pin, WDT

adc = (ADC(26), ADC(27), ADC(28))
ok = Pin(15, Pin.OUT, value=0)
led = Pin(25, Pin.OUT, value=0)
poll = select.poll()
poll.register(sys.stdin, select.POLLIN)

PERIOD_US = 2000          # 500 frames/s
HB_TIMEOUT_MS = 250
TRIP_MS = 50

time.sleep_ms(500)        # let USB enumerate
wdt = WDT(timeout=300)
last_hb = time.ticks_ms() - 10 * HB_TIMEOUT_MS     # start unhealthy until reflexd talks
trip_until = time.ticks_ms()
seq = 0
nxt = time.ticks_us()

while True:
    a = b = c = 0
    for _ in range(4):
        a += adc[0].read_u16()
        b += adc[1].read_u16()
        c += adc[2].read_u16()
    seq = (seq + 1) & 0xFFFF
    sys.stdout.write("T,%d,%d,%d,%d\n" % (seq, a >> 2, b >> 2, c >> 2))

    now = time.ticks_ms()
    while poll.poll(0):
        ch = sys.stdin.read(1)
        if ch == "H":
            last_hb = now
        elif ch == "X":
            trip_until = time.ticks_add(now, TRIP_MS)

    healthy = (time.ticks_diff(now, last_hb) < HB_TIMEOUT_MS) and (time.ticks_diff(trip_until, now) <= 0)
    ok.value(1 if healthy else 0)
    led.value(1 if healthy else 0)
    wdt.feed()

    nxt = time.ticks_add(nxt, PERIOD_US)
    d = time.ticks_diff(nxt, time.ticks_us())
    if d > 0:
        time.sleep_us(d)
    else:
        nxt = time.ticks_us()
