import streamlit as st
from agents.agente_executivo import criar_agente_executivo

st.set_page_config(page_title="Agente Executivo", page_icon="💼")

st.title("💼 Agente Executivo — LangChain + Streamlit")

st.write("Envie uma pergunta para o agente executivo baseado em GPT-4o-mini:")

user_input = st.text_area("Sua mensagem:", height=120)

if st.button("Enviar"):
    if not user_input.strip():
        st.warning("Digite uma mensagem antes de enviar.")
    else:
        with st.spinner("Gerando resposta..."):
            try:
                agent = criar_agente_executivo()
                response = agent.invoke({"input": user_input})

                st.subheader("📘 Resposta do Agente:")
                st.write(response)

            except Exception as e:
                st.error(f"Ocorreu um erro ao gerar a resposta: {e}")

st.markdown("---")
st.caption("Aplicação construída com Streamlit + LangChain + OpenAI")
