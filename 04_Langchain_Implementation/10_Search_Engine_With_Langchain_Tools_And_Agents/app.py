import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper,WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun,WikipediaQueryRun,DuckDuckGoSearchRun
from langchain.agents import initialize_agent,AgentType
from langchain.callbacks.streamlit import StreamlitCallbackHandler
import os
from dotenv import load_dotenv

# Load environment variables from .env file (if it exists)
# This is typically used to load API keys securely.
load_dotenv()

## Arxiv and wikipedia Tools
# Initialize Arxiv API wrapper with specific settings
# top_k_results=1: Retrieves only the most relevant result.
# doc_content_chars_max=200: Limits the content of the fetched document to 200 characters
# to keep the input to the LLM concise.
arxiv_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=200)
# Create an ArxivQueryRun tool using the configured wrapper.
# This tool allows the agent to search for academic papers on ArXiv.
arxiv = ArxivQueryRun(api_wrapper=arxiv_wrapper)

# Initialize Wikipedia API wrapper with similar settings
# top_k_results=1: Retrieves only the most relevant result.
# doc_content_chars_max=200: Limits the content of the fetched page to 200 characters.
api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=200)
# Create a WikipediaQueryRun tool using the configured wrapper.
# This tool allows the agent to search for information on Wikipedia.
wiki = WikipediaQueryRun(api_wrapper=api_wrapper)

# Create a DuckDuckGoSearchRun tool for general web searches.
# name="Search": Assigns a descriptive name to the tool, which the agent uses internally.
search = DuckDuckGoSearchRun(name="Search")

# Set the title of the Streamlit web application.
st.title("🔎 LangChain - Chat with search")
# Display a descriptive text block below the title, explaining the app's functionality.
"""
In this example, we're using `StreamlitCallbackHandler` to display the thoughts and actions of an agent in an interactive Streamlit app.
Try more LangChain 🤝 Streamlit Agent examples at [github.com/langchain-ai/streamlit-agent](https://github.com/langchain-ai/streamlit-agent).
"""

## Sidebar for settings
# Set the title for the sidebar in the Streamlit app.
st.sidebar.title("Settings")
# Create a text input field in the sidebar for the user to enter their Groq API key.
# type="password": Hides the input characters for security.
api_key = st.sidebar.text_input("Enter your Groq API Key:", type="password")

# Initialize chat message history in Streamlit's session state.
# st.session_state is used to persist data across app reruns.
# If "messages" list doesn't exist, it's created with an initial assistant message.
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assisstant", "content": "Hi,I'm a chatbot who can search the web. How can I help you?"}
    ]

# Display all existing messages from the session state in the chat interface.
# st.chat_message(role) styles the message based on whether it's from "user" or "assistant".
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg['content'])

# Create a chat input box at the bottom of the Streamlit app.
# The walrus operator (:=) assigns the user's input to 'prompt' and checks if it's not empty.
if prompt := st.chat_input(placeholder="What is machine learning?"):
    # Append the user's new message to the session state.
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display the user's message immediately in the chat.
    st.chat_message("user").write(prompt)

    # Initialize the ChatGroq LLM with the provided API key and model name.
    # model_name="Llama3-8b-8192": Specifies the particular Groq model to use.
    # streaming=True: Enables real-time, token-by-token output from the LLM.
    llm = ChatGroq(groq_api_key=api_key, model_name="Llama3-8b-8192", streaming=True)
    # Define the list of tools that the agent can utilize.
    tools = [search, arxiv, wiki]

    # Initialize the LangChain agent.
    # tools: The list of external capabilities the agent can use.
    # llm: The language model driving the agent's reasoning.
    # agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION: Specifies the agent type,
    # which uses the ReAct framework for reasoning (Thought, Action, Observation).
    # handling_parsing_errors=True: Allows the agent to attempt to recover from
    # errors in parsing the LLM's output, making it more robust.
    search_agent = initialize_agent(
        tools,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        handling_parsing_errors=True
    )

    # Create a chat message container for the assistant's response.
    with st.chat_message("assistant"):
        # Initialize the StreamlitCallbackHandler.
        # st.container(): Creates a new, independent container within the assistant's message
        # to display the agent's internal thoughts and actions.
        # expand_new_thoughts=False: New thoughts will be collapsed by default,
        # requiring a click to expand and view details.
        st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
        # Run the agent with the current chat history.
        # callbacks=[st_cb]: Attaches the callback handler to display the agent's
        # execution steps (thoughts, tool calls, observations) in the Streamlit UI.
        response = search_agent.run(st.session_state.messages, callbacks=[st_cb])
        # Append the agent's final response to the session state.
        st.session_state.messages.append({'role': 'assistant', "content": response})
        # Display the agent's final response in the chat interface.
        st.write(response)
