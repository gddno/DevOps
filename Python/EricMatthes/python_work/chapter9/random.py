from random import randint

class Die:
    def __init__(self):
	    self.sides = 6
    def roll_die(self):
	    x = randint(1,self.sides)
	    print(x)
my_cub = Die()
my_cub.roll_die()