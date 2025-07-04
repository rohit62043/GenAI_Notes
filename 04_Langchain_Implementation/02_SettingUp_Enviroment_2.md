# LangChain Series: Getting Started with LangChain and OpenAI

## **Overview**

In this video, we will:

1. Set up **LangChain**, **LangSmith**, and **LangServe**.
2. Build a **simple sample application** using LangChain and OpenAI models.
3. Use **open-source models** like **Llama** as alternatives to OpenAI.
4. Monitor and debug the application using **LangSmith**.
5. Make the application **production-ready** with **LangServe**.

---

## **What We'll Cover**

1. **Introduction to LangChain Modules**

   - LangChain
   - LangSmith
   - LangServe

2. **Basic Components of LangChain**

   - Prompt Templates
   - Models
   - Output Parsers

3. **Building a Sample Application**

   - End-to-end application using OpenAI API keys.
   - Monitoring with LangSmith.
   - Deployment-ready setup with LangServe.

4. **Open-Source Alternatives**
   - Use **Llama** for open-source model integrations.

---

## **Setting Up LangChain, LangSmith, and LangServe**

### **Step 1: Sign Up for LangChain and LangSmith**

1. Go to the LangChain portal.
2. Create an account for **LangSmith** for monitoring and debugging.
3. In LangSmith:
   - Navigate to **Settings** > **API Keys**.
   - Generate a **LangSmith API key**.

---

### **Step 2: Obtain OpenAI API Key**

1. Visit [OpenAI Platform](https://platform.openai.com).
2. Log in with your OpenAI account.
3. Navigate to **API Keys** and create a key.
   - **Note**: OpenAI requires a minimum credit of **$5**.
4. Optionally configure billing limits under **Payments**.

---

## **Environment Setup**

### **Create a `.env` File**

Add the following API keys and project name:

```plaintext
OPENAI_API_KEY=your_openai_api_key
LANGCHAIN_API_KEY=your_langsmith_api_key
LANGCHAIN_PROJECT=GenI_App_with_OpenAI
```

# Requirements.txt

## List of Necessary Libraries

```plaintext
langchain
python-dotenv
```

# Install Dependencies

1. **Activate your virtual environment (venv)**.
2. **Install the required libraries**:

```bash
pip install -r requirements.txt
```

## Why Use LangSmith?

LangSmith provides:

- **Monitoring and debugging** for GenAI applications.
- **Visualization** of logs, requests, and application behavior.

---

## Next Steps

In the upcoming videos, we will:

1. Explore key **LangChain components**:
   - **Prompt Templates**
   - **Models**
   - **Output Parsers**
2. Monitor and trace applications using **LangSmith**.
3. Use **LangServe** for **API-based deployments**.
