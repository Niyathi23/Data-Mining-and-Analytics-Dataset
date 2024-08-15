import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Load the CSV file
df = pd.read_csv('Dataset.csv')

# Draw plots
print("\nPlots:")

# 1. Pie chart on designation
plt.figure(figsize=(8, 6))
df['Designation'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Designation Distribution')
plt.show()

# 2. Histogram of Salary
plt.figure(figsize=(8, 6))
df['Salary'].plot(kind='hist', bins=20)
plt.title('Salary Distribution')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.show()

# 3. Scatter plot of Salary to Experience
plt.figure(figsize=(8, 6))
plt.scatter(df['Experience'], df['Salary'])
plt.title('Salary vs Experience')
plt.xlabel('Experience')
plt.ylabel('Salary')
plt.show()