'''Form a subclass Quarter from the class Coin. A quarter has a state theme.
The getDescription method should yield a string such as
'Quarter, value=0.25, state=California'''

#A coin with a monetary value.
class Coin:
  #Constructs a coin.
  #@param aValue the monetary value of the coin.
  #@param aName the name of the coin
  ...
        
  #Gets the coin value.
  #@return the value
  ...
        
  #Gets the coin description.
  #return a description of this coin
  ...
    
#A quarter with a state theme.
class Quarter(Coin):
  #Constructs a quarter.
  #@param aValue the monetary value of the quarter.
  #@param aName the name of the quarter
  ...
        
  def getDescription(self):
    ...

c = Quarter("Michigan")
print(c.getDescription())
n = Coin(0.05, "Nickel")
print(n.getDescription())