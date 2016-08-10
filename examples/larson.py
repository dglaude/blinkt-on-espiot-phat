import math
import time

from blinkt import set_pixel, show, set_brightness

reds = [0, 0, 0, 0, 0, 16, 64, 255, 64, 16, 0, 0, 0, 0, 0, 0]

start_time = time.ticks_ms()

while True:
    delta = time.ticks_ms() - start_time

    # Triangle wave, a snappy ping-pong effect
    offset = int(abs((delta % 16) - 8))

    for i in range(8):
        set_pixel(i , reds[offset + i], 0, 0)
    show()

    time.sleep(0.1)

