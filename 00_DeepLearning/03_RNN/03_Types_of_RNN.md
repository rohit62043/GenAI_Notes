# Types of Recurrent Neural Networks (RNNs)

In this session, we explore the different architectures of Recurrent Neural Networks (RNNs) based on input-output relationships. Specifically, we focus on:

1. **Many-to-One**
2. **One-to-Many**
3. **Many-to-Many**
4. **One-to-One**
   |

---

## 1. **Many-to-One Architecture**

⏰ **[03:18]**

### Definition:

- A sequence of inputs is mapped to a single output.

### Applications:

- **Sentiment Analysis**: Classifying a review as positive or negative.
- **Text Classification**: Categorizing documents into specific classes.

### Structure:

- **Input**: \( x_1, x_2, ..., x_T \)
- **Output**: \( y \) (a single prediction)

---

## 2. **One-to-Many Architecture**

⏰ **[07:29]**

### Definition:

- A single input produces a sequence of outputs.

### Applications:

- **Image Captioning**: Generating a sequence of words to describe an image.
- **Music Generation**: Producing music sequences from a single note or seed.

### Structure:

- **Input**: \( x \) (single input)
- **Output**: \( y_1, y_2, ..., y_T \) (sequence)

---

## 3. **Many-to-Many Architecture**

⏰ **[10:53]**

### Definition:

- Both input and output consist of sequences, which may or may not be of the same length.

### Subtypes:

1. **Sequence-to-Sequence**:

   - Input sequence \( x_1, x_2, ..., x_T \) is encoded into a fixed representation by an **Encoder**.
   - The **Decoder** takes this representation and generates the output sequence \( y*1, y_2, ..., y*{T'} \).

2. **Encoder-Decoder**:
   - Designed to handle tasks where input and output sequences have different lengths.
   - The **Encoder** processes the input into a context vector (compressed form), and the **Decoder** generates outputs step by step.

### Applications:

- **Machine Translation**: Translating a sentence in one language to another.
- **Speech Recognition**: Audio sequences converted into text sequences.

### Structure:

- **Input**: \( x_1, x_2, ..., x_T \)
- **Encoder**: Processes the input sequence into a **context vector**.
- **Decoder**: Generates \( y*1, y_2, ..., y*{T'} \) as the output sequence.
- **Output**: \( y*1, y_2, ..., y*{T'} \)

### Key Components:

- **Encoder**: Captures the input sequence information into a fixed-length context vector.
- **Decoder**: Generates the output sequence from the context vector.

---

## 4. **One-to-One Architecture**

⏰ **[19:52]**

### Definition:

- A single input maps to a single output.

### Applications:

- **Simple Regression Tasks**: Predicting a numeric output from a single input.
- **Binary Classification**: Determining a class from one input.

### Structure:

- **Input**: \( x \) (single input)
- **Output**: \( y \) (single output)

---

## 🎯 **Summary Table**

| Architecture    | Input            | Output           | Example Applications                     |
| --------------- | ---------------- | ---------------- | ---------------------------------------- |
| Many-to-One     | Sequence         | Single Output    | Sentiment Analysis, Text Classification  |
| One-to-Many     | Single Input     | Sequence         | Music Generation, Image Captioning       |
| Many-to-Many    | Sequence         | Sequence         | Machine Translation, Speech Recognition  |
| Variable-Length | Dynamic Sequence | Dynamic Sequence | Speech Recognition, Text Generation      |
| One-to-One      | Single Input     | Single Output    | Binary Classification, Simple Regression |

---

## 📌 **Key Takeaways**

- **Sequence-to-Sequence** and **Encoder-Decoder** are essential for handling variable-length Many-to-Many tasks.
- **Many-to-Many** tasks are crucial for applications like **Machine Translation** and **Speech Recognition**.
- Choosing the correct RNN architecture ensures model performance and efficiency.

---

🎥 **Watch the Full Video** for detailed explanations and visual insights!
