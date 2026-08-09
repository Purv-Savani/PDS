def greet(name):
    return "Hello " + name


def add(a, b):
    return a + b


def check_result(marks):
    if marks >= 40:
        return "Pass"
    else:
        return "Fail"


name = input("Enter your name: ")
print(greet(name))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", add(a, b))

marks = int(input("Enter marks: "))
print("Result:", check_result(marks))
