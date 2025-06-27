
# Transformer Decoder Architecture and Masked Multi-Head Attention

## 🔹 Introduction
- Speaker: **Nitesh**
- Playlist: Deep Learning – Transformers
- Previous focus: Transformer encoder architecture
- Current focus: **Decoder architecture**, particularly **Masked Multi-Head Attention**
- Decoder appears more complex but follows similar building-block logic
- New components: 
  - Masked Multi-Head Attention (variation of self-attention)
  - Cross-Attention

---

## 🔹 Autoregressive vs Non-Autoregressive Behavior

### ➤ Definitions
- **Autoregressive model**: Generates output step-by-step, each output depends on the previous one
- **Non-Autoregressive training**: Parallel processing of tokens during training

### ➤ Inference (Prediction)
- Decoder is **autoregressive**
- Predicts tokens **sequentially**, starting with a start token
- Relies on previously generated tokens and encoder outputs

### ➤ Training
- Decoder is **non-autoregressive** due to **teacher forcing**
- Uses ground truth next tokens instead of model predictions
- Enables **parallelization** during training

---

## 🔹 Encoder-Decoder Architecture Recap

- **Encoder**: Processes input (e.g., "How are you") and generates context vector
- **Decoder**:
  - Takes start token + context vector
  - Predicts each token in sequence: depends on prior outputs (autoregressive)
  - Continues until end token is predicted

---

## 🔹 Importance of Autoregressive Models

- Necessary due to **sequential nature of language**
- Cannot generate all tokens at once — later tokens depend on earlier ones
- Inference must be **sequential**, but training can be optimized

---

## 🔹 Training with Teacher Forcing

- Example:
  - Input: "How are you"
  - Output: "आप कैसे हैं"
- Decoder receives correct next word at each step (not model prediction)
- Ensures model learns correct sequence
- Loss is calculated by comparing output to ground truth
- **Training is sequential** across tokens

---

## 🔹 Challenges in Autoregressive Training

- **Slow training** due to step-by-step decoding
- Long sentences = longer training time
- But inference **requires** stepwise processing

---

## 🔹 Non-Autoregressive Parallel Training

- Training can be parallelized using **teacher forcing**
- Ground truth next tokens remove dependency on model outputs
- Decoder blocks can operate in parallel
- **Faster training**, but introduces risk of **data leakage**

---

## 🔹 Data Leakage Problem

- Parallel execution leads to **future tokens influencing current token**
- Not possible in inference → unfair advantage
- Leads to **excellent training performance**, but **poor generalization**

---

## 🔹 Self-Attention Mechanics Refresher

### ➤ Core Concepts
- Words → Embeddings → Self-Attention Block
- Self-attention generates **contextual embeddings**
- Word meaning adjusts based on surrounding words (e.g., "bank" with "river" vs "money")

### ➤ Self-Attention Steps
1. Word embeddings multiplied with:
   - Query weight matrix
   - Key weight matrix
   - Value weight matrix
2. Generates:
   - Query vectors
   - Key vectors
   - Value vectors
3. Attention scores = dot(Query, Key.T)
4. Scale scores → Apply softmax → Get attention weights
5. Multiply attention weights with value vectors → sum = Contextual embedding

---

## 🔹 Masking in Self-Attention

### ➤ Problem:
- During training, current word uses **future tokens** → unrealistic
- Need to **prevent future context**

### ➤ Solution: **Masking**
- Add **mask matrix** (same shape as attention matrix)
- Insert **-∞** in positions representing future tokens
- After softmax, those positions → 0
- Ensures each word attends only to previous and current tokens

### ➤ Result:
- **Parallel training possible**
- **Data leakage prevented**
- Combines benefits of:
  - **Autoregressive correctness**
  - **Parallel speed**

---

## 🔹 Final Thoughts

- **Masked Multi-Head Attention** is the key to achieving parallel training without data leakage
- Deep dive helps demystify key transformer components
- Knowing this helps with:
  - Better interview answers
  - Clear intuition for research/implementation
- Encouragement to continue the journey through transformer architecture

---

## ✅ Summary

| Topic                         | Key Idea                                                                 |
|------------------------------|--------------------------------------------------------------------------|
| Decoder vs Encoder           | Decoder has Masked MHA & Cross-Attention                                 |
| Inference                    | Autoregressive: step-by-step prediction                                  |
| Training                     | Non-autoregressive: parallel via teacher forcing                         |
| Data Leakage                 | Future tokens used in training → needs masking                           |
| Self-Attention               | Queries, Keys, Values → Attention scores → Weighted sums                 |
| Masking                      | Masks prevent attention to future tokens during training                 |
| Masked MHA Benefit           | Achieves parallel speed + correctness of autoregressive behavior         |

