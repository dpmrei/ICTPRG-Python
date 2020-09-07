

import random

dict1 = {'heads': 0, 'tails': 0}

count = 0

flips = input("press 'f' to flip ('q' to stop)")

while flips == 'f':
    
    for i in range (10):
        toss = random.randint(1,2)
    
        if toss == 1:
            side = 'heads'
            dict1['heads']+=1
        else:
            side = 'tails'
            dict1['tails']+=1
    
        print (side)
        flips = input("press 'f' to flip ('q' to stop)")
        if flips == 'q':
            break

        count = count + 1

    print (dict1)
    print (count)