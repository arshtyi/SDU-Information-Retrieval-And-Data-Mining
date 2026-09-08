import numpy as np


def dice_score(y_true, y_pred):
    return round(2 * np.logical_and(y_pred, y_true).sum() / (y_true.sum() + y_pred.sum()), 3)


if __name__ == "__main__":
    y_true = np.array(eval(input()))
    y_pred = np.array(eval(input()))
    print(f"{dice_score(y_true, y_pred):.3f}")
