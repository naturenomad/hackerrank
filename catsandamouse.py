##############################################################################
#### CATS AND A MOUSE ########################################################

# https://www.hackerrank.com/challenges/cats-and-a-mouse/

# Two cats and a mouse are at various positions on a line. You will be given their starting positions. Your task is to determine which cat will reach the mouse first, assuming the mouse does not move and the cats travel at equal speed. 

# If the cats arrive at the same time, the mouse will be allowed to move and it will escape while they fight. 
# Given queries in the form of x, y, and z representing the respective positions for cats A and B, and for mouse C.
# Complete the function catAndMouse to return the appropriate answer to each query, which will be printed on a new line.

# If cat A catches the mouse first, print "Cat A".
# If cat B catches the mouse first, print "Cat B."
# If both cats reach the mouse at the same time, print "Mouse C" as the two cats fight and mouse escapes. 

#!/bin/python3

import math
import os
import random
import re
import sys

def catAndMouse(x,y,z):
    if (abs(x-z) < abs(y-z)):
        return "Cat A"
    elif (abs(x-z) > abs(y-z)):
        return "Cat B"
    elif (abs(x-z) == abs (y-z)):
        return "Mouse C"
    else:
        return "Error"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
    
# Test cases :

#catAndMouse(1,1,3)
# Mouse C
#catAndMouse(1,1,1)
# Mouse C
#catAndMouse(2,5,4)
# Cat B
#catAndMouse(1,2,3)
# Cat B
#catAndMouse(1,3,2)
# Mouse C
