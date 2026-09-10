import numpy as np


def train_neuron(features, labels, initial_weights, initial_bias, learning_rate, epochs):
    weights = initial_weights.astype(float)
    bias = initial_bias
    mse_values = []
    for _ in range(epochs):
        z = features @ weights + bias
        predictions = 1 / (1 + np.exp(-z))
        mse = np.mean((predictions - labels) ** 2)
        mse_values.append(round(mse, 4))
        error = predictions - labels
        delta = error * predictions * (1 - predictions)
        n = len(labels)
        weight_gradient = (2 / n) * (features.T @ delta)
        bias_gradient = (2 / n) * np.sum(delta)
        weights -= learning_rate * weight_gradient
        bias -= learning_rate * bias_gradient
    return (np.round(weights, 4).tolist(), round(bias, 4), mse_values)


if __name__ == "__main__":
    features = np.array(eval(input()))
    labels = np.array(eval(input()))
    initial_weights = np.array(eval(input()))
    initial_bias = float(input())
    learning_rate = float(input())
    epochs = int(input())
    print(train_neuron(features, labels, initial_weights, initial_bias, learning_rate, epochs))
