from apa102 import APA102
from machine import Pin 

DAT = 13
CLK = 14
NUM_PIXELS = 8 
BRIGHTNESS = 7 

# set GPIO14 to output to drive the clock
clock = Pin(CLK, Pin.OUT)    
# set GPIO13 to output to drive the data
data = Pin(DAT, Pin.OUT)    
# create APA102 driver on the clock and the data pin for 8 pixels
pixels = APA102(clock, data, NUM_PIXELS)

# set all pixel brightness value without touching the r,g,b
def set_brightness(brightness):
    for x in range(NUM_PIXELS):
        pixels[x] = (pixels[x][0], pixels[x][1], pixels[x][2], int(31.0 * brightness) & 0b11111)

set_brightness(BRIGHTNESS)

# set all pixel to 0,0,0 without touching the brightness
def clear():
    for x in range(NUM_PIXELS):
        pixels[x] = (0, 0, 0, pixels[x][3])

# write data to all pixels
def show():
    pixels.write()

# set a pixel to a r,g,b value or r,g,b,brightness value
def set_pixel(x, r, g, b, brightness=None):
    if brightness is None:
        brightness = pixels[x][3]
    else:
        brightness = int(31.0 * brightness) & 0b11111
    pixels[x] = [int(r) & 0xff, int(g) & 0xff, int(b) & 0xff, brightness]

