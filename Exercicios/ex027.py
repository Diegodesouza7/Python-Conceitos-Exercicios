""" Faça um programa que leia 
    o nome completo de uma pessoa 
    mostrando em seguida o primeiro e o
    ultimo nome separadamente 

    Ex: Diego Botelho de Souza
    Primeiro = Diego
    Ultimo = Souza """

nome = str(input('Digite seu nome completo: ')).strip()
nome = nome.split()
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[len(nome) - 1]))