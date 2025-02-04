
dict={"cat": "A small animal",
      "table": ["a piece of furniture","list of facts and figure"]}

print(dict)


classRooms = {
    "Room1": "python",
    "Room2": "java",
    "Room3": "c++",
    "Room4": "javascript",
    "Room4": "C"
}

print(classRooms)
print(len(classRooms))


setClassRooms = {"python","java","c++","python","javascript","java","python","java","c++","c"}
print(setClassRooms)
print(len(setClassRooms))


dictMarks={}
print(type(dictMarks))
print(dictMarks)

x=int(input("Please enter physics marks: "))
dictMarks.update({"physics":x})

x=int(input("Please enter math marks: "))
dictMarks.update({"math":x})


x=int(input("Please enter chemistry marks: "))
dictMarks.update({"chemistry":x})
print(dictMarks)