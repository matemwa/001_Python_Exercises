from random import randint


class Die():

    def __init__(self, num_sides=6):
        """Assume number of sides"""
        self.num_sides = num_sides

    def roll(self) -> object:
        """Returns a random value between 1 and number of sides"""
        return randint(1, self.num_sides)
