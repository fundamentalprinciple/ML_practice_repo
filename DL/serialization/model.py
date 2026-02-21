import torch
import torch.nn as nn

from pathlib import Path
MODEL_PATH = Path("dirSave")
MODEL_PATH.mkdir(parents=True, exist_ok=True)
MODEL_NAME = "model_01.pth"
MODEL_SAVE_PATH = MODEL_PATH / MODEL_NAME
#print(MODEL_SAVE_PATH.absolute())

class LinearRegressionModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.weight = nn.Parameter(torch.randn(1))
        self.bias = nn.Parameter(torch.randn(1))

    def forward(self, x):
        return self.weight*x + self.bias

model = LinearRegressionModel()

torch.save(model.state_dict(), MODEL_SAVE_PATH)

file_size = MODEL_SAVE_PATH.stat().st_size
#print(file_size)

#print(len(model.state_dict()))


