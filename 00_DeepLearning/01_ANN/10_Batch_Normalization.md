# Batch Normalization in Neural Networks

Batch Normalization (BN) transforms the internal workings of neural networks by normalizing inputs within each mini-batch. It stabilizes activations and helps improve the training process by addressing issues like vanishing/exploding gradients.

---

## What is Batch Normalization?

- **Batch Normalization** is a technique that normalizes the inputs to each layer across the mini-batch. This normalization ensures that the activations for each layer have a stable distribution, typically with zero mean and unit variance.
- It applies a normalization step to each mini-batch of data before passing it to the next layer.

## Why Use Batch Normalization?

- **Improved Convergence Speed**: BN helps the model converge faster during training.
- **Mitigating Vanishing/Exploding Gradients**: It stabilizes the training process by reducing sensitivity to network initialization.
- **Higher Learning Rates**: With BN, you can use higher learning rates, which can speed up training.

## Internal Covariate Shift

- Internal covariate shift refers to the changes in the distribution of network activations due to updates in the parameters of previous layers during training.
- Batch Normalization addresses this issue by normalizing layer inputs, which helps maintain stable distributions.

## Batch Normalization - The How?

- The process involves:
  - Calculating the mean and variance of the inputs for each mini-batch.
  - Normalizing the inputs using these statistics.
  - Scaling and shifting the normalized values using learnable parameters (gamma and beta).

## Batch Normalization During Test

- During testing, BN uses the running averages of the mean and variance (computed during training) instead of the mini-batch statistics to ensure consistent behavior.

## The Advantages

- **Reduces Sensitivity**: Helps reduce sensitivity to weight initialization.
- **Acts as a Regularizer**: May reduce the need for other regularization techniques like dropout.
- **Improves Performance**: Overall, it can lead to better performance and faster training times.

## Keras Implementation

- Batch Normalization can be easily implemented in Keras using the `BatchNormalization` layer. Here’s an example:

```python
from tensorflow.keras.layers import BatchNormalization, Dense

model = Sequential()
model.add(Dense(64, activation='relu', input_shape=(input_dim,)))
model.add(BatchNormalization())
model.add(Dense(10, activation='softmax'))
```
