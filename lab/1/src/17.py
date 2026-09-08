import numpy as np


def r_squared(y_true, y_pred):
    """
    Calculate the R-squared (RÂ²) coefficient of determination.

    Args:
        y_true (numpy.ndarray): Array of true values
        y_pred (numpy.ndarray): Array of predicted values

    Returns:
        float: R-squared value rounded to 3 decimal places
    """
    return round(1.0 - np.sum((y_true - y_pred) ** 2) / np.sum((y_true - np.mean(y_true)) ** 2), 3)


if __name__ == "__main__":
    y_true = np.array(eval(input()))
    y_pred = np.array(eval(input()))
    print(f"{r_squared(y_true, y_pred):.3f}")
