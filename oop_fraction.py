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

class MixedFraction(Fraction):
    def __init__(self, whole, numerator, denominator):
        Fraction. __init__(self, numerator, denominator)
        self.__whole = whole

    def print(self):
        print(self.__whole, end = " + ")
        Fraction.print(self)

aMix = MixedFraction(1,1,4)
aMix.print()