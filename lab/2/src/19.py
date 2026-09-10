import numpy as np


def sgdm_linear_regression(X, y, learning_rate, momentum_decay, epochs):
    m, n = X.shape
    theta = np.zeros((n, 1))
    v = np.zeros((n, 1))
    for _ in range(epochs):
        y_pred = X @ theta
        gradient = X.T @ (y_pred - y) / m
        v = momentum_decay * v + learning_rate * gradient
        theta -= v
    return np.round(theta.flatten(), 2).tolist()


if __name__ == "__main__":
    m, n = map(int, input().split())
    epochs = int(input())
    X = np.array([list(map(float, input().split())) for _ in range(m)])
    y = np.array(list(map(float, input().split()))).reshape(-1, 1)
    learning_rate, momentum_decay = map(float, input().split())
    theta = sgdm_linear_regression(X, y, learning_rate, momentum_decay, epochs)
    print(" ".join(map(str, np.round(theta, 2))))
