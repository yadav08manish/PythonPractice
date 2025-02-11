#When one class derives the propoerties ans methods of another class

class Car:
    @staticmethod
    def start():
        print("Car Starts")

class Toyota(Car):
    def __init__(self, name):
        self.name=name


car1= Toyota("Fortuner")
print(car1.name)
car1.start()
