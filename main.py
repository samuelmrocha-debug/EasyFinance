import sys
from database import Database
from validators import Validator
from finance_engine import FinanceEngine
from courses import CourseManager
from goals import GoalManager

class EasyFinance:
    def __init__(self):
        # Inicialização dos dados e módulos
        self.dados = Database.carregar()
        self.usuario_logado = None
        self.course_manager = CourseManager()
        self.goal_manager = GoalManager()

    def menu_inicial(self):
        while True:
            print("\n" + "="*40)
            print("     EASYFINANCE | Samuel & Richar     ")
            print("="*40)
            print("1. Cadastrar Novo Usuário")
            print("2. Login")
            print("0. Sair")
            op = input("Escolha uma opção: ")

            if op == "1": 
                self.tela_cadastro()
            elif op == "2": 
                self.tela_login()
            elif op == "0": 
                print("Encerrando sistema... Até logo!")
                sys.exit()
            else:
                print("Opção inválida. Tente novamente.")

    def tela_cadastro(self):
        print("\n--- NOVO CADASTRO ---")
        
        # RF001: Validação de E-mail
        email = input("E-mail: ")
        val, msg = Validator.validar_email(email, self.dados['usuarios'])
        if not val:
            print(f"❌ {msg}")
            return

        # RF002: Validação de Senha e Confirmação
        senha = input("Senha (4-8 dígitos, 1 maiúscula, 1 número): ")
        conf = input("Confirme a senha: ")
        val, msg = Validator.validar_senha(senha, conf)
        if not val:
            print(f"❌ {msg}")
            return

        # RF002: Validação de CPF/CNPJ
        doc = input("CPF/CNPJ (XX.XXX.XXX/0001-XX): ")
        val, msg = Validator.validar_cpf_cnpj(doc, self.dados['usuarios'])
        if not val:
            print(f"❌ {msg}")
            return

        # Salvamento no banco de dados (RF008)
        self.dados['usuarios'].append({
            "email": email, 
            "senha": senha, 
            "documento": doc
        })
        Database.salvar(self.dados)
        print("✅ Usuário cadastrado com sucesso!")

    def tela_login(self):
        print("\n--- ACESSO AO SISTEMA ---")
        email = input("E-mail: ")
        senha = input("Senha: ")
        
        for u in self.dados['usuarios']:
            if u['email'] == email and u['senha'] == senha:
                self.usuario_logado = email
                print(f"✅ Bem-vindo, {email}!")
                self.menu_principal()
                return
        
        print("❌ E-mail ou senha incorretos.")

    def menu_principal(self):
        while self.usuario_logado:
            # Cálculos em tempo real para o Dashboard
            saldo = FinanceEngine.calcular_saldo(self.usuario_logado, self.dados['transacoes'])
            
            # Soma apenas as entradas para o GoalManager
            entradas_totais = sum(t['valor'] for t in self.dados['transacoes'] 
                                 if t['user_email'] == self.usuario_logado and t['tipo'] == 'Entrada')

            print("\n" + "—"*40)
            print(f" EASYFINANCE DASHBOARD | Usuário: {self.usuario_logado}")
            print(f" SALDO ATUAL: R$ {saldo:.2f}")
            print("—"*40)
            print("1. Registrar Entrada/Saída")
            print("2. Ver Diagnóstico de Saúde Financeira")
            print("3. Gestão de Metas de Faturamento")
            print("4. Aba de Cursos (Educação Financeira)")
            print("5. Sair (Logoff)")
            
            op = input("\nSelecione uma funcionalidade: ")

            if op == "1":
                self.registrar_movimento(saldo)
            elif op == "2":
                # RF007: Diagnóstico Semanal
                print(f"\n{FinanceEngine.gerar_diagnostico(self.usuario_logado, self.dados['transacoes'])}")
            elif op == "3":
                # Nova Funcionalidade de Metas
                print(self.goal_manager.calcular_progresso(entradas_totais))
                if input("\nDeseja ajustar sua meta mensal? (S/N): ").upper() == "S":
                    self.goal_manager.configurar_meta()
            elif op == "4":
                self.course_manager.exibir_aba()
            elif op == "5":
                # RF009: Encerrar sessão com confirmação
                if input("Deseja realmente sair? (S/N): ").upper() == "S":
                    print("Limpando sessão...")
                    self.usuario_logado = None
            else:
                print("Opção inválida.")

    def registrar_movimento(self, saldo_atual):
        print("\n--- REGISTRAR MOVIMENTAÇÃO ---")
        tipo_op = input("1. Entrada (+) / 2. Saída (-): ")
        tipo = "Entrada" if tipo_op == "1" else "Saída"
        
        try:
            valor = float(input("Valor (R$): "))
            if valor <= 0:
                print("❌ O valor deve ser maior que zero.")
                return

            # RF003: Alerta de saldo negativo
            if tipo == "Saída" and valor > saldo_atual:
                print(f"⚠️ ATENÇÃO: Esta operação deixará seu saldo negativo (R$ {saldo_atual - valor:.2f}).")
                if input("Deseja continuar assim mesmo? (S/N): ").upper() != "S":
                    print("Operação cancelada.")
                    return

            # RF004: Validação de data (não permite data futura)
            data_input = input("Data (DD/MM/AAAA): ")
            val_data, data_obj = Validator.validar_data(data_input)
            if not val_data:
                print(f"❌ {data_obj}")
                return

            desc = input("Descrição/Categoria (Ex: Aluguel, Venda de Produto): ")
            if not desc:
                print("❌ A descrição não pode ficar vazia.")
                return

            # Registro e Persistência (RF008)
            nova_transacao = {
                "user_email": self.usuario_logado,
                "tipo": tipo,
                "valor": valor,
                "data": data_obj.strftime("%d/%m/%Y"),
                "desc": desc
            }
            
            self.dados['transacoes'].append(nova_transacao)
            Database.salvar(self.dados)
            print("✅ Registro salvo com sucesso!")

        except ValueError:
            print("❌ Erro: Insira um valor numérico válido.")

if __name__ == "__main__":
    app = EasyFinance()
    app.menu_inicial()