# BILL DIVISION

#!/bin/python3

import math
import os
import random
import re
import sys


# List index method : 
# This gives a time limit exceeded message
def bonAppetit(bill, k, b):
    sumshared = 0
    for i in bill :
        if bill.index(i) != k:
            sumshared += i
    annadue = sumshared / 2
    if b == annadue :
        print("Bon Appetit")
    else :
        print(int(b-annadue))
        
# List comprehension method :
# Successful :
def bonAppetit(bill, k, b):
    sharedbill = []
    sumshared = 0
    sharedbill = [bill[i] for i in range(len(bill)) if i != k]
    for i in sharedbill :
        sumshared += i
    annadue = sumshared / 2
    if b == annadue :
        print("Bon Appetit")
    else :
        print(int(b-annadue))


# Sample inputs :
bill = [3, 10, 2, 9]
k = 1
b = 7
b = 12

# Calling programme internally
#bonAppetit(bill, k, b)


# Calling programme externally 
#    n: number of items ordered
#    k: an integer representing the zero-based index of the item Anna doesn't eat
#    bill: an array of integers representing the cost of each item ordered
#    b: the amount of money that Anna contributed to the bill

if __name__ == '__main__':
    nk = input().rstrip().split()
    
    n = int(nk[0])
    
    k = int(nk[1])
    
    bill = list(map(int, input().rstrip().split()))
    
    b = int(input().strip())
    
    bonAppetit(bill, k, b)


