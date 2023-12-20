'''Form a subclass Quarter from the class Coin. A quarter has a state theme.
The getDescription method should yield a string such as
'Quarter, value=0.25, state=California'''

#A coin with a monetary value.
class Coin:
    def __init__(self, name, monetary): #Constructs a coin.
        self.__name = name #@param aName the name of the coin
        self.__monetary = monetary #@param aValue the monetary value of the coin.

    def getCoinValue(self): #Gets the coin value.
       return __monetary #@return the value
    
    def getDescription(self): #Gets the coin description.
       return __name + "," + "value=" + __monetary #return a description of this coin
    
#A quarter with a state theme.
class Quarter(Coin):
    def __init__(self, name, monetary, state):#Constructs a quarter.
        super().__init__(monetary, name)
        __state = state

    def getDescription(self):
        return __name + "," + "value=" + __monetary + "state=" + __state

c = Quarter("Michigan")
print(c.getDescription())
n = Coin(0.05, "Nickel")
print(n.getDescription())