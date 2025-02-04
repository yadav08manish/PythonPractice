# Methods tht dont use self prameter (Work at class level)

# class student:
#     @staticmethod  #decorator
#     def college():
#         print("My name")

class Student:
    @staticmethod
    def college():
        print("Hello")
Student.college()
