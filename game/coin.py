import random

class Coin:
    def __init__(self, size, width, height):
        self.size = size
        self.position = [random.randint(0, width - size), random.randint(0, height - size)]
