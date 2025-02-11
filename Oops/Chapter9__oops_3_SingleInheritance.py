class Car:
    color="black"
    @staticmethod
    def start():
        print("Car Started")
    
    def stop():
        print("Car Stopeed")
    

class ToyotaCar(Car):
    def __init__(self, name):
        self.name=name
        print("Instance Created for Toyota car")


car1 = ToyotaCar("Fortuner")
print(car1.name)
print(car1.color)
car1.start()

