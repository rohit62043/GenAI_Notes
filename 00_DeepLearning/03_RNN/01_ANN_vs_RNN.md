# Sentiment Analysis using Neural Networks

## Problem Statement

We aim to perform **sentiment analysis** using text data. The example dataset contains sentences and outputs:

- **1** represents a positive sentiment.
- **0** represents a negative sentiment.

Example Dataset:  
| Sentence | Output |
|------------------------------|--------|
| The food is good | 1 |
| The food is bad | 0 |
| The food is not good | 0 |

---

## Key Issues with Artificial Neural Networks (ANN) for Sequential Data

### 1. **Text Preprocessing**

To use text in ANN, we need to convert text into vectors using:

- **Bag of Words (BoW)**
- **One-Hot Encoding**
- **TF-IDF (Term Frequency - Inverse Document Frequency)**

**Example of Bag of Words**:

- **Unique Words**: Food, Good, Bad, Not
- **Vector Representation**:
  - Sentence 1: `1100`
  - Sentence 2: `1010`
  - Sentence 3: `1011`

---

### 2. **Loss of Sequence Information**

- Words in sentences are not sequentially considered (e.g., `Food` comes first due to frequency).
- Sequence **context** is lost.
- For example:
  - `The food is not good` → Misinterpreted as `good`.

---

### 3. **Training with All Words at Once**

- In ANN, all words are passed **at once** during forward propagation.
- For sequential data, words should be passed **one at a time** (timestamp-based input).

---

## Why ANN Fails for Sequential Data

1. **Sequence Matters**: ANN does not retain the order of words.
2. **Context Loss**: ANN cannot understand relationships between words over time.
3. **No Memory**: ANN lacks memory to retain information about previous words.

---

## Solution: Recurrent Neural Networks (RNN)

- RNNs are specifically designed for sequential data.
- Words are passed **one by one** over time, and RNN maintains a **memory** of previous words.
