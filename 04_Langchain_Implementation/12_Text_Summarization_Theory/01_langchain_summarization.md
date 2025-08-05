# LangChain Text Summarization Module - Detailed Notes

## **Overview**

This session focuses on the **Summarize Text** module in LangChain. It introduces multiple techniques to summarize structured and unstructured content from various data sources.

---

## **Data Sources**

- **Unstructured Data**: YouTube videos, Twitter posts, Wikipedia pages, speeches, etc.
- **Structured Data**: Data in tabular formats or structured files.

The end-to-end project will summarize both types of content, including content from URLs or website data.

---

## **Three Summarization Techniques in LangChain**

1. **Stuff**
2. **MapReduce**
3. **Refine**

### **Basic Implementation Covered in this Video**

- Overview of how to implement `stuff`, `MapReduce`, and `refine`.
- Demonstrates summarization on a **sample speech by PM Narendra Modi**.

---

## **Approach 1: Using Chat Messages (System & Human Messages)**

**Key imports:**

```python
from langchain.schema import AIMessage, HumanMessage, SystemMessage
```

### **Message Types**

- **SystemMessage**: Instructions to the LLM about how it should behave.
- **HumanMessage**: User query or content to process.
- **AIMessage**: Response from the LLM.

**Steps:**

1. Import environment variables (using `dotenv`).
2. Use Groq API to connect with open-source LLMs.
3. Create a `chat_message` list:
   - **SystemMessage**: Define expertise (e.g., summarizing speeches).
   - **HumanMessage**: Provide content with placeholders.
4. Pass `chat_message` to the LLM.
5. Check **token count**:
   - Input tokens: 895
   - Output tokens: 108
6. Display summary from AIMessage content.

**Pros:** Simple and direct for short texts. **Cons:** Limited by token size; not efficient for very large documents.

---

## **Approach 2: Using LLMChain with PromptTemplate**

**Key imports:**

```python
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
```

### **Concept: LLMChain**

Combines:

- LLM Model
- Prompt Template

(No string output parser needed; uses default.)

### **Steps:**

1. Create a **generic prompt template**:

   - Example: Summarize a speech and translate the summary into a target language.
   - Variables: `speech`, `language`.

   ```python
   template = """Write a summary of the following speech:
   {speech}
   Translate the precise summary to {language}.
   """
   ```

2. Define `PromptTemplate` with input variables and the template.

3. Format prompt with actual values (e.g., `language='French'`).

4. Measure token count:

   - Original: 909
   - After adding instructions: 931

5. Create `LLMChain` and execute `run()` method.

6. Output is summary translated into the chosen language (French, Hindi, etc.).

**Pros:**

- Flexible prompt customization.
- Multiple tasks in a single prompt.
- Can combine summarization with translation.

**Cons:**

- Still limited by token size.

---

## **Challenges with Large Documents**

When working with long texts (e.g., 100–200 pages or large PDFs), direct summarization isn't feasible due to token limits.

**Token Limit Examples:**

- GPT-3.5: \~4096 tokens max.
- Large inputs must be split before processing.

---

## **Upcoming Techniques**

### **Stuff Document Chain**

- Concatenates documents into a single prompt.
- Suitable for small documents.

### **MapReduce Document Chain**

- Splits document into batches.
- Summarizes each batch.
- Summarizes the summaries into a final output.

### **Refine Document Chain**

- Creates an initial summary.
- Iteratively refines it by going through the document sequence.

**Reference from documentation:**

- **Stuff**: Concatenate docs into prompt.
- **MapReduce**: Batch split → summarize each → merge summaries.
- **Refine**: Rolling summary updated iteratively.

---

## **Next Steps (In Next Video)**

- Implement summarization techniques with larger documents (5–6 pages PDFs).
- Compare **Stuff**, **MapReduce**, and **Refine** approaches with diagrams.
- Build a complete summarization workflow.

---

**End of Notes**

