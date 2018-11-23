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



def showMessage(nextMessage,duration,myMessage):
    # start - fixed message 4 
    # remember to change globalvariables.message#
    i = 0
    for r in range(0,8):
        for c in range(0,8):
            color = myMessage[r][c]
            lookupColor(color,i)
            i += 1
    for r in range(0,8):
        for c in range(8,16):
            color = myMessage[r][c]
            lookupColor(color,i)
            i += 1
    strip.write()
    time.sleep(duration)

    # switch to next message
    globalvariables.messageID = nextMessage



while True:
    if globalvariables.messageID == 1:
        # showMessage(nextMessage,messageDuration,message)
        showMessage(2,1,globalvariables.message1)


    elif globalvariables.messageID == 2:
        # shortcut for message 2
        showMessage(3,2,globalvariables.message2)


    elif globalvariables.messageID == 3:
        # shortcut for message 3
        showMessage(4,1,globalvariables.message3)


    elif globalvariables.messageID == 4:
        # shortcut for message 4
        showMessage(5,2,globalvariables.message4)


    elif globalvariables.messageID == 5:
        # shortcut for message 5
        showMessage(1,5,globalvariables.message1)
