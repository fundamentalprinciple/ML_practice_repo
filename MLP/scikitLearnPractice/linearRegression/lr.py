from sklearn.linear_model import LinearRegression

from sklearn.datasets import load_iris

from sklearn.model_selection import train_test_split

from sklearn.metrics import mean_squared_error

X,y = load_iris(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)

print(X.shape,X_train.shape,X_test.shape)

lr_model = LinearRegression()
lr_model.fit(X_train,y_train)
y_pred = lr_model.predict(X_test)
mse = mean_squared_error(y_test,y_pred)
print(mse)

