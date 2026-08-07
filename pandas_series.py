
import pandas as pd
import numpy as np

# Create Series from List
data = [10, 20, 30, 40, 50]
series = pd.Series(data)

print("Series from List:")
print(series)

# Create Series with Custom Index
series2 = pd.Series(data, index=["A", "B", "C", "D", "E"])

print("\nSeries with Custom Index:")
print(series2)

# Create Series from Dictionary
student = {
    "Rahul": 85,
    "Amit": 92,
    "Neha": 88,
    "Priya": 95
}

series3 = pd.Series(student)

print("\nSeries from Dictionary:")
print(series3)

# Access Elements
print("\nFirst Element:")
print(series.iloc[0])

print("\nLast Element:")
print(series.iloc[-1])

print("\nElement with Index C:")
print(series2["C"])

# Slicing
print("\nFirst Three Elements:")
print(series[:3])

print("\nLast Two Elements:")
print(series[-2:])

# Mathematical Operations
print("\nAddition (+5):")
print(series + 5)

print("\nMultiplication (*2):")
print(series * 2)

print("\nSquare:")
print(series ** 2)

# Statistics
print("\nSum:")
print(series.sum())

print("\nMean:")
print(series.mean())

print("\nMedian:")
print(series.median())

print("\nMaximum:")
print(series.max())

print("\nMinimum:")
print(series.min())

print("\nStandard Deviation:")
print(series.std())

# Filtering
print("\nValues Greater Than 25:")
print(series[series > 25])

# Sorting
print("\nSorted Values:")
print(series.sort_values())

print("\nSorted Index:")
print(series2.sort_index())

# Check Missing Values
series4 = pd.Series([10, np.nan, 30, 40, np.nan])

print("\nSeries with Missing Values:")
print(series4)

print("\nIs Null:")
print(series4.isnull())

print("\nDrop Missing Values:")
print(series4.dropna())

print("\nFill Missing Values with 0:")
print(series4.fillna(0))

# Apply Function
print("\nSquare Root:")
print(series.apply(np.sqrt))

# Value Counts
fruit = pd.Series(["Apple", "Mango", "Apple", "Banana", "Mango", "Apple"])

print("\nValue Counts:")
print(fruit.value_counts())

# Convert Series to List
print("\nSeries to List:")
print(series.tolist())

# Convert Series to NumPy Array
print("\nSeries to NumPy Array:")
print(series.to_numpy())
