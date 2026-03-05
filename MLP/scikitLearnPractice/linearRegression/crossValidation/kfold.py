from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score

X,y = load_iris(return_X_y=True)
lr_model = LinearRegression()
score = cross_val_score(lr_model, X, y, cv=5)
print(score)
