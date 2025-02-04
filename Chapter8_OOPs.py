# Class and objects in Python:

# Class is a blueprint for creating objects:

# Creating Class

# class Student:
#     name="Manish"


# #creating object(Instance)
# s1= Student()
# print(s1 )
# print(s1.name)


# CONSTRUCTOR:

# All Classes have a function called __init__(), which is always executed when a class being initiated.

# creating a class:
class Student:
   def __init__(self, name):
      # Here self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class

      print("adding new student")
      print(self)
      self.name= name

# Creating object

s1= Student("Yadav")
print(s1)
print(s1.name) 

s2= Student("karan")
print(s2.name)