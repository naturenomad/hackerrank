
##########################################################
#### FIND DIGITS #########################################

# https://www.hackerrank.com/challenges/find-digits

# An integer d is a divisor of an integer n if the remainder of n/d = 0. 
# Given an integer, for each digit that makes up the integer determine 
# whether it is a divisor. Count the number of divisors occurring within the integer.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def findDigits(n):
    s = str(n)
    count = 0
    for i in s:
        if not int(i) == 0:
          if not (n%int(i)):
              count +=  1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()


# Test cases

findDigits(124)
# Check whether 1, 2 and 4 are divisors of 124. 
# All 3 numbers divide evenly into so return 3. 

findDigits(111)
# Expect 3

findDigits(10)
# Expect 1

findDigits(12)
# Expect 2

findDigits(1012)
# Expect 3
