import streamlit as st

st.set_page_config(page_title="Farm-GPT", page_icon="🌾")
st.title("Farm-GPT 🌾")
st.write("Your AI Farming Assistant for Nigeria")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input("Ask about crops, soil, pests..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    
    prompt_lower = prompt.lower()
    
    if "ibadan" in prompt_lower and "rainy" in prompt_lower:
        response = "For Ibadan during rainy season (April-Oct):\n\n1. **Maize** - Plant March-April\n2. **Yam** - Plant March-May\n3. **Cassava** - Plant anytime\n4. **Vegetables** - Okra, Pepper, Tomato\nTip: Ensure good drainage to avoid flooding."
    
    elif "crop" in prompt_lower:
        response = "Best crops for Nigeria:\n**Rainy**: Maize, Yam, Rice, Cassava\n**Dry**: Irrigated Vegetables\nWhat location are you farming in?"
    
    else:
        response = "I can help with crops, soil, pests, and planting times in Nigeria.\n\nTry: 'Best crops to plant in Ibadan during rainy season'"

    st.chat_message("assistant").write(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
