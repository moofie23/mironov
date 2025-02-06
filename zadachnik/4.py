class calc:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def calcc(self):
        global res1 
        global res2
        res1 = self.x // self.y
        res2 = self.x % self.y

    def result(self):
        print('Всем досталась по ', res1,'яблок','остаток яблок = ', res2)

calculator = calc(8,4)

calculator.calcc()
calculator.result()