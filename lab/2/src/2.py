import numpy as np


def softmax(scores: list[float]) -> list[float]:
    x = np.array(scores)
    exp_x = np.exp(x - np.max(x))
    return np.round(exp_x / np.sum(exp_x), 4).tolist()


if __name__ == "__main__":
    scores = np.array(eval(input()))
    print(softmax(scores))
