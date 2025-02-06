import math

class calc:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def calcc(self):
        if self.y < 3:
            return 'Точка попадает в II зону'
        elif self.y == 3:
            return 'Введите другое число'
        else:
            return 'Точка попадает в I зону'
         
calculator = calc(4,5)

print(calculator.calcc())
