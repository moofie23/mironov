import math
class calc:
    def __init__(self, x):
        self.x = x

    def cal(self):
        y = 17 * self.x**2 - 6*self.x + 13
        print(y)
        
calculator = calc(5)

calculator.cal()

