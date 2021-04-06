# UTOPIAN TREE

# The Utopian Tree goes through 2 cycles of growth every year. 
# Each spring, it doubles in height. 
# Each summer, its height increases by 1 meter.

# A Utopian Tree sapling with a height of 1 meter is planted at the onset of spring. 
# How tall will the tree be after n growth cycles?


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    height = 1
    for i in range(n):
        if i%2 == 0: 
            # Spring
            height *= 2
        else:
            # Summer
            height += 1
    return height

# This problem could also be written with recursion, and perhaps as 2^(((n + (n%2))/2 + 1) - (1 + n%2)

# Calling internally
utopianTree(0)
#1
utopianTree(1)
#2
utopianTree(4)
#7

# Calling externally
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        n = int(input())
        result = utopianTree(n)
        fptr.write(str(result) + '\n')
    fptr.close()
