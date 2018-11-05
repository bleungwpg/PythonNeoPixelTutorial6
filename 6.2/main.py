import globalvariables

import time
import board
import neopixel
 
pixpin = board.A3
numpix = 128


strip = neopixel.NeoPixel(pixpin, numpix, brightness=0.1, auto_write=False)


def lookupColor(color,i):
    # no color
    if color == 10:
        strip[i] = (0,0,0)
    # orange
    elif color == 11:
        strip[i] = (255,179,0)
    # yellow
    elif color == 12:
        strip[i] = (255,255,0)
    # green
    elif color == 13:
        strip[i] = (0,255,0)
    # blue
    elif color == 14:
        strip[i] = (0,0,255)
    # violet
    elif color == 15:
        strip[i] = (62,0,105)
    # pink
    elif color == 16:
        strip[i] = (247,50,255)
    # red
    elif color == 17:
        strip[i] = (255,0,0)



def showMessage1():
    # start - fixed message 1
    # remember to change globalvariables.message#
    i = 0
    for r in range(0,8):
        for c in range(0,8):
            color = globalvariables.message1[r][c]
            lookupColor(color,i)
            i += 1
    for r in range(0,8):
        for c in range(8,16):
            color = globalvariables.message1[r][c]
            lookupColor(color,i)
            i += 1
    strip.write()
    time.sleep(3)
   # end - fixed message 1

    globalvariables.messageID = 2


def showMessage2():
    # start - fixed message 2
    # remember to change globalvariables.message#
    i = 0
    for r in range(0,8):
        for c in range(0,8):
            color = globalvariables.message2[r][c]
            lookupColor(color,i)
            i += 1
    for r in range(0,8):
        for c in range(8,16):
            color = globalvariables.message2[r][c]
            lookupColor(color,i)
            i += 1
    strip.write()
    time.sleep(3)
    # end - fixed message 2

    globalvariables.messageID = 3


def showMessage3():
    # start - fixed message 3
    # remember to change globalvariables.message#
    i = 0
    for r in range(0,8):
        for c in range(0,8):
            color = globalvariables.message3[r][c]
            lookupColor(color,i)
            i += 1
    for r in range(0,8):
        for c in range(8,16):
            color = globalvariables.message3[r][c]
            lookupColor(color,i)
            i += 1
    strip.write()
    time.sleep(3)
    # end - fixed message 3

    globalvariables.messageID = 4



def showMessage4():
    # start - fixed message 4 
    # remember to change globalvariables.message#
    i = 0
    for r in range(0,8):
        for c in range(0,8):
            color = globalvariables.message4[r][c]
            lookupColor(color,i)
            i += 1
    for r in range(0,8):
        for c in range(8,16):
            color = globalvariables.message4[r][c]
            lookupColor(color,i)
            i += 1
    strip.write()
    time.sleep(3)
    # end - fixed message 4 

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
