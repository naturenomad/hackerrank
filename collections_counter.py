
##########################################################
#### COLLECTIONS.COUNTER() ###############################

# https://www.hackerrank.com/challenges/collections-counter

# A counter is a container that stores elements as dictionary keys, 
# and their counts are stored as dictionary values.

# Task

# Shop has x number of shoes.
# There is a list containing the size of each shoe he has in his shop.
# There are n number of customers who are willing to pay p amount of money 
# only if they get the shoe of their desired size.

# Task is to compute how much money earned.

from collections import Counter

# collect int x number of shoes from input
x = int(input())

# collect list shoe sizes in shop from input
cShoes = Counter(map(int, input().split()))

# collect int n customers from input
n = int(input())

# iteratively collect each list of pairs of customer shoe size and price from input
# Doing this as a list of tuples because dictionaries can't have duplicate keys
# and the customers' shoe/price preferences don't change.
custShoesPrices = []
for i in range(n):
    size, price = map(int, input().split())
    tupCust = (size, price)
    custShoesPrices.append(tupCust)

def moneyEarned(x, cShoes, n, custShoesPrices):
    # Add to total for customers who can buy shoes in their size
    # in the order of customer number.
    # Decrement 1 from cShoes Counter for that size.
    
    total = 0
    for i in custShoesPrices :       
        if i[0] in cShoes.keys():           
            total += i[1]
            cShoes[i[0]] -= 1
            if cShoes[i[0]] == 0:
                del cShoes[i[0]]
            
    print(total)

moneyEarned(x, cShoes, n, custShoesPrices)
