class Car:
    @staticmethod
    def Start():
        print("Car Started")
    @staticmethod
    def Stop():
        print("Car Stopped")

class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand=brand
        print("Brand of ToyotaCar id ", brand)

class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type=type
        print("Type of Fortuner is ", type)

f1=Fortuner("Diesel")
f1.Start()
f1.Stop()