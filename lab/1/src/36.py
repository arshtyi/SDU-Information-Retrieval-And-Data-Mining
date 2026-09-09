import numpy as np


def pegasos_kernel_svm(data, labels, kernel="linear", lambda_val=0.01, iterations=100, sigma=1.0):
    n_samples = len(data)
    alphas = np.zeros(n_samples, dtype=float)
    b = 0.0
    if kernel == "linear":
        K = data @ data.T
    elif kernel == "rbf":
        diff = data[:, None, :] - data[None, :, :]
        dist_sq = np.sum(diff**2, axis=2)
        K = np.exp(-dist_sq / (2 * sigma**2))
    else:
        raise ValueError("kernel must be 'linear' or 'rbf'")
    for t in range(1, iterations + 1):
        eta = 1.0 / (lambda_val * t)
        for i in range(n_samples):
            decision = np.sum(alphas * labels * K[:, i]) + b
            if labels[i] * decision < 1:
                alphas[i] += eta * (labels[i] - lambda_val * alphas[i])
                b += eta * labels[i]
    return np.round(alphas, 4).tolist(), np.round(b, 4)


if __name__ == "__main__":
    data = np.array(eval(input()))
    labels = np.array(eval(input()))
    kernel = eval(input())
    lambda_val = float(input())
    iterations = int(input())
    sigma = float(input())
    print(pegasos_kernel_svm(data, labels, kernel, lambda_val, iterations, sigma))
