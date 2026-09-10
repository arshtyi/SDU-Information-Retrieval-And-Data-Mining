import numpy as np

m, n = map(int, input().split())
image = np.array([list(map(int, input().split())) for _ in range(m)], dtype=float)
k = int(input())
kernel = np.array([list(map(float, input().split())) for _ in range(k)], dtype=float)
r = k // 2
padded = np.pad(image, pad_width=r, mode="constant", constant_values=0)
result = np.zeros((m, n), dtype=float)
for i in range(m):
    for j in range(n):
        region = padded[i : i + k, j : j + k]
        result[i, j] = np.sum(region * kernel)
for row in result:
    print(*[round(x, 2) for x in row])
