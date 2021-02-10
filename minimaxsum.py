# MINI-MAX SUM

# Sum first 4 and last 4 entries in array

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    sumMin = 0
    sumMax = 0
    for i in range(4):
        sumMin += arr[i]
    for i in range(len(arr)-4, len(arr)):
        sumMax += arr[i]
    print(sumMin, sumMax)

#miniMaxSum([3,2,1,4,5])

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    
    miniMaxSum(arr)

