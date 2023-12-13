import random

def GenerateChangeInCoordinate(num):
    num += random.randint(-1,1)
    while num <= 0 or num >= 39:
        num += random.randint(-1,1)
    return num

class Animal:
    def __init__(self):
        self.__across = random.randint(0,39)
        self.__down = random.randint(0,39)
        self.__score = 0
    def eatFood(self):
        __score += 1
        #GenerateFood
        self.__init__
    def move(self):
        __across = GenerateChangeInCoordinate(__across)
        __down = GenerateChangeInCoordinate(__down)

desert1 = Desert()

class Desert:
    def __init__(self):
        gride = [['*' for i in range(40)]for i in range(40)]
        stepCounter = 0
        animalList = []

        numberOfAnimals = 
    def incrementStepCounter(self):

    def GenerateFood(self):

    def DisplayGrid(self):

