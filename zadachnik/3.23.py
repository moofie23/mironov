class calc:

    def __init__(self, x):
        self.x = x
    
    def calcc(self):
        res1 = str(self.x)
        return int(res1[-1] + res1[:-1])

calculator = calc(93532)

print(calculator.calcc())