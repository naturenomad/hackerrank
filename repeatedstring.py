# REPEATED STRING

# There is a string, s, of lowercase English letters that is repeated infinitely many times. 
# Given an integer, n, find and print the number of letter a's in the first n letters of the infinite string.

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
# Loops are not optimal enough to pass the performance test
# Need to use integer division // of n times number of a's in string
# ....Plus remainder of n muliplied by number of a's in string
def repeatedString(s, n):    
    # First deal with the whole words
    countAsinword = s.count('a')
    countwholewordsinN = n // len(s)
    countAsinwholewords = countAsinword * countwholewordsinN
    
    # Then deal with any remaining part word
    sizeremainingpartwordinN = n % len(s)
    countAsinremainder = s[:sizeremainingpartwordinN].count('a')
    
    totalAs = countAsinwholewords + countAsinremainder
    return totalAs

# Calling internally
#repeatedString('abcac', 10) # Expect 4
#repeatedString('aba', 10) # Expect 7
#repeatedString('a', 1000000000000) # Expect 1000000000000

# Calling externally
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    s = input()
    
    n = int(input())
    
    result = repeatedString(s, n)
    
    fptr.write(str(result) + '\n')
    
    fptr.close()
