import numpy as np


def recall(y_true, y_pred):
    return round(np.sum((y_true == 1) & (y_pred == 1)) / np.sum(y_pred == 1), 3)


if __name__ == "__main__":
    y_true = np.array(eval(input()))
    y_pred = np.array(eval(input()))
    print(f"{recall(y_true, y_pred):.3f}")
