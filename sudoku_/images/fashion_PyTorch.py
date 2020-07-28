import torch

def activation(x):
    return 1/(1+torch.exp(-x))
    
