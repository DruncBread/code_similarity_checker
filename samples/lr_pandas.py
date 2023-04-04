import pandas as pd
import  numpy as np

# Assume we have a dataset with two features and one label stored in a CSV file
df = pd.read_csv("data.csv")

# Split the data into features and labels
X = df[["feature1", "feature2"]]
y = df["label"]

# Initialize the weights and bias
w = np.zeros(X.shape[1])
b = 0

# Define the learning rate
learning_rate = 0.01

# Perform gradient descent to learn the optimal weights and bias
for i in range(1000):
    # Calculate the prediction using the current weights and bias
    y_pred = np.dot(X, w) + b

    # Calculate the error
    error = y - y_pred

    # Calculate the gradient for the weights and bias
    gradient_w = -(2 / X.shape[0]) * np.dot(error, X)
    gradient_b = -(2 / X.shape[0]) * np.sum(error)

    # Update the weights and bias
    w = w - learning_rate * gradient_w
    b = b - learning_rate * gradient_b

# Print the learned weights and bias
print(f"Weights: {w}")
print(f"Bias: {b}")
