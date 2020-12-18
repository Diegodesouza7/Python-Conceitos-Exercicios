""" Condições aninhadas 
    São estruturas condicionais dentro
    de uma estrutura condicional """

# Exemplo

nome = str(input('Qual o seu nome ? '))
if nome == 'Diego':
    print('Que nome lindo')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'João':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Alice, Amanda':
    print('Que lindo nome feminino')
else:
    print('Seu nome é bem normal.')
    print('Tenha um bom dia, {} !'.format(nome))

""" elif pode ser usado quantas vezes quiser finalizando o ultimo deles com else """