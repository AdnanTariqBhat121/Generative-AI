from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
model = ChatMistralAI(model = "mistral-small-2603",temperature=0.9)
print("Choose your AI mode")
print("press 1 for funny mode")
print("press 2 for angry mode")
print("press 3 for sad mode")
choice = int(input("Enter your response:"))
if choice == 1:
    mode = "You are a very funny AI agent.You respond with humor and jokes"
elif choice == 2:
    mode = "You are an angry AI agent. You respod aggressively and impatiently"
elif choice == 3:
    mode = "You are a sad AI agent. You respond with sadness and empathy"
messages = [
    SystemMessage(content=mode)

]
print("_______________Welcome type 0 to exit the application_______________")
while True:
    prompt = input("You:")
    messages.append(HumanMessage(content=prompt))
    if prompt == "0":
        break
    response = model.invoke(messages)
    messages.append(AIMessage(content=response.content))
    print("Bot:",response.content)
print(messages)
    
