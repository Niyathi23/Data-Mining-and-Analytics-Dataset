import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv("Dataset.csv")

# Display the dimensions (rows, columns) of the DataFrame
print("\nDimensions of the Dataset:")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

# Display the structure of the DataFrame including data types and non-null counts
print("\nStructure of the Dataset:")
print(df.info())

# Display the names of the attributes (columns)
print("\nAttribute Names:")
print(df.columns.tolist())

# Display the first few rows to show example attribute values
print("\nFirst Few Records (Attribute Values):")
print(df.head())
