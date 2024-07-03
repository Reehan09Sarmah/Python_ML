import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

data = pd.read_csv("canada_per_capita_income.csv")

# Create a linear regression object
reg = linear_model.LinearRegression()
reg.fit(data[['year']], data.per_capita_income)  # train the data .fit(x,y) --> x= input feature, y = target value

# show the parameters
print(f'w1: {reg.coef_}')  # shows w
print(f'b: {reg.intercept_}')  # shows b


# Let's plot the data along with the linear regression model
plt.xlabel('year', fontsize=20)
plt.ylabel('per capita income (US$)', fontsize=20)
plt.scatter(data.year, data.per_capita_income, color='red', marker='X')
plt.plot(data.year, reg.predict(data[['year']]), color='blue')
plt.show()

# predict the per capita income for the year 2020
print(reg.predict([[2017]]))  # .predict(x) --> x must be a 2D Array