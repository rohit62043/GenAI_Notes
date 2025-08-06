import streamlit as st  # For creating the interactive web application
from langchain_groq import ChatGroq  # To use Groq-hosted LLMs like Gemma 2
from langchain.chains import LLMMathChain, LLMChain  # Prebuilt chain for math problems and custom chains
from langchain.prompts import PromptTemplate  # For designing custom LLM prompts
from langchain_community.utilities import WikipediaAPIWrapper  # For Wikipedia search capability
from langchain.agents.agent_types import AgentType  # Enum to define the type of agent
from langchain.agents import Tool, initialize_agent  # For defining tools and initializing the multi-tool agent
from langchain.callbacks import StreamlitCallbackHandler # To display real-time thought process in Streamlit


st.set_page_config(
    page_title="Text To Math Problem Solver And Data Search Assistant",
    page_icon="🧮"  
)
st.title("Text To Math Problem Solver Using Google Gemma 2")

# Sidebar: API Key Input
groq_api_key = st.sidebar.text_input(
    label="Groq API Key",  # Label in the sidebar
    type="password"  # Mask input for security
)

if not groq_api_key:
    st.info("Please add your Groq API key to continue")
    st.stop()
    
llm = ChatGroq(
    model="gemma2-9b-it",
    groq_api_key=groq_api_key
)

# Tool 1: Wikipedia Search Tool

wikipedia_wrapper=WikipediaAPIWrapper() # Create a Wikipedia API wrapper

wikipedia_tool = Tool(
    name="Wikipedia",
    func=wikipedia_wrapper.run,
    description="A tool for searching Wikipedia for information on various topics."
)

# Tool 2: Math Problem Solver
math_chain = LLMMathChain.from_llm(llm=llm)  # Create a math-solving chain using the LLM
calculator = Tool(
    name="Calculator",  # Tool name
    func=math_chain.run,  # Function to perform math calculations
    description="A tool for solving math expressions. Only the mathematical expression should be provided."
)

# Tool 3: Logical Reasoning Tool (Custom Prompt)

# Prompt template for logical/step-by-step math reasoning
prompt = """
You are an agent tasked with solving the user's mathematical question.
Logically arrive at the solution and provide a detailed explanation,
displaying the steps point-wise.

Question: {question}
Answer:
"""

prompt_template=PromptTemplate(
    input_variables=["question"],
    template=prompt
)

chain=LLMChain(llm=llm, prompt=prompt_template)

reasoning_tool=Tool(
    name="Reasoning Tool",
    func=chain.run,
    description="A tool for answering logic-based and reasoning questions."
)

# Initialize the Agent with Tools

assistant_agent=initialize_agent(
    tools=[wikipedia_tool,calculator,reasoning_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False,  # Set to True for debugging in console
    handle_parsing_errors=True  # Prevent crashes if LLM output is not perfectly formatted
)

# Session State: Message History
if "messages" not in st.session_state:
    st.session_state["messages"]=[
        {"role":"assistant","content":"Hi, I'm a math chatbot who can answer all your math questions!"}
    ]

#Display previous Chat Message
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# User Input: Question Text Area
question = st.text_area(
    "Enter your question:",
    "I have 5 bananas and 7 grapes. I eat 2 bananas and give away 3 grapes. "
    "Then I buy a dozen apples and 2 packs of blueberries. Each pack of blueberries "
    "contains 25 berries. How many total pieces of fruit do I have at the end?"
)

# Button: Process the Question
if st.button("Find my answer"):
    if question:
        with st.spinner("Generating response.."):
            # Store the user question in chat history
            st.session_state.messages.append({"role": "user", "content": question})
            st.chat_message("user").write(question)
            
            #Callback handler for showing intermediate reasoning
            st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
            
            # Run the agent with the question
            response = assistant_agent.run(
                question,
                callbacks=[st_cb]
            )

            # Store and display the assistant's response
            st.session_state.messages.append({'role': 'assistant', "content": response})
            st.write('### Response:')
            st.success(response)
    else:
        st.warning("Please enter a question before clicking the button.")

