# Bahdanau Attention vs. Luong Attention

## Overview

Bahdanau Attention and Luong Attention are two widely used attention mechanisms in sequence-to-sequence models, particularly in machine translation tasks. These mechanisms help the model focus on different parts of the input sequence while generating each element of the output sequence. Understanding their differences is crucial for optimizing sequence-based models.

---

## 1. Introduction to Attention Mechanisms

Attention mechanisms enhance the performance of sequence-to-sequence models by dynamically selecting relevant parts of the input sequence when generating each output token.

- **Bahdanau Attention** (Additive Attention): Introduces **alignment scores** to determine how much focus each encoder hidden state should receive.
- **Luong Attention** (Multiplicative Attention): Simplifies attention computation by using a **global score function**.

---

## 2. Bahdanau Attention (Additive Attention)

### Overview

- Introduced by **Bahdanau et al. (2015)**.
- Designed to improve translation accuracy by allowing the decoder to access all encoder states at each timestep.

### Key Components

1. **Alignment Scores**

   - A feedforward network calculates alignment scores between the decoder state and each encoder hidden state.
   - These scores determine **attention weights** after applying a softmax function.

2. **Context Vector Computation**

   - The attention weights are used to compute a weighted sum of encoder hidden states, forming a **context vector**.
   - This context vector helps generate the next output token.

3. **Computation Formula**

   - The alignment score \( e\_{ti} \) is computed as:

     \[
     e*{ti} = v^T \tanh(W_s s*{t-1} + W_h h_i)
     \]

   - Attention weights \( \alpha\_{ti} \) are obtained using softmax:

     \[
     \alpha*{ti} = \frac{\exp(e*{ti})}{\sum*{k} \exp(e*{tk})}
     \]

   - The context vector \( C_t \) is:

     \[
     C*t = \sum*{i} \alpha\_{ti} h_i
     \]

---

## 3. Neural Network Implementation of Bahdanau Attention

- The feedforward neural network is responsible for computing alignment scores.
- It uses learnable parameters to generate a **dynamic attention distribution** at each decoding step.
- This approach allows **flexible focus** on different input positions for different output tokens.

---

## 4. Architecture of Bahdanau Attention

- The **encoder** processes the input sequence and generates hidden states.
- The **attention mechanism** computes alignment scores for each encoder state.
- The **decoder** uses the computed **context vector** to generate the next output token.

---

## 5. Luong Attention (Multiplicative Attention)

### Overview

- Introduced by **Luong et al. (2015)**.
- Offers a **simpler and computationally efficient** attention mechanism compared to Bahdanau Attention.
- Uses **multiplicative scoring functions** instead of a feedforward network.

### Key Components

1. **Global vs. Local Attention**

   - **Global Attention:** Considers all encoder states for computing context.
   - **Local Attention:** Focuses on a fixed-sized window of encoder states.

2. **Scoring Functions in Luong Attention**

   - Luong Attention scores are computed using **dot product**, **general**, or **concat** functions:

     - **Dot Score** (simplest form):

       \[
       score(s_t, h_i) = s_t^T h_i
       \]

     - **General Score**:

       \[
       score(s_t, h_i) = s_t^T W h_i
       \]

     - **Concat Score**:

       \[
       score(s_t, h_i) = v^T \tanh(W[s_t; h_i])
       \]

3. **Context Vector Computation**
   - Attention weights are computed using softmax over the scores.
   - The context vector is obtained as a weighted sum of encoder hidden states.

---

## 6. Architecture of Luong Attention

- Similar to Bahdanau Attention but replaces additive scoring with multiplicative scoring.
- The **encoder** generates hidden states.
- The **decoder** computes attention scores and generates the output sequence based on the context vector.

---

## 7. Key Differences Between Bahdanau and Luong Attention

| Feature                      | Bahdanau Attention (Additive)                              | Luong Attention (Multiplicative)                          |
| ---------------------------- | ---------------------------------------------------------- | --------------------------------------------------------- |
| **Scoring Mechanism**        | Uses a feedforward network                                 | Uses dot product or linear transformation                 |
| **Computational Efficiency** | More complex due to extra parameters                       | More efficient as it avoids additional parameters         |
| **Alignment Calculation**    | Calculates alignment at each timestep                      | Uses simpler score functions                              |
| **Performance**              | Provides better results for long sequences                 | Works well for shorter sequences                          |
| **Architecture Type**        | Attention applied before computing the decoder’s new state | Attention applied after computing the decoder’s new state |

---

## 8. Conclusion

- **Bahdanau Attention** is more flexible but computationally expensive due to extra parameters.
- **Luong Attention** is simpler and faster but may not perform as well on long sequences.
- The choice of attention mechanism depends on the specific requirements of the model and computational constraints.

---

## 9. References

- **Bahdanau et al., 2015**: "Neural Machine Translation by Jointly Learning to Align and Translate"
- **Luong et al., 2015**: "Effective Approaches to Attention-based Neural Machine Translation"
