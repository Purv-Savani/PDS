
import numpy as np
from statistics import mean, median, mode
import random

# Sample Data
data = [12, 15, 18, 20, 22, 25, 28, 30, 30, 35]

print("Original Data:")
print(data)

# Mean
print("\nMean:")
print(mean(data))

# Median
print("\nMedian:")
print(median(data))

# Mode
print("\nMode:")
print(mode(data))

# Minimum and Maximum
print("\nMinimum:")
print(min(data))

print("\nMaximum:")
print(max(data))

# Range
print("\nRange:")
print(max(data) - min(data))

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

# Probability Example (Coin Toss)
coin = ["Head", "Tail"]

print("\n10 Coin Tosses:")
for i in range(10):
    print(random.choice(coin), end=" ")

print()

# Probability Example (Dice Roll)
print("\n10 Dice Rolls:")
for i in range(10):
    print(random.randint(1, 6), end=" ")

print()

# Random Integers
print("\nRandom Integer Array:")
print(np.random.randint(1, 101, size=10))

# Random Float Numbers
print("\nRandom Float Numbers:")
print(np.random.random(5))

# Normal Distribution
print("\nNormal Distribution:")
normal = np.random.normal(loc=50, scale=10, size=10)
print(normal)

# Uniform Distribution
print("\nUniform Distribution:")
uniform = np.random.uniform(1, 10, size=10)
print(uniform)

# Random Sample
print("\nRandom Sample:")
sample = random.sample(data, 5)
print(sample)

# Shuffle Data
random.shuffle(data)

print("\nShuffled Data:")
print(data)

# Correlation
x = np.array([10, 20, 30, 40, 50])
y = np.array([15, 25, 35, 45, 55])

print("\nCorrelation Coefficient:")
print(np.corrcoef(x, y))
