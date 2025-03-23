# Encoder-Decoder Architecture with LSTMs

## Introduction

The Encoder-Decoder architecture is a key component of sequence-to-sequence models, commonly used in machine translation, text summarization, and other NLP tasks. It consists of two primary parts:

1. **Encoder**: Processes the input sequence and generates a context vector.
2. **Decoder**: Uses the context vector to generate the output sequence.

---

## 🏗 **Working of Encoder**

The encoder processes the input sentence word by word and generates a **context vector** that summarizes the input.

### Step-by-Step Process:

1. **Processing Each Word**:
   - Each word is passed sequentially into the LSTM.
   - The LSTM maintains **hidden state (HT)** and **cell state (CT)**.
2. **Passing Words into LSTM**:

   - The third word is passed into the third LSTM layer.
   - This continues until the end of the sentence is reached.

3. **Final Word Processing**:

   - The last word (End of Sentence - `EOS`) is passed.
   - The final **hidden state (HT)** and **cell state (CT)** are obtained.
   - These states form the **context vector**.

4. **Components of LSTM in Encoder**:

   - **Forget Gate**: Determines what information should be discarded.
   - **Input Gate**: Decides what new information should be stored.
   - **Output Gate**: Computes the final hidden state.

5. **Generating Context Vector**:
   - The final HT and CT values represent the **context vector**.
   - The context vector is passed to the decoder.

---

## 🏗 **Working of Decoder**

The decoder takes the context vector from the encoder and generates the target sequence.

### Step-by-Step Process:

1. **Passing Context Vector to Decoder**

   - The decoder receives the **CT and HT** from the encoder.

2. **Processing Output Words**

   - The decoder receives training data (e.g., translating "gracias" from English to Spanish).
   - The **first word (Start of Sentence - `SOS`)** is passed.
   - Words are converted into vector format (One-Hot Encoding / Embedding Layer).

3. **Softmax Activation in Decoder**

   - The decoder predicts words using a **fully connected layer with softmax activation**.
   - Softmax helps in **multi-class classification** by predicting the next word.

4. **Prediction Process**

   - Given a word, the model predicts the next word using softmax probabilities.
   - Example of probability values for three words:
     ```
     0.1 -> SOS
     0.6 -> Gracias
     0.3 -> EOS
     ```
   - The highest probability determines the predicted output.

5. **Backpropagation & Optimization**

   - The difference between **true output (Y truth)** and **predicted output (Y hat)** is computed.
   - The loss function (e.g., **MSE** or **Cross-Entropy**) is used to minimize errors.
   - The model updates weights using an **optimizer**.

6. **Iterative Prediction**
   - The correct output is passed as the next input (Teacher Forcing).
   - The process repeats until the **End of Sentence (`EOS`)** is reached.

---

## 🔄 **Forward & Backward Propagation**

- The entire model follows **forward propagation** during inference.
- **Backpropagation** is applied to update weights and reduce loss.
- If the predicted word is incorrect, weight adjustments are made for better predictions.

---

## 🏗 **Architecture Summary**

1. **Encoder**: Processes input sequence, generates context vector.
2. **Decoder**: Uses context vector to generate output sequence.
3. **Softmax Activation**: Determines the most probable next word.
4. **Loss Function**: Measures the difference between true and predicted values.
5. **Backpropagation**: Updates weights to improve predictions.

---

## 🎯 **Key Takeaways**

- The **context vector** is crucial for the decoder to generate meaningful outputs.
- **Softmax** helps in multi-class classification by assigning probabilities.
- **Loss optimization** ensures accurate predictions over time.
- The **encoder-decoder model** is widely used in NLP tasks like translation.

---

## 📌 **Next Steps**

In the next section, we will discuss the **problems** of the Encoder-Decoder architecture and explore improvements like **Attention Mechanism**.

🚀 _Stay tuned!_
