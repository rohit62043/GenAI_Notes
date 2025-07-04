**LangChain Prompt Component: Full Video Notes with Code Explanation**

---

## 🧠 Introduction to Prompts in LangChain

- Nitesh recaps previous videos:
  - 1: LangChain and its necessity
  - 2: Six LangChain components with real-life examples
  - 3: Deep dive into Models
- This fourth video dives into **Prompts**, the second LangChain component.
- Topics include:
  - Temperature parameter
  - Prompt types
  - Static vs dynamic prompts
  - Prompt templates
  - ChatPromptTemplate
  - Message placeholders

---

## 🔥 Temperature Parameter in LLMs

- **Definition**: Controls randomness of LLM output.
- **Low temperature (0)**: Deterministic, same output for same prompt.
- **High temperature (1.5)**: Creative, variable output.

```python
from langchain.chat_models import ChatOpenAI

model = ChatOpenAI(model_name="gpt-4", temperature=0)
model.invoke("Write a 5-line poem about cricket")
```

---

## ✉️ Text-Based Prompting

- **Prompt** = Input message to an LLM
- Supports multimodal input (image/audio/video), but focus is on text
- Slight changes in prompt drastically change outputs
- Prompt design is critical → Leads to job role: **Prompt Engineer**

---

## 🆚 Static vs Dynamic Prompts

### ❌ Static Prompt (less control)

```python
user_input = input("Enter prompt: ")
response = model.invoke(user_input)
```

- Poor consistency
- High chance of errors from user input

### ✅ Dynamic Prompt Template

- Predefined structure
- User fills parameters → model gets structured query

```python
from langchain.prompts import PromptTemplate

prompt = PromptTemplate.from_template(
    "Summarize the paper '{paper}' in a {style} way and keep it {length} long."
)
prompt.format(paper="Attention is All You Need", style="simple", length="short")
```

---

## 🖼️ Streamlit UI for Research Assistant

```python
import streamlit as st

st.header("Research Summary Assistant")
paper = st.selectbox("Select Paper", [...])
style = st.selectbox("Style", ["Simple", "Math-heavy", "Code-heavy"])
length = st.selectbox("Length", ["Short", "Medium", "Long"])

if st.button("Generate Summary"):
    formatted_prompt = prompt.format(paper=paper, style=style, length=length)
    response = model.invoke(formatted_prompt)
    st.write(response.content)
```

---

## 📦 Prompt Templates vs f-Strings

- **f-strings work**, but not recommended.
- PromptTemplates advantages:
  - Placeholder validation
  - Template reusability (save as `.json`)
  - Seamless chaining

### Save Prompt Template

```python
prompt.save("template.json")
```

### Load Prompt Template

```python
from langchain.prompts import load_prompt
prompt = load_prompt("template.json")
```

---

## 🔗 Model Chains with Prompt Template

```python
from langchain.chains import LLMChain

chain = LLMChain(prompt=prompt, llm=model)
chain.invoke({"paper": "Transformers", "style": "code-heavy", "length": "medium"})
```

- `LLMChain` simplifies the process: template + model + inputs

---

## 🤖 Build Console Chatbot with LangChain

```python
from langchain.chat_models import ChatOpenAI
model = ChatOpenAI()

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit": break
    print("AI:", model.invoke(user_input).content)
```

### Problem: No memory/context

---

## 💬 Chat History for Context

```python
from langchain.schema import HumanMessage, AIMessage

chat_history = []

while True:
    user_input = input("You: ")
    if user_input == "exit": break
    chat_history.append(HumanMessage(content=user_input))
    response = model.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))
    print("AI:", response.content)
```

---

## 📥 Message Types in LangChain

- `SystemMessage`: Role definition (e.g. "You are a helpful doctor")
- `HumanMessage`: User input
- `AIMessage`: Model output

```python
from langchain.schema import SystemMessage

chat_history = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="What's the capital of France?")
]
response = model.invoke(chat_history)
```

---

## 🧱 ChatPromptTemplate with Placeholders

```python
from langchain.prompts import ChatPromptTemplate

template = ChatPromptTemplate.from_messages([
    ("system", "You are a {domain} expert."),
    ("human", "Tell me about {topic}.")
])

filled = template.format_messages(domain="cricket", topic="Sachin Tendulkar")
response = model.invoke(filled)
```

---

## 🧠 MessagePlaceholder for Chat History

```python
from langchain.prompts import MessagesPlaceholder

template = ChatPromptTemplate.from_messages([
    ("system", "You are a customer support agent."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{query}")
])

filled = template.format_messages(chat_history=chat_history, query="Where is my refund?")
response = model.invoke(filled)
```

---

## 📂 Chat History from Storage (Text File Example)

```python
with open("chat_history.txt") as f:
    lines = f.readlines()

chat_history = [
    HumanMessage(content=lines[0]),
    AIMessage(content=lines[1])
]
```

---

| Feature                  | `PromptTemplate`                                       | `ChatPromptTemplate`                                                                                                            |
| ------------------------ | ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------- |
| **Used with**            | Text completion models (`OpenAI`, `HuggingFace`, etc.) | Chat-based models (`ChatOpenAI`, `Claude`, etc.)                                                                                |
| **Output format**        | Single prompt string                                   | Structured chat messages (`SystemMessage`, `HumanMessage`, etc.)                                                                |
| **Supports chat roles**  | ❌ No                                                  | ✅ Yes (`system`, `human`, `AI`, etc.)                                                                                          |
| **Template Flexibility** | Basic string templating                                | Advanced: multi-role, multi-turn formatting                                                                                     |
| **Use case**             | Traditional prompts (e.g., `Q: ... A: ...`)            | Simulating conversations, agents, role-play                                                                                     |
| **Example**              | `python\nPromptTemplate(template="Q: {question}")\n`   | `python\nChatPromptTemplate.from_messages([\n    ("system", "You are a helpful AI."),\n    ("human", "What is {topic}?")\n])\n` |
| **Support for few-shot** | Manual (string formatting)                             | Built-in support via message lists                                                                                              |

## 📌 Summary

- Prompt engineering is critical in LangChain.
- Covered:
  - Temperature tuning
  - Static vs dynamic prompts
  - Prompt templates (load/save)
  - Chat prompt templates
  - Message types and placeholders
  - Basic chatbot with memory
- Next focus: **Prompt Engineering Techniques (CoT, ReAct, etc.)**
