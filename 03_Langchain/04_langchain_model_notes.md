**LangChain Model Component: Full Video Notes with Code Explanation**

---

## 🔹 What are Models in LangChain?

- LangChain models act as a **common interface** to interact with different **AI models** (OpenAI, Claude, HuggingFace, etc.).
- Problem: Every API behaves differently.
- Solution: LangChain **standardizes** communication across all APIs.

### Types of Models:

1. **Language Models**

   - Input: Text
   - Output: Text
   - Used for text generation, Q&A, summarization

2. **Embedding Models**
   - Input: Text
   - Output: Vector (Embeddings)
   - Used for semantic search, RAG, similarity comparison

---

## 🔹 Language Models: LLMs vs Chat Models

### 1. **LLMs (Large Language Models)**

- Generic models
- Work with a single text input/output
- Examples: OpenAI GPT, Anthropic Claude
- **Deprecated for new LangChain projects**

### 2. **Chat Models**

- Designed for multi-turn conversations
- Handle **conversation history**
- Support **roles** (e.g., system, user, assistant)
- Preferred for: Chatbots, Agents, Assistants

### Key Differences:

| Feature       | LLM              | Chat Model                    |
| ------------- | ---------------- | ----------------------------- |
| Input         | Single string    | List of messages              |
| Memory        | No               | Yes (context-aware)           |
| Role Handling | No               | Yes                           |
| Use Case      | Static NLP tasks | Conversational AI, assistants |

---

## 📚 Setting Up Environment

### 🔍 Step-by-Step

1. **Folder**: Create `LangChainModels`
2. **Terminal Setup**:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate (Windows)
   pip install -r requirements.txt
   ```
3. **Create Folders**:

   - `llms/`
   - `chatmodels/`
   - `embedmodels/`

4. **Test Setup**:
   ```python
   import langchain
   print(langchain.__version__)
   ```

---

## 💡 OpenAI LLM Code Example

```python
from langchain.llms import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

llm = OpenAI(model_name="gpt-3.5-turbo", openai_api_key=openai_api_key)
response = llm.invoke("What is the capital of India?")
print(response)
```

- `invoke()`: Sends a prompt to the LLM and returns output.
- Output: Plain text (e.g., "New Delhi")

---

## 💬 Chat Model Code: OpenAI

```python
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
chat_model = ChatOpenAI(model_name="gpt-4")
response = chat_model.invoke("What is the capital of India?")
print(response.content)
```

- Returns structured output (content + metadata)
- `response.content`: Extracts only the generated answer

---

## 💬 Claude (Anthropic) Chat Model Code

```python
from langchain.chat_models import ChatAnthropic
from dotenv import load_dotenv
import os

load_dotenv()
chat_model = ChatAnthropic(model_name="claude-3-opus-20240229")
response = chat_model.invoke("What is the capital of India?")
print(response.content)
```

- Similar setup to OpenAI
- Requires Anthropic API key in `.env`
- Consistent usage across APIs

---

## 🧵 Temperature and Max Token Params

### 🔹 Temperature:

- Controls randomness
- `0` = Deterministic, `1.2` = Creative
- Range:
  - 0.1–0.3: Factual/Code
  - 0.5–0.7: General purpose
  - 0.9–1.2: Creative writing

### 🔹 Max Tokens:

- Limits response length
- Helps control **costs** and **output size**
- Example:

```python
chat_model = ChatOpenAI(model_name="gpt-4", temperature=0.7, max_tokens=10)
```

---

## 🌟 Hugging Face Chat Model via API

```python
from langchain.chat_models import ChatHuggingFace

model = ChatHuggingFace(repo_id="TinyLlama/TinyLlama-1.1B", task="text-generation")
response = model.invoke("What is the capital of India?")
print(response.content)
```

- Accessed via **HuggingFace Inference API**
- No local download needed
- Set token in `.env`

---

## 🚀 Run HuggingFace Chat Model Locally

```python
from langchain.llms import HuggingFacePipeline
from transformers import pipeline
import os

os.environ['HF_HOME'] = "D:/hf_cache"  # Change model cache location
pipe = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B")
llm = HuggingFacePipeline(pipeline=pipe)
response = llm.invoke("What is the capital of India?")
print(response)
```

- Requires significant resources
- First run downloads 300-500MB files
- Reuses cached files in later runs

---

## 🔹 Embedding Models with OpenAI

```python
from langchain.embeddings import OpenAIEmbeddings

embed = OpenAIEmbeddings(model="text-embedding-3-large")
vector = embed.embed_query("Delhi is the capital of India")
print(vector)
```

- Returns 3072-d vector (or less, based on config)
- Used in RAG pipelines, semantic search

### Multiple Embeddings:

```python
docs = ["Delhi is capital", "Kohli is cricketer", "Python is language"]
vectors = embed.embed_documents(docs)
```

---

## 🔹 Hugging Face Embedding Models

```python
from langchain.embeddings import HuggingFaceEmbeddings

embed = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector = embed.embed_query("Delhi is the capital of India")
print(vector)
```

- Model size: ~90MB
- Returns 384-d vector
- Can embed single or multiple documents

---

## 🤖 Document Similarity Search with Embeddings

### 🔍 Code:

```python
from langchain.embeddings import OpenAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

embed = OpenAIEmbeddings(model="text-embedding-3-large")
docs = ["Virat is batsman", "Rohit is captain", "Ashwin is spinner"]
query = "Who is captain of India?"

# Generate vectors
doc_vecs = embed.embed_documents(docs)
query_vec = embed.embed_query(query)

# Calculate cosine similarity
scores = cosine_similarity([query_vec], doc_vecs)[0]

# Find best match
best_idx = np.argmax(scores)
print("Best match:", docs[best_idx])
```

---

## 🔸 Conclusion

- Mastering LangChain models simplifies LLM development.
- Covered:
  - LLMs vs Chat Models
  - Closed vs Open Source
  - API vs Local
  - Embedding generation
  - Document similarity
- Next Topic: **Prompt Engineering in LangChain**
