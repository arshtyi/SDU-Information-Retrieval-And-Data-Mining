import numpy as np


def log_softmax(scores: list) -> np.ndarray:
    scores = np.array(scores)
    c = np.max(scores, axis=-1, keepdims=True)
    sum_exp = np.sum(np.exp(scores - c), axis=-1, keepdims=True)
    return scores - c - np.log(sum_exp)


if __name__ == "__main__":
    scores = eval(input())
    print(log_softmax(scores))
