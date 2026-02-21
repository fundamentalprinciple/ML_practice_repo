from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

import numpy as np

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression())
])

X_train = np.array([[1,2],
                    [3,4]])
Y_train = np.array([0,1])

print(pipeline.fit(X_train, Y_train))

print(pipeline.named_steps['model'].coef_)

