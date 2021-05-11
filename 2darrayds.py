
# https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=arrays

# Interview Preparation Kit Challenge

# 2D Array - DS

# AKA - HOURGLASS SUM :

# Given a 6x6 2D Array, return an array of the sums of each of the 16 hourglasses represented graphically as follows :
# a b c
#   d
# e f g

import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    sums = []
    for rows in range(4):
        for columns in range(4):
            sum = (arr[rows][columns] + arr[rows][columns+1] + arr[rows][columns+2] + 
                arr[rows+1][columns+1] +
                arr[rows+2][columns] + arr[rows+2][columns+1] + arr[rows+2][columns+2])
            sums.append(sum)
    return(max(sums))

# Generate sample array
#arr = []
#row = [1,2,3,4,5,6]
#for i in range(6):
#    arr.append(row)

# Alternative sample array :
#arr = [[-9,-9,-9,1,1,1],[0,-9,0,4,3,2],[-9,-9,-9,1,2,3],[0,0,8,6,6,0],[0,0,0,-2,0,0],[0,0,1,2,4,0]]

# Calling internally :
hourglassSum(arr)

# Calling externally with array from input :
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    for i in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    result = hourglassSum(arr)
    
    fptr.write(str(result) + '\n')
    
    fptr.close()
