# THE HURDLE RACE

# How many doses of magic potion (height conferred = 1) does hurdler have to take to be able to
# clear all the hurdles?
# k = height hurdler can already jump
# height = array of hurdle heights

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hurdleRace function below.
def hurdleRace(k, height):
    maxheight = max(height)
    return((maxheight - k) if maxheight > k else 0)

# Calling internally :
#print(hurdleRace(4, [1, 6, 3, 5, 2]))
#print(hurdleRace(7, [2, 5, 4, 5, 2]))

# Calling externally :
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    nk = input().split()
    
    n = int(nk[0])
    
    k = int(nk[1])
    
    height = list(map(int, input().rstrip().split()))
    
    result = hurdleRace(k, height)
    
    fptr.write(str(result) + '\n')
    
    fptr.close()
