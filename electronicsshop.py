
# https://www.hackerrank.com/challenges/electronics-shop/problem

# ELECTRONICS SHOP

# A person wants to determine the most expensive computer keyboard and USB drive 
# that can be purchased with a given budget. 
# Given price lists for keyboards and USB drives and a budget, find the cost to buy them. 
# If it is not possible to buy both items, return -1


#!/bin/python3

import os
import sys

# This version does not pass all the tests, but the test-sets are too large to explore by hand
def getMoneySpent(keyboards, drives, b):
    spend = [i+j for i in keyboards for j in drives if i+j<b]
    if len(spend) > 0:
        return max(spend)
    else:
        return -1


# Alternative
def getMoneySpent(keyboards, drives, b):
    maxspend = -1
    keyboards.sort()
    drives.sort()
    for i in keyboards:
        for j in drives:
            val = i+j
            if val <=b and val > maxspend:
                maxspend = val
    return maxspend


# Calling internally
getMoneySpent([3,1],[5,2,8],10)
#9
getMoneySpent([4],[5],5)
#-1
getMoneySpent([40,50,60],[5,8,12],60)
#58


# Calling externally
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    bnm = input().split()
    b = int(bnm[0])
    n = int(bnm[1])
    m = int(bnm[2])
    keyboards = list(map(int, input().rstrip().split()))
    drives = list(map(int, input().rstrip().split()))
    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #
    moneySpent = getMoneySpent(keyboards, drives, b)
    fptr.write(str(moneySpent) + '\n')
    fptr.close()
