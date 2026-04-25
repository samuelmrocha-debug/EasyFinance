# src/goals.py

def gerenciar_metas(metas):
    """
    Controla o sistema de metas financeiras do usuário.
    Utiliza uma lista de dicionários para organizar o nome do objetivo e o valor alvo.
    """
    while True:
        print("\n" + "-"*10 + " ABA DE METAS " + "-"*10)
        print("1 - Criar Nova Meta")
        print("2 - Ver Minhas Metas")
        print("0 - Voltar")
        
        escolha = input("Escolha: ")

        if escolha == "1":
            nome = input("Objetivo: ")
            valor = input("Valor: ")
            # Salvamos como uma linha de texto separada por vírgula
            metas.append(f"{nome},{valor}") 
            print("✅ Meta guardada!")
            
        elif escolha == "2":
            print("\n--- MINHAS METAS ---")
            for i, m in enumerate(metas, 1):
                # enumerate() é usado para obter o índice (i) e o valor (m) da lista de metas, ou seja, cada meta recebe um número em sequeência. Ex: 1. Comprar um carro - R$ 20.000
                dados = m.split(",") 
                print(f"{i}. {dados[0]} - R$ {dados[1]}")
            # Pausa para leitura dos dados antes de limpar a tela ou voltar ao menu        
            input("\nPressione Enter para continuar...")
            
        elif escolha == "0":
            # Retorno ao menu principal
            break