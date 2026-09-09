import numpy as np


def gradient_descent(X, y, weights, learning_rate, n_iterations, batch_size=1, method="batch"):
    m = X.shape[0]
    for _ in range(n_iterations):
        if method == "batch":
            y_pred = X @ weights
            gradient = (2 / m) * X.T @ (y_pred - y)
            weights = weights - learning_rate * gradient
        elif method == "stochastic":
            for i in range(m):
                X_i = X[i]
                y_i = y[i]
                y_pred = X_i @ weights
                gradient = 2 * X_i * (y_pred - y_i)
                weights = weights - learning_rate * gradient
        elif method == "mini_batch":
            for start in range(0, m, batch_size):
                end = min(start + batch_size, m)
                X_batch = X[start:end]
                y_batch = y[start:end]
                y_pred = X_batch @ weights
                batch_m = len(X_batch)
                gradient = (2 / batch_m) * X_batch.T @ (y_pred - y_batch)
                weights = weights - learning_rate * gradient
    return weights


if __name__ == "__main__":
    X = np.array(eval(input()))
    y = np.array(eval(input()))
    weights = np.array(eval(input()))
    learning_rate = eval(input())
    n_iterations = eval(input())
    batch_size = eval(input())
    method = eval(input())
    print(gradient_descent(X, y, weights, learning_rate, n_iterations, batch_size, method))
