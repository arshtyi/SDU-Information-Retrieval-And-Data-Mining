import json
import math

import numpy as np

data = json.loads(input())
x = np.array(data["x"], dtype=float)
mu = np.array(data["mu"], dtype=float)
sigma = np.array(data["sigma"], dtype=float)
d = len(x)
diff = x - mu
det_sigma = np.linalg.det(sigma)
inv_sigma = np.linalg.inv(sigma)
exponent = -0.5 * (diff.T @ inv_sigma @ diff)
coefficient = 1 / math.sqrt(((2 * math.pi) ** d) * det_sigma)
result = coefficient * math.exp(exponent)
print(round(float(result), 2))
