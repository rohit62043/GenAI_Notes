# Differences Between LSTM and GRU

## 1. Number of Gates
- **LSTM**: Has three gates — *input (or update) gate*, *forget gate*, and *output gate*.
- **GRU**: Has two gates — *reset gate* and *update gate*.

## 2. Memory Units
- **LSTM**: Uses two separate states — the *cell state* (\(c_t\)) and the *hidden state* (\(h_t\)). The cell state acts as an "internal memory" and is crucial for carrying long-term dependencies.
- **GRU**: Simplifies this by using a single *hidden state* (\(h_t\)) to both capture and output the memory.

## 3. Parameter Count
- **LSTM**: Generally has more parameters than a GRU because of its additional gate and separate cell state.  
  For an input size of \(d\) and a hidden size of \(h\), the LSTM has:  
  \(4 \times ((d \times h) + (h \times h) + h)\) parameters.
- **GRU**: Has fewer parameters. For the same sizes, the GRU has:  
  \(3 \times ((d \times h) + (h \times h) + h)\) parameters.

## 4. Computational Complexity
- **LSTM**: Due to the extra gate and cell state, LSTMs are typically more computationally intensive than GRUs.
- **GRU**: Is simpler and can be faster to compute, especially on smaller datasets or when computational resources are limited.

## 5. Empirical Performance
- **LSTM**: In many tasks, especially more complex ones, LSTMs have been observed to perform slightly better than GRUs.
- **GRU**: Can perform comparably to LSTMs on certain tasks, especially when data is limited or tasks are simpler. They can also train faster due to fewer parameters.

## Notes
- The choice between LSTM and GRU often comes down to empirical testing. Depending on the task, either architecture could be more suitable.
