# LIST COMPREHENSIONS

# Given three integers representing the dimensions of a cuboid along with an integer n, print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k is not equal to n.

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

# Traditional method
def makelist(x,y,z,n):
    out=list()
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if i+j+k != n:
                    out.append([i,j,k])
    print(out)


makelist(1,1,1,2)
makelist(2,2,2,2)

# List comprehension method
def makelist(x,y,z,n):
    out = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if ((i+j+k) != n)]
    print(out)

makelist(1,1,1,2)
makelist(2,2,2,2)
