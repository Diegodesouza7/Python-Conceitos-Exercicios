""" Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
     desconsiderando os espaços. Exemplos de palíndromos:

APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA,
 O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA. """


frase = str(input('Digite uma frase qualquer: ')).replace(' ', '').strip().upper()
print('O inverso de {} é {}'.format(frase, frase[::-1]))
if frase[::-1] == frase:
    print('Ou seja, a frase é um palíndromo')
else:
    print('Ou seja, a frase não é um palíndromo')