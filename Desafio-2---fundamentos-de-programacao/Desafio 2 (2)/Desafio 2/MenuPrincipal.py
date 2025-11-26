
from professores.menu_professores import exibir_menu_professores
from alunos.menu_alunos import exibir_menu_alunos
from sessoes.sessao_reforco_escolar import exibir_menu_reforco


def menuPrincipal():
    opcao = 0
    while opcao != 5:
        print("====== Menu Principal ======")
        print("1. Menu Professores/Voluntários ")
        print("2. Menu Alunos ")
        print("3. Menu Sessões de Reforço ")
        print("4. Relatórios ")
        print("5. Sair")
        print("==============================")


        opcao = int(input("Informe a opção desejada: "))
        if opcao == 1:
            exibir_menu_professores()
        elif opcao == 2:
            exibir_menu_alunos()
        elif opcao == 3:
            exibir_menu_reforco()




menuPrincipal()       


    