class calc:

    def __init__(self, x):
        self.x = x
    
    def calcc(self):
        self.x = self.x // 7

    def result(self):
        print('Недель полных прошло = ', self.x)

calculator = calc(234)

calculator.calcc()
calculator.result()