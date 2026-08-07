
import pandas as pd

# Create DataFrame
student = {
    "ID": [101, 102, 103, 104, 105],
    "Name": ["Rahul", "Amit", "Neha", "Priya", "Riya"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [85, 92, 78, 95, 88],
    "City": ["Surat", "Ahmedabad", "Rajkot", "Vadodara", "Surat"]
}

df = pd.DataFrame(student)

print("Original DataFrame:")
print(df)

# Display First Five Rows
print("\nFirst 5 Rows:")
print(df.head())

# Display Last Five Rows
print("\nLast 5 Rows:")
print(df.tail())

# Data Types
print("\nData Types:")
print(df.dtypes)

# Shape
print("\nShape:")
print(df.shape)

# Columns
print("\nColumn Names:")
print(df.columns)

# Information
print("\nInformation:")
print(df.info())

# Statistical Summary
print("\nStatistical Summary:")
print(df.describe())

# Select Single Column
print("\nName Column:")
print(df["Name"])

# Select Multiple Columns
print("\nName and Marks:")
print(df[["Name", "Marks"]])

# Select Row using iloc
print("\nFirst Row:")
print(df.iloc[0])

# Select Multiple Rows
print("\nFirst Three Rows:")
print(df.iloc[0:3])

# Filter Data
print("\nStudents with Marks > 85:")
print(df[df["Marks"] > 85])

# Sort by Marks
print("\nSorted by Marks:")
print(df.sort_values("Marks"))

# Add New Column
df["Result"] = ["Pass", "Pass", "Pass", "Pass", "Pass"]

print("\nAfter Adding Result Column:")
print(df)

# Update Marks
df.loc[0, "Marks"] = 90

print("\nUpdated Marks:")
print(df)

# Delete Column
df.drop("Result", axis=1, inplace=True)

print("\nAfter Deleting Result Column:")
print(df)

# Check Missing Values
print("\nMissing Values:")
print(df.isnull())

# Count Missing Values
print("\nTotal Missing Values:")
print(df.isnull().sum())

# Unique Cities
print("\nUnique Cities:")
print(df["City"].unique())

# Value Counts
print("\nCity Count:")
print(df["City"].value_counts())

# Mean Marks
print("\nAverage Marks:")
print(df["Marks"].mean())

# Maximum Marks
print("\nHighest Marks:")
print(df["Marks"].max())

# Minimum Marks
print("\nLowest Marks:")
print(df["Marks"].min())

# Save DataFrame to CSV
df.to_csv("students.csv", index=False)

print("\nDataFrame saved as students.csv")
