import numpy as np


def accuracy_score(y_true, y_pred):
    return np.mean(y_pred == y_true)


if __name__ == "__main__":
    y_true = np.array(eval(input()))
    y_pred = np.array(eval(input()))
    print(accuracy_score(y_true, y_pred))
