# Class and Instance Attributes:

# 2 types of Attribute available
# Instance Attributes
# class Attribute

class Student:
    name="Anonymous"  # Class Instance
    college_name="St. Aloysius"
    def __init__(self):
        print("default Constructor initialized")

    def __init__(self, name, marks):
        self.name=name
        self.marks=marks
        print(":paremeterized initialized")

# s1= Student()
# s1.name="Manish"   # Instance attributes
# s1.marks=100       # Instance attributes
# print(s1.name)
# print(s1.marks)

s2=Student("Saroj",200)
print(s2.name)
print(s2.marks)
print(s2.college_name)

