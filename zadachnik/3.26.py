class calc:

    def __init__(self, x):
        self.x = x
    
    def calcc(self):
        res1 = str(self.x)
        print(res1)
        res2 = int(res1[:-2]+res1[2] + res1[1])
        print(res2)
        res3 = res1[1] + res1[0]+res1[2:]
        print(res3)
        res4 = res1[1] + res1[2:] + res1[0]
        print(res4)
        res5 = res1[2:] + res1[1] + res1[0]
        print(res5)
        res6 = res1[2:] + res1[0] + res1[1]
        print(res6)

calculator = calc(935)

calculator.calcc()