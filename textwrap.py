# https://www.hackerrank.com/challenges/text-wrap/problem

# TEXT WRAP

# Given a string S and width W .
# Task is to wrap the string into a paragraph of width W.

def wrap(string, max_width):
    segments = ''
    segment = ''
    for i in range(0,len(string)):
        if len(segment) == max_width:
            segments+='\n'
            segment = ''
        segment += string[i]
        segments += string[i]
    
    return(segments)

# Call internally
#print(wrap('ABCDEFGHIJKLIMNOQRSTUVWXYZ', 4))

# Call externally
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
