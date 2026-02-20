import torch
import torch.nn as nn

class MyLinearModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.weight = nn.Parameter(torch.randn(1))
        self.bias = nn.Parameter(torch.randn(1))

instance = MyLinearModel()
print(list(instance.parameters()))
