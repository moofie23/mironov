x = int(input('Введите радиус окружности'))

import math

class calc:
    def __init__(self, x):
        self.x = x

    def cal(self):
        y = 2*self.x
        print(y)
        
calculator = calc(5)

calculator.cal()
