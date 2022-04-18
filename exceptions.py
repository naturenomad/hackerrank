
##########################################################
#### EXCEPTIONS ##########################################

# https://www.hackerrank.com/challenges/exceptions

# Examples:

# ZeroDivisionError
# This error is raised when the second argument of a division or modulo operation is zero.

# ValueError
# This error is raised when a built-in operation or function receives an argument that has 
# the right type but an inappropriate value.

# >>> a = '1'
# >>> b = '#'
# >>> print int(a) / int(b)
# >>> ValueError: invalid literal for int() with base 10: '#'


# Output Format

# Print the value of a/b.
# In the case of ZeroDivisionError or ValueError, print the error code.

# For integer division in Python 3 use //. 


def integerDivision(): 
    # Adding some extra handling for invalid count input :
    try:
        # Hackerrank doesn't like the instructions added
        #n = int(input("Enter number of divisions to do:"))
        n = int(input())
    except:
        print("Not a valid integer")
    
    for i in range(n):
        try:
            # Hackerrank doesn't like the instructions added
            #xy = input("Division pair {}: ".format(i+1)).split()
            xy = input().split()
            
            x = int(xy[0])
            y = int(xy[1])
            print(x // y)
        except ZeroDivisionError as e:
            print("Error Code: integer division or modulo by zero")
        except ValueError as e:
            print("Error Code: {}".format(e))   


# Test case :
integerDivision()
3
1 0
2 $
3 1

# Expect :
# Error Code: integer division or modulo by zero
# Error Code: invalid literal for int() with base 10: '$'
# 3

# Note could use BaseError to catch all exceptions in the same manner as ValueError above.
