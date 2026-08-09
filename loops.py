print("For Loop:")

for i in range(1, 6):
    print(i)

print("\nWhile Loop:")

i = 1

while i <= 5:
    print(i)
    i += 1

print("\nBreak:")

for i in range(1, 10):
    if i == 5:
        break
    print(i)

print("\nContinue:")

for i in range(1, 6):
    if i == 3:
        continue
    print(i)
