import matplotlib.pyplot as plt

from part_1 import data


# Box Plot for 'salary_in_usd' column
plt.boxplot(data['salary_in_usd'])
plt.title('Box Plot of Salary')
plt.xlabel('Salary')
plt.ylabel('Values')
plt.show()

# Bar Graph for 'job_title' vs 'salary_in_usd'
x = data['job_title']
y = data['salary_in_usd']

plt.bar(x, y, color='red')
plt.title('Bar Graph: Job Title vs Salary')
plt.xlabel('Job Title')
plt.ylabel('Salary')
# Adjust layout for better visualization
plt.tight_layout()
plt.show()

# Histogram for 'salary_in_usd' column
plt.hist(data['salary_in_usd'], bins=30, color='green')  # Adjust bin count and color
plt.title('Histogram of Salary')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.show()

