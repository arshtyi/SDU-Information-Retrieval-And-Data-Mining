import numpy as np


def leaky_relu(z, alpha=0.01):
    return np.maximum(alpha * z, z)


if __name__ == "__main__":
    z = eval(input())
    alpha = eval(input())
    print(leaky_relu(z, alpha))
