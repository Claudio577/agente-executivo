from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from config import get_llm

EXECUTIVE_PROMPT = """
Você é um Executivo Sênior especializado em estratégia corporativa.
Responda sempre de maneira clara, objetiva e estruturada.
"""

def criar_agente_executivo():
    llm = get_llm()

    prompt = ChatPromptTemplate.from_messages([
        ("system", EXECUTIVE_PROMPT),
        ("human", "{input}")
    ])

    chain = RunnableSequence(
        prompt,
        llm,
        StrOutputParser()
    )

    return chain
