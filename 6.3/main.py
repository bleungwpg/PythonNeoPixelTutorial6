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



def showMessage(nextMessage,duration,myMessage,myMaxLength,myCountToMax):
    # start - show Message
    i = 0

    for r in range(0,8):
        for c in range(myCountToMax,myCountToMax+8):
            temp = c % globalvariables.maxLengthOfAdvertisement1
            color = myMessage[r][temp]
            lookupColor(color,i)
            i += 1

    for r in range(0,8):
        for c in range(myCountToMax+8,myCountToMax+16):
            temp = c % 
            color = myMessage[r][temp]
            lookupColor(color,i)
            i += 1


    strip.write()
    time.sleep(duration)

    myCountToMax += 1
    if myCountToMax > myMaxLength:
        myCountToMax = 0
        globalvariables.messageID = nextMessage





while True:
    if globalvariables.messageID == 1:
        # shortcut for message 1
        strip.write()
        # showMessage(nextMessage,messageDuration,message,maxLengthOfAdvertisement,countToMax)
        showMessage(2,1,globalvariables.message1,globalvariables.maxLengthOfAdvertisement1,globalvariables.countToMaxLength1)



    elif globalvariables.messageID == 2:
        # shortcut for message 2
        strip.write()
        showMessage(3,2,globalvariables.message2,globalvariables.maxLengthOfAdvertisement2,globalvariables.countToMaxLength2)



    elif globalvariables.messageID == 3:
        # shortcut for message 3
        strip.write()
        showMessage(4,1,globalvariables.message3,globalvariables.maxLengthOfAdvertisement3,globalvariables.countToMaxLength3)


    elif globalvariables.messageID == 4:
        # shortcut for message 4
        strip.write()
        showMessage(1,2,globalvariables.message4,globalvariables.maxLengthOfAdvertisement4,globalvariables.countToMaxLength4)




