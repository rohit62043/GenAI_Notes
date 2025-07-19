import requests
import streamlit as st

def get_groq_response(input_text):
    json_body = {
        "input": {
            "language": "French",
            "text": input_text  # Use user input here
        },
        "config": {},
        "kwargs": {}
    }

    # Corrected: use json= instead of data=
    response = requests.post("http://127.0.0.1:8000/chain/invoke", json=json_body)

    # Debugging: print response
    print(response.status_code, response.text)

    # Return JSON response
    return response.json()


# Streamlit app
st.title("LLM Application Using LCEL")
input_text = st.text_input("Enter the text you want to convert to French")

if input_text:
    result = get_groq_response(input_text)
    st.write("### Translated Response:")
    st.write(result)
