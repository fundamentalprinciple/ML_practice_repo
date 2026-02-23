from sklearn.feature_extraction import DictVectorizer

dv = DictVectorizer()
Dict = [{'foo':1,'bar':2},{'foo':3,'bar':1}]
X = dv.fit_transform(Dict)
print(X)
