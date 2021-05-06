
# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem

# JUMPING ON THE CLOUDS

# There is a new mobile game that starts with consecutively numbered clouds. Some of the clouds are thunderheads 
# and others are cumulus. The player can jump on any cumulus cloud having a number that is equal to the number 
# of the current cloud plus 1 or 2.
# The player must avoid the thunderheads. Determine the minimum number of jumps it will take to jump from the 
# starting postion to the last cloud. It is always possible to win the game.
# For each game, you will get an array of clouds numbered 0 if they are safe or 1 if they must be avoided. 

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    pos = 0
    count = 0
    while pos+2 < len(c):
        if c[pos + 2] == 0:
            pos += 2
        else:
            pos += 1
        count += 1
    else:
        if pos+1 < len(c):
            pos += 1
            count += 1
    return(count)

# Calling internally
#jumpingOnClouds([0,0,0,1,0,0]) # Expect 3
#jumpingOnClouds([0,0,1,0,0,1,0]) # Expect 4
#jumpingOnClouds([0,0,0,0,1,0]) # Expect 3
#jumpingOnClouds([0,1,0,0,0,1,0]) # Expect 3

# Calling externally
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    n = int(input())
    
    c = list(map(int, input().rstrip().split()))
    
    result = jumpingOnClouds(c)
    
    fptr.write(str(result) + '\n')
    
    fptr.close()
