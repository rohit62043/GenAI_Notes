# 📘 LangChain Runnables - Complete Conceptual Notes

## 🎬 Introduction to LangChain and Runnables
- Nitesh introduces the LangChain playlist and focuses on a core concept called **Runnables**.
- Recap of earlier topics: chains like sequential, parallel, and conditional.
- Emphasizes Runnables as foundational units that make chains work effectively in LangChain.

---

## 📅 Background: Rise of LLM Apps and LangChain Motivation
### 📈 2022 and the OpenAI API Boom
- Public release of ChatGPT and OpenAI's API.
- Explosion in developer interest to build **LLM-based applications**.
- LangChain identified an opportunity to build a framework simplifying this.

### 🧩 Problem: Fragmented APIs
- Each LLM provider (OpenAI, Anthropic, Google) had different APIs.
- LangChain created a **unified interface** to interact with any LLM API seamlessly.

### 💡 Insight: LLM Calls are Just One Part
- Example: Building a PDF reader isn’t just about sending a query to an LLM.
- Additional steps: Load documents → Split → Embed → Store → Retrieve → Query.

---

## 🔧 LangChain Components (Modular Lego Blocks)
- Document Loaders
- Text Splitters
- Embedding Models
- Vector Stores
- Retrievers
- Output Parsers

These are plug-and-play components for building any LLM application.

---

## 🧪 Code Examples
### 1. Simple LLM App
- User inputs a topic.
- Prompt created → sent to LLM → Response displayed.

### 2. PDF Reader App
- Load documents
- Split text
- Generate embeddings
- Store in vector database
- Retrieve relevant chunks
- Query LLM with the chunk

---

## 🔁 Chains in LangChain
- Built-in abstraction to connect components.
- Example: **LLMChain** takes a prompt and an LLM → automates prompt creation and response.

### RAG Example (Retriever QA Chain)
- Query → Search vector DB → Fetch relevant content → Send to LLM → Get answer.
- Simplifies the entire **Retrieval Augmented Generation (RAG)** process.

### Other Chain Types
- **Sequential Chain**: Multiple LLM chains in sequence.
- **SQL/Math/API Chains**: Specialized chains for common AI workflows.

---

## ⚠️ Problem: Too Many Chains
### ❌ Challenges
1. Codebase became large and difficult to maintain.
2. Hard for new developers to know which chain to use.

### ⚙️ Root Cause
- Components were not standardized.
- LLMs used `.predict()`, prompts used `.format()`, retrievers used `.get_relevant_documents()`.
- Manual wiring needed → explosion of custom chains.

---

## ✅ Solution: Standardization via Runnables
### 🧱 What are Runnables?
- **Units of work** with common interfaces.
- Methods:
  - `invoke()` → Single input
  - `batch()` → Multiple inputs
  - `stream()` → Streamed outputs

- Like Lego blocks:
  - Consistent interface
  - Can be connected
  - Composite chains behave like individual blocks

---

## 👨‍💻 Demo: Building Runnables from Scratch
### Step 1: Dummy Components
- **Fake LLM Class** with `.predict()`
- **Prompt Template** with `.format()`

### Step 2: Combine Manually
- Create prompt → format → send to LLM → get response

### Step 3: LLMChain Class
- Automates step above
- Limitation: Cannot scale to multi-step workflows

### Step 4: Abstract Runnable Class
- Create a base `Runnable` class with `invoke()` method.
- Force all components to implement `invoke()`.
- Add deprecation warnings for `.predict()`/`.format()`.

### Step 5: RunnableConnector
- Accepts list of runnables.
- Connects output of one to input of the next.
- Enables true **chain of components**.

---

## 🔗 Advanced Chaining
### Example: Joke Generator & Explainer
- Chain 1: Generate joke from topic
- Chain 2: Explain the joke
- Final Chain: Input → Output (Explanation of joke)

### Benefits:
- No need to write new code for each use-case
- Just plug different prompt templates and LLMs

---

## 🧠 Internal Structure of LangChain
- Actual LangChain classes like `ChatOpenAI` inherit from abstract `Runnable`
- Demonstrates that LangChain uses the same fundamental structure as demoed.

---

## 🎯 Conclusion
- Runnables solve the standardization problem.
- They make chaining components modular and scalable.
- Next video will explore actual LangChain `Runnable` classes.
- Encouragement to explore, build, and subscribe for deeper understanding.

---

> **🚀 Key Takeaway:** Runnables are the backbone of LangChain's modern architecture—standardized, composable, and reusable units that power AI workflows.

