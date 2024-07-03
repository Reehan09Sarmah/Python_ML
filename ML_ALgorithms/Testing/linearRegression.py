import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../Datasets/test.csv')

# to plot on a graph
# plt.scatter(data.studytime, data.score)
# plt.show()


# this function tells how much off prediction is
def loss_function(w, b, points):
    total_error = 0
    for i in range(len(points)):
        # iloc is a function in pandas --> that helps us to select
        # a specific row or column from the data set.
        x = points.iloc[i].studytime
        y = points.iloc[i].score
        total_error += ((w * x + b) - y) ** 2
    total_error / float(len(points))


def gradient_descent(w_now, b_now, points, a):
    w_derivative = 0.0
    b_derivative = 0.0

    n = len(points)

    for i in range(n):
        x = points.iloc[i].studytime
        y = points.iloc[i].score

        w_derivative += x * ((w_now * x + b_now) - y)
        b_derivative += ((w_now * x + b_now) - y)

    w = w_now - a * (1/n) * w_derivative
    b = b_now - a * (1/n) * b_derivative

    return w, b


w = 0.0
b = 0.0
a = 0.001
epochs = 600  # 600 iterations

for i in range(epochs):
    if i % 100 == 0:
        print(f'Epochs: {i}')
    w, b = gradient_descent(w, b, data, a)


print(w, b)

# Not correct plotting --> maybe fault with range or with algorithm
plt.scatter(data.studytime, data.score, color='black')
plt.plot(list(range(100)), [(w * x + b) for x in range(100)], color='red')
plt.show()


# TRY AGAIN