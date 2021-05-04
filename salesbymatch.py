
# https://www.hackerrank.com/challenges/sock-merchant/problem

# SALES BY MATCH

# There is a large pile of socks that must be paired by color. 
# Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    sockcounts = list()
    for i in ar :
        if not sockcounts:
            sockcounts.append([i, ar.count(i)])
        elif i not in [j[0] for j in sockcounts]:
            sockcounts.append([i, ar.count(i)])
    
    pairs = 0
    for i in sockcounts:
        if i[1] > 1:
            pairs += int(i[1]/2)
    
    return(pairs)

# Calling code for within python :
#sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20])

# Calling code when calling programme externally :
if __name__ == '__main__':
    
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # Need to set OUTPUT_PATH environment variable
    # Eg. export OUTPUT_PATH="home/ca/Desktop/output.txt"
    
    fptr = sys.stdout
    
    n = int(input())
    
    ar = list(map(int, input().rstrip().split()))
    
    result = sockMerchant(n, ar)
    
    fptr.write(str(result) + '\n')
    
    fptr.close()
