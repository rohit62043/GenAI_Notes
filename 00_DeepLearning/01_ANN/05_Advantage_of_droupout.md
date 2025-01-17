# Practical Tips and Tricks

## 1. Overfitting & Underfitting

- _Overfitting_ --> then increase the value of _p_.

- _Underfitting_ --> then decrease the value of _p_.

## 2. Dropout in Last Layer

- _Dropout_ -->first start to apply droupout with last layer.

## 3. Network Type Specific Dropout Rates

- _CNN (Convolutional Neural Network):_

  - Recommended dropout rate: 40-50%

- _ANN (Artificial Neural Network):_

  - Recommended dropout rate: 10-20%

- _RNN (Recurrent Neural Network):_
  - Recommended dropout rate: 20-30%

# Drawbacks of Using Dropout

## 1. Delay in Convergence

- _Convergence Delay_: Dropout can significantly delay the convergence of the training process. This happens because dropout randomly deactivates a portion of neurons in each training phase, which means the network must adapt to work with different subsets of neurons at each iteration.

## 2. Impact on Learning

- _Complex Learning Dynamics_: When dropout is used, each training iteration effectively trains a different "thinned" network with some neurons dropped out. This can lead to more complex learning dynamics and instability in the learning process.

- _Changes in Loss Function_: With dropout, since the network architecture dynamically changes during training, it can result in fluctuations in the value of the loss function. These fluctuations may make it more difficult to track progress and adjust hyperparameters effectively.

- _Stability Issues_: As neurons are randomly dropped during training, it might affect the stability of the network, especially if the dropout rate is too high, leading to poorer performance on validation or test sets if not properly managed.
