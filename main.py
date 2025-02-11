import json  # Biblioteca para salvar e carregar dados em formato JSON
import time  # Biblioteca para manipulação de tempo (pausas no programa)
import os  # Biblioteca para manipulação do sistema operacional (limpar tela, listar arquivos)

# Dicionário global que armazena a lista de compras
compras = {}


# Função para adicionar um item à lista de compras
def adicionar_item(compras, item, quantidade):
    compras[item] = quantidade


# Função para remover um item da lista de compras
def remover_item(compras, item):
    if item in compras:
        del compras[item]
    else:
        'Item não existe'


# Função para exibir a lista de compras na tela
def visualizar_compras(compras):
    for item, quantidade in compras.items():
        print(f'{item}: {quantidade}')
    print()
    print('Pressione enter para continuar')
    input()


# Função para salvar a lista de compras em um arquivo JSON
def salvar_compras(compras, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(compras, arquivo)


# Função para carregar uma lista de compras de um arquivo JSON
def carregar_compras(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        return json.load(arquivo)


# Função principal que gerencia o fluxo de interação do usuário com a lista de compras
def gerenciar_compras(compras, nome_arquivo=None):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela (compatível com Windows e Linux/Mac)
        print('1 Adicionar item')
        print('2 Remover item')
        print('3 Visualizar lista')
        print('4 Salvar e sair')
        print('5 Sair sem salvar')

        escolha = input('Escolha uma opção: ')

        if escolha == '1':
            item = input('Digite o nome do item: ')
            quantidade = int(input('Digite a quantidade: '))
            adicionar_item(compras, item, quantidade)
        elif escolha == '2':
            item = input('Digite o nome do item: ')
            remover_item(compras, item)
        elif escolha == '3':
            visualizar_compras(compras)
        elif escolha == '4':
            if nome_arquivo is None:
                nome_arquivo = input('Digite o nome do arquivo para salvar: ')
            if not nome_arquivo.endswith('.json'):
                nome_arquivo += '.json'  # Garante que o arquivo tenha extensão .json
            salvar_compras(compras, nome_arquivo)
            break
        elif escolha == '5':
            break
        else:
            print('Opção inválida')
            time.sleep(1)


# Função principal que inicia o programa e permite criar ou carregar listas de compras
def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('1 Criar uma nova lista de compras')
        print('2 Carregar uma lista existente')
        print('3 Sair')

        escolha = input('Escolha uma opção:')

        if escolha == '1':
            compras = {}
            gerenciar_compras(compras)
        elif escolha == '2':
            print('Listas disponíveis:')
            arquivos = [arquivo for arquivo in os.listdir() if arquivo.endswith('.json')]  # Lista arquivos JSON
            if not arquivos:
                print('Nenhuma lista encontrada')
                time.sleep(2)
                continue
            for i, arquivo in enumerate(arquivos, 1):
                print(f'{i} {arquivo}')

            escolha = int(input('Escolha uma lista para carregar (0 se nenhuma):'))
            if escolha == 0:
                continue
            if escolha < 0 or escolha > len(arquivos):
                print('Opção inválida')
                time.sleep(1)
                continue

            compras = carregar_compras(arquivos[escolha - 1])
            gerenciar_compras(compras, arquivos[escolha - 1])
        elif escolha == '3':
            break
        else:
            print('Opção inválida')
            time.sleep(1)


if __name__ == '__main__':
    main()
