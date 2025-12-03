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



def exibir_menu_reforco():

    while True:
        print("\n=== Menu de Sessão de Reforço Escolar ===\n")
        print("1 - Cadastrar Sessão")
        print("2 - Listar Sessões")
        print("3 - Atualizar Sessão")
        print("4 - Excluir Sessão")
        print("5 - Voltar ao Menu Principal")
        print("\n============================================\n")

        opcao = int(input("Escolha uma opção: "))

       
        if opcao == 1:

            print("\n=== Cadastrar nova sessão ===")

        
            alunos = carregar_alunos()
            if not alunos:
                print("Nenhum aluno cadastrado!")
                continue

            print("\nSelecione o aluno:")
            for a in alunos:
                print(f"{a['id']} - {a['nome']}")

            id_aluno = int(input("Digite o ID do aluno: "))

            aluno_encontrado = next((a for a in alunos if a["id"] == id_aluno), None)
            if not aluno_encontrado:
                print("Aluno não encontrado!")
                continue


            print("\nSelecione a disciplina:")
            for i, d in enumerate(DISCIPLINAS, 1):
                print(f"{i}. {d}")

            opc_disciplina = int(input("Digite o número da disciplina: "))
            disciplina_escolhida = DISCIPLINAS[opc_disciplina - 1]


            professores = carregar_professores()
            profs_da_disciplina = [ p for p in professores if p["disciplina"] == disciplina_escolhida  ]

            if not profs_da_disciplina:
                print("\n Não há professores cadastrados nessa disciplina!")
                continue

            print("\nProfessores disponíveis:")
            for p in profs_da_disciplina:
                print(f"{p['id']} - {p['nome']} ({p['disciplina']})")

            id_professor = int(input("ID do professor: "))

            professor_encontrado = next(
                (p for p in profs_da_disciplina if p["id"] == id_professor), None )

            if not professor_encontrado:
                print("Professor inválido para essa disciplina!")
                continue


            data = input("Data da sessão (DD/MM/AAAA): ")

           
            sessoes = ler_sessoes()

            novo_id = (max([s["id"] for s in sessoes]) + 1) if sessoes else 1
            nova_sessao = {
                "id": novo_id,
                "aluno": aluno_encontrado["nome"],
                "professor": professor_encontrado["nome"],
                "disciplina": disciplina_escolhida,
                "data": data
            }

            sessoes.append(nova_sessao)
            salvar_sessoes(sessoes)

            print("\nSessão cadastrada com sucesso! ✔")


        elif opcao == 2:
            sessoes = ler_sessoes()
            print("\n=== Lista de Sessões ===")

            if not sessoes:
                print("Nenhuma sessão cadastrada.")
            else:
                for s in sessoes:
                    print(  f"ID: {s['id']} | Aluno: {s['aluno']} | Professor: {s['professor']} " f"| Disciplina: {s['disciplina']} | Data: {s['data']}")


    
        elif opcao == 3:
            sessoes = ler_sessoes()
            print("\n=== Atualizar Sessão ===")

            id_atualizar = int(input("ID da sessão: "))

            for s in sessoes:
                if s["id"] == id_atualizar:
                    print("\nDeixe vazio para manter o valor atual.")

                    novo_aluno = input(f"Aluno ({s['aluno']}): ") or s["aluno"]
                    novo_professor = input(f"Professor ({s['professor']}): ") or s["professor"]
                    nova_disciplina = input(f"Disciplina ({s['disciplina']}): ") or s["disciplina"]
                    nova_data = input(f"Data ({s['data']}): ") or s["data"]

                    s["aluno"] = novo_aluno
                    s["professor"] = novo_professor
                    s["disciplina"] = nova_disciplina
                    s["data"] = nova_data

                    salvar_sessoes(sessoes)
                    print("\nSessão atualizada com sucesso!")
                    break
            else:
                print("Sessão não encontrada.")


        elif opcao == 4:
            sessoes = ler_sessoes()
            print("\n=== Excluir Sessão ===")

            id_excluir = int(input("ID da sessão: "))

            for s in sessoes:
                if s["id"] == id_excluir:
                    sessoes.remove(s)
                    salvar_sessoes(sessoes)
                    print("Sessão excluída com sucesso!")
                    break
            else:
                print("Sessão não encontrada.")


        elif opcao == 5:
            print("Voltando ao menu principal...")
            break

        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    exibir_menu_reforco()


