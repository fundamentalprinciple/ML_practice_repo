import torch
from torch.utils.data import TensorDataset
from torch.utils.data import DataLoader

X = torch.arange(0,1,0.02).unsqueeze(dim=1)
#print(x, x.shape)

w = 0.7
b = 0.3

Y = 0.7*X + b
#print(y)

train_split = int(0.8*len(X))
X_train = X[:train_split]
Y_train = Y[:train_split]

X_test = X[train_split:]
Y_test = Y[train_split:]

train_dataset = TensorDataset(X_train, Y_train)
test_dataset = TensorDataset(X_test, Y_test)

#print(X_train[6],Y_train[6])
#print(train_dataset[6])

batch_size = 8
num_workers = 0

'''
A FAILED ATTEMPT TO ESTIMATE W WITH LINEAR ALGEBRA

XXT_P = torch.linalg.pinv(torch.matmul(X_train,torch.transpose(X_train,0,1)))
XXT_PX = torch.matmul(torch.transpose(X_train,0,1),XXT_P)
print(XXT_PX.shape)
W = torch.matmul(XXT_PX, Y_train)
print(W,W.shape)
'''

train_loader = DataLoader(
    train_dataset,
    batch_size = batch_size,
    shuffle = True,
    num_workers = num_workers
)

test_loader = DataLoader(
    test_dataset,
    batch_size = batch_size,
    shuffle = False,
    num_workers = num_workers
)

for batch_X, batch_Y in train_loader:
    print(batch_X.shape)
    print(batch_Y.shape)
    break    

#print(test_dataset[0:])

for batch_X, batch_Y in test_loader:
    print(batch_X.shape)
    print(batch_Y.shape)
    #print(batch_X)
    #print(batch_Y)
        






