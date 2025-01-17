# Notes on LSTM RNN Architecture

## Overview

- LSTM RNN (Long Short-Term Memory Recurrent Neural Network) is a type of RNN designed to overcome the limitations of traditional RNNs, such as short-term memory.

## Key Components of LSTM

1. **Forget Gate**

   - Determines which information to discard from the long-term memory.
   - Involves input from the current state (`x_t`) and the hidden state of the previous timestamp (`h_(t-1)`).
   - Uses a sigmoid activation function to decide what to forget.

2. **Input Gate and Candidate Memory**

   - Responsible for deciding which new information to store in the memory.
   - Involves two main operations:
     - Candidate memory update.
     - Input gate update.

3. **Output Gate**
   - Controls the output from the current cell.
   - Combines the hidden state and memory cell information to produce the output.

## LSTM Workflow

- Input at each timestamp:
  - `x_t`: Input at time `t` (e.g., a word).
  - `h_(t-1)`: Hidden state from the previous timestamp.
  - `c_(t-1)`: Memory cell from the previous timestamp (long-term memory).
- Operations involve:
  - **Combining** inputs and applying **activation functions** (sigmoid or tanh).
  - **Point-wise operations** (e.g., multiplication, addition).
  - **Updating memory cell (`c_t`)** with relevant context for long-term memory.
  - Generating the new hidden state (`h_t`) for the next timestamp.

## Notations

- **Neural Network Layer**:
  - Represents a hidden layer with neurons that apply specific activation functions (e.g., sigmoid or tanh).
- **Point-wise Operations**:
  - **Multiplication**: Element-wise product of two vectors.
  - **Addition**: Element-wise sum of two vectors.
  - **Activation (tanh)**: Applies the `tanh` function element-wise to a vector.
- **Concatenation**:
  - Combines two vectors into one larger vector without altering individual elements.
  - Example: Vectors `[1, 2, 3]` and `[4, 5, 6]` combine to form `[1, 2, 3, 4, 5, 6]`.

## Memory Cell (`c_t`)

- **Purpose**: Stores long-term information.
- **Process**:
  - `c_(t-1)`: Previous memory cell.
  - `c_t`: Updated memory cell after adding/removing relevant information.

## Basic Operations

1. **Vector Transfer**: Movement of data between components.
2. **Copying**: Duplicating data for reuse.
3. **Concatenation**: Combining vectors into a single vector.

---

## Next Steps

- Deep dive into the **Forget Gate**:
  - Discuss its role and internal operations in detail.
  - Understand its impact on memory cell updates.
- Explore **Input Gate**, **Candidate Memory**, and **Output Gate** in subsequent sections.

---

Thank you!
