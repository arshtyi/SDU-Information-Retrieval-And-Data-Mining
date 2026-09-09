import numpy as np
from itertools import combinations_with_replacement


def polynomial_features(X, degree):
    n_samples, n_features = X.shape
    combinations = []
    for d in range(degree + 1):
        combinations.extend(combinations_with_replacement(range(n_features), d))
    X_new = np.empty((n_samples, len(combinations)))
    for i, combination in enumerate(combinations):
        if len(combination) == 0:
            X_new[:, i] = 1
        else:
            X_new[:, i] = np.prod(X[:, combination], axis=1)
    return X_new


if __name__ == "__main__":
    X = np.array(eval(input()))
    degree = int(input())
    print(polynomial_features(X, degree))
