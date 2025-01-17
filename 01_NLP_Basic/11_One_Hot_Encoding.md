# One-Hot Encoding in NLP

## Overview

In this video, we explore the concept of one-hot encoding, a technique for converting text into numerical vectors. We will understand its theoretical basis and practical implementation.

## Text Example

Consider the following text documents:

- **Document 1**: "The food is good"
- **Document 2**: "The food is bad"
- **Document 3**: "Pizza is amazing"

## Vocabulary

To use one-hot encoding, first identify the unique vocabulary from the corpus:

- **Vocabulary**: [the, food, is, good, bad, pizza, amazing]

This vocabulary has 7 unique words.

## One-Hot Encoding Process

1. **Determine the Vocabulary Size (V)**:

   - For our example, V = 7.

2. **Create Binary Vectors**:
   - Each word is represented by a binary vector of length V.
   - A vector is all zeros except for the position of the word in the vocabulary, which is set to 1.

### Example: Document 1 - "The food is good"

- **Vocabulary**: [the, food, is, good, bad, pizza, amazing]

  - "The" → [1, 0, 0, 0, 0, 0, 0]
  - "Food" → [0, 1, 0, 0, 0, 0, 0]
  - "Is" → [0, 0, 1, 0, 0, 0, 0]
  - "Good" → [0, 0, 0, 1, 0, 0, 0]

  Resulting Matrix for Document 1:

  ```
  [[1, 0, 0, 0, 0, 0, 0],
  [0, 1, 0, 0, 0, 0, 0],
  [0, 0, 1, 0, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0]]
  ```

### Example: Document 2 - "The food is bad"

- **Vocabulary**: [the, food, is, good, bad, pizza, amazing]
- "The" → [1, 0, 0, 0, 0, 0, 0]
- "Food" → [0, 1, 0, 0, 0, 0, 0]
- "Is" → [0, 0, 1, 0, 0, 0, 0]
- "Bad" → [0, 0, 0, 0, 1, 0, 0]

Resulting Matrix for Document 2:

```
[[1, 0, 0, 0, 0, 0, 0],
[0, 1, 0, 0, 0, 0, 0],
[0, 0, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0, 0]]
```

## Shape of the Vectors

- For each document, the shape is `number of words x vocabulary size`.
- Example for Document 1: 4 words × 7 vocabulary size = 4 × 7 matrix.

## Advantages and Disadvantages

- **Advantages**:
- Simple to implement and understand.
- Straightforward representation of words.

- **Disadvantages**:
- High dimensionality with large vocabularies.
- Inefficient for capturing semantic meaning.
- Sparse representation with many zeros.

## Next Steps

In the next video, we will discuss alternative techniques like Bag of Words (BoW) and TF-IDF, which address some of the limitations of one-hot encoding.
