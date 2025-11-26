
from professores.arquivos import carregar_dados, salvar_dados
from disc import DISCIPLINAS

def cadastrar_professor(professores):
    nome = input("Nome do professor/voluntário: ")
    matricula = int(input("Número da matrícula: "))

    print("\n Selecione a disciplina ensinada: ")
    for i, d in enumerate(DISCIPLINAS, 1):
        print (f"{i}. {d}")

    opc_disc = int(input("Digite o número da disciplina"))    
    disciplina = DISCIPLINAS[opc_disc - 1]


    novo_professor = {
        "id": len(professores) + 1,
        "nome": nome,
        "matricula": matricula,
        "disciplina": disciplina
    }

    professores.append(novo_professor)
    salvar_dados(professores)
    print(f"Professor/Voluntário '{nome}' cadastrado com sucesso!\n")


def listar_professor(professores):
    if not professores:
        print("Nenhum professor/voluntário cadastrado.\n")
        return

    print("\nLista de Professores/Voluntários:")
    for p in professores:
        print(f"ID: {p['id']} | Nome: {p['nome']} | Matrícula: {p['matricula']} | Disciplina: {p['disciplina']}")
    print()


def atualizar_professor(professores):
    listar_professor(professores)
    try:
        id_professor = int(input("Digite o ID do professor que deseja atualizar: "))

        for p in professores:
            if p["id"] == id_professor:
                print(f"Editando: {p['nome']}")

                novo_nome = input("Novo nome: ")
                nova_matricula = input("Nova matrícula: ")
                
                print("\n Selecione a nova disciplina: ")
                for i, d in enumerate(DISCIPLINAS, 1):
                     print(f"{i}. {d}")
            
                entrada = input("Número da disciplina: ")
                if entrada.strip() != "":
                    nova_disciplina = DISCIPLINAS[int(entrada) - 1]
                else:
                    nova_disciplina = p["disciplina"]

                if novo_nome:
                    p["nome"] = novo_nome
                if nova_matricula:
                    p["matricula"] = nova_matricula
                if nova_disciplina:
                    p["disciplina"] = nova_disciplina

                salvar_dados(professores)
                print("Professor atualizado com sucesso!\n")
                return

        print("Professor/voluntário não encontrado!\n")

    except ValueError:
        print("ID inválido.\n")


def deletar_professor(professores):
    listar_professor(professores)
    try:
        id_professor = int(input("Digite o ID do professor/voluntário que deseja excluir: "))

        for p in professores:
            if p["id"] == id_professor:
                professores.remove(p)
                salvar_dados(professores)
                print(f"Professor '{p['nome']}' removido com sucesso!\n")
                return

        print("Professor não encontrado!\n")

    except ValueError:
        print("ID inválido!\n")

