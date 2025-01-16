class RealString:
    def __init__(self, str1, str2):
        self.string1 = str1
        self.string2 = str2
        
    def odd(self):
        return abs((len(self.string1)-len(self.string2)))
        
    def print_result(self):
        print("//////////////////////////")
        print("Первая строчка : "+self.string1+"\nДлина строчки : "+str(len(self.string1)))
        print("Вторая строчка : "+self.string2+"\nДлина строчки : "+str(len(self.string2)))
        print("//////////////////////////")    
        print("Разница : "+str(self.odd()))
        
    def odd_char_result(self):
        numChar1=0
        numChar2=0
        
        print("//////////////////////////")
        print("Первая строчка : "+self.string1+"\nДлина строчки : "+str(len(self.string1))+"\n")
        for i in range(len(self.string1)):
            numChar1+=ord(self.string1[i])
            print("[ "+self.string1[i]+" ] : "+str(numChar1))
        print("\nОбщее сложенное : "+str(numChar1))
        print("//////////////////////////")
        print("Вторая строчка : "+self.string2+"\nДлина строчки : "+str(len(self.string2))+"\n")
        for i in range(len(self.string2)):
            numChar2+=ord(self.string2[i])
            print("[ "+self.string2[i]+" ] : "+str(numChar2))
        print("\nОбщее сложенное : "+str(numChar2))
        print("//////////////////////////")
        print("Разница : "+str(abs((numChar1-numChar2))))
        
    def odd_char(self):
        numChar1=0
        numChar2=0
        
        for i in range(len(self.string1)):
            numChar1+=ord(self.string1[i])
            
        for i in range(len(self.string2)):
            numChar2+=ord(self.string2[i])
            
        return abs((numChar1-numChar2))
        
        
    
rs=RealString("Apple","Яблоко")