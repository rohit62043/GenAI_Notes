# Exponentially Weighted Moving Average (EWMA)

## 📖 Introduction

In time series analysis and optimization algorithms, the **Exponentially Weighted Moving Average (EWMA)** is a crucial technique. It is used to smooth data, identify trends, and is widely applied in **deep learning optimizers** to enhance convergence.

---

## 🌀 What is EWMA?

- **Definition**: EWMA assigns exponentially decreasing weights to older observations, giving more importance to recent data points.
- Used in:
  - **Time series forecasting**
  - **Signal processing**
  - **Deep learning optimizers** (e.g., Momentum, Adam)

---

## 🧮 Mathematical Formula

The EWMA at time \( t \) is defined as:

\[
V_t = \beta \cdot V_{t-1} + (1 - \beta) \cdot X_t
\]

Where:
- \( V_t \): EWMA at time \( t \)
- \( X_t \): Current data point
- \( \beta \): Smoothing factor (\( 0 < \beta < 1 \))
- \( V_{t-1} \): Previous EWMA value

---

## 📊 Key Properties

- **Recent data** has **higher weight**.
- **Older data** decays exponentially.
- Smaller \( \beta \): Faster decay → more responsive.
- Larger \( \beta \): Slower decay → smoother trend.

---

## 🛠 Applications

1. **Time Series Analysis**
   - Smooth noisy data.
2. **Stock Market Trends**
   - Identify trends in price movements.
3. **Deep Learning Optimizers**
   - In Momentum and Adam optimizers, EWMA helps track gradients and adjust learning rates.

---

## 🚀 EWMA in Deep Learning

- **Momentum Optimizer**
  - EWMA used to smooth gradient updates.
- **Adam Optimizer**
  - Combines EWMA of gradients and squared gradients for adaptive learning rates.

---

## 📚 References

- [A Gentle Introduction to Exponential Moving Average](https://machinelearningmastery.com)
- [Adam: A Method for Stochastic Optimization (arXiv)](https://arxiv.org/abs/1412.6980)
- [Deep Learning Book by Goodfellow et al.](https://www.deeplearningbook.org/)

✅ *Understanding EWMA builds the foundation for advanced optimizers like Momentum and Adam.*

