import numpy as np


def sigmoid(x):
    return 1.0 / (1 + np.exp(-x))


def discriminator(sample):
    return sigmoid(sample)


if __name__ == "__main__":
    n = int(input())
    real_data = [float(input()) for _ in range(n)]
    generated_data = real_data
    for sample in generated_data:
        print(f"{discriminator(sample):.2f}")
