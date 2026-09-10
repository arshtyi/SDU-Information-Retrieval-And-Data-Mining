import numpy as np


def compute_qkv(X, W_q, W_k, W_v):
    return np.dot(X, W_q), np.dot(X, W_k), np.dot(X, W_v)


def self_attention(Q, K, V):
    d_k = Q.shape[-1]
    scores = np.dot(Q, K.T) / np.sqrt(d_k)
    exp_scores = np.exp(scores - np.max(scores, axis=-1, keepdims=True))
    attention_weights = exp_scores / np.sum(exp_scores, axis=-1, keepdims=True)
    return np.dot(attention_weights, V)


if __name__ == "__main__":
    X = np.array(eval(input()))
    W_q = np.array(eval(input()))
    W_k = np.array(eval(input()))
    W_v = np.array(eval(input()))
    Q, K, V = compute_qkv(X, W_q, W_k, W_v)
    print(self_attention(Q, K, V))
