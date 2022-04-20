
##########################################################
#### ALPHABET RANGOLI ####################################

# https://www.hackerrank.com/challenges/alphabet-rangoli

# Print an alphabet rangoli of size . 
# (Rangoli is a form of Indian folk art based on creation of patterns.)

# Examples :

#size 5

# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------

#size 3

# ----c---- row 2
# --c-b-c-- row 1
# c-b-a-b-c row 0
# --c-b-c-- row -1
# ----c---- row -2

from string import ascii_lowercase

def print_rangoli(size):
    
    # Get list of letters for ease :
    letterlist = ascii_lowercase[0:size]
    
    # Treat row zero as the middle row with all the letters :
    for y in range(size-1, -size, -1):
    
        # need dashes as a function of y :
        dashes = abs(2*y) * '-'
        
        # counting letter list from high to low and back to high again (eg cbabc) :
        letters = letterlist[size-1:abs(y):-1] + letterlist[abs(y):size]
        
        # Add dashes and letters together :
        str = dashes + '-'.join(letters) + dashes
        
        print(str)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)


# Test cases :

print_rangoli(3)
print_rangoli(5)
