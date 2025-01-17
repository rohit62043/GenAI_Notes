# ReLU Activation Function

## Definition:

\[
f(x) = \max(0, x)
\]

- If \(x \geq 0\), \(f(x) = x\)
- If \(x < 0\), \(f(x) = 0\)

## Advantages:

1. **Non-linear** activation function.
2. **Not saturated** in the positive region.
3. **Computationally inexpensive** (simple max operation).
4. **Faster convergence** compared to sigmoid or tanh.

## Disadvantages:

- \(x < 0 \Rightarrow f(x) = 0\) (Neuron remains inactive).
- **Dying ReLU problem** (many neurons stop learning if they output 0 too often).

---

# Dying ReLU Problem

- Occurs when **ReLU neurons become inactive** (forever output 0).
- Leads to **vanishing gradients** and **non-updated weights**.
- Severe issue when:
  - A large portion (e.g., **50% or more**) of neurons are dead.
  - **100% dead neurons** => no learning.

### Explanation:

- For ReLU:  
  \[
  f(x) = \max(0, z)
  \]

  - If \(z < 0\), \(f(z) = 0\) (causing the neuron to die).

- **Weight updates**:
  \[
  \frac{\partial L}{\partial z_i} = 0
  \]
  - If the neuron dies, gradients stay 0, and no weight updates happen.
  - **Dead neurons cannot backpropagate gradients** effectively.

### Example:

1. Input \(x_1, x_2\) and weights \(w_1, w_2\).
2. If the weighted sum \(z_i\) becomes negative, \(f(z_i) = 0\).
3. Gradients like \( \frac{\partial L}{\partial z_i} \) stay 0, preventing updates in further backpropagation steps.

---

## Solutions to Dying ReLU:

1. **Use a lower learning rate**.
2. **Bias shifting**: Add a small bias value like 0.01.
3. **Do not use ReLU** for all neurons:
   - Use **Leaky ReLU** or other variants (e.g., **PReLU**, **ELU**, **SELU**).

---

# Leaky ReLU

## Definition:

\[
f(x) = \max(\alpha \cdot x, x)
\]

- If \(z \geq 0\), \(f(z) = z\).
- If \(z < 0\), \(f(z) = \alpha \cdot z\), where \( \alpha \) is a small value (e.g., 0.01).

### Derivative:

- \(f'(z) = 1\) for \(z \geq 0\).
- \(f'(z) = \alpha\) for \(z < 0\).

## Advantages:

1. **Non-saturated** (reduces the risk of vanishing gradients).
2. **Easy to compute**.
3. **Prevents the dying ReLU problem**.
4. **Close to zero-centered behavior**.

## Disadvantages:

- Still not completely zero-centered: output may drift towards positive values.

# SELU - Scaled Exponential Linear Unit

_Date: 09 June 2022_

---

## SELU Formula:

\[
\text{SELU}(x) = \begin{cases}
\lambda x & \text{if } x \geq 0 \\
\lambda (\alpha e^x - \alpha) & \text{if } x < 0
\end{cases}
\]

Where:

- \(\alpha \approx 1.6732632423543772848170429916717\)
- \(\lambda \approx 1.0507009873554804934193349852946\)

> Fixed scale factor and training normalization.

---

## Self-Normalizing Activation

### Properties:

- Mean (\(m\)) = 0
- Standard Deviation (\(\sigma\)) = 1

- **Self-Normalizing**: The output automatically gets normalized.
- **Faster Convergence**: Helps neural networks converge more quickly.

---

# Parametric ReLU

---

## Parametric ReLU Formula:

\[
f(x) = \begin{cases}
x & \text{if } x > 0 \\
\alpha x & \text{otherwise}
\end{cases}
\]

- \(\alpha\) is a trainable parameter.
- **Flexibility**: Adapts based on the training data.

---

# ELU - Exponential Linear Unit

---

## ELU Formula:

\[
\text{ELU}(x) = \begin{cases}
x & \text{if } x > 0 \\
\alpha (e^x - 1) & \text{if } x \leq 0
\end{cases}
\]

- **Advantages**:
  - Closer to zero-centered mean, which accelerates the learning process.
  - Helps with better generalization.
  - Works well with deep neural networks.
- **Disadvantage**:
  - Computationally expensive due to exponentiation.
