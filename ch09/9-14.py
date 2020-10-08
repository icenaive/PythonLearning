from random import randint

class Die():
    def __init__(self, sides = 6):
        self.sides = sides
    
    def roll_die(self):
        for _ in range(0, 10):
            x = randint(1, self.sides)
            print(x)

die = Die()
die.roll_die()
die = Die(100)
die.roll_die()