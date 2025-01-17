# Data Scaling in Neural Networks | Feature Scaling in ANN

## 1. Importance of Feature Scaling in Neural Networks

- Neural networks work by optimizing the weights associated with each input feature.
- **Feature scaling** helps improve the convergence speed and performance of the model.
- Non-scaled data can lead to inefficient learning, slower training, and suboptimal model performance.
- In Non-scaled loss fxn graph are non-symmetric and convergence of gradient descent is very unstable.

## 2. Types of Feature Scaling

### 2.1 Normalization (Min-Max Scaling)

- Transforms features by scaling them to a fixed range, typically [0, 1].
- Formula:
  ```math
  X' = \frac{X - X_{min}}{X_{max} - X_{min}}
  ```
  Ensures that all input features are on a similar scale, especially useful for algorithms that compute distances like k-NN.

## 2.2 Standardization (Z-score Normalization)

- Centers the data around 0 with a standard deviation of 1.
- Formula:

  ```math
  X' = \frac{X - \mu}{\sigma}
  ```

  Where:

- **μ** is the mean of the feature
- **σ** is the standard deviation of the feature

Often preferred for algorithms like neural networks since it makes the gradient descent process more stable.

## 3. Why Feature Scaling is Crucial for Neural Networks

Neural networks use gradient-based optimization techniques (like gradient descent), which are sensitive to the scale of input features.  
Non-scaled features can lead to:

- Large updates to some weights, which may cause oscillations and prevent convergence.
- Small updates to other weights, slowing down the learning process.

## 4. Impact of Data Scaling on Activation Functions

### 4.1 Sigmoid Activation Function

- Sigmoid squashes the input to a range between 0 and 1.
- Without scaling, if inputs are too large, it may push activations to the saturated ends, causing **vanishing gradients**.

### 4.2 Tanh Activation Function

- Tanh function squashes inputs to the range [-1, 1].
- Like sigmoid, large values can push the activations to saturation, leading to slow learning.

### 4.3 ReLU Activation Function

- ReLU is less affected by scaling since it only takes the positive part of the input. However, extreme values can still cause issues.

## 5. Best Practices for Scaling in Neural Networks

- **Always scale input features** before feeding them into the network.
- If using a neural network with multiple layers, you may need to re-scale the output of one layer before feeding it to the next, depending on the activation functions.
- For inputs with widely different ranges (e.g., age, income), normalization is typically recommended.
- For data with outliers, **robust scaling** (using percentiles) can be an alternative to min-max scaling.

## 6. Feature Scaling in Different Layers of ANN

- **Input Layer**: Input features should be scaled for better convergence.
- **Hidden Layers**: In deeper networks, weights can be initialized using techniques like **Xavier** or **He** initialization to account for scaling.
- **Output Layer**: In some cases (e.g., regression), you may need to scale the output values, though classification outputs (like softmax) typically don’t require scaling.

## 7. When Not to Use Scaling

- In certain cases (e.g., decision trees), feature scaling isn't required as the model is not sensitive to the scale of the features.

## 8. Tools for Scaling

- **Scikit-learn** provides various scaling functions:
  - `MinMaxScaler` for normalization.
  - `StandardScaler` for standardization.

These tools can be easily integrated into your preprocessing pipeline in neural networks.

## 9. Summary

- Feature scaling ensures uniformity in feature magnitudes, making gradient descent more efficient.
- Common scaling methods are **Normalization** (0 to 1)(use when Xmin and Xmax is known oe there are outliers in data--> data comes in unit cube) and **Standardization** (zero mean, unit variance)(use when data is normally distibuted--> mean become zero).
- Appropriate scaling depends on the nature of the data and the neural network architecture.

## 4. Comparison of Normalization vs Standardization

| Aspect                 | Normalization                                   | Standardization                          |
| ---------------------- | ----------------------------------------------- | ---------------------------------------- |
| **Range**              | Scales data to a fixed range, e.g., [0, 1]      | Centers data with mean 0 and std. dev. 1 |
|                        |
| **Best For**           | Non-Gaussian data, models sensitive to distance | Gaussian data, gradient-based algorithms |
| **Use Cases**          | k-NN, SVM, Neural Networks                      | Regression, Neural Networks, PCA         |
| **Impact on Outliers** | Sensitive to outliers                           | Less sensitive to outliers               |

---

## 5. Tools for Scaling

- **Scikit-learn** provides utilities for both scaling methods:
  - `MinMaxScaler` for normalization.
  - `StandardScaler` for standardization.

These can be used to quickly scale features in your machine learning pipeline.
