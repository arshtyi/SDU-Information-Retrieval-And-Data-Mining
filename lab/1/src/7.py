import numpy as np


def shuffle_data(X, y, seed=None):
    if seed:
        np.random.seed(seed)
    indices = list(range(len(X)))
    np.random.shuffle(indices)
    X = X[indices]
    y = y[indices]
    return X, y


if __name__ == "__main__":
    X = np.array(eval(input()))
    y = np.array(eval(input()))
    print(shuffle_data(X, y, 42))
