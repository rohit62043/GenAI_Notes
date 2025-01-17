# Notes: Average Word2Vec and Spam-Ham Classification

## Introduction to Average Word2Vec:

- **Average Word2Vec** is important for solving classification problems.
- **Word2Vec** alone converts individual words into vectors, but for sentence-level classification, we need to combine these vectors into one.
- The solution is **averaging** the Word2Vec vectors for each word in a sentence, creating one vector per sentence.

### Steps in Average Word2Vec:

1. **Word2Vec Representation**:
   - Each word in a sentence is converted into a 300-dimension vector (in the case of using Google's pre-trained Word2Vec).
   - For instance, the sentence `"The food is good"` would have four separate 300-dimension vectors, one for each word.
2. **Problem**:
   - Every word is converted into a separate vector, but we need **one vector** to represent the entire sentence.
3. **Solution**:
   - Compute the **average** of all the word vectors in the sentence.
   - This creates a single 300-dimension vector representing the entire sentence.
   - This averaged vector can then be used as input for classification tasks.

---

## Example: Process of Average Word2Vec

1. For each sentence:
   - Convert each word to a vector using Word2Vec (e.g., 300 dimensions).
   - Average all the word vectors to get a single vector for the sentence.
2. The result:
   - For each document or sentence, we get one vector (e.g., of 300 dimensions).
   - This single vector can then be passed into machine learning models for training and classification.

---

## Libraries and Implementation:

1. **Gensim**:

   - Gensim is a popular library for NLP and Word2Vec tasks.
   - **Pre-trained Word2Vec** (Google News dataset) can be used for converting words to vectors.

2. **Key Steps**:
   - Import the **Word2Vec model** using Gensim.
   - Load the **Google pre-trained Word2Vec** model or train a Word2Vec model from scratch.
   - Convert the sentences into vectors by averaging word vectors.

---
