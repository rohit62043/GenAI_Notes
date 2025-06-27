# Transformer Decoder Architecture: Detailed Study Notes

## 1. Introduction to Decoder Architecture

- **Speaker**: Nitish
- **Focus**: Decoder part of Transformer (Training Phase)
- **Pre-requisite**: Prior 12 videos for understanding encoder
- **Difference Between Training and Inference**:
  - *Training*: Decoder is non-autoregressive
  - *Inference*: Decoder is autoregressive
- **Video Plan**:
  - Simplified overview of decoder
  - Detailed explanation of decoder components
  - Real-world example application (English to Hindi translation)

---

## 2. Simplified Transformer Overview

- **Architecture Metaphor**: Big box (Transformer) contains Encoder and Decoder boxes
- **Encoder**:
  - 6 stacked encoder blocks
  - Each block: Self-attention + Feed-forward NN
  - Same architecture, different parameter values
- **Decoder**:
  - 6 decoder blocks
  - Input: Encoder output
  - Output: Final prediction

---

## 3. Decoder Block Components

- Each decoder block has 3 parts:
  1. Masked Multi-head Self-Attention
  2. Cross-Attention (Encoder-Decoder Attention)
  3. Feed-forward Neural Network

- **6 blocks** total, connected sequentially
- Understanding one block = Understanding all blocks

---

## 4. Application Example: English to Hindi Translation

- **Dataset**: English-Hindi sentence pairs
- **Encoder**:
  - Processes English sentence
  - Generates contextual embeddings for each token
- **Decoder**:
  - Uses embeddings + target Hindi sentence (during training)

---

## 5. Decoder Input Processing Steps

1. **Shift Right**:
   - Add `<start>` token
   - Move sentence one step right

2. **Tokenization**:
   - Break sentence into individual tokens

3. **Embedding**:
   - Each token -> 512-dimensional vector

4. **Positional Encoding**:
   - Injects positional info into embeddings
   - Added to embedding vectors

Result: Input vectors for decoder's first block

---

## 6. Masked Multi-head Attention

- Inputs: x1, x2, x3, x4 → Outputs: z1, z2, z3, z4
- **Masking**:
  - Prevents decoder from seeing future tokens
- **Residual Connection**:
  - Add input vector to attention output → z'
- **Layer Normalization**:
  - Normalize after addition
  - Keeps training stable

---

## 7. Cross Attention Mechanism

- **Two Inputs**:
  - From decoder masked attention (query)
  - From encoder output (key, value)
- **Mechanism**:
  - Decoder output = Query
  - Encoder output = Key, Value
  - Compute attention using all three

- **Process**:
  - Output contextual vectors (J_CV)
  - Add with previous layer output (residual)
  - Normalize again

---

## 8. Feed Forward Neural Network (FFN)

- **Two Layers**:
  1. Linear(512 → 2048) + ReLU
  2. Linear(2048 → 512) + No activation

- **Parameters**:
  - First layer: 512x2048 weights + 2048 biases
  - Second layer: 2048x512 weights + 512 biases

- **Batch Processing**:
  - 4x512 input → 4x2048 → ReLU → 4x512

- **Residual + Layer Norm**:
  - Add input vectors + FFN output
  - Normalize the result

Result: Final output of one decoder block

---

## 9. Full Decoder Stack

- Repeats all 3 steps (Masked Attention, Cross Attention, FFN) across 6 blocks
- Each block has independent weights
- Output of one feeds into the next

---

## 10. Decoder Output Layer

- **Input**: Final output from 6th decoder block (e.g., y_f1_norm, y_f2_norm)
- **Two Layers**:
  1. Linear Layer:
     - Input: 512-d
     - Output: Vocabulary size 'v'
     - Weights: 512 x v
     - Biases: v
  2. Softmax Layer:
     - Converts raw scores to probability distribution over vocabulary

- **Prediction**:
  - Token vector × weight matrix → score vector (1 x v)
  - Apply softmax → probability
  - Token with highest probability is chosen

---

## 11. Final Recap

- **Input Processing**:
  - Shift right → Tokenize → Embed → Positional Encoding
- **Decoder Block Flow**:
  - Masked Attention → Norm
  - Cross Attention → Norm
  - FFN → Norm
- **6 Blocks Total**: Each processes outputs from previous
- **Output Layer**:
  - Linear → Softmax
  - Predict token with highest probability

---

## 12. Next Steps

- This video covers decoder during *training*
- Next video will explore *inference* where decoder behaves *autoregressively*
- Encoder remains unchanged during inference

