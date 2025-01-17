# Activation Functions in Neural Networks

Activation functions in neural networks define the output of a node given an input or set of inputs. They introduce non-linear properties to the network, which allows them to learn more complex functions.

## Sigmoid Activation Function

- **Description**: The sigmoid function maps any value to a value between 0 and 1. It is defined as \(\sigma(x) = \frac{1}{1 + e^{-x}}\).
- **Advantages**:
  - **Smooth gradient**, preventing jumps in output values.
  - Outputs are interpretable as probabilities.
- **Disadvantages**:
  - **Vanishing gradient problem**: For large values, the gradient is almost zero, which slows down the learning process.
  - Outputs are not zero-centered.
  - **Computationally expensive** due to the exponential function.

## Tanh (Hyperbolic Tangent) Activation Function

- **Description**: The tanh function is similar to the sigmoid but maps the input values to a range between -1 and 1. It is defined as \(\tanh(x) = \frac{2}{1 + e^{-2x}} - 1\).
- **Advantages**:
  - **Zero-centered** output, which can make learning easier in multi-layer networks.
  - Like sigmoid, provides a smooth gradient.
- **Disadvantages**:
  - **Vanishing gradient problem**: Like sigmoid, gradients can be small for large values, affecting learning speed.
  - Computationally expensive.

## ReLU (Rectified Linear Unit) Activation Function

- **Description**: ReLU function outputs the input if it is positive; otherwise, it outputs zero. It is defined as \(f(x) = \max(0, x)\).
- **Advantages**:
  - **Avoids and alleviates the vanishing gradient problem**, allowing models to learn faster and perform better.
  - **Computationally efficient**—requires simple max operation.
- **Disadvantages**:
  - **Dying ReLU problem**: For inputs less than zero, the gradient can be zero, which causes neurons to die for all inputs.
  - Not zero-centered output.

## Summary

Each activation function has its strengths and weaknesses. The choice of which activation function to use depends on the specific requirements of the neural network and the task at hand. Sigmoid and tanh are typically used for binary classification tasks where probabilities are needed, while ReLU is more common in convolutional neural networks due to its efficiency and effectiveness.
