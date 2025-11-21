import json
import os

ARQUIVO = 'professores.json'

def carregar():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, 'r') as f:
        return json.load(f)

def salvar(lista):
    with open(ARQUIVO, 'w') as f:
        json.dump(lista, f, indent=4)

def adicionar():
    lista = carregar()
    nome = input("Nome: ")
    disciplina = input("Disciplina: ")
    novo_id = lista[-1]['id'] + 1 if lista else 1
    lista.append({"id": novo_id, "nome": nome, "disciplina": disciplina})
    salvar(lista)
    print("Adicionado com sucesso.")

def listar():
    lista = carregar()
    print("\n--- Professores ---")
    for p in lista:
        print(f"ID: {p['id']} | Nome: {p['nome']} | Disciplina: {p['disciplina']}")

def atualizar():
    id_p = int(input("ID para atualizar: "))
    lista = carregar()
    for p in lista:
        if p['id'] == id_p:
            p['nome'] = input("Novo nome: ")
            p['disciplina'] = input("Nova disciplina: ")
            salvar(lista)
            print("Atualizado com sucesso.")
            return
    print("ID nao encontrado.")

def deletar():
    id_p = int(input("ID para deletar: "))
    lista = carregar()
    nova_lista = [p for p in lista if p['id'] != id_p]
    salvar(nova_lista)
    print("Deletado com sucesso.")

while True:
    print("\n1. Adicionar  2. Listar  3. Atualizar  4. Deletar  5. Sair")
    opcao = input("Opcao: ")

    if opcao == '1':
        adicionar()
    elif opcao == '2':
        listar()
    elif opcao == '3':
        atualizar()
    elif opcao == '4':
        deletar()
    elif opcao == '5':
        break