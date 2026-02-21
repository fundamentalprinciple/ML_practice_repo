from sklearn.datasets import fetch_openml

dataset = fetch_openml(name="iris",version=1)
X = dataset.data
y = dataset.target
print(X,y)
