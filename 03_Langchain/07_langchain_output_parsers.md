**LangChain Output Parsers: Full Video Notes with Code Explanation**

---

## 🎯 Introduction

- This video continues from the previous discussion on **structured output**.
- Focus: Handling models (especially open-source) that **don't support structured output** by default.
- Solution: Use **output parsers** to convert LLM responses into structured formats (e.g., JSON, dict).

---

## 🔍 What are Output Parsers?

- **Purpose**: Transform raw LLM text output into usable structured formats.
- Can be used **with or without structured output support** from the LLM.
- Works across models: GPT, Claude, Hugging Face, etc.

---

## 🧰 Four Main Output Parsers in LangChain

| Parser Type              | Description                                | Schema Enforcement | Validation |
| ------------------------ | ------------------------------------------ | ------------------ | ---------- |
| String Output Parser     | Returns plain string content               | ❌                  | ❌          |
| JSON Output Parser       | Parses raw output to JSON/dict             | ❌                  | ❌          |
| Structured Output Parser | Extracts structured JSON with fixed schema | ✅                  | ❌          |
| Pydantic Output Parser   | Uses Pydantic for structure + validation   | ✅                  | ✅          |

---

## 🧵 1. String Output Parser

- Extracts only `result.content` from LLM response.
- Use case: Chain multiple prompts (e.g., generate report ➝ summarize).

```python
from langchain.output_parsers import StrOutputParser

chain = (
    prompt1 | model | StrOutputParser() | prompt2 | model | StrOutputParser()
)
```

---

## 🧾 2. JSON Output Parser

- Forces LLM to return JSON-formatted text.
- Uses `format_instructions` dynamically in the prompt.
- Does **not** validate schema.

```python
from langchain.output_parsers import JsonOutputParser
parser = JsonOutputParser()
prompt = PromptTemplate(
    template="Generate a person's info. {format_instructions}",
    partial_variables={"format_instructions": parser.get_format_instructions()}
)
chain = prompt | model | parser
```

---

## 🧱 3. Structured Output Parser

- Enforces a specific schema using `ResponseSchema`.
- Useful when strict field structure is required.

```python
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

schemas = [
    ResponseSchema(name="fact1", description="First fact"),
    ResponseSchema(name="fact2", description="Second fact"),
]
parser = StructuredOutputParser.from_response_schemas(schemas)
prompt = PromptTemplate(
    template="Give 2 facts. {format_instructions}",
    partial_variables={"format_instructions": parser.get_format_instructions()}
)
```

---

## ✅ 4. Pydantic Output Parser

- Combines structured output with **data validation**.
- Uses Pydantic `BaseModel` to define schema.
- Rejects invalid types (e.g., age must be integer > 18).

```python
from pydantic import BaseModel, Field
from langchain.output_parsers import PydanticOutputParser

class Person(BaseModel):
    name: str
    age: int = Field(gt=18)
    city: str

parser = PydanticOutputParser(pydantic_object=Person)
prompt = PromptTemplate(
    template="Generate a person's info from {place}. {format_instructions}",
    partial_variables={"format_instructions": parser.get_format_instructions()}
)
```

---

## 📌 Summary

- **Output Parsers** convert LLM text ➝ usable data.
- Use **String/JSON parser** for general usage.
- Use **Structured/Pydantic parsers** for fixed schema and validation.
- Compatible with **GPT, Claude, Hugging Face**, and **LangChain Chains**.

---

## 🔜 Next Topic

➡️ Exploring **Tool Integration and Function Calling** with LangChain & LLMs.

