import os
from datetime import datetime

def limpar_tela():
    os.system('cls')

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
        for lista in lista_de_compras:
            print(f'{produto}  -  {valor:2}  -  {prioridade}')
        produto = input('Produto: ')
        valor = input('Valor: ')
        prioridade = ('Grau de prioridade: ')
        lista_de_compras([
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
            numeracao = 0
            if len(lista_de_compras) == 0:
                print('Nada para listar')
            for i in lista_de_compras:
                numeracao += 1
                print(numeracao, end=' - ')
                for detalhe in i:
                    print(detalhe , end='  ')
                print('')
    
    elif opcao.lower() == 'f':
        limpar_tela()
        numeracao = 0
        if len(lista_de_compras) == 0:
            print('Nada para listar')
        for i in lista_de_compras:
            numeracao += 1
            print(numeracao, end=' - ')
            for detalhe in i:
                print(detalhe , end='  ')
            print('')
        break

limpar_tela()
print("Lista de compras final:")
for item in lista_de_compras:
    print(f'{produto}  -  {valor:2}  -  {prioridade}')
    