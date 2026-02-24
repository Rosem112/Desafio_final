import requests
from dados import carregar_dados_usuario, carregar_gastos
from prompts import SYSTEM_PROMPT


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3"  # altere se estiver usando outro modelo


def montar_contexto():
    dados_usuario = carregar_dados_usuario()
    gastos = carregar_gastos()

    renda = dados_usuario.get("renda_mensal", 0)
    total_gastos = sum(g["valor"] for g in gastos)
    saldo = renda - total_gastos

    gastos_por_categoria = {}
    for g in gastos:
        categoria = g["categoria"]
        gastos_por_categoria[categoria] = (
            gastos_por_categoria.get(categoria, 0) + g["valor"]
        )

    contexto = f"""
Dados do Usuário:
- Nome: {dados_usuario.get('nome')}
- Renda Mensal: R$ {renda}

Resumo Atual:
- Total de Gastos: R$ {total_gastos}
- Saldo Restante: R$ {saldo}

Gastos por Categoria:
"""

    for cat, val in gastos_por_categoria.items():
        contexto += f"- {cat}: R$ {val}\n"

    contexto += """
Instrução:
Responda apenas com base nos dados acima.
Caso a informação não esteja disponível, informe que não possui dados suficientes.
"""

    return contexto


def perguntar_llm(pergunta):
    contexto = montar_contexto()

    prompt_final = SYSTEM_PROMPT + "\n\n" + contexto + "\nPergunta do usuário:\n" + pergunta

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt_final,
            "stream": False
        },
    )

    return response.json()["response"]
