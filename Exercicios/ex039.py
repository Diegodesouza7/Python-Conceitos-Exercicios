"""  Faça um programa que leia o ano de nascimento de um jovem e
    informe, de acordo com a sua idade, se ele ainda vai se alistar
    ao serviço militar, se é a hora exata de se alistar ou se já
    passou do tempo do alistamento. Seu programa também deverá
    mostrar o tempo que falta ou que passou do prazo. """

from datetime import date
atual = date.today().year

nasc = int(input('Digite o seu ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos no ano de {}'.format(nasc, idade, atual)) 
if idade == 18:
    print('Você tem que se Alistar IMEDIATAMENTE')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos'.format(saldo))    
