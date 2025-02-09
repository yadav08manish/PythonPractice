# When one class(child/derived class) derives the properties and methods of another class(parent/base)

# class car:
#     ....
#     ....

# class ToyotaCar( car):
#     .....

# class Car:
#     @staticmethod
#     def start():
#         print("Car Starts")
    
#     @staticmethod
#     def stop():
#         print("Car Stops")
    
# class ToyotaCar(Car):
#     def __init__(self, name):
#         self.name=name
#         print(name)
    
# car1=ToyotaCar("Fortuner")
# car2=ToyotaCar("Test")
# car1.start()
# car1.stop()

# Three Types of Inheritance:

# 1. Single Inheritance
# 2. Multi-Level Inheritance
# 3. Multiple Inheritance

#1. Single Inheritance
class A:
     a="Class A variable"
class B(A):
     b="Class B variable"

print("Single Inheritance")   
objB= B
print(objB.a)
print(objB.b)

#2. MultiLevel Inheritance
class C(B):
     c="Class C variable"
print("MultiLevel Inheritance")
objC= C
print(objC.a)
print(objC.b)
print(objC.c)

#3 Multiple Inheritance
print("Multiple Inheritance")
class A1:
     a1="Class A1 variable"
class B1:
     b1="Class B1 variable"
class C1:
     c1="Class C1 variable"
class D(A1,B1,C1):
     d="Class D Variable"
objD=D
print(objD.a1)
print(objD.b1)
print(objD.c1)
print(objD.d)
    




     