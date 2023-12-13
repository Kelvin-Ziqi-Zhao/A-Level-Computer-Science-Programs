import random

def GenerateChangeInCoordinate(num):
    num += random.randint(-1,1)
    while num <= 0 or num >= 39:
        num += random.randint(-1,1)
    return num

class Animal:
    def __init__(self):
        self.__aross = random.randint(0,39)
        self.__down = random.randint(0,39)
        self.__score = 0
    def EatFood(self):
        __score += 1
        #GenerateFood
        self.__init__
    def Move(self):
