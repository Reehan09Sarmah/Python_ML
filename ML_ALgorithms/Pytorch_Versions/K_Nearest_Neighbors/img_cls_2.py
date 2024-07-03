import numpy as np
from torch.utils.data import DataLoader
from collections import Counter
from torchvision import datasets, transforms


class KNN:
    def __init__(self, k=3):
        self.k = k
        self.X_train = None
        self.y_train = None

    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    def predict(self, X_test):
        predictions = [self.predict_image(x) for x in X_test]
        return np.array(predictions)

    def predict_image(self, x):
        # calculate Euclidean distance to all points
        distances = [np.linalg.norm(x-x_train) for x_train in self.X_train]

        # get the top k nearest points indices
        k_nearest_indices = np.argsort(distances)[:self.k]

        # get the labels of these k nearest points
        k_nearest_labels = [self.y_train[i] for i in k_nearest_indices]

        # Majority count to predict the class
        label_counts = {}
        for label in k_nearest_labels:
            label_counts[label] = label_counts.get(label, 0) + 1

        max_label = max(label_counts, key=label_counts.get)
        return max_label


# Load MNIST dataset using DataLoader
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))])

mnist_train_dataset = datasets.MNIST(root='./data', train=True, transform=transform, download=True)
mnist_test_dataset = datasets.MNIST(root='./data', train=False, transform=transform, download=True)

train_loader = DataLoader(dataset=mnist_train_dataset, batch_size=len(mnist_train_dataset), shuffle=True)
test_loader = DataLoader(dataset=mnist_test_dataset, batch_size=len(mnist_test_dataset), shuffle=False)


# Extract data and labels from the DataLoader
X_train, y_train = next(iter(train_loader))
X_train = X_train.view(len(mnist_train_dataset), -1).numpy()
y_train = y_train.numpy()
X_train_subset = X_train[0:10000, :]
y_train_subset = y_train[0:10000]

print(X_train_subset.shape, y_train_subset.shape)

X_test, y_test = next(iter(test_loader))
X_test = X_test.view(len(mnist_test_dataset), -1).numpy()
y_test = y_test.numpy()
y_test_subset = y_test[0:5000]
X_test_subset = X_test[0:5000, :]

print(X_test_subset.shape, y_test_subset.shape)

# Initialize and Fit the dataset into the model
knn_model = KNN(2)
knn_model.fit(X_train_subset, y_train_subset)
print("Done fitting")

# Make Predictions
predictions = knn_model.predict(X_test_subset)
print("Done predicting")

# Evaluate accuracy
accuracy = np.mean(predictions == y_test_subset)
print(f'Test Accuracy: {accuracy * 100:.2f}%')

# Test a single image
print("Testing a single image")
input_image = X_test[9234, :]
label_image = y_test[9234]

print(input_image.shape)
print(f"Actual Label: {label_image}")
print(f"Predicted Label: {knn_model.predict_image(input_image)}")