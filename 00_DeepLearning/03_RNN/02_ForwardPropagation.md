# Forward Propagation in Simple RNN

In this discussion, we will break down **forward propagation** in a **simple RNN** step by step using an example sentence.

## Recap: RNN Architecture

Before diving into forward propagation, let’s recall the basic architecture of a simple RNN:

- **Input Layer**: Receives the input word as a vector.
- **Hidden Layer**: Performs computations with hidden neurons.
- **Feedback Loop**: Passes the output of the hidden layer back to itself for the next time step.
- **Output Layer**: Generates the final output (prediction).

---

## Example: Forward Propagation with the Sentence

Consider the sentence:  
`The food is good.`

We will use the following steps to demonstrate forward propagation:

### 1. **Identify Unique Words**

The unique words are:  
`[the, food, good, bad, not]`

- Total unique words = **5**

### 2. **Convert Words to Vectors**

We use **one-hot encoding** for simplicity. Each word is represented as a vector of size 5.

| Word   | Vector            |
| ------ | ----------------- |
| `the`  | `[1, 0, 0, 0, 0]` |
| `food` | `[0, 1, 0, 0, 0]` |
| `good` | `[0, 0, 1, 0, 0]` |
| `bad`  | `[0, 0, 0, 1, 0]` |
| `not`  | `[0, 0, 0, 0, 1]` |

---

### 3. **RNN Architecture Setup**

For simplicity:

- Input size = 5 (number of unique words)
- Hidden layer = 3 neurons
- Output = Single neuron (binary classification)

### 4. **Forward Propagation Mechanics**

Forward propagation occurs **sequentially** over time steps, passing the hidden state and word input through the network.

#### **Time Step t = 1**

- Input: `X_11 = [1, 0, 0, 0, 0]` (vector for "the")
- Calculation:
  \[
  O_1 = f(X_11 \* W + B)
  \]
  - \( W \): Weight matrix for the input (5x3)
  - \( B \): Bias for the hidden neurons (3 values)
  - \( f \): Activation function (e.g., tanh or ReLU)

---

#### **Time Step t = 2**

- Input: `X_12 = [0, 1, 0, 0, 0]` (vector for "food")
- Hidden state from \( t=1 \): \( O_1 \)
- Calculation:
  \[
  O*2 = f(X_12 * W + O*1 * W' + B)
  \]
  - \( W' \): Weight matrix for the hidden state (3x3)

---

#### **Time Step t = 3**

- Input: `X_13 = [0, 0, 1, 0, 0]` (vector for "good")
- Hidden state from \( t=2 \): \( O_2 \)
- Calculation:
  \[
  O*3 = f(X_13 * W + O*2 * W' + B)
  \]

---

### 5. **Final Output Layer**

At the final time step (t=4), we use the last hidden state to compute the output:

- For **binary classification**, we apply the **sigmoid activation**:
  \[
  \hat{Y} = \sigma(O*4 \cdot W*{out} + B\_{out})
  \]
- If it were **multi-class classification**, we would use **softmax** instead.

---

## Parameters in the RNN

1. **Weight Matrices**:

   - Input-to-Hidden: \( W \) → \( 5 X 3 \) (15 weights)
   - Hidden-to-Hidden: \( W' \) → \( 3 X 3 \) (9 weights)
   - Hidden-to-Output: \( W\_{out} \) → \( 3 X 1 \) (3 weights)

2. **Biases**:

   - Hidden Bias: 3 values
   - Output Bias: 1 value

3. **Total Trainable Parameters**:
   \[
   \text{Total} = 15 (W) + 9 (W') + 3 (W\_{out}) + 4 (\text{bias}) = 31
   \]

---

## Final Summary of Forward Propagation

At each time step \( t \):

1. Multiply the input word vector with the input weights \( W \).
2. Add the hidden state (previous output) multiplied by \( W' \).
3. Add bias and apply the activation function \( f \).
4. Pass the updated hidden state to the next time step.
5. At the final step, compute the output and apply sigmoid (or softmax).

This ensures that each hidden layer captures the **context** of previous words in the sequence.

---

## Conclusion

Understanding forward propagation in RNN is critical for comprehending **sequential data processing**. Once you master this, understanding advanced architectures like **LSTM** and **GRU** becomes much easier.

In the next discussion, we will explore **backpropagation** in RNNs.

---
