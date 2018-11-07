import globalvariables

import time
import board
import neopixel
 
pixpin = board.A3
numpix = 128


strip = neopixel.NeoPixel(pixpin, numpix, brightness=0.1, auto_write=False)


def lookupColor(color,i):
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
    # red
    elif color == 17:
        strip[i] = (255,0,0)




def showMessage(nextMessage,duration,myMessage,myMaxLength):
    # start - show Message
    i = 0
    for r in range(0,8):
        for c in range(globalvariables.countToMaxLength,globalvariables.countToMaxLength+8):
            temp = c % myMaxLength
            color = myMessage[r][temp]
            lookupColor(color,i)
            i += 1

    for r in range(0,8):
        for c in range(globalvariables.countToMaxLength+8,globalvariables.countToMaxLength+16):
            temp = c % myMaxLength
            color = myMessage[r][temp]
            lookupColor(color,i)
            i += 1

    strip.write()

    globalvariables.countToMaxLength += 1
    if globalvariables.countToMaxLength > duration or globalvariables.countToMaxLength > myMaxLength:
        globalvariables.countToMaxLength = 0
        globalvariables.messageID = nextMessage





while True:
    if globalvariables.messageID == 1:
        # Call function - showMessage(nextMessageID, messageDuration, message, maxLengthOfAdvertisement)
        showMessage(2,12,globalvariables.message1,globalvariables.maxLengthOfAdvertisement1)


    elif globalvariables.messageID == 2:
        # Call function - showMessage(nextMessageID, messageDuration, message, maxLengthOfAdvertisement)
        showMessage(3,10,globalvariables.message2,globalvariables.maxLengthOfAdvertisement2)


    elif globalvariables.messageID == 3:
        # Call function - showMessage(nextMessageID, messageDuration, message, maxLengthOfAdvertisement)
        showMessage(4,5,globalvariables.message3,globalvariables.maxLengthOfAdvertisement3)


    elif globalvariables.messageID == 4:
        # Call function - showMessage(nextMessageID, messageDuration, message, maxLengthOfAdvertisement)
        showMessage(1,5,globalvariables.message4,globalvariables.maxLengthOfAdvertisement4)




