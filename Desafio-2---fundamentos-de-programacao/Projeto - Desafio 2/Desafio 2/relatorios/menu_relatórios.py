from relatorios.gerar_relatorios import relatorio_total_professores, relatorio_professores_por_disciplina, relatorio_total_alunos, relatorio_lista_alunos, relatorio_total_sessoes, relatorio_sessoes_por_professor, relatorio_sessoes_por_disciplina, relatorio_sessoes_por_aluno


def exibir_menu_relatorios():
    while True:
        print("\n======= MENU DE RELATÓRIOS =======")
        print("1. Total de Professores")
        print("2. Professores por Disciplina")
        print("3. Total de Alunos")
        print("4. Lista de Alunos")
        print("5. Total de Sessões")
        print("6. Sessões por Professor")
        print("7. Sessões por Disciplina")
        print("8. Sessões por Aluno")
        print("9. Voltar ao Menu Principal")
        print("===================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            relatorio_total_professores()
        elif opcao == "2":
            relatorio_professores_por_disciplina()
        elif opcao == "3":
            relatorio_total_alunos()
        elif opcao == "4":
            relatorio_lista_alunos()
        elif opcao == "5":
            relatorio_total_sessoes()
        elif opcao == "6":
            relatorio_sessoes_por_professor()
        elif opcao == "7":
            relatorio_sessoes_por_disciplina()
        elif opcao == "8":
            relatorio_sessoes_por_aluno()
        elif opcao == "9":
            print("Voltando ao menu principal...")
            break
        else:
            print("Opção inválida!\n")

if __name__ == "__main__":
    exibir_menu_relatorios()