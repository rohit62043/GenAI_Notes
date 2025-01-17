# Notes: Training Data with LSTM, RNN

## Key Concepts Discussed

### Architecture Recap

1. **LSTM Overview**:

   - Composed of **three gates**:
     - **Forget Gate**: Decides what information to discard.
     - **Input Gate**: Updates memory with new relevant information.
     - **Output Gate**: Outputs the final result based on the updated memory.
   - Two important memory lines:
     - **Long-Term Memory (Ct-1)**.
     - **Short-Term Memory (Ht-1)**.

2. **Example**:
   - Text-based prediction example:
     - Input: Reviews about food.
     - Output: Predict whether the food is "good" (1) or "bad" (0).

### Training Workflow

1. **Input Preparation**:

   - Convert text into vectors using an **embedding layer**.
   - Example embedding technique: **Word2Vec**.
     - Converts words into vectors based on relationships with specific features.

2. **Word-to-Vector Mapping**:
   - Example dimensions: 3D vector for "good," "bad," and "healthy."
   - Relationship scoring:
     - "Tasty": Good = 0.9, Bad = 0.0, Healthy = 0.1.
   - Words are processed one at a time and fed into the model.

### Processing Steps in LSTM

1. **Forget Gate**:

   - Filters irrelevant information from the memory cell.
   - Example: "Tasty and crispy" is added, while unrelated earlier information is forgotten.

2. **Input Gate**:

   - Adds relevant information to the memory cell.
   - Updates vectors based on new sentences:
     - Example: "Not good for health" reduces "Good" and increases "Bad."

3. **Candidate Memory Update**:

   - Combines new input with the previous memory.
   - Adjusts vectors to reflect the new context:
     - Example: "Made with whey protein and vegetables" increases "Healthy."

4. **Output Gate**:
   - Outputs the processed vector based on current memory states.
   - Updates **Short-Term Memory (Ht)** and **Long-Term Memory (Ct)**.

### Forward and Backward Propagation

- **Forward Propagation**:
  - Sequentially updates memory cells using input at each timestamp.
  - Adjusts vectors dynamically based on the sentence context.
- **Backward Propagation**:
  - Updates weights to minimize loss based on the error.

### Vector Dynamics

- Words like "Tasty" or "Not good" dynamically alter vectors for "Good," "Bad," and "Healthy."
- Memory cells prioritize context-relevant information:
  - Example:
    - Good = 0.9 → 0.7 (decreased due to negative context).
    - Bad = 0.0 → 0.4 (increased for negative context).

## Summary

1. LSTM manages both short-term and long-term dependencies in sequential data.
2. The **Forget Gate** filters irrelevant information, while the **Input Gate** ensures useful information is added.
3. Vectors for each word are dynamically updated to reflect evolving sentence context.
4. The training process involves continuous adjustments of weights through propagation.

### Next Steps

- Understanding vector adjustments during training with additional examples.
- Explore deeper details of embedding techniques like **Word2Vec**.

---
