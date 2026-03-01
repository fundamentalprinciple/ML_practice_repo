from sklearn.linear_model import SGDRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_california_housing
from sklearn.metrics import mean_squared_error

sgd = Pipeline([
                ('feature_scaling', StandardScaler()),
                ('sgd_regressor', SGDRegressor(shuffle=True))
                ])

X,y = fetch_california_housing(return_X_y=True) 

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)

sgd.fit(X_train,y_train)
y_pred = sgd.predict(X_test)
print(mean_squared_error(y_pred, y_test))

