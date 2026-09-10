import json
import numpy as np

data = json.loads(input())
train = np.array(data["train"], dtype=float)
test = np.array(data["test"], dtype=float)
X_train = train[:, :-1]
y_train = train[:, -1].astype(int)
classes = np.array([0, 1])
priors = {}
means = {}
variances = {}
for c in classes:
    X_c = X_train[y_train == c]
    priors[c] = len(X_c) / len(X_train)
    means[c] = np.mean(X_c, axis=0)
    var = np.var(X_c, axis=0, ddof=0)
    var = np.where(var == 0, 1e-9, var)
    variances[c] = var
predictions = []
for x in test:
    log_posteriors = []
    for c in classes:
        mu = means[c]
        var = variances[c]
        log_prob = np.log(priors[c])
        log_prob += np.sum(-0.5 * np.log(2 * np.pi * var) - ((x - mu) ** 2) / (2 * var))
        log_posteriors.append(log_prob)
    pred = int(classes[np.argmax(log_posteriors)])
    predictions.append(pred)
print(json.dumps(predictions))
