# Transformer Architecture: Layer Normalization & Batch Normalization

## 🎓 Introduction to the Series

Nitesh welcomes viewers to the deep learning playlist focused on the **Transformer architecture**. He shares that the series has covered embeddings, attention mechanisms, and positional encoding, and the current focus is on the **final piece of the architecture: normalization**, specifically **Layer Normalization**.

---

## 🔑 Key Components of Transformers

- **Embeddings**
- **Self-Attention & Multi-Head Attention**
- **Positional Encoding**
- **Layer Normalization** ← **Current Focus**

---

## 📚 What is Normalization?

Normalization is the process of transforming data to have specific statistical properties. In deep learning, it helps:

- Stabilize training
- Speed up convergence
- Prevent issues like vanishing/exploding gradients

### 🧮 Types of Normalization

- **Standardization**: Subtract mean, divide by std deviation
- **Min-Max Scaling**: Scale between fixed min & max range

### 📌 Normalization Targets:

- **Inputs** (features like f1, f2)
- **Activations** of **hidden layers**

---

## ✅ Benefits of Normalization

1. Training becomes stable
2. Faster convergence
3. Mitigates **Internal Covariate Shift**
4. Acts as a form of **Regularization**

### 🔍 Internal Covariate Shift:

- During training, weight updates cause changes in layer activations' distributions
- Causes unstable training and poor generalization

---

## 🧪 Batch Normalization (BN)

### 💡 Concept:

- BN normalizes activations across **batch dimension**
- Mean and variance are computed **per feature** over the batch

### ⚙️ Steps:

1. Compute weighted sums \( z_1, z_2, z_3, \ldots \)

2. Normalize using mean \( \mu \) and standard deviation \( \sigma \):

   $$
   z_{\text{norm}} = \frac{z - \mu}{\sigma}
   $$

3. Scale and shift using learnable parameters \( \gamma \), \( \beta \):
   $$
   z_{\text{scaled}} = \gamma \cdot z_{\text{norm}} + \beta
   $$

### ❌ Why BN Fails in Transformers:

- Transformers process **sequential data** (varying length)
- Padding causes skewed stats (means, std dev)
- BN fails when multiple sequences have different lengths and padding

---

## ✅ Layer Normalization (LN)

### 💡 Concept:

- LN normalizes **per data point**, **across features**
- Better suited for sequences and attention mechanisms

### ⚙️ Steps:

1. For each vector:

   $$
   \mu = \frac{1}{d} \sum_{i=1}^{d} x_i,\quad
   \sigma = \sqrt{\frac{1}{d} \sum_{i=1}^{d}(x_i - \mu)^2}
   $$

2. Normalize:

   $$
   x' = \frac{x - \mu}{\sigma}
   $$

3. Apply learnable scale and shift:
   $$
   \text{LN}(x) = \gamma \cdot x' + \beta
   $$

### ✅ Why LN is Better for Transformers:

- No dependence on batch size
- Handles padding effectively
- Doesn’t get affected by sentence length

### 📌 Visualization:

Given input embedding of shape `(seq_len × d_model)`:

- **BatchNorm** computes stats across batch dimension (bad for padded sequences)
- **LayerNorm** computes stats across feature dimension (independent of padding)

---

## 🔁 Batch vs Layer Normalization

| Feature                   | Batch Norm      | Layer Norm        |
| ------------------------- | --------------- | ----------------- |
| Normalizes over           | Batch dimension | Feature dimension |
| Sensitive to batch size?  | ✅ Yes          | ❌ No             |
| Handles padding well?     | ❌ No           | ✅ Yes            |
| Suitable for Transformers | ❌ No           | ✅ Yes            |

---

## 🔚 Conclusion

- **Layer Normalization** is preferred in Transformer architectures
- It ensures **stable training**, handles **padded sequences**, and works **independently of batch size**
- The series now transitions into applying these components to understand the **complete Transformer architecture**.

👉 If you're interested in the decoder or further architecture walkthrough, stay tuned for the next video.
