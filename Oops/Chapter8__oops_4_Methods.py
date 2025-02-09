# Methods
# Methods are functions that belong to objects

class Student:
    def __init__(self, name):
        self.name=name

    def Hello(self):
        print("Hello ", self.name)

s1=Student("Manish")
s1.Hello()


