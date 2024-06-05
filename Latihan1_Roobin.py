import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('Data_Roobin.csv')

# Menampilkan 5 baris pertama data
print("5 Baris Pertama Data:")
print(data.head())

# Info singkat tentang data
print("\nInfo Data:")
print(data.info())

# Statistik deskriptif
print("\nStatistik Deskriptif:")
print(data.describe())

# Handling missing values (mengganti nilai yang hilang dengan mean)
# Kita asumsikan kolom yang bisa memiliki nilai hilang adalah 'salary' dan 'rating'
data['salary'].fillna(data['salary'].mean(), inplace=True)
data['rating'].fillna(data['rating'].mean(), inplace=True)

# Membuat scatter plot antara age dan salary
plt.figure(figsize=(10, 6))
plt.scatter(data['age'], data['salary'], color='blue')
plt.title('Scatter Plot Age vs Salary')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.grid(True)
plt.show()

# Membuat box plot untuk kolom salary
plt.figure(figsize=(10, 6))
plt.boxplot(data['salary'], vert=False, patch_artist=True)
plt.title('Box Plot Salary')
plt.xlabel('Salary')
plt.grid(True)
plt.show()

# Membuat box plot untuk kolom rating
plt.figure(figsize=(10, 6))
plt.boxplot(data['rating'], vert=False, patch_artist=True)
plt.title('Box Plot Rating')
plt.xlabel('Rating')
plt.grid(True)
plt.show()

# Menyimpan data setelah preprocessing
data.to_csv('Data_Roobin_preprocessed.csv', index=False)
print("\nData setelah preprocessing telah disimpan ke 'Data_Roobin_preprocessed.csv'")
