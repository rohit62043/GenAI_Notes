# Data Ingestion with LangChain: Document Loaders

This section delves into data ingestion using **Document Loaders** within the LangChain framework. Document Loaders offer a variety of methods to load data from diverse sources.

## Key Concepts

- **Data Ingestion:** The process of acquiring and loading data from external sources.
- **Document Loaders:** Classes within LangChain that streamline the process of loading data from various sources, such as files, websites, databases, and more.
- **Importance of Documentation:** The LangChain documentation provides comprehensive information about available Document Loaders and their usage. However, it can sometimes be challenging to navigate due to its extensive nature.

## LangChain Document Loaders

LangChain provides a variety of **Document Loaders** to ingest data from different sources. Each loader is tailored to handle specific formats or platforms.

---

### 1. **Text Loader**

**Purpose**: Loads data from text files.

**Details**:

- This snippet loads the content of a text file into a list of **Document** objects.
- Each Document object contains:
  - **Text Content**
  - **Metadata** (e.g., source file).

**Example**:

```python
from langchain.document_loaders import TextLoader

loader = TextLoader("speech.txt")
documents = loader.load()
print(documents)
```

## 2. PDF Loader

**Purpose**: Loads data from PDF files.

### Details

- Extracts the content of a PDF file into a list of **Document** objects.
- Each **Document** object typically represents a single page of the PDF.

### Example

```python
from langchain.document_loaders import PDFLoader

loader = PDFLoader("attention.pdf")
documents = loader.load()
print(documents)
```

## 3. Web-Based Loader

**Purpose**: Loads data from websites.

### Details

- Retrieves content from a specified URL.
- The `bs4_kwargs` parameter allows filtering content using **HTML elements** (e.g., classes) with **BeautifulSoup**.

### Example

```python
from langchain.document_loaders import WebBaseLoader
from bs4 import BeautifulSoup

loader = WebBaseLoader(
    web_paths=["https://[invalid URL removed]"],
    bs4_kwargs={"parse_only": BeautifulSoup.SoupStrainer(
        class_=lambda c: c.startswith("post-")
    )}
)
documents = loader.load()
print(documents)
```

## 4. arXiv Loader

**Purpose**: Loads research papers from the arXiv repository.

### Details

- Fetches research papers using a specified **arXiv ID**.

### Example

```python
from langchain.document_loaders import ArxivLoader

loader = ArxivLoader(query="1605.03799", max_downloads=2)
documents = loader.load()
print(documents)
```

## 5. Wikipedia Loader

**Purpose**: Loads information from Wikipedia based on search queries.

### Details

- Extracts information from Wikipedia using a provided search query.

### Example

```python
from langchain.document_loaders import WikipediaLoader

loader = WikipediaLoader(query="Generative AI")
documents = loader.load()
print(documents)
```

## Installation

To use LangChain, install the necessary libraries:

```bash
pip install -r requirements.txt
```

# Notes on LangChain: Next Steps and Conclusion

## Next Steps

The next tutorial will focus on **text splitting**, a critical step for preparing loaded data for further processing.

---

## Conclusion

LangChain's **Document Loaders** provide a versatile mechanism for ingesting data from various sources. This flexibility is vital for building diverse and effective applications with LangChain.
