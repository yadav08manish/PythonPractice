class A:
    varA="Welcome to class A"
class B:
    varB="Welcome to Class B"
class C(A,B):
    varC="Welcome to Class C"

c=C()
print(c.varA)
print(c.varB)
print(c.varC)