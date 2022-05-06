
##########################################################
#### NEW YEAR CHAOS (ARRAYS) #############################

# https://www.hackerrank.com/challenges/new-year-chaos

# It is New Year's Day and people are in line for the Wonderland rollercoaster ride. 
# Each person wears a sticker indicating their initial position in the queue from 1 to n.

# Any person can bribe the person DIRECTLY IN FRONT of them to swap positions, 
# but they still wear their original sticker. One person can bribe at most two others.

# Determine the minimum number of bribes that took place to get to a given queue order. 
# Print the number of bribes, or, if anyone has bribed more than two people, print Too chaotic.


#!/bin/python3

import math
import os
import random
import re
import sys


### Two versions done ###

# Version 1 :

def minimumBribes(q):
    bribes = 0
    positions = []
    persons = []
    
    # Pulling out the current positions and person starting positions into lists,
    # for clarity more than anything,
    # plus vetting for the "Too chaotic" scenario at the same time :
    for position, person in enumerate(q):
        # A briber cannot be more than two places lower than their value :
        if person - (position+1) > 2:
            print("Too chaotic")
            return
        else:
           positions.append(position + 1)
           persons.append(person)
    
    # Now cycle till the lists match :
    while True:
        for position in positions[0:len(positions)-1]:
            if persons[position-1] > persons[position] :
                bribes += 1
                persons[position-1], persons[position] = persons[position], persons[position-1]
        if positions == persons :
            break
    
    print(bribes)


###############

# Version 2 :

def minimumBribes(q):
    bribes = 0
    # Create a seperate list of positions for comparison with list updates :
    positions = list(range(1, len(q)+1))

    # Vetting for the "Too chaotic" scenario :
    for position, person in enumerate(q):
        # A briber cannot be more than two places lower than their value :
        if person - (position+1) > 2:
            print("Too chaotic")
            return

    # Now cycle till the lists match :
    while True:
        # swap any elements where current value is greater than the next value :
        for i,j in enumerate(q):
            # Don't try to swap over the list length :
            if i < len(q)-1:
                if j > q[i+1] :
                    bribes += 1
                    # Swap :
                    q[i], q[i+1] = q[i+1], q[i]
        
        # Break when the list matches the positions :
        if positions == q :
            break

    print(bribes)


# Calling code : 

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)


# Test cases :

q = [5,1,2,3,7,8,6,4]
minimumBribes(q)
# Too chaotic

q=[1,2,5,3,7,8,6,4]
minimumBribes(q)
# 7

q = [1,2,3,5,4,6,7,8]
minimumBribes(q)
# 1

q = [4,1,2,3]
minimumBribes(q)
# Too chaotic

q = [2, 1, 5, 3, 4]
minimumBribes(q)
# 3

q = [2, 5, 1, 3, 4]
minimumBribes(q)
#Too chaotic

