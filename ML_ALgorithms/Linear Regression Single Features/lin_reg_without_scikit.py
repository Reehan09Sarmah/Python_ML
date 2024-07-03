from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Linear Regression Class
class LR:
    def __init__(self):
        self.w = None
        self.b = None

    def fit(self, X_train, y_train):
        numerator = 0
        denominator = 0

        for i in range(X_train.shape[0]):
            # These equations come after you minimize the cost function w.r.t 'w' and 'b'. Check copy
            numerator = numerator + ((y_train[i] - y_train.mean()) * (X_train[i] - X_train.mean()))
            denominator = denominator + ((X_train[i] - X_train.mean()) * (X_train[i] - X_train.mean()))

        self.w = numerator / denominator
        self.b = y_train.mean() - (self.w * X_train.mean())
        print(f"w: {self.w}")
        print(f"b: {self.b}")

    def predict(self, X_test):
        return self.w * X_test + self.b

    def mean_squared_error(self, y_true, y_pred):
        n_samples = len(y_true)
        mse = ((y_true - y_pred) ** 2).sum() / n_samples
        return mse

    def r2_score(self, y_true, y_pred):
        # Calculate the mean of the true target values
        y_mean = np.mean(y_true)

        # Calculate the total sum of squares (TSS)
        tss = np.sum((y_true - y_mean) ** 2)

        # Calculate the residual sum of squares (RSS)
        rss = np.sum((y_true - y_pred) ** 2)

        # Calculate R-squared (R2) score
        r2 = 1 - (rss / tss)

        return r2


data = pd.read_csv("canada_per_capita_income.csv")
X = data.iloc[:, 0].values
y = data.iloc[:, 1].values
# Create a linear regression object
reg = LR()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=2)
reg.fit(X_train, y_train)
y_pred = reg.predict(X_test)
acc = reg.r2_score(y_test, y_pred)
print(f"R2 score: {acc}")

# Let's plot the data along with the linear regression model
plt.xlabel('year', fontsize=20)
plt.ylabel('per capita income (US$)', fontsize=20)
plt.scatter(data.year, data.per_capita_income, color='red', marker='+')
plt.plot(data.year, reg.predict(data[['year']]), color='blue')
plt.show()