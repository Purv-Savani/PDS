marks = int(input("Enter your marks: "))

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 40:
    grade = "D"
else:
    grade = "Fail"

print("Grade:", grade)

age = int(input("Enter your age: "))

if age >= 18 and marks >= 40:
    print("Eligible")
else:
    print("Not Eligible")
