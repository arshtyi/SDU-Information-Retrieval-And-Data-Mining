import sys
import numpy as np
from scipy.stats import multivariate_normal


def e_step(X, pi, mu, sigma):
    N = X.shape[0]
    K = len(pi)
    gamma = np.zeros((N, K))
    for k in range(K):
        rv = multivariate_normal(mean=mu[k], cov=sigma[k], allow_singular=True)
        gamma[:, k] = pi[k] * rv.pdf(X)
    gamma_sum = np.sum(gamma, axis=1, keepdims=True)
    gamma = gamma / (gamma_sum + 1e-300)
    gamma += 1e-6
    return gamma


def m_step(X, gamma):
    N, D = X.shape
    K = gamma.shape[1]
    Nk = np.sum(gamma, axis=0)
    pi = Nk / N
    mu = np.zeros((K, D))
    for k in range(K):
        mu[k] = np.sum(gamma[:, k, None] * X, axis=0) / Nk[k]
    sigma = np.zeros((K, D, D))
    for k in range(K):
        diff = X - mu[k]
        sigma[k] = ((gamma[:, k, None] * diff).T @ diff) / Nk[k]
    return pi, mu, sigma


def assign_labels(X, pi, mu, sigma):
    N = X.shape[0]
    K = len(pi)
    probability = np.zeros((N, K))
    for k in range(K):
        rv = multivariate_normal(mean=mu[k], cov=sigma[k], allow_singular=True)
        probability[:, k] = pi[k] * rv.pdf(X)
    return np.argmax(probability, axis=1)


def main():
    np.random.seed(0)
    N = int(sys.stdin.readline())
    X = np.array([list(map(float, sys.stdin.readline().split())) for _ in range(N)])
    K, T = map(int, sys.stdin.readline().split())
    D = 2
    indices = np.random.choice(N, K, replace=False)
    mu = X[indices].copy()
    sigma = np.array([np.eye(D) for _ in range(K)])
    pi = np.ones(K) / K
    for _ in range(T):
        gamma = e_step(X, pi, mu, sigma)
        pi, mu, sigma = m_step(X, gamma)
    labels = assign_labels(X, pi, mu, sigma)
    for label in labels:
        print(label)


if __name__ == "__main__":
    main()
