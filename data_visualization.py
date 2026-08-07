
import matplotlib.pyplot as plt
import numpy as np

# Sample Data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [120, 150, 180, 170, 200, 220]

students = ["Rahul", "Amit", "Neha", "Priya", "Riya"]
marks = [85, 92, 78, 95, 88]

age = [18, 19, 20, 21, 22]
score = [70, 75, 82, 90, 96]

# -----------------------------------
# Line Plot
# -----------------------------------
plt.figure(figsize=(6,4))
plt.plot(months, sales, marker="o")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

# -----------------------------------
# Bar Chart
# -----------------------------------
plt.figure(figsize=(6,4))
plt.bar(students, marks)
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# -----------------------------------
# Horizontal Bar Chart
# -----------------------------------
plt.figure(figsize=(6,4))
plt.barh(students, marks)
plt.title("Horizontal Bar Chart")
plt.show()

# -----------------------------------
# Scatter Plot
# -----------------------------------
plt.figure(figsize=(6,4))
plt.scatter(age, score)
plt.title("Age vs Score")
plt.xlabel("Age")
plt.ylabel("Score")
plt.grid(True)
plt.show()

# -----------------------------------
# Histogram
# -----------------------------------
data = [45,55,60,65,70,75,80,85,90,95,60,70,75,80]

plt.figure(figsize=(6,4))
plt.hist(data, bins=5)
plt.title("Histogram")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

# -----------------------------------
# Pie Chart
# -----------------------------------
subjects = ["Python","Java","DBMS","OS"]
hours = [30,25,20,25]

plt.figure(figsize=(6,6))
plt.pie(hours,
        labels=subjects,
        autopct="%1.1f%%",
        startangle=90)
plt.title("Study Time Distribution")
plt.show()

# -----------------------------------
# Multiple Line Plot
# -----------------------------------
python = [80,82,85,88,92,95]
java = [75,78,81,84,86,90]

plt.figure(figsize=(6,4))
plt.plot(months, python, marker="o", label="Python")
plt.plot(months, java, marker="s", label="Java")
plt.title("Python vs Java")
plt.xlabel("Month")
plt.ylabel("Marks")
plt.legend()
plt.grid(True)
plt.show()

# -----------------------------------
# Subplots
# -----------------------------------
fig, ax = plt.subplots(1,2,figsize=(10,4))

ax[0].plot(months,sales,marker="o")
ax[0].set_title("Sales")

ax[1].bar(students,marks)
ax[1].set_title("Marks")

plt.tight_layout()
plt.show()

# -----------------------------------
# Box Plot
# -----------------------------------
plt.figure(figsize=(5,4))
plt.boxplot(data)
plt.title("Box Plot")
plt.show()

# -----------------------------------
# Stem Plot
# -----------------------------------
x = np.arange(1,11)
y = np.array([5,8,2,9,7,6,3,5,4,8])

plt.figure(figsize=(6,4))
plt.stem(x,y)
plt.title("Stem Plot")
plt.show()

# -----------------------------------
# Fill Between
# -----------------------------------
x = np.arange(1,11)
y1 = x
y2 = x + 3

plt.figure(figsize=(6,4))
plt.plot(x,y1)
plt.plot(x,y2)
plt.fill_between(x,y1,y2,alpha=0.3)
plt.title("Fill Between")
plt.show()

# -----------------------------------
# Save Figure
# -----------------------------------
plt.figure(figsize=(6,4))
plt.plot(months,sales,marker="o")
plt.title("Monthly Sales")
plt.savefig("monthly_sales.png")
plt.show()

print("Data Visualization Completed Successfully!")
