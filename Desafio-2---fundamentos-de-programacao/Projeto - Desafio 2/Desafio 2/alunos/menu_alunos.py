from alunos.arquivos import carregar_dados
from alunos.alunos import criar_aluno, ler_todos, atualizar_aluno, deletar_aluno

def exibir_menu_alunos():
    alunos = carregar_dados()

    while True:
        print("========== MENU – GERENCIADOR DE ALUNOS ==========\n")
        print("1. Cadastrar novo aluno")
        print("2. Ler todos os alunos")
        print("3. Atualizar aluno")
        print("4. Excluir aluno")
        print("5.Voltar ao menu principal")
        print("\n===================================================\n")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_aluno(alunos)
        elif opcao == "2":
            ler_todos(alunos)
        elif opcao == "3":
            atualizar_aluno(alunos)
        elif opcao == "4":
            deletar_aluno(alunos)
        elif opcao == "5":
            print("Voltar ao Menu Principal ")
            break
        else:
            print("Opção inválida! Tente novamente.\n")

if __name__ == "__main__":
    exibir_menu_alunos()

