from dotenv import load_dotenv
import streamlit as st

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Multi Personality AI",
    page_icon="🤖",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
.main {
    padding-top: 1rem;
}
.big-title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #4F8BF9;
}
.subtitle {
    text-align: center;
    color: gray;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# Initialize model
model = ChatMistralAI(
    model="mistral-small-2603",
    temperature=0.9
)

# Title
st.markdown('<div class="big-title">🤖 Multi Personality AI</div>',
            unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Choose a personality and start chatting!</div>',
    unsafe_allow_html=True
)

# Sidebar
with st.sidebar:
    st.header("⚙️ AI Personality")

    personality = st.radio(
        "Select Mode",
        [
            "😂 Funny Mode",
            "😡 Angry Mode",
            "😢 Sad Mode"
        ]
    )

    st.divider()

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# Personality selection
if personality == "😂 Funny Mode":
    mode = "You are a very funny AI agent. You respond with humor and jokes."
    mode_name = "Funny"

elif personality == "😡 Angry Mode":
    mode = "You are an angry AI agent. You respond aggressively and impatiently."
    mode_name = "Angry"

else:
    mode = "You are a sad AI agent. You respond with sadness and empathy."
    mode_name = "Sad"

st.info(f"Current Personality: **{mode_name}**")

# Session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "current_mode" not in st.session_state:
    st.session_state.current_mode = personality

# Reset chat when mode changes
if st.session_state.current_mode != personality:
    st.session_state.messages = []
    st.session_state.current_mode = personality

# Chat history
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)

    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.write(msg.content)

# User input
prompt = st.chat_input("Type your message...")

if prompt:

    with st.chat_message("user"):
        st.write(prompt)

    # Build conversation
    conversation = [SystemMessage(content=mode)]

    conversation.extend(st.session_state.messages)

    conversation.append(HumanMessage(content=prompt))

    # Get response
    response = model.invoke(conversation)

    # Save messages
    st.session_state.messages.append(
        HumanMessage(content=prompt)
    )

    st.session_state.messages.append(
        AIMessage(content=response.content)
    )

    # Display response
    with st.chat_message("assistant"):
        st.write(response.content)