import json
import os

from disc import DISCIPLINAS
from professores.arquivos import carregar_dados as carregar_professores
from alunos.arquivos import carregar_dados as carregar_alunos

ARQUIVO_SESSOES = os.path.join(os.path.dirname(__file__), "sessoes.json")

def ler_sessoes():
    if not os.path.exists(ARQUIVO_SESSOES):
        with open(ARQUIVO_SESSOES, 'w') as f:
            json.dump([], f)
    with open(ARQUIVO_SESSOES, 'r') as f:
        return json.load(f)

def salvar_sessoes(sessoes):
    with open(ARQUIVO_SESSOES, 'w') as f:
        json.dump(sessoes, f, indent=2)

sessoes = []

def exibir_menu_reforco():

  while True:
    print ("\n=== Menu de Sessão de Reforço Escolar ===")
    print ("1 - Cadastrar Sessão")
    print ("2 - Listar Sessão")
    print ("3 - Atualizar Sessão")
    print ("4 - Excluir Sessão")
    print ("5 - Voltar ao menu principal")
    print ("===================================")

    opcao = int(input("Escolha uma Opção: "))

    if opcao == 1:

        print ("=== Cadastrar nova sessão ===")
        aluno = input ("Nome do Aluno: ")
        professor = input ("Nome do Professor/Voluntário: ")
        materia = input ("Matéria: ")
        data = input("Data da Sessão (DD/MM/AAAA): ")
        sessoes= ler_sessoes()

        sessao = {
            "id": int(len(sessoes)+1),
            "aluno": aluno,
            "professor": professor,
            "materia": materia,
            "data": data
        }

        sessoes.append(sessao)

        salvar_sessoes(sessoes)

        print("Sessão cadastrada com sucesso!")

    elif opcao == 2:
        sessoes = ler_sessoes()
        print ("\n=== Lista de Sessões ===")
        if len(sessoes) == 0:
            print ("Nenhuma sessão cadastrada.")
        else:

            for s in sessoes:
                print (f"ID: {s['id']} | Aluno: {s['aluno']} | Professor: {s['professor']} | Matéria: {s['materia']} | Data: {s['data']}")

    elif opcao == 3:
        print ("\n=== Atualizar Sessão ===")
        id_atualizar = int(input("Digite o ID da sessão que deseja atualizar: "))
        sessoes = ler_sessoes()
        for s in sessoes: 
            if s["id"] == id_atualizar:
                print ("Deixe em branco se não quiser alterar o campo.")
                novo_aluno = input(f"Novo nome do aluno ({s['aluno']}): ") or s["aluno"]
                novo_professor = input(f"Novo professor ({s['professor']}): ") or s["professor"]
                nova_materia = input(f"Nova matéria ({s['materia']}): ") or s["materia"]
                nova_data = input(f"Nova data ({s['data']}): ") or s["data"]

                s["aluno"] = novo_aluno
                s["professor"] = novo_professor
                s["materia"] = nova_materia
                s["data"] = nova_data
                print ("Sessão atualizada com sucesso!")
                salvar_sessoes(sessoes)
                break
        else:
            print ("Sessão não encontrada")

    elif opcao == 4:
        print ("\n=== Excluir Sessão ===")
        sessoes = ler_sessoes()
        id_excluir = int(input("Digite o ID da sessão que deseja excluir: "))
        for s in sessoes:
            if s["id"] == id_excluir:
                sessoes.remove(s)
                salvar_sessoes(sessoes)
                print ("Sessão excluída com sucesso!")
                break
        else:
            print("Sessão não cadastrada")

    elif opcao == 5:
        print("Saindo...")
        break
    else:
        print ("Opção inválida, tente novamente.")

if __name__ == "__main__":
   exibir_menu_reforco()        