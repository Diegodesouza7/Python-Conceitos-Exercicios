""" Criar um programa que leia um numero
real qualquer pelo teclado e mostrar na tela
a sua porção inteira.
Ex: 8.127 parte inteira 8 """

from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))