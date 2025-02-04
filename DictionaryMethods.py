infoOfStudents={
    "Name": "Manish",
    "LName":"Yadav",
    "Subjects": {"Maths":99, "Chem":98, "Physics": 97},
    "Age":40,
    "Is_Adult": True
}

# myDict.keys()  --> return all keys
print(infoOfStudents.keys()) #return all keys

# myDict.values()  --> return all values
print(infoOfStudents.values()) #return all values

# myDict.items()  --> return all key values pair as tuple
print(infoOfStudents.items()) #return all key values pair as tuple

# myDict.get("key")  --> return the key according to value
print(infoOfStudents.get("Name")) #return the key according to value

# myDict.update(newDict)  --> insert the specified items to the dictionary
infoOfStudents.update({"Age": 39, "Location":"India"})
print(infoOfStudents) #insert the specified items to the dictionary
