# del Keyword:
# Used to delete object properties or object itself

# To delete object
# del sq

# To delete properties
# del s1.name 


class Student:
    def __init__(self, name):
        self.name=name

s1=Student("Manish")
print(s1.name)

# del s1.name
# print(s1.name)

print(s1)

del s1
print(s1)