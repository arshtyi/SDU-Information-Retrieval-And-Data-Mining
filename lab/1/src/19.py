import numpy as np


def jaccard_index(y_true, y_pred):
    return round(np.logical_and(y_true, y_pred).sum() / np.logical_or(y_true, y_pred).sum(), 3)


if __name__ == "__main__":
    y_true = np.array(eval(input()))
    y_pred = np.array(eval(input()))
    print(f"{jaccard_index(y_true, y_pred):.3f}")
