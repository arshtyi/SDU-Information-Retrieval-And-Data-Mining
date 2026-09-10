import numpy as np


def pos_encoding(position: int, d_model: int):
    pos = np.arange(position)[:, np.newaxis]
    div_term = np.exp(np.arange(0, d_model, 2) * (-np.log(10000.0) / d_model))
    pe = np.zeros((position, d_model))
    pe[:, 0::2] = np.sin(pos * div_term)
    pe[:, 1::2] = np.cos(pos * div_term[: d_model // 2])
    return pe


if __name__ == "__main__":
    position, d_model = map(int, input().split())
    print(pos_encoding(position, d_model).tolist())
