# __init__ Function:

# A Class have a function called __init__(), which is always executed when the class is being initiated

# class Student:          # Creating a class
#     def __init__(self, name):
#         self.name=name
# s1=Student("Manish")    # Creating an object
# print(s1.name)


class College:
    #default Constructor
    def __init__(self):
        print(self)
        print("adding a default constructor")
    
    #Parameterized Constructor
    def __init__(self, collegename):
        self.collegename=collegename
        print("Calling parameterized Cobnstructor")

        


# c1= College()
c2=College("SRIT")
print(c2.collegename)

c3= College("MITS")
print(c3.collegename)

# c4=College()

