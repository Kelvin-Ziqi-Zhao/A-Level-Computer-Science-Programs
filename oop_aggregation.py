'''Ideally, a Vehicle class should have a responsibility: 
to describe a vehicle which has some type of self-contained propulsion. 
A Propulsion class is responsible for the details of propulsion characteristics. 
Your task is to complete the Vehicle class by using Propulsion class below. '''

def main():
    #Do not modify the main method that is use for checking.
    myFord = Vehicle("Ford","Taurus","2010", Propulsion("combustion","gasoline"))
    print(myFord.formatForPrinting())
    
class Propulsion:
    def __init__(self, engineType, fuel):
        self.__engineType = engineType
        self.__fuel = fuel
   
    def format(self):
        return "; Engine Type: " + self.__engineType + "; Fuel: " + self.__fuel
    
class Vehicle:
    #TODO: using the Propulsion class. 
    def __init__(self, make, model, year, propulsion):
        self.__make = make
        self.__model = model
        self.__year = year 
        self.__propulsion = propulsion #data type: class propulsion
   
    def formatForPrinting(self):
        result = "Make: " + self.__make + "; Model: " + self.__model + "; Year: " + self.__year + self.__propulsion.format()
        #TODO
        ...
        return result
    
main()