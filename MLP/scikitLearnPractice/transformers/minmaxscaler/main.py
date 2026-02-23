from sklearn.preprocessing import MinMaxScaler

import numpy as np

x = np.array([[15,2,5,-2,-5]]).reshape(5,1)
print(x,x.shape)
mms = MinMaxScaler()
print(mms.fit_transform(x))

