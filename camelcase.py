
##############################################################
#### CAMELCASE ###############################################

# https://www.hackerrank.com/challenges/camelcase

# Return word count from a camelCase string


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'camelcase' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def camelcase(s):
    n=1
    for i in s:
        if i.isupper():
            n+=1
    return n

# ... or ...

def camelcase(s):
    # using list comprehension
    n = [i for i in s if i.isupper()]
    return len(n)+1
    
# ... or ...

def camelcase(s):
    # using regex (probable fastest)
    return len(re.findall("[A-Z]",s)) + 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    s = input()
    
    result = camelcase(s)
    
    fptr.write(str(result) + '\n')
    
    fptr.close()


# Test cases
camelcase("oneTwoThree")
#3

camelcase("saveChangesInTheEditor")
#5
