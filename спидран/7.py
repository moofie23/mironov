import math

class calc:
    def __init__(self, x):
        self.x = x

    def print(self):
        print(f"{self.x:.2}")

calculator = calc(math.e)

calculator.print()