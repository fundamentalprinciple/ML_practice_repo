from sklearn.linear_model import LogisticRegression

import numpy as np

X = np.array([[1,2],[3,4]])
Y = np.array([0,1])

print(X.shape,Y.shape)

model = LogisticRegression(C=0.5)
model.fit(X, Y)
print(model.coef_)
print(model.intercept_)
print(model.C)

