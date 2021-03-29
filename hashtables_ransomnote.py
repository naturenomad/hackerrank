
# HASH TABLES - RANSOM NOTE

# Can a ransom note be recreated from the words in a magazine (Yes/No)?
# The words in the note are case-sensitive and must use only whole words available in the magazine. 

# CA comment. Implemented solution did not explicitly interact with hash tables. Some different solutions proposed below. 
# Solutions 3 and 4 satisfy all the edge cases, but solution 4, using the Counter oject from the Collections library, 
# is the only one which passed HackerRank's performance test.

#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the checkMagazine function below.

# Method 1 : Using sets
def checkMagazine(magazine, note):
    # Split each string into word list
    notewords = set(note.split())
    magazinewords = set(magazine.split())
    if notewords.issubset(magazinewords):
        return "Yes"
    else:
        return "No"
    # The above does not catch the edge case where, say, there is only one of a magazine word, 
    # but the word is needed twice in the note.


# Method 2 : Using list.count() and dictionary.items() methods to catch words and their frequencies
def checkMagazine(magazine, note):
    notedict = dict((word, notelist.count(word)) for word in notelist)
    magdict = dict((word, maglist.count(word)) for word in maglist)
    
    print(notedict)
    print(magdict)
    
    if notedict.items() <= magdict.items():
        print("Yes")
    else:
        print("No")
    # This does not work if the number of instances is less than in magazine


# Method 3 : Using just list.count()
def checkMagazine(magazine, note):
    # Correct for prior strip() done on hackerrank
    if type(note) == str:
        notelist = note.split()
    else:
        notelist = note
    
    if type(magazine) == str:
        maglist = magazine.split()
    else:
        maglist = magazine
    
    success = "Yes"
    for word in notelist:
        if word in maglist:
            if notelist.count(word) > maglist.count(word):
                success = "No"
        else:
            success = "No"
    print(success)
    # This does not pass the hackerrank time limit


# Method 4 : Using collections.Counter (still needs a for loop)

# collections.Counter()
# A counter is a container that stores elements as dictionary keys, 
# and their counts are stored as dictionary values.

# This one finally passes the HackerRank performance requirements, so using Counter is faster than using list.count()

from collections import Counter

def checkMagazine(magazine, note):
    # Correct for prior strip() done on hackerrank
    if type(note) == str:
        notelist = note.split()
    else:
        notelist = note
    
    if type(magazine) == str:
        maglist = magazine.split()
    else:
        maglist = magazine
        
    countnote = Counter(notelist)
    countmag = Counter(maglist)
    
    success = "Yes"
    for key in countnote:
        if key in countmag:
            if countmag[key] < countnote[key]:
                success = "No"
        else:
            success = "No"
    
    print(success)


# Calling internally :

# Example 5
magazine="apgo clm w lxkvg mwz elo bg elo lxkvg elo apgo apgo w elo bg"
note="elo lxkvg bg mwz clm w"
checkMagazine(magazine, note)
# Yes

# Example 3 - edge case of word needed more times than available
magazine="two times three is not four"
note="two times two is four"
checkMagazine(magazine, note)
# No

# Example 1
note="Attack at dawn"
magazine="attack at dawn"
checkMagazine(magazine, note)
# No

# Example 2
magazine="give me one grand today night"
note="give one grand today"
checkMagazine(magazine, note)
# Yes

# Example 4
magazine="ive got a lovely bunch of coconuts"
note="ive got some coconuts"
checkMagazine(magazine, note)
# No

# Calling externally :
if __name__ == '__main__':
    mn = input().split()
    
    m = int(mn[0])
    
    n = int(mn[1])
    
    magazine = input().rstrip().split()
    
    note = input().rstrip().split()
    
    checkMagazine(magazine, note)
