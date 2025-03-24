# Transformers: What and Why?

## Introduction

Transformers are a type of deep learning model that leverage the **self-attention mechanism** to analyze and process natural language data. They are widely used for various applications, including **machine translation**, which is a type of **sequence-to-sequence task**.

## Sequence-to-Sequence (Seq2Seq) Tasks

- Seq2Seq tasks involve input and output sequences of varying lengths.
- Example: **Language Translation** (e.g., English to French in Google Translate).
- Input and output both consist of multiple words → **Many-to-Many Mapping**.
- As sentence length increases, accuracy must remain high.
- Transformers effectively handle these tasks.

## Encoder-Decoder Architecture

Before transformers, **encoder-decoder** models with **LSTMs** were used for Seq2Seq tasks:

### Basic Encoder-Decoder Architecture:

1. **Encoder:**

   - Takes input words sequentially (X1, X2, X3, ...).
   - Converts words into **vector representations** via an **embedding layer**.
   - Processes embeddings using **LSTM layers**.
   - Generates a **context vector** (C-vector) representing the entire sentence.

2. **Decoder:**
   - Uses the **context vector** to generate output sequences.
   - Processes the context vector using **LSTM layers**.
   - Predicts the output using a **Softmax layer**.

### Problems with Encoder-Decoder Architecture:

- **Context Vector Limitation**: As sentence length increases, the context vector fails to represent the entire sentence adequately.
- **Decreasing BLEU Score**: Accuracy drops for longer sentences.
- **Sequential Processing**: LSTM processes words one at a time based on timestamps, making training **slow and non-scalable**.

## Introduction of Attention Mechanism

To solve the **context vector limitation**, the **Attention Mechanism** was introduced:

- Instead of passing a single context vector, attention provides **additional context vectors** at each decoding step.
- Attention assigns **alignment scores** to words based on their relevance to the output.
- **Attention weights** determine the contribution of each input word to the output.

### Issues with Attention Mechanism

- Uses **Bi-directional LSTM (RNN)**, which still processes words sequentially.
- **Non-parallel Execution**: Words are sent based on timestamps, preventing efficient training on large datasets.
- **Limited Scalability**: Still slow for large datasets.

## Introduction of Transformers

To solve the limitations of **LSTM-based attention models**, **Transformers** were introduced:

- Transformers **do not use LSTMs or RNNs**.
- Instead, they use a **Self-Attention Module**.
- **All words are processed in parallel**, making training **scalable and efficient**.
- Requires **Positional Encoding** to retain word order information.

### Advantages of Transformers

1. **Parallel Processing**:

   - Unlike LSTMs, which process words sequentially, transformers process **all words at once**.
   - Improves training speed and scalability.

2. **Self-Attention Mechanism**:
   - Creates **contextual embeddings** for words.
   - Each word’s vector is influenced by its relationship with other words.
   - Allows **better understanding of context** in a sentence.

## Contextual Embeddings

Transformers create **contextual embeddings**, meaning:

- A word's vector representation is influenced by other words in the sentence.
- Example:
  - Sentence: "My name is Krish, and I play cricket."
  - Traditional embeddings (Word2Vec, GloVe) assign **fixed** vectors to words.
  - Transformers generate **dynamic** word vectors based on surrounding words.
  - Example: "I" and "Krish" have a strong correlation → affects vector representations.

## Impact of Transformers

- Enabled **state-of-the-art (SOTA) models** in NLP.
- Led to powerful models like **BERT, GPT**.
- Companies no longer need to train models from scratch → **Transfer Learning**.
- Used in **Multimodal tasks** (NLP + Image Processing):
  - Example: **DALL·E** (text-to-image generation by OpenAI).
- Integral to **Generative AI** and **Large Language Models (LLMs)**.

## Key Takeaways

1. Transformers solve **parallelization** and **contextual embedding** issues of previous models.
2. **Self-Attention Module** allows processing all words at once.
3. Contextual embeddings improve **word representations** based on relationships.
4. Transformers are the foundation of modern **Generative AI** and **LLMs**.

## Next Steps

- **Deep dive into Self-Attention Module**.
- **Understanding Positional Encoding**.
- **Exploring Transformer Architecture in detail**.

---

_Thank you! Stay tuned for more insights into Transformers!_
