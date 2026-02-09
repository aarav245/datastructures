student = {"Name":"Aarav","Age":14,"Grade":"9th"}
print(student)
#accessing values
print(student["Age"])
print(student["Grade"])
#adding new items
student["intrests"] = "Reading"
print(student)
#updating existing value
student["Grade"] = "10th"
print(student)
#removing items
student.pop("Age")
print(student)
del student["Grade"]
print(student)
#extracting keys
print(student.keys())
#values
print(student.values())
#items
print(student.items())
#iterating through a dictionary
for i,l in student.items():
    print(i,l)
