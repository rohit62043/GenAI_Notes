# PyTorch Autograd - Educational Notes

## 1. Introduction to Autograd

Autograd is PyTorch's automatic differentiation engine. It tracks operations on tensors so gradients can be computed automatically for optimization.

**Key concept:** When you perform operations on tensors with `requires_grad=True`, PyTorch creates a computation graph, allowing `.backward()` to calculate gradients.

---

## 2. Creating Tensors with Gradient Tracking

```python
import torch

# Tensor with gradient tracking enabled
x = torch.ones(3, requires_grad=True)
print(x)
```

- `` → tells PyTorch to track operations on this tensor.

---

## 3. Performing Operations

```python
y = x + 2
print(y)
```

- Even simple addition creates a computation graph when `requires_grad=True`.

```python
z = y * y * 3
out = z.mean()
print(out)
```

- PyTorch keeps track of these operations.

---

## 4. Computing Gradients

```python
out.backward()  # Computes d(out)/dx
i = x.grad
print(i)
```

- `.backward()` → Triggers backpropagation.
- `.grad` → Returns gradients for `x`.

**Gradient meaning:** The gradient tells how much `out` changes for a small change in `x`.

---

## 5. Stopping Gradient Tracking

Sometimes, we don't need gradients:

```python
with torch.no_grad():
    y = x * 2
```

Or:

```python
x.requires_grad_(False)
```

- Disables autograd to save memory & computation.

---

## 6. Example: Gradient Calculation

```python
a = torch.randn(2, 2, requires_grad=True)
b = a * 3
c = b.mean()
c.backward()
print(a.grad)
```

- This computes the derivative of `c` with respect to `a`.

---

## 7. Summary Table

| Function           | Purpose                                |
| ------------------ | -------------------------------------- |
| `.backward()`      | Performs backpropagation               |
| `.grad`            | Accesses computed gradients            |
| `requires_grad_()` | Changes gradient tracking status       |
| `torch.no_grad()`  | Temporarily disables gradient tracking |

---

**Key Takeaway:** PyTorch autograd builds and maintains a computation graph for tensors that require gradients, enabling efficient and automatic differentiation, essential for training neural networks.

