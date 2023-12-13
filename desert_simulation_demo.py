import random
def GenerateChangeInCoordinate(Coord):
  lowerBound = -1
  upperBound = 1
  if Coord == 0:
    lowerBound = 0 
  elif Coord == 19: 
    upperBound = 0 
  return random.randint(lowerBound, upperBound)

class Animal:
  def __init__ (self):
    self.__Across = random.randint(0,19)
    self.__Down = random.randint(0,19) 
    self.__Score = 0 
 
  def SetAcross(self, A):
    self.__Across = A

  def GetAcross(self): 
    return self.__Across

  def SetDown(self, A):
    self.__Down = A

  def GetDown(self): 
    return self.__Down

  def GetScore(self): 
    return self.__Score

  def Move(self): 
    self.__Across += GenerateChangeInCoordinate(self.__Across) 
    self.__Down += GenerateChangeInCoordinate(self.__Down) 
    if d.Grid[self.__Across][self.__Down] == 'F': 
      self.EatFood() 

  def EatFood(self):
    d.Grid[self.__Across][self.__Down] = '*'
    self.__Score += 1
    d.GenerateFood()
#    newAnimal = Animal()
#    desert.Grid[newAnimal.GetAcross()][newAnimal.GetDown()] = "A" 
#    desert.AnimalList.append(newAnimal) 

class Desert:
  def __init__ (self) : 
    self.Grid = [['*' for i in range(20)] for j in range(20)] 
    self.AnimalList = [] 
    for i in range(5) : 
      newAnimal = Animal()
      self.Grid[newAnimal.GetAcross()][newAnimal.GetDown()] = "A" 
      self.AnimalList.append(newAnimal) 
    for i in range(10):
      self.GenerateFood() 

  def DisplayGrid(self):
    for i in self.Grid:
      print("".join(i))

  def GenerateFood(self):
    x = random.randint(0,19)
    y = random.randint(0,19)
    self.Grid[x][y] = "F"

d = Desert()
for step in range(100):
  for i in d.AnimalList:
    i.Move()
for i in d.AnimalList:
  print(i.GetAcross(), i.GetDown(), i.GetScore())
d.DisplayGrid()