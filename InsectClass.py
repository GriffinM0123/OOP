import random


class Insect:
    def __init__(self, wings, legs):
        self.miles = 0
        self.wings = wings
        self.legs = legs

    def fly(self):
        random.randint(1, 10) == self.miles

    def get_miles(self):
        return self.miles
