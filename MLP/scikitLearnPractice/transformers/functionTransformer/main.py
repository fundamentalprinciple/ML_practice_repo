from sklearn.preprocessing import FunctionTransformer
import numpy as np

x = np.array([[1,2,3,4],[5,6,7,8]]).reshape(4,2)
print(x)
ft = FunctionTransformer(np.log2)
print(ft.fit_transform(x))
