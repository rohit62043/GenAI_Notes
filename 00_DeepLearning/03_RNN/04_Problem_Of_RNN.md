# Notes on Vanishing Gradient Problem in RNNs and Solutions

## Understanding the Problem in Simple RNNs

### Key Concepts

1. **Output Derivatives**:

   - For an RNN, the output at a particular timestamp, `O3`, is computed using:
     \[
     O3 = \text{sigmoid}(X\_{I3} \cdot W_I + O2 \cdot W_H + B)
     \]
     where:
     - \( X\_{I3} \): Input feature
     - \( W_I \): Input weight
     - \( O2 \): Previous hidden state output
     - \( W_H \): Hidden state weight
     - \( B \): Bias term

2. **Sigmoid Derivative**:

   - The derivative of the sigmoid activation function is bounded between \( 0 \) and \( 0.25 \).
   - As computations progress through layers or time steps, repeated multiplications with these small derivatives cause the values to shrink.

3. **Impact on Gradients**:
   - Due to repeated multiplications with small derivatives, values diminish and approach zero, especially for earlier timestamps.
   - This leads to the **vanishing gradient problem**, where earlier inputs have minimal to no contribution in updating weights.

### Illustration of the Problem

- When calculating the loss gradient for `O3` (at timestamp 3):
  - Derivative chain becomes very small for earlier timestamps.
  - The contributions of inputs at earlier timestamps (e.g., \( t=1 \)) are negligible in weight updates.
- For later timestamps (e.g., \( t=50 \)):
  - The gradient chain is relatively large, making recent inputs more significant in predictions.

### Result

- **Long-term dependencies** are not effectively captured by simple RNNs.
- This bias toward recent inputs results in the **vanishing gradient problem**.

---

## Addressing the Vanishing Gradient Problem

### Activation Function Modifications

1. **Switch from Sigmoid to Tanh**:
   - Tanh has a derivative range between \( 0 \) and \( 1 \), which slightly alleviates the issue but does not eliminate it.
2. **ReLU or Leaky ReLU**:
   - ReLU derivatives are consistent and near \( 1 \), preventing significant shrinkage of gradients.

### Improved Architectures

1. **Long Short-Term Memory (LSTM)**:

   - LSTMs solve the vanishing gradient problem by introducing:
     - **Cell states**: Long-term memory that persists through time.
     - **Gates**: Mechanisms to control the flow of information:
       - Forget gate
       - Input gate
       - Output gate
   - These gates allow selective retention of relevant information and mitigate gradient shrinkage.

2. **Gated Recurrent Units (GRU)**:
   - GRUs are a simpler alternative to LSTMs with similar benefits.
   - They use fewer gates:
     - Update gate
     - Reset gate
   - GRUs are computationally efficient while addressing long-term dependencies.

---

## Summary

- **Simple RNNs** suffer from the vanishing gradient problem due to repeated multiplications with small derivatives.
- This results in earlier inputs having negligible contributions, hindering the model's ability to capture long-term dependencies.
- Solutions:
  - Use alternative activation functions (e.g., ReLU, Leaky ReLU).
  - Leverage advanced architectures like **LSTMs** and **GRUs** that are specifically designed to manage long-term dependencies.

---

In the next steps, the focus will shift to understanding **LSTMs**, **GRUs**, and their mechanisms to overcome the limitations of simple RNNs.
