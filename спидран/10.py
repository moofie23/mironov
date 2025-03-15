import math
class calc:
    def __init__(self, x):
        self.x = x

    def cal(self):
        y = 3 * self.x**2 + 5*self.x - 21
        print(y)
        
calculator = calc(5)

calculator.cal()

