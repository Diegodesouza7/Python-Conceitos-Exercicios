""" Interrompendo repetições While 
s = 0
n = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')    # NOVO TIPO DE FORMAT """


""" Exemplos de f string """
nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))
print(f'Seu nome é {nome} e sua idade é {idade}')