# Notes on LSTM: Input Gate and Candidate Memory

## Overview

This session focuses on the **Input Gate** and **Candidate Memory** in an LSTM (Long Short-Term Memory) network. Additionally, it explains the operations performed during the forget and input stages, including the mathematical intuitions and step-by-step calculations.

---

## Recap: Forget Gate

- The forget gate calculates \( f*t \), which determines how much information from the previous cell state (\( C*{t-1} \)) should be retained or discarded.
- **Operation**:
  \[
  f*t = \sigma(W_f \cdot [h*{t-1}, x_t] + b_f)
  \]
  - \( h\_{t-1}, x_t \): Concatenated hidden state and input at time \( t \).
  - \( W_f \): Weight matrix for the forget gate.
  - \( b_f \): Bias for the forget gate.
  - \( \sigma \): Sigmoid activation function.

---

## Input Gate

The input gate determines what new information will be added to the cell state (\( C_t \)).

### Mathematical Operations:

1. **Compute the Input Gate Activation (\( i_t \)):**
   \[
   i*t = \sigma(W_i \cdot [h*{t-1}, x_t] + b_i)
   \]

   - \( W_i, b_i \): Weight and bias for the input gate.
   - \( \sigma \): Sigmoid activation function.

2. **Compute the Candidate Memory (\( \tilde{C}\_t \)):**
   \[
   \tilde{C}_t = \tanh(W_c \cdot [h_{t-1}, x_t] + b_c)
   \]

   - \( W_c, b_c \): Weight and bias for candidate memory.
   - \( \tanh \): Hyperbolic tangent activation function.

3. **Pointwise Multiplication (Input Gate and Candidate Memory):**
   \[
   i_t \odot \tilde{C}\_t
   \]
   - Determines how much of the candidate memory to integrate into the current cell state.

---

## Candidate Memory

The candidate memory (\( \tilde{C}\_t \)) provides potential new information to be added to the cell state.

### Process:

1. **Concatenate inputs (\( h\_{t-1} \) and \( x_t \)).**
2. Pass through a hidden layer with weights \( W_c \) and bias \( b_c \).
3. Apply the \( \tanh \) activation function to regulate the scale of the new information.

---

## Cell State Update

The updated cell state (\( C_t \)) combines:

1. **Forget Gate Operation:**
   \[
   f*t \odot C*{t-1}
   \]

   - Retains necessary information from the previous cell state.

2. **Input Gate and Candidate Memory Operation:**
   \[
   i_t \odot \tilde{C}\_t
   \]
   - Adds relevant new information to the cell state.

### Final Cell State:

\[
C*t = (f_t \odot C*{t-1}) + (i_t \odot \tilde{C}\_t)
\]

---

## Example: Contextual Learning

- Input Sentence: "I stay in India. I speak **\_**."
- The LSTM:
  - Stores "India" in the memory cell as context.
  - Uses this context to predict "Hindi" or "English" based on the region-specific association.

---

## Key Takeaways

1. **Forget Gate**: Decides what to discard from the memory.
2. **Input Gate + Candidate Memory**:
   - Input gate decides the importance of new information.
   - Candidate memory proposes new information.
   - Pointwise multiplication integrates new information into the cell state.
3. **Final Cell State**: Combines the retained information and the new context.

The combination of these gates enables LSTMs to maintain long-term dependencies and contextual understanding effectively.

---
