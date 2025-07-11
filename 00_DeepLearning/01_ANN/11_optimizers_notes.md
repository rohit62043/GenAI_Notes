# Neural Network Training Optimization: Optimizers and Challenges

## 🧠 Introduction

In deep learning, training a neural network can often be slow and resource-intensive, especially for very deep architectures. This session discusses how to optimize neural network training by introducing **optimizers**, the challenges with conventional methods, and advanced techniques to improve speed and convergence.

---

## ⚡ Why Optimization Matters

- **Deep Neural Networks (DNNs)** with many layers take a lot of time to train.
- Scientists focus on techniques to **speed up training** without compromising accuracy.
- Three techniques discussed previously:
  1. **Weight Initialization**
  2. **Batch Normalization**
  3. **Choice of Activation Functions**
- Now moving to the **fourth and most critical technique**: **Optimizers**

---

## 🚀 What is an Optimizer?

- An **optimizer** helps update the weights and biases of a neural network to minimize the **loss function**.
- Goal: Find the most optimal parameter values (weights/biases) for which predictions are **closest to real values**.
- Optimizers use algorithms like **Gradient Descent** to iteratively improve parameter values.

---

## 📉 Gradient Descent (GD)

- Core idea: Start with random weights, compute gradients, and update weights to reduce loss.
- **Update Rule**:
  ```
  w_new = w_old - learning_rate * gradient
  ```
- Visualize as finding the lowest point (global minimum) on a 3D cost surface.

### Types of Gradient Descent

1. **Batch Gradient Descent**
   - Processes the **entire dataset** before each weight update.
2. **Stochastic Gradient Descent (SGD)**
   - Updates weights after **each data point**.
3. **Mini-Batch Gradient Descent**
   - Processes data in **small batches**.

---

## ⚠️ Challenges with Conventional Gradient Descent

### 1️⃣ Learning Rate Tuning

- Choosing the right **learning rate (LR)** is hard.
  - Too small → Slow convergence.
  - Too large → May overshoot or diverge.
- **Learning Rate Scheduling** helps but requires pre-defined schedules which may not adapt to all datasets.

### 2️⃣ Same Learning Rate for All Parameters

- In GD, **one global LR** is used for all weights.
- Problem: Some directions in parameter space may require **different step sizes**.

### 3️⃣ Local Minima and Saddle Points

- The cost surface may have many **local minima** and **saddle points**.
- GD can get stuck in these regions.

### 4️⃣ Data Dependency in Scheduling

- Pre-defined LR schedules might not generalize across different datasets.

---

## 🆕 Why Advanced Optimizers?

To overcome these challenges, advanced optimizers introduce:

- **Adaptive Learning Rates**
- **Momentum** to escape saddle points
- **Better convergence** in complex cost landscapes

---

## 🛠 Optimizers to Explore

1. **Momentum**
2. **Nesterov Accelerated Gradient (NAG)**
3. **RMSprop**
4. **Adam**
5. **AdaGrad**

These are refinements over gradient descent with tweaks like learning rate adaptation and momentum-based updates.

---

## 🌟 Next Step

In the upcoming sessions, we’ll cover:

- **Exponential Moving Average (EMA)**
- Advanced optimizers in detail (Momentum, Adam, etc.)

---

## 📚 References

- [Gradient Descent and its Variants (Paper)](https://arxiv.org/abs/1609.04747)
- [Adaptive Optimization Methods in Deep Learning (Paper)](https://arxiv.org/abs/1904.09237)
- [Deep Learning Book by Ian Goodfellow](https://www.deeplearningbook.org/)

---

✅ *Make sure you understand Gradient Descent well before proceeding to advanced optimizers.*

