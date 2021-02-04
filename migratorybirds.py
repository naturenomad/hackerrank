#MIGRATORY BIRDS

#Given an array of bird sightings where every element represents a bird type id, determine the id of the most 
#frequently sighted type.


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    # Constraints
    if len(arr) < 5 or len(arr) > 20000:
        print('Incorrect array length')
        return False
        
    for i in arr:
        if i not in (1,2,3,4,5):
            print('Incorrect bird type listed')
            return False
    
    # Algorithm :
    birdcounts = list()
    
    for i in arr :
        if not birdcounts :
            birdcounts.append([i, arr.count(i)])
        elif i not in [a[0] for a in birdcounts]:
            birdcounts.append([i,arr.count(i)])
             
    birdcounts.sort(key=lambda x: (-x[1], x[0])) #sort by count descending first, then by birdid increasing second
    
    return birdcounts[0][0]


#Calling internally :
#migratoryBirds([3,4,4,2,4,1,2,2,3,1])
#migratoryBirds([1, 4, 4, 4, 5, 3])
#migratoryBirds([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4])


#Calling externally :
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    arr_count = int(input().strip())
    
    arr = list(map(int, input().rstrip().split()))
    
    result = migratoryBirds(arr)
    
    fptr.write(str(result) + '\n')
    
    fptr.close()
