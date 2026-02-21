from sklearn.datasets import make_blobs

X,y = make_blobs(
    n_samples=200,
    centers=3
)

print(X)

