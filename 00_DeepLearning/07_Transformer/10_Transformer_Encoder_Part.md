# 🧠 Transformer Encoder Architecture — Masterclass Notes

---

## 📌 Overview

- **Instructor**: Nitesh (YouTube Channel)
- **Focus**: **Encoder** part of the Transformer.
- **Approach**: Focuses on **core components first** before explaining the full model.
- **Source**: Inspired by the seminal paper — _“Attention is All You Need” (Vaswani et al., 2017)_.

---

## 🧭 Why Transformers?

Transformers revolutionized deep learning for sequential data by:

- Removing recurrence (used in RNNs/LSTMs)
- Using **attention mechanisms** to model **global dependencies**
- Enabling parallelization for faster training

---

## 📦 High-Level Transformer Architecture

       Input Sentence
            ↓
        Encoder Stack
            ↓
         Decoder Stack
            ↓
      Final Predictions

- 🔹 **Encoder**: Reads and encodes input sequence
- 🔸 **Decoder**: Generates output (e.g., translation, summary)
- Transformer = Stack of N encoder + N decoder blocks (typically N = 6)

---

## 🧱 Components of the Encoder Block

Each encoder block contains:

1. **Multi-Head Self-Attention**
2. **Add & Layer Normalization**
3. **Feed-Forward Neural Network (FFN)**
4. **Add & Layer Normalization**

Each of the 6 encoder blocks has:

- **Same architecture**
- **Unique weights and parameters**

---

## ✍️ Step-by-Step: Encoding the Sentence `"How are you"`

---

### 1. 🔤 Input Preprocessing

#### a. **Tokenization**

- Sentence → Tokens: `"How"`, `"are"`, `"you"`

#### b. **Embedding Layer**

- Converts tokens into **dense vectors** (e.g., 512-dimensional)
- These embeddings are **learned** during training

#### c. **Positional Encoding**

- Injects **order information** into the model (since attention is order-agnostic)
- Formula involves **sinusoidal functions**:
- Final input = Word Embedding + Positional Encoding

---

### 2. 🧠 Inside One Encoder Block

#### 🔹 A. Multi-Head Self-Attention

- Allows the model to **focus on different positions** (context)
- Each attention head performs:
  $\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$
- **Queries (Q)**, **Keys (K)**, and **Values (V)** are computed via linear projections of input
- Outputs from all heads are concatenated and projected:
  $\text{MultiHead}(Q, K, V) = \text{Concat}(\text{head}_1, \ldots, \text{head}_8) \cdot W^O$

#### 🔹 D. Add & Layer Norm (Post-FFN)

- Adds input of FFN to its output
- Normalized to ensure stability
  $y_1 = \text{LayerNorm}(z_1 + \text{FFN}(z_1))$

---

## 🔁 Repeating Encoder Blocks

- Input vector goes through **6 such blocks** (can vary)
- Output vector shape is preserved: **[sequence_length, d_model]** = [3, 512]
- Final encoder output → passed to the decoder

---

## 🔍 Why Residual Connections?

| Benefit                        | Explanation                                                 |
| ------------------------------ | ----------------------------------------------------------- |
| 🔄 Prevent vanishing gradients | Helps gradients flow backward across deep networks          |
| 🧩 Retain original features    | If transformation is poor, identity path helps              |
| 🚀 Faster convergence          | Empirically shown to improve training speed and performance |

Origin: Introduced in **ResNet** to tackle deep network degradation.

---

## 🧠 Why Feed-Forward Neural Networks?

- Attention is a **linear operator** ➝ lacks expressive power
- FFNs add **non-linearity** to model complex features
- Research (2021): FFNs act like **key-value memory stores**:
  - Each FFN encodes distributional semantics
  - Stores pattern-matching structures seen during training

> **Fact**: FFNs contribute to **~2/3 of all transformer parameters**

---

## 📊 Final Encoder Output

| Token | Vector (512-d) | Interpretation                   |
| ----- | -------------- | -------------------------------- |
| How   | `y₁`           | Context-aware, normalized vector |
| are   | `y₂`           | Encodes position + semantics     |
| you   | `y₃`           | Ready for decoder processing     |

Shape: **[3 x 512]**

This matrix captures:

- **Word meaning**
- **Word position**
- **Contextual dependencies**

---

## 🧩 Why Stack Multiple Encoder Blocks?

| Reason                      | Description                                    |
| --------------------------- | ---------------------------------------------- |
| 🧠 Language is complex      | One layer is insufficient to model nuances     |
| 🔁 Depth increases capacity | More layers capture abstract features          |
| 🧪 Empirically optimal      | 6 layers found optimal in original Transformer |

> Deep stacking is a core principle in deep learning to **extract hierarchical features**.

---

## ✅ Summary

| Component            | Purpose                                       |
| -------------------- | --------------------------------------------- |
| Tokenization         | Breaks sentence into tokens                   |
| Embedding            | Converts tokens to 512-d vectors              |
| Positional Encoding  | Adds position info                            |
| Multi-Head Attention | Learns context-sensitive embeddings           |
| FFN                  | Introduces non-linearity                      |
| Residual + LayerNorm | Stabilizes training, preserves identity paths |
| Stacking 6 Layers    | Increases model depth & understanding         |

---

## 🚧 Coming Up Next

🔜 **Decoder Architecture**

- More complex due to:
  - Encoder-Decoder Attention
  - Masked Attention (for autoregressive decoding)
- Used for generation tasks (translation, summarization)

---

## 🧠 Advanced Thought Prompts

- What happens if we remove positional encoding?
- Can attention fully replace convolutions?
- How do different attention heads specialize?

---
