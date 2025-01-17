# Lemmatization in NLP

## Introduction

In this video, we discuss **Lemmatization**, a technique used in Natural Language Processing (NLP) to obtain the root form of a word, unlike **Stemming** which can alter the word's meaning.

## Stemming Recap

- **Stemming**: Reduces a word to its root form using an algorithm.
- Disadvantage: It may not always produce meaningful or correct root forms, potentially changing the word's meaning.

## Lemmatization Overview

- **Lemmatization**: A technique that reduces words to their exact root form (lemma) while preserving meaning.
- Example:
  - "eating" becomes "eat"
  - "history" remains "history"
  - "goes" becomes "go"

## WordNet Lemmatizer

- The technique discussed uses the **WordNet Lemmatizer** from the NLTK library.
- **WordNet Lemmatizer**: Finds the root form (lemma) of a word by referring to a corpus (WordNet).
