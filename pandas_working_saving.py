import pandas as pd

data = {
    "Name": ["Amit", "Neha", "Raj", "Priya"],
    "Marks": [85, 92, 76, 88]
}

df = pd.DataFrame(data)

df["Result"] = df["Marks"].apply(
    lambda x: "Pass" if x >= 40 else "Fail"
)

print(df)

print("\nStudents with marks above 80:")
print(df[df["Marks"] > 80])

df.to_csv("student_result.csv", index=False)

print("\nData saved successfully.")
