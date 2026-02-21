import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[1,2],
              [2,3],
              [3,4]])

Y = np.array([3,5,7])

model = LinearRegression()
model.fit(X,Y)

print(model.coef_)

