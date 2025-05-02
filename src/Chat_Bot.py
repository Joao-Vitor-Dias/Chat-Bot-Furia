from dotenv import load_dotenv
import os
import google.generativeai as genai
import documentos
import streamlit as st

load_dotenv()

genai.configure(api_key=os.environ["GEMINI_API_TOKEN"])

model = documentos.modelo_doc

st.session_state.history = documentos.history_inicial

st.set_page_config(
    page_title="Chat da FURIA",
    page_icon="https://api.draft5.gg/teams/330/logo",
 )
col1, col2 = st.columns([10, 3]) 

with col1:
    st.title("Converse com a FURIA")
    st.subheader("Pergunte o que quiser sobre o nosso time #GoFuria")

st.markdown("--------------------------------------------------")

with col2:
    st.image("https://api.draft5.gg/teams/330/logo", width=150)

with st.sidebar:
    
    st.subheader(" Acesse a nossa loja oficial: ")
    "[Furia.gg](https://www.furia.gg/)"

    st.subheader(" Siga a gente em nossas redes para não perder nada: ")
    "[Instagram.com](https://www.instagram.com/furiagg/)"
    "[Twitter.com](https://x.com/FURIA)"
   

user_input = st.chat_input("Digite sua pergunta aqui...")

for i in range(9, len(st.session_state.history) - 1 , 2):
        user_msg = st.session_state.history[i]["parts"][0]
        bot_msg = st.session_state.history[i+1]["parts"][0]
        with st.chat_message("user"):
            st.markdown(user_msg)
        with st.chat_message("assistant"):
            st.markdown(bot_msg)    

if user_input:
    # Mostra mensagem do usuário
    with st.chat_message("user"):
        st.markdown(user_input)

    # Envia para o modelo
    chat_session = model.start_chat(history=st.session_state.history)
    response = chat_session.send_message(user_input)
    model_response = response.text

    # Mostra resposta do modelo
    with st.chat_message("assistant"):
        st.markdown(model_response)

    # Atualiza histórico na sessão
    st.session_state.history.append({"role": "user", "parts": [user_input]})
    st.session_state.history.append({"role": "model", "parts": [model_response]})