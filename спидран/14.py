x = int(input('Введите сторону квадрата'))

import math

class calc:
    def __init__(self, x):
        self.x = x

    def cal(self):
        y = 4*self.x
        print(y)
        
calculator = calc(5)

calculator.cal()
