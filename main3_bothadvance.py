# Y9 Demo
# CircuitPython demo - NeoPixel 16 x 8 pixels
# demonstrates all lights on the board works
 
import time
import board
import neopixel
 
pixpin = board.D0
numpix = 128

start1 = 0
start2 = 64

end1 = 64
end2 = 128

count1 = start1
count2 = start2

count3 = 0



strip = neopixel.NeoPixel(pixpin, numpix, brightness=0.1, auto_write=False)

 
while True:
    # clear all lights to black
    for r in range(0,128):
      strip[r] = (0,0,0)


    temp = count2 + 7 - (count3)

    # turn the current light to red
    strip[count1] = (255,0,0)
    strip[temp] = (0,255,0)

    strip.write()
    time.sleep(0.1)


    # increase i by 1, thereby moving the light to the next value
    count1 += 1
    count2 += 1
    count3 += 2

    # reset i back to 0 if it reaches the maximum value
    if count1 == end1:
      count1 = start1

    if count2 == end2:
      count2 = start2

    if count3 == 16:
      count3 = 0