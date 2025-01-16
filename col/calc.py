class Calc:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        
    def sum(self):
        return self.num1 + self.num2
    
    def multiply(self):
        return self.num1 * self.num2
    
    def subtract(self):
        return self.num1 - self.num2
    
    def divide(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return 'На ноль делить нельзя!' 