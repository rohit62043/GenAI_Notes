# Table of Contents

1. [The Importance of Effective Initialization](#the-importance-of-effective-initialization)
2. [The Problem of Exploding or Vanishing Gradients](#the-problem-of-exploding-or-vanishing-gradients)
3. [What is Proper Initialization?](#what-is-proper-initialization)
4. [Mathematical Justification for Xavier Initialization](#mathematical-justification-for-xavier-initialization)

---

## I. The Importance of Effective Initialization

To build a machine learning model, typically the following steps are followed:

1. **Define the model architecture** (e.g., logistic regression, support vector machine, neural network).
2. **Training Process**:
   - Initialize parameters.
   - Select an optimization algorithm.
   - Repeat the following steps:
     1. Forward propagate the input.
     2. Compute the cost function.
     3. Compute gradients of the cost w.r.t parameters using backpropagation.
     4. Update the parameters using the gradients and optimization algorithm.
3. Use the trained model to predict the class of new data points.

### Why Initialization is Crucial:

- Initialization affects model performance significantly.
- Choosing the wrong initialization can hinder the learning process.

#### Example of Symmetrical Initialization:

- **Symmetry Problem**:
  - When all weights are initialized to the same value, neurons learn identical features.
  - This prevents different neurons from learning diverse information.
  - tanh/sigmoid/relu-->behave like perceptron unable to capture non-linearity.

#### Impact of Poor Initialization:

1. **Zero Initialization**:

   - Leads to neurons evolving symmetrically, hence no diversification in learning.
   - Poor performance due to identical gradients across neurons.
   - tanh/relu-->no update/no learning
   - sigmoid-->behave like percepton.

2. **Very Small or Very Large Initialization**:

   - **Too Small**: Results in slow learning.
   - tanh/sigmoid->vanishing gradient problem
   - relu->very slow training and little vanishing gradient problem

   - **Too Large**: Causes divergence in the learning process.
   - tanh/sigmoid-->slow training and vanishing gradient problem
   - relu-->exploding gradient problem

---

## II. The Problem of Exploding or Vanishing Gradients

When training deep neural networks, gradients tend to either:

- **Explode**: Become excessively large.
- **Vanish**: Become too small, approaching zero.

### Explaining the Phenomenon:

1. **Forward and Backpropagation in Deep Networks**:

   - With each forward and backward pass, the gradients may be amplified or diminished.

2. **Example (Linear Activation Functions)**:
   - The output at layer `L` is expressed as:
     \[
     \hat{y} = W^{[L]} W^{[L-1]} ... W^{[1]} x
     \]
   - If weights are initialized as identical matrices, the activations grow (or shrink) exponentially.

### Different Initialization Outcomes:

1. **Too-Large Initialization (Exploding Gradients)**:

   - Weights initialized as slightly larger than the identity matrix, e.g., `W = [[1.5, 0], [0, 1.5]]`.
   - Results in exponentially increasing activations and gradients, causing oscillation in the cost function.

2. **Too-Small Initialization (Vanishing Gradients)**:
   - Weights initialized smaller than the identity matrix, e.g., `W = [[0.5, 0], [0, 0.5]]`.
   - Leads to vanishing activations and gradients, slowing or halting learning.

#### Generalization:

- Both exploding and vanishing gradients result from inappropriate weight initialization and apply to general initialization strategies, not just symmetric matrices.

---

## III. What is Proper Initialization?

### Key Rules of Thumb:

1. **Mean of Activations**:

   - The mean should be zero across layers.

2. **Variance of Activations**:
   - The variance should remain consistent from one layer to the next.

#### Effect on Gradients:

- With consistent mean and variance, gradients won’t explode or vanish, ensuring efficient backward propagation.

### Xavier Initialization (or Glorot Initialization):

- **Weights** are initialized from a normal distribution:
  \[
  W^{[l]} \sim \mathcal{N}\left(0, \frac{1}{n^{[l-1]}}\right)
  \]
  where `n^{[l-1]}` is the number of neurons in layer `l-1`.
- **Biases** are initialized to zero.

This approach ensures that the variance of the activations stays constant across layers.

---

## IV. Mathematical Justification for Xavier Initialization

### Objective:

- Ensure the variance of the activations remains consistent across layers to prevent gradient explosion or vanishing.

### Assumptions:

1. **Activations follow a normal distribution** around zero.
2. **Activation function** is `tanh` (which is linear in the small region near zero).

### Stepwise Derivation:

1. **Forward Propagation**:

   - For layer `l`:
     \[
     z^{[l]} = W^{[l]} a^{[l-1]} + b^{[l]}
     \]
     \[
     a^{[l]} = \tanh(z^{[l]}) \approx z^{[l]}
     \]

2. **Relationship between Variances**:

   - We aim to maintain:
     \[
     \text{Var}(a^{[l-1]}) = \text{Var}(a^{[l]})
     \]

3. **Computing Variances**:

   - Using independence assumptions for weights and inputs:
     \[
     \text{Var}(z*k^{[l]}) = \sum*{j=1}^{n^{[l-1]}} \text{Var}(w\_{kj}^{[l]}) \text{Var}(a_j^{[l-1]})
     \]
   - This leads to the condition:
     \[
     \text{Var}(W^{[l]}) = \frac{1}{n^{[l-1]}}
     \]

4. **Result**:
   - By initializing weights using Xavier initialization, the variance of activations remains constant across layers, avoiding gradient explosion or vanishing.

---

### Conclusion:

Xavier Initialization effectively ensures stable gradient propagation across deep neural networks by maintaining zero-mean activations and consistent variance across layers.

# Weight Initialization Techniques

## Initialization Methods

1. **Random Initialization**:

   - `np.random.randn`
   - Example: \( \sim -3 \) to \( 3 \)
   - Distributions:
     - Normal
     - Uniform

2. **What Can Be Done**:
   - Heuristics (empirical practices, or "jugad")
   - Xavier / Glorot Initialization (for `tanh`, `sigmoid`):
     - \( \sim \mathcal{N}(0, \frac{1}{n\_{\text{in}}}) \)
     - \( \sim \mathcal{U}[-\text{limit}, \text{limit}] \)
     - Limit formula:
       \[
       \text{limit} = \sqrt{\frac{6}{n*{\text{in}} + n*{\text{out}}}}
       \]
   - He Initialization (for `ReLU`):
     - Uses variance-based scaling.

## Explanation of Intuition

- For **Xavier Initialization** (normal):
  - Weights initialized with variance \( \frac{1}{n} \), where \( n \) is the number of inputs.
  - This ensures inputs propagate efficiently through the network.
- For large networks:
  - Small weight initializations:
    \[
    \text{np.random.randn(250, 250)} \times 0.01
    \]
    - Ensures values remain close to zero.
  - Large weight initializations:
    \[
    \text{np.random.randn(250, 250)} \times 3
    \]
    - Results in large weights, which can cause exploding gradients.

## Variance Explanation

- \( \frac{1}{n} \) is the variance formula used in initialization.
- \( n \) is the number of neurons/inputs into the layer.

## Xavier Initialization (Normal)

- Formula:
  \sqrt{\frac{1}{\text{fan-in}}}

- Used when the number of inputs coming into each node is `fan-in`.
- Weights are initialized as:
  \[
  \text{np.random.randn(2, 2)} \times \sqrt{\frac{1}{2}}
  \]

## He Initialization (Normal)

- For `ReLU` activations, use:
  \[
  \sqrt{\frac{2}{n\_{\text{in}}}}
  \]

## Uniform Distribution

- **Xavier Uniform**:
  \[
  [-\text{limit}, \text{limit}]
  \]

  - Limit formula:
    \[
    \text{limit} = \sqrt{\frac{6}{n*{\text{in}} + n*{\text{out}}}}
    \]

- **He Uniform**:
  \[
  [-\text{limit}, \text{limit}]
  \]
  - Limit formula:
    \[
    \text{limit} = \sqrt{\frac{6}{n\_{\text{in}}}}
    \]
