#src/auth.py
def fazer_login(lista_emails, lista_senhas):
    """ realiza a autenticação do usuário e retorna o email do usuário logado ou None se falhar """
    print("\n" + "="*12 + " TELA DE LOGIN " + "="*12)

    # Verificação de pré-requisito: Impede tentativa de login em base de dados vazia
    if not lista_emails:
        print("⚠️ Nenhum usuário cadastrado.")
        return None
    # Captura de credenciais via entrada padrão
    email_login = input("E-mail: ")
    senha_login = input("Senha: ")
    
    # --- PROCESSO DE VALIDAÇÃO ---
    # 1. Verifica se o e-mail existe na base de dados
    if email_login in lista_emails:
        # 2. Localiza o índice do e-mail para encontrar a senha correspondente
        # Como as listas são paralelas, o índice do e-mail é o mesmo da senha.
        indice = lista_emails.index(email_login)
        # 3. Comparação de integridade da senha
        if senha_login == lista_senhas[indice]:
            print(f"✅ Login realizado com sucesso!")
            return email_login
        else: 
            # Caso o e-mail exista, mas a senha não coincida com o índice
            print("❌ Senha incorreta!")
    else:
        print("❌ Usuário não encontrado!")
    return None
