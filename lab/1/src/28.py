import numpy as np


def divide_on_feature(X, feature_i, threshold):
    if isinstance(threshold, (int, float, np.number)):
        mask = X[:, feature_i] >= threshold
    else:
        mask = X[:, feature_i] == threshold
    X1 = X[mask]
    X2 = X[~mask]
    return [X1, X2]


if __name__ == "__main__":
    X = np.array(eval(input()))
    feature_i = int(input())
    threshold = eval(input())
    print(divide_on_feature(X, feature_i, threshold))
