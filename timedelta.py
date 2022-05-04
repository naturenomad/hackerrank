
##########################################################
#### TIME DELTA ##########################################

# https://www.hackerrank.com/challenges/python-time-delta

# Given two timestamps of one such post that a user can see on his newsfeed in the following format:
# Day dd Mon yyyy hh:mm:ss +xxxx
# Where +xxxx represents the time zone. 
# Task is to print the absolute difference (in seconds) between them. 

# Constraints :
# Input contains only valid timestamps 
# year <= 3000


#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import *


def time_delta(t1, t2):
    # Needs to be absolute to pass all the test cases
    return str(int(abs((datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z") - datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")).total_seconds())))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()


# Test cases :
#2
#Sun 10 May 2015 13:54:36 -0700
#Sun 10 May 2015 13:54:36 -0000
#Sat 02 May 2015 19:54:36 +0530
#Fri 01 May 2015 13:54:36 -0000
# Outputs :
# 25200
# 88200
