from sklearn.datasets import load_iris

data = load_iris()

#print(data, type(data))

X = data.data
y = data.target

print(X,y)

