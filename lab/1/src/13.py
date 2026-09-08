import numpy as np


def precision(y_true, y_pred):
    return np.sum((y_true == 1) & (y_pred == 1)) / np.sum(y_pred == 1)


if __name__ == "__main__":
    y_true = np.array(eval(input()))
    y_pred = np.array(eval(input()))
    print(precision(y_true, y_pred))
