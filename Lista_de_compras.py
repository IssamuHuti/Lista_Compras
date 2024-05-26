import os
from datetime import datetime

def limpar_tela():
    os.system('cls')

def demonstracao_lista():
    print('Grau de prioridade: (1) Desnecessário  -  (5) Importante')
    numeracao = 0
    if len(lista_de_compras) == 0:
        print('Nada listado')
    for i in lista_de_compras:
        numeracao += 1
        print(numeracao, end='')
        for detalhe in i:
            print(' - ', detalhe, end='')
        print()
    print()

lista_de_compras = []

data_compra = datetime.now()
data_formatada = data_compra.strftime('%d/%m/%Y')
print('Data da compra:', data_formatada)

limite_gasto = input('Limite máximo de gastos na compra: R$ ')

while True:
    os.system('cls')
    opcao = input('Escolha uma opção: (i)Inserir  (r)Retirar  (l)Listar  (f)Finalizar: ')

    if opcao.lower() == 'i':
        limpar_tela()
        print('Lista de compras:')
        demonstracao_lista()
        produto = input('Produto: ')
        valor = input('Valor: R$ ')
        prioridade = input('Grau de prioridade: ')
        lista_de_compras.append([
            produto,
            valor,
            prioridade
        ])

    elif opcao.lower() == 'r':
        limpar_tela()
        indice_str = int(input('Escolha o indice que será retirada: '))
        try:
            indice = int(indice_str)
            del lista_de_compras[indice]
        except ValueError:
            print('Por favor digite um número inteiro')
        except IndexError:
            print('Índice não existe na lista')

    elif opcao.lower() == 'l':
        limpar_tela()
        demonstracao_lista()
    
    elif opcao.lower() == 'f':
        break

limpar_tela()
print("Lista de compra da data ", data_formatada)
demonstracao_lista()
