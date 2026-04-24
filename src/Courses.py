# src/Courses.py
def exibir_cursos():
    while True:
        print("\n" + "="*20 + " ACADEMIA EASY FINANCE " + "="*20)
        print("Aprenda a dominar seu dinheiro com especialistas:")
        print("1 - Organização Financeira para Iniciantes (Nath Finanças)")
        print("2 - Como sair das dívidas (Me Poupe! - Nath Arcuri)")
        print("3 - O que é Selic e Investimentos Básicos (Primo Pobre)")
        print("0 - Voltar")
        print("="*63)

        escolha = input("Escolha um tema para ver o link: ")

        if escolha == "1":
            print("\n📚 [CURSO: ORGANIZAÇÃO BÁSICA]")
            print("Dica: Aprenda a regra dos 50-30-20.")
            print("🔗 Assistir agora: https://www.youtube.com/watch?v=zV_zE02UshE")
            input("\nPressione Enter para voltar...")

        elif escolha == "2":
            print("\n💸 [CURSO: SAIR DAS DÍVIDAS]")
            print("Dica: Como negociar e priorizar o que pagar.")
            print("🔗 Assistir agora: https://www.youtube.com/watch?v=7p_GZfOAsFw")
            input("\nPressione Enter para voltar...")

        elif escolha == "3":
            print("\n📈 [CURSO: INVESTIMENTOS]")
            print("Dica: Entenda como fazer o dinheiro trabalhar para você.")
            print("🔗 Assistir agora: https://www.youtube.com/watch?v=3mY_2S4V2Is")
            input("\nPressione Enter para voltar...")

        elif escolha == "0":
            break
        else:
            print("⚠️ Opção inválida!")