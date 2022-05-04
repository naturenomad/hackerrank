
##########################################################
#### CAPITALIZE ##########################################

# https://www.hackerrank.com/challenges/capitalize

# Ensure that the first and last names of people begin with a capital letter


#!/bin/python3

import math
import os
import random
import re
import sys


def solve(s):
    # Note need to explicitly state the seperator so that any
    # other seperations are preserved, eg double-space etc.
    slist = s.split(' ')
    for key,value in enumerate(slist): 
        slist[key]=value.capitalize()
    return ' '.join(slist)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()


# Test cases :

solve('hello world')
# 'Hello World'

solve('hello   world  bah')
# 'Hello   World  bah'

