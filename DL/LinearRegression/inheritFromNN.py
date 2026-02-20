import torch
import torch.nn as nn

class LinearRegressionModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.weight = nn.Parameter(torch.randn(1))
        self.bias = nn.Parameter(torch.randn(1))        

    def forward(self, x):
        return self.weight*x + self.bias

x = torch.tensor([[1.0],[2.0],[3.0]])
model = LinearRegressionModel()

y = model(x)
#print(y,y.shape)
#print(list(model.parameters()))


class MAE(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, predictions, targets):
        residuals = predictions - targets
        absolute_errors = torch.abs(residuals)
        return torch.mean(absolute_errors)

class HuberLoss(nn.Module):
    def __init__(self, delta=1.0):
        super().__init__()
        self.delta = delta

    def forward(self, predictions, targets):
        residuals = predictions - targets
        abs_residuals = torch.abs(residuals)
    
        quadratic_mask = abs_residuals <= self.delta
        linear_mask = abs_residuals > self.delta

        quadratic_loss = 0.5*residuals**2
        linear_loss = self.delta*abs_residuals - 0.5*self.delta**2
        
        loss = quadratic_mask*quadratic_loss + linear_mask*linear_loss

        return torch.mean(loss) 

sample_predictions = torch.tensor([1.0,2.0,3.0])
sample_targets = torch.tensor([1.5,1.8,2.5]) 

builtin_l1 = nn.L1Loss()
custom_mae = MAE()
huber = HuberLoss()

print(builtin_l1(sample_predictions, sample_targets))
print(custom_mae(sample_predictions, sample_targets))
print(huber(sample_predictions, sample_targets))



