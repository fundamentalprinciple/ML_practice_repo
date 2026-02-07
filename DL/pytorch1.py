import torch

import numpy as np
import matplotlib.pyplot as plt
import matplotlib

'''
print(np.__version__)

t = torch.tensor(7)
print(t)
print(type(t))

a = torch.tensor([1,2], dtype=torch.int64)
print(a)
print(a.type)
print(a.element_size())

np_arr = np.array([[1,2,3],[4,5,6]])
print(np_arr)
t = torch.from_numpy(np_arr)
print(np_arr.dtype)

np_arr[0,0] = 100

t = torch.empty(3,3)

t = torch.logspace(1,4,5)

t = torch.eye(2,4)
'''

v = torch.tensor([1,2,3])
t = torch.diag(v)
print(t)



