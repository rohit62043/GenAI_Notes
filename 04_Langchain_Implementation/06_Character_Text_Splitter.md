# Text Splitting Techniques: Recursive Character vs. Character Text Splitter

## Introduction

Hello everyone!

In this discussion, we will continue exploring **text splitting techniques**.

### Recap of Recursive Character Text Splitter

In the **previous video**, we covered the **Recursive Character Text Splitter** and its implementation.

#### Key Points:

- The **Recursive Character Text Splitter** is **recommended** for **generic text**.
- It is **parameterized by a list of characters** and splits text until chunks are small enough.
- The **default list** includes:
  - `/n` (new line)
  - Blank space
- This method **tries to keep paragraphs, sentences, and words together** for as long as possible.

### How Text is Split in Recursive Character Text Splitter

1. **By the list of characters** used for splitting.
2. **By measuring chunk size in number of characters**.

---

## Character Text Splitter

Now, in this video, we are discussing the **Character Text Splitter**.

### How It Works:

- **Splits text based on a given character sequence**.
- The **default character** used for splitting is `\n` (new line).
- The list of characters may include:
  - `/n`
  - Blank spaces
- Works by:
  1. **Splitting text using a single character separator**.
  2. **Measuring chunk size by number of characters**.

---
