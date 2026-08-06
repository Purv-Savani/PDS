
import numpy as np

# Create 1D Array
arr1 = np.array([10, 20, 30, 40, 50])
print("1D Array:")
print(arr1)

# Create 2D Array
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])
print("\n2D Array:")
print(arr2)

# Array Type
print("\nType:")
print(type(arr1))

# Data Type
print("\nData Type:")
print(arr1.dtype)

# Number of Dimensions
print("\nDimensions:")
print(arr2.ndim)

# Shape
print("\nShape:")
print(arr2.shape)

# Size
print("\nSize:")
print(arr2.size)

# Create Zeros Array
zeros = np.zeros((2, 3))
print("\nZeros Array:")
print(zeros)

# Create Ones Array
ones = np.ones((2, 3))
print("\nOnes Array:")
print(ones)

# Identity Matrix
identity = np.eye(3)
print("\nIdentity Matrix:")
print(identity)

# Arange
numbers = np.arange(1, 11)
print("\nArange:")
print(numbers)

# Even Numbers
even = np.arange(2, 21, 2)
print("\nEven Numbers:")
print(even)

# Linspace
line = np.linspace(0, 1, 5)
print("\nLinspace:")
print(line)

# Reshape
reshape = np.arange(1, 13).reshape(3, 4)
print("\nReshape:")
print(reshape)

# Flatten
flat = reshape.flatten()
print("\nFlatten:")
print(flat)
