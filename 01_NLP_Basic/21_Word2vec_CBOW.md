# Understanding Word2Vec: CBOW and Skip-Gram

## Introduction

In this video, we will continue our discussion on Word2Vec, focusing on how the Word2Vec model is created, including its deep learning architecture, inputs, outputs, and training processes.

### Prerequisites

Before diving into Word2Vec, it's essential to have some knowledge about loss functions and optimizers. If you're unfamiliar with these concepts, it's recommended to review them first.

### Pre-trained Models

Word2Vec can be used with pre-trained models, such as Google's, which is trained on 3 billion words. However, you can also train a model from scratch to understand how feature representations are created.

## Continuous Bag of Words (CBOW)

CBOW is one of the two Word2Vec models (the other being Skip-Gram). It works as follows:

1. **Corpus Example**

   - Example Corpus: "I neuron I neuron company is related to data science."
   - For simplicity, we will use a smaller corpus for illustration.

2. **Window Size**

   - Choose a window size (e.g., 5). This determines the number of surrounding words to consider around a central word.
   - The window size affects the input and output data for training.

3. **Data Preparation**

   - **Input and Output Generation:**
     - For each central word in the window, create input and output pairs.
     - Example with a window size of 5:
       - Input: `I neuron company` | Output: `is related to data science`
       - Next window: `neuron company is` | Output: `related to data science`
       - Continue sliding the window and create pairs.

4. **One-Hot Encoding**

   - Convert words into one-hot encoded vectors based on the vocabulary.
   - Example for words in a vocabulary of 7:
     - "I" → `[1, 0, 0, 0, 0, 0, 0]`
     - "neuron" → `[0, 1, 0, 0, 0, 0, 0]`
     - And so on.

5. **Neural Network Architecture**

   - **Input Layer:**
     - The input layer will have nodes equal to the window size, each representing one word's vector.
   - **Hidden Layer:**
     - The hidden layer size is equal to the window size.
     - Example: For a window size of 5, the hidden layer has 5 nodes.
   - **Output Layer:**
     - The output layer represents the vocabulary size, with each node corresponding to a word's vector.

6. **Training the Model**

   - **Forward Propagation:**
     - Pass the input vectors through the network to get predictions.
   - **Loss Calculation:**
     - Compare predictions with the actual output using a loss function.
   - **Backward Propagation:**
     - Adjust weights to minimize the loss using optimization techniques.

7. **Feature Representation**
   - The vector representation of each word is obtained by minimizing the loss.
   - Example: After training, "neuron" might be represented by a 5-dimensional vector.

### Summary

- CBOW is a simple fully connected neural network where each word's context helps predict the central word.
- The window size impacts the feature representation dimensions.
- Training involves forward and backward propagation to adjust weights and learn accurate word vectors.

## Next Steps

In the next video, we will discuss the Skip-Gram model and compare the advantages and disadvantages of CBOW and Skip-Gram.

Thank you for watching!
