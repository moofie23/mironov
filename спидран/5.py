class calc:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print(self):
        print('',self.x,'\n', '\n', self.y)

calculator = calc(1,2)

calculator.print()