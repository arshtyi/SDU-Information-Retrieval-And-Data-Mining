import json
import numpy as np

data = json.loads(input())
train = np.array(data["train"], dtype=float)
test = np.array(data["test"], dtype=float)
mu = np.mean(train, axis=0)
Xc = train - mu
n = train.shape[0]
cov = (Xc.T @ Xc) / n
eigenvalues, eigenvectors = np.linalg.eigh(cov)
v = eigenvectors[:, -1]
for value in v:
    if abs(value) > 1e-12:
        if value < 0:
            v = -v
        break
ans = []
for x in test:
    centered = x - mu
    z = centered @ v
    x_hat = mu + z * v
    mse = np.mean((x - x_hat) ** 2)
    ans.append(f"{mse:.2f}")
print(json.dumps(ans))
