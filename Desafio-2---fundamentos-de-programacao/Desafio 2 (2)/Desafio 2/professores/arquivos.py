import json
import os


CAMINHO = os.path.join(os.path.dirname(__file__), "professor.json")

def carregar_dados ():
    if os.path.exists(CAMINHO):
        with open (CAMINHO, "r", encoding= "utf-8") as f:
            return json.load(f)
    return []


def salvar_dados(professor):
    with open (CAMINHO, "w", encoding="utf-8") as f:
        json.dump (professor, f, indent= 4, ensure_ascii= False)
        
