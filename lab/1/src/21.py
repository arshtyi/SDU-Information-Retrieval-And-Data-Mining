from collections import Counternumpy
import numpy as np


def confusion_matrix(data):
    arr = np.array(data)
    y_true = arr[:, 0]
    y_pred = arr[:, 1]
    TP = np.sum((y_true == 1) & (y_pred == 1))
    FN = np.sum((y_true == 1) & (y_pred == 0))
    FP = np.sum((y_true == 0) & (y_pred == 1))
    TN = np.sum((y_true == 0) & (y_pred == 0))
    return [[TP, FN], [FP, TN]]


if __name__ == "__main__":
    data = eval(input())
    print(confusion_matrix(data))
