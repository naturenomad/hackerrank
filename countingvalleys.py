#COUNTING VALLEYS

#Given the sequence of up and down steps during a hike, find and print the number of valleys walked through. 

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    valleys=0
    height=0
    for i in path:
        if i == 'D':
            if height == 0:
                valleys += 1
            height -= 1
        elif i == 'U':
            height += 1
        else:
            print('Error in path')
            return
    return valleys

# Calling programme internally :
# countingValleys(8,'UDDDUDUU')
# countingValleys(8,'DDUUUUDD')
# countingValleys(8,'DUUDDUDU')

# Calling programme externally :
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
