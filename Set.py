# Set is the collection of Unordered Items
# Each element is the set Must be Unique and Immutable

setTest={1,33,4,1,2,5,6,"Hello","Hello"}
print(setTest)
print(type(setTest))

setTest1 = {}
print(setTest1)
print(type(setTest1))

setTest2 = set()
print(setTest2)
print(type(setTest2))



# Set Methods

# set.add(el)  adds an element
setTest2.add(3)
print(setTest2)

setTest2.add((11,22,33))
print(setTest2)


# set.remove(el)  remove an element
print("=====================================================================")
setTest2.remove(3)
print(setTest2)

# set.clear()  remove all elements, clear the set
print("=====================================================================")
setTest3={2,7,4,4,4,7,1,6,3,2}
print(setTest3)
setTest3.clear()
print(setTest3)



# set.pop() returns random value from set
print("=====================================================================")
setTest4={"Hi", "Hello","Namaste", "Jai Ram Ji"}
print(setTest4.pop())
print("================Sets are MUTABLE since we can add or remove values in/from SET, BUT elements of Set are Immutable hence we can not add list and dictionary as an element in Set ========================================")

# setTest2.add([11,22,33])
# print(setTest2)


# setTest2.add({"FirstNumber":11,"SecondNumber":22,"ThirdNumber":33})
# print(setTest2)


# set.union(set2) Combine both set values and returns new
set1 = {1,2,3,4}
print(set1)
set2 = {3,4,5}
print(set2)
print(set1.union(set2))
print(set1)

#set.intersection(set2) Combines common values and returns
print(set1.intersection(set2))
print("=====================================================================")

x={int(9),float(9.0)}
print(type(x))
print(x)
