# Keras Functional Model | How to Build Non-linear Neural Networks

## Introduction

The **Keras Functional API** is a way to create models that are more flexible than the **Sequential API**. It allows the creation of complex architectures like multi-input/output models, shared layers, and non-linear topologies (like residual networks). While the **Sequential API** is limited to linear stacks of layers, the Functional API can handle models where layers connect in arbitrary ways.

---

## The Problem with Sequential Model

The **Sequential model** in Keras is simple but rigid, making it difficult to build non-linear models, multi-input/output networks, or shared layer models. It only supports models that consist of a linear stack of layers, which limits its use for more complex architectures.

**Limitations:**

- Inability to handle models with multiple inputs or outputs.
- Cannot build models with layers that have multiple connections (like residuals or shared layers).
- Does not support non-linear architectures.

---

## A Simple Example

The **Functional API** enables us to define a model where inputs and outputs may have multiple connections or even share the same layer. Here's an example of a simple neural network using the Functional API.

### Example:

Suppose we want to create a model where:

- We have two inputs (e.g., for two different feature sets).
- These inputs are processed by separate layers and later merged.

---

## Code Implementation

```python
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.models import Model

# Define two inputs
input_1 = Input(shape=(32,))
input_2 = Input(shape=(32,))

# Define the layers for the first input
x1 = Dense(64, activation='relu')(input_1)

# Define the layers for the second input
x2 = Dense(64, activation='relu')(input_2)

# Merge the outputs of both models
merged = keras.layers.concatenate([x1, x2])

# Add a final dense layer
output = Dense(1, activation='sigmoid')(merged)

# Create the model
model = Model(inputs=[input_1, input_2], outputs=output)

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# View the model summary
model.summary()
```

## Complex Examples

The **Functional API** allows for more sophisticated architectures. Let's explore some examples.

### Multi-Input Model:

In this case, a model accepts multiple inputs, each processed by different layers, and combines the learned features at some point.

### Multi-Output Model:

A **multi-output model** is one that can make predictions for multiple targets. For instance, a model might predict both the price of a house and the likelihood of the house selling within 30 days. In such a case, the network may share layers at the beginning and split into multiple branches for different tasks.

---

### Multi-Output Model Example

```python
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.models import Model

# Input layer
input_layer = Input(shape=(64,))

# Shared layers
shared = Dense(128, activation='relu')(input_layer)

# Output 1: Regression output for house price
output_1 = Dense(1, name='price_output')(shared)

# Output 2: Binary output for likelihood of sale
output_2 = Dense(1, activation='sigmoid', name='sale_output')(shared)

# Create the model with two outputs
model = Model(inputs=input_layer, outputs=[output_1, output_2])

# Compile the model with different losses for each output
model.compile(optimizer='adam',
              loss={'price_output': 'mse', 'sale_output': 'binary_crossentropy'},
              metrics={'price_output': 'mae', 'sale_output': 'accuracy'})

# View the model summary
model.summary()
```
