# Y9 Demo
# CircuitPython demo - NeoPixel 16 x 8 pixels
# demonstrates all lights on the board works
 
import time
import board
import neopixel
 
pixpin = board.D0
numpix = 128

i = 0

strip = neopixel.NeoPixel(pixpin, numpix, brightness=0.1, auto_write=False)

 
while True:
    # clear all lights to black
    for r in range(0,128):
      strip[r] = (0,0,0)

    # turn the current light to red
    strip[i] = (255,0,0)
    strip.write()

    time.sleep(0.1)

    # increase i by 1, thereby moving the light to the next value
    i += 1


    # reset i back to 0 if it reaches the maximum value
    if i == 128:
      i = 0