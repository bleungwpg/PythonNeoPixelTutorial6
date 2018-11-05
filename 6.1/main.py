import globalvariables

import time
import board
import neopixel
 
pixpin = board.A3
numpix = 128


strip = neopixel.NeoPixel(pixpin, numpix, brightness=0.1, auto_write=False)


def showMessage1():
	# reset previous colors
    strip[96] = (0,0,0)
    strip[103] = (0,0,0)

    # show color
    strip[0] = (255,0,0)
    strip[7] = (255,0,0)
    strip.write()
    time.sleep(1)

    # switch to next message
    globalvariables.messageID = 2



def showMessage2():
	# reset previous colors
    strip[0] = (0,0,0)
    strip[7] = (0,0,0)

    # show color
    strip[32] = (0,255,0)
    strip[39] = (0,255,0)
    strip.write()
    time.sleep(1)

    # switch to next message
    globalvariables.messageID = 3


def showMessage3():
	# reset previous colors
    strip[32] = (0,0,0)
    strip[39] = (0,0,0)

    # show color
    strip[64] = (255,50,200)
    strip[71] = (255,50,200)
    strip.write()
    time.sleep(1)

    # switch to next message
    globalvariables.messageID = 4


def showMessage4():
	# reset previous colors
    strip[64] = (0,0,0)
    strip[71] = (0,0,0)

    # show color
    strip[96] = (0,0,255)
    strip[103] = (0,0,255)
    strip.write()
    time.sleep(1)

    # switch to next message
    globalvariables.messageID = 1



while True:
    if globalvariables.messageID == 1:
        strip.write()
        showMessage1()
    elif globalvariables.messageID == 2:
        strip.write()
        showMessage2()
    elif globalvariables.messageID == 3:
        strip.write()
        showMessage3()
    elif globalvariables.messageID == 4:
        strip.write()
        showMessage4()
