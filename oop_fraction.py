class Fraction:
    def __init__(self, numerator, denominator):
        self.__numerator = numerator
        self.__denominator = denominator
    
    def gcd(self, x, y):
        if x == 0:
            print(y)
            return y
        return self.gcd(y%x, x)
    
    def reduce(self):
        if self.__numerator <= self.__denominator:
            g = self.gcd(self.__numerator,self.__denominator)
        else:
            g = self.gcd(self.__denominator,self.__numerator)
        
        self.__numerator = self.__numerator/g
        self.__denominator = self.__denominator/g

    def print(self):
        print(self.__numerator,"/",self.__denominator)

a = Fraction(30,50)
a.reduce()
a.print()