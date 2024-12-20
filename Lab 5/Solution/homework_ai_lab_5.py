# -*- coding: utf-8 -*-
"""Homework AI Lab 5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UyelAEv98NT83I4MMVS36JoK0wcSLuvo
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file_path = './heart_attack_prediction_dataset.csv'
df = pd.read_csv(file_path)

print("First 5 rows of the dataset:")
print(df.head())

print("\nBasic Info:")
print(df.info())

print("\nMissing values in the dataset:")
print(df.isnull().sum())



# Show column names
print("\nColumns in the dataset:")
print(df.columns)

# Histogram of a few important columns
important_columns = df.columns[:5]  # Change the number according to your dataset

df[important_columns].hist(bins=15, figsize=(10, 8), layout=(3, 2))
plt.tight_layout()
plt.show()

# Scatter plot matrix for selected columns
from pandas.plotting import scatter_matrix
scatter_matrix(df[important_columns], figsize=(10, 8), diagonal='kde')
plt.show()

# Checking for outliers using boxplots
df[important_columns].plot(kind='box', subplots=True, layout=(3,2), figsize=(10,8), sharex=False, sharey=False)
plt.tight_layout()
plt.show()

# Applying NumPy functions - calculating mean, median, and standard deviation
print("\nMean of Income column:")
print(np.mean(df['Income']))

print("\nMedian of Income column:")
print(np.median(df['Income']))

print("\nStandard deviation of Income column:")
print(np.std(df['Income']))