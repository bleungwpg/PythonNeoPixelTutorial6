messageID = 1

myStart = 0

countToMaxLength = 0

durationCounter = 0

mask1 = [[10,10,17,10,17,10,17,17,17,10,10,17,10,10,10,10],
         [10,10,17,10,17,10,17,10,10,10,17,10,17,10,10,10],
         [10,10,17,10,17,10,17,10,10,10,17,10,17,10,10,10],
         [10,10,17,10,17,10,17,10,10,10,17,10,17,10,10,10],
         [10,10,17,10,17,10,17,17,17,10,17,17,17,10,10,10],
         [10,10,17,10,17,10,10,10,17,10,17,10,17,10,10,10],
         [10,10,17,10,17,10,10,10,17,10,17,10,17,10,10,10],
         [10,10,10,17,10,10,17,17,17,10,17,10,17,10,10,10]]




message2 = [[10,10,12,10,12,10,12,12,12,10,12,10,10,10,10,12,12,10,10,12,10,10,12,10,12,10,12,12,12,10,10,10,10,10,10],
            [10,10,12,10,12,10,12,10,10,10,12,10,10,10,12,10,10,10,12,10,12,10,12,12,12,10,12,10,10,10,10,10,10,10,10],
            [10,10,12,10,12,10,12,10,10,10,12,10,10,10,12,10,10,10,12,10,12,10,12,10,12,10,12,10,10,10,10,10,10,10,10],
            [10,10,12,10,12,10,12,12,10,10,12,10,10,10,12,10,10,10,12,10,12,10,12,10,12,10,12,12,10,10,10,10,10,10,10],
            [10,10,12,10,12,10,12,12,10,10,12,10,10,10,12,10,10,10,12,10,12,10,12,10,12,10,12,12,10,10,10,10,10,10,10],
            [10,10,12,10,12,10,12,10,10,10,12,10,10,10,12,10,10,10,12,10,12,10,12,10,12,10,12,10,10,10,10,10,10,10,10],
            [10,10,12,12,12,10,12,10,10,10,12,10,10,10,12,10,10,10,12,10,12,10,12,10,12,10,12,10,10,10,10,10,10,10,10],
            [10,10,12,10,12,10,12,12,12,10,12,12,12,10,10,12,12,10,10,12,10,10,12,10,12,10,12,12,12,10,10,10,10,10,10]]


message3 = [[12,12,14,12,12,12,12,12,12,12,12,12,12,12,12,12],
            [12,12,12,14,12,12,12,12,12,12,12,12,12,12,12,12],
            [12,12,12,12,14,12,12,12,12,12,12,12,12,12,12,12],
            [12,12,12,12,12,14,12,12,12,12,12,12,12,12,12,12],
            [12,12,12,12,12,12,14,12,12,12,12,12,12,12,12,12],
            [12,12,12,12,12,12,12,14,12,12,12,12,12,12,12,12],
            [12,12,12,12,12,12,12,12,14,12,12,12,12,12,12,12],
            [12,12,12,12,12,12,12,12,12,14,12,12,12,12,12,12],
            [12,12,12,12,12,12,12,12,12,12,14,12,12,12,12,12],
            [12,12,12,12,12,12,12,12,12,12,12,14,12,12,12,12],
            [12,12,12,12,12,12,12,12,12,12,12,12,14,12,12,12],
            [12,12,12,12,12,12,12,12,12,12,12,12,12,14,12,12],
            [12,12,12,12,12,12,12,12,12,12,12,12,12,12,14,12],
            [12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,14],
            [12,12,12,12,12,12,12,12,12,12,12,12,12,12,14,12],
            [12,12,12,12,12,12,12,12,12,12,12,12,12,14,12,12],
            [12,12,12,12,12,12,12,12,12,12,12,12,14,12,12,12],
            [12,12,12,12,12,12,12,12,12,12,12,14,12,12,12,12],
            [12,12,12,12,12,12,12,12,12,12,14,12,12,12,12,12],
            [12,12,12,12,12,12,12,12,12,14,12,12,12,12,12,12],
            [12,12,12,12,12,12,12,12,14,12,12,12,12,12,12,12],
            [12,12,12,12,12,12,12,14,12,12,12,12,12,12,12,12],
            [12,12,12,12,12,12,14,12,12,12,12,12,12,12,12,12],
            [12,12,12,12,12,14,12,12,12,12,12,12,12,12,12,12],
            [12,12,12,12,14,12,12,12,12,12,12,12,12,12,12,12],
            [12,12,12,14,12,12,12,12,12,12,12,12,12,12,12,12]]


message4 = [[11,11,15,11,11,11,11,11,11,11,11,11,11,11,11,11],
            [11,11,15,11,11,11,11,11,11,11,11,11,11,11,11,11],
            [12,12,12,12,15,12,12,12,12,12,12,15,12,12,12,12],
            [12,12,12,15,15,12,12,12,12,12,12,15,12,12,12,12],
            [11,11,11,15,11,11,15,11,11,11,11,15,11,11,11,11],
            [11,11,11,15,11,11,11,11,11,15,11,15,11,11,11,11],
            [13,13,13,13,13,13,13,13,13,15,13,13,13,13,13,13],
            [13,13,13,13,13,13,13,13,13,15,13,13,13,13,13,13],
            [11,11,11,11,11,11,11,11,11,11,11,11,11,15,11,11],
            [11,11,11,11,11,11,11,15,11,11,11,15,11,11,11,11],
            [11,11,15,11,11,11,11,15,11,11,11,15,11,15,11,11],
            [11,11,15,11,11,11,15,11,11,11,11,11,11,15,11,11],
            [11,11,15,11,11,11,11,11,11,11,11,11,15,11,11,11],
            [14,14,15,14,14,15,14,15,14,14,14,14,15,14,14,15],
            [14,14,14,14,14,14,14,14,14,14,14,14,15,14,15,15],
            [14,14,14,14,14,15,14,14,14,14,14,14,14,14,14,15],
            [11,11,11,11,11,15,11,11,11,11,11,11,11,11,15,11],
            [11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,15],
            [11,11,11,11,11,11,15,11,11,11,15,11,11,11,11,11],
            [11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11],
            [11,11,11,11,15,11,15,11,15,11,11,11,15,11,11,11],
            [11,11,11,11,15,11,15,11,11,11,11,11,15,11,11,11],
            [11,11,11,11,15,11,15,11,15,11,11,11,15,11,11,11],
            [11,11,11,11,11,11,11,11,15,11,11,11,11,11,11,11],
            [11,11,11,15,11,11,11,11,11,11,11,11,11,11,11,11],
            [11,11,15,15,11,11,11,11,11,11,11,11,11,11,11,11]]