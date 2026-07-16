import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="Farm-GPT", page_icon="🌾")
st.title("Farm-GPT 🌾")
st.write("Ask me anything about farming")

# This downloads the model once, then works offline
@st.cache_resource
def load_model():
    return pipeline("text-generation", model="google/flan-t5-base")

generator = load_model()

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input("Ask about crops, soil, pests..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = generator(f"Answer this farming question: {prompt}", max_length=200)[0]['generated_text']
        st.write(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
