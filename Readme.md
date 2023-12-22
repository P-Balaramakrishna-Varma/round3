# Task
Create a training pipeline that takes in new data of batch size 32. To prevent catastrophic forgetting we do two things:
- Use 32 batch size data from initial 50% set and concatenate with current online batch.
- Use weight averaging with  weight factor between old and new weights.
- Monitor accuracy on old dataset and each new batch (before training).


# Steps taken to solve
## Traning the model on the initial dataset
1. Loading the MNIST dataset
2. Splitting the dataset into 50% and 50% for initial and online training
3. Creating a model (MLP)
4. Training the model on the initial dataset


## Training the model on the online data
