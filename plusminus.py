# PLUS MINUS

# Count +ves, -ves and zeros in an array as a proportion to 6dp

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    pos = 0
    neg = 0
    neither = 0
    for i in arr:
        if i < 0 :
            neg += 1
        elif i > 0 :
            pos += 1
        else :
            neither +=1
    print('{:.6f}'.format(pos/len(arr)))
    print('{:.6f}'.format(neg/len(arr)))
    print('{:.6f}'.format(neither/len(arr)))

# arr = [1,1,0,-1,-1]
# plusMinus(arr)


if __name__ == '__main__':
    n = int(input())
    
    arr = list(map(int, input().rstrip().split()))
    
    plusMinus(arr)


