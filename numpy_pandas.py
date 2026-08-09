import numpy as np
import pandas as pd

marks = np.array([78, 85, 92, 67, 88])

df = pd.DataFrame({
    "Student": ["A", "B", "C", "D", "E"],
    "Marks": marks
})

df["Result"] = np.where(df["Marks"] >= 40, "Pass", "Fail")

print(df)

print("\nAverage Marks:", np.mean(marks))
print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))
