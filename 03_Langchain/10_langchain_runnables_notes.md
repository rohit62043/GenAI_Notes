# 📚 LangChain Runnables and Runnable Primitives – Detailed Notes

---

## 🔁 Introduction & Motivation

- **Video Continuation:** Focuses on _Runnables_, which standardize execution of all LangChain components.
- **Recap:** Previous videos covered chains, prompts, models, parsers, and retrievers—now shifting to execution model (`invoke`-based abstraction).

---

## 🤩 Problem with Early LangChain Components

- Components had **non-standard methods** like:
  - `.format()`
  - `.predict()`
  - `.parse()`
  - `.get_relevant_documents()`
- ❌ Difficult to chain and integrate in workflows.

### ✅ Solution: `Runnable` Abstract Class

- Introduced **standard **``** method**.
- All LangChain components now inherit from `Runnable`.
- Ensures **consistency and composability** across workflows.

---

## 🧠 Two Categories of Runnables

### 1. **Task-Specific Runnables**

- Designed for **specific operations**.
  - Prompt Templates
  - LLMs (like `ChatOpenAI`)
  - Parsers (e.g. `StrOutputParser`)
  - Retrievers

### 2. **Runnable Primitives**

- Low-level **workflow orchestration tools**:
  - `RunnableSequence`
  - `RunnableParallel`
  - `RunnableBranch`
  - `RunnableLambda`
  - `RunnablePassthrough`

---

## 🔗 `RunnableSequence`: Sequential Execution

### ➕ Purpose:

Connect multiple runnables **in order**.

### 🔍 Example:

- Input → Prompt → LLM → Parser → Output
- Extended version:
  - Joke → Explain Joke (multi-step chaining)

### 🔧 Syntax:

```python
chain = RunnableSequence([
    prompt,
    model,
    parser
])
```

---

## 🌐 `RunnableParallel`: Parallel Execution

### 🚀 Purpose:

Run **multiple chains concurrently** with the same input.

### 🔍 Example:

Generate both:

- Tweet
- LinkedIn Post from same topic input.

### 🔧 Syntax:

```python
chain = RunnableParallel({
    "tweet": tweet_chain,
    "linkedin": linkedin_chain
})
```

- Output is a dictionary with all results.

---

## 🔄 `RunnablePassthrough`: Identity Runnable

### 💡 Purpose:

Pass input **as-is** to the next step.

### 🔍 Example:

Used to print both:

- Original joke
- Its explanation

### 🔧 Usage:

```python
from langchain_core.runnables import RunnablePassthrough
pt = RunnablePassthrough()
```

---

## 🔢 `RunnableLambda`: Custom Python Functions

### 🚀 Purpose:

Convert **any Python function** into a Runnable.

### 🔍 Example:

- Clean messy user text (HTML, punctuation, emojis)
- Count words in LLM output

### 🔧 Syntax:

```python
word_count_fn = lambda x: len(x.split())
word_counter = RunnableLambda(word_count_fn)
```

---

## ⚖️ `RunnableBranch`: Conditional Logic

### 🚀 Purpose:

Create **if-else** style branching logic in workflows.

### 🔍 Example:

- Generate report → If >500 words → Summarize
- Else → Print as-is

### 🔧 Syntax:

```python
RunnableBranch([
  (lambda x: len(x.split()) > 500, summarize_chain),
  (lambda x: True, print_chain)  # default case
])
```

---

## 🔄 LCEL: LangChain Expression Language

### ✅ Purpose:

Declarative syntax to build chains using the **pipe (**``**) operator**.

### 🔧 Example:

```python
chain = prompt | model | parser
```

- Improves **readability and simplicity**.
- Currently supports **sequential** chains.

---

## 🌟 Summary

| Runnable Primitive  | Purpose                        | Use Case Example                    |
| ------------------- | ------------------------------ | ----------------------------------- |
| RunnableSequence    | Connect runnables sequentially | Joke → Explanation                  |
| RunnableParallel    | Run chains in parallel         | Tweet + LinkedIn                    |
| RunnablePassthrough | Pass data as-is                | Print original + transformed output |
| RunnableLambda      | Add custom Python logic        | Word count, text cleaning           |
| RunnableBranch      | Conditional logic (if-else)    | Summarize if long, else print       |

> ✅ Understanding runnables is key to building robust, modular, and scalable AI workflows in LangChain.

| Aspect              | **Chains** (Old Approach)                                                 | **Runnables** (Modern & Standardized)                                                                       |              |
| ------------------- | ------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ------------ |
| **Definition**      | Abstraction to connect multiple components in LangChain.                  | A _standard interface_ for any component (LLM, Prompt, etc.) to ensure consistent behavior via `.invoke()`. |              |
| **Flexibility**     | Limited to predefined patterns (like Sequential, Simple Chains).          | Highly flexible: support sequential, parallel, conditional, and custom logic using primitives.              |              |
| **Standardization** | Components used different method names (`.format()`, `.predict()`, etc.). | All components use `.invoke()` for a unified interface.                                                     |              |
| **Composability**   | Difficult to compose complex workflows (needed manual wiring).            | Easily composable into pipelines using primitives like `RunnableSequence`, `RunnableParallel`, etc.         |              |
| **Extensibility**   | Custom chains required more boilerplate code.                             | Runnables allow wrapping Python logic (with `RunnableLambda`) or branching (`RunnableBranch`) with ease.    |              |
| **Syntax Style**    | Imperative and class-based setup.                                         | Supports declarative chaining with **LCEL** using \`                                                        | \` operator. |
| **Evolution**       | Foundation for early LangChain demos.                                     | Backbone of modern LangChain apps — modular, robust, and scalable.                                          |              |
