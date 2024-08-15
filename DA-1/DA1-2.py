import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv("Dataset.csv")

# Display the first 5 records
print("\nFirst 5 Records:")
print(df.head(5))

# Display the last 5 records
print("\nLast 5 Records:")
print(df.tail(5))

# Display 'Name', 'Designation', and 'Salary' of the first 10 records
print("\nName, Designation, Salary of First 10 Records:")
print(df[['Name', 'Designation', 'Salary']].head(10))

# Display 'Name' of all records
print("\nName of All Records:")
print(df['Name'])

# Display all records
print("\nAll Records:")
print(df)
