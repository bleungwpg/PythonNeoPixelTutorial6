import globalvariables

import time
import board
import neopixel
 
pixpin = board.A3
numpix = 128


strip = neopixel.NeoPixel(pixpin, numpix, brightness=0.1, auto_write=False)


def lookupColor(color,i):
    if color == 0:
        strip[i] = (255,0,0)
    # orange
    elif color == 1:
        strip[i] = (255,179,0)
    # yellow
    elif color == 2:
        strip[i] = (255,255,0)
    # green
    elif color == 3:
        strip[i] = (0,255,0)
    # blue
    elif color == 4:
        strip[i] = (0,0,255)
    # violet
    elif color == 5:
        strip[i] = (62,0,105)
    # pink
    elif color == 7:
        strip[i] = (247,50,255)
    # black
    elif color == 9:
        strip[i] = (0,0,0)



def showMessage1():
    i = 0

    for r in range(0,8):
        for c in range(globalvariables.countToMaxLength1,globalvariables.countToMaxLength1+8):
            temp = c % globalvariables.maxLengthOfAdvertisement1
            color = globalvariables.message1[r][temp]
            lookupColor(color,i)
            i += 1


    for r in range(0,8):
        for c in range(globalvariables.countToMaxLength1+8,globalvariables.countToMaxLength1+16):
            temp = c % globalvariables.maxLengthOfAdvertisement1
            color = globalvariables.message1[r][temp]
            lookupColor(color,i)
            i += 1


    globalvariables.countToMaxLength1 += 1
    if globalvariables.countToMaxLength1 > globalvariables.maxLengthOfAdvertisement1:
        globalvariables.countToMaxLength1 = 0
        globalvariables.messageID = 2


def showMessage2():
    i = 0

    for r in range(0,8):
        for c in range(globalvariables.countToMaxLength2,globalvariables.countToMaxLength2+8):
            temp = c % globalvariables.maxLengthOfAdvertisement2
            color = globalvariables.message2[r][temp]
            lookupColor(color,i)
            i += 1


    for r in range(0,8):
        for c in range(globalvariables.countToMaxLength2+8,globalvariables.countToMaxLength2+16):
            temp = c % globalvariables.maxLengthOfAdvertisement2
            color = globalvariables.message2[r][temp]
            lookupColor(color,i)
            i += 1


    globalvariables.countToMaxLength2 += 1
    if globalvariables.countToMaxLength2 > globalvariables.maxLengthOfAdvertisement2-6:
        globalvariables.countToMaxLength2 = 0
        globalvariables.messageID = 3


def showMessage3():
    i = 0

    for r in range(0,8):
        for c in range(globalvariables.countToMaxLength3,globalvariables.countToMaxLength3+8):
            temp = c % globalvariables.maxLengthOfAdvertisement3
            color = globalvariables.message3[r][temp]
            lookupColor(color,i)
            i += 1


    for r in range(0,8):
        for c in range(globalvariables.countToMaxLength3+8,globalvariables.countToMaxLength3+16):
            temp = c % globalvariables.maxLengthOfAdvertisement3
            color = globalvariables.message3[r][temp]
            lookupColor(color,i)
            i += 1


    globalvariables.countToMaxLength3 += 1
    if globalvariables.countToMaxLength3 > globalvariables.maxLengthOfAdvertisement3-6:
        globalvariables.countToMaxLength3 = 0
        globalvariables.messageID = 4



def showMessage4():
    i = 0

    for r in range(0,8):
        for c in range(globalvariables.countToMaxLength4,globalvariables.countToMaxLength4+8):
            temp = c % globalvariables.maxLengthOfAdvertisement4
            color = globalvariables.message4[r][temp]
            lookupColor(color,i)
            i += 1


    for r in range(0,8):
        for c in range(globalvariables.countToMaxLength4+8,globalvariables.countToMaxLength4+16):
            temp = c % globalvariables.maxLengthOfAdvertisement4
            color = globalvariables.message4[r][temp]
            lookupColor(color,i)
            i += 1


    globalvariables.countToMaxLength4 += 1
    if globalvariables.countToMaxLength4 > globalvariables.maxLengthOfAdvertisement4-6:
        globalvariables.countToMaxLength4 = 0
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
