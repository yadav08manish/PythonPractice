#Create a Student class that takes name and marks of 3 subjects in constructor.
#Then create a method to print the average

class Student:
    def __init__(self, name,marks):
        self.name=name
        self.marks=marks
    
    def GetAverage(self):
        sum=0
        for val in self.marks:
            sum +=val
        print(self.name, "has average marks ",sum/len(self.marks))
s1=Student("Manish",[79,78,77])
s1.GetAverage()