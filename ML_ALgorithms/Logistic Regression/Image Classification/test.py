import torch

# Example data
y_pred = torch.tensor([[0.2, 0.5, 0.3], [0.7, 0.1, 0.2], [0.4, 0.4, 0.2]])
y_true = torch.tensor([1, 0, 2])

# Gather predicted probabilities for the true classes
selected_probabilities = y_pred.gather(1, y_true.view(-1, 1))

print(y_true.view(-1, 1))
print(selected_probabilities)
