from professores.arquivos import carregar_dados
from professores.professores import cadastrar_professor, listar_professor, atualizar_professor, deletar_professor


def exibir_menu_professores():
    professores = carregar_dados()  

    while True:
        print("\n ====== Gerenciador de Professores/Voluntários ======\n")
        print("1. Cadastrar professor/Voluntário")
        print("2. Ler todos os professores/voluntários")
        print("3. Atualizar professor/voluntário")
        print("4. Excluir professor/voluntário")
        print("5. Voltar ao Menu Principal")
        print("\n================================\n")

        escolha = int(input("Escolha uma opção: "))

        if escolha == 1:
            cadastrar_professor(professores)
             
        elif escolha == 2:
            listar_professor(professores)

        elif escolha == 3:
            atualizar_professor(professores)

        elif escolha == 4:
            deletar_professor(professores)

        elif escolha == 5:
            print("Voltar ao Menu Principal ")
            break

        else:
            print("Opção inválida!! Tente novamente.\n")


if __name__ == "__main__":
    exibir_menu_professores()

