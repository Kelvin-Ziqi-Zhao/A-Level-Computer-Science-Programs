class Moth():
    def __init__(self, initPosition):
        self.__position = initPosition
    
    def moveToLight(self,lightPosition):
        self.__position = (self.__position + lightPosition)/2

    def getPosition(self):
        return self.__position
    
gypsy = Moth(10)
gypsy.moveToLight(0)
print(gypsy.getPosition())
gypsy.moveToLight(10)
print(gypsy.getPosition())
gypsy.moveToLight(0)
print(gypsy.getPosition())