class calc:

    def __init__(self, x):
        self.x = x
    
    def calcc(self):
        res1 = str(self.x)
        return int(res1[:-2]+res1[2] + res1[1])

calculator = calc(935)

print(calculator.calcc())