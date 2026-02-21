#loader
from sklearn.datasets import load_iris

X,y = load_iris(return_X_y=True)
#X,y=dataset.data,dataset.target

#print(X,y)


#fetcher
from sklearn.datasets import fetch_california_housing

dataset = fetch_california_housing()
X,y=dataset.data,dataset.target
#print(X,y)

#generator
from sklearn.datasets import make_regression

X,y = make_regression(n_samples=100, n_features=5)
#print(X,y)


