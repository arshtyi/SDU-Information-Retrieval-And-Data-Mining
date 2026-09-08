import numpy as np


def ridge_loss(X, w, y_true, alpha):
    m = X.shape[0]
    y_pred = np.dot(X, w)
    return 0.5 / m * np.sum((y_pred - y_true) ** 2) + 0.5 / m * alpha * np.sum(w**2)


if __name__ == "__main__":
    X = np.array(eval(input()))
    w = np.array(eval(input()))
    y_true = np.array(eval(input()))
    alpha = eval(input())
    print(ridge_loss(X, w, y_true, alpha))
