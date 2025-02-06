class calc:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def calcc(self):
        global res1 
        res1 = self.x // self.z

    def result(self):
        print('можно отрезать = ', res1)

calculator = calc(540, 130, 130)

calculator.calcc()
calculator.result()