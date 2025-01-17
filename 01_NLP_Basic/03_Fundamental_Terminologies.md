# Basic Terminologies in Natural Language Processing (NLP)

## Introduction

In this video, we will cover some fundamental terminologies essential for understanding NLP. These terminologies will be frequently used throughout the course, so it's crucial to grasp their meanings with some basic examples.

## Key Terminologies

### 1. **Corpus**

- **Definition**: A corpus is a large collection of text, often referred to as a paragraph or set of documents.
- **Example**: When you have a paragraph of text, it is generally called a corpus.

### 2. **Documents**

- **Definition**: A document refers to a sentence or a set of sentences within a corpus.
- **Example**: Each sentence in a paragraph can be considered a document.

### 3. **Vocabulary**

- **Definition**: Vocabulary is the set of all unique words present in a corpus.
- **Example**: If you have a dictionary, the vocabulary consists of all the unique words listed in that dictionary.

### 4. **Words**

- **Definition**: Words are the individual tokens or units that make up sentences within a corpus.
- **Example**: In a paragraph, each distinct word is considered separately as a word token.

## Tokenization

### What is Tokenization?

- **Definition**: Tokenization is the process of breaking down text into smaller components called tokens. Depending on the level of tokenization, these tokens can be sentences, words, or even characters.
- **Example**:
  - Converting a paragraph into sentences.
  - Converting sentences into individual words.

### Example of Tokenization

- Let's say we have the following paragraph:
- My name is Krish. I have an interest in teaching ML, NLP, and DL. I am also a YouTuber.

- **Paragraph to Sentences**:

  - **Token 1**: "My name is Krish."
  - **Token 2**: "I have an interest in teaching ML, NLP, and DL."
  - **Token 3**: "I am also a YouTuber."

- **Sentence to Words**:
  - **Token 1**: "My", "name", "is", "Krish"
  - **Token 2**: "I", "have", "an", "interest", "in", "teaching", "ML", "NLP", "and", "DL"
  - **Token 3**: "I", "am", "also", "a", "YouTuber"

### Why Tokenization is Important

- Tokenization is crucial in NLP as it is a foundational step in text preprocessing. Each word or sentence needs to be tokenized to facilitate further processing, such as converting words into vectors for machine learning models.

## Understanding Vocabulary with an Example

- Consider the following sentences:
- I like to drink apple juice. My friend likes mango juice.

- **Total Words**: 11 words.
- **Unique Words (Vocabulary)**: 9 unique words (after removing duplicates).

Vocabulary refers to these 9 unique words, which are the foundation of the paragraph.

## Conclusion

Understanding these basic terminologies—corpus, documents, vocabulary, and words—is essential for grasping more advanced concepts in NLP. Tokenization, as discussed, is a key process in breaking down text for further analysis.

## Next Steps

In the next video, we will explore how to perform tokenization using the NLTK library in Python.

---
