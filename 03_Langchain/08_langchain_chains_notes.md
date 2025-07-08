# 📘 LangChain: Chains In-Depth Notes

## 🎥 Video Overview
This session is part of a LangChain playlist that has previously covered how to:
- Interact with various LLMs
- Handle different types of inputs
- Generate structured outputs using Output Parsers

Now, the video introduces **Chains** in LangChain—a mechanism to build complex pipelines by connecting multiple components.

---

## 🔗 What are Chains?
Chains are a way to:
- Break LLM applications into modular, reusable steps
- Automate data flow between steps
- Build efficient and scalable applications

**Why Chains?**
- LLM apps typically require: user input → prompt design → LLM call → output handling.
- Manually linking these steps is inefficient and repetitive.
- Chains streamline this with automatic step-by-step execution.

---

## 🛠️ How Chains Work
### Pipeline Creation:
Each step in the pipeline feeds its output as input to the next.
- Input → Prompt Template → LLM → Output Parser → Result
- Execution is triggered once with an input and flows automatically through each component.

---

## 🧱 Types of Chains in LangChain

### 1. Sequential Chain
- Steps execute in series, one after another.
- Example:
  - Prompt user → Generate 5 facts → Parse and return output

#### 🧪 Simple Example:
- Libraries used: `ChatOpenAI`, `PromptTemplate`, `StrOutputParser`
- Example task: "5 facts about cricket"
- Pipeline:
  - PromptTemplate → Model → Parser → Output
- Use `pipe` operator to connect all components.
- Visualize chain with `.get_graph().print()`

#### 🧪 Complex Example:
- Step 1: Generate detailed report from topic
- Step 2: Summarize report into 5 key points
- Components used:
  - Two PromptTemplates
  - Same model used twice
  - OutputParser to clean up both outputs

### 2. Parallel Chain
- Executes multiple chains **simultaneously**
- Ideal for tasks that can be done independently and merged later

#### 🧪 Example:
- Input: Large document on Linear Regression
- Tasks:
  - Chain 1: Generate Notes using OpenAI model
  - Chain 2: Generate Quiz using Anthropic model
- Merging:
  - Merge both outputs into one final result
- Tools:
  - `RunnableParallel`
  - `RunnableSequence`

### 3. Conditional Chain
- Executes one of several possible chains based on a **condition**
- Similar to if-else logic in programming

#### 🧪 Example: Sentiment-based reply system
- Input: User feedback
- Step 1: Classify sentiment as positive/negative
- Step 2:
  - If Positive: Reply with thank you + review request
  - If Negative: Apologize + inform customer support

##### ⚙️ Key Concepts:
- Use `Pydantic` to create structured parsers → guarantees sentiment output is either `"positive"` or `"negative"`
- Use `RunnableBranch` for branching logic:
  - `(condition, chain)` tuples
  - Default chain if no condition matches
- Use `RunnableLambda` to convert a lambda function into a chain

---

## 🧩 Important Components Used
- **PromptTemplate**: To structure input prompts
- **ChatOpenAI / ChatAnthropic**: LLMs
- **StrOutputParser / PydanticOutputParser**: Format and structure LLM output
- **RunnableParallel**: Execute chains in parallel
- **RunnableBranch**: Conditional logic
- **RunnableLambda**: Converts Python lambda into a runnable chain
- **get_graph().print()**: Visualizes the chain structure

---

## 🧠 Summary
- Chains simplify and modularize LLM workflows
- Three chain types:
  - **Sequential**: Linear step-by-step tasks
  - **Parallel**: Simultaneous execution
  - **Conditional**: Decision-based branching
- Use `Runnable` components to build scalable and expressive workflows

➡️ **Next video**: Deep dive into `Runnable`, LangChain Expressions, and how internal chaining logic works.

---

## 💬 Closing Notes
- Practical and scalable chaining is key to building real-world LLM applications.
- These techniques are foundational to creating **Agentic AI systems**.
- Like 👍 and Subscribe 🔔 to stay updated with the rest of the LangChain playlist!

