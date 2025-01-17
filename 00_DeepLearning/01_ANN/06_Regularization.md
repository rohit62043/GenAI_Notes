# Video Notes: Improving Neural Network Performance and Regularization

## 00:00 - Intro

- Introduction to the topic of improving neural network performance.
- Overview of challenges in training neural networks.

## 00:40 - Improving NN Performance

- Focus on techniques to enhance the performance of neural networks.
- Various strategies to optimize the training process.

## 01:53 - Overfitting

- Explanation of **overfitting**: when a model performs well on training data but poorly on unseen data.
- Symptoms of overfitting and how it impacts the generalization of the model.

## 04:52 - Why Neural Networks Overfit?

- Complex models like neural networks have a high number of parameters.
- **High capacity** models tend to memorize training data rather than generalizing.
- Factors contributing to overfitting:
  - Insufficient training data.
  - Too many parameters compared to the amount of data.
  - Lack of regularization or data augmentation.

## 09:08 - Ways to Solve Overfitting

- Several approaches to reduce overfitting:

  - **Data Augmentation**: artificially increasing the dataset by transformations like rotation, scaling, etc.
  - **Dropout**: randomly dropping units in the neural network during training to prevent co-adaptation of neurons.
  - **Early Stopping**: stop training when performance on validation data starts to degrade.
  - **Regularization** (L1, L2, Elastic Net).
  - **Cross-Validation**: helps to determine if the model is overfitting or underfitting.

  # Regularization in Neural Networks: L1 and L2 Regularization

Regularization is a technique used to prevent **overfitting** in machine learning models, including neural networks (NNs). Regularization methods such as **L1** and **L2** regularization add a penalty to the loss function based on the complexity of the model, encouraging the network to learn simpler, more generalizable patterns.

## 1. L1 Regularization (Lasso)

L1 regularization adds the **absolute values** of the model parameters (weights) to the loss function. It is also known as **Lasso** (Least Absolute Shrinkage and Selection Operator).

- **Loss function with L1 regularization**:
  \[
  L = L*0 + \lambda \sum*{i} |w_i|
  \]
  Where:

  - \( L_0 \) is the original loss (e.g., MSE).
  - \( \lambda \) is the regularization strength (a hyperparameter).
  - \( w_i \) are the weights of the model.

- **Effects**:

  - L1 regularization encourages **sparsity** in the weight matrix, meaning that it tends to make many weights exactly zero. This effectively results in **feature selection**, as some input features will have no impact on the output.
  - Good for problems where you expect that only a few input features are important.

- **Application**:
  - L1 is used when we want a **sparse model**, i.e., fewer weights contributing to the model output.
  - It helps in reducing the complexity of the model by driving some weights to zero.

## 2. L2 Regularization (Ridge)

L2 regularization adds the **squared values** of the model parameters (weights) to the loss function. It is also known as **Ridge** regularization.

- **Loss function with L2 regularization**:
  \[
  L = L*0 + \lambda \sum*{i} w_i^2
  \]
  Where:

  - \( L_0 \) is the original loss (e.g., MSE).
  - \( \lambda \) is the regularization strength (a hyperparameter).
  - \( w_i \) are the weights of the model.

- **Effects**:

  - L2 regularization encourages **smaller weights** but does not drive them to zero. It penalizes large weights, forcing the network to distribute the importance across many features, reducing the risk of overfitting.
  - L2 is more effective when all input features may contribute to the output, but we want to limit their individual impact.

- **Application**:
  - L2 is typically used when we expect that many input features will contribute to the output, but we want to **regularize** the magnitude of the weights to avoid overfitting.
  - It helps in stabilizing the learning process by controlling large weight updates.

## 3. L1 vs L2 Regularization

| **L1 (Lasso)**                                        | **L2 (Ridge)**                                         |
| ----------------------------------------------------- | ------------------------------------------------------ |
| Adds the **absolute values** of weights to the loss   | Adds the **squared values** of weights to the loss     |
| Results in **sparse** weights (some weights become 0) | Tends to **shrink** weights but rarely makes them zero |
| Useful for **feature selection**                      | Useful for **preventing overfitting**                  |
| More robust to **outliers**                           | All weights remain non-zero, but smaller               |
| Suitable for cases with a **few important features**  | Suitable for cases with **many contributing features** |

## 4. Elastic Net Regularization

**Elastic Net** is a combination of both **L1 and L2** regularization.

- **Loss function**:

### Loss function:

The loss function is defined as:

\[ L = L_0 + \lambda_1 \sum |w_i| + \lambda_2 \sum w_i^2 \]

Where:

- \( \lambda_1 \) controls the L1 regularization.
- \( \lambda_2 \) controls the L2 regularization.

- **Effect**: Elastic Net encourages both **sparsity** (like L1) and **small weights** (like L2). It is useful when some features may be irrelevant, but many are still contributing.

## 5. Impact on the Gradient Descent Optimization

- **L1 regularization**: During gradient descent, the update rule for weights involves a **constant factor**, which can drive weights towards zero more aggressively.
- **L2 regularization**: The weights are updated **proportionally** to their current values, leading to smoother and smaller weights over time.
