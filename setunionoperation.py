# https://www.hackerrank.com/challenges/py-set-union/problem

# SET .UNION() OPERATION

# Return number of items in common between two sets

# Two ways to do this :
# a.union(b)
# a | b


def getunion(nset, bset):
    print(len(nset | bset))

# Calling internally
getunion({1, 2, 3, 4, 5, 6, 7, 8, 9}, {10, 1, 2, 3, 11, 21, 55, 6, 8})

#Calling externally:
if __name__ == '__main__':
    n=input()
    nset=set(map(int, input().split()))
    b=input()
    bset=set(map(int, input().split()))

    print(len(nset | bset))
