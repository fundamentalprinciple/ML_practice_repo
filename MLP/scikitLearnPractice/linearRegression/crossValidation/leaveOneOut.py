from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_diabetes
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import LeaveOneOut
from sklearn.model_selection import KFold

X,y = load_diabetes(return_X_y=True)
lr_model = LinearRegression()
kfold_cv = KFold(n_splits=X.shape[0])
scores = cross_val_score(lr_model, X, y, cv=kfold_cv, scoring="neg_mean_squared_error")
print(scores.mean())
