# Dictionary is Mutable we can change the values

info={
    "name":"Manish",
    "EmailID":"yadav08.manish@gmail.com",
    "Age": 40,
    "is_Adult":True

}

print(type(info))
print(info)

print(info["name"])
# print(info["LName"])


# Dictionary is mutable

print(info)
info["LName"]="yadav"
print(info)



info["Subjects"]=["Maths", "Checm", "Physics"]

print(info)

#Nested Dictionary
info["SujectsWithMarks"]={"Maths":99 , "Physics":98, "Chem":97}
print(info)

infoOfStudents={
    "Name": "Manish",
    "LName":"Yadav",
    "Subjects": {"Maths":99, "Chem":98, "Physics": 97},
    "Age":40,
    "Is_Adult": True
}
print(infoOfStudents)
print(infoOfStudents["Subjects"])
print(infoOfStudents["Subjects"]["Maths"])

# Dictionary Methods
infoOfStudents.keys() #return all keys