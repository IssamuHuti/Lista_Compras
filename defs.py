import os
from datetime import datetime

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def demonstracao_lista(lista_de_compras):
    print('Grau de prioridade: (1) Desnecessário  -  (5) Importante')
    numeracao = -1
    if len(lista_de_compras) == 0:
        print('Nada listado')
    for i, item in enumerate(lista_de_compras):
        print(f'{i} - Produto: {item[0]} - Valor: R$ {item[1]} - Prioridade: {item[2]}')
    
    print()

def retirar_indice(lista_de_compras):
    indice_str = input('Escolha o indice que será retirada: ')
    try:
        indice = int(indice_str)
        del lista_de_compras[indice]
    except ValueError:
        print('Por favor digite um número inteiro')
    except IndexError:
        print('Índice não existe na lista')

def data_lista(data_formatada, lista_de_compras):
    print("Lista de compra da data ", data_formatada)
    demonstracao_lista(lista_de_compras)
