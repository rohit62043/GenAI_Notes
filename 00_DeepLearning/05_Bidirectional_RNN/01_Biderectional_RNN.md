# **NLP with Deep Learning – Bidirectional RNNs**

This lecture builds on previous discussions about **Recurrent Neural Networks (RNNs), Long Short-Term Memory (LSTM), and Gated Recurrent Units (GRUs)**. The focus is on **Bidirectional RNNs**, why they are useful, and how they work.

---

## **1. Recap of Previous Concepts**

### **1.1 Simple RNN**

- **Structure:**

  - Takes a sequential input (e.g., words in a sentence) and processes one element at a time.
  - Maintains a **hidden state** that carries information from previous timesteps.
  - Uses an **activation function (sigmoid/tanh)** to compute the hidden state.
  - Produces an **output** at each timestep or at the final timestep (depending on task).

- **Issues with Simple RNNs:**
  - Struggles with long sequences due to the **vanishing gradient problem**.
  - Cannot retain long-term dependencies well.

### **1.2 LSTM & GRU**

- **LSTM (Long Short-Term Memory):**

  - Introduces **cell state** and **gates (input, forget, and output gates)**.
  - Retains long-term dependencies by controlling what information to keep or forget.
  - Mitigates the vanishing gradient problem.

- **GRU (Gated Recurrent Unit):**
  - A simplified version of LSTM with **reset and update gates**.
  - Fewer parameters than LSTM, making it computationally more efficient.

---

## **2. Understanding Bidirectional RNNs**

### **2.1 Why Do We Need Bidirectional RNNs?**

- In traditional RNNs (including LSTM and GRU), information flows **only from past to future**.
- However, in many NLP tasks, **context from both past and future words** is essential.
  - Example:
    - Sentence: **"Krish eats \_\_ in Bangalore."**
    - To predict the missing word, we need to consider:
      - **Previous words**: "Krish eats" → Suggests it might be food-related.
      - **Future words**: "in Bangalore" → Helps in determining what food is popular in Bangalore (e.g., "dosa").
    - A **unidirectional RNN** will only have past information and may miss important context.

### **2.2 How Bidirectional RNNs Work**

- A **Bidirectional RNN (BiRNN)** processes input in **two directions**:
  - **Forward RNN:** Reads input **from left to right** (past to future).
  - **Backward RNN:** Reads input **from right to left** (future to past).
- At each timestep, the **outputs from both directions** are combined to make a final prediction.

#### **Architecture of BiRNN**

1. The input sequence is passed **twice**:
   - First, through a **forward RNN**.
   - Second, through a **backward RNN**.
2. The hidden states from both RNNs are **concatenated** or **summed** to form the final hidden state.
3. The final hidden states are used to generate output.

**Mathematical Representation:**

- Forward hidden state:
  ```math
  h_t^{\rightarrow} = f(W_x x_t + W_h h_{t-1}^{\rightarrow} + b_h)
  ```
- Backward hidden state:
  ```math
  h_t^{\leftarrow} = f(W_x x_t + W_h h_{t+1}^{\leftarrow} + b_h)
  ```
- Final output:
  ```math
  y_t = g(W_o [h_t^{\rightarrow}, h_t^{\leftarrow}] + b_o)
  ```

---

## **3. Types of RNN Architectures**

### **3.1 One-to-One (1-to-1)**

- **Example:** Standard feedforward networks.
- **Use Case:** Simple classification tasks.

### **3.2 One-to-Many (1-to-M)**

- **Example:** Image captioning.
- **Use Case:** One image generates a sequence of words.

### **3.3 Many-to-One (M-to-1)**

- **Example:** Sentiment analysis.
- **Use Case:** A sequence of words maps to a single sentiment score.

### **3.4 Many-to-Many (M-to-M)**

- **Example:** Machine translation.
- **Use Case:** Input and output both have sequences of varying lengths.

---

## **4. Applications of Bidirectional RNNs**

### **4.1 Named Entity Recognition (NER)**

- Example:
  - **Input:** "Apple is looking to hire AI engineers in New York."
  - **Output:**
    - "Apple" → **ORG** (Organization)
    - "New York" → **LOC** (Location)

### **4.2 Part-of-Speech (POS) Tagging**

- Example:
  - **Input:** "She is running fast."
  - **Output:**
    - "She" → Pronoun
    - "is" → Verb
    - "running" → Verb
    - "fast" → Adverb

### **4.3 Machine Translation**

- Example:
  - **Input:** "Bonjour tout le monde."
  - **Output:** "Hello everyone."

### **4.4 Speech Recognition**

- Example:
  - **Input (Audio features over time)**: "H-e-ll-o"
  - **Output (Text transcription)**: "Hello"

---

## **5. Advantages & Disadvantages**

### **5.1 Advantages**

✅ **Better Context Understanding:** Uses both past and future context for better predictions.  
✅ **Useful for Sequence Labeling Tasks:** Like NER, POS tagging, and speech recognition.  
✅ **Improves Model Accuracy:** Especially in language modeling and translation tasks.

### **5.2 Disadvantages**

❌ **Increased Computational Cost:** Since it runs two RNNs instead of one.  
❌ **Higher Memory Usage:** Stores forward and backward states separately.  
❌ **Not Suitable for Real-Time Processing:** Requires the entire sequence before making predictions.

---

## **6. Conclusion**

- **Bidirectional RNNs improve NLP tasks** by considering both **past and future** context.
- They are widely used in **text processing, speech recognition, and language modeling**.
- **LSTMs and GRUs** can also be used in a bidirectional manner to improve performance.

---

This concludes the detailed notes on **Bidirectional RNNs and RNN Variants**. Let me know if you need further clarification or implementation details! 🚀
