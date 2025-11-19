from config import get_llm

EXECUTIVE_PROMPT = """
Você é um Executivo Sênior especializado em estratégia corporativa.
Responda sempre de maneira clara, objetiva e estruturada.
"""

def criar_agente_executivo():
    llm = get_llm()

    def agente(input_text: str):
        messages = [
            {"role": "system", "content": EXECUTIVE_PROMPT},
            {"role": "user", "content": input_text}
        ]
        return llm(messages)

    return agente
