
# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=arrays

# Interview Preparation Challenge

# ARRAYS - LEFT ROTATION

# A left rotation operation on an array shifts each of the array's elements unit to the left. 
# Note that the lowest index item moves to the highest index in a rotation. This is called a circular array. 

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    for i in range(d):
        a.append(a.pop(0))
    return(a)

# Calling internally
#rotLeft([1,2,3,4,5], 4) # Expect [5,1,2,3,4]
#rotLeft([1,2,3,4,5], 2) # Expect [3,4,5,1,2]

# Calling externally 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    nd = input().split()
    
    n = int(nd[0])
    
    d = int(nd[1])
    
    a = list(map(int, input().rstrip().split()))
    
    result = rotLeft(a, d)
    
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    
    fptr.close()
