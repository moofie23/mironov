import math

class calc:
    def __init__(self, x):
        self.x = x
    def cal(self):
        y = 2*math.pi*self.x
        z = math.pi*self.x**2
        print('длина окружности = ', y, 'площадь круга = ', z)
        
calculator = calc(5)

calculator.cal()
