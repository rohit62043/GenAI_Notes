# Transformer Inference Architecture: Detailed Notes

## 1. Introduction

- **Presenter**: Nitesh
- **Topic**: Inference behavior of Transformer architecture
- **Context**: Final video of a 12–15 part series on Transformers
- **Focus**: Differences in decoder behavior during training vs inference

---

## 2. Teaching Strategy

- Transformer is broken down into smaller parts for teaching:
  - First: Encoder components and full encoder architecture
  - Then: Decoder components and full decoder architecture
- Previously covered: *Training phase*
- Current focus: *Inference phase*

---

## 3. Inference Setup: Machine Translation Example

- **Task**: Translate English to Hindi
- **Dataset**: ~100,000 English-Hindi sentence pairs
- **Example**: "We are friends" → Hindi
- After training, inference starts with input sentence passed to encoder

---

## 4. Encoder Behavior During Inference

- **Behavior**: Same during training and inference
- **Steps**:
  - Tokenize English input
  - Convert to embeddings
  - Add positional encoding
  - Process through 6 encoder blocks
    - Multi-head attention + Feed-forward + Norm
- **Output**: Context vectors for each token

---

## 5. Decoder Behavior: Training vs Inference

- **Training**:
  - Non-autoregressive
  - Full sentence (target Hindi) input at once

- **Inference**:
  - Autoregressive
  - One token generated at a time
  - No knowledge of future words

---

## 6. Decoder Start and Initial Input

- **Start**: SOS (Start of Sequence) token is input
- **Steps**:
  1. SOS token embedded to 512-d vector
  2. Positional encoding added
  3. Result = x1 → sent to decoder's masked attention block

---

## 7. Masked Self-Attention (Time Step 1)

- **Input**: x1
- **Operations**:
  - Compute Q, K, V from x1
  - Q·K → similarity → scaled → softmax → attention score
  - Attention score × V → z1
  - Residual connection: z1 + x1
  - Layer normalization → z1_norm

---

## 8. Cross-Attention (Time Step 1)

- **Query**: From decoder output (z1_norm)
- **Key/Value**: From encoder output
- **Steps**:
  - Q·K (between decoder & encoder) → scaled → softmax → weights
  - Weights × V (encoder values) → output vector z_c
  - Residual connection: z_c + z1_norm → normalization → final output

---

## 9. Feed-Forward Neural Network

- **Structure**:
  - Input: 512-d
  - Layer 1: 2048 neurons + ReLU
  - Layer 2: 512 neurons + Linear

- **Process**:
  - z_c → 2048-d → ReLU → 512-d → y1
  - Residual connection: y1 + z_c → layer norm → y1_norm

---

## 10. Output Prediction (Time Step 1)

- **Linear Layer**:
  - Input: y1_norm
  - Output: V-dimensional (size of Hindi vocabulary)

- **Softmax Layer**:
  - Converts raw scores to probability distribution
  - Highest probability → predicted token (e.g., 'हम')

---

## 11. Autoregressive Decoding: Time Step 2 and Beyond

- **Inputs**: SOS + previous output tokens (e.g., 'हम')
- **Embedding**: Tokens → 512-d vectors
- **Positional Encoding**: Applied to each position
- **Masking**: Future tokens masked (triangular matrix)
- **Attention**:
  - Multi-head self-attention → cross-attention → FFN → output

- **Example Time Step 2**:
  - Input: SOS, 'हम'
  - Compute attention between:
    - SOS ↔ SOS, SOS ↔ 'हम'
    - 'हम' ↔ SOS, 'हम' ↔ 'हम'
  - Use masking to block future attention

---

## 12. Masking During Inference

- **Purpose**: Prevent attention to future tokens
- **Mechanism**:
  - Use upper-triangular matrix
  - Mask scores for future positions (set to -inf before softmax)

- **Consistency**: Same masking approach as in training

---

## 13. Final Decoder Output Process

- **After All 6 Blocks**:
  - Last token’s vector → Linear + Softmax
  - Highest probability → next predicted token (e.g., 'दोस्त')

- **Repeat**:
  - Inputs grow each step: SOS, 'हम', 'दोस्त', ...
  - Continue until <EOS> (end of sentence) token generated

---

## 14. Summary: Encoder vs Decoder (Inference)

- **Encoder**:
  - Same for training and inference
  - Processes entire input sentence once

- **Decoder**:
  - **Training**: Non-autoregressive, all tokens known
  - **Inference**: Autoregressive, token-by-token generation
  - Masking is crucial in both modes

---

## 15. Conclusion and Future Topics

- **Series Recap**:
  - Covered full transformer architecture (training + inference)
- **Upcoming Topics**:
  - GPT, BERT, fine-tuning methods
- **Call to Action**:
  - Like, subscribe, and stay tuned for more content

