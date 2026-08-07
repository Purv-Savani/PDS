
import numpy as np

# Create Arrays
a = np.array([10, 20, 30, 40, 50])
b = np.array([1, 2, 3, 4, 5])

print("Array A:", a)
print("Array B:", b)

# Addition
print("\nAddition:")
print(a + b)

# Subtraction
print("\nSubtraction:")
print(a - b)

# Multiplication
print("\nMultiplication:")
print(a * b)

# Division
print("\nDivision:")
print(a / b)

# Floor Division
print("\nFloor Division:")
print(a // b)

# Modulus
print("\nModulus:")
print(a % b)

# Power
print("\nPower:")
print(np.power(a, 2))

# Square Root
print("\nSquare Root:")
print(np.sqrt(a))

# Absolute Value
c = np.array([-10, -20, 30, -40, 50])
print("\nAbsolute Value:")
print(np.abs(c))

# Exponential
print("\nExponential:")
print(np.exp(b))

# Natural Log
print("\nNatural Log:")
print(np.log(a))

# Base-10 Log
print("\nLog Base 10:")
print(np.log10(a))

# Trigonometric Functions
angles = np.array([0, 30, 45, 60, 90])

print("\nSin:")
print(np.sin(np.radians(angles)))

print("\nCos:")
print(np.cos(np.radians(angles)))

print("\nTan:")
print(np.tan(np.radians(angles)))

# Maximum
print("\nMaximum Value:")
print(np.max(a))

# Minimum
print("\nMinimum Value:")
print(np.min(a))

# Sum
print("\nSum:")
print(np.sum(a))

# Mean
print("\nMean:")
print(np.mean(a))

# Median
print("\nMedian:")
print(np.median(a))

# Standard Deviation
print("\nStandard Deviation:")
print(np.std(a))

# Variance
print("\nVariance:")
print(np.var(a))

# Cumulative Sum
print("\nCumulative Sum:")
print(np.cumsum(a))

# Product
print("\nProduct:")
print(np.prod(a))
