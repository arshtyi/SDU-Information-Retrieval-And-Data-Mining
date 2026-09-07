import numpy as np


def batch_iterator(X, y=None, batch_size=64):
    batches = []
    for i in range(0, len(X), batch_size):
        X_batch = X[i : i + batch_size]
        if y is None:
            batches.append(X_batch)
        else:
            y_batch = y[i : i + batch_size]
            batches.append([X_batch, y_batch])
    return batches


if __name__ == "__main__":
    X = np.array(eval(input()))
    y = np.array(eval(input()))
    batch_size = int(input())
    print(batch_iterator(X, y, batch_size))
