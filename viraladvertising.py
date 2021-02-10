# VIRAL ADVERTISING

# Product launched to 5 people on social media. Each day half (floor) like and share it with 3 of their friends.
# Function to return cumulative likes on day n.

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    #initialise parameters for day 1:
    shared = 5
    liked = int(shared/2)
    cumulative = liked
    
    for day in range(1,n):
        shared = liked * 3
        liked = int(shared/2)
        cumulative += liked
    
    return(cumulative)

#Calling internally :
#viralAdvertising(5)
#24
#viralAdvertising(3)
#9


#Calling externally :
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    n = int(input())
    
    result = viralAdvertising(n)
    
    fptr.write(str(result) + '\n')
    
    fptr.close()


