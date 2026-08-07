
import pandas as pd

# Create Sample DataFrame
data = {
    "Student": ["Rahul", "Amit", "Neha", "Priya", "Riya", "Karan"],
    "Age": [20, 21, 19, 22, 20, 21],
    "Gender": ["Male", "Male", "Female", "Female", "Female", "Male"],
    "Department": ["IT", "CS", "IT", "CS", "IT", "CS"],
    "Marks": [85, 92, 78, 95, 88, 81]
}

df = pd.DataFrame(data)

print("Original Data")
print(df)

# First 5 Rows
print("\nFirst 5 Rows")
print(df.head())

# Last 5 Rows
print("\nLast 5 Rows")
print(df.tail())

# Shape
print("\nShape")
print(df.shape)

# Columns
print("\nColumns")
print(df.columns)

# Data Types
print("\nData Types")
print(df.dtypes)

# Information
print("\nInformation")
df.info()

# Statistical Summary
print("\nStatistical Summary")
print(df.describe())

# Mean Marks
print("\nAverage Marks")
print(df["Marks"].mean())

# Median Marks
print("\nMedian Marks")
print(df["Marks"].median())

# Maximum Marks
print("\nHighest Marks")
print(df["Marks"].max())

# Minimum Marks
print("\nLowest Marks")
print(df["Marks"].min())

# Student with Highest Marks
print("\nTop Scorer")
print(df[df["Marks"] == df["Marks"].max()])

# Students Scoring Above 80
print("\nStudents with Marks > 80")
print(df[df["Marks"] > 80])

# Sort by Marks
print("\nSorted by Marks")
print(df.sort_values(by="Marks", ascending=False))

# Department Wise Average
print("\nDepartment Wise Average Marks")
print(df.groupby("Department")["Marks"].mean())

# Gender Wise Average
print("\nGender Wise Average Marks")
print(df.groupby("Gender")["Marks"].mean())

# Department Wise Count
print("\nDepartment Wise Student Count")
print(df["Department"].value_counts())

# Correlation
print("\nCorrelation Matrix")
print(df[["Age", "Marks"]].corr())

# Add Grade Column
def grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    else:
        return "D"

df["Grade"] = df["Marks"].apply(grade)

print("\nData with Grade")
print(df)

# Save Analysis Result
df.to_csv("student_analysis.csv", index=False)

print("\nData Analysis Completed Successfully!")
