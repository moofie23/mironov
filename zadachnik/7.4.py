import math

class calc:

    def __init__(self, x):
        self.x = x
    
    def calcc(self):
        i = 0
        while i != 9:
            b = int(input('Введите массу'))
            self.x = self.x + b  
            i = i + 1 
        return self.x
               
calculator = calc(0)

print(calculator.calcc())
