#Abstraction: Hiding the implementation details of a calls and only showing the essential features to the user:

class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False
    
    def Starts(self):
        self.clutch=True
        self.acc=True
        print("Car Started")


c1=Car()
c1.Starts()