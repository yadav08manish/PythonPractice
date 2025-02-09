# Super Method 
# Super method is used to access methods of parent class

class Car:

    def __init__(self,type):
        self.type=type
        print("Type of Car ",type)
        
    @staticmethod
    def starts():
        print("Car Started")
    
    @staticmethod
    def stops():
        print("Car Stoped")
    
class Toyota(Car):
    def __init__(self,name):
        self.name=name
        print("name of Car", name)


# car1= Car()
# car1.starts()
# car1.stops()

carT=Toyota("Fortuner","electric");
carT.starts();
carT.stops();