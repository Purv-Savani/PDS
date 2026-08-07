
import numpy as np

# Create Array
data = np.array([12, 15, 18, 20, 25, 30, 35, 40, 45, 50])

print("Original Data:")
print(data)

# Count
print("\nNumber of Elements:")
print(data.size)

# Sum
print("\nSum:")
print(np.sum(data))

# Mean
print("\nMean:")
print(np.mean(data))

# Median
print("\nMedian:")
print(np.median(data))

# Minimum
print("\nMinimum:")
print(np.min(data))

# Maximum
print("\nMaximum:")
print(np.max(data))

# Range
print("\nRange:")
print(np.max(data) - np.min(data))

# Variance
print("\nVariance:")
print(np.var(data))

# Standard Deviation
print("\nStandard Deviation:")
print(np.std(data))

# Percentiles
print("\n25th Percentile:")
print(np.percentile(data, 25))

print("\n50th Percentile:")
print(np.percentile(data, 50))

print("\n75th Percentile:")
print(np.percentile(data, 75))

# Average
print("\nAverage:")
print(np.average(data))

# Cumulative Sum
print("\nCumulative Sum:")
print(np.cumsum(data))

# Cumulative Product
print("\nCumulative Product:")
print(np.cumprod(data))

# Sort
print("\nSorted Data:")
print(np.sort(data))

# Unique Values
sample = np.array([10, 20, 20, 30, 40, 40, 50])

print("\nOriginal Sample:")
print(sample)

print("\nUnique Values:")
print(np.unique(sample))

# Index of Maximum
print("\nIndex of Maximum:")
print(np.argmax(data))

# Index of Minimum
print("\nIndex of Minimum:")
print(np.argmin(data))
