# Y9 Demo
# CircuitPython demo - NeoPixel
# full demo of scrolling letters on both boards
 
import time
import board
import neopixel
 
pixpin = board.D0
numpix = 128


# STUDENTS SHOULD MODIFY THE MAXIMUM VALUE BASED ON THEIR ADVERTISEMENT LENGTH
# 6.1 modify maxlengthofadvertisement to the maximum length of pixels
maxlengthofadvertisement = 24

# this variable is responsible for scrolling all the columns
counttomaxlength = 0

# counter to help remap array (x,y) coordinates into a single value
i = 0

strip = neopixel.NeoPixel(pixpin, numpix, brightness=0.1, auto_write=False)


# STUDENTS SHOULD MODIFY THE ARRAY BELOW
# 6.2 modify the following table of RGB values, add more columns as necessary
allrows = [[[0  ,0  ,0  ],[0  ,0  ,0  ],[255,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[255,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,255,0  ],[0  ,255,0  ],[0  ,255,0  ],[0  ,255,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,255],[0  ,0  ,255],[0  ,0  ,255],[0  ,0  ,255],[0  ,0  ,0  ],[0  ,0  ,0  ]],
           [[0  ,0  ,0  ],[0  ,0  ,0  ],[255,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[255,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,255,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,255],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,255],[0  ,0  ,0  ],[0  ,0  ,0  ]],
           [[0  ,0  ,0  ],[0  ,0  ,0  ],[255,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[255,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,255,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,255],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,255],[0  ,0  ,0  ],[0  ,0  ,0  ]],
           [[0  ,0  ,0  ],[0  ,0  ,0  ],[255,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[255,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,255,0  ],[0  ,255,0  ],[0  ,255,0  ],[0  ,255,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,255],[0  ,0  ,255],[0  ,0  ,255],[0  ,0  ,255],[0  ,0  ,0  ],[0  ,0  ,0  ]],
           [[0  ,0  ,0  ],[0  ,0  ,0  ],[255,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[255,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,255,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,255],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,255],[0  ,0  ,0  ],[0  ,0  ,0  ]],
           [[0  ,0  ,0  ],[0  ,0  ,0  ],[255,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[255,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,255,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,255],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,255],[0  ,0  ,0  ],[0  ,0  ,0  ]],
           [[0  ,0  ,0  ],[0  ,0  ,0  ],[255,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[255,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,255,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,255],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,255],[0  ,0  ,0  ],[0  ,0  ,0  ]],
           [[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[255,0  ,0  ],[255,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,255,0  ],[0  ,255,0  ],[0  ,255,0  ],[0  ,255,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,255],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,255],[0  ,0  ,0  ],[0  ,0  ,0  ]]]



 
 
while True:

    # initialize values values
    strip.brightness = 0.1
    i = 0


    # first loop remaps columns 0 - 7 into the first circuit board 0 - 63
    for r in range(0,8):
        for c in range(counttomaxlength,counttomaxlength+8):
            temp = c % maxlengthofadvertisement
            strip[i] = (allrows[r][temp][0],allrows[r][temp][1],allrows[r][temp][2])
            i += 1

    # second loop remaps columns 8 - 15 into the second circuit board 64 - 127
    # look at the subtle difference in the inner loop for details.
    for r in range(0,8):
        for c in range(counttomaxlength+8,counttomaxlength+16):
            temp = c % maxlengthofadvertisement
            strip[i] = (allrows[r][temp][0],allrows[r][temp][1],allrows[r][temp][2])
            i += 1


    # write data to circuit board
    strip.write()
    time.sleep(0.2)


    # reset advertisement when it reaches it's maximum
    counttomaxlength += 1
    if counttomaxlength > maxlengthofadvertisement:
        counttomaxlength = 0
