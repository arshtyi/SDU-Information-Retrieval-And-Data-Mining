import numpy as np


def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    return np.round((np.linalg.inv(X.T @ X) @ X.T @ y).flatten(), 4).tolist()


if __name__ == "__main__":
    import ast

    x = np.array(ast.literal_eval(input()))
    y = np.array(ast.literal_eval(input())).reshape(-1, 1)

    # Perform linear regression
    coefficients = linear_regression_normal_equation(x, y)

    # Print the coefficients
    print(coefficients)
