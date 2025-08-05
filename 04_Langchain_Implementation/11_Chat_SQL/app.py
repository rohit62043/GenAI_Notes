# Import required libraries
import streamlit as st  # Streamlit for building the interactive web UI
from pathlib import Path  # Path handling for local database files
from langchain.agents import create_sql_agent  # For creating SQL agents
from langchain.sql_database import SQLDatabase  # SQL database wrapper for LangChain
from langchain.agents.agent_types import AgentType  # Enum for agent types
from langchain.callbacks import StreamlitCallbackHandler  # Callback for live updates in Streamlit
from langchain.agents.agent_toolkits import SQLDatabaseToolkit  # Toolkit for SQL database agents
from sqlalchemy import create_engine  # SQLAlchemy for database connections
import sqlite3  # For working with SQLite databases
from langchain_groq import ChatGroq  # Groq LLM wrapper for LangChain

# Configure the Streamlit page
st.set_page_config(page_title="LangChain: Chat with SQL DB", page_icon="🦜")
st.title("🦜 LangChain: Chat with SQL DB")

# Constants for DB selection
LOCALDB = "USE_LOCALDB"
MYSQL = "USE_MYSQL"

# Sidebar options for DB selection
radio_opt = ["Use SQLLite 3 Database- Student.db", "Connect to you MySQL Database"]
selected_opt = st.sidebar.radio(label="Choose the DB which you want to chat", options=radio_opt)

# If MySQL is selected, request connection details
if radio_opt.index(selected_opt) == 1:
    db_uri = MYSQL
    mysql_host = st.sidebar.text_input("Provide MySQL Host")
    mysql_user = st.sidebar.text_input("MYSQL User")
    mysql_password = st.sidebar.text_input("MYSQL password", type="password")
    mysql_db = st.sidebar.text_input("MySQL database")
else:
    db_uri = LOCALDB

# Ask for Groq API key
api_key = st.sidebar.text_input(label="GRoq API Key", type="password")

# Validation checks for DB URI and API key
if not db_uri:
    st.info("Please enter the database information and uri")
if not api_key:
    st.info("Please add the groq api key")

# Initialize the LLM model (Groq LLaMA3)
llm = ChatGroq(groq_api_key=api_key, model_name="Llama3-8b-8192", streaming=True)

# Function to configure database connection
@st.cache_resource(ttl="2h")
def configure_db(db_uri, mysql_host=None, mysql_user=None, mysql_password=None, mysql_db=None):
    if db_uri == LOCALDB:
        # Locate the SQLite file and connect in read-only mode
        dbfilepath = (Path(__file__).parent / "student.db").absolute()
        creator = lambda: sqlite3.connect(f"file:{dbfilepath}?mode=ro", uri=True)
        return SQLDatabase(create_engine("sqlite:///", creator=creator))
    elif db_uri == MYSQL:
        # Check for complete MySQL details before connecting
        if not (mysql_host and mysql_user and mysql_password and mysql_db):
            st.error("Please provide all MySQL connection details.")
            st.stop()
        return SQLDatabase(create_engine(f"mysql+mysqlconnector://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_db}"))

# Create database connection based on selection
if db_uri == MYSQL:
    db = configure_db(db_uri, mysql_host, mysql_user, mysql_password, mysql_db)
else:
    db = configure_db(db_uri)

# Create the SQL toolkit
toolkit = SQLDatabaseToolkit(db=db, llm=llm)

# Create the SQL agent using the toolkit
agent = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION
)

# Initialize or clear message history
if "messages" not in st.session_state or st.sidebar.button("Clear message history"):
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

# Display message history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Capture user input query
user_query = st.chat_input(placeholder="Ask anything from the database")

if user_query:
    # Store and display user query
    st.session_state.messages.append({"role": "user", "content": user_query})
    st.chat_message("user").write(user_query)

    # Generate response using the SQL agent
    with st.chat_message("assistant"):
        streamlit_callback = StreamlitCallbackHandler(st.container())
        response = agent.run(user_query, callbacks=[streamlit_callback])
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.write(response)

