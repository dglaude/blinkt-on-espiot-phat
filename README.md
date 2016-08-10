# blinkt-on-espiot-phat
Port of Blinkt! library for microPython on ESP8266

The Blinkt! library https://github.com/pimoroni/blinkt is build to permit to write Python program that drive 8 APA102 RGB LEDs. This is a port of the API for microPython on ESP8266.

Using the script of https://github.com/pimoroni/espiot-phat it is possible to flash https://github.com/micropython/micropython firmware of the ESP IoT pHAT of @Pimoroni.
Notice that this require a a Raspberry Pi and microSD card.

Lattest version of microPython contain support for APA102, blinkt.py is a thin layer to try to reuse Blinkt! example without a Rasberry Pi, only with the Blinkt! and the ESP IoT pHAT.

Power and console access to the ESP IoT pHAT can be done from a host (PC/MAC/Linux) using a terminal emulator and a USB-to-UART Serial Console Cable https://shop.pimoroni.com/products/usb-to-uart-serial-console-cable

Bill of Material:
- Blinkt! https://shop.pimoroni.com/products/blinkt
- ESP8266 pHAT (aka ESP IoT pHAT) https://shop.pimoroni.com/products/esp8266-phat
- USB to UART serial console cable https://shop.pimoroni.com/products/usb-to-uart-serial-console-cable

Despite compatible API, many example from Blinkt! library https://github.com/pimoroni/blinkt/tree/master/examples do not work out of the box or might never work due to limitation and missing library on microPython:
- cpu_load.py and mem_load.py using psutil can not work (and do not make a lot of sense on an ESP8266)
- pulse.py using numpy can not work out of the box but could be replaced by precomputed table
- cheerlights.py using requests would need to be modified to work
- ...

Other problems
- time.time() on ESP8266 only provide second accuracy, could be replaced by time.ticks_ms()
- colorsys is missing but a port of colorsys.hsv_to_rgb can be found here: https://gist.github.com/dries007/26a2f36770c28500b912b0ecf1276129
- ...
