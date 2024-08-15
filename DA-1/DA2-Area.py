import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv('Fuel.csv')

# Create an area diagram for fuel price trends for Delhi
plt.figure(figsize=(10,6))
plt.plot(data['Year'], data['Delhi'], label='Delhi')
plt.fill_between(data['Year'], data['Delhi'], alpha=0.3)
plt.title('Fuel Price Trends for Delhi')
plt.xlabel('Year')
plt.ylabel('Price (INR/Litre)')
plt.legend()
plt.grid(True)
plt.show()

# Create an area diagram for fuel price trends for Bangalore
plt.figure(figsize=(10,6))
plt.plot(data['Year'], data['Bangalore'], label='Bangalore')
plt.fill_between(data['Year'], data['Bangalore'], alpha=0.3)
plt.title('Fuel Price Trends for Kolkata')
plt.xlabel('Year')
plt.ylabel('Price (INR/Litre)')
plt.legend()
plt.grid(True)
plt.show()

# Create an area diagram for fuel price trends for Mumbai
plt.figure(figsize=(10,6))
plt.plot(data['Year'], data['Mumbai'], label='Mumbai')
plt.fill_between(data['Year'], data['Mumbai'], alpha=0.3)
plt.title('Fuel Price Trends for Mumbai')
plt.xlabel('Year')
plt.ylabel('Price (INR/Litre)')
plt.legend()
plt.grid(True)
plt.show()

# Create an area diagram for fuel price trends for Chennai
plt.figure(figsize=(10,6))
plt.plot(data['Year'], data['Chennai'], label='Chennai')
plt.fill_between(data['Year'], data['Chennai'], alpha=0.3)
plt.title('Fuel Price Trends for Chennai')
plt.xlabel('Year')
plt.ylabel('Price (INR/Litre)')
plt.legend()
plt.grid(True)
plt.show()