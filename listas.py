""" Listas """

#Podem ser mutaveis

#Exemplo 1
""" num = [2,4,5,6,7]
num[2] = 3
num.append(9)
num.sort()
num.sort(reverse=True)
num.insert(1,0)
num.remove(2)
#num.pop(2)
print(num)
print(f'Essa lista tem {len(num)} elementos') """

# Exemplo 2
""" valores = []
valores.append(9)
valores.append(10)
valores.append(2)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v} !')
print('Cheguei ao final da lista.')    """

#Exemplo 3
valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v} !')
print('Cheguei ao final da lista.')

a = [2,3,4,7]
b = a[:] #Cria uma copia dos valores de A
print(f'Lista A: {a}')
print(f'Lista B: {b}')
