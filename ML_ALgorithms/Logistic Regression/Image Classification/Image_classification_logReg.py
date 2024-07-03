import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

class LogisticRegression:
    def __init__(self, input_size, num_classes, learning_rate=0.001):
        self.W = torch.randn(input_size, num_classes, requires_grad=True)
        self.b = torch.zeros(num_classes, requires_grad=True)
        self.learning_rate = learning_rate

    def linear(self, X):
        return torch.matmul(X, self.W) + self.b

    def softmax(self, logits):
        exp_logits = torch.exp(logits)
        return exp_logits / exp_logits.sum(dim=1, keepdim=True)

    def cross_entropy_loss(self, y_pred, y_true):
        predicted_probabilities = y_pred.gather(1, y_true.view(-1, 1))  # collect the values predicted from given possibilities
        loss = -torch.mean(torch.log(predicted_probabilities))  # negative log likelihood loss
        return loss

    def train(self, train_loader, num_epochs=10):
        for epoch in range(num_epochs):
            total_loss = 0.0
            for images, labels in train_loader:
                X = images.view(images.size(0), -1)
                y = labels

                # Forward pass
                logits = self.linear(X)
                y_pred = self.softmax(logits)

                # Compute the loss
                loss = self.cross_entropy_loss(y_pred, y)

                # Backward pass
                loss.backward()

                # Update weights and bias
                with torch.no_grad():
                    self.W -= self.learning_rate * self.W.grad
                    self.b -= self.learning_rate * self.b.grad

                    # Manually zero the gradients after updating
                    self.W.grad.zero_()
                    self.b.grad.zero_()

                total_loss += loss.item()

            average_loss = total_loss / len(train_loader)
            print(f'Epoch {epoch + 1}/{num_epochs}, Average Loss: {average_loss}')

    def evaluate(self, test_loader):
        correct = 0
        total = 0

        with torch.no_grad():
            for images, labels in test_loader:
                X = images.view(images.size(0), -1)
                y_true = labels

                # Forward pass
                logits = self.linear(X)
                y_pred = self.softmax(logits)

                # Predictions
                _, predicted = torch.max(y_pred, 1)

                # Update total and correct predictions
                total += labels.size(0)
                correct += (predicted == labels).sum().item()

        accuracy = correct / total
        print(f'Test Accuracy: {100 * accuracy:.2f}%')


# Load MNIST dataset
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])
mnist_train_dataset = datasets.MNIST(root='./data', train=True, transform=transform, download=True)
mnist_test_dataset = datasets.MNIST(root='./data', train=False, transform=transform, download=True)

train_loader = DataLoader(dataset=mnist_train_dataset, batch_size=64, shuffle=True)
test_loader = DataLoader(dataset=mnist_test_dataset, batch_size=64, shuffle=False)

# Initialize Logistic Regression model
input_size = 28 * 28  # Size of flattened MNIST images
num_classes = 10
logistic_model = LogisticRegression(input_size, num_classes)

# Train the Logistic Regression model
logistic_model.train(train_loader, num_epochs=5)

# Evaluate on the test set
logistic_model.evaluate(test_loader)
