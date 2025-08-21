#Load keys
import os
from dotenv import load_dotenv
load_dotenv()


from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


##langsmith tracking
os.environ['LANGSMITH_API_KEY'] = os.getenv('LANGSMITH_API_KEY')
langsmith_project = os.getenv('LANGSMITH_PROJECT')
if langsmith_project is not None:
	os.environ['LANGSMITH_PROJECT'] = langsmith_project
os.environ['LANGCHAIN_TRACING_V2'] = "true"

#Prompt Template
prompt = ChatPromptTemplate.from_messages([
	("system","You are a helpful assistant. Please respond to the question asked"),
	("user","Question:{question}")
])

#streamlit framework
st.title("Langchain Demo with Gemma Model")
input_text = st.text_input("What question do you have in mind?")

##Ollama Llama2 model
llm = Ollama(model="gemma:2b") 
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
	st.write(chain.invoke({"question" : input_text}))
