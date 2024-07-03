import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from word2number import w2n
import math
from sklearn.metrics import r2_score

data = pd.read_csv("hiring.csv")

# Data preprocessing --> Fill up missing data points, filling NaN points
data.experience = data.experience.fillna('zero')

# taking median of other values to fill the NaN (missing) value of test_score column
median_test_score = math.floor(data.test_score.median())
data.test_score = data.test_score.fillna(median_test_score)

# converting string to number --> experience column
data.experience = data.experience.apply(w2n.word_to_num)

# Create the model
reg = linear_model.LinearRegression()
reg.fit(data[['experience', 'test_score', 'interview_score']], data.salary)

# print the parameters chosen in mode
print("Parameters:")
print(f"[w1 w2 w3]: {reg.coef_}")
print(f"b: {reg.intercept_}")
# predict [2 years, 9 test score, 6 interview score] & [12 years, 10 test, 10 interview]
print(f"Salary for 2 years, 9 test score, 6 interview score: ${reg.predict([[2,9,6]])[0]}")
print(f"Salary for 12 years, 10 test score, 10 interview score: ${reg.predict([[12,10,10]])[0]}")

# Plot the graph
plt.xlabel('Experience', fontsize=20)
plt.ylabel('Salary(US$)', fontsize=20)
plt.scatter(data.experience, data.salary, color='red', marker='X')
# plot the model against 1st feature = experience
plt.plot(data.experience, reg.predict(data[['experience', 'test_score', 'interview_score']]), color='blue')
plt.show()