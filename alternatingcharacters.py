# ALTERNATING CHARACTERS

# Given a string containing characters A and B
# Task is to change it into a string such that there are no matching adjacent characters. 
# Can delete zero or more characters in the string.

# Find the minimum number of required deletions.


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    deletes = 0
    for i in range(len(s)-1):
        if s[i+1] == s[i]:
            deletes += 1
    return deletes


# Calling internally
alternatingCharacters('AAAA')
#3
alternatingCharacters('BBBBB')
#4
alternatingCharacters('ABABABAB')
#0
alternatingCharacters('BABABA')
#0
alternatingCharacters('AAABBB')
#4

# Calling externally 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    q = int(input())
    
    for q_itr in range(q):
        s = input()
        
        result = alternatingCharacters(s)
        
        fptr.write(str(result) + '\n')
    
    fptr.close()
