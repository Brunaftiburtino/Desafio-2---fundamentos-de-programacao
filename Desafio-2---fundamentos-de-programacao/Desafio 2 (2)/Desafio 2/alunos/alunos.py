from alunos.arquivos import carregar_dados, salvar_dados

def criar_aluno(alunos):
    nome = input("Nome do aluno: ")
    matricula = input("Número da matrícula: ")

    aluno = {
        "id": len(alunos) + 1,
        "nome": nome,
        "matricula": matricula
    }

    alunos.append(aluno)
    salvar_dados(alunos)
    print(f"Aluno '{nome}' cadastrado com sucesso!\n")


def ler_todos(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado.\n")
        return

    print("\n📚 Lista de Alunos:")
    for a in alunos:
        print(f"ID: {a['id']} | Nome: {a['nome']} | Matrícula: {a['matricula']}")
    print()


def atualizar_aluno(alunos):
    ler_todos(alunos)
    try:
        id_aluno = int(input("Digite o ID do aluno que deseja atualizar: "))
        for a in alunos:
            if a["id"] == id_aluno:
                print(f"Editando: {a['nome']}")
                a["nome"] = input("Novo nome: ") or a["nome"]
                a["matricula"] = input("Nova matrícula: ") or a["matricula"]

                salvar_dados(alunos)
                print("Aluno atualizado com sucesso!\n")
                return
        print("Aluno não encontrado.\n")
    except ValueError:
        print("ID inválido.\n")


def deletar_aluno(alunos):
    ler_todos(alunos)
    try:
        id_aluno = int(input("Digite o ID do aluno que deseja excluir: "))
        for a in alunos:
            if a["id"] == id_aluno:
                alunos.remove(a)
                salvar_dados(alunos)
                print(f"Aluno '{a['nome']}' removido com sucesso!\n")
                return
        print("Aluno não encontrado.\n")
    except ValueError:
        print("ID inválido.\n")
