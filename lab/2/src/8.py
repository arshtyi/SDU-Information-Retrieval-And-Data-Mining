import numpy as np


def generate_data(noise, real):
    return np.array(noise) + np.array(real)


if __name__ == "__main__":
    np.random.seed(42)
    n, d = map(int, input().split())
    noise = [list(map(float, input().split())) for _ in range(n)]
    real_data = [list(map(float, input().split())) for _ in range(n)]
    data = generate_data(noise, real_data)
    for row in data:
        print(" ".join(str(round(row[i], 2)) for i in range(d)))
