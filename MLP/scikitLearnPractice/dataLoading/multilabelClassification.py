from sklearn.datasets import make_multilabel_classification

X,y = make_multilabel_classification(
    n_samples = 100,
    n_features = 10,
    n_classes = 5
)

print(X,y)
