
##########################################################
#### CUT THE STICKS ######################################

# https://www.hackerrank.com/challenges/cut-the-sticks

# You are given a number of sticks of varying lengths. 
# You will iteratively cut the sticks into smaller sticks, 
# discarding the shortest pieces until there are none left. 

# At each iteration, determine the length of the shortest stick remaining, 
# cut that length from each of the longer sticks 
# and then discard all the pieces of that shortest length. 
# When all the remaining sticks are the same length, they cannot be shortened 
# so discard them.

# Given the lengths of n sticks, print the number of sticks that are left 
# before each iteration until there are none left.


# Function Description

# cutTheSticks has the following parameter(s):
#    int arr[n]: the lengths of each stick

# Returns
#    int[]: the number of sticks after each iteration


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    sticks = []
    sticks.append(len(arr))
    
    # At each iteration 
    # (finishing when all remaining sticks are same length) : 
    while len(set(arr))>1 :
        
        # determine the length of the shortest stick remaining
        smallest = min(arr) 

        # Cut that length from each of the longer sticks.
        # The issue with the enumerate() and pop() approach is that it 
        # mutates the list while iterating over it.
        # Use list comprehension :
        arr = [(i - smallest) for i in arr]
        
        # Then discard all the pieces of that shortest length.
        arr = [i for i in arr if i > 0]

        sticks.append(len(arr))
        
    return sticks


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


# Test cases

cutTheSticks([1,2,3])
# Expect
# 3
# 2
# 1

cutTheSticks([5,4,4,2,2,8])
# 6
# 4
# 2
# 1

cutTheSticks([1,2,3,4,3,3,2,1])
# 8
# 6
# 4
# 1
