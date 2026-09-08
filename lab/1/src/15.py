import numpy as np


def f_score(y_true, y_pred, beta):
    tp = np.sum((y_pred == 1) & (y_true == 1))
    fp = np.sum((y_true == 0) & (y_pred == 1))
    fn = np.sum((y_true == 1) & (y_pred == 0))
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    if precision + recall == 0:
        return 0.0
    f_score = (1 + beta**2) * (precision * recall) / ((beta**2) * precision + recall)
    return round(f_score, 3)


if __name__ == "__main__":
    y_true = np.array(eval(input()))
    y_pred = np.array(eval(input()))
    beta = float(input())
    print(f"{f_score(y_true, y_pred, beta):.3f}")
