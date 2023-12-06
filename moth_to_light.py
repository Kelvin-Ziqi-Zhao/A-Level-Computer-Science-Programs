class Moth():
    def __init__(self, initPosition):
        self.__position = initPosition

    def getPosition(self):
        return self.__position
    
gypsy = Moth(10)
print(gypsy.getPosition())