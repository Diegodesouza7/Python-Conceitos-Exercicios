""" Variaveis compostas """

# Exemplos

# Tuplas são imutaveis
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)
print(sorted(lanche))
print(lanche[1])
print(lanche[1:3])
print(lanche[2:])
print(lanche[-2])
print(lanche[-2:])
print(lanche[2:])
print(lanche[:2])

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
for c in enumerate(lanche):
    print(f'Eu vou comer {c}')
print('Comi pra caramba !!')

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')


a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(len(c))
print(c.count(5))
print(c.index(8))

pessoa = ('Diego', 27, 'M', 92.3)
print(pessoa)

print(c.count(5))