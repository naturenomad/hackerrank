
# https://www.hackerrank.com/challenges/mark-and-toys/problem

# MARK AND TOYS

#  Given a list of toy prices and an amount to spend, determine the maximum number of gifts he can buy.


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    spend = 0
    toys = 0
    prices.sort()
    for i in prices:
        spend += i
        if spend > k:
            break
        toys += 1
    return toys


# Calling internally
# maximumToys([1,2,3,4], 7) # Expect 3
# maximumToys([1,12,5,111,200,1000,10], 50) # Expect 4


# Calling externally 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    nk = input().split()
    
    n = int(nk[0])
    
    k = int(nk[1])
    
    prices = list(map(int, input().rstrip().split()))
    
    result = maximumToys(prices, k)
    
    fptr.write(str(result) + '\n')
    
    fptr.close()
