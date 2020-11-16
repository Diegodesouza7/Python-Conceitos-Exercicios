""" Crie um programa que leia duas notas de um aluno e
    calcule sua média, mostrando uma mensagem no final,
     de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO """

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2) / 2
if media < 5.0:
    print('Sua média é de {} menor que 5.0 então está Reprovado'.format(media))
elif 7 > media >= 5:
    print('Sua média é de {} e está entre 5.0 e 6.9 então está de Recuperação'.format(media))   
elif media >= 7.0:
    print('Sua média é de {} então está Aprovado'.format(media))    
