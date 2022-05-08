

##############################################################
#### SHERLOCK AND ANAGRAMS ###################################

# https://www.hackerrank.com/challenges/sherlock-and-anagrams

# Two strings are anagrams of each other if the letters of one string can be rearranged 
# to form the other string. 
# Given a string, find the number of pairs of substrings of the string that are anagrams 
# of each other. 


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


# Two versions :

# Version 1 using for loops does not satisfy the performance requirements on hackerrank :

def sherlockAndAnagrams(s): 
    
    substrings = [] # to hold all possible substrings
    pairs = 0
    
    # First get all the length options for the anagrams :
    for i in range(len(s)):
 
        # For each length option, get all substrings of s of this length :
        # Cycle through starting positions j, based on length of block :
        for j in range(1,len(s)+1-i):
            substrings.append(s[i:i+j])
    
    # Cycle through list of substrings counting all subsequent anagrams :
    for k,v in enumerate(substrings) :
        for s in substrings[k+1:len(substrings)]:
            if sorted(v) == sorted(s):
                pairs += 1
    return pairs


# Version 2 - replaced a for loop with an if statement :

def sherlockAndAnagrams(s): 
    
    substrings = [] # to hold all possible substrings
    pairs = 0
    
    # First get all the length options for the anagrams :
    for i in range(len(s)):
        
        # Then for each of these length options, get all substrings of s of this length :
        # Cycle through starting positions j, based on length of block :
        for j in range(1,len(s)+1-i):
            
            substrings.append(''.join(sorted(s[i:i+j])))
    
    substrings.sort()
    
    for k,v in enumerate(substrings) :
        if v in substrings[k+1:len(substrings)]:
            pairs += substrings[k+1:len(substrings)].count(v)
    
    return pairs


# Calling code :

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()


# Test cases :

s = 'abba'
sherlockAndAnagrams(s)
#4

s = 'abcd'
sherlockAndAnagrams(s)
#0

s = 'ifailuhkqq'
sherlockAndAnagrams(s)
#3

s = 'kkkk'
sherlockAndAnagrams(s)
#10

s = 'cdcd'
sherlockAndAnagrams(s)
#5
