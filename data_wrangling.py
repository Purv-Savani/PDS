
import pandas as pd

# Create Employee DataFrame
employee = {
    "Emp_ID": [101, 102, 103, 104, 105],
    "Name": ["Rahul", "Amit", "Neha", "Priya", "Riya"],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Salary": [50000, 45000, 60000, 55000, 48000]
}

emp_df = pd.DataFrame(employee)

# Create Department DataFrame
department = {
    "Department": ["IT", "HR", "Finance"],
    "Manager": ["Rakesh", "Mahesh", "Suresh"]
}

dept_df = pd.DataFrame(department)

print("Employee DataFrame")
print(emp_df)

print("\nDepartment DataFrame")
print(dept_df)

# Merge DataFrames
merged_df = pd.merge(emp_df, dept_df, on="Department")

print("\nMerged DataFrame")
print(merged_df)

# Filter Employees
print("\nEmployees with Salary > 50000")
print(merged_df[merged_df["Salary"] > 50000])

# Group By Department
print("\nAverage Salary Department Wise")
print(merged_df.groupby("Department")["Salary"].mean())

# Maximum Salary Department Wise
print("\nMaximum Salary Department Wise")
print(merged_df.groupby("Department")["Salary"].max())

# Count Employees
print("\nEmployee Count Department Wise")
print(merged_df.groupby("Department")["Emp_ID"].count())

# Sort Salary
print("\nSort by Salary")
print(merged_df.sort_values(by="Salary", ascending=False))

# Concatenate DataFrames
extra = pd.DataFrame({
    "Emp_ID": [106],
    "Name": ["Karan"],
    "Department": ["IT"],
    "Salary": [65000]
})

concat_df = pd.concat([emp_df, extra], ignore_index=True)

print("\nAfter Concatenation")
print(concat_df)

# Pivot Table
pivot = pd.pivot_table(
    merged_df,
    values="Salary",
    index="Department",
    aggfunc="mean"
)

print("\nPivot Table")
print(pivot)

# Aggregate Functions
print("\nAggregate Functions")
print(
    merged_df.groupby("Department").agg({
        "Salary": ["min", "max", "mean", "sum"]
    })
)

# Query Method
print("\nEmployees from IT Department")
print(merged_df.query("Department == 'IT'"))

# Apply Function
merged_df["Bonus"] = merged_df["Salary"].apply(lambda x: x * 0.10)

print("\nBonus (10%)")
print(merged_df)

# Rename Column
merged_df.rename(columns={"Salary": "Monthly_Salary"}, inplace=True)

print("\nRenamed Column")
print(merged_df)

# Save Result
merged_df.to_csv("employee_wrangled.csv", index=False)

print("\nData Wrangling Completed Successfully!")
