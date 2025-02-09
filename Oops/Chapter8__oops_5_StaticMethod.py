# Static Methods
# Static methods that dont use self parameter (work at class level)

class Student:
    def __init__(self):
        print("Instance Created")
    @staticmethod
    def college():
        print("ABC College")

Student.college()
s1=Student()
s1.college()