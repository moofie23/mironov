class calc:

    def __init__(self, x):
        self.x = x
    
    def calcc(self):
        self.x = self.x // 100

    def result(self):
        print('Полных центнеров = ', self.x)

calculator = calc(1998)

calculator.calcc()
calculator.result()
