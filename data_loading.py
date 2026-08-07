
import pandas as pd

# Create Sample DataFrame
data = {
    "ID": [101, 102, 103, 104, 105],
    "Name": ["Rahul", "Amit", "Neha", "Priya", "Riya"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [85, 92, 78, 95, 88]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Save DataFrame to CSV
df.to_csv("students.csv", index=False)
print("\nCSV File Created Successfully!")

# Read CSV File
csv_data = pd.read_csv("students.csv")

print("\nData Read from CSV:")
print(csv_data)

# Display First Five Rows
print("\nFirst Five Rows:")
print(csv_data.head())

# Display Last Five Rows
print("\nLast Five Rows:")
print(csv_data.tail())

# Display Shape
print("\nShape:")
print(csv_data.shape)

# Display Column Names
print("\nColumns:")
print(csv_data.columns)

# Display Data Types
print("\nData Types:")
print(csv_data.dtypes)

# Display Information
print("\nInformation:")
csv_data.info()

# Statistical Summary
print("\nStatistical Summary:")
print(csv_data.describe())

# Save to Excel
df.to_excel("students.xlsx", index=False)
print("\nExcel File Created Successfully!")

# Read Excel File
excel_data = pd.read_excel("students.xlsx")

print("\nData Read from Excel:")
print(excel_data)

# Save to JSON
df.to_json("students.json", orient="records", indent=4)
print("\nJSON File Created Successfully!")

# Read JSON File
json_data = pd.read_json("students.json")

print("\nData Read from JSON:")
print(json_data)

# Convert DataFrame to Dictionary
dictionary = df.to_dict()

print("\nDataFrame as Dictionary:")
print(dictionary)

# Convert DataFrame to List
records = df.values.tolist()

print("\nDataFrame as List:")
print(records)

print("\nData Loading Completed Successfully!")
