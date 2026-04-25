import json
import os

# src/database.py
import os

def salvar_dados(nome_arquivo, lista_dados):
    """
    Salva uma lista de strings em um arquivo de texto.
    Cria o diretório 'data' caso ele não exista para evitar erros de execução.
    """
    # Verifica a existência da pasta e a cria se necessário
    if not os.path.exists('data'):
        os.makedirs('data')
        
    caminho = os.path.join('data', nome_arquivo)
    # 'w' indica escrita (write), sobrescrevendo o arquivo para atualizar os dados
    with open(caminho, 'w') as f:
        for item in lista_dados:
            f.write(f"{item}\n")

def carregar_dados(nome_arquivo):
    """
    Lê um arquivo de texto e retorna seu conteúdo em uma lista de strings.
    Caso o arquivo não exista, retorna uma lista vazia para evitar erros no sistema.
    """
    caminho = os.path.join('data', nome_arquivo)
    if not os.path.exists(caminho):
        return []
    
    with open(caminho, 'r') as f:
        # List Comprehension: lê cada linha e remove o caractere de quebra de linha (\n)
        return [linha.strip() for linha in f.readlines()]

def salvar_valores_financeiros(nome_arquivo, lista_valores):
    """
    Salva valores numéricos (entradas/saídas) em arquivos específicos na pasta 'data'.
    """
    if not os.path.exists('data'):
        os.makedirs('data')
        
    caminho = os.path.join('data', nome_arquivo)
    with open(caminho, 'w') as f:
        for valor in lista_valores:
            # Os valores são convertidos para string apenas para o armazenamento no arquivo
            f.write(f"{valor}\n")

def carregar_valores_financeiros(nome_arquivo):
    """
    Lê valores do arquivo e os converte de volta para o formato numérico (float).
    Essencial para permitir operações matemáticas (soma, média) posteriormente.
    """
    caminho = os.path.join('data', nome_arquivo)
    if not os.path.exists(caminho):
        return []
    
    with open(caminho, 'r') as f:
        # Converte cada linha lida (string) em um número real (float)
        return [float(linha.strip()) for linha in f.readlines()]