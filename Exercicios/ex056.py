""" Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
    No final do programa, mostre: a média de idade do grupo, qual é o
    nome do homem mais velho e quantas mulheres têm menos de 20 anos. """


somaidade = 0
mediaidade = 0
maioridadeh = 0
nomevelho = ''
totm20 = 0
for p in range(1,5):
    print('{}º Pessoa '.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo M / F : ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mn':
        maioridadeh = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadeh:
        maioridadeh = idade
        nomevelho = nome 
    if sexo in 'Ff' and idade < 20:
        totm20 += 1
        mediaidade = somaidade / 4   

mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e seu nome é {}'.format(maioridadeh, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totm20))