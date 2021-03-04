# BUBBLE SORT

# Given an array of integers, sort the array in ascending order using the Bubble Sort algorithm. 
# Once sorted, print the following three lines:

# Array is sorted in numSwaps swaps., where numSwaps is the number of swaps that took place.
# First Element: firstElement, where firstElement is the first element in the sorted array.
# Last Element: lastElement, where lastElement is the last element in the sorted array.

# To complete this challenge, you must add a variable that keeps a running tally of all swaps that occur during execution. 


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    swaps = 0
    for i in range(len(a)) :
        for j in range(len(a)-1) :
            # Swap adjacent elements if they are in decreasing order
            if a[j] > a[j+1] :
                a[j], a[j+1] = a[j+1], a[j]
                swaps += 1
    print('Array is sorted in {} swaps.'.format(swaps))
    print('First Element: {}'.format(a[0]))
    print('Last Element: {}'.format(a[len(a)-1]))


# Calling internally
countSwaps([3,2,1]) # Expect 3 swaps
countSwaps([1,2,3]) # Expect 0 swaps
countSwaps([6,4,1]) # Expect 3 swaps


# Calling externally 
if __name__ == '__main__':
    n = int(input())
    
    a = list(map(int, input().rstrip().split()))
    
    countSwaps(a)
