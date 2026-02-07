import torch
import numpy as np

t = torch.rand(3,4)
print(t)
print(t.shape)
print(torch.min(t))
print(torch.max(t))
print(torch.mean(t))
print(torch.std(t))
print(f"{torch.min(t):.10f}")
