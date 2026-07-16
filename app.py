import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="Farm-GPT", page_icon="🌾")

st.title("Farm-GPT 🌾")
st.write("Ask me anything about farming.")

@st.cache_resource
def load_model():
    return pipeline(
        "text2text-generation",
        model="google/flan-t5-base"
    )

generator = load_model()

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("Ask about crops, pests, soil..."):

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            answer = generator(
                f"You are an agricultural expert in Nigeria.\nQuestion: {prompt}",
                max_new_tokens=150
            )[0]["generated_text"]

        st.write(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )
