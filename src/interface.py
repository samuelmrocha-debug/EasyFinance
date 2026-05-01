#src/interface.py
import os
from src.finance_engine import registrar_transacao, exibir_alertas, exibir_diagnostico, gerar_relatorio_mensal
from src.Courses import exibir_cursos
from src.goals import gerenciar_metas
from src.database import carregar_sessao_usuario, salvar_dados_usuario, salvar_todo_o_db, carregar_todo_o_db
from src.validators import validar_email

def configurar_perfil(usuario_logado):
    """
    CRUD de Usuário: Permite Editar (Update) o e-mail ou Deletar (Delete) a conta.
    Retorna o novo e-mail se alterado, None se deletado, ou o original se nada mudar.
    """
    print("\n" + "="*15 + " AJUSTES DE PERFIL " + "="*15)
    print(f"Usuário atual: {usuario_logado}")
    print("1 - Alterar meu E-mail (Update)")
    print("2 - Excluir minha Conta (Delete)")
    print("0 - Voltar")
    
    opcao = input("Escolha uma opção: ")
    db = carregar_todo_o_db()

    if opcao == "1":
        novo_email = input("Digite o novo e-mail: ").strip()
        
        if not validar_email(novo_email):
            print("❌ Erro: Formato de e-mail inválido!")
            return usuario_logado
        
        if novo_email in db["usuarios_cadastrados"]:
            print("❌ Erro: Este e-mail já está em uso!")
            return usuario_logado

        # --- LÓGICA DE UPDATE (E do CRUD) ---
        # Movemos os dados da chave antiga para a nova chave no JSON
        db["usuarios_cadastrados"][novo_email] = db["usuarios_cadastrados"].pop(usuario_logado)
        db["repositorio_dados"][novo_email] = db["repositorio_dados"].pop(usuario_logado)
        
        salvar_todo_o_db(db)
        print("✅ E-mail atualizado! Você será deslogado para segurança.")
        return None # Força logout para atualizar a sessão com o novo e-mail

    elif opcao == "2":
        confirmar = input(f"⚠️ TEM CERTEZA que deseja apagar a conta {usuario_logado}? (s/n): ")
        if confirmar.lower() == 's':
            # --- LÓGICA DE DELETE (D do CRUD) ---
            db["usuarios_cadastrados"].pop(usuario_logado)
            db["repositorio_dados"].pop(usuario_logado)
            
            salvar_todo_o_db(db)
            print("🗑️ Conta excluída com sucesso.")
            return None # Retorna None para sair do menu
            
    return usuario_logado
def menu_principal(usuario_logado):
    """
    Exibe o menu de funcionalidades principais após o login.
    Controla o fluxo entre as abas de finanças, cursos, metas e relatórios.
    """
    # Carrega as informações dos arquivos de texto para as listas em memória ao iniciar o programa
    lista_metas, lista_lembretes, valores_entradas, valores_saidas = carregar_sessao_usuario(usuario_logado)

    while True:
        # Renderização do cabeçalho de navegação
        print("\n" + "="*30)
        print("      EASY FINANCE - HOME")
        print(f"   Usuário: {usuario_logado}")
        print("="*30)
        print("1 - Registrar Entrada/Saída")
        print("2 - Alertas de Vencimento")
        print("3 - Diagnóstico Financeiro")
        print("4 - Relatórios Mensais")
        print("5 - Aba de Cursos")
        print("6 - Aba de Metas")
        print("7 - Configurações de Perfil")
        print("0 - Encerrar Sessão (Logout)")
        print("="*30)

        escolha = input("Escolha uma opção: ")

        # --- ORQUESTRAÇÃO DE FUNCIONALIDADES ---

        if escolha == "1":
            # Gerencia entradas e saídas e sincroniza as alterações no banco de dados
            registrar_transacao(valores_entradas, valores_saidas)

            salvar_dados_usuario(usuario_logado, 
                entradas=list(valores_entradas), 
                saidas=list(valores_saidas)
            )
            print(f"✅ Sincronizado! Total de entradas agora: {len(valores_entradas)}")
            print(f"✅ Sincronizado! Total de saídas agora: {len(valores_saidas)}")

        elif escolha == "2":
            # 1. Chama a função de alertas enviando a lista
            exibir_alertas(lista_lembretes)
            # 2. ASSIM QUE VOLTAR DA FUNÇÃO, SALVA NO ARQUIVO:
            salvar_dados_usuario(usuario_logado, lembretes=list(lista_lembretes))
            print("💾 Lembretes sincronizados com o banco de dados!")

        elif escolha == "3":
            # O diagnóstico calcula saúde financeira baseada em entradas vs saídas
            # Parâmetros: [Reserva Alvo], Total Entradas, Total Saídas, Meses de Cobertura
            saldo_total = sum(valores_entradas) - sum(valores_saidas)
            historico_real = [1000, saldo_total]
            exibir_diagnostico(historico_real, sum(valores_entradas), sum(valores_saidas), 6)

        elif escolha == "4":
             # Módulo de visualização de balanço simplificado
             gerar_relatorio_mensal(valores_entradas, valores_saidas) # Chama a página de relatórios
             
        elif escolha == "5":
           #módulo de cursos e educação financeira
           exibir_cursos() 

        elif escolha == "6":
            gerenciar_metas(lista_metas)
            # Menu de metas pessoais com salvamento automático ao sair da aba
            salvar_dados_usuario(usuario_logado, metas=list(lista_metas))
            print("💾 Metas sincronizadas com o banco de dados!")

        elif escolha == "7":
            # Chama a nova função de Editar/Deletar
            resultado_perfil = configurar_perfil(usuario_logado)
            if resultado_perfil is None: # Se deletou ou mudou e-mail
                break # Sai do loop e volta para o menu inicial do sistema
            else:
                usuario_logado = resultado_perfil

      
            
        elif escolha == "0":
            print("\nSessão encerrada!")
            break 
        else:
            print("\nOpção inválida!")

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')