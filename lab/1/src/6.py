import random

import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

iris = load_iris()
X = iris.data
y = iris.target

n = int(input())

random.seed(42)

indices = list(range(len(X)))
random.shuffle(indices)
X = X[indices]
y = y[indices]

X_train = X[:-n]
y_train = y[:-n]
X_test = X[-n:]
y_test = y[-n:]

model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)

for i in range(len(y_pred)):
    print(f"{iris.target_names[y_pred[i]]} {np.max(y_prob[i]):.2f}")
