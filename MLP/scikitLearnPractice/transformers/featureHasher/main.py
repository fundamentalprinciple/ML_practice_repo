from sklearn.feature_extraction import FeatureHasher

data = [
    {'age': 4, 'height': 96},
    {'age': 1, 'height': 73.9},
    {'age': 3, 'height': 85},
    {'age': 2, 'height': 60}
]

hasher = FeatureHasher(n_features=4, input_type='dict')
X = hasher.fit_transform(data)

print(X.toarray())
