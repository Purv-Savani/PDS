A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print("Set A:", A)
print("Set B:", B)

print("Union:", A | B)
print("Intersection:", A & B)
print("A - B:", A - B)
print("B - A:", B - A)
print("Symmetric Difference:", A ^ B)

A.add(10)
A.discard(2)

print("Updated Set A:", A)
print("Is 5 present in A?", 5 in A)
