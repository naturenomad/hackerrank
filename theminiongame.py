
# https://www.hackerrank.com/challenges/the-minion-game/problem

# THE MINION GAME (Medium, 40 points) :

# Who can make the most substrings out of provided string. Stuart's start with consonent, Kevin's start with vowel.

def minion_game(string):
    kevin = 0
    stuart = 0
    for i in range(len(string)):
        if string[i].lower() in ('aeiou'):
            kevin += len(string) - i
        else :
            stuart += len(string) - i
    if stuart > kevin:
        print('Stuart {}'.format(stuart))
    elif kevin > stuart:
        print('Kevin {}'.format(kevin))
    else:
        print('Draw')


# Calling internally:
# minion_game('banana')

# Calling externally:
if __name__ == '__main__':
    s = input()
    minion_game(s)
