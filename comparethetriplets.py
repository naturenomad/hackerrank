
# https://www.hackerrank.com/challenges/compare-the-triplets/problem

# COMPARE THE TRIPLETS

# Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding points on a 
# scale from 1 to 100 for three categories: problem clarity, originality, and difficulty. 
# Return array of [Alice score, Bob score]


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    compare=[0,0]
    for i in range(0,3):
        if a[i]>b[i]:
            compare[0] += 1
        elif b[i]>a[i]:
            compare[1] += 1
        else:
            pass
    return compare

# Calling internally (examples):
#compareTriplets([5,6,7], [3,6,10])
#compareTriplets([17,28,30], [99,6,8])


# Calling externally :
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    a = list(map(int, input().rstrip().split()))
    
    b = list(map(int, input().rstrip().split()))
    
    result = compareTriplets(a, b)
    
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    
    fptr.close()
