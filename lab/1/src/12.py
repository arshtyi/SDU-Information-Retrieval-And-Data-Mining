import numpy as np


def kernel_function(x1, x2):
    return x1 @ x2


if __name__ == "__main__":
    x1 = np.array(eval(input()))
    x2 = np.array(eval(input()))
    print(kernel_function(x1, x2))
