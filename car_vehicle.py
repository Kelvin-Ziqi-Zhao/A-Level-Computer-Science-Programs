'''Complete the Car class below so that it inherits from the given Vehicle class. 
Cars lose value over time. In this example, you should assume that the value 
is reduced by 25 cents per mile driven, until it reaches zero.'''

class Vehicle:
    def __init__(self, aValue):
        self.__value = aValue
        self.__mileage = 0

    def drive(self, milesMoved):
        self.__mileage += milesMoved

    def getValue(self):
        return self.__value
   
    def getMileage(self):
        return self.__mileage
    
#TODO: Inherit from Vehicle
class Car...
    #TODO: Complete constructor
    ...
    
    #TODO: Override the getValue method
    ...
    
myCar = Car(20000)
print(myCar.getValue())
myCar.drive(10000)
print(myCar.getValue())
myCar.drive(30000)
print(myCar.getValue())
myCar.drive(40000)
print(myCar.getValue())
myCar.drive(10000)
print(myCar.getValue())