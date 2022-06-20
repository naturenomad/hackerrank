
##############################################################
#### PICKING NUMBERS #########################################

# https://www.hackerrank.com/challenges/picking-numbers

# Given an array of integers, find the longest subarray where the absolute difference 
# between any two elements is less than or equal to 1.


#!/bin/python3

import math
import os
import random
import re
import sys


# The below has not understood the question - it assumes that there is an interval <= 1
# between two consecutive members
def pickingNumbers(a):
    #a.sort()
    maxLength = 0
    length = 0
    for k,v in enumerate(a):
        if k != 0 :
            if abs(v-a[k-1]) <= 1 :
                length += 1
            else :
                print(k,v)
                if length > maxLength :
                    maxLength = length
                    length = 1
    
    return max(length, maxLength)


# Version where we look for the maximum size of array containing two contiguous numbers :

def pickingNumbers(a):
    a.sort()
    maxLength = 0
    
    for k,v in enumerate(a):
        if k < len(a)-1 and abs(a[k+1] - v) <= 1 :
            if a[k+1] != v and (a.count(a[k+1]) + a.count(v)) > maxLength :
                maxLength = a.count(a[k+1]) + a.count(v)
            elif a.count(v) > maxLength :
                maxLength = a.count(v)
    
    return maxLength


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()


# Test cases :

a = [1,1,2,2,4,4,5,5,5]
pickingNumbers(a)
# 5

a = [66,66,66,66,66]
pickingNumbers(a)
# 5

a = [4,6,5,3,3,1]
pickingNumbers(a)
# 3

a = [1,2,2,3,1,2]
pickingNumbers(a)
# 5
