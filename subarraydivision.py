
##############################################################
#### SUBARRAY DIVISION #######################################

# https://www.hackerrank.com/challenges/the-birthday-bar

# Two children want to share a chocolate bar. Each of the squares has an integer on it.
#
# Lily decides to share a contiguous segment of the bar selected such that:
#    The length of the segment matches Ron's birth month, and,
#    The sum of the integers on the squares is equal to his birth day.
#
# Determine how many ways she can divide the chocolate.

# Function inputs :
# s = List of squares of chocolate
# d = birth day
# m = birth month


#!/bin/python3

import math
import os
import random
import re
import sys


def birthday(s, d, m):
    ways = 0
    
    # Iterate through the bar to the beginning of the last section of size m :
    for i in range(0,len(s)+1-m):
        # Test if sum of divided block values equals birthday d
        if sum(s[i:(i+m)]) == d :
            ways += 1
    return ways


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()


# Test cases :

s = [2,2,1,3,2]
d=4
m=2
birthday(s, d, m)
#2

s = [1,2,1,3,2]
d = 3 
m = 2
birthday(s, d, m)
#2

s = [1,1,1,1,1,1]
d = 3 
m = 2
birthday(s, d, m)
#0

s = [4]
d = 4 
m = 1
birthday(s, d, m)
#1
