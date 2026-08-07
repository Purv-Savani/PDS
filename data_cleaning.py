
import pandas as pd
import numpy as np

# Create Sample DataFrame
data = {
    "ID": [101, 102, 103, 104, 104],
    "Name": ["Rahul", "Amit", "Neha", None, "Priya"],
    "Age": [20, 21, np.nan, 22, 22],
    "Marks": [85, np.nan, 78, 95, 95],
    "City": ["Surat", "Ahmedabad", "Rajkot", "Surat", "Surat"]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Check Missing Values
print("\nMissing Values:")
print(df.isnull())

# Count Missing Values
print("\nTotal Missing Values:")
print(df.isnull().sum())

# Fill Missing Values
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
df["Name"] = df["Name"].fillna("Unknown")

print("\nAfter Filling Missing Values:")
print(df)

# Check Duplicate Rows
print("\nDuplicate Rows:")
print(df.duplicated())

# Remove Duplicate Rows
df = df.drop_duplicates()

print("\nAfter Removing Duplicates:")
print(df)

# Rename Columns
df.rename(columns={"Marks": "Score"}, inplace=True)

print("\nAfter Renaming Column:")
print(df)

# Change Data Type
df["Age"] = df["Age"].astype(int)

print("\nAfter Changing Age Data Type:")
print(df.dtypes)

# Replace Values
df["City"] = df["City"].replace("Surat", "SURAT")

print("\nAfter Replacing Values:")
print(df)

# Strip Extra Spaces
df["Name"] = df["Name"].str.strip()

# Convert to Uppercase
df["Name"] = df["Name"].str.upper()

print("\nUppercase Names:")
print(df)

# Add New Column
df["Status"] = "Pass"

print("\nAfter Adding Status Column:")
print(df)

# Drop Column
df.drop("Status", axis=1, inplace=True)

print("\nAfter Dropping Status Column:")
print(df)

# Sort by Score
df = df.sort_values(by="Score", ascending=False)

print("\nSorted by Score:")
print(df)

# Reset Index
df.reset_index(drop=True, inplace=True)

print("\nReset Index:")
print(df)

# Save Cleaned Data
df.to_csv("cleaned_students.csv", index=False)

print("\nCleaned data saved as cleaned_students.csv")
