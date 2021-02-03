
#Returns number of times a substring occurs in a string :
def count_substring(string, sub_string):
    counter = 0
    for i in range(0, len(string)):
        if string[i:i+len(sub_string)] == sub_string:
            counter += 1
    return counter

#Below line for calling direct in python :
#count_substring('hellogoodhellohegoodhe', 'he')

#Below for calling externally :
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
