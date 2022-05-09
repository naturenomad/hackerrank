

##############################################################
#### EQUALIZE THE ARRAY ######################################

# https://www.hackerrank.com/challenges/equality-in-a-array

# Given an array of integers, determine the minimum number of elements to delete 
# to leave only elements of equal value.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalizeArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equalizeArray(arr):
    # Get a count of the most common value in the list
    # And then remove this value from the length of the list
    return len(arr) - arr.count(max(set(arr), key=arr.count))


# Calling code :
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    n = int(input().strip())
    
    arr = list(map(int, input().rstrip().split()))
    
    result = equalizeArray(arr)
    
    fptr.write(str(result) + '\n')
    
    fptr.close()


# Test cases :
arr = [1,2,2,3]
equalizeArray(arr)
#2

arr = [3, 3, 2, 1, 3]
equalizeArray(arr)
#2   

arr = [1,2,3,1,2,3,3,3]
equalizeArray(arr)
#4
