import math

class calc:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def calcc(self):
        res1 = self.y**2
        res2 = math.pi * self.x**2
        a = 0
        if res1 > res2:
            a = res1
        elif res1 == res2:
            a = 'Числа равны'
        else:
            a = res2
        return a
        
         
calculator = calc(4,5)
print('Наибольшее число = ',)

print(calculator.calcc())
