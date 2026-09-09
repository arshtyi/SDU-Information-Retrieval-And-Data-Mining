import numpy as np


def l1_regularization_gradient_descent(
    X: np.array, y: np.array, alpha: float = 0.1, learning_rate: float = 0.01, max_iter: int = 1000, tol: float = 1e-4
) -> tuple:
    n_samples, n_features = X.shape
    weights = np.zeros(n_features, dtype=float)
    bias = 0.0
    for _ in range(max_iter):
        y_pred = X @ weights + bias
        error = y_pred - y
        grad_weights = (X.T @ error) / n_samples
        grad_weights += alpha * np.sign(weights)
        grad_bias = np.mean(error)
        old_weights = weights.copy()
        old_bias = bias
        weights -= learning_rate * grad_weights
        bias -= learning_rate * grad_bias
        if np.linalg.norm(weights - old_weights) < tol and abs(bias - old_bias) < tol:
            break
    return [round(w, 3) for w in weights], round(bias, 3)


if __name__ == "__main__":
    X = np.array(eval(input()))
    y = np.array(eval(input()))
    alpha = float(input())
    weights, bias = l1_regularization_gradient_descent(X, y, alpha)
    print(weights, bias)
