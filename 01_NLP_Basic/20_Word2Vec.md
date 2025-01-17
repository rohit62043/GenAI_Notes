# Word2Vec Overview

## Introduction

- Continuing the discussion on natural language processing (NLP).
- Focus on Word2Vec, a deep learning model for word embeddings.
- Word embeddings aim to convert words into vectors, maintaining their meanings.

## Definition

- **Word2Vec**: A word embedding technique published by Google in 2013.
- Uses a neural network model to learn word associations from a large corpus of text.
- Once trained, Word2Vec can detect synonyms, suggest additional words for partial sentences, and more.
- Represents each distinct word with a vector of numbers, capturing semantic meaning.

## Comparison with Previous Techniques

- Previous methods include Bag of Words, TF-IDF, which result in sparse matrices or decimal values.
- Word2Vec provides dense, meaningful vectors for each word.

## Feature Representation

- Words in the vocabulary are converted into vectors based on feature representations.
- Example features: gender, royal, age, food, etc.
- Each word is represented in a multi-dimensional space (e.g., 300 dimensions).

## Example Vocabulary and Features

- Vocabulary: `boy`, `girl`, `king`, `queen`, `apple`, `mango`.
- Feature representation example:
  - Gender: `boy` might be `[-1]`, `girl` `[1]`.
  - Royal: `boy` might be `[0.01]`.
  - Age: `boy` might be `[0.03]`.
- Vectors are learned from the corpus and reflect relationships between words.

## Practical Example

- Example calculation: `king - man + queen = woman`.
- Demonstrates how vector arithmetic can reveal relationships between words.

## Cosine Similarity

- Measures the angle between two vectors.
- Formula: `1 - cosine similarity`.
- Example calculations:
  - **45 degrees**: `cos(45) ≈ 0.7071`, distance = `1 - 0.7071 ≈ 0.2929`.
  - **90 degrees**: `cos(90) = 0`, distance = `1 - 0 = 1`.
  - **0 degrees**: `cos(0) = 1`, distance = `1 - 1 = 0`.

## Application in Recommendations

- Example: For a movie like "Avengers," similar movies (e.g., "Iron Man") would have vectors close to each other based on features like genre.

## Summary

- Word2Vec creates a feature representation for each word in a high-dimensional space.
- Next steps include understanding how feature representations are created and how vectors are trained in Word2Vec.
- Prerequisites: Knowledge of neural networks, loss functions, and optimizers.

## Next Video

- Discussion on how Word2Vec models are trained and practical implementations.
