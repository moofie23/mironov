import math

class calc:

    def __init__(self, x, y, z, b):
        self.x = x
        self.y = y
        self.z = z
        self.b = b
    
    def calcc(self):
        res1 = self.x/self.y
        res2 = self.z/self.b
        a = 0
        if res1 > res2:
            a = res1
        elif res1 == res2:
            a = 'Числа равны'
        else:
            a = res2
        return a
        
         
calculator = calc(4,5,8,15)
print('Наибольшее число = ',)

print(calculator.calcc())
