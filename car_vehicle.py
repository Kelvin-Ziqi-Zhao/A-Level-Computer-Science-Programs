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
class Car(Vehicle):
    def __init__(self, aValue):
        super().__init__(aValue)
    
    def getValue(self):
        output = Vehicle.getValue(self) - Vehicle.getMileage(self)*0.25
        if output <0:
            return 0
        return output 
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