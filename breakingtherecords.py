
# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

# BREAKING THE RECORDS

# From array of season's scores, calculate how many times minimum and maximum records are broken,
# taking the first score as the first record :

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    maxmin=[0,0]
    minrecord = scores[0]
    maxrecord = scores[0]
    for i in scores :
        if i > maxrecord :
            maxmin[0] += 1
            maxrecord = i
        elif i < minrecord :
            maxmin[1] += 1
            minrecord = i
    return(maxmin)

# Sample inputs :
#scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]
#scores = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]

# Calling internally
#print(' '.join(map(str, breakingRecords(scores))))

# Calling externally :
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    n = int(input())
    
    scores = list(map(int, input().rstrip().split()))
    
    result = breakingRecords(scores)
    
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    
    fptr.close()
