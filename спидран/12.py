import math

class calc:
    def __init__(self, x):
        self.x = x

    def cal(self):
        y = math.sqrt(2*self.x+math.sin(abs(3*self.x))/3.56)
        print(y)
        
calculator = calc(5)

calculator.cal()
