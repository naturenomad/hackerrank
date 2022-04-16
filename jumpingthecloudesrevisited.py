
##############################################################################
#### JUMPING ON THE CLOUDS REVISITED #########################################

# https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited

# A child is playing a cloud hopping game. In this game, there are sequentially numbered clouds that can be thunderheads or cumulus clouds. The character must jump from cloud to cloud until it reaches the start again. 

# Energy level e starts at 100
# Cumulus cloud = 0
# Thundercloud = 1
# Energy used per jump = 1
# Energy used if lands on a thundercloud = 2
# The game ends when the character lands back on cloud 0.

# jumpingOnClouds() has the following parameter(s):

#    int c[n]: the cloud types along the path
#    int k: the length of one jump

# Returns

#    int: the energy level remaining.


#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import cycle

def jumpingOnClouds(c, k):
    # Variables :
    d = {} # dictionary to hold key-value pairs for cloud list c
    e = 100 # starting energy level
    
    # Make clouds to a dictionary to store the keys of the clouds as well :
    for key,value in enumerate(c): 
        d[key]=value  
    
    # Iterate through these in a cycle :
    iterator = cycle(d)
    # Get to starting position :
    i = next(iterator)
    
    # Now jumping :
    while True:
        i = jump(k, iterator)

        # Deduct energy :
        e -= 1
        if d[i] == 1:
            e -= 2

        # Break if back at start :
        if i == 0:
            break
    return e

# Function to iterate by the correct step size, returns the iterator new position :    
def jump(k, iterator):
    for _ in range(k):
        i = next(iterator)
    return i

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()


# Some tests :

jumpingOnClouds([0, 0, 1, 0, 0, 1, 1, 0], 2)
# Expect 92

jumpingOnClouds([0,0,1,0],2)
# Expect 96

