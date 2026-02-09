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
'''

t = torch.rand(2,4)
s = torch.rand(4,2)
print(t+10, t-10, t*10)
print(t*t)
print(torch.matmul(t,s))
print(t@s)


