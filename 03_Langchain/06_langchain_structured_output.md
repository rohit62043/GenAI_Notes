**LangChain Structured Output: Full Video Notes with Code Explanation**

---

## 🚀 Introduction to LLM Communication with External Systems

- **Purpose**: Enable LLMs to communicate with machines (e.g., databases, APIs).
- Importance: Foundation for building **AI agents**.
- Builds on prior knowledge of prompts and models.
- LLM outputs: Can be **unstructured** (free text) or **structured** (e.g., JSON).

---

## 🔍 Structured vs Unstructured Output

- **Unstructured**: Plain text answers, not machine-readable.
- **Structured**: Defined format (e.g., JSON) — easier to parse, use, and store.
- Examples:
  - Resume parsing into JSON for databases.
  - Review extraction: topics, pros, cons, sentiment.
  - Agent tool use (e.g., calculator) needs structured input.

---

## 📌 Use Cases

1. **Resume Parsing**: Convert uploaded resumes into structured data (name, scores, etc.) using LLMs → store in DB.
2. **Review Processing**: Extract structured summaries (topics, pros, cons, sentiment) → serve via API.
3. **Agent Tools**: Use structured data to interact with calculators or APIs.

Structured output allows LLMs to interact **beyond human chat**.

---

## ⚙️ LangChain: Working with Structured Output Models

- Use `.with_structured_output()` on models that support it.
- Specify format using **typed dictionaries**, **Pydantic**, or **JSON Schema**.

### 🔸 Typed Dictionaries (Python’s typing module)

```python
from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int
```

- Helps IDEs but no runtime validation.

---

## 📦 Structured Output: Phone Review Example

- Goal: Extract `summary`, `sentiment`, `themes`, `pros`, `cons`, `reviewer name`

### Step 1: Define Schema with TypedDict

```python
class Review(TypedDict):
    summary: str
    sentiment: Literal['positive', 'negative']
    themes: List[str]
    pros: Optional[List[str]]
    cons: Optional[List[str]]
    name: Optional[str]
```

### Step 2: Annotate Fields for Clarity

```python
from typing_extensions import Annotated

class Review(TypedDict):
    summary: Annotated[str, "Short summary of the review"]
    ...
```

### Step 3: Generate Structured Output

```python
model.with_structured_output(Review).invoke("This phone has a great battery but poor camera.")
```

---

## 🚫 Limitations of TypedDict

- No validation at runtime → LLM might return invalid types.

---

## ✅ Pydantic for Validation

### 🔹 Basics

```python
from pydantic import BaseModel

class Student(BaseModel):
    name: str
```

- Enforces type at runtime
- Raises error for invalid input

### 🔹 Advanced Features

- `Optional`, default values
- Type coercion
- Built-in validators (email, regex)
- Field constraints

```python
from pydantic import Field

class Student(BaseModel):
    cgpa: float = Field(ge=0, le=10, description="CGPA between 0–10")
```

### 🔹 Conversion

- `.dict()` → Python dict
- `.json()` → JSON string

---

## 🔁 Structured Output with Pydantic in LangChain

```python
model.with_structured_output(ReviewModel).invoke(review_text)
```

- Safer than TypedDict
- Provides validation + documentation

---

## 🌐 JSON Schema for Cross-Language Compatibility

### Example:

```json
{
  "title": "Student",
  "type": "object",
  "properties": {
    "name": { "type": "string" },
    "age": { "type": "integer" }
  },
  "required": ["name"]
}
```

- Use when collaborating across languages (Python, JS, etc.)
- Also usable with `.with_structured_output()`

---

## ⚙️ Choosing Schema Format

| Format      | Runtime Validation | Editor Hints | Cross-Language |
| ----------- | ------------------ | ------------ | -------------- |
| TypedDict   | ❌ No              | ✅ Yes       | ❌ No          |
| Pydantic    | ✅ Yes             | ✅ Yes       | ❌ No          |
| JSON Schema | ✅ Yes             | ❌ No        | ✅ Yes         |

> 💡 Use **Pydantic** for most Python apps, **JSON Schema** for cross-platform projects.

## 🧩 `with_structured_output()` Method: JSON Mode vs Function Calling

The `with_structured_output()` method in LangChain enables LLMs to return data in a structured format. Depending on the model you're using, it works in **two distinct modes**:

---

### 🔷 1. JSON Mode

> **Used with**: `Claude`, `Gemini`, other open-source models.

- These models **do not natively support function calling**.
- LangChain injects formatting instructions into the prompt.
- The model returns a response in **JSON format**.
- Useful for:
  - Summarization
  - Data extraction
  - Review parsing
- ⚠️ No native schema enforcement; may require output parsing.

```text
with_structured_output()
  └── JSON Mode
       └── JSON formatted response
```

---

### 🔶 2. Function Calling Mode

> **Used with**: `OpenAI GPT-3.5`, `GPT-4`, and similar models.

- These models support **native function calling**.
- LangChain utilizes OpenAI’s function-calling interface.
- Automatically invokes **tools/functions** with arguments.
- Very useful for:
  - AI agents
  - Tool usage (e.g., calculators, search tools)
  - API integration

```text
with_structured_output()
  └── Function Calling Mode
       └── Direct function call (used in agents)
```

---

### ✅ Summary Table

| Mode                 | Used By              | Returns             | Use Cases                  |
| -------------------- | -------------------- | ------------------- | -------------------------- |
| **JSON Mode**        | Claude, Gemini       | JSON string         | Data extraction, summaries |
| **Function Calling** | OpenAI (GPT-4, etc.) | Function invocation | Agents, tools, APIs        |

---

---

## 🛠️ Structured Output Modes

- **JSON Mode**: For Claude, Gemini, or general models
- **Function Calling Mode**: For OpenAI (preferred)
- Open-source models like TinyLlama may **not support** structured output → manual parsing required

---

## 🧾 Summary

- Structured output helps LLMs talk to machines.
- Three schema options: TypedDict, Pydantic, JSON Schema
- Use `.with_structured_output()` in LangChain for easy integration
- Use function calling or JSON mode based on model support
- Next topic: **Output Parsers in LangChain**
