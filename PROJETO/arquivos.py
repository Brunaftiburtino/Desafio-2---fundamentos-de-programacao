import json
import os

ARQUIVO = "alunos.json"

def carregar_dados():
    """Carrega os dados do arquivo JSON ou cria um novo se não existir."""
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_dados(alunos):
    """Salva os dados no arquivo JSON."""
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(alunos, f, indent=4, ensure_ascii=False)
