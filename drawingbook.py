# DRAWING BOOK

# Book starts page 1 on rhs. Otherwise 2 pages on each page except possibly the last.
# Given n pages long and p the page the student wants to turn to, 
# find and print the minimum number of pages that must be -turned- from start or end to arrive at page p.


#!/bin/python3

import os
import sys

def pageCount(n, p): 
    # Need floor division
    # Floor division is a normal division operation except that it returns the largest possible integer. 
    if n // p >= 2:
        # start from beginning
        if p > 1:
            count = int(p//2)
        else:
            count = 0
    else:
        # start from end
        if p < n:
            count = int(n//2 - p//2)
        else:
            count = 0
    return count


# This could also be solved more simply using min instead of if..else:
# return min(p//2, n//2 - p//2)


# Calling internally
pageCount(5,3)
#1
pageCount(6,2)
#1
pageCount(5,4)
#0
pageCount(2,1)
#0

# Calling externally
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    p = int(input())
    result = pageCount(n, p)
    fptr.write(str(result) + '\n')
    fptr.close()
