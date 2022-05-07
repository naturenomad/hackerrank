
##############################################################
#### SHERLOCK AND THE VALID STRING ###########################

# https://www.hackerrank.com/challenges/sherlock-and-valid-string

# (1) Consider a string to be valid if all characters of the string appear the same number of times. 
# (2) It is also valid if can remove just one character at one index in the string, 
# and the remaining characters will occur the same number of times. 

# Given a string , determine if it is valid. If so, return YES, otherwise return NO.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Get frequency count of all the letters and add to a dictionary :
    dict = {}
    for c in s :
        if c in dict :
            dict[c] += 1
        else :
            dict[c] = 1
    
    # Make a set to find the unique different frequencies :
    counts = set(dict.values())      
    
    # If there is only one frequency, we satisfy validity criterion 1 :
    if len(counts) == 1 :
        return "YES"
        
    # To satisfy criterion 2, total number of frequencies must be 2 : 
    elif len(counts) == 2 : 
        # ...and also the less common frequency must be either 1, 
        # or 1 more than the most common,
        # and must only occur once :
        
        # Getting the commonest frequency :
        
        # First building a frequency dictionary :
        lst = list(dict.values())
        freqdict = {}
        for l in lst :
            if l in freqdict :
                freqdict[l] += 1
            else :
                freqdict[l] = 1
        
        # (Alternatives : [ [l, lst.count(l)] for l in set(lst) ] (slow) or Counter (faster) )
        
        # Then getting the commonest frequency from that :
        k = list(freqdict.keys())
        v = list(freqdict.values())
        mostcommon = k[v.index(max(v))]
        leastcommon = k[v.index(min(v))]
        
        # Finally applying criterion 2 tests :
        if (leastcommon == 1 or leastcommon == (mostcommon + 1)) and v.count(1) == 1 :
            return "YES"
        else:
            return "NO"
    else :
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()


# Test cases :
s = 'abc'
isValid(s)
# YES

s = 'abcc'
isValid(s)
# YES

s = 'abccc'
isValid(s)
# NO

s = 'aabbcd'
isValid(s)
# NO

s = 'aabbccddeefghi'
isValid(s)
# NO

s = 'abcdefghhgfedecba'
isValid(s)
# YES

s = 'aabbccddeefghi'
isValid(s)
# NO
