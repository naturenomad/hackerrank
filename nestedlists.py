
# https://www.hackerrank.com/challenges/nested-list/problem

# NESTED LISTS

# Given the names and grades for each student in a class of students, store them in a nested list and print the 
# name(s) of any student(s) having the second lowest grade.

from operator import itemgetter
from itertools import groupby


def nested(players):
    players.sort(key=itemgetter(1))
    
    grouped = groupby(players, itemgetter(1))
    score=list(grouped)[1][0]
    
    #seconds = list()
    #for i in players:
    #    if i[1] == score:
    #        seconds.append(i[0])
    
    seconds=[i[0] for i in players if i[1] == score]
    
    seconds.sort()
    for i in seconds:
        print(i)


# Calling internally
nested([['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]])
# Expect :
# Berry
# Harry


# Calling externally
if __name__ == '__main__':
    players=list()
    for i in range(int(input())):
        name = input()
        score = float(input())
        players.append([name,score])
        nested(players)
