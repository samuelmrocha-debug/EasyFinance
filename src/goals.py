# src/goals.py

def gerenciar_metas(metas): # Recebe a lista do main
    while True:
        print("\n" + "-"*10 + " ABA DE METAS " + "-"*10)
        print("1 - Criar Nova Meta")
        print("2 - Ver Minhas Metas")
        print("0 - Voltar")
        
        escolha = input("Escolha: ")

        if escolha == "1":
            nome = input("Qual o objetivo? ")
            valor = input("Quanto precisa poupar? R$ ")
            # Salvamos um dicionário com os dados dentro da lista
            metas.append({"objetivo": nome, "valor": valor})
            print(f"✅ Meta '{nome}' guardada!")
            
        elif escolha == "2":
            print("\n--- MINHAS METAS ---")
            if not metas:
                print("📭 Nenhuma meta guardada ainda.")
            else:
                for i, m in enumerate(metas, 1):
                    print(f"{i}. {m['objetivo']} - R$ {m['valor']}")
            input("\nPressione Enter para continuar...")
            
        elif escolha == "0":
            break