""" Escreva um programa que faça o computador pensar
    em um número inteiro entre 0 e 5 e peça para o usuário
    tentar descobrir qual foi o numero escolhido pelo computador
    O programa deverá escrever na tela se o usuário venceu ou perdeu """

from random import randint
from time import sleep
computador = randint(0,5) # Faz o computador gerar um numero aleatorio
print('===' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('===' * 20)
jogador = int(input('Em que número pensei ? ')) # Jogador digita o número
print('Processando...')
sleep(4)
if jogador == computador:
    print('PARABÉNS !! você conseguiu me vencer')
else:
    print('GANHEI !! eu pensei no número {} e não no {} !'.format(computador,jogador))
