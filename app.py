import streamlit as st
from huggingface_hub import InferenceClient

st.set_page_config(page_title="Farm-GPT", page_icon="🌾")
st.title("🌾 Farm-GPT")
st.write("Ask me anything about farming")

client = InferenceClient("google/flan-t5-base", token=st.secrets["HF_TOKEN"])

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input("Ask about crops, soil, pests..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    
    with st.chat_message("assistant"):
        response = client.text_generation(
    prompt,
    max_new_tokens=300,
)
        answer = response.choices[0].message.content
        st.write(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})
