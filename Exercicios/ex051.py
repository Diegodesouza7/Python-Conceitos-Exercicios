""" Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
     No final, mostre os 10 primeiros termos dessa progressão. """

pri = int(input('Primeiro termo: '))
ra = int(input('Razão: '))
décimo = pri + (10 - 1) * ra
for c in range(pri, décimo + ra, ra):
    print('{}'.format(c), end = '.')
print('Acabou')    
