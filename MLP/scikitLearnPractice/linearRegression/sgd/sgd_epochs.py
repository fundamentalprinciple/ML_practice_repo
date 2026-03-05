from sklearn.linear_model import SGDRegressor
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import numpy as np

X,y = fetch_california_housing(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

print(X_train.shape[0])
max_iter = np.ceil(1e+6/X_train.shape[0])
print(max_iter)

sgd = Pipeline([
            ('scaler', StandardScaler()),
            ('model', SGDRegressor(max_iter=int(max_iter), random_state=42, shuffle=True))
            ])

sgd.fit(X_train,y_train)
y_pred = sgd.predict(X_test)
print(mean_squared_error(y_pred,y_test))
