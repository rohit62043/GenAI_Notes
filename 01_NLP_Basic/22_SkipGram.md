## Natural Language Processing: Skipgram Architecture

In this video, we discuss the Skipgram architecture in natural language processing, comparing it to the Continuous Bag of Words (CBOW) model previously covered.

### Overview of Skipgram

- **Data Setup**: Let's consider the dataset where "Enron company is related to data science".
- **CBOW vs. Skipgram**:
  - **CBOW**: Input is the context (surrounding words), and output is the target word.
  - **Skipgram**: Input is a target word, and output is the context (surrounding words).

### Architecture Details

- **CBOW Input/Output**:

  - Input: Entire context window.
  - Output: Target word.

- **Skipgram Input/Output**:
  - Input: Target word.
  - Output: Context words.

**Example**:

- With a window size of 5:
  - **CBOW**: Input = Context (e.g., [Enron, company, is, related, to]), Output = Target word (e.g., "data").
  - **Skipgram**: Input = Target word (e.g., "data"), Output = Context words (e.g., [Enron, company, is, related, to]).

### Neural Network Structure

- **Input Layer**: Number of vectors corresponds to vocabulary size (e.g., 7 dimensions).
- **Hidden Layer**: Nodes corresponding to window size.
- **Output Layer**: Number of words in the context.

  - **Example**:
    - Input = [0010000] (for a word in the vocabulary).
    - Window Size = 5.
    - Weight Matrices:
      - Input to Hidden: 7 x 5
      - Hidden to Output: 5 x 7

### Training Process

- **Forward Propagation**:

  - Input vectors are multiplied by weights, bias is added, and activation functions are applied.
  - Softmax function is used to calculate the probability distribution for output words.

- **Loss Calculation**:
  - Loss function is computed.
  - Backward Propagation is used to minimize the loss by adjusting weights.

### When to Use CBOW vs. Skipgram

- **CBOW**: Best for smaller datasets.
- **Skipgram**: Suitable for larger datasets.

### Improving Performance

1. **Increase Training Data**: More data generally leads to better accuracy.
2. **Increase Window Size**: Larger window sizes increase vector dimensions and can improve performance.

### Pre-trained Models

- **Example**: Google Word2Vec trained on 3 billion words provides 300-dimensional feature vectors for words (e.g., "cricket").

### Upcoming Content

- **Next Video**: Implementation of Word2Vec using the Gensim library, including using pre-trained models and training on new datasets.
