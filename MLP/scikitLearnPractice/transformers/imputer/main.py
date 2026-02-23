import numpy as np

X = np.array([
    [5, 2],
    [np.nan, 3],
    [7, np.nan],
    [6, 4]
])

from sklearn.impute import SimpleImputer
i1 = SimpleImputer(strategy='mean')
print(i1.fit_transform(X))

from sklearn.impute import KNNImputer
i2 = KNNImputer()
print(i2.fit_transform(X))


from sklearn.impute import MissingIndicator
i3 = MissingIndicator()
print(i3.fit_transform(X))


