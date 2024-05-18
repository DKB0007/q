from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv
import logging

# Setup logging
logging.basicConfig(level=logging.DEBUG)

# Load environment variables from .env file
load_dotenv()

# Get environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")
langchain_api_key = os.getenv("LANGCHAIN_API_KEY")

# Check if environment variables are set
if not openai_api_key:
    logging.error("OPENAI_API_KEY environment variable is not set.")
    st.error("OPENAI_API_KEY environment variable is not set.")
else:
    logging.debug("OPENAI_API_KEY is set.")

if not langchain_api_key:
    logging.error("LANGCHAIN_API_KEY environment variable is not set.")
    st.error("LANGCHAIN_API_KEY environment variable is not set.")
else:
    logging.debug("LANGCHAIN_API_KEY is set.")

# Set environment variables
os.environ["OPENAI_API_KEY"] = openai_api_key
os.environ["LANGCHAIN_API_KEY"] = langchain_api_key

# Langsmith tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# Custom CSS for background
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.pexels.com/photos/16103245/pexels-photo-16103245.jpeg");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries."),
        ("user", "Question:{question}")
    ]
)

# Streamlit framework
st.title('Langchain Demo With OpenAI API Made by DKB')
input_text = st.text_input("Search the topic you want")

# OpenAI LLM 
llm = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    response = chain.invoke({'question': input_text})
    st.write(response)
