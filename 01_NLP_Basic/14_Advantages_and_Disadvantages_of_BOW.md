# Advantages and Disadvantages of Bag of Words (BoW)

## Advantages

1. **Simple and Intuitive**

   - Bag of Words is straightforward to implement and understand.
   - Converts text into a fixed-size vector representation.

2. **Fixed Size Input**
   - Unlike one-hot encoding, BoW ensures that each sentence is converted into a vector of fixed size based on the vocabulary.
   - Facilitates training with machine learning algorithms by providing consistent input dimensions.

## Disadvantages

1. **Sparse Matrix**

   - BoW creates sparse matrices where the majority of values are zero.
   - For large vocabularies, this can lead to inefficiency and high-dimensional feature space, potentially causing overfitting.

2. **Loss of Word Order**

   - BoW ignores the order of words, which means that the meaning can change based on word sequence.
   - Example: "good boy" vs. "boy good" results in the same vector representation despite different meanings.

3. **Out of Vocabulary (OOV) Issue**

   - New or unseen words in the test data that were not in the training vocabulary are ignored.
   - Important words in new data may be excluded from the feature representation.

4. **Limited Semantic Information**
   - BoW captures only the presence or frequency of words but does not account for the semantic meaning or context.
   - Example: Sentences with similar vectors but different meanings (e.g., "The food is good" vs. "The food is not good") can be misleading.

## Summary

- Bag of Words provides a basic and effective way to convert text into vectors but comes with limitations regarding word order, semantic meaning, and vocabulary management.
- Advanced techniques such as Word2Vec and other word embeddings address these issues by capturing context and meaning more effectively.

## Next Steps

- The next video will demonstrate practical implementation of Bag of Words using `sklearn`.
