import numpy as np


def gini_impurity(y: list[int]) -> float:
    y = np.array(y)
    total_count = len(y)
    if total_count == 0:
        return 0.0
    _, counts = np.unique(y, return_counts=True)
    return round(1.0 - np.sum((counts / total_count) ** 2), 3)


if __name__ == "__main__":
    y = eval(input())
    print(f"{gini_impurity(y):.3f}")
