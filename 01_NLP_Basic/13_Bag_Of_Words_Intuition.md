# Introduction to Bag of Words (BoW)

## Overview

The video covers the Bag of Words (BoW) technique for converting text into vectors, which is used for tasks such as sentiment classification and text classification.

## Steps to Implement Bag of Words

1. **Initial Data Preparation**:

   - **Example Dataset**:
     - Sentence 1: "He is a good boy."
     - Sentence 2: "She is a good girl."
     - Sentence 3: "Boy and girl are good."
   - **Output Labels**: All sentences are positive (label = 1).

2. **Text Preprocessing**:

   - **Lowercasing**:
     - Convert all words to lowercase to ensure consistency (e.g., "Boy" and "boy" are treated as the same word).
   - **Stop Words Removal**:
     - Remove common words like "he", "she", "is", "a" that do not contribute to the sentiment (e.g., "good boy" becomes the cleaned form for Sentence 1).

3. **Vocabulary Construction**:

   - Identify unique words across all sentences:
     - Vocabulary: ["good", "boy", "girl"]
   - Calculate frequency of each word:
     - "good": 3 times
     - "boy": 2 times
     - "girl": 2 times
   - Sort vocabulary by frequency if necessary.

4. **Vector Representation**:

   - Create a feature vector for each sentence based on the vocabulary:
     - **Sentence 1**: "good boy" → [1, 1, 0]
     - **Sentence 2**: "good girl" → [1, 0, 1]
     - **Sentence 3**: "boy girl good" → [1, 1, 1]

5. **Binary vs. Normal Bag of Words**:
   - **Binary BoW**:
     - Represents the presence or absence of words (1 if present, 0 otherwise).
     - Ignores the frequency of words.
   - **Normal BoW**:
     - Represents the frequency of words.
     - Allows for multiple counts (e.g., "good" appearing twice in a sentence will be recorded as 2).

## Summary

- Bag of Words converts text into vectors based on word presence and frequency.
- **Binary BoW** and **Normal BoW** handle word frequencies differently.
- BoW is useful for text classification tasks like sentiment analysis.

## Next Steps

- The next video will discuss the advantages and disadvantages of the Bag of Words technique, similar to the discussion on one-hot encoding.
