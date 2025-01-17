# Natural Language Processing: Text Preprocessing Techniques

## Tokenization Recap

- **Tokenization** is the process of converting a paragraph into sentences, sentences into words, or words into tokens.
- Previously, we saw how to perform tokenization using **NLTK**.

## Introduction to Stemming

- **Stemming** is the process of reducing a word to its root or base form, known as the **word stem** or **lemma**.
- Stemming is crucial in **Natural Language Understanding (NLU)** and **Natural Language Processing (NLP)**.

### Stemming in Action

- Consider a sentiment classification problem where we determine if product reviews are positive or negative.
- Words like "eating," "eats," and "eaten" share the root "eat." Similarly, "going," "gone," and "goes" share the root "go."
- Stemming helps reduce these words to their base forms ("eat," "go"), thus simplifying the model's input features.
