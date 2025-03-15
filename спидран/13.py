import math

class calc:
    def __init__(self, x):
        self.x = x

    def cal(self):
        y = math.sin((3.2 + math.sqrt(1 + self.x)/abs(5*self.x)))
        print(y)
        
calculator = calc(5)

calculator.cal()
