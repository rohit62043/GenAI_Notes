## **Introduction**

Hello everyone!

In this discussion, we will explore how to **split JSON data** into smaller chunks.

### **Why Split JSON Data?**

- When dealing with **large API responses**, we need to split JSON data into **manageable chunks** before passing it to an LLM model.
- The **Recursive JSON Splitter** allows:
  - **Controlled chunk sizes** (min & max size).
  - **Preserving nested JSON objects** when possible.
  - **Splitting large JSON objects if required**.
  - **Combining with other text splitters** for better granularity.

---

## **How Does It Work?**

- It **traverses the JSON depth-first** and builds smaller JSON chunks.
- It attempts to keep **nested JSON objects intact**, but splits them if needed.
- It measures **chunk size by character count**.
- If a **string value is too large**, it remains **unsplit**.

---
