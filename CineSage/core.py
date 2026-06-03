from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
load_dotenv()
from langchain_mistralai import ChatMistralAI
model = ChatMistralAI(model = "mistral-small-2603")
prompt = ChatPromptTemplate.from_messages(
    [("system", 
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
     ("human", """Extract information from the provided text: {paragraph}""")]
)


para = input("Enter the text to analyze: ")
final_prompt = prompt.invoke(
    {"paragraph": para}
)


result = model.invoke(final_prompt) 

print(result.content)