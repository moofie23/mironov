import math
class calc:
    def __init__(self, x):
        self.x = x

    def cal(self):
        y = (self.x**2 + 10)/(math.sqrt(self.x**2 + 1))
        print(y)
        
calculator = calc(5)

calculator.cal()

