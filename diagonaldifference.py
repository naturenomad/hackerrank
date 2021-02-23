# DIAGONAL DIFFERENCE
# Given a square matrix, calculate the absolute difference between the sums of its diagonals. 

#!/bin/python3

import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    sumLR = 0
    sumRL = 0
    size = len(arr)
    for i in range(size):
        sumLR += arr[i][i]
    for j in range(size):
        sumRL += arr[j][size-1-j]
    
    return(abs(sumLR-sumRL))

# Calling internally - example -
#arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
#print(diagonalDifference(arr))

# Calling externally -
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    n = int(input().strip())
    
    arr = []
    
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    
    result = diagonalDifference(arr)
    
    fptr.write(str(result) + '\n')
    
    fptr.close()

