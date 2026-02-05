import streamlit as st
from groq import Groq

# 1. Configurazione Iniziale
st.set_page_config(page_title="La mia IA Psicologo", page_icon="🔥")
st.markdown("<h1 style='text-align: center;'>🧠 Chat AI Psicologo</h1>", unsafe_allow_html=True)

# 2. Inserisci la tua API Key qui (quella che hai preso prima)
API_KEY = st.secrets["GROQ_API_KEY"]
client = Groq(api_key=API_KEY)

# 3. Gestione della Memoria (Cronologia Chat)
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostra i messaggi vecchi
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

# 4. Logica di Interazione
if prompt := st.chat_input("Scrivi un messaggio..."):
    # Aggiungi messaggio utente
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Risposta dell'IA
    with st.chat_message("assistant"):
        chat_completion = client.chat.completions.create(
            messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
            model="llama-3.3-70b-versatile",
        )
        response = chat_completion.choices[0].message.content
        st.markdown(response)
   
    # Salva la risposta dell'IA in memoria
    st.session_state.messages.append({"role": "assistant", "content": response})