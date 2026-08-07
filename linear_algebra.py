
import numpy as np

# Create Matrices
A = np.array([[2, 4],
              [6, 8]])

B = np.array([[1, 3],
              [5, 7]])

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

# Matrix Addition
print("\nAddition (A + B):")
print(A + B)

# Matrix Subtraction
print("\nSubtraction (A - B):")
print(A - B)

# Element-wise Multiplication
print("\nElement-wise Multiplication:")
print(A * B)

# Matrix Multiplication
print("\nMatrix Multiplication:")
print(np.dot(A, B))

# Matrix Transpose
print("\nTranspose of A:")
print(A.T)

# Determinant
print("\nDeterminant of A:")
print(np.linalg.det(A))

# Inverse
print("\nInverse of A:")
print(np.linalg.inv(A))

# Rank
print("\nRank of A:")
print(np.linalg.matrix_rank(A))

# Trace
print("\nTrace of A:")
print(np.trace(A))

# Eigenvalues and Eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

print("\nEigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)

# Identity Matrix
print("\nIdentity Matrix (3x3):")
print(np.eye(3))

# Zero Matrix
print("\nZero Matrix (2x3):")
print(np.zeros((2,3)))

# Ones Matrix
print("\nOnes Matrix (2x3):")
print(np.ones((2,3)))

# Matrix Reshape
arr = np.arange(1, 13)

print("\nOriginal Array:")
print(arr)

print("\nReshape to 3x4:")
print(arr.reshape(3,4))

# Solve Linear Equations
C = np.array([[2, 1],
              [5, 3]])

D = np.array([8, 18])

print("\nSolution of Linear Equation:")
print(np.linalg.solve(C, D))
