from datetime import datetime

from defs import limpar_tela, demonstracao_lista, retirar_indice, data_lista

lista_de_compras = []

data_compra = datetime.now()
data_formatada = data_compra.strftime('%d/%m/%Y')
print('Data da compra:', data_formatada)
limite_gasto = input('Limite máximo de gastos na compra: R$ ')

while True:
    limpar_tela()
    opcao = input('Escolha uma opção: (i)Inserir  (r)Retirar  (l)Listar  (f)Finalizar: ')

    if opcao.lower() == 'i':
        limpar_tela()
        print('Lista de compras:')
        demonstracao_lista(lista_de_compras)
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
        retirar_indice(lista_de_compras)

    elif opcao.lower() == 'l':
        limpar_tela()
        demonstracao_lista(lista_de_compras)
    
    elif opcao.lower() == 'f':
        break

limpar_tela()
total = 0
for compra in lista_de_compras:
    total += int(compra[1])
print(f'Valor da lista: R$ {total}')
print()

data_lista(data_formatada, lista_de_compras)
while total > int(limite_gasto):
    limpar_tela()
    print('Valor dos itens maior do que limite de gastos, tire alguns itens da lista')
    demonstracao_lista(lista_de_compras)
    print('Para retirar os itens leve em consideração a classificação das prioridades dos itens')
    print()
    retirar_indice(lista_de_compras)
    total = 0
    for compra in lista_de_compras:
        total += int(compra[1])

limpar_tela()
data_lista(data_formatada, lista_de_compras)
