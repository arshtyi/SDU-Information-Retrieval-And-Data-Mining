import numpy as np


def adam_optimizer(f, grad, x0, learning_rate=0.001, beta1=0.9, beta2=0.999, epsilon=1e-8, num_iterations=10):
    x = np.array(x0, dtype=float, copy=True)
    m = np.zeros_like(x)
    v = np.zeros_like(x)
    for t in range(1, num_iterations + 1):
        g = grad(x)
        m = beta1 * m + (1 - beta1) * g
        v = beta2 * v + (1 - beta2) * (g**2)
        m_hat = m / (1 - beta1**t)
        v_hat = v / (1 - beta2**t)
        x -= learning_rate * m_hat / (np.sqrt(v_hat) + epsilon)
    return x


if __name__ == "__main__":
    import numpy as np

    def objective_function(x):
        return x[0] ** 2 + x[1] ** 2

    def gradient(x):
        return np.array([2 * x[0], 2 * x[1]])

    x0 = np.array(eval(input()))
    print(adam_optimizer(objective_function, gradient, x0))
