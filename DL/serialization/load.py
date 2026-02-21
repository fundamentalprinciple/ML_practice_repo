import torch
from model import MODEL_SAVE_PATH

saved_state=torch.load(MODEL_SAVE_PATH, weights_only=True)

#print(saved_state)

for name, tensor in saved_state.items():
    if tensor.numel() == 1:
        print(f"{name}: {tensor.item()}")
    else:
        print(f"{name} -> shape: {tensor.shape}, dtype: {tensor.dtype}")

