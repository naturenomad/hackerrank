
##############################################################
#### MINIMUM DISTANCES #######################################

# https://www.hackerrank.com/challenges/minimum-distances

# The distance between two array values is the number of indices between them. 
# Given a, find the minimum distance between any pair of equal elements in the array. 
# If no such value exists, return -1.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    minDist = -1
    
    # Iterate through unique values only :
    for val in set(a):
        
        # isolate just the key-value list pairs we want :
        if a.count(val) > 1 :
            positions = [i for i,j in enumerate(a) if j==val]
            
            # Iterate through the positions list of these same values
            # and do a distance comparison with all remaining positions in the list
            # to obtain the minimum value :
            for k,v in enumerate(positions[:-1]):
                for x,y in enumerate(positions[k+1:]):
                    if minDist == -1 or abs(v-y) < minDist :
                        minDist = abs(v-y)
    return minDist


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    n = int(input().strip())
    
    a = list(map(int, input().rstrip().split()))
    
    result = minimumDistances(a)
    
    fptr.write(str(result) + '\n')
    
    fptr.close()


# Test cases :
a = [3,2,1,2,3]
minimumDistances(a)
#2

a = [7,1,3,4,1,7]
minimumDistances(a)
#3
