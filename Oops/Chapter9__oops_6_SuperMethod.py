# When we want to access Parent class properties in child class constructor the we user Super() Method

class Car:
    def __init__(self,type):
        self.type=type
        print("Patrent Class ",self.type)
    @staticmethod
    def Start():
        print("Car Started")
    @staticmethod
    def Stop():
        print("Car Stopped")
    

class Toyoto(Car):
    def __init__(self, name,type):
        self.name=name
        self.type=type
        super().__init__(type)
        super().Start()

car1=Toyoto("Fortuner","diesel")
print(car1.name)
print("Child Class ",car1.type)



# car1.Start()