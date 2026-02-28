from sklearn.linear_model import SGDRegressor

from sklearn.datasets import fetch_california_housing

from sklearn.model_selection import train_test_split

X,y = fetch_california_housing(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

sgd_model = SGDRegressor(random_state=42)

print(X.shape)

sgd_model.fit(X_train,y_train)
y_pred = sgd_model.predict(X_test)

print(y_pred)
