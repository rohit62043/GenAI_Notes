
# Transformer Architecture - Decoder and Cross Attention

## Overview

### Transformer Architecture Plan
- The speaker begins by outlining the plan for explaining the Transformer architecture.
- Rather than presenting the entire architecture in one video, the goal is to build understanding incrementally.
- Encoder components have been covered, and the decoder is now being studied.

## Completed Study of Encoder Components
- Topics covered:
  - Embeddings
  - Positional Encoding
  - Self-Attention
  - Multi-Head Attention
  - Normalization
- Encoder architecture is complete.
- Decoder introduction started in the previous video.

## Decoder Architecture and Cross Attention Block
- Decoder contains a special multi-head attention block.
- Unlike typical multi-head attention (where Q, K, and V come from the same source), in this block:
  - Q comes from the decoder
  - K and V come from the encoder

## Understanding Cross Attention

### Machine Translation Example
- Encoder processes English sentence: "I like eating ice cream."
- Encoder generates a summary or context vector.
- Decoder uses this summary to generate the Hindi sentence step-by-step:
  - Step 1: "mujhe"
  - Step 2: "ice cream"
  - Step 3: "khaane" etc.

### Factors Influencing Next Word in Decoder
1. Previously generated words (e.g., "mujhe", "ice cream")
2. Encoder output (context vector from English sentence)

## Decoder Output Depends on Generated Words and Input
- Decoder uses:
  - Self-attention for internal sequence context.
  - Cross-attention to relate generated output to the encoder's input.

### Matrix of Word Relationships
- A matrix quantifies relationships between input and output tokens.
- Cross-attention helps the decoder generate output that’s semantically aligned with the input.

## Cross Attention Mechanism

### Cross Attention vs Self-Attention
- Self-attention:
  - Input = one sequence (e.g., "we are friends")
  - Outputs contextual embeddings using Q, K, V from same source

- Cross-attention:
  - Q comes from the output sequence (e.g., Hindi)
  - K and V come from the input sequence (e.g., English)
  - Used to align and generate one sequence from another

## Differences Between Self-Attention and Cross-Attention

### Inputs
- Self-attention: One sequence for Q, K, V.
- Cross-attention: Two sequences — Q from decoder, K and V from encoder.

### Processing
- Both use dot product between Q and K, scaling, softmax, and weighted sum with V.

### Output
- Self-attention: Contextual embedding for each token in the same sequence.
- Cross-attention: Contextual embedding for each token in the output sequence based on input sequence.

## Self-Attention Calculations Recap

### Q, K, V Matrices
- W_Q, W_K, W_V are learnable matrices.
- Applied to embeddings to generate Q, K, V vectors.

### Attention Score Matrix
- Q.K^T to get scores (dot product similarity)
- Softmax applied to scores → attention weights
- Weights multiplied with V → contextual embeddings

## Cross-Attention Vector Calculations

### Query from Output Sequence
- Hindi word → Query vector

### Keys and Values from Input Sequence
- English words → Key and Value vectors

### Attention Matrix
- Dot product (Q.K^T), softmax, and scaling to get similarity scores
- Use attention weights to calculate weighted sum of value vectors

## Contextual Embedding Formation

### Self Attention
- Contextual embedding of a token = weighted sum of all embeddings in the sequence

### Cross Attention
- For each output word, contextual embedding is influenced by all input words
- Output = weighted combination of input sequence’s value vectors

## Relation to Traditional Attention Models

### Bag-of-Words and Long Attention
- Bag-of-words attention: Context vectors calculated using neural network similarity
- Long attention: Dot product similarity used instead
- Cross-attention is similar in function but adapted for transformers

## Encoder-Decoder Attention Mechanism

### Source of Q, K, V
- Q from decoder (output tokens)
- K and V from encoder (input tokens)
- Each output token attends to all input tokens

## Cross Attention in Multimodal Data

### Applications
- Machine translation
- Question answering
- Image captioning (image input, text output)
- Text-to-image generation
- Text-to-speech systems

## Importance of Cross Attention in Deep Learning

- Key for transformer models and large language models (LLMs)
- Essential for generative AI tasks
- Understanding cross attention deepens transformer architecture knowledge

## Closing Notes
- Speaker promises more detailed decoder architecture videos soon
- Encourages viewers to like, subscribe, and stay tuned
