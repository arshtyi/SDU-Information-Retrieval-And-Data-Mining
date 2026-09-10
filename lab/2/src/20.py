import numpy as np


def rmsprop_linear_regression(X, y, learning_rate, decay_rate, epochs):
    m, n = X.shape
    theta = np.zeros((n, 1))
    s = np.zeros((n, 1))
    epsilon = 1e-8
    for _ in range(epochs):
        y_pred = X @ theta
        gradient = (X.T @ (y_pred - y)) / m
        s = decay_rate * s + (1 - decay_rate) * (gradient**2)
        theta -= learning_rate * gradient / (np.sqrt(s) + epsilon)
    return np.round(theta.flatten(), 2).tolist()


if __name__ == "__main__":
    m, n = map(int, input().split())
    epochs = int(input())
    X = np.array([input().split() for _ in range(m)]).astype(float)
    y = np.array(input().split()).astype(float).reshape(-1, 1)
    learning_rate, decay_rate = map(float, input().split())
    theta = rmsprop_linear_regression(X, y, learning_rate, decay_rate, epochs)
    print(" ".join(map(str, np.round(theta, 2))))
