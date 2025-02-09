# Class And Instance Attributes

# Class Objects
# Instance Objects

class Student:
    collegeName="SRIT Collge"    # Class Attribute
    def __init__(self, name, marks):
        self.name=name   #Instance Attribte
        self.marks=marks #Instance Attribte
    
S1 = Student("Manish", 90)
print(S1.name)
print(S1.marks)
print(S1.collegeName)

s2 = Student("Saroj",99)
print("Student ", s2.name, " from College ", s2.collegeName, " got ",s2.marks,"Marks")
    
