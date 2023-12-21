import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

from part_1 import data

#Dataset
x = data.experience_level
x = pd.get_dummies(data=x, drop_first = True) #Categorical data to numerical
y = data.salary_in_usd

#Split the dataset from training and testing, with a 20% split of testing for a 80%
x_train, x_test, y_train, y_test = train_test_split(x, y,test_size = 0.2, random_state = 1)

#Regression line model using the LinearRegression() function
re=LinearRegression()
re.fit(x_train, y_train)

#creating and predicting the y-variable data
y_pred = re.predict(x_test)
print(y_pred)

print(re.score(x_test, y_test))