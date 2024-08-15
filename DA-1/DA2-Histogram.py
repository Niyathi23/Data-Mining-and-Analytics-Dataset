import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv('Fuel.csv')

# Create a histogram for fuel price distribution for Delhi
plt.figure(figsize=(10,6))
plt.hist(data['Delhi'], bins=20, alpha=0.5, label='Delhi')
plt.title('Fuel Price Distribution for Delhi')
plt.xlabel('Price (INR/Litre)')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True)
plt.show()

# Create a histogram for fuel price distribution for Bangalore
plt.figure(figsize=(10,6))
plt.hist(data['Bangalore'], bins=20, alpha=0.5, label='Bangalore')
plt.title('Fuel Price Distribution for Bangalore')
plt.xlabel('Price (INR/Litre)')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True)
plt.show()

# Create a histogram for fuel price distribution for Mumbai
plt.figure(figsize=(10,6))
plt.hist(data['Mumbai'], bins=20, alpha=0.5, label='Mumbai')
plt.title('Fuel Price Distribution for Mumbai')
plt.xlabel('Price (INR/Litre)')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True)
plt.show()

# Create a histogram for fuel price distribution for Chennai
plt.figure(figsize=(10,6))
plt.hist(data['Chennai'], bins=20, alpha=0.5, label='Chennai')
plt.title('Fuel Price Distribution for Chennai')
plt.xlabel('Price (INR/Litre)')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True)
plt.show()