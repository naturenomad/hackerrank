# MAKING ANAGRAMS

# Two strings are anagrams of each other if the first string's letters can be rearranged to form the second string.
# Both strings must contain the same exact letters in the same exact frequency.

# Find minimum number of character deletions required to make the two strings anagrams.
# Any characters can be deleted from either of the strings. 


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    a = sorted(a.strip())
    b = sorted(b.strip())
    deletes = 0
    adeletes = list()
    bdeletes = list()
    
    # First delete all chars in b that are not in a:
    for i in a:
        if i not in b:
            adeletes.append(i)
            deletes += 1
    
    # Then delete all chars in a that are not in b:
    for j in b:
        if j not in a:
            bdeletes.append(j)
            deletes += 1
    
    # Finally account for duplicate letters:
    # Can't be done with sets, because this would delete the duplicate letters we want
    # Plus sets perform worse than list comprehension
    # Use list comprehension
    a = [i for i in a if i not in adeletes]
    b = [j for j in b if j not in bdeletes]
    for i in set(a):
        deletes += abs(a.count(i) - b.count(i))
    
    return deletes


# Calling internally
makeAnagram('cde', 'abc')
#4
makeAnagram('cde', 'dcf')
#2
makeAnagram('fcrxzwscanmligyxyvym', 'jxwtrhvujlmrpdoqbisbwhmgpmeoke')
#expect 30


# Calling externally
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    a = input()
    
    b = input()
    
    res = makeAnagram(a, b)
    
    fptr.write(str(res) + '\n')
    
    fptr.close()
