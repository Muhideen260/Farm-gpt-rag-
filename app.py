import streamlit as st
from huggingface_hub import InferenceClient

# -----------------------
# Page Config
# -----------------------
st.set_page_config(
    page_title="Farm-GPT 🌾",
    page_icon="🌾",
    layout="centered"
)

st.title("🌾 Farm-GPT")
st.caption("Your AI Farming Assistant for Nigeria 🇳🇬")

# -----------------------
# Hugging Face Token
# -----------------------
HF_TOKEN = st.secrets["HF_TOKEN"]

client = InferenceClient(
    provider="hf-inference",
    api_key=HF_TOKEN,
)

# -----------------------
# Chat History
# -----------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# -----------------------
# User Input
# -----------------------
prompt = st.chat_input("Ask anything about farming...")

if prompt:

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):

        with st.spinner("🌱 Thinking..."):

            response = client.chat.completions.create(
                model="HuggingFaceH4/zephyr-7b-beta",
                messages=[
                    {
                        "role": "system",
                        "content":
                        "You are Farm-GPT, an agricultural expert in Nigeria. "
                        "Answer farming questions clearly with practical advice."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                max_tokens=300,
            )

            answer = response.choices[0].message.content

            st.write(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )
