import pandas as pd
import numpy as np
from scipy import stats

# Load the CSV file into a DataFrame
df = pd.read_csv("Dataset.csv")

# Display the DataFrame to understand its structure
print("Data Overview:")
print(df.head())

# Convert necessary columns to numeric for calculations
df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')
df['Experience'] = pd.to_numeric(df['Experience'], errors='coerce')

# a) Mean, Median, and Mode
mean_salary = df['Salary'].mean()
median_salary = df['Salary'].median()
mode_salary = df['Salary'].mode()[0] if not df['Salary'].mode().empty else np.nan

mean_experience = df['Experience'].mean()
median_experience = df['Experience'].median()
mode_experience = df['Experience'].mode()[0] if not df['Experience'].mode().empty else np.nan

print("\nSalary Statistics:")
print(f"Mean Salary: {mean_salary}")
print(f"Median Salary: {median_salary}")
print(f"Mode Salary: {mode_salary}")

print("\nExperience Statistics:")
print(f"Mean Experience: {mean_experience}")
print(f"Median Experience: {median_experience}")
print(f"Mode Experience: {mode_experience}")

# b) Variance and Covariance
variance_salary = df['Salary'].var()
variance_experience = df['Experience'].var()
covariance_salary_experience = df[['Salary', 'Experience']].cov().iloc[0, 1]

print("\nVariance:")
print(f"Salary Variance: {variance_salary}")
print(f"Experience Variance: {variance_experience}")

print("\nCovariance:")
print(f"Covariance between Salary and Experience: {covariance_salary_experience}")

# c) Correlation of Salary to Experience
correlation_salary_experience = df['Salary'].corr(df['Experience'])

print("\nCorrelation:")
print(f"Correlation between Salary and Experience: {correlation_salary_experience}")
