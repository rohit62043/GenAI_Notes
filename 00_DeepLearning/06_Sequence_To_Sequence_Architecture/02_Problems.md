# Encoder-Decoder (Seq2Seq) Architecture and Its Problems

## 🔹 Overview

- Discussing **encoder-decoder sequence-to-sequence architecture**
- Understanding its problems and how to fix them using **attention mechanism**

---

## 🔹 Encoder Structure

- Uses **LSTM (Long Short-Term Memory)** for sequence processing
- Each time step (t=1,2,3,4) takes an input and generates a hidden state
- Uses an **embedding layer** to convert words into vector representations

### 📌 Key Components of the Encoder

1. **Embedding Layer** → Converts words into dense vectors
2. **LSTM Layers** → Process sequences and generate hidden states
3. **Context Vector (C)** → Encapsulates sentence meaning into a fixed-size vector

---

## 🔹 Decoder Structure

- Takes the **context vector** from the encoder
- Generates output step-by-step using **LSTM layers**
- Uses **Softmax activation** to predict the next word
- The generated output is fed back into the decoder for the next prediction

---

## 🔹 Problem with Seq2Seq Architecture

### ❌ **Context Vector Bottleneck**

- The **entire sentence is represented by a single context vector (C)**
- Works well for **short sentences**, but fails for **longer sentences**
- The **BLEU score (performance metric for translation accuracy) drops** as sentence length increases

### 🔍 Why Does This Happen?

- The last hidden state (context vector) **retains more information** about the **recent words**
- Words from earlier in the sentence **lose importance** in long sequences
- This leads to **poor performance** on long text sequences

---

## 🔹 Solution: **Attention Mechanism**

- Introduces **additional context** instead of relying only on the **final context vector**
- Improves the model’s ability to focus on **relevant words** in long sentences
- Uses a **weighted sum of hidden states** instead of a single context vector

---

## 🔹 Introduction to Attention

- Based on the research paper **"Neural Machine Translation by Jointly Learning to Align and Translate"**
- Uses **Bidirectional LSTM** instead of a single-direction LSTM
- Allows decoder to focus on **important words dynamically** at each timestep

### 🎯 **Key Changes with Attention**

1. Instead of a **single context vector**, multiple context vectors are used
2. The decoder gets **more information from different parts of the sentence**
3. Improves accuracy for **longer sentences**

---

## 🔹 Next Steps

- In the next session, we will **deep dive into the Attention Mechanism**
- Understand **how it modifies the Encoder-Decoder architecture**
- Explore the **architecture diagram and implementation details**

---

## 🎯 Summary

✅ **Problem:** Traditional Seq2Seq models struggle with **long sentences**  
✅ **Reason:** The context vector loses **early sentence information**  
✅ **Solution:** **Attention Mechanism** dynamically assigns weights to different words  
✅ **Next Topic:** Understanding **how Attention improves Seq2Seq models**

---

📌 **Stay tuned for the next session on Attention Mechanism!** 🎥
