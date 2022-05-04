
##########################################################
#### MERGE THE TOOLS #####################################

# https://www.hackerrank.com/challenges/merge-the-tools

# Inputs :

# String s
# Integer k, which is a factor of s

# Task interpretation : Split s into s/k substrings, retaining order, 
# then print the unique characters in each substring on a seperate line, retaining order.


def merge_the_tools(s, k):
    substr = ''
    for i in range(1,(len(s)+1)):
        if s[i-1] not in substr:
            substr += s[i-1]
        if not i%k :
            print(substr)
            substr = ''

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)


# Test cases :

s = 'AAABCADDE'
k = 3
merge_the_tools(s,k)
# 'A'
# 'BCA'
# 'DE'

s = 'AABCAAADA'
k = 3
merge_the_tools(s,k)
# AB
# CA
# AD
