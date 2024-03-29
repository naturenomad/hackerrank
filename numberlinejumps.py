
# https://www.hackerrank.com/challenges/kangaroo/problem

# NUMBER LINE JUMPS

# Given two kangaroos on a number line ready to jump in the positive direction.

# The first kangaroo starts at location x1 and moves at a rate of v1 meters per jump.
# The second kangaroo starts at location x2 and moves at a rate of v2 meters per jump.

# Get both kangaroos at the same location at the same time as part of the show. If it is possible, return YES, otherwise return NO. 

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.

def kangaroo(x1, v1, x2, v2):
    if (x2 > x1 and v2 > v1) or (x1 > x2 and v1 > v2):
        return "NO"
    elif (v2 - v1) != 0:
        if (x1 - x2) % (v2 - v1) == 0:
            return "YES"
        else:
            return "NO"
    else:
        if (x1 - x2) == 0:
            return "YES"
        else:
            return "NO"

# Calling internally
print(kangaroo(0, 3, 4, 2))
# Yes

print(kangaroo(0, 2, 5, 3))
# No

# Calling externally
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    x1V1X2V2 = input().split()
    x1 = int(x1V1X2V2[0])
    v1 = int(x1V1X2V2[1])
    x2 = int(x1V1X2V2[2])
    v2 = int(x1V1X2V2[3])
    result = kangaroo(x1, v1, x2, v2)
    fptr.write(result + '\n')
    fptr.close()
