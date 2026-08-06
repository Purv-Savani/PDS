
import numpy as np

# Create 1D Array
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])

print("Original Array:")
print(arr)

# Access Elements
print("\nFirst Element:")
print(arr[0])

print("\nLast Element:")
print(arr[-1])

print("\nThird Element:")
print(arr[2])

# Basic Slicing
print("\nElements from index 1 to 4:")
print(arr[1:5])

print("\nFirst Four Elements:")
print(arr[:4])

print("\nElements from index 4 onwards:")
print(arr[4:])

print("\nEvery Second Element:")
print(arr[::2])

print("\nReverse Array:")
print(arr[::-1])

# Create 2D Array
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("\n2D Array:")
print(matrix)

# Access Elements
print("\nElement at Row 1 Column 2:")
print(matrix[1, 2])

print("\nFirst Row:")
print(matrix[0])

print("\nSecond Column:")
print(matrix[:, 1])

print("\nLast Row:")
print(matrix[-1])

print("\nLast Column:")
print(matrix[:, -1])

print("\nSub Matrix:")
print(matrix[0:2, 1:3])

# Boolean Indexing
print("\nElements Greater Than 40:")
print(arr[arr > 40])

print("\nEven Numbers:")
print(arr[arr % 2 == 0])

# Fancy Indexing
print("\nFancy Indexing:")
print(arr[[0, 2, 4, 6]])

# Copy
copy_arr = arr.copy()
copy_arr[0] = 999

print("\nOriginal Array After Copy:")
print(arr)

print("\nCopied Array:")
print(copy_arr)

# View
view_arr = arr.view()
view_arr[1] = 888

print("\nOriginal Array After View:")
print(arr)

print("\nView Array:")
print(view_arr)
