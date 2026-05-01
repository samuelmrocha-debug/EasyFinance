import os

# Códigos de Cores ANSI
RESET = "\033[0m"
BOLD = "\033[1m"
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
WHITE = "\033[97m"

def limpar_tela():
    """Limpa o terminal (funciona em Windows e Linux/Mac)."""
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_cabecalho(titulo):
    """Cria um topo colorido para as telas do programa."""
    limpar_tela()
    print(f"{BLUE}{'='*50}{RESET}")
    print(f"{BOLD}{CYAN}{titulo.center(50)}{RESET}")
    print(f"{BLUE}{'='*50}{RESET}\n")

def formatar_moeda(valor):
    """Transforma um número (1500.5) em Real (R$ 1.500,50)."""
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def exibir_tabela_financeira(transacoes):
    """
    Exibe uma lista de transações em um formato de tabela organizada.
    transacoes: deve ser uma lista de dicionários ou tuplas.
    """
    if not transacoes:
        print(f"{YELLOW}Nenhuma transação encontrada. {RESET}")
        return
    #cabeçalho da tabela
    print(f"{BOLD}{'*65'}")
    print(f"{'Descrição':<25}|{'valor':<15}|{'Tipo':<10}|{'Data':<10}")
    print(f"{'-'*65}{RESET}")

    for item in transacoes:
        desc = item.get('descrição', 'S/D')[:23]
        valor = formatar_moeda(item.get('valor', 0))
        tipo = item.get('tipo', '---')
        data = item.get('data', '--/--/----')

        cor_linha = GREEN if tipo.lower() == 'ENTRADA' else RED

        print(f"{cor_linha}{desc:<25}{RESET}|{valor:<15}|{tipo:<10}|{data:<10}")
        print(f"{BOLD}{'-'*65}{RESET}")
