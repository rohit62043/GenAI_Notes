# 🌟 Notes: Building End-to-End Generative AI Projects with LangChain

## 🎯 Objective

- Build an **end-to-end AI Search Engine App** using:
  - LangChain
  - Tools
  - Agents
- Go beyond simple LLM Q&A by integrating external tools for **live and updated information retrieval**.

---

## 🛠️ Tools

### What are Tools?

> **Definition (from LangChain docs):**  
> Tools are interfaces that an agent, chain, or LLM can use to interact with the world.  
> They combine:
>
> - Tool name
> - Description of what the tool does

### Why Tools?

- LLMs (like GPT-4) have a **knowledge cutoff** (e.g. December 2023 for GPT-4).
- Cannot provide real-time data (e.g. current news, weather, latest documentation updates).
- Tools help fetch **live, updated information**.

### Examples of Tools

#### ✅ RCF Tool

- Access research paper data.
- Ideal for academic and research queries.

#### ✅ Wikipedia Tool

- Fetch content from Wikipedia for general knowledge and facts.

#### ✅ Custom Tools

- Example: **Document Q&A Tool**
  - Store your documents.
  - Ask questions to extract insights or specific information.

---

## 🤖 Agents

### What are Agents?

> **Definition (from LangChain docs):**  
> The core idea of an agent is to use a language model to choose a **sequence of actions** to perform.

- Agents **decide which tools to call** and in what order.
- Enable complex, dynamic workflows:
  - E.g. search RCF first, then Wikipedia, then custom tools based on the query.

---

## 🔍 How the Search Engine AI App Works

- User asks a question.
- LLM **analyzes the query.**
- If the LLM has the answer (based on its training data), it responds directly.
- If **external data** is required:
  - The LLM (via agents) triggers the right tool.
  - E.g. fetch from:
    - Wikipedia
    - RCF
    - Yahoo Finance
    - YouTube
    - Weather APIs
    - Or custom tools
- Agent coordinates tools to **return a consolidated answer.**

---

## 💻 Libraries & Ecosystem

- **LangChain**
  - Main framework to build chains, tools, and agents.
- **Other Libraries**
  - E.g. `QI` (mentioned as another library for multi-tool setups).

---

## 🚀 Upcoming in the Video Series

- Deep dive into **tools**:
  - Creating tools in LangChain.
- Exploration of **agents**:
  - How to implement agents for dynamic workflows.
- Building an **end-to-end Search Engine project** with:
  - Tool integrations
  - Agent orchestration
  - Real-world examples

---

## 📚 Additional Tool Examples in LangChain

- Weather APIs
- Yahoo Finance News
- YouTube search
- Wikipedia
- And many more!
  - Some free, some require APIs.

---

## 🔑 Key Takeaways

- Tools empower LLMs to **break knowledge cutoffs** and retrieve fresh data.
- Agents coordinate tools, enabling complex task execution.
- A search engine AI app leverages tools + agents to deliver **powerful, real-time search experiences.**
- LangChain offers an ecosystem to easily integrate these capabilities.

---

✨ **Next Video**:

- Practical implementation of Tools in LangChain.
- Followed by Agents implementation.
- Finally, building the full Search Engine project!
