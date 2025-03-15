a = int(input('Введите число:'))
import math
class calc:
    def __init__(self, x):
        self.x = x

    def print(self):
        print('Вы ввели число:', self.x)

calculator = calc(a)

calculator.print()