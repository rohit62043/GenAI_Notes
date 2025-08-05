# ------------------------------
# Import required libraries
# ------------------------------

import validators  # For validating the input URL (check if it's a valid format)
import streamlit as st  # For building the interactive web application UI
from langchain.prompts import PromptTemplate  # To create reusable prompt templates for LLM
from langchain_groq import ChatGroq  # Groq LLM wrapper for LangChain
from langchain.chains.summarize import load_summarize_chain  # Built-in summarization chains in LangChain
from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader  
# YoutubeLoader: Extracts transcripts/info from YouTube videos
# UnstructuredURLLoader: Scrapes and parses text content from general web URLs

# ------------------------------
# Streamlit Page Configuration
# ------------------------------

st.set_page_config(
    page_title="LangChain: Summarize Text From YT or Website",  # Browser tab title
    page_icon="🦜"  # Emoji icon for the tab
)

# Main title and subheading in the web app
st.title("🦜 LangChain: Summarize Text From YT or Website")
st.subheader('Summarize URL')

# ------------------------------
# Sidebar: API Key Input
# ------------------------------

with st.sidebar:
    groq_api_key = st.text_input(
        "Groq API Key",  # Input label
        value="",  # Default value
        type="password"  # Mask input for privacy
    )

# ------------------------------
# Main Input: URL (YouTube or Website)
# ------------------------------

generic_url = st.text_input(
    "URL",  # Label (hidden)
    label_visibility="collapsed"  # Hide label to keep UI clean
)

# ------------------------------
# Initialize Groq LLM
# ------------------------------

if not groq_api_key.strip():
    st.error("Please enter your Groq API Key")
    st.stop()

llm = ChatGroq(model="llama-3.3-70b-versatile", api_key=groq_api_key)



# ------------------------------
# Prompt Template for Summarization
# ------------------------------

prompt_template = """
You are an expert technical writer tasked with creating a clear, concise, and well-structured **executive summary**.

Follow these rules:
- Limit to 300 words.
- Use **section headings** if possible.
- Preserve **important technical details** and **dates**.
- Keep a **neutral, factual tone**.
- Write in **full sentences** with no slang.

Content to summarize:
{text}
"""



# Create a PromptTemplate object for use in the summarization chain
prompt = PromptTemplate(
    template=prompt_template,  # Prompt text
    input_variables=["text"]   # Variables to replace dynamically
)

from langchain.prompts import PromptTemplate

combine_prompt_template = """
You are a professional technical summarizer.

You will receive several partial summaries of a document.  
Your task is to merge them into a single, **cohesive, well-structured** final summary.

Guidelines:
- Maintain a **neutral, factual tone**.
- Use **clear section headings**.
- Limit to **300 words**.
- Include **important dates, names, and technical details**.
- Avoid repetition and filler words.
- Present in a **clean markdown format**.

Partial Summaries:
{text}

Final professional summary:
"""
combine_prompt = PromptTemplate(
    template=combine_prompt_template,
    input_variables=["text"]
)

# ------------------------------
# Button: Trigger Summarization
# ------------------------------

if st.button("Summarize the Content from YT or Website"):
    
    # Step 1: Validate inputs
    if not groq_api_key.strip() or not generic_url.strip():
        st.error("Please provide the information to get started")  # Missing API key or URL
    
    elif not validators.url(generic_url):
        st.error("Please enter a valid Url. It can may be a YT video url or website url")  # Invalid URL format

    else:
        try:
            with st.spinner("Waiting..."):  # Show loading spinner while processing
                
                # Step 2: Load data from YouTube or website
                if "youtube.com" in generic_url:
                    # Load YouTube transcript + metadata
                    loader = YoutubeLoader.from_youtube_url(
                        generic_url,
                        add_video_info=True  # Include video title, channel, etc.
                    )
                else:
                    # Load and parse content from a general webpage
                    loader = UnstructuredURLLoader(
                        urls=[generic_url],  # List of URLs
                        ssl_verify=False,  # Skip SSL certificate verification
                        headers={  # Provide a custom User-Agent to mimic a real browser
                            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) "
                                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                                          "Chrome/116.0.0.0 Safari/537.36"
                        }
                    )

                # Actually fetch the content
                docs = loader.load()

                # Step 3: Create summarization chain
                chain = load_summarize_chain(
                    llm,
                    chain_type="map_reduce",
                    combine_prompt=combine_prompt
                )


                # Step 4: Run the summarization
                # Step 4
                result = chain.invoke(docs)
                summary_text = result["output_text"]

                # Step 5
                st.markdown(
                    f"""
                    <div style='background-color:#000000; padding:15px; border-radius:10px;'>
                        {summary_text}
                    </div>
                    """,
                    unsafe_allow_html=True
                )



        except Exception as e:
            # Handle any unexpected errors
            st.exception(f"Exception: {e}")
