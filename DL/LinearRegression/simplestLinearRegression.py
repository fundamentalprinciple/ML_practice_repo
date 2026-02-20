import torch
from torch.utils.data import TensorDataset
from torch.utils.data import DataLoader

import matplotlib.pyplot as plt

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
    #print(batch_X.shape)
    #print(batch_Y.shape)
    break    

#print(test_dataset[0:])

for batch_X, batch_Y in test_loader:
    #print(batch_X.shape)
    #print(batch_Y.shape)
    #print(batch_X)
    #print(batch_Y)
    break
        
def plot_predictions(
    train_data=X_train,
    train_labels=Y_train,
    test_data=X_test,
    test_labels=Y_test,
    predictions=None
):
    plt.figure(figsize=(10,7))
    plt.scatter(train_data, train_labels,
                c="green",
                s=25,
                alpha=0.8,
                label="Training Data",
                marker="o")    

    plt.scatter(test_data, test_labels,
                c="blue",
                s=25,
                alpha=0.8,
                label="Test Data",
                marker="^")

    if predictions is not None:
        plt.scatter(test_data, predictions,
                    c="red",
                    s=25,
                    alpha=0.8,
                    label="Predictions",
                    marker="X")

    plt.xlabel("X values", fontsize=14)
    plt.ylabel("Y values", fontsize=14)
    plt.title("Linear Regression", fontsize=16, fontweight="bold")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
    return

plot_predictions()


