class calc:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def subsctract(self):
        self.x -= 1
        self.y -= 1
        self.z -= 1

    def print(self):
        print(self.x, ' ', self.y , ' ',self.z, ' ',)

calculator = calc(32, 19, 80)

calculator.subsctract()

calculator.print()