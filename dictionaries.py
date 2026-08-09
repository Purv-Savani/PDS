student = {
    "name": "Amit",
    "age": 20,
    "course": "Computer Engineering",
    "marks": 85
}

print(student)

print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])
print("Marks:", student["marks"])

student["marks"] = 90
student["city"] = "Surat"

print("Updated Dictionary:", student)

print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

for key, value in student.items():
    print(key, ":", value)
