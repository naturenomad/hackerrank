##############################################################################
#### APPLE AND ORANGE ########################################################

# https://www.hackerrank.com/challenges/apple-and-orange

# Sam's house has an apple tree and an orange tree that yield an abundance of fruit. Using the information given below, 
# determine the number of apples and oranges that land on Sam's house. 

# Function Description

# Complete the countApplesAndOranges function in the editor below. It should print the number of apples and oranges that land 
# on Sam's house, each on a separate line.

# countApplesAndOranges has the following parameter(s):

#    s: integer, starting point of Sam's house location.
#    t: integer, ending location of Sam's house location.
#    a: integer, location of the Apple tree.
#    b: integer, location of the Orange tree.
#    apples: integer array, distances at which each apple falls from the tree.
#    oranges: integer array, distances at which each orange falls from the tree.

# Output Format

# Print two integers on two different lines:

#    The first integer: the number of apples that fall on Sam's house.
#    The second integer: the number of oranges that fall on Sam's house.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    applecount=0
    orangecount=0
    for apple in apples:
        if ((a+apple)>=s) and ((a+apple)<=t):
            applecount += 1
    for orange in oranges:
        if ((b+orange)<=t) and ((b+orange)>=s):
            orangecount += 1
    print(applecount)
    print(orangecount)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)



# Expect:

countApplesAndOranges(7,10,4,12,[2,3,-4],[3,-2,-4])
# 1
# 2

countApplesAndOranges(7,11,5,15,[-2,2,1],[5,-6])
# 1
# 1

