'''Form a subclass Quarter from the class Coin. A quarter has a state theme.
The getDescription method should yield a string such as
'Quarter, value=0.25, state=California'''

#A coin with a monetary value.
class Coin:
    def __init__(self,monetary, name): #Constructs a coin.
        self.__name = name #@param aName the name of the coin
        self.__monetary = monetary #@param aValue the monetary value of the coin.

    def getCoinValue(self): #Gets the coin value.
       return self.__monetary #@return the value
    
    def getDescription(self): #Gets the coin description.
       return self.__name + ", " + "value=" + str(self.__monetary) #return a description of this coin
    
#A quarter with a state theme.
class Quarter(Coin):
    def __init__(self, state):#Constructs a quarter.
        super().__init__(0.25, "Quater")
        self.__state = state

    def getDescription(self):
        return Coin.getDescription(self) + ", state=" + self.__state

c = Quarter("Michigan")
print(c.getDescription())
n = Coin(0.05, "Nickel")
print(n.getDescription())
