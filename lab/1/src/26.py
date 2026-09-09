import numpy as np


def k_nearest_neighbors(X, y, test_sample, k):
    distances = np.sqrt(np.sum((X - test_sample) ** 2, axis=1))
    nearest_indices = np.argsort(distances)[:k]
    nearest_labels = y[nearest_indices]
    labels, counts = np.unique(nearest_labels, return_counts=True)
    return int(labels[np.argmax(counts)])


if __name__ == "__main__":
    m, n = map(int, input().split())
    X = np.array([list(map(float, input().split())) for _ in range(m)])
    y = np.array(list(map(int, input().split())))
    test_sample = np.array(list(map(float, input().split())))
    k = int(input())
    print(k_nearest_neighbors(X, y, test_sample, k))
