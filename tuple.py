# Tupples are immutable, we can not add or change values in tuple

tup=(10,23,31,14)
print(tup)
print(tup[0])
print(tup[1])


tup=(1,0)
print(tup)
print(type(tup))

tup=(1)
print(tup)
print(type(tup))

tup=("Hello")
print(tup)
print(type(tup))

tup=("Hello",)
print(tup)
print(type(tup))

tup=("Hello",2)
print(tup)
print(type(tup))


# SLICING

tup=(2,33,2,1,44,77,32,56,5)
print(tup)
print(tup[2:5])  #Slicing


# TUPLE Methods

tup = (1,2,7,4,3,1,2)
print(tup)

print(tup.index(1))  # return index of first occurence
print(tup.count(1)) #count total occurence



# PRACTICLES:

