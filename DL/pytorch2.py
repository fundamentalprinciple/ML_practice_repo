import torch
import numpy as np

'''
t = torch.rand(300,400)
print(t)
print(t.shape)
print((torch.min(t),torch.max(t),torch.mean(t),torch.std(t)))
print(f"{torch.min(t):.6f}")
'''

#image-like tensors

'''
t = torch.rand(224,224,3)
print(t)
print(t.shape)
print(t.dtype)
print(t.element_size())
print(t.nelement())
print(t.nelement()*t.element_size())
'''

'''
h, w, shape = t.shape
print(h, w, shape)
pixels = h*w
print(pixels)
'''

'''
t = torch.arange(0,100,2)
print(t)

t = torch.zeros_like(t)
print(t)
print(t.device)
'''

'''
t = torch.tensor([3.0, 6.0, 9.0], requires_grad=False)

t = torch.rand(2,4)
s = torch.rand(4,2)
print(t+10, t-10, t*10)
print(t*t)
print(torch.matmul(t,s))
print(t@s)
'''

'''
t = torch.arange(1,10)
print(t)
print(t.shape)
t = t.reshape(3,3)
print(t)
print(t.shape)
'''

'''
t = torch.arange(1,10)
v = t.view(3,3)
print(v)
'''

'''
t = torch.arange(1,10)
t = t.reshape(3,3)
s = torch.stack([t,t,t,t], dim=0)
print(s)
print(s.shape)
'''

'''
t = torch.arange(1,8).reshape(1,7)
print(t)
print(t.shape)
t = t.squeeze()
print(t)
print(t.shape)
t = t.unsqueeze(0).unsqueeze(0)
print(t)
print(t.shape)
'''

t = torch.arange(1,10).reshape(3,3)
print(t)
t = t.permute(1,0)
print(t)
print(t.shape)










































