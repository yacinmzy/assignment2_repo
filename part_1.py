import pandas as pd

# DataFrame loaded from a CSV file
data = pd.read_csv("ds_salaries.csv")
print(data.head())

# Accessing and printing specific columns/features
print(data.job_title)
print(data['salary_in_usd'])

# Slicing and printing (rows 3 to 11)
print(data.iloc[3:11, :])

# Describing and printing information about the 'salary_in_usd' column/feature
print(data.salary_in_usd.describe())