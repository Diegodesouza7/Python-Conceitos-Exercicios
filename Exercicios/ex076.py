"""  Crie um programa que tenha uma tupla única com nomes
     de produtos e seus respectivos preços, na sequência. 
     No final, mostre uma listagem de preços, organizando
     os dados em forma tabular. """

lista = ('Caneta', 1.75,
         'Borracha', 2,
         'Caderno', 15.90,
         'Compasso', 10,
         'Mochila', 55)
print('-' * 40)
print(f'{"Listagem de Materiais / Preços":^40}')
print('-' * 40)
for pos in range(len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:>7.2f}')
print('-' * 40)        
