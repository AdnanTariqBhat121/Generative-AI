import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI

load_dotenv()

# Model
model = ChatMistralAI(model="mistral-small-2603")

# Prompt
prompt = ChatPromptTemplate.from_messages([
    ("system",
     """
    You are a movie information extraction assistant.
    Extract the following details in the format provided below.
    Use "Not Mentioned" if information is unavailable. Do not invent facts.

    Follow the format strictly:
    Movie Title:
    Genre:
    Director:
    Cast:
    Writers:
    Producers:
    Music Composer:
    Release Year:
    Short Summary:
    """),
    ("human", "Extract information from the provided text: {paragraph}")
])

# UI
st.title("Movie Information Extractor")

text = st.text_area("Enter movie description:")

if st.button("Extract"):
    if text.strip():
        final_prompt = prompt.invoke({"paragraph": text})
        result = model.invoke(final_prompt)
        st.write(result.content)