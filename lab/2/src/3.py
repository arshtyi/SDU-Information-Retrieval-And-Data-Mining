import numpy as np


def single_neuron_model(features, labels, weights, bias):
    z = np.dot(features, weights) + bias
    probabilities = 1 / (1 + np.exp(-z))
    mse = np.mean((probabilities - labels) ** 2)
    return np.round(probabilities, 4).tolist(), round(float(mse), 4)


if __name__ == "__main__":
    features = np.array(eval(input()))
    labels = np.array(eval(input()))
    weights = np.array(eval(input()))
    bias = float(input())
    print(single_neuron_model(features, labels, weights, bias))
