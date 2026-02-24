import streamlit as st
from agente import perguntar_llm

st.set_page_config(page_title="FinanBot", page_icon="💰")

st.title("💰 FinanBot")
st.write("Seu assistente de organização financeira pessoal.")

pergunta = st.text_input("Faça sua pergunta sobre suas finanças:")

if st.button("Enviar") and pergunta:
    with st.spinner("Analisando seus dados..."):
        resposta = perguntar_llm(pergunta)
    st.success("Resposta do FinanBot:")
    st.write(resposta)
