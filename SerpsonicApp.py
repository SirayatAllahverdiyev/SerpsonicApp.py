from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os 
from dotenv import load_dotenv

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
## Langsmith tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

## Prompt Template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful Textgenerator assistant. Please respond to the user prompts")
        ("user", "Prompt: {prompt}")
    ]
)

## streamlit framework

st.title('Serpsonic Demo With OPENAI API')
input_text = st.text_input("Generate a text about {keyword} keyword")

## openAI LLm
llm = ChatOpenAI(model = "gpt-4-turbo")
outout_parsser = StrOutputParser()
chain = prompt|llm|outout_parsser

if input_text:
    st.write(chain.invoke({'keyword':input_text}))