class RealString:
    def __init__(self, string):
        self.string = string  

    def len(self):
        return len(self.string)  

    def eq(self, other):
        if isinstance(other, RealString):
            return len(self) == len(other)  
        elif isinstance(other, str):
            return len(self) == len(other)  
        return False  


str1 = RealString("hello")
str2 = "world"

print(str1 == str2)   
