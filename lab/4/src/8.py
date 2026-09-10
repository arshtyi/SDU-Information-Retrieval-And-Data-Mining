import ast
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

data = ast.literal_eval(input())
data = np.array(data, dtype=object)
X = data[:, :-1]
y = data[:, -1]
encoder_x = LabelEncoder()
X[:, -1] = encoder_x.fit_transform(X[:, -1])
X = X.astype(float)
encoder_y = LabelEncoder()
y = encoder_y.fit_transform(y)
model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)
ans = np.argmax(model.feature_importances_)
print(int(ans))
