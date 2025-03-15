import math

class calc:
    def __init__(self, x):
        self.x = x

    def print(self):
        print(f"{self.x:.4}")

calculator = calc(math.pi)

calculator.print()