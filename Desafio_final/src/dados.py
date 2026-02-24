import json
import pandas as pd


def carregar_dados_usuario():
    with open("src/data/dados_usuario.json", "r", encoding="utf-8") as f:
        return json.load(f)


def carregar_gastos():
    with open("src/data/gastos_mensais.json", "r", encoding="utf-8") as f:
        return json.load(f)


def carregar_historico():
    return pd.read_csv("src/data/historico_mensal.csv")
