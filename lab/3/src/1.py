import numpy as np


def OSA(source: str, target: str) -> int:
    n = len(source)
    m = len(target)
    d = np.zeros((n + 1, m + 1), dtype=int)
    for i in range(n + 1):
        d[i, 0] = i
    for j in range(m + 1):
        d[0, j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = 0 if source[i - 1] == target[j - 1] else 1
            d[i, j] = min(d[i - 1, j] + 1, d[i, j - 1] + 1, d[i - 1, j - 1] + cost)
            if i > 1 and j > 1 and source[i - 1] == target[j - 2] and source[i - 2] == target[j - 1]:
                d[i, j] = min(d[i, j], d[i - 2, j - 2] + 1)
    return int(d[n, m])


if __name__ == "__main__":
    source = eval(input())
    target = eval(input())
    print(OSA(source, target))
