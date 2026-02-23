from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler

dataset = load_iris()
X = dataset.data
scaler = StandardScaler()
scaler.fit(X)

print(scaler.mean_)

print(X,scaler.transform(X))
