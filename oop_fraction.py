class Fraction:
    def __init__(self, numerator, denominator):
        self.__numerator = numerator
        self.__denominator = denominator
    
    def gcd(self, x, y):
        if x == 0:
            return y
        return self.gcd(y%x, x)
    
    def reduce(self):
        if self.__numerator <= self.__denominator:
            g = self.gcd(self.__numerator,self.__denominator)
        else:
            g = self.gcd(self.__denominator,self.__numerator)
        
        self.__numerator = self.__numerator//g
        self.__denominator = self.__denominator//g

    def plus(self, numerator, denominator):
        self.__numerator = self.__numerator * denominator + self.__denominator * numerator
        self.__denominator = self.__denominator * denominator
        self.reduce()

    def print(self):
        print(self.__numerator,"/",self.__denominator)

a = Fraction(1,4)
a.plus(2,4)
a.print()