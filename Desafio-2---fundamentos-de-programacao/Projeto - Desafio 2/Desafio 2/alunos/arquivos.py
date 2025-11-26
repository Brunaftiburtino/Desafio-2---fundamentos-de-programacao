import json
import os

ARQUIVO = os.path.join(os.path.dirname(__file__), "alunos.json")

def carregar_dados():
    
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_dados(alunos):
    
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(alunos, f, indent=4, ensure_ascii=False)
