# __init__(self)
# Above Constructor is called default constructor:

# __init__(self, name, marks)
# Above Constructor is called parameterized constructor

# class Student:
#     def __init__(self):
#         print("Default constructor is called")

#     # def __init__(self, name):
#     #     print("Parameterized constructor called")


# s1=Student()
# s1.name="Manish"
# print(s1.name)

class Student:
    def __init__(self, name):
        print("Parameterized constructor called")
        self.name   = name


s1=Student("Manish")
print(s1.name)


