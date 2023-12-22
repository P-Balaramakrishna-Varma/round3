import torchvision
import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets


train_dataset = torchvision.datasets.MNIST('./data', train=True, download=True)
# intial_train_size = len(train_dataset) // 2
dataloader =