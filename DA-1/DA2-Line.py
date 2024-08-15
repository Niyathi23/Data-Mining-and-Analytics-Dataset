import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv('Fuel.csv')

# Create a line chart for fuel prices for Delhi
plt.figure(figsize=(10,6))
plt.plot(data['Year'], data['Delhi'], label='Delhi')
plt.title('Fuel Price Trend for Delhi')
plt.xlabel('Year')
plt.ylabel('Price (INR/Litre)')
plt.legend()
plt.grid(True)
plt.show()

# Create a line chart for fuel prices for Bangalore
plt.figure(figsize=(10,6))
plt.plot(data['Year'], data['Bangalore'], label='Bangalore')
plt.title('Fuel Price Trend for Bangalore')
plt.xlabel('Year')
plt.ylabel('Price (INR/Litre)')
plt.legend()
plt.grid(True)
plt.show()

# Create a line chart for fuel prices for Mumbai
plt.figure(figsize=(10,6))
plt.plot(data['Year'], data['Mumbai'], label='Mumbai')
plt.title('Fuel Price Trend for Mumbai')
plt.xlabel('Year')
plt.ylabel('Price (INR/Litre)')
plt.legend()
plt.grid(True)
plt.show()

# Create a line chart for fuel prices for Chennai
plt.figure(figsize=(10,6))
plt.plot(data['Year'], data['Chennai'], label='Chennai')
plt.title('Fuel Price Trend for Chennai')
plt.xlabel('Year')
plt.ylabel('Price (INR/Litre)')
plt.legend()
plt.grid(True)
plt.show()