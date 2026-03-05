from sklearn.linear_model import SGDRegressor
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

X,y = fetch_california_housing(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

sgd = Pipeline([
            ('scaler', StandardScaler()),
            ('model', SGDRegressor(random_state=42, shuffle=True, max_iter=500, tol=1e-3, n_iter_no_change=5, validation_fraction=0.2))
            ])

sgd.fit(X_train,y_train)
y_pred = sgd.predict(X_test)
print(mean_squared_error(y_pred,y_test))
