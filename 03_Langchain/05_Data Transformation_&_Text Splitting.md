# **LangChain: Data Transformation & Text Splitting**

## **Introduction**

- This discussion continues the exploration of **LangChain**.
- Previously, we covered **data ingestion techniques** and different **document loaders**.
- In this session, we focus on **data transformation**, specifically **text splitting**.

---

## **Why Split Text into Chunks?**

- **LLMs (Large Language Models) have context size limitations**.
- Splitting documents into **smaller text chunks** helps optimize **model processing**.
- Text chunking ensures that **LLMs can handle long documents effectively**.

---

## **Recursive Character Text Splitting**

- This is a method to **break down large documents** into **manageable text chunks**.
- It ensures that **each chunk has a maximum character limit** while maintaining **some overlap** between chunks.

### **Required Library**

To use text splitting, install:

```sh
pip install langchain-text-splitters
```
