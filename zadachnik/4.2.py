import math

class calc:

    def __init__(self, x):
        self.x = x
    
    def calcc(self):
        if self.x > 0:
            res1 = pow(math.sin(self.x), 2) * self.x  
        else:
            res1 = 1 - 2 * math.sin(self.x) * pow(self.x, 2)  
        return res1

calculator = calc(9)

print(calculator.calcc())
