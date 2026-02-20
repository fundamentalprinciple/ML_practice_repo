import torch
from LinearRegression import LinearRegressionModel 

torch.manual_seed(42)

model_0 = LinearRegressionModel()
print(model_0.parameters())
print(model_0.state_dict())

model_0.eval()
with torch.inference_mode():
    Y_preds = model_0(X_test)


