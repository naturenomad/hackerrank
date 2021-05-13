
# https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=arrays

# Interview Preparation Challenge

# MINIMUM SWAPS 2

# Find the minimum number of swaps required to sort the array in ascending order. 

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    # First priority : achieve correct positions in minimum swaps
    # Second priority : achieve this in minimum time
    
    swaps = 0
    
    # Create a lookup table of correct positions :
    lookup_arr = sorted(arr)
    
    # Get index, value dict for arr:
    arr_dict = {v: i for i,v in enumerate(arr)}
    
    # Iterate through arr. On first find which is not in correct position,
    #   swap with the element that should be in this position, update its dict as well
    for i,v in enumerate(arr):
        if v != lookup_arr[i]:
            swapindex = arr_dict[lookup_arr[i]]
            arr[swapindex], arr[i] = arr[i], arr[swapindex]
            arr_dict[lookup_arr[i]], arr_dict[v] = i, swapindex
            swaps += 1
    return(swaps)

# Calling internally 
#minimumSwaps([4,3,1,2]) # Expect 3
#minimumSwaps([2,3,4,1,5]) # Expect 3
#minimumSwaps([1,3,5,2,4,6,7]) # Expect 3
#minimumSwaps([7,1,3,2,4,5,6]) # Expect 5

# Calling externally
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    n = int(input())
    
    arr = list(map(int, input().rstrip().split()))
    
    res = minimumSwaps(arr)
    
    fptr.write(str(res) + '\n')
    
    fptr.close()
