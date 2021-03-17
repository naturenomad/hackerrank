# This file containts hackerrank challenges which come under the category of itertools problems 

####################################
###### ITERTOOLS.PRODUCT() #########
####################################

# This tool computes the cartesian product of input iterables.
# It is equivalent to nested for-loops.
# For example, product(A, B) returns the same as ((x,y) for x in A for y in B). 

# SAMPLE CODE

from itertools import product

print list(product([1,2,3],repeat = 2))

#[(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]

print list(product([1,2,3],[3,4]))
#[(1, 3), (1, 4), (2, 3), (2, 4), (3, 3), (3, 4)]
 
a = [1, 2]
b = [3, 4]

# PROBLEM TO SOLVE :
# Output the space separated tuples of the cartesian product.

from itertools import product

a=list(map(int, input().split()))
b=list(map(int, input().split()))

results=product(a,b)
print(*results)
