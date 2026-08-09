numbers = [10, 20, 30, 40, 50]

print("Original List:", numbers)

numbers.append(60)
numbers.insert(1, 15)
numbers.remove(30)

print("Updated List:", numbers)
print("First Element:", numbers[0])
print("Last Element:", numbers[-1])
print("List Slice:", numbers[1:4])
print("Length:", len(numbers))

squares = [x * x for x in range(1, 6)]
print("Squares:", squares)

student = ("Amit", 20, "Computer Engineering")

print("Tuple:", student)
print("Student Name:", student[0])
print("Age:", student[1])
print("Course:", student[2])
print("Tuple Length:", len(student))
