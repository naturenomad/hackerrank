# SORTING - COMPARATOR

# Create a comparator and use it to sort an array. 

from functools import cmp_to_key

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def __repr__(self):
        # Represent:
        # Override the inbuilt repr function to give a clearer object description
        # Returns the object representation in string format.
        # If we don’t add a __str__ method, Python falls back on the result of __repr__ when looking for __str__. 
        # Could contain information about object so that it can be constructed again.
        # Make __repr__ strings unambiguous and helpful for developers.
        return (f'{self.__class__.__name__}('
                f'{self.name}, {self.score})')
   
    def comparator(a, b):
        val = b.score - a.score
        if val == 0:
            if a.name < b.name:
                return -1
            else:
                return 1
        return val     

#my_player=Player('me',3)
#repr(my_player)
#'Player(me, 3)'

n = int(input())
data = []

for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)
    
data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)
