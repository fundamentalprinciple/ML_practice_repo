import torch
x = torch.arange(0,1,0.02).unsqueeze(dim=1)
#print(x, x.shape)

w = 0.7
b = 0.3

y = 0.7*x + b
print(y)
