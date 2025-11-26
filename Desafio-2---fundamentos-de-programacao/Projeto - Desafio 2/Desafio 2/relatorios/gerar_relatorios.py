from professores.arquivos import carregar_dados as carregar_professores
from alunos.arquivos import carregar_dados as carregar_alunos
from sessoes.sessao_reforco_escolar import ler_sessoes


def relatorio_total_professores():
    professores = carregar_professores()
    print("\n=== TOTAL DE PROFESSORES/VOLUNTÁRIOS ===")
    print(f"Total cadastrado: {len(professores)}\n")


def relatorio_professores_por_disciplina():
    professores = carregar_professores()
    if not professores:
        print("Nenhum professor cadastrado.\n")
        return

    disciplinas = {}

    for p in professores:
        disc = p["disciplina"]
        disciplinas[disc] = disciplinas.get(disc, 0) + 1

    print("\n=== PROFESSORES POR DISCIPLINA ===")
    for disc, qtd in disciplinas.items():
        print(f"{disc}: {qtd} professor(es)")
    print()


def relatorio_total_alunos():
    alunos = carregar_alunos()
    print("\n=== TOTAL DE ALUNOS ===")
    print(f"Total cadastrado: {len(alunos)}\n")


def relatorio_lista_alunos():
    alunos = carregar_alunos()
    if not alunos:
        print("Nenhum aluno cadastrado.\n")
        return

    print("\n=== LISTA DE ALUNOS ===")
    for a in alunos:
        print(f"ID: {a['id']} | Nome: {a['nome']} | Matrícula: {a['matricula']}")
    print()


def relatorio_total_sessoes():
    sessoes = ler_sessoes()
    print("\n=== TOTAL DE SESSÕES DE REFORÇO ===")
    print(f"Total cadastrado: {len(sessoes)}\n")


def relatorio_sessoes_por_professor():
    sessoes = ler_sessoes()
    if not sessoes:
        print("Nenhuma sessão cadastrada.\n")
        return

    contagem = {}

    for s in sessoes:
        prof = s["professor"]
        contagem[prof] = contagem.get(prof, 0) + 1

    print("\n=== SESSÕES POR PROFESSOR ===")
    for prof, qtd in contagem.items():
        print(f"{prof}: {qtd} sessão(ões)")
    print()


def relatorio_sessoes_por_disciplina():
    sessoes = ler_sessoes()
    if not sessoes:
        print("Nenhuma sessão cadastrada.\n")
        return

    contagem = {}

    for s in sessoes:
        materia = s["disciplina"]  
        contagem[materia] = contagem.get(materia, 0) + 1

    print("\n=== SESSÕES POR DISCIPLINA ===")
    for materia, qtd in contagem.items():
        print(f"{materia}: {qtd} sessão(ões)")
    print()


def relatorio_sessoes_por_aluno():
    sessoes = ler_sessoes()
    if not sessoes:
        print("Nenhuma sessão cadastrada.\n")
        return

    contagem = {}

    for s in sessoes:
        aluno = s["aluno"]
        contagem[aluno] = contagem.get(aluno, 0) + 1

    print("\n=== SESSÕES POR ALUNO ===")
    for aluno, qtd in contagem.items():
        print(f"{aluno}: {qtd} sessão(ões)")
    print()



