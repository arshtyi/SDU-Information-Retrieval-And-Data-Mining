import numpy as np


def rmse(y_true, y_pred):
    return round(np.sqrt(np.mean((y_true - y_pred) ** 2)), 3)


if __name__ == "__main__":
    y_true = np.array(eval(input()))
    y_pred = np.array(eval(input()))
    print(f"{rmse(y_true, y_pred):.3f}")
