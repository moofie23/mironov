class calc:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print(self):
        print('',self.x,'\n', self.y)

calculator = calc(50,10)

calculator.print()