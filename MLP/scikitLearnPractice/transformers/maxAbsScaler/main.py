from sklearn.preprocessing import MaxAbsScaler
import numpy as np

x = np.array([1,2,3,4,5]).reshape(5,1)
print(x,x.shape)

mas = MaxAbsScaler()
print(mas.fit_transform(x))

