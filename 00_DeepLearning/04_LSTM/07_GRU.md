# Detailed Notes on GRU (Gated Recurrent Units)

## 1. Introduction

- **GRU (Gated Recurrent Unit):** A type of recurrent neural network (RNN) designed to handle sequential data while mitigating the vanishing gradient problem.
- **Key Features:**
  - Combines **reset** and **update gates** to control the flow of information.
  - Simplified architecture compared to LSTM, resulting in fewer parameters and faster computation.
  - Effective for tasks like time series prediction, natural language processing, and speech recognition.

---

## 2. Key Components of GRU

### 2.1 Reset Gate (\(r_t\))

- **Purpose:** Decides how much of the previous hidden state (\(h\_{t-1}\)) to forget or reset.
- **Formula:**
  \[
  r*t = \sigma(W_r \cdot [x_t, h*{t-1}] + b_r)
  \]

  - \( W_r \): Weight matrix for the reset gate.
  - \( b_r \): Bias term.
  - \( \sigma \): Sigmoid activation function.

- **Operation:**

  - Input: Concatenated vector of \(x*t\) (current input) and \(h*{t-1}\) (previous hidden state).
  - Output: A vector of values between 0 and 1 representing how much information to reset.

- **Example Calculations:**
  - Reset 20% of \(0.6 \rightarrow 0.6 \times 0.2 = 0.12\).
  - Reset 40% of \(0.5 \rightarrow 0.5 \times 0.4 = 0.20\).
  - Reset 80% of \(0.3 \rightarrow 0.3 \times 0.8 = 0.24\).

---

### 2.2 Candidate Hidden State (\(\tilde{h_t}\))

- **Purpose:** Represents the new information computed based on the reset gate and current input.
- **Formula:**
  \[
  \tilde{h*t} = \text{tanh}(W_h \cdot [r_t \odot h*{t-1}, x_t] + b_h)
  \]

  - \( W_h \): Weight matrix for candidate hidden state.
  - \( b_h \): Bias term.
  - \( \odot \): Element-wise multiplication.

- **Operation:**
  - The reset gate (\(r*t\)) scales the previous hidden state (\(h*{t-1}\)).
  - Combine scaled \(h\_{t-1}\) with the current input (\(x_t\)).
  - Apply a tanh activation function to calculate the candidate hidden state (\(\tilde{h_t}\)).

---

### 2.3 Update Gate (\(z_t\))

- **Purpose:** Balances the contribution of the previous hidden state (\(h\_{t-1}\)) and the candidate hidden state (\(\tilde{h_t}\)).
- **Formula:**
  \[
  z*t = \sigma(W_z \cdot [x_t, h*{t-1}] + b_z)
  \]

  - \( W_z \): Weight matrix for the update gate.
  - \( b_z \): Bias term.

- **Operation:**
  - Input: Concatenated vector of \(x*t\) (current input) and \(h*{t-1}\) (previous hidden state).
  - Output: A vector of values between 0 and 1 representing how much information to retain from the past and how much to incorporate from the present.

---

### 2.4 Final Hidden State (\(h_t\))

- **Purpose:** Combines information from the previous hidden state (\(h\_{t-1}\)) and the candidate hidden state (\(\tilde{h_t}\)) using the update gate (\(z_t\)).
- **Formula:**
  \[
  h*t = z_t \odot \tilde{h_t} + (1 - z_t) \odot h*{t-1}
  \]

  - \( z_t \): Update gate controlling the contribution of \(\tilde{h_t}\).
  - \( 1 - z*t \): Contribution from the previous hidden state (\(h*{t-1}\)).

- **Explanation:**
  - \(z_t\): Determines how much of the new context (\(\tilde{h_t}\)) to include.
  - \(1 - z*t\): Determines how much of the past context (\(h*{t-1}\)) to retain.
  - Pointwise addition combines these two components to produce \(h_t\).

---

## 3. Step-by-Step Summary of GRU Operations

1. Compute **Reset Gate (\(r_t\))**:
   \[
   r*t = \sigma(W_r \cdot [x_t, h*{t-1}] + b_r)
   \]
2. Compute **Candidate Hidden State (\(\tilde{h_t}\))**:
   \[
   \tilde{h*t} = \text{tanh}(W_h \cdot [r_t \odot h*{t-1}, x_t] + b_h)
   \]
3. Compute **Update Gate (\(z_t\))**:
   \[
   z*t = \sigma(W_z \cdot [x_t, h*{t-1}] + b_z)
   \]
4. Compute **Final Hidden State (\(h_t\))**:
   \[
   h*t = z_t \odot \tilde{h_t} + (1 - z_t) \odot h*{t-1}
   \]

---

## 4. Key Insights

- **Coupled Gates:**

  - The reset gate (\(r_t\)) controls past information that should be ignored.
  - The update gate (\(z_t\)) balances old and new information to update the hidden state.

- **Interpretation of \(h_t\):**

  - Combines the context of the previous hidden state (\(h\_{t-1}\)) and the current candidate hidden state (\(\tilde{h_t}\)).

- **Efficiency:**
  - Fewer parameters than LSTMs due to the absence of separate input and forget gates.
  - Faster training with similar performance in many tasks.

---

## 5. Comparison: GRU vs. LSTM

| Feature                  | GRU                             | LSTM                                 |
| ------------------------ | ------------------------------- | ------------------------------------ |
| **Gates**                | Reset, Update                   | Input, Forget, Output                |
| **Hidden State Updates** | Combines reset and update gates | Uses separate input and forget gates |
| **Number of Parameters** | Fewer                           | More                                 |
| **Efficiency**           | Faster training                 | Slower due to complexity             |

---

## 6. Advantages of GRU

1. **Simplicity:** Fewer gates and parameters compared to LSTM.
2. **Efficiency:** Faster training and inference.
3. **Performance:** Handles long-term dependencies effectively, similar to LSTMs.
4. **Adaptability:** Works well on smaller datasets due to fewer parameters.

---

## 7. Applications of GRU

- **Natural Language Processing:** Text generation, sentiment analysis, machine translation.
- **Time Series Forecasting:** Predicting stock prices, weather, etc.
- **Speech Recognition:** Transcribing audio into text.
- **Sequential Data Processing:** Handling tasks where context and order are crucial.

---

## 8. Conclusion

- GRUs are a simplified and efficient alternative to LSTMs for handling sequential data.
- By using reset and update gates, GRUs manage to retain essential information while discarding irrelevant context.
- Their computational efficiency and strong performance make them a popular choice for various sequence modeling tasks.
