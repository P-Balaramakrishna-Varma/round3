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
### Training
```train_online``` function takes in the online data (new batch) and trains the model. The pseudo code for the function is as follows:
> ```
> weight_initial = model.get_weights()
>
> for _ in range(5):
>     cur_batch = mix(old_batch, new_batch)
>     pred = model(cur_batch)
>     model.update()
>
> weight_after = model.get_weights()
> model.set_weights(x * weight_initial + (1 - x) * weight_after) 
> ```


### Monitioring Accuracy
Accuracy is monitored on
- Test set using ```test_loss``` function.
- Old dataset + new batches using ```test_online``` function.

```test_online``` function takes test dataloader and new batches trained till now. The pseudo code for the function is as follows:
> ```
> for X, y in chain(old_dataloader, new_batches):
>      pred = model(X)
>      loss += loss_fn(pred, y)
>      size += len(X)
> return loss / size
>```